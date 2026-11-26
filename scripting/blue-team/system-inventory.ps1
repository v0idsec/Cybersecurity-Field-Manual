# System Inventory
# Collects basic Windows system information.
#
# Usage:
#   .\system-inventory.ps1
#
# Output:
#   system-inventory.json

$OutputFile = ".\system-inventory.json"

Write-Host "[*] Collecting system information..." -ForegroundColor Cyan

$Computer = Get-CimInstance Win32_ComputerSystem
$OperatingSystem = Get-CimInstance Win32_OperatingSystem
$Processor = Get-CimInstance Win32_Processor
$Disks = Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3"
$NetworkAdapters = Get-CimInstance Win32_NetworkAdapterConfiguration |
    Where-Object { $_.IPEnabled }

$Inventory = [PSCustomObject]@{

    Computer = [PSCustomObject]@{
        Name         = $Computer.Name
        Manufacturer = $Computer.Manufacturer
        Model        = $Computer.Model
        Domain       = $Computer.Domain
        TotalMemoryGB = [math]::Round(
            $Computer.TotalPhysicalMemory / 1GB, 2
        )
    }

    OperatingSystem = [PSCustomObject]@{
        Caption        = $OperatingSystem.Caption
        Version        = $OperatingSystem.Version
        BuildNumber    = $OperatingSystem.BuildNumber
        InstallDate    = $OperatingSystem.InstallDate
        LastBootUpTime = $OperatingSystem.LastBootUpTime
    }

    Processor = @(
        $Processor | Select-Object Name, NumberOfCores,
            NumberOfLogicalProcessors
    )

    Disks = @(
        $Disks | Select-Object DeviceID, VolumeName,
            @{Name = "SizeGB"; Expression = {
                [math]::Round($_.Size / 1GB, 2)
            }},
            @{Name = "FreeGB"; Expression = {
                [math]::Round($_.FreeSpace / 1GB, 2)
            }}
    )

    Network = @(
        $NetworkAdapters | Select-Object Description,
            MACAddress, IPAddress, DefaultIPGateway, DNSServerSearchOrder
    )
}

$Inventory |
    ConvertTo-Json -Depth 5 |
    Set-Content -Path $OutputFile -Encoding UTF8

Write-Host "[+] Inventory complete." -ForegroundColor Green
Write-Host "[+] Output saved to: $OutputFile"
