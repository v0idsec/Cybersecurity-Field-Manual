# OSINT Tools Reference

## Overview

This document provides a practical reference to commonly used OSINT platforms and tools.

It focuses on:
- What each tool is useful for.
- When to use it.
- Common commands and queries.
- How to interpret results.
- Operational limitations.

It is not an installation or configuration guide.

All collection and testing must remain within the engagement's authorised scope.

---

## 1. SpiderFoot

<https://www.spiderfoot.net/>

<badge color="success">Automated OSINT</badge>

SpiderFoot automates OSINT collection and correlates information from multiple data sources.

### Common Use Cases

- Domain and subdomain discovery.
- Email address discovery.
- IP and infrastructure intelligence.
- Public exposure research.
- Relationship discovery.
- Initial reconnaissance.

### Typical Workflow

1. Define the organisation's approved identifiers.
2. Select relevant collection modules.
3. Run a scoped investigation.
4. Review discovered entities.
5. Investigate relationships.
6. Validate important findings independently.
7. Export relevant evidence.

### Useful Capabilities

| Capability | Purpose |
|---|---|
| Domain discovery | Identify related domains |
| DNS intelligence | Discover DNS relationships |
| Email discovery | Identify public email references |
| IP intelligence | Correlate public infrastructure |
| Threat intelligence | Identify relevant threat indicators |
| Data correlation | Connect related observations |

### Operational Notes

- Module availability depends on the version and integrations.
- Some modules require API keys.
- Automated results can contain false positives.
- Avoid collecting unnecessary personal information.
- Treat discovered credentials as sensitive and do not use them.

---

## 2. Flare

<https://flare.io/>

<badge color="success">External Exposure Intelligence</badge>

Flare provides digital risk protection and external threat intelligence capabilities.

### Common Use Cases

- Corporate credential exposure.
- Infostealer-related exposure.
- Dark web intelligence.
- Brand and domain monitoring.
- Third-party exposure.
- External threat intelligence.

### Assessment Workflow

1. Establish approved organisation identifiers.
2. Search relevant domains and corporate identities.
3. Review exposed credential intelligence.
4. Identify relevant historical or current observations.
5. Correlate results with known assets.
6. Assess confidence and relevance.
7. Record minimal supporting evidence.
8. Report through approved channels.

### Investigation Checklist

- [ ] Is the affected domain associated with the target?
- [ ] Is the observation current or historical?
- [ ] Is the source reliable?
- [ ] Is the information independently corroborated?
- [ ] Does it represent a genuine security concern?
- [ ] Has sensitive material been appropriately redacted?

### Operational Notes

- Capabilities depend on subscription and product access.
- Intelligence may be historical or incomplete.
- Never attempt to authenticate using discovered credentials.
- Follow the client's data-handling requirements.

---

## 3. theHarvester

<https://github.com/laramies/theHarvester>

<badge>Domain and Email Discovery</badge>

theHarvester collects publicly available information associated with domains.

### Common Use Cases

- Email discovery.
- Hostname discovery.
- Domain reconnaissance.
- Initial external footprint mapping.

### Commands

```bash
theHarvester -d example.com -b all
```

Specify a source:

```bash
theHarvester -d example.com -b bing
```

Save output:

```bash
theHarvester -d example.com -b all -f harvester-results
```

### Operational Notes

- Data-source support changes between versions.
- Some sources require API keys.
- Results may include outdated addresses and hostnames.
- Validate all discovered assets before further testing.

---

## 4. Maltego

<https://www.maltego.com/>

<badge>Visual Intelligence and Correlation</badge>

Maltego is used to visualise relationships between entities.

### Common Use Cases

- Domain relationship mapping.
- Organisation research.
- Email and infrastructure correlation.
- Public identity research.
- Visualising complex intelligence datasets.

### Typical Entities

- Domains.
- IP addresses.
- DNS names.
- Email addresses.
- Organisations.
- Websites.
- Social profiles.
- Certificates.

### Typical Workflow

1. Start with a confirmed entity.
2. Select an appropriate transformation.
3. Review discovered relationships.
4. Expand relevant entities.
5. Remove unrelated results.
6. Validate important relationships.
7. Export the final intelligence graph.

### Operational Notes

- Transform availability depends on the edition and integrations.
- A graph relationship is not proof of ownership.
- Large graphs can contain substantial noise.
- Keep source and confidence information associated with important entities.

---

## 5. Amass

<https://github.com/owasp-amass/amass>

<badge>Attack Surface Discovery</badge>

Amass supports external attack-surface mapping and domain enumeration.

### Common Commands

Passive enumeration:

```bash
amass enum -passive -d example.com
```

Save results:

```bash
amass enum -passive -d example.com -o amass-results.txt
```

Multiple domains:

```bash
amass enum -passive -d example.com -d example.org
```

### Common Use Cases

- Subdomain discovery.
- Domain relationship mapping.
- External attack-surface research.
- DNS intelligence.

### Operational Notes

- Passive and active capabilities differ.
- Confirm scope before active enumeration.
- Validate discovered hostnames.
- Historical and third-party assets may appear in results.

---

## 6. Shodan

<https://www.shodan.io/>

<badge>Internet-Facing Services</badge>

Shodan indexes internet-connected devices and services.

### Useful Search Queries

Domain:

```text
hostname:example.com
```

Domain relationship:

```text
domain:example.com
```

Organisation:

```text
org:"Example Corporation"
```

TLS certificate:

```text
ssl.cert.subject.cn:example.com
```

Common ports:

```text
hostname:example.com port:443
hostname:example.com port:22
hostname:example.com port:3389
```

Product identification:

```text
hostname:example.com product:nginx
```

