# SIEM & EDR Tool Reference

## Overview

A practical reference for common SIEM, EDR and endpoint investigation tools, commands and query patterns.

Commands and queries should be validated against the deployed product version, permissions and logging configuration.

---

## Windows Event Logging

### Query Failed Logons

```powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'Security'
    Id = 4625
    StartTime = (Get-Date).AddHours(-24)
}
```

### Query Successful Logons

```powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'Security'
    Id = 4624
    StartTime = (Get-Date).AddHours(-24)
}
```

### Query Privileged Logons

```powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'Security'
    Id = 4672
    StartTime = (Get-Date).AddHours(-24)
}
```

### Query New Services

```powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'System'
    Id = 7045
    StartTime = (Get-Date).AddDays(-7)
}
```

### Query PowerShell Script Block Logging

```powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'Microsoft-Windows-PowerShell/Operational'
    Id = 4104
    StartTime = (Get-Date).AddHours(-24)
}
```

### Query Sysmon Process Creation

```powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'Microsoft-Windows-Sysmon/Operational'
    Id = 1
    StartTime = (Get-Date).AddHours(-24)
}
```

---

## Windows Endpoint Investigation

### Running Processes

```powershell
Get-Process
```

### Process Command Lines

```powershell
Get-CimInstance Win32_Process |
    Select-Object ProcessId, ParentProcessId, Name, ExecutablePath, CommandLine
```

### Active Network Connections

```powershell
Get-NetTCPConnection
```

### Listening Ports

```powershell
Get-NetTCPConnection -State Listen
```

### Scheduled Tasks

```powershell
Get-ScheduledTask
```

### Services

```powershell
Get-CimInstance Win32_Service |
    Select-Object Name, State, StartMode, PathName
```

### File Hash

```powershell
Get-FileHash -Algorithm SHA256 "C:\Path\file.exe"
```

---

## Linux Investigation

### Authentication Events

```bash
grep -i "failed password" /var/log/auth.log
```

### Recent Authentication Activity

```bash
journalctl -u ssh --since "24 hours ago"
```

### Active Network Connections

```bash
ss -plant
```

### Running Processes

```bash
ps auxf
```

### Scheduled Tasks

```bash
crontab -l
```

### systemd Services

```bash
systemctl list-units --type=service
```

### File Hash

```bash
sha256sum /path/to/file
```

### Audit Events

```bash
ausearch -ts today
```

---

## Microsoft Sentinel — KQL

### Failed Logons

```kql
SecurityEvent
| where TimeGenerated > ago(24h)
| where EventID == 4625
| summarize Attempts = count() by TargetUserName, IpAddress
| order by Attempts desc
```

### Successful Logons

```kql
SecurityEvent
| where TimeGenerated > ago(24h)
| where EventID == 4624
| project TimeGenerated, Computer, TargetUserName, IpAddress, LogonType
| order by TimeGenerated desc
```

### Entra ID Failed Sign-ins

```kql
SigninLogs
| where TimeGenerated > ago(24h)
| where ResultType != "0"
| summarize
    FailedAttempts = count(),
    Applications = make_set(AppDisplayName)
    by UserPrincipalName, IPAddress
| order by FailedAttempts desc
```

### New Service Installation

```kql
SecurityEvent
| where TimeGenerated > ago(7d)
| where EventID == 4697
| project TimeGenerated, Computer, SubjectUserName, ServiceName
| order by TimeGenerated desc
```

### PowerShell Script Block Activity

```kql
WindowsEvent
| where TimeGenerated > ago(24h)
| where EventID == 4104
| project TimeGenerated, Computer, EventData
| order by TimeGenerated desc
```

Table names and fields depend on the connected data sources and ingestion configuration.

---

## Splunk — SPL

### Failed Logons

```spl
index=windows EventCode=4625
| stats count by user, src, host
| sort - count
```

### Successful Logons

```spl
index=windows EventCode=4624
| table _time, host, user, src, Logon_Type
| sort - _time
```

### Process Creation

```spl
index=windows EventCode=4688
| table _time, host, user, New_Process_Name, Creator_Process_Name
| sort - _time
```

### PowerShell Activity

```spl
index=windows EventCode=4104
| table _time, host, user, ScriptBlockText
| sort - _time
```

Field names and indexes depend on the deployed Splunk configuration and data model.

---

## Common Windows Event IDs

| Event ID | Description |
|---|---|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4634 | Logoff |
| 4648 | Explicit credentials used |
| 4672 | Special privileges assigned |
| 4688 | Process creation |
| 4697 | Service installed |
| 4698 | Scheduled task created |
| 4720 | User account created |
| 4728 | Added to global security group |
| 4732 | Added to local security group |
| 4740 | Account locked out |
| 4768 | Kerberos TGT requested |
| 4769 | Kerberos service ticket requested |
| 4771 | Kerberos pre-authentication failed |
| 1102 | Security audit log cleared |

## Common Sysmon Event IDs

| Event ID | Description |
|---|---|
| 1 | Process creation |
| 3 | Network connection |
| 5 | Process termination |
| 6 | Driver loaded |
| 7 | Image loaded |
| 8 | CreateRemoteThread |
| 10 | Process access |
| 11 | File created |
| 12–14 | Registry activity |
| 15 | File stream hash |
| 22 | DNS query |
| 23 | File deletion |
| 25 | Process tampering |
| 26 | File deletion detected |

Sysmon events depend on the deployed configuration.

---

## Common SIEM and EDR Tools

| Tool | Purpose |
|---|---|
| Microsoft Sentinel | Cloud SIEM and security analytics |
| Microsoft Defender for Endpoint | Endpoint detection and response |
| Splunk Enterprise Security | SIEM and security operations |
| Elastic Security | SIEM and endpoint security |
| Wazuh | Security monitoring and endpoint detection |
| CrowdStrike Falcon | EDR and threat intelligence |
| SentinelOne | Endpoint protection and response |
| Velociraptor | Endpoint visibility and digital forensics |
| osquery | Endpoint querying and monitoring |
| Sysmon | Windows system telemetry |
| Zeek | Network security monitoring |
| Suricata | Network threat detection |

## Useful References

- Microsoft Sentinel: https://learn.microsoft.com/azure/sentinel/
- Microsoft Defender for Endpoint: https://learn.microsoft.com/defender-endpoint/
- Windows Event IDs: https://learn.microsoft.com/windows/security/threat-protection/auditing/
- Sysmon: https://learn.microsoft.com/sysinternals/downloads/sysmon
- Splunk Search Reference: https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/
- Kusto Query Language: https://learn.microsoft.com/azure/data-explorer/kusto/query/
- Sigma: https://sigmahq.io/
- Wazuh: https://documentation.wazuh.com/
- Velociraptor: https://docs.velociraptor.app/
- osquery: https://osquery.io/

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
