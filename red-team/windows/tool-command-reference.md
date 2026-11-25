# Windows Tool and Command Reference

A practical command reference for Windows host reconnaissance, account enumeration, service assessment, privilege review, network discovery, security configuration and evidence collection.

Commands should be used only on authorised systems.

This page is a quick reference, not a replacement for the detailed guides in this section.

## 1. Identity and System Information

| Command | Purpose |
|---|---|
| `whoami` | Current identity |
| `whoami /all` | Identity, groups and privileges |
| `whoami /priv` | Current token privileges |
| `whoami /groups` | Current group memberships |
| `hostname` | Computer name |
| `systeminfo` | System information |
| `ver` | Windows version |
| `set` | Environment variables |
| `echo %USERNAME%` | Current username |
| `echo %USERPROFILE%` | User profile path |

PowerShell:

```powershell
Get-ComputerInfo

Get-CimInstance Win32_OperatingSystem

Get-CimInstance Win32_ComputerSystem
```

## 2. User and Group Enumeration

| Command | Purpose |
|---|---|
| `net user` | List local users |
| `net user <username>` | Account details |
| `net localgroup` | List local groups |
| `net localgroup Administrators` | Local administrators |
| `net accounts` | Account policy |
| `query user` | Interactive sessions |
| `qwinsta` | Terminal sessions |
| `whoami /priv` | Privileges |

PowerShell:

```powershell
Get-LocalUser

Get-LocalGroup

Get-LocalGroupMember Administrators

Get-LocalGroupMember 'Remote Desktop Users'
```

## 3. Network Enumeration

| Command | Purpose |
|---|---|
| `ipconfig /all` | Network configuration |
| `ipconfig /displaydns` | DNS cache |
| `route print` | Routing table |
| `arp -a` | ARP cache |
| `netstat -ano` | Network connections and listeners |
| `net share` | Shared resources |
| `net use` | Network connections |
| `nslookup <host>` | DNS lookup |
| `tracert <host>` | Route tracing |
| `pathping <host>` | Route and packet-loss analysis |

PowerShell:

```powershell
Get-NetIPConfiguration

Get-NetIPAddress

Get-NetRoute

Get-NetTCPConnection

Get-NetUDPEndpoint

Get-DnsClientServerAddress
```

## 4. Process Enumeration

| Command | Purpose |
|---|---|
| `tasklist` | Running processes |
| `tasklist /v` | Detailed process list |
| `tasklist /svc` | Processes and services |
| `taskkill /PID <PID>` | Terminate a process |
| `wmic process list brief` | Legacy WMI process inventory |

PowerShell:

```powershell
Get-Process

Get-CimInstance Win32_Process |
    Select-Object ProcessId, ParentProcessId, Name, ExecutablePath
```

Use process termination only where explicitly authorised.

## 5. Service Enumeration

| Command | Purpose |
|---|---|
| `sc query` | Service state |
| `sc query type= service state= all` | All services |
| `sc qc <service>` | Service configuration |
| `sc sdshow <service>` | Service security descriptor |
| `net start` | Running services |
| `tasklist /svc` | Service-to-process mapping |

PowerShell:

```powershell
Get-Service

Get-CimInstance Win32_Service |
    Select-Object Name, StartName, State, StartMode, PathName
```

## 6. Scheduled Tasks

| Command | Purpose |
|---|---|
| `schtasks /query` | List tasks |
| `schtasks /query /fo LIST /v` | Detailed task information |
| `schtasks /query /tn <task>` | Specific task |
| `schtasks /showSid /tn <task>` | Task security identifier information |

PowerShell:

```powershell
Get-ScheduledTask

Get-ScheduledTaskInfo -TaskName <task_name>
```

Avoid modifying or deleting tasks during reconnaissance.

## 7. Filesystem and Permissions

| Command | Purpose |
|---|---|
| `dir /a` | List all files, including hidden |
| `tree /f` | Directory tree |
| `where <file>` | Locate executable |
| `icacls <path>` | ACL inspection |
| `takeown /?` | Ownership command reference |
| `attrib` | File attributes |
| `fsutil fsinfo drives` | Filesystem drive information |

PowerShell:

```powershell
Get-ChildItem -Force

Get-Acl <path>

Get-PSDrive -PSProvider FileSystem

Get-Volume
```

## 8. Registry

| Command | Purpose |
|---|---|
| `reg query <key>` | Query registry |
| `reg query <key> /s` | Recursive registry query |
| `reg compare` | Compare registry keys |
| `reg export` | Export registry key |
| `reg save` | Save registry hive |

PowerShell:

```powershell
Get-ItemProperty <registry_path>

Get-ChildItem <registry_path>

Get-Acl <registry_path>
```

Registry modification and hive extraction should be separately authorised.

## 9. Security Controls

| Command | Purpose |
|---|---|
| `netsh advfirewall show allprofiles` | Firewall profile status |
| `auditpol /get /category:*` | Audit policy |
| `gpresult /r` | Applied Group Policy summary |
| `gpresult /h report.html` | Group Policy report |
| `manage-bde -status` | BitLocker status |
| `sfc /verifyonly` | System file verification |
| `dism /online /get-features` | Windows feature inventory |

