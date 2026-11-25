# Alert Triage

## Overview

Alert triage is the process of assessing security alerts, determining their significance and deciding whether further investigation or response is required.

Effective triage reduces noise while ensuring potentially serious threats are not overlooked.

## Triage Objectives

- Establish whether an alert is credible.
- Identify affected users and systems.
- Determine the potential impact.
- Identify related suspicious activity.
- Assign an appropriate severity.
- Escalate or close the alert with documented reasoning.

## Initial Assessment

Begin by reviewing:

| Field | Questions |
|---|---|
| Alert name | What behaviour was detected? |
| Severity | How was the alert prioritised? |
| Timestamp | When did the activity occur? |
| Hostname | Which system was involved? |
| User | Which account was involved? |
| Source IP | Where did the activity originate? |
| Process | What executable was involved? |
| Detection source | Which product generated the alert? |
| Evidence | What triggered the detection? |

## Validate the Alert

Determine whether the activity is:

- Expected business activity
- Unusual but legitimate activity
- Suspicious activity requiring investigation
- Confirmed malicious activity

Do not close alerts solely because an activity is unfamiliar or because the user claims it was legitimate.

## Contextual Investigation

### User Context

Review:

- Role and privileges
- Normal working hours
- Recent authentication activity
- Recent password changes
- Group membership
- MFA activity
- Known administrative responsibilities

### Endpoint Context

Review:

- Asset criticality
- Operating system
- EDR health
- Recent process execution
- Recent alerts
- Installed software
- Network connections

### Network Context

Review:

- Source and destination addresses
- Domain reputation
- Destination ports
- Connection frequency
- Geographic context
- Related firewall or proxy events

### Threat Intelligence

Where appropriate, check:

- File hashes
- IP addresses
- Domains
- URLs
- Certificate information
- Known malware indicators

Threat intelligence should be treated as supporting evidence, not definitive proof.

## Alert Severity

Example severity model:

| Severity | Description | Typical Response |
|---|---|---|
| Critical | Confirmed or highly credible severe compromise | Immediate escalation |
| High | Strong indicators of compromise or significant exposure | Urgent investigation |
| Medium | Suspicious activity requiring further context | Investigate promptly |
| Low | Limited risk or weak indicators | Review and monitor |
| Informational | Contextual or expected activity | Record if relevant |

Severity should consider:

- Confidence
- Business impact
- Asset criticality
- Privilege level
- Scope
- Potential data exposure
- Whether activity is ongoing

## Common Triage Scenarios

### Multiple Failed Logins

Investigate:

- Number of failures
- Targeted accounts
- Source addresses
- Authentication protocol
- Successful logins following failures
- MFA activity
- Account lockouts

### Suspicious PowerShell Execution

Investigate:

- Parent process
- Command-line arguments
- Script content
- User context
- File and network activity
- Related endpoint alerts

### Malware Detection

Investigate:

- File hash
- Detection name
- File location
- Execution status
- Process ancestry
- Quarantine status
- Related endpoints

### Unusual Privileged Activity

Investigate:

- Account identity
- Privilege assignment
- Change approval
- Source endpoint
- Related authentication
- Subsequent administrative activity

## False Positives

Common causes include:

- Legitimate administrative scripts
- Software deployment
- Vulnerability scanning
- Approved penetration testing
- Backup operations
- Software updates
- Security tooling

Document the reason for classifying an alert as a false positive.

Where appropriate, recommend detection tuning rather than suppressing all similar activity.

## Escalation Criteria

Escalate when:

- Compromise is confirmed or strongly suspected.
- Privileged accounts are involved.
- Sensitive data may be exposed.
- Multiple systems are affected.
- Activity is ongoing.
- Security controls appear disabled.
- The incident exceeds the analyst's authority.

## Triage Documentation

Record:

- Alert identifier
- Detection source
- Initial assessment
- Evidence reviewed
- Affected systems and accounts
- Severity
- Actions taken
- Escalation details
- Final disposition
- Analyst and timestamps

## Final Dispositions

Common outcomes include:

- True positive
- False positive
- Benign positive
- Duplicate
- Informational
- Escalated
- Inconclusive

Use the organisation's defined classification model.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
