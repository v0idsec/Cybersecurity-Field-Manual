# Behavioural Detection

## Overview

Behavioural detection identifies suspicious activity based on how users, processes, systems and applications behave.

Rather than relying exclusively on known malicious indicators, behavioural detections identify activity that may indicate compromise, misuse or policy violations.

## Behavioural Detection Concepts

### Baselines

A baseline represents expected activity within an environment.

Examples:

- Typical login hours
- Normal administrative activity
- Common process execution
- Expected network connections
- Typical data transfer volumes
- Common service account behaviour

Baselines should account for legitimate variation.

### Deviations

A deviation is activity that differs from an established baseline.

Examples:

- A service account authenticating interactively.
- An administrator logging in from an unusual location.
- A workstation initiating unexpected server connections.
- A user downloading significantly more data than normal.

A deviation is an investigation lead, not proof of malicious activity.

## User and Entity Behaviour Analytics

UEBA analyses behaviour associated with users and entities.

Entities may include:

- User accounts
- Devices
- Servers
- Applications
- Service principals
- Cloud resources

Potential signals include:

- Unusual login patterns
- Unusual resource access
- Privilege changes
- Abnormal data access
- Unexpected authentication methods

## Process Behaviour

Monitor relationships between processes.

Examples of suspicious patterns:

- Office applications launching scripting interpreters.
- Browsers spawning unexpected command-line tools.
- Unexpected processes accessing credential-related resources.
- Services launching unusual child processes.
- Processes executing from temporary directories.

Investigate process ancestry, signatures, command lines and execution context.

## Identity Behaviour

Useful detection opportunities include:

- Unusual authentication frequency
- New device registrations
- Unexpected MFA changes
- Privileged account activity
- Service account interactive logons
- Unusual application consent
- Sign-ins from unexpected locations

## Network Behaviour

Potential behavioural indicators include:

- Unusual outbound connections
- Unexpected lateral connections
- Large data transfers
- Unusual DNS query volumes
- Repeated connections to rare destinations
- Unexpected remote administration protocols

## Cloud Behaviour

Monitor:

- Unusual role assignments
- Unexpected API activity
- New access keys
- Public storage exposure
- Changes to logging configuration
- Unusual resource creation
- Unexpected geographic access

## Detection Example: Unusual Login Time

A detection may identify successful logins outside an account's normal working pattern.

Consider:

- User role
- Timezone
- Shift patterns
- Business travel
- Remote work
- Maintenance windows
- Known automation

Avoid treating working-hour deviations as inherently suspicious.

## Detection Example: Service Account Interactive Login

Service accounts commonly have defined authentication patterns.

Investigate unexpected interactive logons, especially where the account normally operates only through a service or application.

Correlate:

- Account identity
- Logon type
- Source endpoint
- Authentication method
- Recent password changes
- Privileged access
- Related process execution

## Thresholds and Statistical Models

Common approaches include:

- Fixed thresholds
- Moving averages
- Frequency analysis
- Percentile-based thresholds
- Standard deviation
- Peer-group comparison
- Time-series analysis

Choose an approach appropriate to the available data and expected behaviour.

## Baseline Maintenance

Baselines should be reviewed when:

- Working patterns change.
- New applications are deployed.
- Infrastructure is migrated.
- Business operations change.
- New users or devices are introduced.
- Seasonal activity changes.

Avoid allowing baselines to automatically learn persistent malicious behaviour.

## False Positives

Common sources include:

- Business travel
- Remote work
- Software updates
- Administrative maintenance
- Automated workloads
- Seasonal demand
- New business processes

Use contextual enrichment to improve accuracy.

## Investigation Requirements

Behavioural alerts should include:

- The observed deviation
- Expected baseline
- Relevant timeframe
- User or entity
- Related activity
- Supporting telemetry
- Detection confidence
- Suggested investigation steps

## Further Reading

- MITRE ATT&CK: https://attack.mitre.org/
- Microsoft UEBA: https://learn.microsoft.com/azure/sentinel/identify-threats-with-entity-behavior-analytics
- Elastic Security: https://www.elastic.co/guide/en/security/current/index.html

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
