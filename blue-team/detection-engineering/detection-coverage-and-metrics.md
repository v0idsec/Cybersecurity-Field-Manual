# Detection Coverage and Metrics

## Overview

Detection coverage measures how effectively an organisation can identify relevant security threats and suspicious activity.

Metrics provide visibility into detection quality, operational performance and areas requiring improvement.

## Coverage Assessment

Assess coverage across:

- Endpoints
- Identity infrastructure
- Network infrastructure
- Cloud environments
- Applications
- Email systems
- Critical business services

Coverage should reflect the organisation's actual attack surface.

## MITRE ATT&CK Coverage

ATT&CK provides a structured knowledge base of adversary tactics and techniques.

It can be used to organise detection requirements and identify potential gaps.

Example coverage matrix:

| ATT&CK Technique | Detection Requirement | Status |
|---|---|---|
| T1078 - Valid Accounts | Detect unusual account activity | Implemented |
| T1059.001 - PowerShell | Detect suspicious PowerShell execution | Implemented |
| T1053.005 - Scheduled Task | Detect unexpected task creation | Partial |
| T1543.003 - Windows Service | Detect suspicious service installation | Implemented |
| T1021 - Remote Services | Detect unusual remote access | Planned |

Coverage status should be supported by actual testing evidence.

## Coverage Limitations

A technique marked as covered may have significant limitations.

Consider:

- Which platforms are monitored?
- Which variants are detectable?
- Is required telemetry available?
- Does the rule generate actionable alerts?
- Has the detection been tested?
- Can analysts investigate the result?

Avoid treating every technique as a simple binary covered/not-covered value.

## Detection Metrics

### Detection Coverage

Measures the proportion of prioritised detection requirements with implemented and validated detections.

A useful coverage measure should distinguish implemented detections from tested detections.

### False-Positive Rate

One possible calculation:

\[
\text{False Positive Rate} =
\frac{\text{False Positives}}{\text{All Classified Alerts}}
\times 100
\]

Ensure the classification process is consistent.

### Mean Time to Detect

Measures the average time between the start of an incident and its detection.

### Mean Time to Acknowledge

Measures the time between alert generation and analyst acknowledgement.

### Mean Time to Respond

Measures the time between detection and the initiation of an appropriate response.

### Mean Time to Contain

Measures the time between detection and effective containment.

## Example Operational Dashboard

| Metric | Example Value |
|---|---:|
| Active detections | 85 |
| Tested detections | 72 |
| Detections requiring review | 9 |
| Detection coverage requirements | 60 |
| Validated requirements | 42 |
| Average daily alerts | 140 |
| Alerts awaiting triage | 12 |

Values are illustrative.

## Data Quality Metrics

Track:

- Ingestion availability
- Event latency
- Parsing failures
- Missing log sources
- Agent health
- Event volume changes
- Retention compliance

Poor telemetry quality can undermine otherwise well-designed detections.

## Detection Effectiveness

Measure effectiveness through:

- Controlled testing
- Historical incident review
- Purple-team exercises
- Threat-informed assessments
- Detection regression tests

An alert count alone does not demonstrate detection effectiveness.

## Reporting

Reports should communicate:

- Critical detection gaps
- Coverage across important systems
- Untested detections
- Detection failures
- False-positive trends
- Telemetry issues
- Improvement priorities

## Metric Pitfalls

Avoid:

- Measuring success only by alert volume.
- Treating ATT&CK coverage as proof of security.
- Comparing teams without considering environment differences.
- Optimising false-positive rates at the expense of coverage.
- Treating untested rules as validated.
- Using averages without understanding outliers.

## Further Reading

- MITRE ATT&CK: https://attack.mitre.org/
- MITRE ATT&CK Navigator: https://mitre-attack.github.io/attack-navigator/
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
