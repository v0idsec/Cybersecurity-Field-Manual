# Windows Services and Scheduled Tasks

A reference for assessing Windows services, service permissions, executable paths, scheduled tasks and automated execution mechanisms.

Services and scheduled tasks frequently operate with elevated privileges. Incorrect permissions or unsafe execution paths can expose local privilege escalation opportunities.

## 1. Windows Services Overview

Windows services are background processes managed by the Service Control Manager (SCM).

A service can run under identities such as:

- LocalSystem.
- LocalService.
- NetworkService.
- Local user accounts.
- Domain service accounts.
- Group Managed Service Accounts (gMSAs).

The security impact of a service weakness depends on its execution identity, configuration permissions and the resources it can access.

## 2. Service Enumeration

### 2.1 List Services

```powershell
Get-Service

Get-Service |
    Where-Object Status -eq 'Running'
```

### 2.2 Detailed Service Information

```powershell
Get-CimInstance Win32_Service |
    Select-Object Name, DisplayName, State, StartMode, StartName, PathName
```

### 2.3 Command Prompt

```cmd
sc query
sc query type= service state= all
sc qc <service_name>
```

Record:

- Service name.
- Display name.
- Description.
- Executable path.
- Startup type.
- Execution account.
- Current state.
- Dependencies.
- Recovery configuration.

## 3. Service Configuration Assessment

Inspect:

- Automatic versus manual startup.
- Disabled services.
- Services running under privileged accounts.
- Unexpected service binaries.
- Unnecessary services.
- Service dependencies.
- Recovery actions.
- Failure handling.
- Service account privileges.

### 3.1 Service Configuration

```cmd
sc qc <service_name>
```

### 3.2 Service Security Descriptor

```cmd
sc sdshow <service_name>
```

Service security descriptors determine which principals can query, start, stop, modify or delete a service.

Interpret access control entries carefully. The presence of a permission in an SDDL string does not automatically mean the current account can exploit it.

## 4. Service Permissions

Assess whether unprivileged users can:

- Modify service configuration.
- Change the executable path.
- Change the service account.
- Start or stop sensitive services.
- Delete a service.
- Modify service-related registry keys.

Use:

- AccessChk.
- PowerShell ACL inspection.
- `sc sdshow`.
- Security descriptor analysis.

Example:

```cmd
accesschk.exe -c <service_name>
```

Review the permissions granted to:

- Everyone.
- Authenticated Users.
- Users.
- Interactive.
- Custom application groups.

Do not modify service permissions on production systems without explicit approval.

## 5. Unquoted Service Paths

An unquoted executable path containing spaces can create ambiguity in executable resolution.

Example:

```text
C:\Program Files\Example Application\Service Host\service.exe
```

Assess:

1. Does the path contain spaces?
2. Is the executable path quoted?
3. Which directories are involved in resolution?
4. Can an unprivileged user write to any relevant directory?
5. Does the service run with elevated privileges?
6. Is the relevant executable resolution behaviour applicable to the operating system?

A service path being unquoted is not sufficient evidence by itself. Validate the complete set of conditions.

## 6. Writable Service Binaries and Directories

Identify the executable path:

```powershell
Get-CimInstance Win32_Service |
    Select-Object Name, StartName, PathName
```

Inspect permissions:

```cmd
icacls "C:\Program Files\Example Application"
icacls "C:\Program Files\Example Application\service.exe"
```

Assess whether the current account can modify:

- The executable.
- Parent directories.
- Configuration files.
- DLLs loaded by the service.
- Scripts invoked by the service.
- Update mechanisms.

A writable directory is particularly important when a privileged service trusts files stored within it.

## 7. Service DLL and Dependency Assessment

Review:

- DLL search paths.
- Application directory permissions.
- Dependency locations.
- Service working directories.
- Side-by-side assembly configuration.
- Configuration-controlled library loading.

Potential weaknesses include unsafe DLL search order and writable dependency locations.

Validate in a dedicated test environment wherever possible.

## 8. Service Accounts

Identify service identities:

```powershell
Get-CimInstance Win32_Service |
    Select-Object Name, StartName, State
```

Assess:

- Excessive local privileges.
- Unnecessary administrative membership.
- Interactive logon rights.
- Password management.
- Shared service identities.
- Account lifecycle management.
- Credential exposure.
- Network access requirements.

Prefer dedicated, least-privileged service identities.

## 9. Scheduled Task Enumeration

### 9.1 List Tasks

```powershell
Get-ScheduledTask
```

### 9.2 Task Details

```powershell
Get-ScheduledTask |
    Select-Object TaskName, TaskPath, State
```

### 9.3 Task Actions and Principals

```powershell
Get-ScheduledTask | ForEach-Object {
    [PSCustomObject]@{
        TaskName = $_.TaskName
        TaskPath = $_.TaskPath
        User     = $_.Principal.UserId
        RunLevel = $_.Principal.RunLevel
        Actions  = ($_.Actions | ForEach-Object {
            "$($_.Execute) $($_.Arguments)"
        }) -join '; '
    }
}
```

### 9.4 Command Prompt

```cmd
schtasks /query /fo LIST /v
```

Review:

- Task name.
- Trigger.
- Execution account.
- Run level.
- Executable.
- Arguments.
- Working directory.
- Task permissions.
- Last and next run times.
- Execution history.

## 10. Scheduled Task Security Assessment

Investigate whether:

- Standard users can modify privileged tasks.
- Task scripts are writable.
- Executables are stored in writable directories.
- Arguments contain sensitive information.
- Tasks execute with unnecessary privileges.
- Tasks reference missing or unsafe paths.
- Task permissions are broader than required.

A privileged task referencing a user-writable script can create a privilege escalation path.

Do not alter task actions or triggers on production systems as part of routine validation.

## 11. Startup and Automatic Execution

Review legitimate automatic execution locations:

- Service startup configuration.
- Scheduled tasks.
- Startup folders.
- Approved logon scripts.
- Application update mechanisms.
- Software deployment systems.

Assess whether each mechanism is authorised, appropriately permissioned and monitored.

See `windows-persistence-and-access.md` for broader persistence auditing.

## 12. Event Logging

Relevant event sources include:

| Event ID | Description |
|---|---|
| 4697 | Service installed |
| 7045 | New service installed |
| 7034 | Service terminated unexpectedly |
| 7036 | Service entered a state |
| 4698 | Scheduled task created |
| 4699 | Scheduled task deleted |
| 4700 | Scheduled task enabled |
| 4701 | Scheduled task disabled |
| 4702 | Scheduled task updated |

Event availability depends on audit policy, operating system version and logging configuration.

## 13. Reporting

Document:

- Service or task name.
- Executable or script path.
- Execution identity.
- Relevant permissions.
- Configuration weakness.
- Preconditions.
- Validation evidence.
- Potential impact.
- Recommended remediation.

## 14. Remediation

Recommended controls:

- Restrict service configuration permissions.
- Protect executable and dependency directories.
- Quote service executable paths.
- Use least-privileged service accounts.
- Restrict scheduled task modification.
- Protect task scripts and referenced files.
- Remove unnecessary services and tasks.
- Monitor service and task changes.
- Review service account credentials.
- Audit privileged automatic execution.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
