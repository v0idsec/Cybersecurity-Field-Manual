# Phishing Infrastructure and Indicators

## Overview

Phishing infrastructure analysis identifies technical indicators associated with suspicious email campaigns and helps defenders detect, investigate and disrupt malicious activity.

This guide focuses on defensive identification and intelligence handling.

## Common Infrastructure

Phishing campaigns may use:

- Registered domains
- Compromised websites
- Cloud hosting
- Redirect services
- URL shorteners
- Email delivery services
- Disposable infrastructure
- Legitimate compromised accounts
- Lookalike domains

Infrastructure alone does not establish malicious intent.

## Indicator Types

| Indicator | Example |
|---|---|
| Sender address | `billing@example.invalid` |
| Domain | `example.invalid` |
| URL | `hxxps://example[.]invalid/login` |
| IP address | `192.0.2.10` |
| File hash | SHA-256 value |
| Message ID | Email message identifier |
| Certificate | Certificate fingerprint |
| Attachment name | Suspicious filename |

The examples use reserved or defanged values.

## Domain Analysis

Investigate:
- Registration date
- Registrar
- Name servers
- DNS records
- Hosting provider
- Certificate information
- Historical resolutions
- Related domains

A newly registered domain may warrant investigation but is not proof of phishing.

## DNS Records

Useful record types:

| Type | Purpose |
|---|---|
| A | IPv4 address |
| AAAA | IPv6 address |
| MX | Mail exchange |
| NS | Name server |
| TXT | Text records, including SPF |
| CNAME | Alias record |

Example lookup:

```bash
dig example.com A
```

```bash
dig example.com MX
```

```bash
dig example.com TXT
```

Only investigate domains within approved scope or through passive intelligence sources.

## Certificate Transparency

Certificate transparency records can reveal certificates issued for domains.

Useful sources include:
- crt.sh
- Certificate Transparency search services

Investigate:
- Newly observed domains
- Lookalike names
- Related subdomains
- Certificate issuance times

Certificate issuance does not prove a domain is malicious.

## IP and Hosting Analysis

Review:
- ASN
- Hosting provider
- Geolocation
- Reverse DNS
- Historical resolution
- Reputation
- Related infrastructure

Shared hosting and cloud platforms can host legitimate and malicious services simultaneously.

Avoid broad IP blocking without assessing collateral impact.

## Threat Intelligence Sources

Common resources:

- VirusTotal
- URLhaus
- PhishTank
- OpenPhish
- Spamhaus
- Cisco Talos Intelligence
- AbuseIPDB
- urlscan.io

Consider:
- Data freshness
- Source reliability
- Confidence
- False positives
- Sharing restrictions
- Privacy implications

## IOC Management

For each indicator, record:

- Indicator
- Type
- Source
- First observed
- Last observed
- Confidence
- Context
- Associated campaign
- Expiry or review date
- Action taken

Do not retain indicators indefinitely without review.

## Detection Opportunities

Potential detection opportunities include:

- Newly registered lookalike domains
- Suspicious URL destinations
- Unexpected external forwarding
- Unusual sender infrastructure
- Repeated attachment hashes
- Similar messages across multiple users
- Authentication anomalies
- Mailbox rule changes

Correlate multiple indicators to reduce false positives.

## Example: IOC Record

```text
Indicator:
Type:
Source:
First observed:
Last observed:
Confidence:
Associated messages:
Affected users:
Related infrastructure:
Detection rule:
Blocking decision:
Expiry/review date:
Analyst notes:
```

## Safe Handling

- Defang URLs in reports.
- Avoid browsing suspicious infrastructure from production systems.
- Do not submit sensitive information to public services.
- Validate indicators before blocking.
- Preserve original evidence.
- Document intelligence source and collection time.

## Common Mistakes

- Treating reputation scores as definitive.
- Blocking shared hosting infrastructure broadly.
- Ignoring indicator age.
- Failing to record source confidence.
- Treating certificate issuance as proof of compromise.
- Sharing confidential indicators publicly.
- Failing to review expired indicators.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
