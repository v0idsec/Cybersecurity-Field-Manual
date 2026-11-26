# Process Review
# Lists running processes and their executable paths.
#
# Usage:
#   .\process-review.ps1
#
# Output:
#   process-review.csv
#
# Some process details may require elevated permissions.

$OutputFile = ".\process-review.csv"

Write-Host "[*] Collecting running process information..." -ForegroundColor Cyan

$Results = Get-CimInstance Win32_Process |
    Select-Object `
        ProcessId,
        ParentProcessId,
        Name,
        ExecutablePath,
        CommandLine,
        CreationDate

$Results |
    Sort-Object Name |
    Export-Csv -Path $OutputFile -NoTypeInformation

Write-Host "[+] Processes collected: $($Results.Count)" -ForegroundColor Green
Write-Host "[+] Results saved to: $OutputFile"
