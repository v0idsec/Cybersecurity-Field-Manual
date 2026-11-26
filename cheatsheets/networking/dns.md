# DNS Cheatsheet

Quick-reference commands for DNS records, queries, troubleshooting and security assessment.

## What is DNS?

The Domain Name System translates domain names into records used by network clients and services.

Example:

```text
example.com → 192.0.2.10
```

## Common DNS record types

| Record | Purpose |
|---|---|
| A | IPv4 address |
| AAAA | IPv6 address |
| CNAME | Canonical name / alias |
| MX | Mail exchange |
| NS | Authoritative name server |
| TXT | Text records |
| PTR | Reverse DNS lookup |
| SOA | Start of Authority |
| SRV | Service location |
| CAA | Permitted certificate authorities |

## DNS lookup commands

### Linux

```bash
dig example.com
```

Query a specific record:

```bash
dig example.com A
dig example.com AAAA
dig example.com MX
dig example.com NS
dig example.com TXT
dig example.com SOA
```

Query a specific DNS server:

```bash
dig @192.0.2.53 example.com
```

Short output:

```bash
dig +short example.com
```

Reverse lookup:

```bash
dig -x 192.0.2.10
```

### Windows

```cmd
nslookup example.com
```

Query a specific record:

```cmd
nslookup -type=MX example.com
nslookup -type=NS example.com
nslookup -type=TXT example.com
```

PowerShell:

```powershell
Resolve-DnsName example.com
Resolve-DnsName example.com -Type MX
Resolve-DnsName example.com -Type TXT
Resolve-DnsName example.com -Type SOA
```

## DNS server information

Find authoritative name servers:

```bash
dig NS example.com
```

Query SOA:

```bash
dig SOA example.com
```

Query a specific authoritative server:

```bash
dig @ns1.example.com example.com SOA
```

## Reverse DNS

Reverse DNS maps an IP address back to a hostname using PTR records.

Example:

```bash
dig -x 192.0.2.10
```

## DNS troubleshooting

Check resolver configuration:

```bash
cat /etc/resolv.conf
```

Windows:

```cmd
ipconfig /all
```

Test a DNS server:

```bash
dig @192.0.2.53 example.com
```

Check DNS over TCP:

```bash
dig +tcp example.com
```

Compare answers from multiple resolvers:

```bash
dig @1.1.1.1 example.com
dig @8.8.8.8 example.com
```

## DNS enumeration

For authorised assessments, identify:

- Public DNS records.
- Mail exchange records.
- Name servers.
- Service records.
- Certificate Authority Authorisation records.
- Subdomains from approved passive sources.
- DNS configuration errors.
- Unintended information disclosure.

Example DNS record collection:

```bash
for record in A AAAA MX NS TXT SOA CAA; do
    echo "### $record"
    dig +short example.com "$record"
done
```

## Zone transfers

DNS zone transfers replicate zone information between DNS servers.

A misconfigured server may allow unauthorised transfers.

Test only against authorised DNS infrastructure:

```bash
dig AXFR example.com @ns1.example.com
```

A successful transfer may expose internal hostnames and infrastructure information.

## DNS security concepts

| Concept | Purpose |
|---|---|
| DNSSEC | DNS data origin authentication and integrity |
| DoH | DNS over HTTPS |
| DoT | DNS over TLS |
| Split-horizon DNS | Different answers for different network contexts |
| DNS filtering | Blocking or redirecting malicious domains |
| RPZ | Response Policy Zone for DNS filtering |

## Security review checklist

- [ ] Review authoritative name servers.
- [ ] Check for unintended zone transfers.
- [ ] Review DNSSEC configuration.
- [ ] Review stale DNS records.
- [ ] Identify exposed internal hostnames.
- [ ] Review TXT records for sensitive disclosures.
- [ ] Check CAA records.
- [ ] Review DNS logging and monitoring.
- [ ] Investigate unexpected DNS tunnelling patterns.
- [ ] Review resolver access controls.

## Important notes

- DNS responses can be cached.
- Different resolvers may return different answers.
- DNS does not prove that a service is reachable.
- A failed lookup may be caused by resolver configuration rather than a missing record.
- Do not attempt zone transfers against systems outside your approved scope.

---

*Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
