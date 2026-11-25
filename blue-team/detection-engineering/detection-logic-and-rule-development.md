# Detection Logic and Rule Development

## Overview

Detection logic defines the conditions under which security telemetry should generate an alert.

Good detection logic is specific enough to identify meaningful behaviour while remaining flexible enough to account for legitimate environmental variation.

## Detection Development Process

1. Define the behaviour.
2. Identify the relevant data source.
3. Identify required fields.
4. Establish expected activity.
5. Write detection logic.
6. Test against representative data.
7. Review false positives.
8. Document the detection.
9. Deploy and monitor.

## Define the Detection Objective

A detection objective should describe a specific behaviour.

Weak objective:

> Detect suspicious activity.

Better objective:

> Identify successful authentication to privileged accounts following repeated authentication failures from the same source.

The objective should explain what is being detected and why it matters.

## Identify Required Telemetry

Determine:

- Event source
- Event identifier
- Relevant fields
- Timestamp
- User or account identity
- Host or asset identity
- Source and destination information
- Required enrichment

Check that the telemetry is actually available before developing the rule.

## Detection Logic Components

| Component | Purpose |
|---|---|
| Selection | Identify relevant events |
| Filtering | Remove irrelevant activity |
| Aggregation | Summarise related events |
| Threshold | Identify unusual frequency |
| Time window | Define the period of interest |
| Correlation | Connect related activity |
| Exclusion | Account for known legitimate activity |
| Output | Provide investigation context |

## Example: Multiple Failed Logons

### KQL

```kql
SecurityEvent
| where TimeGenerated > ago(1h)
| where EventID == 4625
| summarize
    FailureCount = count(),
    Accounts = make_set(TargetUserName)
    by IpAddress, Computer, bin(TimeGenerated, 5m)
| where FailureCount >= 10
| order by FailureCount desc
```

### SPL

```spl
index=windows EventCode=4625
| bin _time span=5m
| stats count AS failures
        values(user) AS accounts
        by _time, src, host
| where failures >= 10
| sort - failures
```

These examples depend on the available event fields and data ingestion configuration.

## Example: New Local Account Creation

Windows Security Event ID 4720 records user account creation.

### KQL

```kql
SecurityEvent
| where TimeGenerated > ago(24h)
| where EventID == 4720
| project
    TimeGenerated,
    Computer,
    SubjectUserName,
    TargetUserName
| order by TimeGenerated desc
```

Investigate:

- Who created the account?
- Was the activity approved?
- Was the account created on an expected host?
- Was it assigned privileged access?
- Was it used shortly after creation?

## Example: Unexpected Service Installation

### KQL

```kql
SecurityEvent
| where TimeGenerated > ago(24h)
| where EventID == 4697
| project
    TimeGenerated,
    Computer,
    SubjectUserName,
    ServiceName,
    ServiceFileName
| order by TimeGenerated desc
```

Event 4697 requires appropriate auditing.

System Event ID 7045 is another useful source for service installation activity.

## Correlation Logic

Correlation links related events across a defined period.

Example:

- Multiple failed authentication attempts.
- A successful authentication from the same source.
- Subsequent privileged activity.

Correlation requires reliable identifiers and timestamps.

Potential correlation keys include:

- User identity
- Hostname
- IP address
- Logon ID
- Process ID
- Session ID
- Cloud resource ID

Avoid relying on IP address alone where NAT, proxies or shared infrastructure may affect attribution.

## Threshold Selection

Thresholds should be based on:

- Normal activity
- Environment size
- Account behaviour
- Time of day
- Asset criticality
- Threat scenario

A threshold that works in a small environment may generate excessive alerts in a large enterprise.

## Detection Context

Include useful context in alert output:

- Event timestamp
- Hostname
- User
- Source address
- Destination address
- Process information
- Relevant event details
- Detection rationale

Avoid producing alerts that require analysts to manually reconstruct basic context from unrelated data sources.

## Exclusions

Exclusions should be:

- Narrowly scoped
- Justified
- Documented
- Reviewed periodically
- Approved where required

Avoid broad exclusions for administrative accounts, entire subnets or common system processes.

## Rule Validation

Before deployment, verify:

- Expected activity triggers the rule.
- Unrelated activity does not trigger it unnecessarily.
- Missing fields do not break the logic.
- Time windows behave as expected.
- Duplicate events are handled appropriately.
- Alert output contains useful context.
- Performance is acceptable.

## Further Reading

- Microsoft KQL: https://learn.microsoft.com/azure/data-explorer/kusto/query/
- Splunk Search Reference: https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/
- Sigma: https://sigmahq.io/
- Elastic Detection Engineering: https://www.elastic.co/guide/en/security/current/detection-engine-overview.html

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
