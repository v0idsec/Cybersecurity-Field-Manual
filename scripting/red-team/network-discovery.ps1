# Network Discovery
# Checks a defined IPv4 range for responding hosts.
#
# Usage:
#   .\network-discovery.ps1
#
# Configure the network range before execution.
# Only use against authorised networks.

$NetworkPrefix = "192.168.1"
$StartAddress = 1
$EndAddress = 254

$Results = [System.Collections.Generic.List[object]]::new()

Write-Host "[*] Starting network discovery..." -ForegroundColor Cyan

for ($i = $StartAddress; $i -le $EndAddress; $i++) {

    $IP = "$NetworkPrefix.$i"

    Write-Host "[*] Checking $IP"

    $Responding = Test-Connection `
        -ComputerName $IP `
        -Count 1 `
        -Quiet `
        -ErrorAction SilentlyContinue

    if ($Responding) {

        $Results.Add([PSCustomObject]@{
            IPAddress = $IP
            Status    = "Responding"
            Checked   = Get-Date
        })

        Write-Host "[+] Host responding: $IP" -ForegroundColor Green
    }
}

$OutputFile = ".\network-discovery-results.csv"

$Results | Export-Csv -Path $OutputFile -NoTypeInformation

Write-Host ""
Write-Host "[+] Discovery complete." -ForegroundColor Green
Write-Host "[+] Responding hosts: $($Results.Count)"
Write-Host "[+] Results saved to: $OutputFile"
