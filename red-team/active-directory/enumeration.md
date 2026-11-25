
# Active Directory Enumeration

> Professional reference guide for discovering Active Directory structure, identities, infrastructure, relationships and security configuration.

## Contents

- [Overview](#overview)
- [Enumeration Objectives](#enumeration-objectives)
- [Domain and Forest Discovery](#domain-and-forest-discovery)
- [Users and Groups](#users-and-groups)
- [Computer Objects](#computer-objects)
- [Group Policy](#group-policy)
- [Trust Relationships](#trust-relationships)
- [Service Accounts](#service-accounts)
- [LDAP Enumeration](#ldap-enumeration)
- [PowerShell Reference](#powershell-reference)
- [Assessment Methodology](#assessment-methodology)
- [Common Findings](#common-findings)
- [Evidence Collection](#evidence-collection)
- [Tools and References](#tools-and-references)
- [Assessment Checklist](#assessment-checklist)

---

## Overview

Active Directory enumeration is the process of collecting information about a directory environment to understand its structure, identities, permissions and potential attack paths.

Enumeration may be conducted from:

- An unauthenticated network position.
- A domain-joined workstation.
- A standard domain user account.
- A privileged administrative account.
- An assessment workstation with approved directory access.

The available information and visibility will differ depending on the access level.

## Enumeration Objectives

Identify:

- Forests and domains.
- Domain controllers.
- Domain functional levels.
- Users and groups.
- Privileged memberships.
- Computers and servers.
- Group Policy Objects.
- Organisational Units.
- Trust relationships.
- Service accounts.
- Delegation configuration.
- Password and account policies.
- Certificate services.
- Exposed administrative interfaces.

## Domain and Forest Discovery

Establish the domain context and directory architecture.

### Windows Commands

```powershell
# Current domain context
$env:USERDOMAIN
$env:USERDNSDOMAIN
whoami /all

# Domain information
Get-ADDomain

# Forest information
Get-ADForest

# Domain controllers
Get-ADDomainController -Filter *

# Domain trusts
Get-ADTrust -Filter *
```

### DNS Discovery

Active Directory relies heavily on DNS.

Review:

- Domain DNS records.
- Domain controller hostnames.
- LDAP service records.
- Kerberos service records.
- Global Catalog records.

```powershell
# Locate domain controllers
nltest /dclist:$env:USERDNSDOMAIN

# Discover LDAP service records
nslookup -type=SRV _ldap._tcp.dc._msdcs.example.local

# Discover Kerberos service records
nslookup -type=SRV _kerberos._tcp.example.local
```

Replace example domains with authorised assessment targets.

## Users and Groups

User and group enumeration helps identify privilege relationships and potential attack paths.

### User Attributes

Review:

- `sAMAccountName`
- `userPrincipalName`
- `displayName`
- `description`
- `memberOf`
- `adminCount`
- `lastLogon`
- `lastLogonTimestamp`
- `pwdLastSet`
- `userAccountControl`
- `servicePrincipalName`

Example:

```powershell
Get-ADUser -Filter * -Properties `
    DisplayName,Description,MemberOf,LastLogonDate,`
    PasswordLastSet,ServicePrincipalName,Enabled
```

### Group Enumeration

```powershell
# Domain groups
Get-ADGroup -Filter *

# Members of a group
Get-ADGroupMember -Identity "Domain Admins"

# Recursive group membership
Get-ADGroupMember -Identity "Domain Admins" -Recursive

# Privileged group membership
Get-ADGroupMember -Identity "Enterprise Admins"
Get-ADGroupMember -Identity "Schema Admins"
Get-ADGroupMember -Identity "Administrators"
```

Review nested groups and indirect membership, not only direct assignments.

### High-Value Groups

Investigate membership of:

- Domain Admins.
- Enterprise Admins.
- Schema Admins.
- Administrators.
- Account Operators.
- Server Operators.
- Backup Operators.
- DNSAdmins.
- Group Policy Creator Owners.
- Protected Users.

Group names and privileges can vary by domain configuration.

## Computer Objects

Identify domain-joined systems and their roles.

```powershell
Get-ADComputer -Filter * -Properties `
    OperatingSystem,OperatingSystemVersion,`
    LastLogonDate,ServicePrincipalName,Description
```

Prioritise:

- Domain controllers.
- File servers.
- Database servers.
- Application servers.
- Management workstations.
- Backup infrastructure.
- Certificate authorities.
- Privileged access workstations.
- Legacy operating systems.

Review stale computer accounts and systems with outdated operating systems.

## Group Policy

Group Policy can enforce security settings across domain systems.

Enumerate:

```powershell
Get-GPO -All
```

Review:

- Password and account policies.
- User rights assignments.
- Local administrator membership.
- Windows Defender configuration.
- Firewall rules.
- Audit policies.
- Credential protection settings.
- Restricted groups.
- Startup and logon scripts.
- Software deployment settings.

Assess who can modify each GPO and which organisational units it affects.

A GPO linked to a privileged server or domain controller may have significant security implications.

## Trust Relationships

Trust relationships connect domains and forests.

Enumerate:

```powershell
Get-ADTrust -Filter *
nltest /domain_trusts
```

Review:

- Trust direction.
- Trust type.
- Transitivity.
- Forest trusts.
- External trusts.
- Selective authentication.
- SID filtering.
- Privileged access across trust boundaries.

Do not assume that a trust automatically grants access to the trusted domain.

## Service Accounts

Identify accounts associated with services.

Review:

- Service Principal Names.
- Group Managed Service Accounts.
- Managed Service Accounts.
- Legacy service accounts.
- Password rotation practices.
- Privileged group membership.
- Interactive logon permissions.

```powershell
Get-ADUser -Filter * -Properties ServicePrincipalName |
    Where-Object {$_.ServicePrincipalName}
```

Pay attention to service accounts with:

- Excessive privileges.
- Long-lived passwords.
- Weak password policies.
- Unnecessary interactive logon.
- Broad resource access.

## LDAP Enumeration

LDAP provides access to directory objects and attributes.

Common directory search concepts include:

| Component | Purpose |
|---|---|
| Base DN | Starting directory location |
| Search scope | Base, one-level or subtree |
| Filter | Selects matching objects |
| Attributes | Specifies returned properties |

Example filter concepts:

```text
(objectClass=user)
(objectCategory=person)
(&(objectCategory=person)(objectClass=user))
(servicePrincipalName=*)
(adminCount=1)
```

Investigate LDAP signing and channel binding requirements, anonymous access, and whether directory information is exposed beyond intended trust boundaries.

## PowerShell Reference

```powershell
# Current identity and group memberships
whoami /all

# Domain information
Get-ADDomain

# Forest information
Get-ADForest

# Domain controllers
Get-ADDomainController -Filter *

# All users
Get-ADUser -Filter *

# All computers
Get-ADComputer -Filter *

# All groups
Get-ADGroup -Filter *

# Group members
Get-ADGroupMember -Identity "Domain Admins" -Recursive

# Service Principal Names
Get-ADUser -Filter * -Properties ServicePrincipalName

# Group Policy Objects
Get-GPO -All

# Trust relationships
Get-ADTrust -Filter *
```

## Assessment Methodology

1. Establish the current identity and access level.
2. Identify the forest and domain structure.
3. Locate domain controllers.
4. Enumerate users and groups.
5. Identify privileged memberships.
6. Enumerate computer objects.
7. Review Group Policy.
8. Identify service accounts.
9. Map trust relationships.
10. Identify delegation and certificate services.
11. Correlate findings into potential attack paths.
12. Validate findings within the agreed scope.

## Common Findings

| Finding | Security significance |
|---|---|
| Excessive privileged group membership | Unnecessary administrative access |
| Stale accounts | Unmanaged identity exposure |
| Weak service account management | Credential compromise risk |
| Excessive GPO permissions | Potential privilege escalation |
| Legacy systems | Increased attack surface |
| Insecure trust configuration | Cross-domain exposure |
| Sensitive descriptions | Information disclosure |
| Unrestricted LDAP exposure | Excessive directory visibility |

## Evidence Collection

Record:

- Domain and forest names.
- Domain controller details.
- Enumeration identity and privileges.
- Relevant user and group objects.
- GPO configuration and permissions.
- Trust configuration.
- Service account details.
- Relevant timestamps.
- Security impact.
- Reproduction and validation steps.

Redact credentials, hashes and sensitive personal information.

## Tools and References

- Active Directory PowerShell module.
- LDAP utilities.
- BloodHound / SharpHound.
- NetExec.
- Impacket.
- PowerView.
- PingCastle.
- Purple Knight.
- Microsoft AD DS documentation.

## Assessment Checklist

- [ ] Forest and domain structure identified.
- [ ] Domain controllers enumerated.
- [ ] Users and groups reviewed.
- [ ] Privileged memberships identified.
- [ ] Nested group membership assessed.
- [ ] Computer objects reviewed.
- [ ] Group Policy configuration assessed.
- [ ] GPO permissions reviewed.
- [ ] Trust relationships mapped.
- [ ] Service accounts identified.
- [ ] Delegation and AD CS presence investigated.
- [ ] Findings correlated with attack paths.
- [ ] Evidence securely retained.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
