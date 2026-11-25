# Windows Event Logs and Investigation

## Event Viewer

Open Event Viewer:

```cmd
eventvwr.msc
```

Common event log channels:

| Log | Purpose |
|---|---|
| Security | Authentication, account and audit events |
| System | Operating system and service events |
| Application | Application events |
| Setup | Windows installation and servicing |
| Microsoft-Windows-PowerShell/Operational | PowerShell operational events |
| Microsoft-Windows-Sysmon/Operational | Sysmon telemetry, if installed and configured |

## Get-WinEvent

```powershell
# List available logs
Get-WinEvent -ListLog *

# Recent Security events
Get-WinEvent -LogName Security -MaxEvents 20

# Recent System events
Get-WinEvent -LogName System -MaxEvents 20

# Filter by Event ID
Get-WinEvent -FilterHashtable @{
    LogName = "Security"
    Id = 4625
} -MaxEvents 50

# Filter by time
Get-WinEvent -FilterHashtable @{
    LogName = "Security"
    StartTime = (Get-Date).AddHours(-24)
}

# Filter by Event ID and time
Get-WinEvent -FilterHashtable @{
    LogName = "Security"
    Id = 4624, 4625
    StartTime = (Get-Date).AddDays(-1)
}
```

## Important Windows Event IDs

### Authentication and accounts

| Event ID | Description |
|---|---|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4634 | Logoff |
| 4647 | User-initiated logoff |
| 4648 | Logon using explicit credentials |
| 4672 | Special privileges assigned to new logon |
| 4720 | User account created |
| 4722 | User account enabled |
| 4723 | Attempt to change account password |
| 4724 | Attempt to reset account password |
| 4725 | User account disabled |
| 4726 | User account deleted |
| 4728 | Member added to security-enabled global group |
| 4732 | Member added to security-enabled local group |
| 4738 | User account changed |
| 4740 | User account locked out |

### Kerberos and NTLM

| Event ID | Description |
|---|---|
| 4768 | Kerberos TGT requested |
| 4769 | Kerberos service ticket requested |
| 4770 | Kerberos service ticket renewed |
| 4771 | Kerberos pre-authentication failed |
| 4776 | NTLM credential validation |

### System and services

| Event ID | Description |
|---|---|
| 4688 | Process creation |
| 4697 | Service installed in Security log |
| 7045 | Service installed in System log |
| 1102 | Security audit log cleared |
| 4719 | System audit policy changed |

### PowerShell

| Event ID | Description |
|---|---|
| 400 | PowerShell engine started |
| 403 | PowerShell engine stopped |
| 4103 | Module logging |
| 4104 | Script Block Logging |

PowerShell events depend on logging policy and configuration.

### Sysmon

| Event ID | Description |
|---|---|
| 1 | Process creation |
| 3 | Network connection |
| 5 | Process termination |
| 6 | Driver loaded |
| 7 | Image loaded |
| 8 | CreateRemoteThread |
| 10 | Process access |
| 11 | File creation |
| 12–14 | Registry events |
| 15 | File stream created |
| 22 | DNS query |
| 23, 26 | File deletion events |
| 25 | Process tampering |

Sysmon events are only available when Sysmon is installed and configured. Event generation depends on its configuration.

## Useful investigation queries

```powershell
# Failed logons in the last 24 hours
Get-WinEvent -FilterHashtable @{
    LogName = "Security"
    Id = 4625
    StartTime = (Get-Date).AddHours(-24)
}

# Successful logons in the last 24 hours
Get-WinEvent -FilterHashtable @{
    LogName = "Security"
    Id = 4624
    StartTime = (Get-Date).AddHours(-24)
}

# New user accounts
Get-WinEvent -FilterHashtable @{
    LogName = "Security"
    Id = 4720
    StartTime = (Get-Date).AddDays(-7)
}

# Service installation events
Get-WinEvent -FilterHashtable @{
    LogName = "System"
    Id = 7045
    StartTime = (Get-Date).AddDays(-7)
}

# Security log cleared
Get-WinEvent -FilterHashtable @{
    LogName = "Security"
    Id = 1102
}
```

## Export event logs

```powershell
# Export Security log
wevtutil epl Security C:\Temp\Security.evtx

# Export System log
wevtutil epl System C:\Temp\System.evtx

# Export PowerShell operational log
wevtutil epl Microsoft-Windows-PowerShell/Operational C:\Temp\PowerShell.evtx
```

## Investigation considerations

- Record the system's timezone and clock status.
- Preserve original EVTX files.
- Record relevant event IDs and timestamps.
- Correlate events across multiple logs.
- Identify account, host, source address and logon type.
- Consider missing or incomplete telemetry.
- Check whether audit policies were enabled.
- Avoid assuming an event alone proves malicious activity.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
