# Windows Domain Troubleshooting

## DNS troubleshooting

```powershell
# Current DNS servers
Get-DnsClientServerAddress

# Resolve domain
Resolve-DnsName domain.local

# Find domain controllers
Resolve-DnsName _ldap._tcp.dc._msdcs.domain.local -Type SRV

# Clear DNS cache
Clear-DnsClientCache

# Test DNS server connectivity
Test-NetConnection dc01.domain.local -Port 53
```

## Domain controller discovery

```cmd
:: Discover a domain controller
nltest /dsgetdc:domain.local

:: List domain controllers
nltest /dclist:domain.local

:: Verify domain secure channel
nltest /sc_verify:domain.local

:: Display domain trusts
nltest /domain_trusts
```

## Secure channel troubleshooting

```powershell
# Test secure channel
Test-ComputerSecureChannel -Verbose

# Test using a specified domain controller
Test-ComputerSecureChannel -Server dc01.domain.local -Verbose

# Repair secure channel (requires suitable privileges)
Test-ComputerSecureChannel -Repair -Credential (Get-Credential)
```

Do not repair a secure channel until the failure has been investigated and the change is approved.

## Time synchronisation

Kerberos authentication is sensitive to time differences between systems.

```cmd
:: Display current time configuration
w32tm /query /status

:: Display time source
w32tm /query /source

:: Display configuration
w32tm /query /configuration

:: Check time against a domain controller
w32tm /stripchart /computer:dc01.domain.local /samples:5 /dataonly
```

## Replication

```cmd
:: Replication summary
repadmin /replsummary

:: Show replication partners
repadmin /showrepl

:: Display replication queue
repadmin /queue

:: Display domain controller diagnostics
dcdiag

:: DNS diagnostics
dcdiag /test:dns
```

## Common ports

| Port | Protocol | Purpose |
|---|---|---|
| 53 | TCP/UDP | DNS |
| 88 | TCP/UDP | Kerberos |
| 135 | TCP | RPC endpoint mapper |
| 389 | TCP/UDP | LDAP |
| 445 | TCP | SMB |
| 464 | TCP/UDP | Kerberos password change |
| 636 | TCP | LDAPS |
| 3268 | TCP | Global Catalog |
| 3269 | TCP | Global Catalog over TLS |
| 9389 | TCP | Active Directory Web Services |
| 49152–65535 | TCP | Dynamic RPC range, commonly used by modern Windows |

Actual port requirements depend on the services, operating system versions and network configuration.

## Connectivity checks

```powershell
# DNS
Test-NetConnection dc01.domain.local -Port 53

# Kerberos
Test-NetConnection dc01.domain.local -Port 88

# LDAP
Test-NetConnection dc01.domain.local -Port 389

# SMB
Test-NetConnection dc01.domain.local -Port 445

# LDAPS
Test-NetConnection dc01.domain.local -Port 636

# Global Catalog
Test-NetConnection dc01.domain.local -Port 3268
```

## Troubleshooting checklist

- [ ] Client has the expected IP configuration.
- [ ] DNS servers point to the correct infrastructure.
- [ ] Domain controller SRV records resolve.
- [ ] Client can reach required domain controller ports.
- [ ] System time is synchronised.
- [ ] Kerberos tickets are valid.
- [ ] Secure channel is healthy.
- [ ] Domain controller replication is healthy.
- [ ] Relevant Windows event logs have been reviewed.
- [ ] Changes are documented and approved.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
