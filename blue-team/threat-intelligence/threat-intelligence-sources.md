# Threat Intelligence Sources

## Overview

Threat intelligence comes from a range of public, commercial and internal sources.

Source selection should be based on relevance, reliability, timeliness and intended use.

## Government and National CERT Sources

| Source | Focus | Website |
|---|---|---|
| Australian Cyber Security Centre | Australian cyber threat advisories | https://www.cyber.gov.au/ |
| CISA | US cybersecurity advisories and alerts | https://www.cisa.gov/ |
| CERT-EU | European Union cyber threat information | https://cert.europa.eu/ |
| NCSC UK | UK cybersecurity guidance and threat information | https://www.ncsc.gov.uk/ |
| CERT NZ | New Zealand cyber security guidance | https://www.cert.govt.nz/ |

## Open Threat Intelligence Platforms

| Platform | Purpose | Website |
|---|---|---|
| AlienVault OTX | Community threat intelligence | https://otx.alienvault.com/ |
| AbuseIPDB | IP reputation and abuse reporting | https://www.abuseipdb.com/ |
| URLhaus | Malicious URL intelligence | https://urlhaus.abuse.ch/ |
| MalwareBazaar | Malware sample intelligence | https://bazaar.abuse.ch/ |
| ThreatFox | IOC sharing | https://threatfox.abuse.ch/ |
| VirusTotal | File, URL, domain and IP analysis | https://www.virustotal.com/ |
| MISP | Threat intelligence sharing platform | https://www.misp-project.org/ |

## Research and Vendor Reporting

Examples include:

- Microsoft Security Blog.
- Google Threat Intelligence.
- Palo Alto Networks Unit 42.
- Cisco Talos.
- CrowdStrike Intelligence.
- Recorded Future research.
- Sophos X-Ops.

Vendor reports can provide useful campaign context, but attribution and conclusions should be assessed critically.

## Internal Sources

Internal sources are often the most relevant.

Examples:

- SIEM alerts.
- EDR detections.
- Firewall logs.
- Proxy logs.
- DNS telemetry.
- Email security alerts.
- Incident reports.
- Vulnerability assessments.
- Previous threat hunts.

## Source Evaluation

Assess each source using:

| Factor | Question |
|---|---|
| Reliability | Is the source generally trustworthy? |
| Accuracy | Can claims be corroborated? |
| Timeliness | Is the information current? |
| Relevance | Does it relate to our environment? |
| Transparency | Is supporting evidence provided? |
| Licensing | Are we permitted to use and redistribute the data? |

## Safe Use of Public Intelligence

- Do not upload confidential files to public analysis services without approval.
- Review service privacy and retention policies.
- Avoid exposing internal IPs, hostnames or customer information.
- Treat community submissions as unverified until assessed.
- Do not automatically block every published IOC.
- Record the original source and collection date.

## Key Takeaways

Use a combination of trusted external reporting and internal telemetry.

The best source is the one that helps answer a defined organisational question reliably.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
