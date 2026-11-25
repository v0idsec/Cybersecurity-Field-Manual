# Windows Forensics

## Overview

Windows systems generate a wide range of forensic artefacts that can help reconstruct user activity, process execution, authentication, persistence and system changes.

Important evidence sources include:

- Windows Event Logs
- Registry hives
- Prefetch
- Amcache
- Shimcache
- Windows Defender records
- PowerShell logs
- Scheduled tasks
- Services
- NTFS metadata
- Browser artefacts
- Volume Shadow Copies

## Windows Event Logs

Event Logs are stored in EVTX format.

Common log locations:

```text
C:\Windows\System32\winevt\Logs\
```

Important channels include:

- Security
- System
- Application
- Microsoft-Windows-PowerShell/Operational
- Microsoft-Windows-Sysmon/Operational
- Microsoft-Windows-Windows Defender/Operational

Availability depends on system configuration, retention and logging policy.

## Important Windows Event IDs

| Event ID | Description |
|---|---|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4634 | Logoff |
| 4648 | Logon using explicit credentials |
| 4672 | Special privileges assigned |
| 4688 | Process creation |
| 4697 | Service installed in Security log |
| 4720 | User account created |
| 4722 | User account enabled |
| 4728 | Member added to security-enabled global group |
| 4732 | Member added to security-enabled local group |
| 4740 | User account locked out |
| 4768 | Kerberos authentication ticket requested |
| 4769 | Kerberos service ticket requested |
| 4771 | Kerberos pre-authentication failed |
| 7045 | Service installed in System log |

Event IDs alone are not enough. Review the event fields, source host, account, timestamp and surrounding activity.

## PowerShell Logging

PowerShell Script Block Logging commonly records Event ID 4104 in:

```text
Microsoft-Windows-PowerShell/Operational
```

Example:

```powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'Microsoft-Windows-PowerShell/Operational'
    Id = 4104
} | Select-Object TimeCreated, Id, Message
```

Logging may not be enabled or retained.

## Sysmon

Sysmon provides additional endpoint telemetry when configured.

Useful Event IDs include:

| Event ID | Activity |
|---|---|
| 1 | Process creation |
| 3 | Network connection |
| 5 | Process termination |
| 6 | Driver loaded |
| 7 | Image loaded |
| 8 | CreateRemoteThread |
| 10 | Process access |
| 11 | File created |
| 12 | Registry object created or deleted |
| 13 | Registry value set |
| 14 | Registry object renamed |
| 15 | File stream created |
| 22 | DNS query |
| 23 | File deletion archived |
| 25 | Process tampering |
| 26 | File deletion detected |

Sysmon event coverage depends on the installed version and configuration.

## Registry Forensics

Important registry hives include:

```text
C:\Windows\System32\config\
```

Common hives:

- SYSTEM
- SOFTWARE
- SAM
- SECURITY
- DEFAULT

User-specific hives:

```text
C:\Users\<user>\NTUSER.DAT
```

Potential evidence:
- Installed applications
- User activity
- Startup configuration
- Services
- Device history
- Network configuration
- Persistence mechanisms

Registry analysis should consider transaction logs and available backups.

## Prefetch

Typical location:

```text
C:\Windows\Prefetch\
```

Prefetch artefacts can provide information about application execution.

They may contain:
- Executable names
- Execution-related metadata
- Referenced files
- Run information

Prefetch behaviour varies by Windows version and configuration.

Do not treat Prefetch as a complete execution log.

## Amcache

Amcache can provide information about application compatibility and executable artefacts.

It may help identify:
- Executable paths
- File metadata
- Application information
- Hash-related values

Interpretation depends on Windows version and artefact context.

## Shimcache

AppCompatCache, commonly called Shimcache, records compatibility-related information.

It may provide useful file metadata and path information.

A Shimcache entry does not independently prove that a program executed.

## Scheduled Tasks

Review scheduled tasks for suspicious persistence.

```powershell
Get-ScheduledTask |
    Select-Object TaskName, TaskPath, State
```

Inspect task details:

```powershell
Get-ScheduledTask |
    ForEach-Object {
        $_ | Select-Object TaskName, TaskPath, State,
            @{Name='Actions';Expression={$_.Actions.Execute}}
    }
```

Investigate:
- Unexpected task names
- Unusual execution paths
- Encoded commands
- Unexpected service accounts
- Suspicious triggers

## Services

Enumerate services:

```powershell
Get-CimInstance Win32_Service |
    Select-Object Name, DisplayName, State, StartMode, PathName
```

Investigate unexpected services and executable paths.

Correlate with:
- Event ID 7045
- Event ID 4697
- File creation timestamps
- Process execution telemetry

## Windows Defender

Review Defender operational events:

```powershell
Get-WinEvent -LogName 'Microsoft-Windows-Windows Defender/Operational' |
    Select-Object TimeCreated, Id, Message
```

Look for:
- Threat detections
- Quarantine events
- Configuration changes
- Protection exclusions
- Real-time protection changes

## NTFS Artefacts

Relevant structures:
- MFT
- USN Journal
- `$LogFile`
- Alternate Data Streams
- Volume Shadow Copies
- Recycle Bin

See [Disk Forensics](disk-forensics.md).

## Investigation Workflow

1. Preserve relevant disk and memory evidence.
2. Export relevant event logs.
3. Review authentication events.
4. Examine process creation.
5. Review PowerShell and Sysmon activity.
6. Inspect registry persistence locations.
7. Examine Prefetch and Amcache.
8. Review scheduled tasks and services.
9. Examine suspicious files.
10. Correlate timestamps and external telemetry.
11. Document conclusions and limitations.

## Common Mistakes

- Assuming all event logging is enabled.
- Treating Shimcache as proof of execution.
- Ignoring event-log retention.
- Failing to correlate process creation with network activity.
- Ignoring registry transaction logs.
- Assuming an absent artefact proves an action never occurred.
- Treating a single event as conclusive evidence.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
