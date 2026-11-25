# Windows Privilege Escalation

A methodology for identifying and validating local Windows privilege escalation weaknesses.

The focus is on understanding security boundaries, identifying misconfigurations and demonstrating impact through controlled assessment.

This guide does not replace the detailed references for services, ACLs, credentials and scheduled tasks.

## 1. Privilege Escalation Methodology

A local privilege escalation assessment should follow a repeatable process:

1. Identify the current account and token.
2. Determine the host's operating system and security configuration.
3. Enumerate local groups and privileges.
4. Review filesystem and registry permissions.
5. Inspect services and scheduled tasks.
6. Review installed software and exposed components.
7. Assess credential handling and stored secrets.
8. Identify potential escalation paths.
9. Validate the weakest link using a controlled proof.
10. Document impact and remediation.

## 2. Establish the Current Context

```cmd
whoami
whoami /all
hostname
systeminfo
```

Determine:

- Current identity.
- Integrity level.
- Local group memberships.
- Enabled privileges.
- Operating system build.
- Architecture.
- Whether the session is elevated.
- Whether the account is local or domain-based.

Do not confuse membership of Administrators with an elevated process token.

## 3. Common Privilege Escalation Categories

| Category | Typical Weakness |
|---|---|
| Service permissions | Unprivileged users can modify privileged service configuration |
| Writable service binaries | Privileged service executes a user-writable binary |
| Unquoted service paths | Executable path parsing creates an unsafe resolution opportunity |
| Scheduled tasks | Privileged tasks reference modifiable files or scripts |
| Filesystem ACLs | Sensitive executables or configuration files are writable |
| Registry permissions | Privileged execution configuration is modifiable |
| Credential exposure | Privileged credentials are exposed in files or configuration |
| Excessive privileges | Dangerous token privileges are assigned unnecessarily |
| Vulnerable software | An installed component has an applicable security vulnerability |
| Misconfigured installers | Installer or update mechanisms provide unintended elevation |
| DLL search order | A privileged application loads a library from an unsafe location |
| Service account configuration | A service runs with excessive privileges or unsafe permissions |

## 4. Service-Based Escalation Assessment

Enumerate services:

```powershell
Get-CimInstance Win32_Service |
    Select-Object Name, StartName, State, StartMode, PathName
```

Review:

- Service executable path.
- Service account.
- Start permissions.
- Configuration permissions.
- Binary and directory permissions.
- Service dependencies.
- Recovery actions.
- Whether the service is automatically started.

Use AccessChk or ACL inspection to establish whether the current account can modify a privileged service or its executable.

Do not modify or replace production service binaries to prove a suspected issue without explicit approval.

See `services-and-scheduled-tasks.md`.

## 5. Unquoted Service Paths

An unquoted service path containing spaces can create executable resolution risks.

Example of a potentially unsafe configuration:

```text
C:\Program Files\Example Application\Service Host\service.exe
```

Assess:

- Whether the path contains spaces.
- Whether it is quoted.
- Whether relevant parent directories are writable.
- Whether the service executes with elevated privileges.
- Whether the operating system's executable resolution behaviour makes the issue exploitable.

A path being unquoted does not automatically establish a vulnerability. The relevant write permissions and execution conditions must also be demonstrated.

## 6. Scheduled Task Assessment

Enumerate tasks:

```powershell
Get-ScheduledTask

Get-ScheduledTask |
    Select-Object TaskName, TaskPath, State
```

Review task actions and principals:

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

Look for:

- Elevated tasks.
- User-writable scripts.
- Writable executable directories.
- Unsafe task permissions.
- Sensitive arguments.
- Unnecessary privileged execution.

Do not alter task triggers or actions on production systems without approval.

## 7. Filesystem Permissions

Review permissions on:

- Service binaries.
- Application directories.
- Startup locations.
- Script directories.
- Update locations.
- Sensitive configuration files.
- Executable search paths.

Example:

```cmd
icacls "C:\Program Files\Example"
```

PowerShell:

```powershell
Get-Acl 'C:\Program Files\Example' |
    Format-List Owner, AccessToString
```

Assess whether an unprivileged account can modify an object that a privileged process later executes or trusts.

See `windows-registry-and-acls.md`.

## 8. Registry Permissions

