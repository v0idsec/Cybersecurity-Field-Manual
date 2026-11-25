# Endpoint Threat Hunting

## Overview

Endpoint threat hunting investigates suspicious activity on workstations, servers and other devices.

Endpoint telemetry can reveal process execution, persistence, credential access, lateral movement and malware activity.

## Hunting Objectives

Common objectives:

- Identify suspicious process execution.
- Discover persistence mechanisms.
- Identify unauthorised remote access.
- Investigate unusual administrative activity.
- Identify suspicious file execution.
- Detect unexpected security control changes.

## Process Hunting

Investigate:

- Process name
- Executable path
- Parent process
- Command-line arguments
- User context
- File hash
- Digital signature
- Execution time

### Windows Process Inventory

```powershell
Get-CimInstance Win32_Process |
    Select-Object ProcessId, ParentProcessId, Name, ExecutablePath, CommandLine
```

### Identify Unusual Parent-Child Relationships

Investigate patterns such as:

- Office applications spawning scripting interpreters.
- Browsers spawning command-line utilities.
- Unexpected services launching command shells.
- Unusual processes running under SYSTEM.
- Applications launching from temporary directories.

These patterns require contextual validation.

## Persistence Hunting

### Windows Services

```powershell
Get-CimInstance Win32_Service |
    Select-Object Name, State, StartMode, StartName, PathName
```

Investigate unexpected services, unusual executable paths and recently modified configurations.

### Scheduled Tasks

```powershell
Get-ScheduledTask |
    Select-Object TaskName, TaskPath, State
```

### Startup Locations

Review:

- Registry Run keys
- Startup folders
- Scheduled tasks
- Services
- WMI event subscriptions
- Startup scripts

## Linux Persistence Hunting

### systemd Services

```bash
systemctl list-unit-files
```

### systemd Timers

```bash
systemctl list-timers --all
```

### Cron Jobs

```bash
crontab -l
```

### SSH Authorised Keys

```bash
find /home -name authorized_keys -type f -ls
```

Investigate unexpected entries and modifications.

## Authentication Hunting

Look for:

- Unexpected interactive logons
- Privileged logons
- Unusual remote access
- Repeated authentication failures
- Unexpected account creation
- Suspicious session activity

Correlate endpoint authentication with identity provider and domain controller logs.

## Network Hunting

Identify:

- Unusual outbound connections
- Unexpected listening services
- Connections to rare destinations
- Unexpected remote administration
- Processes communicating with suspicious infrastructure

### Windows Connections

```powershell
Get-NetTCPConnection |
    Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State, OwningProcess
```

### Linux Connections

```bash
ss -plant
```

## Security Control Tampering

Investigate:

- Antivirus configuration changes
- EDR service failures
- Logging service modifications
- Firewall changes
- Audit policy changes
- Unexpected security exclusions

Correlate configuration changes with administrative activity.

## File Hunting

Look for:

- Executables in unusual directories
- Recently created suspicious files
- Unexpected script files
- Files with unusual extensions
- Unsigned binaries in sensitive locations

Calculate hashes for relevant artefacts.

```powershell
Get-FileHash -Algorithm SHA256 "C:\Path\file.exe"
```

## Hunt Workflow

1. Define the endpoint hunting hypothesis.
2. Identify affected asset groups.
3. Confirm EDR and log coverage.
4. Search process and file telemetry.
5. Examine persistence locations.
6. Review authentication and network activity.
7. Correlate suspicious findings.
8. Preserve evidence.
9. Escalate or document the outcome.

## Important Considerations

- Process names can be spoofed.
- Signed binaries can be abused.
- Administrative tools are not inherently malicious.
- Missing telemetry may conceal activity.
- Do not execute suspicious files during routine hunting.
- Avoid disruptive response actions without authorisation.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
