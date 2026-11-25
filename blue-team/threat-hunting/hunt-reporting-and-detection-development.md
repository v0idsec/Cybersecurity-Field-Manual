# Hunt Reporting and Detection Development

## Overview

Threat hunting should produce documented outcomes that can be used to improve security operations.

A hunt that identifies suspicious activity but fails to communicate findings or improve detection capabilities loses much of its value.

This guide covers reporting, evidence documentation, escalation and the conversion of hunt findings into permanent detection improvements.

## Reporting Objectives

A hunt report should communicate:

- Why the hunt was conducted.
- What was investigated.
- Which data sources were used.
- What activity was identified.
- Whether the hypothesis was supported.
- What limitations existed.
- What actions are recommended.

## Hunt Report Structure

### 1. Executive Summary

Provide a concise summary of:

- Hunting objective
- Key findings
- Risk assessment
- Recommended actions

### 2. Hypothesis

Document the original hypothesis and its justification.

### 3. Scope

Include:

- Systems
- Users
- Networks
- Cloud environments
- Timeframe
- Exclusions

### 4. Data Sources

Record all telemetry sources used.

Examples:

- SIEM
- EDR
- Windows Event Logs
- Identity logs
- Firewall logs
- DNS
- Cloud audit logs

### 5. Methodology

Document:

- Search methods
- Queries
- Filters
- Correlation logic
- Baseline assumptions
- Investigation steps

### 6. Findings

For each finding, record:

- Timestamp
- Host
- User
- Activity
- Supporting evidence
- Risk assessment
- Validation result

### 7. Conclusion

Classify the outcome:

- Hypothesis supported
- Hypothesis partially supported
- Hypothesis not supported
- Inconclusive
- Insufficient telemetry

### 8. Recommendations

Potential recommendations:

- Create a new detection.
- Improve existing detection logic.
- Enable additional logging.
- Investigate affected systems.
- Improve access controls.
- Update incident response procedures.
- Conduct a follow-up hunt.

## Evidence Handling

Preserve:

- Relevant log records
- Query results
- File hashes
- Endpoint artefacts
- Screenshots where appropriate
- Collection timestamps
- Evidence source information

Maintain chain-of-custody records where required.

## Converting Findings into Detections

A hunt may reveal activity that existing controls do not detect.

Use the following process:

1. Identify the behaviour.
2. Determine which telemetry exposed it.
3. Identify the minimum required event fields.
4. Develop detection logic.
5. Test positive and negative cases.
6. Assess false positives.
7. Document investigation guidance.
8. Submit for review.
9. Deploy through the approved process.
10. Monitor detection performance.

## Example

A hunt identifies unexpected scheduled task creation on a group of endpoints.

Potential detection:

- Identify new scheduled task creation.
- Capture the creating account.
- Capture task name and executable.
- Identify the target endpoint.
- Correlate with process execution.
- Alert when the activity deviates from approved administrative behaviour.

Relevant Windows event:

- 4698 — Scheduled task created.

## Improving Telemetry

Hunts can reveal missing visibility.

Examples:

- Process command lines are not collected.
- Sysmon is not deployed to critical endpoints.
- Cloud audit logs have insufficient retention.
- DNS telemetry is unavailable.
- Service account activity is not centrally monitored.

Document telemetry improvements as separate work items.

## Escalation

Escalate findings when:

- Malicious activity is confirmed.
- Compromise is strongly suspected.
- Sensitive information may be exposed.
- Privileged identities are involved.
- Multiple systems are affected.
- Activity remains ongoing.

Follow incident response procedures rather than treating a confirmed incident as an ordinary hunting finding.

## Hunt Metrics

Track:

- Hunts completed
- Hypotheses investigated
- Confirmed findings
- Escalations
- Detection improvements
- Telemetry gaps identified
- Follow-up actions completed

Avoid measuring hunting success only by the number of threats discovered.

## Further Reading

- MITRE ATT&CK: https://attack.mitre.org/
- MITRE CAR: https://car.mitre.org/
- Sigma: https://sigmahq.io/
- NIST Incident Response: https://csrc.nist.gov/pubs/sp/800/61/r2/final

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
