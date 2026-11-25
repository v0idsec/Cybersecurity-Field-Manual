# Windows Reconnaissance

A structured reference for identifying Windows host characteristics, operating system details, network configuration, installed software, running processes and security controls.

The objective is to build an accurate picture of the host before performing deeper assessment activities.

## 1. Host Identification

### 1.1 System Information

```powershell
# General system information
systeminfo

# Computer name
hostname

# Operating system details
Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber, OsArchitecture

# Environment variables
Get-ChildItem Env:

# Current date and time
Get-Date
```

Record:

- Hostname.
- Operating system edition.
- Version and build.
- Architecture.
- Installation date, where available.
- System uptime.
- Domain or workgroup membership.
- System role.
- Time zone.

### 1.2 OS Version and Build

```powershell
[System.Environment]::OSVersion

Get-CimInstance Win32_OperatingSystem |
    Select-Object Caption, Version, BuildNumber, OSArchitecture, InstallDate, LastBootUpTime
```

Version information should be checked against vendor lifecycle and security update information. An older build number alone does not establish that a system is vulnerable.

### 1.3 Hardware Information

```powershell
Get-CimInstance Win32_ComputerSystem |
    Select-Object Manufacturer, Model, TotalPhysicalMemory, NumberOfLogicalProcessors

Get-CimInstance Win32_Processor |
    Select-Object Name, NumberOfCores, NumberOfLogicalProcessors

Get-CimInstance Win32_PhysicalMemory |
    Select-Object Manufacturer, Capacity, Speed
```

Hardware information can help identify virtual machines, specialised endpoints and systems with unusual operational requirements.

## 2. User Context

```powershell
# Current identity
whoami

# Current identity and groups
whoami /all

# Current user
$env:USERNAME

# User profile
$env:USERPROFILE

# Current logon server, if domain joined
$env:LOGONSERVER
```

Determine:

- Current account.
- Local or domain identity.
- Group memberships.
- Enabled and disabled privileges.
- Integrity level.
- Elevated or non-elevated context.
- Whether the session is interactive or service-based.

See `user-and-group-enumeration.md` for detailed account and privilege analysis.

## 3. Network Reconnaissance

### 3.1 Interfaces and Addresses

```powershell
ipconfig /all

Get-NetIPConfiguration

Get-NetIPAddress |
    Select-Object InterfaceAlias, IPAddress, PrefixLength, AddressFamily
```

Record:

- Interface names.
- IPv4 and IPv6 addresses.
- Subnet prefixes.
- Default gateways.
- DNS servers.
- DHCP configuration.
- VPN and virtual interfaces.

### 3.2 Routing

```powershell
route print

Get-NetRoute |
    Sort-Object RouteMetric |
    Format-Table DestinationPrefix, NextHop, InterfaceAlias, RouteMetric
```

Identify:

- Default routes.
- Internal routes.
- VPN routes.
- Virtual network interfaces.
- Unexpected routing paths.

### 3.3 DNS Configuration

```powershell
ipconfig /displaydns

Get-DnsClientServerAddress

Resolve-DnsName example.com
```

DNS cache entries may reveal recently accessed infrastructure. Treat this information as sensitive and avoid retaining unrelated user browsing data.

### 3.4 Connections and Listening Ports

```powershell
netstat -ano

Get-NetTCPConnection |
    Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State, OwningProcess

Get-NetUDPEndpoint |
    Select-Object LocalAddress, LocalPort, OwningProcess
```

Map process IDs to processes:

```powershell
Get-Process -Id <PID>
```

Investigate unexpected listeners, externally reachable services and connections associated with sensitive processes.

## 4. Processes and Services

### 4.1 Running Processes

```powershell
Get-Process |
    Sort-Object ProcessName |
    Format-Table Id, ProcessName, Path

tasklist /v
```

Review:

- Process ownership.
- Executable location.
- Parent-child relationships.
- Unexpected processes.
- Unusual execution paths.
- Processes running with elevated privileges.

### 4.2 Services

```powershell
Get-Service |
    Sort-Object Status, Name

Get-CimInstance Win32_Service |
    Select-Object Name, DisplayName, State, StartMode, StartName, PathName
```

