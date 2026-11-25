# False Positive Management

## Overview

A false positive occurs when a detection generates an alert for activity that is not actually malicious or does not represent the intended threat condition.

False-positive management improves alert quality while preserving meaningful detection coverage.

## Alert Classification

| Classification | Description |
|---|---|
| True positive | Detection correctly identifies malicious or suspicious activity |
| False positive | Detection incorrectly identifies benign activity |
| Benign positive | Detection correctly identifies activity that is legitimate |
| Inconclusive | Available evidence is insufficient to classify |
| Duplicate | Alert represents activity already captured elsewhere |

Organisations may use different classification terminology.

## Common Causes

- Broad detection conditions
- Poor thresholds
- Missing context
- Incorrect field mappings
- Legitimate administrative activity
- Software deployment
- Vulnerability scanning
- Backup operations
- Monitoring tools
- Approved security testing
- Shared infrastructure

## Investigation Before Tuning

Before modifying a detection, determine:

1. What triggered the alert?
2. Which events matched?
3. Was the activity legitimate?
4. Is the behaviour expected?
5. Could the same behaviour be abused?
6. Would an exclusion reduce meaningful coverage?
7. Is additional context available?

Do not suppress an alert simply because it has occurred previously.

## Tuning Methods

### Narrow Conditions

Refine the detection to focus on the intended behaviour.

For example, add relevant process ancestry or event context rather than matching a broad command-line string.

### Contextual Enrichment

Enrich alerts with:

- Asset criticality
- User role
- Process reputation
- Device ownership
- Approved software inventory
- Change records
- Known maintenance windows

### Scoped Exclusions

Exclude only the specific activity that has been confirmed as legitimate.

Example:

- A known deployment process on a defined management server.
- A documented administrative account performing an approved task.
- A scheduled maintenance operation during a defined window.

### Threshold Adjustment

Adjust thresholds using observed activity.

Consider:

- Event frequency
- Number of affected users
- Number of affected endpoints
- Time window
- Asset criticality
- Normal operating patterns

Do not increase thresholds simply to reduce alert volume.

## Exclusion Management

Every exclusion should document:

- Detection identifier
- Excluded activity
- Technical justification
- Scope
- Approval
- Date introduced
- Expiry or review date
- Owner

Prefer time-limited exclusions where practical.

## Example Tuning Scenario

A detection alerts on PowerShell execution containing a particular administrative command.

Investigation shows that an approved management platform runs the command regularly.

Possible approaches:

1. Confirm the executable path and signature.
2. Identify the management platform's service account.
3. Confirm the parent process.
4. Validate the expected execution schedule.
5. Add a narrowly scoped condition.
6. Test that unrelated PowerShell activity still alerts.

Avoid excluding all PowerShell activity from the management server.

## Alert Noise Metrics

Track:

- Total alert volume
- False-positive rate
- Benign-positive rate
- Duplicate alert volume
- Analyst investigation time
- Repeated false-positive causes
- Exclusion count
- Exclusion age

## Regression Testing

After tuning:

- Re-run the original positive test.
- Run negative tests.
- Confirm expected alerts remain.
- Confirm the exclusion is correctly scoped.
- Check for unintended impact on other detections.

## Review Process

Review exclusions and tuned detections regularly.

Reassess when:

- Software changes.
- Systems are migrated.
- Service accounts change.
- Administrative workflows change.
- Threat activity evolves.
- A related incident occurs.

## Key Principle

The objective is not zero alerts.

The objective is high-quality alerts that identify meaningful security activity without overwhelming analysts.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