### Common Use Cases

- Public service discovery.
- Exposed remote access services.
- Internet-facing infrastructure.
- Technology identification.
- External exposure monitoring.

### Operational Notes

- Search results may be stale.
- Shared infrastructure can produce unrelated results.
- A service being indexed does not mean it is vulnerable.
- Do not interact with discovered services outside scope.

---

## 7. Censys

<https://search.censys.io/>

<badge>Internet Infrastructure Intelligence</badge>

Censys provides host, service and certificate intelligence.

### Common Use Cases

- Public host discovery.
- Certificate analysis.
- TLS configuration review.
- Service identification.
- Infrastructure correlation.

### Search Concepts

Useful fields and concepts include:

- Hostname.
- IP address.
- Service port.
- Certificate subject.
- Certificate Subject Alternative Names.
- Autonomous system.
- Service product information.

### Example Investigation

1. Search for the approved domain.
2. Identify related certificates.
3. Review hostnames and service observations.
4. Correlate discovered assets with DNS information.
5. Record historical versus current observations.
6. Validate ownership and scope.

Use the current Censys query language and documentation when constructing detailed queries.

---

## 8. Recon-ng

<https://github.com/lanmaster53/recon-ng>

<badge>Modular Reconnaissance</badge>

Recon-ng provides a modular framework for reconnaissance and OSINT collection.

### Common Use Cases

- Domain research.
- Contact discovery.
- Host discovery.
- Public source correlation.
- Structured reconnaissance workflows.

### Common Commands

Start the framework:

```bash
recon-ng
```

Display available modules:

```text
marketplace search
```

Search for a module:

```text
marketplace search domains
```

Install a selected module:

```text
marketplace install <module-name>
```

Show available modules:

```text
modules search
```

Load a module:

```text
modules load <module-name>
```

Display module options:

```text
options list
```

Execute the loaded module:

```text
run
```

Display workspace information:

```text
workspaces list
```

### Operational Notes

- Module names and availability vary.
- Many modules require API credentials.
- Review module behaviour before execution.
- Use scoped inputs and avoid unnecessary collection.

---

## 9. ExifTool

<https://exiftool.org/>

<badge>Metadata Analysis</badge>

ExifTool extracts metadata from documents, images and other file types.

### Common Commands

Read metadata:

```bash
exiftool document.pdf
```

Read metadata from an image:

```bash
exiftool image.jpg
```

Read all available metadata:

```bash
exiftool -a -u -g1 document.pdf
```

Process a directory:

```bash
exiftool -r ./documents/
```

Export metadata as JSON:

```bash
exiftool -json document.pdf
```

### Useful Metadata Fields

- Author.
- Creator.
- Software.
- Creation date.
- Modification date.
- GPS coordinates.
- Camera information.
- Document properties.

### Operational Notes

- Metadata can be removed or modified.
- Metadata does not independently prove authorship or location.
- Avoid distributing sensitive metadata unnecessarily.

---

## 10. Have I Been Pwned

<https://haveibeenpwned.com/>

<badge>Public Breach Intelligence</badge>

Have I Been Pwned provides breach exposure information for supported email addresses and domains.

### Common Use Cases

- Public breach exposure checks.
- Domain monitoring.
- Reviewing known breach history.
- Supporting credential exposure investigations.

### Assessment Workflow

1. Obtain approval for the relevant domain or email checks.
2. Verify domain ownership where required.
3. Search approved identifiers.
4. Record relevant breach names and dates.
5. Assess whether the exposure is current or historical.
6. Report relevant observations.

### Operational Notes

- Not every breach is represented.
- A breach listing does not prove current account compromise.
- Do not attempt to use exposed credentials.
- Avoid including complete personal or credential records in reports.

---

## Additional Useful Resources

| Resource | Purpose |
|---|---|
| [crt.sh](https://crt.sh/) | Certificate transparency searches |
| [ICANN Lookup](https://lookup.icann.org/) | Domain registration information |
| [DNSdumpster](https://dnsdumpster.com/) | DNS and domain reconnaissance |
| [SecurityTrails](https://securitytrails.com/) | DNS and domain intelligence |
| [BuiltWith](https://builtwith.com/) | Website technology profiles |
| [Wappalyzer](https://www.wappalyzer.com/) | Technology identification |
| [URLScan](https://urlscan.io/) | Website scanning and public scan intelligence |
| [VirusTotal](https://www.virustotal.com/) | File, URL and domain intelligence |
| [Intelligence X](https://intelx.io/) | Searchable intelligence sources |
| [ABN Lookup](https://abr.business.gov.au/) | Australian business information |

## Tool Selection Guide

| Objective | Recommended tools |
|---|---|
| Automated OSINT collection | SpiderFoot |
| External exposure intelligence | Flare |
| Email and hostname discovery | theHarvester |
| Visual relationship mapping | Maltego |
| Subdomain enumeration | Amass |
| Internet-facing service discovery | Shodan, Censys |
| Modular reconnaissance | Recon-ng |
| Document metadata | ExifTool |
| Breach exposure checks | Have I Been Pwned |
| Website technology identification | Wappalyzer, WhatWeb |
| Certificate intelligence | crt.sh, Censys |

## General Operational Checklist

- [ ] Engagement scope confirmed.
- [ ] Collection objectives documented.
- [ ] Approved organisation identifiers established.
- [ ] Third-party infrastructure considered.
- [ ] Passive collection performed first.
- [ ] Active collection separately authorised.
- [ ] Findings independently validated.
- [ ] False positives removed.
- [ ] Sensitive information minimised and redacted.
- [ ] Evidence and collection timestamps recorded.
- [ ] Findings reported through approved channels.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
