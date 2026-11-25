# Domain and Infrastructure Reconnaissance

## Overview

Domain and infrastructure reconnaissance identifies an organisation's publicly visible domains, DNS configuration, network relationships and external infrastructure.

The objective is to develop an accurate picture of the organisation's external footprint and identify assets that may warrant further assessment.

## 1. Domain Registration

WHOIS and RDAP services can provide information about domain registration.

Useful information may include:
- Registrar.
- Registration and expiry dates.
- Nameservers.
- Domain status.
- Registration organisation, where disclosed.
- Abuse contact information.

Privacy protection and registry policies may hide registrant information.

### Useful Resources

- ICANN Lookup: https://lookup.icann.org/
- RDAP: https://www.rdap.org/
- WhoisXML API: https://whoisxmlapi.com/

### Command-Line Reference

```bash
whois example.com
```

RDAP can also be queried through a registry or provider's supported endpoint.

Do not treat registration information as proof of current operational ownership.

## 2. DNS Enumeration

DNS records can reveal infrastructure, service providers and domain relationships.

Common record types:

| Record | Purpose |
|---|---|
| A | IPv4 address |
| AAAA | IPv6 address |
| CNAME | Canonical name / alias |
| MX | Mail exchange |
| NS | Authoritative nameserver |
| TXT | Text records, verification and email policies |
| SOA | Zone authority information |
| PTR | Reverse DNS |
| SRV | Service location |

### DNS Queries

```bash
dig example.com
dig example.com A
dig example.com AAAA
dig example.com MX
dig example.com NS
dig example.com TXT
dig example.com SOA
```

Query a specific resolver:

```bash
dig @1.1.1.1 example.com
```

Reverse DNS lookup:

```bash
dig -x 203.0.113.10
```

Using `nslookup`:

```bash
nslookup example.com
nslookup -type=mx example.com
nslookup -type=txt example.com
```

### SPF, DKIM and DMARC

Email-related DNS records can provide insight into an organisation's email security configuration.

SPF:

```bash
dig TXT example.com
```

DMARC:

```bash
dig TXT _dmarc.example.com
```

DKIM records require the relevant selector:

```bash
dig TXT selector1._domainkey.example.com
```

Review:
- SPF policy strength.
- DMARC policy and reporting configuration.
- DKIM selector exposure.
- Third-party email providers.
- Unnecessary or outdated DNS records.

Do not assume a missing record means email is insecure without considering the organisation's architecture.

## 3. Subdomain Discovery

Subdomains can expose additional applications, development environments, administrative interfaces and forgotten infrastructure.

Common sources:
- Certificate transparency.
- Search engines.
- Public DNS datasets.
- Passive DNS services.
- Public code repositories.
- Commercial attack-surface platforms.

### Certificate Transparency

Certificates can reveal hostnames included in certificate subject names and Subject Alternative Names.

Useful sources:
- https://crt.sh/
- https://transparencyreport.google.com/https/certificates

Example:

```bash
curl -s 'https://crt.sh/?q=%25.example.com&output=json'
```

Certificate entries are historical leads, not proof that a hostname is currently live.

### Amass

Passive enumeration:

```bash
amass enum -passive -d example.com
```

Save results:

```bash
amass enum -passive -d example.com -o amass-results.txt
```

### theHarvester

```bash
theHarvester -d example.com -b all
```

Available data sources depend on the installed version and configured integrations.

## 4. Infrastructure Mapping

Once domains and hostnames are identified, correlate them with public infrastructure information.

Investigate:
- IP addresses.
- ASN ownership.
- Hosting providers.
- CDN providers.
- Cloud providers.
- Reverse DNS.
- Certificate history.
- Related domains.

Useful resources:
- https://bgp.he.net/
- https://ipinfo.io/
- https://viewdns.info/
- https://securitytrails.com/

### ASN and Network Ownership

An IP address may belong to:
- The organisation.
- A cloud provider.
- A CDN.
- A managed service provider.
- Shared hosting infrastructure.

Do not assume that every IP resolving from an organisation's domain is owned or controlled by that organisation.

## 5. Passive DNS

Passive DNS datasets provide historical observations of DNS relationships.

They can help identify:
- Historical IP addresses.
- Previously used subdomains.
- Infrastructure changes.
- Potentially forgotten services.
- Domain relationships.

Historical observations should be labelled with their observation dates.

## 6. Validation

Before reporting a discovered asset, establish:

- Does the hostname currently resolve?
- Is the domain within scope?
- Does the asset appear to belong to the organisation?
- Is it hosted by a third party?
- Is the observation current?
- Is the service accessible?
- Has the asset already been decommissioned?

Do not perform active service testing unless authorised.

## 7. Reporting

Useful output includes:
- Domain inventory.
- Subdomain inventory.
- DNS configuration summary.
- Certificate observations.
- Public IP and ASN relationships.
- Hosting and service-provider relationships.
- Potentially exposed assets.
- Confidence and validation notes.

## Operational Considerations

DNS enumeration is generally low impact, but active scanning and direct service interaction require separate consideration.

Cloud, CDN and shared hosting infrastructure may belong to third parties. Confirm scope before testing those systems.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
