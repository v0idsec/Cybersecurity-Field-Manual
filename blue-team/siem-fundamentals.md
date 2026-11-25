# SIEM Fundamentals

## Overview

A Security Information and Event Management (SIEM) platform collects, processes, correlates and analyses security telemetry from across an environment.

SIEM platforms provide centralised visibility into activity that would otherwise be distributed across individual systems, applications and infrastructure.

## SIEM Architecture

A typical SIEM pipeline consists of:

1. Data generation
2. Collection
3. Forwarding and ingestion
4. Parsing and normalisation
5. Enrichment
6. Storage and indexing
7. Detection and correlation
8. Alerting and investigation

### Data Generation

Common sources include:

- Windows Security Event Logs
- Sysmon
- Linux authentication and system logs
- Firewall events
- DNS queries
- Proxy logs
- VPN authentication
- Active Directory
- Microsoft Entra ID
- Cloud audit logs
- Endpoint security products
- Application audit logs

### Collection

Telemetry can be collected through:

- Agents installed on endpoints
- Syslog forwarding
- API integrations
- Cloud-native connectors
- Windows Event Forwarding
- Network collectors
- File-based ingestion

Collection methods should be selected based on reliability, performance, security and operational requirements.

### Parsing and Normalisation

Raw events often use different formats and field names.

Normalisation converts events into a consistent structure.

Common fields include:

| Field | Description |
|---|---|
| timestamp | Event occurrence time |
| hostname | Reporting system |
| username | Associated account |
| source_ip | Originating IP address |
| destination_ip | Destination IP address |
| event_id | Source event identifier |
| process_name | Associated process |
| action | Recorded activity |
| result | Success, failure or other outcome |

Normalisation makes correlation across different platforms more reliable.

## Detection Types

### Signature-Based Detection

Identifies known indicators or specific event patterns.

Examples:

- Known malicious hashes
- Known malicious IP addresses
- Specific process execution patterns
- Known attack tool indicators

### Behaviour-Based Detection

Identifies activity that deviates from expected behaviour.

Examples:

- Unusual login locations
- Abnormal process execution
- Unexpected administrative activity
- Unusual data transfer volumes

### Correlation-Based Detection

Combines multiple events to identify a broader attack sequence.

Example:

1. Multiple failed logins
2. Successful authentication
3. Privileged group membership change
4. Unusual administrative activity

Each event may be legitimate in isolation. Their combination may indicate account compromise.

## Detection Engineering Considerations

Good detections should have:

- A clearly defined threat or behaviour
- Required telemetry sources
- Documented logic
- Expected false-positive conditions
- Investigation guidance
- Severity and priority
- Testing evidence
- An owner and review date

## SIEM Query Concepts

| Operation | Purpose |
|---|---|
| Filtering | Identify events matching conditions |
| Aggregation | Count or summarise events |
| Grouping | Group by user, host or source |
| Time windows | Identify activity within a period |
| Joins | Combine related datasets |
| Baselines | Compare activity against expected behaviour |
| Correlation | Connect related activity across event sources |

## Data Quality and Coverage

A SIEM is only as useful as the telemetry it receives.

Regularly assess:

- Missing log sources
- Ingestion delays
- Parsing failures
- Time synchronisation
- Retention periods
- Duplicate events
- Collection agent health
- Unexpected drops in event volume

A sudden reduction in telemetry may itself indicate a security issue.

## Common SIEM Platforms

- Microsoft Sentinel
- Splunk Enterprise Security
- Elastic Security
- IBM QRadar
- Google Security Operations
- Wazuh

## Operational Considerations

- Apply least privilege to SIEM access.
- Restrict access to sensitive logs.
- Protect ingestion credentials.
- Monitor changes to logging configurations.
- Retain evidence in accordance with organisational requirements.
- Monitor SIEM availability and ingestion health.
- Avoid collecting unnecessary sensitive information.

## Further Reading

- Microsoft Sentinel: https://learn.microsoft.com/azure/sentinel/
- Splunk: https://docs.splunk.com/
- Elastic Security: https://www.elastic.co/guide/en/security/current/index.html
- Sigma: https://sigmahq.io/
- MITRE ATT&CK: https://attack.mitre.org/

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