Pay particular attention to:

- Services running as LocalSystem.
- Services running under privileged accounts.
- Unquoted executable paths.
- Writable service binaries or directories.
- Unusual service accounts.
- Services with unnecessary network exposure.

See `services-and-scheduled-tasks.md`.

## 5. Installed Software

```powershell
# Installed applications from common uninstall registry locations
$paths = @(
    'HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*',
    'HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*',
    'HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*'
)

Get-ItemProperty $paths -ErrorAction SilentlyContinue |
    Select-Object DisplayName, DisplayVersion, Publisher, InstallDate |
    Sort-Object DisplayName
```

Also inspect:

```powershell
Get-AppxPackage |
    Select-Object Name, Version, Publisher
```

Review:

- Unsupported applications.
- Outdated software.
- Unnecessary remote access utilities.
- Development tools.
- Database clients.
- Security products.
- Software installed in user-writable locations.

Do not assume an old application version is exploitable without checking the actual affected configuration.

## 6. Filesystem Reconnaissance

```powershell
# Available drives
Get-PSDrive -PSProvider FileSystem

# Filesystem volumes
Get-Volume

# Top-level directory contents
Get-ChildItem C:\ -Force -ErrorAction SilentlyContinue

# Environment-based application paths
$env:ProgramFiles
$env:ProgramFiles(x86)
$env:ProgramData
$env:TEMP
$env:TMP
```

Review:

- Application directories.
- Shared data directories.
- Temporary locations.
- Backup locations.
- User-writable program directories.
- Unusual mount points.
- Sensitive configuration locations.

Avoid bulk collection of user documents or personal data.

## 7. Security Controls

### 7.1 Windows Defender

```powershell
Get-MpComputerStatus

Get-MpPreference |
    Select-Object DisableRealtimeMonitoring, DisableBehaviorMonitoring, PUAProtection
```

### 7.2 Firewall

```powershell
Get-NetFirewallProfile |
    Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction
```

### 7.3 UAC

```powershell
Get-ItemProperty `
    'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' |
    Select-Object EnableLUA, ConsentPromptBehaviorAdmin, PromptOnSecureDesktop
```

### 7.4 BitLocker

```powershell
Get-BitLockerVolume
```

Do not retrieve or expose BitLocker recovery passwords during routine reconnaissance.

### 7.5 Application Control

```powershell
Get-CimInstance -Namespace root\Microsoft\Windows\DeviceGuard `
    -ClassName Win32_DeviceGuard -ErrorAction SilentlyContinue
```

Review the status of relevant application control and virtualization-based security features.

## 8. Patch and Update State

```powershell
Get-HotFix |
    Sort-Object InstalledOn -Descending |
    Select-Object -First 20 HotFixID, Description, InstalledOn
```

Patch enumeration is only an initial indicator. Validate patch state against the applicable servicing channel, cumulative updates and vendor advisories.

## 9. Virtualisation and Containers

Identify virtualisation indicators:

```powershell
Get-CimInstance Win32_ComputerSystem |
    Select-Object Manufacturer, Model, HypervisorPresent
```

Review installed container and virtualisation features where relevant:

```powershell
Get-WindowsOptionalFeature -Online |
    Where-Object FeatureName -Match 'Hyper-V|VirtualMachinePlatform|Containers'
```

Container and hypervisor exposure should be assessed according to the host's intended role.

## 10. Reconnaissance Notes

Maintain a structured record:

| Field | Value |
|---|---|
| Hostname | [Hostname] |
| OS / Build | [Version] |
| Architecture | [x64 / ARM64] |
| Current User | [Identity] |
| Integrity Level | [Level] |
| Network Addresses | [Addresses] |
| Domain / Workgroup | [Membership] |
| Running Security Controls | [Products] |
| Relevant Services | [Services] |
| Notable Observations | [Notes] |

## 11. Validation and Reporting

For each observation:

1. Record the source command or evidence.
2. Confirm the result is relevant to the host.
3. Distinguish configuration weaknesses from confirmed vulnerabilities.
4. Identify potential security impact.
5. Avoid retaining unrelated sensitive data.
6. Recommend an actionable corrective measure.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
