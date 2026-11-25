# Threat Hunting Fundamentals

## Overview

Threat Hunting is a proactive security activity focused on identifying threats that may have bypassed existing preventative and detective controls.

Traditional security operations often begin with an alert. Threat hunting instead begins with a question, hypothesis or intelligence-led concern.

The objective is to uncover suspicious activity, validate assumptions and improve the organisation's ability to detect future attacks.

## Threat Hunting vs Alert Triage

| Activity | Threat Hunting | Alert Triage |
|---|---|---|
| Starting point | Hypothesis or intelligence | Security alert |
| Approach | Proactive | Reactive |
| Scope | Often broader | Usually specific |
| Objective | Discover unknown activity | Assess known activity |
| Output | Findings and detection improvements | Alert disposition and escalation |

Both activities are important parts of security operations.

## Hunting Approaches

### Hypothesis-Driven Hunting

Begins with a testable statement about potential attacker behaviour.

Example:

> An attacker with access to a compromised account may be using unusual remote administration methods to move between systems.

The hunt investigates whether supporting evidence exists.

### Intelligence-Driven Hunting

Uses threat intelligence to identify relevant behaviours.

Sources may include:

- MITRE ATT&CK
- CISA advisories
- ACSC advisories
- Vendor research
- Incident reports
- Internal threat intelligence

Focus on behaviours and techniques rather than relying exclusively on known indicators.

### Anomaly-Driven Hunting

Investigates deviations from normal activity.

Examples:

- Unusual authentication patterns
- Unexpected process execution
- Abnormal data transfer
- New administrative activity
- Unusual network connections

Anomalies are leads, not proof of malicious activity.

### Situational Hunting

Responds to a specific concern.

Examples:

- A newly disclosed vulnerability
- A suspected third-party compromise
- A new malware campaign
- A compromised identity provider
- A security incident affecting a similar organisation

## Threat Hunting Lifecycle

1. Define the hunting objective.
2. Develop a hypothesis.
3. Identify relevant telemetry.
4. Establish the scope and timeframe.
5. Develop queries and investigation methods.
6. Examine results.
7. Validate suspicious findings.
8. Document conclusions.
9. Escalate confirmed incidents.
10. Improve detections and controls.

## Hunting Maturity

A simplified maturity model:

| Level | Characteristics |
|---|---|
| Initial | Primarily reactive, limited telemetry |
| Developing | Repeatable hunts and documented procedures |
| Established | Intelligence-led and hypothesis-driven hunts |
| Advanced | Integrated detection engineering and automation |
| Optimised | Continuous feedback and measurable improvement |

This is an illustrative model, not a universal maturity standard.

## What Makes a Good Hunt?

A useful hunt has:

- A clearly defined question.
- A defensible hypothesis.
- Relevant telemetry.
- A defined scope.
- Repeatable investigation steps.
- Documented results.
- Actionable outcomes.

## Common Hunting Mistakes

- Searching without a clear objective.
- Treating every anomaly as malicious.
- Relying on one log source.
- Ignoring missing telemetry.
- Failing to establish a baseline.
- Expanding scope without justification.
- Failing to document negative findings.
- Ending a hunt without improving detection capabilities.

## Hunting Outcomes

Possible outcomes include:

- Confirmed malicious activity.
- Suspicious activity requiring escalation.
- Benign activity.
- No supporting evidence found.
- Insufficient telemetry.
- New detection opportunity.
- Security control improvement.

A hunt that finds no malicious activity can still provide value by validating visibility and identifying coverage gaps.

## Further Reading

- MITRE ATT&CK: https://attack.mitre.org/
- SANS Threat Hunting: https://www.sans.org/cyber-security-courses/
- CISA: https://www.cisa.gov/
- ACSC: https://www.cyber.gov.au/

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
