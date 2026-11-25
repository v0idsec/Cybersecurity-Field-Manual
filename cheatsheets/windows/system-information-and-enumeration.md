# Windows System Information and Enumeration

## Host information

```powershell
# Operating system
Get-CimInstance Win32_OperatingSystem |
    Select-Object Caption, Version, BuildNumber, OSArchitecture

# Computer system
Get-CimInstance Win32_ComputerSystem |
    Select-Object Manufacturer, Model, Domain, PartOfDomain

# BIOS
Get-CimInstance Win32_BIOS

# System uptime
(Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime

# Hostname
$env:COMPUTERNAME

# Current user
whoami
```

## Hardware

```powershell
# Processor
Get-CimInstance Win32_Processor

# Physical memory
Get-CimInstance Win32_PhysicalMemory

# Disk drives
Get-CimInstance Win32_DiskDrive

# Logical disks
Get-CimInstance Win32_LogicalDisk

# Network adapters
Get-NetAdapter
```

## Installed software

```powershell
# Installed applications from common uninstall registry locations
$paths = @(
    "HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*",
    "HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*",
    "HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*"
)

Get-ItemProperty $paths -ErrorAction SilentlyContinue |
    Select-Object DisplayName, DisplayVersion, Publisher, InstallDate |
    Sort-Object DisplayName

# Installed Windows updates
Get-HotFix
```

Registry-based software inventory does not capture every application deployment method.

## Local users and groups

```powershell
# Local users
Get-LocalUser

# Local groups
Get-LocalGroup

# Local administrators
Get-LocalGroupMember -Group Administrators

# Current identity
whoami /all

# Current user's groups
whoami /groups
```

## Security configuration

```powershell
# Defender status
Get-MpComputerStatus

# Firewall profiles
Get-NetFirewallProfile

# BitLocker status
Get-BitLockerVolume

# Secure Boot status
Confirm-SecureBootUEFI

# UAC-related registry configuration
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
```

Some commands require administrative privileges or supported hardware and editions.

## Environment and paths

```powershell
# All environment variables
Get-ChildItem Env:

# PATH
$env:PATH

# User profile
$env:USERPROFILE

# Windows directory
$env:WINDIR

# Program Files
$env:ProgramFiles

# Temporary directory
$env:TEMP
```

## Domain and workgroup information

```powershell
# Computer domain information
Get-CimInstance Win32_ComputerSystem |
    Select-Object Name, Domain, PartOfDomain

# Domain controller discovery
nltest /dsgetdc:domain.local

# Secure channel status
Test-ComputerSecureChannel -Verbose

# Current logon server
$env:LOGONSERVER

# Domain information
systeminfo | Select-String "Domain"
```

## Environment enumeration checklist

- [ ] Hostname and operating system identified.
- [ ] OS version and patch level recorded.
- [ ] Domain membership confirmed.
- [ ] Current user and privileges reviewed.
- [ ] Local administrator membership reviewed.
- [ ] Installed applications inventoried.
- [ ] Running services reviewed.
- [ ] Network interfaces identified.
- [ ] Security products and status reviewed.
- [ ] Encryption status checked.
- [ ] Relevant system logs identified.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
