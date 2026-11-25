# Windows Event Logging

## Overview

Windows Event Logging provides visibility into authentication, process execution, account management, system changes and security-related activity.

Security analysts commonly use Windows Security logs, Sysmon and PowerShell logging to investigate suspicious behaviour.

## Windows Event Log Channels

| Channel | Purpose |
|---|---|
| Security | Authentication, account and audit events |
| System | Operating system and service events |
| Application | Application-generated events |
| Microsoft-Windows-PowerShell/Operational | PowerShell activity |
| Microsoft-Windows-Sysmon/Operational | Detailed system telemetry |
| Microsoft-Windows-Windows Defender/Operational | Defender activity |
| Microsoft-Windows-TaskScheduler/Operational | Scheduled task activity |

## Important Windows Security Event IDs

### Authentication

| Event ID | Description |
|---|---|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4634 | Account logoff |
| 4647 | User-initiated logoff |
| 4648 | Logon using explicit credentials |
| 4672 | Special privileges assigned to new logon |
| 4768 | Kerberos TGT requested |
| 4769 | Kerberos service ticket requested |
| 4771 | Kerberos pre-authentication failed |
| 4776 | NTLM credential validation |

### Account and Group Management

| Event ID | Description |
|---|---|
| 4720 | User account created |
| 4722 | User account enabled |
| 4723 | Password change attempted |
| 4724 | Password reset attempted |
| 4725 | User account disabled |
| 4726 | User account deleted |
| 4728 | Member added to global security group |
| 4729 | Member removed from global security group |
| 4732 | Member added to local security group |
| 4733 | Member removed from local security group |
| 4738 | User account changed |
| 4740 | User account locked out |

### System and Process Activity

| Event ID | Description |
|---|---|
| 4697 | Service installed |
| 4698 | Scheduled task created |
| 4699 | Scheduled task deleted |
| 4702 | Scheduled task updated |
| 4719 | System audit policy changed |
| 1102 | Security audit log cleared |
| 7045 | New service installed (System log) |

### Important Interpretation Notes

Event IDs are contextual.

For example:

- 4624 does not automatically indicate legitimate access.
- 4672 is common for administrative accounts and is not independently suspicious.
- 4769 requires contextual analysis before being treated as Kerberoasting activity.
- 1102 may indicate log tampering, but should be correlated with administrative activity.

## Sysmon

Sysmon provides detailed system telemetry beyond standard Windows auditing.

Important Sysmon Event IDs:

| Event ID | Description |
|---|---|
| 1 | Process creation |
| 2 | File creation time changed |
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
| 15 | File stream hash |
| 22 | DNS query |
| 23 | File deletion |
| 25 | Process tampering |
| 26 | File deletion detected |

Sysmon event coverage depends on the deployed configuration.

A missing event does not necessarily mean the activity did not occur.

## PowerShell Logging

Useful PowerShell logging sources include:

- Script Block Logging
- Module Logging
- Transcription
- PowerShell Operational logs

Script Block Logging commonly records Event ID 4104.

PowerShell telemetry can help identify:

- Encoded commands
- Suspicious downloads
- Unusual script execution
- Credential access behaviour
- Execution from temporary directories
- Unexpected administrative activity

Encoded PowerShell is not inherently malicious. Investigate context and decoded content safely.

## Querying Windows Events

### PowerShell: Recent Failed Logons

```powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'Security'
    Id = 4625
    StartTime = (Get-Date).AddHours(-24)
} | Select-Object TimeCreated, Id, Message
```

### PowerShell: Recent Successful Logons

```powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'Security'
    Id = 4624
    StartTime = (Get-Date).AddHours(-24)
} | Select-Object TimeCreated, Id, Message
```

### PowerShell: Service Installation Events

```powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'System'
    Id = 7045
    StartTime = (Get-Date).AddDays(-7)
}
```

### PowerShell: Sysmon Process Creation

```powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'Microsoft-Windows-Sysmon/Operational'
    Id = 1
    StartTime = (Get-Date).AddHours(-24)
}
```

## Logging Configuration Considerations

Review:

- Advanced Audit Policy Configuration
- Process creation auditing
- Command-line process auditing
- PowerShell Script Block Logging
- PowerShell Module Logging
- Sysmon configuration
- Windows Defender logging
- Event log size and retention
- Event forwarding configuration

## Investigation Considerations

When analysing Windows events, capture:

- Event timestamp
- Hostname
- User and logon ID
- Source address
- Process ID
- Parent process
- Command line
- Event record ID
- Related events

Correlate events across multiple channels rather than relying on one Event ID.

## Further Reading

- Windows Security Auditing: https://learn.microsoft.com/windows/security/threat-protection/auditing/
- Sysmon: https://learn.microsoft.com/sysinternals/downloads/sysmon
- Windows Event Reference: https://learn.microsoft.com/windows/security/threat-protection/auditing/basic-audit-logon-events

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
