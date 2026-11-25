# Endpoint Investigation

## Overview

Endpoint investigations examine activity on workstations, servers and other managed devices to identify compromise, understand execution behaviour and establish incident scope.

This guide focuses on a structured investigation using endpoint telemetry and supporting operating system evidence.

## Investigation Objectives

- Identify the affected endpoint.
- Establish the incident timeline.
- Identify suspicious processes and files.
- Determine the affected user context.
- Identify network communication.
- Identify persistence mechanisms.
- Establish whether other systems are affected.
- Preserve relevant evidence.

## Initial Collection

Record:

- Hostname
- Device identifier
- IP addresses
- Operating system
- Logged-on users
- Asset owner
- Business function
- EDR agent status
- Investigation start time

Record timestamps in a consistent timezone, preferably UTC for cross-system correlation.

## Process Investigation

Examine:

- Process name
- Executable path
- Process ID
- Parent process
- Command line
- User context
- Start and termination times
- Digital signature
- File hash

### Windows Process Review

List running processes:

```powershell
Get-Process
```

Show process details:

```powershell
Get-CimInstance Win32_Process |
    Select-Object ProcessId, ParentProcessId, Name, ExecutablePath, CommandLine
```

Review process start events where available:

```powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'Security'
    Id = 4688
    StartTime = (Get-Date).AddHours(-24)
}
```

Process creation auditing and command-line inclusion must be configured for the relevant fields to be available.

## File Investigation

Examine:

- File path
- File name
- File size
- Creation and modification times
- Hashes
- Digital signatures
- File reputation
- Associated processes

### Calculate File Hashes

```powershell
Get-FileHash -Algorithm SHA256 "C:\Path\file.exe"
```

Linux:

```bash
sha256sum /path/to/file
```

Do not execute suspicious files simply to observe their behaviour.

## Network Investigation

Identify:

- Active connections
- Remote addresses
- Destination ports
- DNS queries
- Associated processes
- Connection timestamps

### Windows

```powershell
Get-NetTCPConnection
```

```powershell
netstat -ano
```

Resolve a process ID:

```powershell
Get-Process -Id 1234
```

### Linux

```bash
ss -plant
```

```bash
lsof -i -P -n
```

Correlate endpoint connections with firewall, DNS, proxy and network detection logs.

## Persistence Investigation

Common persistence locations include:

### Windows

- Registry Run keys
- Startup folders
- Scheduled tasks
- Services
- WMI event subscriptions
- Startup scripts
- Browser extensions
- Unusual account creation

Useful commands:

```powershell
Get-ScheduledTask
```

```powershell
Get-CimInstance Win32_Service |
    Select-Object Name, State, StartMode, PathName
```

Review common Run keys:

```powershell
Get-ItemProperty `
    'HKLM:\Software\Microsoft\Windows\CurrentVersion\Run'
```

```powershell
Get-ItemProperty `
    'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run'
```

### Linux

Review:

- Cron jobs
- systemd services and timers
- SSH authorised keys
- Shell startup files
- User account changes
- Sudoers modifications
- Unexpected binaries in executable paths

Useful commands:

```bash
systemctl list-unit-files
```

```bash
systemctl list-timers --all
```

```bash
crontab -l
```

Review system-wide cron configuration:

```bash
ls -la /etc/cron*
```

## User and Authentication Investigation

Review:

- Logged-on sessions
- Recent authentication
- Privileged account use
- New local accounts
- Password changes
- Remote access activity
- Unexpected authentication sources

Correlate endpoint events with identity provider and domain controller logs.

## Timeline Construction

Build a timeline containing:

| Timestamp | Event | Source | Significance |
|---|---|---|---|
| 09:12 | User authentication | Security log | Initial access context |
| 09:14 | Process execution | EDR | Suspicious execution |
| 09:15 | DNS query | DNS logs | External communication |
| 09:16 | File creation | Sysmon | Possible payload |
| 09:18 | Persistence change | Endpoint logs | Possible persistence |

The example is illustrative only.

## Evidence Preservation

- Preserve original logs where possible.
- Record collection timestamps.
- Document collection methods.
- Calculate hashes for acquired files.
- Maintain chain-of-custody records where required.
- Avoid unnecessary changes to the affected system.
- Follow organisational forensic procedures.

## Investigation Conclusion

Document:

- Confirmed findings
- Suspected activity
- Affected systems
- Affected accounts
- Indicators of compromise
- Timeline
- Scope and impact
- Containment actions
- Remaining uncertainties
- Recommended remediation

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
