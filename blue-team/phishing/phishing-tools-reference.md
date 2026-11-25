# Phishing Tools Reference

## Overview

This reference lists tools and services useful for defensive phishing analysis, email investigation, URL analysis and incident response.

Use approved tools and follow organisational data-handling requirements.

## Email Analysis

| Tool | Purpose |
|---|---|
| Microsoft Defender for Office 365 | Email threat investigation |
| Microsoft Exchange message trace | Mail delivery investigation |
| Google Admin investigation tools | Gmail investigation |
| MXToolbox | Email and DNS diagnostics |
| Google Admin Toolbox Messageheader | Header analysis |
| Microsoft Remote Connectivity Analyzer | Mail configuration diagnostics |

## URL and Domain Analysis

| Tool | Purpose |
|---|---|
| VirusTotal | File and URL reputation |
| URLhaus | Malware URL intelligence |
| PhishTank | Phishing URL intelligence |
| OpenPhish | Phishing intelligence |
| urlscan.io | Website and URL analysis |
| crt.sh | Certificate transparency search |
| WHOIS/RDAP services | Domain registration information |
| DNS tools | DNS record investigation |

## Attachment Analysis

| Tool | Purpose |
|---|---|
| oletools | Office document inspection |
| olevba | VBA macro analysis |
| Mandiant capa | Capability detection |
| Detect It Easy | File identification |
| YARA | Pattern-based file analysis |
| 7-Zip | Archive inspection |
| ExifTool | Metadata examination |
| VirusTotal | File reputation and analysis |

## Email Authentication

Useful tools and references:

- SPF record lookup
- DKIM record lookup
- DMARC record lookup
- Google Admin Toolbox
- MXToolbox

Authentication results should be interpreted alongside the full message context.

## Threat Intelligence

| Source | Purpose |
|---|---|
| VirusTotal | Multi-source reputation |
| AbuseIPDB | IP reputation |
| Spamhaus | Spam and abuse intelligence |
| Cisco Talos | Reputation and threat intelligence |
| URLhaus | Malware URL intelligence |
| PhishTank | Phishing reports |
| OpenPhish | Phishing intelligence |

## Microsoft 365 Investigation

Common capabilities:

- Message trace
- Threat Explorer
- Quarantine
- Email entity investigation
- Advanced hunting
- Audit logs
- Mailbox audit
- Identity sign-in logs

Availability depends on licensing, permissions and configuration.

## Google Workspace Investigation

Potential capabilities:

- Email Log Search
- Security investigation tools
- Gmail audit logs
- Login audit logs
- OAuth application review
- Alert centre

Availability depends on edition and configuration.

## Command-Line Reference

Hash a suspicious attachment:

```bash
sha256sum attachment
```

Identify a file:

```bash
file attachment
```

Inspect an email header:

```bash
grep -Ei \
'^(From|To|Reply-To|Return-Path|Received|Authentication-Results):' \
message.eml
```

Inspect DNS:

```bash
dig example.com MX
```

## Tool Selection

Consider:

- Data privacy
- Licensing
- Evidence retention
- Supported file types
- False-positive rates
- Analysis environment
- Tool version
- Auditability
- Reproducibility

## Operational Warning

Public analysis services may retain submitted files, URLs or metadata.

Never submit confidential business documents, personal information or sensitive incident evidence without approval.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
