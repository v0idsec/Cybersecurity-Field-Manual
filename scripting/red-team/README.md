# Red Team Script Templates

Reusable scripts for authorised security assessments, reconnaissance and information gathering.

These templates are intended to assist with common assessment tasks without replacing proper testing methodology.

## Scripts

| Script | Language | Description |
|---|---|---|
| [network-discovery.ps1](network-discovery.ps1) | PowerShell | Checks a defined range of IP addresses for responding hosts |
| [dns-lookup.py](dns-lookup.py) | Python | Retrieves DNS records and performs basic hostname resolution |
| [tcp-port-check.py](tcp-port-check.py) | Python | Checks specified TCP ports on an authorised target |
| [http-header-review.py](http-header-review.py) | Python | Retrieves HTTP response headers and identifies common security headers |

## Requirements

- PowerShell 5.1 or later for PowerShell scripts.
- Python 3.10 or later for Python scripts.
- Network connectivity to the authorised assessment environment.

Python scripts use standard library modules unless otherwise specified.

## Usage

Review each script before execution.

Update the configuration variables to match the authorised assessment environment.

## Scope and Authorisation

These scripts are intended for authorised security testing and educational use.

Only scan systems, networks and services for which you have explicit permission.