Review registry keys associated with:

- Services.
- Startup configuration.
- Application execution.
- Installer behaviour.
- Security settings.
- Scheduled tasks.

Example:

```powershell
Get-Acl 'HKLM:\SYSTEM\CurrentControlSet\Services'
```

Assess whether a standard user can modify configuration consumed by a privileged process.

Avoid changing registry values during assessment unless the change is explicitly approved.

## 9. Credential-Related Escalation

Potential exposure locations include:

- Application configuration.
- Deployment scripts.
- Scheduled task arguments.
- Service configuration.
- Installer configuration.
- Unattended installation artefacts.
- Backup files.
- Administrative tooling.
- Scripts and automation.

Assess whether credentials are:

- Stored in plaintext.
- Embedded in scripts.
- Exposed through inappropriate permissions.
- Shared between users or services.
- Stored in insecure locations.
- Protected by appropriate Windows security mechanisms.

Do not dump credentials or access unrelated user secrets merely to demonstrate exposure.

See `windows-credentials-and-secrets.md`.

## 10. Token Privilege Assessment

```cmd
whoami /priv
```

Investigate relevant privileges such as:

- SeImpersonatePrivilege.
- SeAssignPrimaryTokenPrivilege.
- SeDebugPrivilege.
- SeBackupPrivilege.
- SeRestorePrivilege.
- SeTakeOwnershipPrivilege.
- SeLoadDriverPrivilege.

The presence of a privilege alone does not prove a viable escalation path.

Validate the effective token, operating system protections, process context and applicable prerequisites.

## 11. Vulnerable Software and Missing Patches

Inventory installed software and patch state.

```powershell
Get-HotFix | Sort-Object InstalledOn -Descending

Get-CimInstance Win32_Product |
    Select-Object Name, Version
```

Avoid using `Win32_Product` for routine inventory where possible. Querying it can trigger Windows Installer consistency checks and may be disruptive.

Prefer uninstall registry inventory and approved asset management sources.

For each suspected vulnerability:

1. Identify the exact component and version.
2. Confirm applicability.
3. Review vendor advisories.
4. Determine whether a security update is missing.
5. Identify required local access.
6. Validate using a safe proof where possible.

## 12. Automated Enumeration

Useful tools include:

| Tool | Purpose |
|---|---|
| WinPEAS | Windows privilege escalation enumeration |
| Seatbelt | Windows host security and configuration enumeration |
| AccessChk | Effective permissions and access checks |
| PowerUp | PowerShell-based privilege escalation checks |
| PrivescCheck | Windows privilege escalation assessment |
| Process Explorer | Process and security context inspection |
| Autoruns | Startup and persistence enumeration |
| Sysmon | Process and system activity telemetry |

Automated output should be treated as leads, not confirmed findings.

For every result:

- Verify the affected object.
- Confirm effective permissions.
- Check whether the condition is exploitable.
- Determine the actual security impact.
- Record false positives and limitations.

## 13. Controlled Validation

Use the least intrusive validation possible.

Preferred validation order:

1. Configuration inspection.
2. Permission inspection.
3. Controlled execution in a lab.
4. Approved test-file or test-service validation.
5. Minimal proof of privilege boundary crossing.

Avoid:

- Replacing production binaries.
- Disabling security controls.
- Modifying privileged scheduled tasks.
- Dumping credentials.
- Installing unauthorised services.
- Establishing persistence.
- Restarting business-critical services.

## 14. Reporting

A privilege escalation finding should include:

- Hostname and operating system.
- Initial user context.
- Target privilege level.
- Affected service, task, file or registry key.
- Exact permission or configuration weakness.
- Preconditions.
- Validation evidence.
- Demonstrated impact.
- Remediation.

Clearly distinguish between:

- A theoretical attack path.
- A misconfiguration.
- A validated privilege escalation.
- A successful proof of impact.

## 15. Remediation Themes

Common corrective actions include:

- Restrict service configuration permissions.
- Protect service binaries and directories.
- Quote service executable paths.
- Restrict scheduled task modification.
- Apply least privilege to service accounts.
- Correct filesystem and registry ACLs.
- Remove exposed credentials.
- Patch vulnerable components.
- Restrict dangerous token privileges.
- Monitor privileged execution and configuration changes.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
