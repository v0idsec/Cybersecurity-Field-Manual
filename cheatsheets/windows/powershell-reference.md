# PowerShell Reference

## Help and discovery

```powershell
# List available commands
Get-Command

# Find commands by name
Get-Command *process*

# Get command help
Get-Help Get-Process

# Full help
Get-Help Get-Process -Full

# Examples
Get-Help Get-Process -Examples

# Update help content
Update-Help

# Display PowerShell version
$PSVersionTable

# Display current location
Get-Location
```

## Navigation and files

```powershell
# List files
Get-ChildItem

# Include hidden files
Get-ChildItem -Force

# Recursive listing
Get-ChildItem -Recurse

# Change directory
Set-Location C:\Windows

# Current directory
Get-Location

# Create directory
New-Item -ItemType Directory -Path C:\Temp

# Create file
New-Item -ItemType File -Path C:\Temp\test.txt

# Copy file
Copy-Item source.txt destination.txt

# Move file
Move-Item source.txt destination.txt

# Remove file
Remove-Item file.txt

# Read file
Get-Content file.txt

# Follow file updates
Get-Content file.txt -Wait

# Search file contents
Select-String -Path *.log -Pattern "error"
```

## Object pipelines

PowerShell passes objects through pipelines rather than relying exclusively on text.

```powershell
# Filter processes
Get-Process | Where-Object CPU -gt 100

# Select properties
Get-Process | Select-Object Name, Id, CPU

# Sort by memory
Get-Process | Sort-Object WorkingSet64 -Descending

# Display first 10 results
Get-Process | Select-Object -First 10

# Count results
Get-Process | Measure-Object

# Export results to CSV
Get-Process | Export-Csv processes.csv -NoTypeInformation

# Convert results to JSON
Get-Process | ConvertTo-Json
```

## Variables and data types

```powershell
# Variable
$name = "Nick"

# Integer
$count = 10

# Array
$items = @("one", "two", "three")

# Hashtable
$user = @{
    Name = "Nick"
    Role = "Analyst"
}

# Access values
$name
$items[0]
$user.Name

# Display object type
$name.GetType()
```

## Conditions and loops

```powershell
# If / else
if ($count -gt 5) {
    Write-Output "Greater than five"
}
else {
    Write-Output "Five or less"
}

# ForEach
foreach ($item in $items) {
    Write-Output $item
}

# For loop
for ($i = 0; $i -lt 5; $i++) {
    Write-Output $i
}

# While loop
while ($count -gt 0) {
    $count--
}
```

## System information

```powershell
# Operating system
Get-CimInstance Win32_OperatingSystem

# Computer information
Get-CimInstance Win32_ComputerSystem

# BIOS
Get-CimInstance Win32_BIOS

# Installed hotfixes
Get-HotFix

# Environment variables
Get-ChildItem Env:

# Computer name
$env:COMPUTERNAME

# Current user
whoami

# Current PowerShell identity
[Security.Principal.WindowsIdentity]::GetCurrent().Name
```

## Error handling

```powershell
try {
    Get-Item "C:\example.txt" -ErrorAction Stop
}
catch {
    Write-Error $_
}
finally {
    Write-Output "Completed"
}
```

## Execution policy

```powershell
# View execution policies
Get-ExecutionPolicy -List

# View current policy
Get-ExecutionPolicy
```

Execution policy is not a security boundary and should not be treated as a substitute for application control.

## Useful shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl + C` | Interrupt command |
| `Ctrl + L` | Clear screen in supported terminals |
| `F7` | Command history in Windows Console |
| `Tab` | Autocomplete |
| `Up / Down` | Command history |
| `Ctrl + R` | Search history in PSReadLine |
| `Ctrl + Space` | Completion menu in supported PSReadLine configurations |

## References

- [PowerShell Documentation](https://learn.microsoft.com/en-us/powershell/)
- [PowerShell Gallery](https://www.powershellgallery.com/)
- [PowerShell GitHub](https://github.com/PowerShell/PowerShell)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