PowerShell:

```powershell
Get-MpComputerStatus

Get-MpPreference

Get-NetFirewallProfile

Get-BitLockerVolume

Get-HotFix

Get-Tpm
```

## 10. Credential and Certificate References

| Command | Purpose |
|---|---|
| `cmdkey /list` | List stored credential targets |
| `certutil -store My` | Inspect certificate store |
| `certutil -dump <file>` | Inspect certificate-related file |
| `klist` | Inspect current Kerberos tickets |

PowerShell:

```powershell
Get-ChildItem Cert:\CurrentUser\My

Get-ChildItem Cert:\LocalMachine\My
```

Do not export credentials, private keys or authentication material without explicit authorisation.

## 11. Event Logs

| Command | Purpose |
|---|---|
| `wevtutil el` | List event logs |
| `wevtutil gli <log>` | Log information |
| `wevtutil qe <log> /c:20 /rd:true /f:text` | Query recent events |
| `auditpol /get /category:*` | Audit configuration |

PowerShell:

```powershell
Get-WinEvent -ListLog *

Get-WinEvent -LogName Security -MaxEvents 20

Get-WinEvent -LogName System -MaxEvents 20

Get-WinEvent -LogName 'Microsoft-Windows-PowerShell/Operational' -MaxEvents 20
```

Security log access may require elevated permissions.

## 12. PowerShell Reconnaissance

| Command | Purpose |
|---|---|
| `$PSVersionTable` | PowerShell version |
| `Get-ExecutionPolicy -List` | Execution policy |
| `Get-Module -ListAvailable` | Available modules |
| `Get-Command` | Available commands |
| `Get-History` | Current session history |
| `Get-ChildItem Env:` | Environment variables |
| `Get-PSSessionConfiguration` | Remoting configurations |

## 13. Useful Sysinternals Tools

| Tool | Purpose |
|---|---|
| AccessChk | Effective permissions |
| AccessEnum | Filesystem and registry permissions |
| Autoruns | Automatic execution enumeration |
| Process Explorer | Process and token inspection |
| Process Monitor | Filesystem, registry and process activity |
| PsList | Process enumeration |
| PsService | Service inspection |
| TCPView | Network connections |
| Sigcheck | Signature and file metadata |
| Sysmon | System activity telemetry |
| Strings | String extraction from files |

Official reference:

https://learn.microsoft.com/sysinternals/

## 14. Privilege Escalation Assessment Tools

| Tool | Purpose |
|---|---|
| WinPEAS | Windows privilege escalation enumeration |
| Seatbelt | Windows security configuration enumeration |
| PowerUp | PowerShell privilege escalation checks |
| PrivescCheck | Windows privilege escalation assessment |
| AccessChk | Permission analysis |
| Process Explorer | Process and token analysis |

Use automated tools as an enumeration aid. Manually validate every significant finding.

## 15. Network and Service Assessment Tools

| Tool | Purpose |
|---|---|
| Nmap | Host and service discovery |
| Wireshark | Network traffic analysis |
| TCPView | Local connection monitoring |
| Netcat | Connectivity testing |
| Sysinternals PsTools | Remote and local administration utilities |

## 16. Useful Event IDs

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
| 4699 | Scheduled task deleted |
| 4702 | Scheduled task updated |
| 4720 | User account created |
| 4722 | User account enabled |
| 4728 | Member added to global group |
| 4732 | Member added to local group |
| 1102 | Security audit log cleared |
| 7045 | Service installed |
| 4104 | PowerShell script block logging |

## 17. Quick Enumeration Sequence

A basic read-only sequence for an authorised Windows host:

```powershell
# Identity
whoami /all

# Host
hostname
systeminfo

# Operating system
Get-CimInstance Win32_OperatingSystem

# Local accounts
Get-LocalUser

# Local groups
Get-LocalGroup

# Local administrators
Get-LocalGroupMember Administrators

# Network
ipconfig /all
route print
netstat -ano

# Processes
Get-Process

# Services
Get-CimInstance Win32_Service |
    Select-Object Name, StartName, State, StartMode, PathName

# Scheduled tasks
Get-ScheduledTask

# Installed software
Get-ItemProperty @(
    'HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*',
    'HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*'
) -ErrorAction SilentlyContinue |
    Select-Object DisplayName, DisplayVersion, Publisher

# Security controls
Get-MpComputerStatus
Get-NetFirewallProfile
Get-BitLockerVolume
```

## 18. Operational Notes

- Confirm command compatibility with the target Windows version.
- Prefer read-only enumeration initially.
- Some PowerShell cmdlets require administrative permissions.
- Avoid disruptive commands on production systems.
- Treat process arguments, environment variables and event logs as potentially sensitive.
- Record tool versions and relevant command output.
- Redact secrets before storing evidence.
- Validate automated findings manually.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
