# Windows Active Directory Commands

## Domain discovery

```powershell
# Current domain
$env:USERDOMAIN

# Domain controller used for logon
$env:LOGONSERVER

# Domain information
Get-CimInstance Win32_ComputerSystem |
    Select-Object Name, Domain, PartOfDomain

# Find domain controller
nltest /dsgetdc:domain.local

# Discover domain controllers
nltest /dclist:domain.local

# Current domain trust information
nltest /domain_trusts
```

## Active Directory PowerShell module

The Active Directory module is commonly available on domain controllers and systems with the relevant Remote Server Administration Tools (RSAT) installed.

```powershell
# Import module
Import-Module ActiveDirectory

# Domain information
Get-ADDomain

# Forest information
Get-ADForest

# Domain controllers
Get-ADDomainController -Filter *

# Current domain
Get-ADDomainController -Discover
```

## User enumeration

```powershell
# List users
Get-ADUser -Filter *

# Find a specific user
Get-ADUser -Identity username

# Display useful user properties
Get-ADUser -Identity username -Properties *

# Enabled users
Get-ADUser -Filter 'Enabled -eq $true'

# Disabled users
Get-ADUser -Filter 'Enabled -eq $false'

# Search users by name
Get-ADUser -Filter 'Name -like "*admin*"'

# Find users with descriptions
Get-ADUser -Filter * -Properties Description |
    Select-Object SamAccountName, Description
```

## Group enumeration

```powershell
# List groups
Get-ADGroup -Filter *

# Find group members
Get-ADGroupMember -Identity "Domain Admins"

# Recursive group membership
Get-ADGroupMember -Identity "Domain Admins" -Recursive

# Find groups for a user
Get-ADPrincipalGroupMembership username

# Find privileged group membership
Get-ADGroupMember -Identity "Enterprise Admins"
```

## Computer enumeration

```powershell
# List domain computers
Get-ADComputer -Filter *

# Computer details
Get-ADComputer -Identity COMPUTER01 -Properties *

# Enabled computers
Get-ADComputer -Filter 'Enabled -eq $true'

# Find operating system information
Get-ADComputer -Filter * -Properties OperatingSystem |
    Select-Object Name, OperatingSystem
```

## Password and account policy

```powershell
# Default domain password policy
Get-ADDefaultDomainPasswordPolicy

# Fine-grained password policies
Get-ADFineGrainedPasswordPolicy -Filter *

# Resultant password policy for a user
Get-ADUserResultantPasswordPolicy username

# Account details
Get-ADUser username -Properties PasswordLastSet, LastLogonDate, Enabled, LockedOut
```

## Kerberos and authentication

```powershell
# List Kerberos tickets
klist

# Purge current user's Kerberos tickets
klist purge

# Request service ticket for current logon session
klist get cifs/server.domain.local

# Display current logon information
whoami /all
```

Use ticket-purging commands cautiously because they can disrupt active sessions and authentication workflows.

## LDAP and domain discovery

```powershell
# Domain controller discovery
nltest /dsgetdc:domain.local

# Domain trust enumeration
nltest /domain_trusts

# Query domain information
Get-ADDomain

# Search users by LDAP filter
Get-ADUser -LDAPFilter "(objectCategory=person)"

# Search computers by LDAP filter
Get-ADComputer -LDAPFilter "(objectCategory=computer)"
```

## Useful AD attributes

| Attribute | Description |
|---|---|
| `sAMAccountName` | Legacy-compatible account name |
| `userPrincipalName` | User principal name |
| `distinguishedName` | LDAP distinguished name |
| `memberOf` | Direct group membership |
| `servicePrincipalName` | Service principal names |
| `adminCount` | Protected account indicator, with limitations |
| `lastLogonTimestamp` | Replicated approximate logon timestamp |
| `pwdLastSet` | Password last-set timestamp |
| `userAccountControl` | Account control flags |
| `description` | Object description |

## Troubleshooting

```powershell
# Test domain secure channel
Test-ComputerSecureChannel -Verbose

# Repair secure channel (requires appropriate authority)
Test-ComputerSecureChannel -Repair -Credential (Get-Credential)

# Check domain controller connectivity
nltest /sc_verify:domain.local

# Show current Kerberos tickets
klist

# Check DNS SRV records
Resolve-DnsName _ldap._tcp.dc._msdcs.domain.local -Type SRV
```

## References

- [Active Directory PowerShell](https://learn.microsoft.com/en-us/powershell/module/activedirectory/)
- [Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/)
- [Windows Server Commands](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
