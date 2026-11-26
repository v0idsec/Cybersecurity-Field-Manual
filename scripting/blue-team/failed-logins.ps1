# Failed Login Review
# Retrieves failed Windows logon events from the Security event log.
#
# Event ID 4625 = An account failed to log on.
#
# Usage:
#   .\failed-logins.ps1
#
# May require elevated permissions to read the Security log.

$HoursBack = 24
$OutputFile = ".\failed-logins.csv"

$StartTime = (Get-Date).AddHours(-$HoursBack)

Write-Host "[*] Reviewing failed logons since $StartTime" -ForegroundColor Cyan

try {

    $Events = Get-WinEvent -FilterHashtable @{
        LogName   = "Security"
        Id        = 4625
        StartTime = $StartTime
    } -ErrorAction Stop

    $Results = foreach ($Event in $Events) {

        [xml]$XML = $Event.ToXml()

        $Data = @{}

        foreach ($Item in $XML.Event.EventData.Data) {
            $Data[$Item.Name] = $Item.'#text'
        }

        [PSCustomObject]@{
            TimeCreated       = $Event.TimeCreated
            TargetUserName    = $Data["TargetUserName"]
            TargetDomainName  = $Data["TargetDomainName"]
            WorkstationName   = $Data["WorkstationName"]
            IpAddress         = $Data["IpAddress"]
            LogonType         = $Data["LogonType"]
            Status            = $Data["Status"]
            SubStatus         = $Data["SubStatus"]
        }
    }

    $Results |
        Sort-Object TimeCreated -Descending |
        Export-Csv -Path $OutputFile -NoTypeInformation

    Write-Host "[+] Events found: $($Results.Count)" -ForegroundColor Green
    Write-Host "[+] Results saved to: $OutputFile"

}
catch {

    Write-Host "[-] Unable to retrieve Security events." -ForegroundColor Red
    Write-Host $_.Exception.Message
}
