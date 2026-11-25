# Windows User and Group Enumeration

A reference for assessing local Windows identities, group memberships, account configuration, privileges, logon sessions and security token context.

This guide focuses on local host security. Domain identity and Active Directory relationships are covered in the Active Directory section.

## 1. Current Security Context

```powershell
whoami

whoami /user

whoami /groups

whoami /priv

whoami /all
```

Review:

- Account SID.
- Group SIDs.
- Enabled and deny-only groups.
- Integrity level.
- Enabled privileges.
- Restricted token attributes.
- Logon session context.

### 1.1 Integrity Levels

Common integrity levels include:

| Level | Typical Context |
|---|---|
| Untrusted | Highly restricted processes |
| Low | Sandboxed or restricted applications |
| Medium | Standard interactive user |
| High | Elevated administrator process |
| System | LocalSystem context |
| Protected Process | Special protected execution contexts |

An account belonging to the local Administrators group does not necessarily mean its current process is elevated.

## 2. Local User Enumeration

### 2.1 Command Prompt

```cmd
net user
net user <username>
```

### 2.2 PowerShell

```powershell
Get-LocalUser

Get-LocalUser |
    Select-Object Name, Enabled, LastLogon, PasswordRequired, PasswordExpires, SID
```

### 2.3 Account Review

Assess:

- Enabled and disabled accounts.
- Unused accounts.
- Unexpected local administrators.
- Shared accounts.
- Guest account status.
- Password policy.
- Account expiry.
- Last logon information.
- Service-associated accounts.

Do not interpret an old or missing last-logon timestamp as definitive proof that an account is unused.

## 3. Local Group Enumeration

```powershell
Get-LocalGroup

Get-LocalGroupMember -Group Administrators

Get-LocalGroupMember -Group Users

Get-LocalGroupMember -Group 'Remote Desktop Users'
```

Command Prompt alternative:

```cmd
net localgroup
net localgroup Administrators
net localgroup "Remote Desktop Users"
```

Important groups may include:

- Administrators.
- Users.
- Guests.
- Remote Desktop Users.
- Remote Management Users.
- Backup Operators.
- Hyper-V Administrators.
- Event Log Readers.
- Performance Log Users.
- Distributed COM Users.

Group membership should be assessed according to the actual privileges and access paths it provides.

## 4. Privilege Enumeration

```cmd
whoami /priv
```

Potentially significant privileges include:

| Privilege | Security Relevance |
|---|---|
| SeDebugPrivilege | Can permit debugging access to other processes |
| SeImpersonatePrivilege | Can enable token impersonation in certain contexts |
| SeAssignPrimaryTokenPrivilege | Allows assignment of primary tokens |
| SeBackupPrivilege | Can bypass some file access checks for backup operations |
| SeRestorePrivilege | Can bypass some file access checks for restore operations |
| SeTakeOwnershipPrivilege | Allows taking ownership of securable objects |
| SeLoadDriverPrivilege | Allows loading device drivers |
| SeTcbPrivilege | Highly privileged trusted-computing-base operations |
| SeManageVolumePrivilege | Allows management of volume-level operations |

A listed privilege is not necessarily enabled or usable in the current context.

Validate:

- Whether the privilege is enabled.
- Whether the process token can exercise it.
- Whether the relevant operating system protections apply.
- Whether the proposed technique is permitted by the engagement.

## 5. Sessions and Logon Information

### 5.1 Current Sessions

```cmd
query user

qwinsta

quser
```

### 5.2 Logged-On Users

```powershell
Get-CimInstance Win32_LoggedOnUser
```

This can return extensive information. Filter and handle results carefully.

### 5.3 Local and Remote Sessions

```cmd
net session
```

This command generally requires elevated privileges to retrieve complete server session information.

### 5.4 Process Ownership

```powershell
Get-CimInstance Win32_Process |
    ForEach-Object {
        $owner = Invoke-CimMethod -InputObject $_ -MethodName GetOwner

        [PSCustomObject]@{
            ProcessId = $_.ProcessId
            Name      = $_.Name
            User      = "$($owner.Domain)\$($owner.User)"
            Path      = $_.ExecutablePath
        }
    }
```

Use this selectively on large systems because process enumeration can be noisy and resource-intensive.

## 6. Security Token Assessment

Windows access decisions are based on security tokens and access checks.

Review:

- User SID.
- Enabled group SIDs.
- Deny-only group SIDs.
- Privileges.
- Integrity level.
- Restricted SIDs.
- Token elevation type.
- Impersonation level.

Useful tools:

- `whoami`.
- Sysinternals AccessChk.
- Process Explorer.
- Windows Security Event Logs.
- PowerShell security-related APIs.

## 7. Local Administrator Assessment

Identify:

- Members of the local Administrators group.
- Unexpected administrative accounts.
- Shared administrator credentials.
- Administrative accounts used for routine work.
- Stale accounts retaining administrative privileges.
- Remote administration exposure.

Review local account management policy and whether Windows LAPS is deployed where appropriate.

Do not attempt password recovery or credential extraction merely to confirm administrative membership.

## 8. Service Account Assessment

Identify service identities:

```powershell
Get-CimInstance Win32_Service |
    Select-Object Name, StartName, State, StartMode
```

Assess:

- Whether built-in service identities are used appropriately.
- Whether dedicated service accounts are overprivileged.
- Whether accounts have interactive logon rights unnecessarily.
- Whether credentials are rotated.
- Whether service accounts are shared.
- Whether service accounts have unnecessary local group membership.

## 9. Account Policy Review

```cmd
net accounts
```

Review local policy:

- Password length requirements.
- Password history.
- Account lockout threshold.
- Lockout duration.
- Lockout counter reset.
- Guest access.
- Password expiry requirements, where applicable.

Modern password policy should be assessed against organisational standards and current identity security guidance rather than relying on arbitrary complexity rules alone.

## 10. Remote Access Groups

```powershell
Get-LocalGroupMember -Group 'Remote Desktop Users'

Get-LocalGroupMember -Group 'Remote Management Users'
```

Assess:

- Whether remote access is necessary.
- Whether membership is restricted.
- Whether MFA or equivalent access protections apply.
- Whether access is limited by network controls.
- Whether access is logged.
- Whether inactive access is removed.

## 11. Finding Indicators

Potential findings include:

- Unauthorised local administrators.
- Excessive group membership.
- Unnecessary privileged service accounts.
- Stale accounts with access.
- Unrestricted remote access.
- Administrative accounts used for routine tasks.
- Excessive token privileges.
- Inadequate account lifecycle management.

## 12. Evidence and Reporting

For each finding, capture:

- Hostname.
- Account or group.
- Relevant SID where useful.
- Effective privilege or access.
- Evidence source.
- Business or technical impact.
- Remediation recommendation.

Redact personal information and avoid collecting password material.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
