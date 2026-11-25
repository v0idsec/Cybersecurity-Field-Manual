# SIEM Detection and Correlation

## Overview

SIEM detection engineering turns security telemetry into actionable alerts.

Effective detections identify suspicious activity, provide sufficient investigation context and minimise unnecessary alert volume.

## Detection Lifecycle

1. Identify a threat or behaviour.
2. Define the detection objective.
3. Identify required telemetry.
4. Develop detection logic.
5. Test against known activity.
6. Assess false positives.
7. Deploy and monitor.
8. Tune and maintain.

## Detection Design

Every detection should define:

| Attribute | Description |
|---|---|
| Name | Unique detection name |
| Objective | Behaviour being identified |
| Data sources | Required telemetry |
| Logic | Query or rule |
| Severity | Expected risk |
| ATT&CK mapping | Relevant technique, where applicable |
| False positives | Known benign conditions |
| Investigation | Analyst steps |
| Response | Recommended actions |
| Owner | Responsible team |
| Review date | Maintenance schedule |

## Detection Logic

### Threshold-Based

Triggers when an activity exceeds a defined threshold.

Example:

- More than 10 failed authentication attempts from one source within five minutes.

Thresholds should account for normal behaviour and environment size.

### Sequence-Based

Identifies a sequence of related events.

Example:

1. Successful authentication.
2. Privileged group membership change.
3. Administrative service creation.

### Anomaly-Based

Identifies activity outside an established baseline.

Examples:

- Unusual login time
- Unexpected data transfer volume
- New administrative activity
- Unusual process execution

### Correlation-Based

Combines information from different telemetry sources.

Examples:

- Failed logins followed by a successful login.
- Suspicious PowerShell execution followed by external network communication.
- New service installation followed by unusual outbound connections.

## Example: Failed Authentication Detection

### Microsoft Sentinel KQL

```kql
SecurityEvent
| where TimeGenerated > ago(1h)
| where EventID == 4625
| summarize
    FailedAttempts = count(),
    TargetAccounts = dcount(TargetUserName)
    by IpAddress, Computer, bin(TimeGenerated, 5m)
| where FailedAttempts >= 10
| order by FailedAttempts desc
```

Field availability depends on the connector and event normalisation configuration.

### Splunk SPL

```spl
index=windows EventCode=4625
| bin _time span=5m
| stats count AS failed_attempts
        dc(TargetUserName) AS target_accounts
        by _time, src, host
| where failed_attempts >= 10
| sort - failed_attempts
```

Field names depend on the deployed data model and parsing configuration.

## Example: Suspicious PowerShell Activity

### Microsoft Sentinel KQL

```kql
WindowsEvent
| where TimeGenerated > ago(24h)
| where EventID == 4104
| where EventData has_any (
    "DownloadString",
    "EncodedCommand",
    "FromBase64String"
)
| project
    TimeGenerated,
    Computer,
    EventData
| order by TimeGenerated desc
```

This is a starting point, not a complete malicious PowerShell detector.

These strings can occur in legitimate scripts. Validate the script content, user, host and execution context.

## Sigma Rules

Sigma provides a vendor-neutral format for describing detection logic.

Example:

```yaml
title: Suspicious PowerShell Download Activity
id: 7d4b6f22-8c1a-4c2d-a3e1-1f3d8f7c2a10
status: experimental
description: Detects PowerShell commands containing common download methods.
logsource:
    product: windows
    category: process_creation
detection:
    selection:
        Image|endswith: '\powershell.exe'
        CommandLine|contains:
            - 'DownloadString'
            - 'Invoke-WebRequest'
    condition: selection
falsepositives:
    - Approved administration scripts
    - Software deployment activity
level: medium
```

This example is illustrative. Validate field mappings and rule compatibility with the target SIEM.

## MITRE ATT&CK Mapping

Map detections to relevant ATT&CK techniques where appropriate.

Examples:

| Activity | ATT&CK Technique |
|---|---|
| Valid account abuse | T1078 |
| PowerShell execution | T1059.001 |
| Scheduled task persistence | T1053.005 |
| Remote services | T1021 |
| Account discovery | T1087 |
| Windows service creation | T1543.003 |

ATT&CK mappings should reflect the behaviour actually detected, not simply the general subject of the alert.

## False Positive Management

Common causes include:

- Administrative scripts
- Software deployment
- Vulnerability scanning
- Backup software
- Monitoring tools
- Approved penetration testing
- Scheduled maintenance

Tune detections carefully.

Avoid broad exclusions that could hide genuine malicious activity.

## Detection Testing

Validate detections using:

- Controlled test events
- Atomic Red Team
- Purple-team exercises
- Historical event replay
- Simulated log generation
- Approved adversary emulation

Testing must be authorised and performed within the approved environment.

## Detection Health Metrics

Track:

- Alert volume
- True-positive rate
- False-positive rate
- Mean time to detect
- Mean time to triage
- Detection coverage
- Telemetry availability
- Rule execution failures
- Uninvestigated alert backlog

Metrics should be interpreted in context rather than used as isolated performance targets.

## Maintenance

Review detections when:

- Logging sources change.
- Systems are migrated.
- Applications are updated.
- New attack techniques become relevant.
- False-positive rates increase.
- Detection requirements change.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
