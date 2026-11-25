# PowerView Reference

## Overview

PowerView is a PowerShell tool from the PowerSploit project used for Active Directory enumeration and domain analysis.

It is commonly used in authorised penetration testing and security assessments.

Repository:

https://github.com/PowerShellMafia/PowerSploit

PowerView is dual-use security tooling. Obtain and review the source from its official repository before using it.

## Loading PowerView

If PowerView is already available in an approved assessment environment:

```powershell
Import-Module .\PowerView.ps1
```

Some distributions expose functions through dot-sourcing:

```powershell
. .\PowerView.ps1
```

## Domain enumeration

```powershell
# Domain information
Get-Domain

# Domain controller information
Get-DomainController

# Domain policy
Get-DomainPolicy

# Domain trusts
Get-DomainTrust

# Forest information
Get-Forest
```

## User enumeration

```powershell
# List domain users
Get-DomainUser

# Specific user
Get-DomainUser -Identity username

# User descriptions
Get-DomainUser -Properties description

# Users with SPNs
Get-DomainUser -SPN

# Users without Kerberos pre-authentication
Get-DomainUser -PreauthNotRequired
```

## Group enumeration

```powershell
# List domain groups
Get-DomainGroup

# Specific group
Get-DomainGroup -Identity "Domain Admins"

# Group members
Get-DomainGroupMember -Identity "Domain Admins"

# Recursive group membership
Get-DomainGroupMember -Identity "Domain Admins" -Recurse
```

## Computer enumeration

```powershell
# List computers
Get-DomainComputer

# Operating system information
Get-DomainComputer -Properties dnshostname, operatingsystem

# Domain controllers
Get-DomainController
```

## Object and ACL review

```powershell
# Domain object ACLs
Get-DomainObjectAcl -Identity "Domain Admins"

# ACLs for a specific user
Get-DomainObjectAcl -Identity username

# Find interesting domain objects
Find-InterestingDomainAcl
```

ACL enumeration can return substantial data. Narrow queries and validate effective permissions before reporting an issue.

## Shares and sessions

```powershell
# Find domain shares
Find-DomainShare

# Find active sessions
Get-NetSession

# Find logged-on users
Get-NetLoggedon
```

Remote session and logged-on user queries depend on host permissions, firewall settings and remote service availability.

## Useful discovery functions

| Function | Purpose |
|---|---|
| `Get-Domain` | Domain details |
| `Get-Forest` | Forest details |
| `Get-DomainController` | Domain controller discovery |
| `Get-DomainUser` | User enumeration |
| `Get-DomainGroup` | Group enumeration |
| `Get-DomainGroupMember` | Group membership |
| `Get-DomainComputer` | Computer enumeration |
| `Get-DomainTrust` | Trust enumeration |
| `Get-DomainObjectAcl` | Directory ACL inspection |
| `Find-InterestingDomainAcl` | Identify potentially interesting ACLs |
| `Find-DomainShare` | Share discovery |

## Operational considerations

- Review the source before execution.
- Use a controlled assessment environment.
- Confirm the tool version and available functions.
- Avoid unnecessary remote enumeration.
- Record the identity used for collection.
- Protect collected directory information.
- Validate findings with native AD tools.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
