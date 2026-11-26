# Blue Team Script Templates

Reusable scripts for defensive security operations, system auditing, investigation and monitoring.

These templates are designed to assist with common Blue Team activities and provide starting points for further automation.

## Scripts

| Script | Language | Description |
|---|---|---|
| [failed-logins.ps1](failed-logins.ps1) | PowerShell | Reviews Windows Security events for failed logon attempts |
| [system-inventory.ps1](system-inventory.ps1) | PowerShell | Collects basic Windows system and configuration information |
| [process-review.ps1](process-review.ps1) | PowerShell | Lists running processes and their executable paths |
| [log-summary.py](log-summary.py) | Python | Summarises log files by severity and keyword |
| [file-integrity.py](file-integrity.py) | Python | Calculates SHA-256 hashes to support file integrity monitoring |

## Requirements

- PowerShell 5.1 or later.
- Python 3.10 or later.
- Administrative permissions may be required for some Windows event logs.

Python scripts use standard library modules unless otherwise specified.

## Usage

Review each script before execution.

Update configuration variables to suit your environment.

Scripts should be tested before being introduced into production monitoring or incident response workflows.

## Important

These scripts are intended to support defensive investigation and administration.

They do not replace a properly configured SIEM, EDR platform, centralised logging solution or formal incident response process.
