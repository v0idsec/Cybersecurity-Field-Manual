# Detection Engineering

## Overview

Detection Engineering is the discipline of designing, developing, testing and maintaining security detections that identify suspicious or malicious activity.

It bridges threat intelligence, security operations, telemetry engineering and incident response.

This section provides practical guidance for building reliable detections that produce actionable alerts and support effective investigations.

## Contents

| Guide | Description |
|---|---|
| [Detection Engineering Fundamentals](detection-engineering-fundamentals.md) | Core concepts, architecture and detection principles |
| [Detection Strategy and Prioritisation](detection-strategy-and-prioritisation.md) | Identifying detection requirements and prioritising coverage |
| [Detection Logic and Rule Development](detection-logic-and-rule-development.md) | Developing effective detection logic |
| [Detection as Code](detection-as-code.md) | Version control, review and deployment workflows |
| [Sigma Rule Development](sigma-rule-development.md) | Creating portable Sigma detection rules |
| [Behavioural Detection](behavioural-detection.md) | Identifying suspicious behaviour and attack patterns |
| [Detection Testing and Validation](detection-testing-and-validation.md) | Testing detection effectiveness |
| [False Positive Management](false-positive-management.md) | Reducing alert noise without losing coverage |
| [Detection Coverage and Metrics](detection-coverage-and-metrics.md) | Measuring detection effectiveness |
| [Detection Maintenance and Lifecycle](detection-maintenance-and-lifecycle.md) | Maintaining detections over time |

## Related Sections

- [SIEM & EDR](../siem-edr/README.md)
- [Threat Hunting](../threat-hunting/README.md)
- [Incident Response](../incident-response/README.md)
- [Threat Intelligence](../threat-intelligence/README.md)
- [Purple Team](../../purple-team/README.md)

## Core Principles

- Build detections around observable behaviour.
- Understand the telemetry required before writing rules.
- Prioritise threats based on organisational risk.
- Test detections before deployment.
- Document investigation and response guidance.
- Avoid broad exclusions that weaken coverage.
- Maintain detections as systems and threats evolve.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
