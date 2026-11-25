# Threat Hunting

## Overview

Threat Hunting is the proactive process of searching an environment for malicious activity that may not have been identified by existing security controls.

Unlike traditional alert-driven monitoring, threat hunting begins with a hypothesis, threat intelligence or suspicious behaviour and uses available telemetry to identify evidence.

This section provides practical methodologies, investigation techniques and query references for conducting structured threat hunts.

## Contents

| Guide | Description |
|---|---|
| [Threat Hunting Fundamentals](threat-hunting-fundamentals.md) | Core concepts and principles |
| [Threat Hunting Methodology](threat-hunting-methodology.md) | Structured hunting workflows |
| [Hypothesis Development](hypothesis-development.md) | Developing testable hunting hypotheses |
| [Threat Hunting Data Sources](threat-hunting-data-sources.md) | Identifying useful telemetry |
| [Endpoint Threat Hunting](endpoint-threat-hunting.md) | Hunting suspicious endpoint activity |
| [Identity and Authentication Hunting](identity-and-authentication-hunting.md) | Investigating identity-based threats |
| [Network Threat Hunting](network-threat-hunting.md) | Identifying suspicious network behaviour |
| [Cloud Threat Hunting](cloud-threat-hunting.md) | Hunting across cloud environments |
| [Threat Hunting with KQL](threat-hunting-with-kql.md) | Microsoft Sentinel hunting queries |
| [Threat Hunting with Splunk](threat-hunting-with-splunk.md) | Splunk investigation queries |
| [Threat Hunting Tools Reference](threat-hunting-tools-reference.md) | Useful tools and commands |
| [Hunt Reporting and Detection Development](hunt-reporting-and-detection-development.md) | Documenting findings and improving detections |

## Core Principles

- Hunt based on evidence and testable hypotheses.
- Understand the environment before interpreting anomalies.
- Use multiple telemetry sources.
- Document assumptions and limitations.
- Preserve relevant evidence.
- Avoid treating unusual activity as automatically malicious.
- Convert useful findings into improved detection capabilities.

## Related Sections

- [SIEM & EDR](../siem-edr/README.md)
- [Detection Engineering](../detection-engineering/README.md)
- [Incident Response](../incident-response/README.md)
- [Digital Forensics](../digital-forensics/README.md)
- [Threat Intelligence](../threat-intelligence/README.md)
- [Purple Team](../../purple-team/README.md)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
