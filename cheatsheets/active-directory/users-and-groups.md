# Active Directory Users and Groups

## User enumeration

```powershell
# All domain users
Get-ADUser -Filter *

# Specific user
Get-ADUser -Identity username

# Selected properties
Get-ADUser username -Properties Description, MemberOf, Enabled, LastLogonDate

# Enabled accounts
Get-ADUser -Filter 'Enabled -eq $true'

# Disabled accounts
Get-ADUser -Filter 'Enabled -eq $false'

# Accounts with descriptions
Get-ADUser -Filter * -Properties Description |
    Select-Object SamAccountName, Description

# Accounts with SPNs
Get-ADUser -Filter 'ServicePrincipalName -like "*"' -Properties ServicePrincipalName

# Accounts that do not require Kerberos pre-authentication
Get-ADUser -Filter 'DoesNotRequirePreAuth -eq $true'

# Accounts with password never expires
Get-ADUser -Filter 'PasswordNeverExpires -eq $true'
```

## Group enumeration

```powershell
# All groups
Get-ADGroup -Filter *

# Specific group
Get-ADGroup -Identity "Domain Admins"

# Group members
Get-ADGroupMember -Identity "Domain Admins"

# Recursive membership
Get-ADGroupMember -Identity "Domain Admins" -Recursive

# Groups for a user
Get-ADPrincipalGroupMembership username

# Groups with privileged names
Get-ADGroup -Filter 'Name -like "*Admin*"'
```

## Privileged groups to review

| Group | Purpose |
|---|---|
| Domain Admins | Domain-wide administrative privileges |
| Enterprise Admins | Forest-wide administrative privileges |
| Schema Admins | Schema modification privileges |
| Administrators | Built-in domain administrative group |
| Account Operators | Account management privileges |
| Backup Operators | Backup and restore privileges |
| Server Operators | Server management privileges |
| DnsAdmins | DNS administration |
| Group Policy Creator Owners | GPO creation and management |

Membership and effective privileges should be assessed in context. Nested groups and delegated permissions can change the effective access of an account.

## Account status

```powershell
# Account details
Get-ADUser username -Properties *

# Password last set
Get-ADUser username -Properties PasswordLastSet

# Last logon timestamp
Get-ADUser username -Properties LastLogonDate

# Locked accounts
Search-ADAccount -LockedOut

# Disabled accounts
Search-ADAccount -AccountDisabled

# Expired accounts
Search-ADAccount -AccountExpired

# Password expired
Search-ADAccount -PasswordExpired
```

`LastLogonDate` is based on the replicated `lastLogonTimestamp` attribute and is not an exact real-time logon record.

## Computers

```powershell
# All computers
Get-ADComputer -Filter *

# Enabled computers
Get-ADComputer -Filter 'Enabled -eq $true'

# Operating system inventory
Get-ADComputer -Filter * -Properties OperatingSystem |
    Select-Object Name, OperatingSystem

# Servers
Get-ADComputer -Filter 'OperatingSystem -like "*Server*"' -Properties OperatingSystem

# Computer details
Get-ADComputer COMPUTER01 -Properties *
```

## Password policy

```powershell
# Default domain policy
Get-ADDefaultDomainPasswordPolicy

# Fine-grained policies
Get-ADFineGrainedPasswordPolicy -Filter *

# Resultant policy for a user
Get-ADUserResultantPasswordPolicy username
```

## Review checklist

- [ ] Privileged group membership reviewed.
- [ ] Nested group membership considered.
- [ ] Dormant accounts identified.
- [ ] Disabled accounts reviewed.
- [ ] Service accounts identified.
- [ ] Accounts with SPNs reviewed.
- [ ] Password policy assessed.
- [ ] Unusual account flags investigated.
- [ ] Excessive permissions identified.
- [ ] Findings validated with directory owners.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
