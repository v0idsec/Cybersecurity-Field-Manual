# Windows Process and Service Management

## Process management

```powershell
# List processes
Get-Process

# Find process by name
Get-Process -Name notepad

# Process details
Get-Process | Select-Object Name, Id, CPU, WorkingSet64

# Sort by CPU usage
Get-Process | Sort-Object CPU -Descending

# Sort by memory usage
Get-Process | Sort-Object WorkingSet64 -Descending

# Find process by PID
Get-Process -Id 1234

# Process command lines
Get-CimInstance Win32_Process |
    Select-Object ProcessId, ParentProcessId, Name, CommandLine
```

## Process termination

```powershell
# Stop process by name
Stop-Process -Name notepad

# Stop process by PID
Stop-Process -Id 1234

# Force termination
Stop-Process -Id 1234 -Force
```

Avoid terminating unknown processes during an investigation until evidence preservation requirements have been considered.

## Parent-child process investigation

```powershell
# Display process relationships
Get-CimInstance Win32_Process |
    Select-Object ProcessId, ParentProcessId, Name

# Query a specific process
Get-CimInstance Win32_Process -Filter "ProcessId = 1234"

# Find child processes by parent PID
Get-CimInstance Win32_Process |
    Where-Object ParentProcessId -eq 1234
```

## Service management

```powershell
# List services
Get-Service

# Find service by name
Get-Service -Name Spooler

# Find running services
Get-Service | Where-Object Status -eq Running

# Start service
Start-Service -Name Spooler

# Stop service
Stop-Service -Name Spooler

# Restart service
Restart-Service -Name Spooler

# Service configuration
Get-CimInstance Win32_Service |
    Select-Object Name, State, StartMode, StartName, PathName
```

## Service investigation

Review:

- Service executable path.
- Service account.
- Startup type.
- Service dependencies.
- File permissions on executable paths.
- Whether the executable is signed.
- Whether the service is expected.
- Associated network connections.

```powershell
# Find services with automatic startup
Get-CimInstance Win32_Service |
    Where-Object StartMode -eq "Auto"

# Find services running as LocalSystem
Get-CimInstance Win32_Service |
    Where-Object StartName -eq "LocalSystem"

# Find stopped services
Get-Service | Where-Object Status -eq Stopped
```

## Scheduled tasks

```powershell
# List scheduled tasks
Get-ScheduledTask

# Find running tasks
Get-ScheduledTask |
    Where-Object State -eq Running

# Task details
Get-ScheduledTask -TaskName "TaskName"

# Task actions
(Get-ScheduledTask -TaskName "TaskName").Actions

# Task triggers
(Get-ScheduledTask -TaskName "TaskName").Triggers

# Last run and next run information
Get-ScheduledTaskInfo -TaskName "TaskName"
```

## Startup locations

```powershell
# Current user's startup folder
Get-ChildItem "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup"

# All users' startup folder
Get-ChildItem "$env:ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"

# Run registry keys
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run"

# 32-bit Run key
Get-ItemProperty "HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Run"
```

## Autoruns

Microsoft Sysinternals Autoruns provides a broad view of Windows auto-start locations.

Useful areas:

- Logon entries.
- Scheduled tasks.
- Services.
- Drivers.
- Explorer extensions.
- Image hijacks.
- Winlogon entries.
- WMI persistence.

Reference: https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns

## Resource monitoring

```powershell
# CPU and memory
Get-Process | Sort-Object CPU -Descending

# System memory
Get-CimInstance Win32_OperatingSystem |
    Select-Object TotalVisibleMemorySize, FreePhysicalMemory

# Disk information
Get-Volume

# Disk space
Get-CimInstance Win32_LogicalDisk |
    Select-Object DeviceID, Size, FreeSpace

# System uptime
(Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
```

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
