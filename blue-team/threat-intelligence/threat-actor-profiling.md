# Threat Actor Profiling

## Overview

Threat actor profiling attempts to understand adversaries by analysing their behaviour, capabilities, objectives and observed activity.

Profiling can help organisations prioritise threats and improve defensive planning.

## Common Threat Actor Categories

| Category | Typical Motivation |
|---|---|
| Cybercriminal groups | Financial gain |
| State-sponsored actors | Espionage or strategic objectives |
| Hacktivists | Political or ideological objectives |
| Insiders | Financial gain, grievance or unauthorised activity |
| Opportunistic attackers | Exploitation of exposed systems |
| Initial access brokers | Selling access to compromised environments |

These categories are broad and do not establish attribution.

## Profiling Information

Useful information may include:

- Known campaigns.
- Target industries.
- Geographic targeting.
- Initial access methods.
- Malware and tooling.
- Infrastructure.
- Exploitation techniques.
- Persistence methods.
- Objectives.
- Known relationships with other groups.

## Behavioural Analysis

Focus on observed techniques rather than relying exclusively on actor names.

Examples:

- Phishing for initial access.
- Exploitation of public-facing applications.
- Credential theft.
- Remote access abuse.
- Privilege escalation.
- Lateral movement.
- Data collection and exfiltration.

Map relevant behaviours to [MITRE ATT&CK](https://attack.mitre.org/).

## Attribution Limitations

Attribution is difficult.

Attackers may:

- Reuse other groups' tools.
- Copy publicly available techniques.
- Use compromised infrastructure.
- Deliberately plant misleading indicators.
- Operate through third-party services.

Avoid claiming attribution based solely on one IP address, malware family or technique.

## Defensive Applications

Threat actor research can support:

- Threat modelling.
- Detection engineering.
- Threat hunting.
- Vulnerability prioritisation.
- Incident response.
- Security awareness.
- Adversary emulation.

## Profiling Report

A useful report should include:

1. Summary.
2. Actor or campaign reference.
3. Confidence level.
4. Known objectives.
5. Targeting patterns.
6. Observed techniques.
7. Relevant indicators.
8. Supporting sources.
9. Defensive recommendations.
10. Intelligence gaps.

## Key Takeaways

Threat actor profiling should focus on evidence and defensive relevance.

Behavioural understanding is often more useful than attempting to identify the person or organisation behind an attack.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
