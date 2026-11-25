# Kerberos Reference

## Kerberos overview

Kerberos is a network authentication protocol commonly used by Active Directory.

Core components:

| Component | Purpose |
|---|---|
| KDC | Key Distribution Centre |
| AS | Authentication Service |
| TGT | Ticket Granting Ticket |
| TGS | Ticket Granting Service |
| SPN | Service Principal Name |
| PAC | Privilege Attribute Certificate |

## Common ports

| Port | Purpose |
|---|---|
| 88 TCP/UDP | Kerberos |
| 464 TCP/UDP | Kerberos password change |
| 389 TCP/UDP | LDAP |
| 636 TCP | LDAPS |

## Native ticket commands

```cmd
:: List current Kerberos tickets
klist

:: Purge current logon session tickets
klist purge

:: Display ticket information
klist tickets

:: Request a service ticket
klist get cifs/server.example.local

:: Display current logon session
klist sessions
```

Purging tickets can interrupt access to network resources. Use only when operationally appropriate.

## PowerShell and Active Directory

```powershell
# Find users with SPNs
Get-ADUser -Filter 'ServicePrincipalName -like "*"' `
    -Properties ServicePrincipalName

# Find computer SPNs
Get-ADComputer -Filter 'ServicePrincipalName -like "*"' `
    -Properties ServicePrincipalName

# Find accounts without Kerberos pre-authentication
Get-ADUser -Filter 'DoesNotRequirePreAuth -eq $true'

# Display current domain policy
Get-ADDefaultDomainPasswordPolicy
```

## SPN examples

Common service classes:

| SPN service | Common use |
|---|---|
| `HTTP` | Web services |
| `CIFS` | File services |
| `MSSQLSvc` | Microsoft SQL Server |
| `LDAP` | Directory services |
| `HOST` | Host services |
| `WSMAN` | Windows Remote Management |

Example:

```text
MSSQLSvc/sql01.example.local:1433
```

## Kerberos-related security events

| Event ID | Description |
|---|---|
| 4768 | TGT requested |
| 4769 | Service ticket requested |
| 4770 | Service ticket renewed |
| 4771 | Kerberos pre-authentication failed |

Review event volume, source hosts, account behaviour, requested SPNs and encryption types together.

## Kerberos security review

Check:

- Accounts with unnecessary SPNs.
- Service accounts with excessive privileges.
- Weak or outdated encryption configurations.
- Accounts without pre-authentication.
- Unusual ticket request patterns.
- Service account password management.
- Domain controller time synchronisation.
- Unusual delegation settings.

## Common attack terminology

| Technique | Defensive review focus |
|---|---|
| Kerberoasting | SPN-bearing accounts and password strength |
| AS-REP roasting | Accounts without pre-authentication |
| Pass-the-ticket | Unusual ticket use and endpoint telemetry |
| Golden Ticket | Domain Kerberos trust and KRBTGT protection |
| Silver Ticket | Service account and service-specific trust |
| Delegation abuse | Unnecessary or unsafe delegation configuration |

This page is a defensive reference. Any attack simulation must be explicitly authorised and conducted within the agreed scope.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
