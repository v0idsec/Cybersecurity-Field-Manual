# Active Directory Domain Enumeration

## Domain information

```powershell
# Import AD module
Import-Module ActiveDirectory

# Current domain
Get-ADDomain

# Current forest
Get-ADForest

# Domain SID
(Get-ADDomain).DomainSID

# Domain functional level
(Get-ADDomain).DomainMode

# Domain controllers
Get-ADDomainController -Filter *

# Discover a domain controller
Get-ADDomainController -Discover
```

## Domain and forest relationships

```powershell
# Forest domains
(Get-ADForest).Domains

# Forest trusts
Get-ADTrust -Filter *

# Domain trusts
Get-ADTrust -Filter * -Server (Get-ADDomain).DNSRoot

# Domain sites
Get-ADReplicationSite -Filter *

# Subnets
Get-ADReplicationSubnet -Filter *
```

## Native Windows enumeration

```cmd
:: Domain information
systeminfo

:: Current domain
echo %USERDOMAIN%

:: Current logon server
echo %LOGONSERVER%

:: Domain controller discovery
nltest /dsgetdc:domain.local

:: List domain controllers
nltest /dclist:domain.local

:: Domain trusts
nltest /domain_trusts

:: Current user and groups
whoami /all

:: Domain group information
net group /domain

:: Domain user information
net user /domain

:: Domain computer information
net view /domain
```

## Domain controller discovery through DNS

```powershell
# LDAP service records
Resolve-DnsName _ldap._tcp.dc._msdcs.domain.local -Type SRV

# Kerberos service records
Resolve-DnsName _kerberos._tcp.domain.local -Type SRV

# Global catalog records
Resolve-DnsName _gc._tcp.domain.local -Type SRV
```

## Domain controller health

```cmd
:: Domain controller diagnostics
dcdiag

:: DNS diagnostics
dcdiag /test:dns

:: Replication summary
repadmin /replsummary

:: Replication status
repadmin /showrepl

:: Replication queue
repadmin /queue
```

These commands may require additional privileges and are primarily intended for domain administration.

## Domain enumeration checklist

- [ ] Domain name and SID recorded.
- [ ] Forest name and functional level identified.
- [ ] Domain controllers identified.
- [ ] DNS configuration reviewed.
- [ ] Trust relationships documented.
- [ ] Sites and subnets identified.
- [ ] Domain functional level recorded.
- [ ] Replication health reviewed.
- [ ] Privileged groups identified.
- [ ] Domain policy configuration reviewed.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
