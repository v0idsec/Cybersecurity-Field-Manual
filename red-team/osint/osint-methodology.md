# OSINT Methodology

## Overview

OSINT is not simply searching for information. It is a structured intelligence process involving collection, correlation, validation and analysis.

A disciplined methodology helps prevent false attribution, reduces unnecessary collection and produces findings that can be independently verified.

## 1. Define the Intelligence Requirements

Start by establishing what the assessment needs to discover.

Typical objectives include:

- Identifying an organisation's external digital footprint.
- Discovering internet-facing infrastructure.
- Identifying technologies and service providers.
- Understanding publicly visible organisational relationships.
- Finding exposed information relevant to security.
- Identifying publicly disclosed credential exposure.
- Mapping an organisation's potential attack surface.

Avoid collecting information without a defined purpose.

### Scope Definition

Record:

| Item | Example |
|---|---|
| Primary organisation | Example Corporation |
| Primary domain | example.com |
| Approved domains | example.com, example.com.au |
| Known IP ranges | Supplied by client |
| Subsidiaries | Explicitly approved entities |
| Personnel research | Approved / excluded |
| Breach intelligence | Approved / excluded |
| Third-party infrastructure | Explicitly defined |
| Assessment period | Agreed dates |

A domain relationship does not automatically establish authorisation to assess the associated infrastructure.

## 2. Establish Known Identifiers

Begin with reliable identifiers supplied by the client.

Useful starting points include:

- Legal organisation name.
- Trading names and subsidiaries.
- Primary domains.
- Known email domains.
- Public IP ranges.
- Corporate social media accounts.
- Official websites.
- Known technology providers.

Record the source of each identifier.

Avoid expanding the scope based solely on similar company names or assumed relationships.

## 3. Collection

Collection can be divided into several categories.

### Domain and Infrastructure Intelligence

Identify:
- Registered domains.
- DNS records.
- Nameservers.
- Mail infrastructure.
- Subdomains.
- Certificate transparency entries.
- Public IP addresses.
- Hosting providers.
- Internet-facing services.

### Organisation Intelligence

Identify:
- Business structure.
- Subsidiaries.
- Publicly documented partnerships.
- Technology providers.
- Public job advertisements.
- Published technical documentation.

### Personnel Intelligence

Where authorised, identify:
- Public professional profiles.
- Job roles and departments.
- Publicly disclosed contact details.
- Public professional relationships.
- Relevant technology and responsibility indicators.

### Exposure Intelligence

Investigate:
- Public breach notifications.
- Exposed credentials through authorised intelligence sources.
- Publicly accessible storage.
- Accidentally published documents.
- Public source-code exposure.
- Security disclosures.

## 4. Passive and Active Collection

### Passive Collection

Passive collection uses existing public information without directly probing the target's infrastructure.

Examples:
- Search engines.
- Public DNS datasets.
- Certificate transparency logs.
- Public company records.
- Public code repositories.
- Threat intelligence platforms.
- Public breach notification services.

Passive collection is generally a sensible starting point.

### Active Collection

Active collection involves interacting with target infrastructure or services.

Examples:
- DNS queries to target-controlled infrastructure.
- Direct HTTP requests.
- Port scanning.
- Service enumeration.
- Automated reconnaissance against live assets.

Active collection may generate logs, trigger security alerts or affect production systems.

Confirm that it is explicitly authorised before performing it.

## 5. Correlation

Individual data points become more useful when connected.

Example:

1. A job advertisement mentions Microsoft Azure.
2. Public DNS records identify Azure-hosted services.
3. A certificate transparency search reveals additional subdomains.
4. A public application identifies a specific technology stack.
5. These observations are correlated into an external technology profile.

Correlation should not be confused with proof.

For example:
- A shared IP address does not prove common ownership.
- A certificate does not prove that a service is currently operational.
- A person's public profile does not prove they have access to a particular system.
- A historical DNS record does not establish current infrastructure ownership.

## 6. Validate Findings

For every potential finding, establish:

- Is the information current?
- Is the source trustworthy?
- Can the information be independently verified?
- Does it belong to the target organisation?
- Is the relationship direct or inferred?
- Is the information relevant to the assessment?
- Could the finding be a false positive?

Prefer multiple independent sources for important conclusions.

## 7. Confidence Assessment

Use a consistent confidence scale.

| Confidence | Meaning |
|---|---|
| High | Directly verified through reliable, current evidence |
| Medium | Supported by multiple sources but not fully verified |
| Low | Based on indirect, historical or incomplete information |

Document uncertainty rather than presenting assumptions as facts.

## 8. Evidence Collection

Preserve enough information for another analyst to reproduce the observation.

Recommended evidence fields:

| Field | Description |
|---|---|
| Finding ID | Unique reference |
| Source | URL, platform or dataset |
| Observation | What was discovered |
| Collection time | Date and time in UTC |
| Screenshot | Supporting visual evidence |
| Confidence | High, medium or low |
| Relevance | Why the information matters |
| Validation | How the observation was confirmed |
| Limitations | Known uncertainty or gaps |

Where possible, preserve original source URLs and collection timestamps.

## 9. Reporting

OSINT findings should explain:

1. What was discovered.
2. Where the information came from.
3. Why it is relevant.
4. Whether it is current and verified.
5. What security implications it creates.
6. What action should be taken.

Avoid reporting large collections of raw information without analysis.

## Operational Considerations

- Respect applicable privacy and data-protection requirements.
- Do not access accounts or systems using discovered credentials unless explicitly authorised.
- Do not attempt to validate credentials against unrelated services.
- Do not contact employees or third parties without approval.
- Avoid downloading or retaining unnecessary personal information.
- Treat third-party intelligence platforms as external data processors where relevant.
- Record collection methods and limitations.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
