# Detection Strategy and Prioritisation

## Overview

A detection strategy defines which threats an organisation needs to detect, why those threats matter and how detection capabilities will be developed.

Without prioritisation, detection engineering can become a collection of disconnected rules that generate alerts without meaningfully reducing risk.

## Establishing Detection Requirements

Start with the organisation's environment and threat profile.

Consider:

- Critical business systems
- Sensitive information
- Internet-facing services
- Privileged accounts
- Identity infrastructure
- Remote access infrastructure
- Cloud workloads
- Third-party integrations
- Regulatory obligations
- Known attack paths

## Risk-Based Prioritisation

Prioritise detections based on:

| Factor | Consideration |
|---|---|
| Business impact | What happens if the threat succeeds? |
| Likelihood | How likely is the activity? |
| Exposure | How accessible is the affected system? |
| Asset criticality | How important is the affected asset? |
| Threat activity | Is the behaviour actively observed? |
| Detection gap | Is there currently sufficient visibility? |
| Response capability | Can the organisation act on an alert? |

A detection for a likely attack against a critical identity system may be more valuable than a low-impact detection for an obscure endpoint event.

## Identify Crown Jewels

Identify the systems and information that would cause the greatest harm if compromised.

Examples:

- Domain controllers
- Identity providers
- Backup infrastructure
- Financial systems
- Customer databases
- Production cloud environments
- Security management platforms
- Privileged administrator workstations

Prioritise detection coverage around these assets.

## Threat-Informed Detection

Use threat intelligence and adversary behaviour to identify relevant detection requirements.

Useful sources include:

- MITRE ATT&CK
- CISA advisories
- Australian Cyber Security Centre advisories
- Vendor threat research
- Incident reports
- Internal incident history
- Sector-specific threat intelligence

Translate intelligence into observable behaviours rather than relying exclusively on published indicators.

## ATT&CK-Based Prioritisation

MITRE ATT&CK can help organise detection requirements by:

- Tactics
- Techniques
- Sub-techniques
- Platforms
- Data sources
- Detection strategies

Example:

| Technique | Potential Detection |
|---|---|
| T1078 - Valid Accounts | Unusual authentication and account activity |
| T1059.001 - PowerShell | Suspicious PowerShell execution |
| T1053.005 - Scheduled Task | Unexpected scheduled task creation |
| T1543.003 - Windows Service | Unexpected service installation |
| T1021 - Remote Services | Unusual remote access and lateral movement |

ATT&CK coverage should not be treated as a simple percentage score. A technique may be covered by multiple detections, while a listed detection may provide only partial coverage.

## Detection Prioritisation Matrix

An example prioritisation model:

| Priority | Description |
|---|---|
| P1 | Critical assets or high-impact attack paths |
| P2 | High-risk behaviours with meaningful exposure |
| P3 | Useful coverage improvements |
| P4 | Lower-risk or specialised detection opportunities |

Define priorities using organisational risk and available resources.

## Detection Backlog

Maintain a backlog containing:

- Detection requirement
- Threat scenario
- Priority
- Data dependencies
- Implementation status
- Test status
- Assigned owner
- Known limitations

Example:

| Detection | Priority | Status |
|---|---|---|
| Privileged account compromise | P1 | Planned |
| Suspicious PowerShell execution | P1 | Testing |
| Unexpected service installation | P2 | Deployed |
| Unusual DNS query patterns | P3 | Backlog |

## Coverage Gaps

Identify where the organisation lacks:

- Required telemetry
- Detection logic
- Investigation context
- Alert routing
- Response procedures

A missing telemetry source may require engineering work before a detection can be developed.

## Review and Governance

Review detection priorities when:

- New systems are deployed.
- Business-critical services change.
- New threat intelligence becomes available.
- Significant incidents occur.
- Attack surface changes.
- Regulatory requirements change.

## Further Reading

- MITRE ATT&CK: https://attack.mitre.org/
- ACSC: https://www.cyber.gov.au/
- CISA: https://www.cisa.gov/
- MITRE CAR: https://car.mitre.org/

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
