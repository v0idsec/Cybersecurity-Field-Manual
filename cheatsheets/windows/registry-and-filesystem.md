# Windows Registry and Filesystem Reference

## Registry structure

| Hive | Description |
|---|---|
| `HKEY_LOCAL_MACHINE` | System-wide configuration |
| `HKEY_CURRENT_USER` | Current user configuration |
| `HKEY_CLASSES_ROOT` | File associations and COM registration view |
| `HKEY_USERS` | Loaded user profiles |
| `HKEY_CURRENT_CONFIG` | Current hardware profile view |

PowerShell registry drives:

| Provider path | Registry location |
|---|---|
| `HKLM:` | HKEY_LOCAL_MACHINE |
| `HKCU:` | HKEY_CURRENT_USER |
| `HKCR:` | HKEY_CLASSES_ROOT |
| `HKU:` | HKEY_USERS |

## Registry operations

```powershell
# Read registry key
Get-Item HKLM:\Software\Microsoft\Windows\CurrentVersion

# Read registry values
Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion

# Create registry key
New-Item -Path HKCU:\Software\Example

# Set registry value
Set-ItemProperty -Path HKCU:\Software\Example -Name Setting -Value "Enabled"

# Remove registry value
Remove-ItemProperty -Path HKCU:\Software\Example -Name Setting

# Remove registry key
Remove-Item HKCU:\Software\Example
```

Review the target key and export relevant data before making registry changes.

## Common investigation locations

### Run keys

```powershell
# Current user
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"

# Local machine
Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run"

# 32-bit machine view
Get-ItemProperty "HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Run"
```

### UserAssist

UserAssist records certain user activity and application execution information.

Location:

```text
HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist
```

Values are encoded using ROT13. Interpret them with an appropriate forensic parser.

### Recent files

```text
%APPDATA%\Microsoft\Windows\Recent
```

### Startup folders

```text
%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

%ProgramData%\Microsoft\Windows\Start Menu\Programs\Startup
```

## Filesystem permissions

```powershell
# Display ACL
Get-Acl C:\Temp\file.txt

# Display owner and access rules
(Get-Acl C:\Temp\file.txt).Access

# Set ACL
$acl = Get-Acl C:\Temp\file.txt

# Export ACL information
Get-Acl C:\Temp\file.txt | Format-List *
```

Use `icacls` for common permission operations:

```cmd
:: Display permissions
icacls C:\Temp\file.txt

:: Recursive permission listing
icacls C:\Temp /T

:: Save ACLs
icacls C:\Temp /save C:\Temp\acl-backup.txt /T

:: Restore ACLs
icacls C:\Temp /restore C:\Temp\acl-backup.txt
```

## File hashes

```powershell
# SHA-256
Get-FileHash file.exe -Algorithm SHA256

# SHA-1
Get-FileHash file.exe -Algorithm SHA1

# SHA-512
Get-FileHash file.exe -Algorithm SHA512
```

## Digital signatures

```powershell
# Inspect file signature
Get-AuthenticodeSignature file.exe

# Check signature status
(Get-AuthenticodeSignature file.exe).Status

# Display signer
(Get-AuthenticodeSignature file.exe).SignerCertificate
```

A valid signature does not guarantee that a file is safe.

## File discovery

```powershell
# Find files by name
Get-ChildItem C:\ -Filter "*.log" -Recurse -ErrorAction SilentlyContinue

# Find files modified recently
Get-ChildItem C:\Temp -File -Recurse |
    Where-Object LastWriteTime -gt (Get-Date).AddHours(-24)

# Find large files
Get-ChildItem C:\ -File -Recurse -ErrorAction SilentlyContinue |
    Sort-Object Length -Descending |
    Select-Object -First 20 FullName, Length

# Find hidden files
Get-ChildItem C:\Temp -Force
```

## Alternate Data Streams

NTFS supports alternate data streams (ADS).

```powershell
# List streams
Get-Item file.txt -Stream *

# Read a named stream
Get-Content file.txt -Stream Zone.Identifier

# Remove a stream
Remove-Item file.txt -Stream Zone.Identifier
```

The `Zone.Identifier` stream may contain Mark-of-the-Web information.

## Important forensic artefacts

| Artefact | Purpose |
|---|---|
| Prefetch | Application execution artefacts, where enabled |
| Amcache | Application inventory and execution-related artefacts |
| Shimcache | Application compatibility cache |
| UserAssist | User activity and application execution artefacts |
| Jump Lists | Recent application and file activity |
| LNK files | Shortcut and file access artefacts |
| `$MFT` | NTFS filesystem metadata |
| USN Journal | NTFS change journal |
| Event Logs | System and security events |
| Browser history | Web activity |

Artefacts have limitations and should be interpreted together rather than as definitive proof of execution or user intent.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
