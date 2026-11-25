# Open-Source Intelligence (OSINT)

Open-Source Intelligence (OSINT) is the process of collecting, analysing and validating information from publicly accessible sources to develop an understanding of an organisation, its people, technology and external exposure.

OSINT is commonly used during the reconnaissance phase of security assessments, red-team engagements, threat intelligence investigations and attack-surface assessments.

This section focuses on practical OSINT techniques, professional workflows and commonly used tools.

## Contents

| Resource | Description |
|---|---|
| [OSINT Methodology](osint-methodology.md) | Planning, collection, analysis, validation and reporting |
| [Domain and Infrastructure Recon](domain-and-infrastructure-recon.md) | Domain intelligence, DNS, subdomains, certificates and infrastructure |
| [Organisation and Personnel OSINT](organisation-and-personnel-osint.md) | Company research, personnel discovery and organisational relationships |
| [Search Engine Reconnaissance](search-engine-reconnaissance.md) | Search operators, indexed content and public information discovery |
| [Technology and Asset Discovery](technology-and-asset-discovery.md) | Technology fingerprinting and external attack-surface discovery |
| [Data Exposure and Breach Intelligence](data-exposure-and-breach-intelligence.md) | Exposure monitoring, breach intelligence and leaked information |
| [Social Media and Public Source Intelligence](social-media-and-public-source-intelligence.md) | Public social media, usernames and contextual intelligence |
| [OSINT Tools Reference](osint-tools-reference.md) | Common OSINT platforms, tools and commands |

## Core Principles

- **Legality:** Only collect and process information within the engagement's authorised scope and applicable laws.
- **Passive first:** Prefer passive collection methods before interacting with target infrastructure.
- **Validation:** Treat collected information as leads until independently verified.
- **Attribution:** Do not assume that shared names, IP addresses, domains or accounts belong to the same entity without supporting evidence.
- **Data minimisation:** Collect only information relevant to the assessment.
- **Evidence:** Preserve source URLs, timestamps, screenshots and collection context.
- **Privacy:** Avoid unnecessary collection or distribution of personal information.

## Typical OSINT Workflow

1. Define objectives, scope and exclusions.
2. Establish known organisation identifiers.
3. Collect domain, infrastructure and technology intelligence.
4. Research public organisational and personnel information.
5. Identify potential exposure and security-relevant information.
6. Correlate and validate findings.
7. Document evidence, confidence and potential impact.
8. Report actionable findings.

## Common Tooling

| Tool | Primary purpose |
|---|---|
| SpiderFoot | Automated OSINT collection and correlation |
| Flare | External exposure and threat intelligence |
| theHarvester | Email, domain and host discovery |
| Maltego | Visual relationship analysis |
| Amass | Attack-surface and subdomain discovery |
| Shodan | Internet-facing service discovery |
| Censys | Internet infrastructure and certificate intelligence |
| Recon-ng | Modular reconnaissance |
| ExifTool | File metadata analysis |
| Have I Been Pwned | Public breach exposure checks |

## Scope and Authorisation

Public availability does not automatically make information appropriate to collect, retain or use.

Before beginning an engagement, establish:
- Approved organisation names and domains.
- Permitted subsidiaries and third-party relationships.
- Whether personnel research is authorised.
- Whether breach and credential intelligence is in scope.
- Whether active verification is permitted.
- Data retention and handling requirements.

OSINT collection must remain within the agreed rules of engagement.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
