# Incident Identification and Analysis

## Overview

The identification and analysis phase determines whether suspicious activity represents a security incident and establishes its scope.

The quality of this phase directly affects containment decisions, evidence preservation and recovery.

## Initial triage

When an alert or report is received, establish:

- What activity was observed?
- Which detection or reporting source identified it?
- When did the activity occur?
- Which users, devices, applications or services are involved?
- Is the activity continuing?
- Is there evidence of compromise?
- What is the potential business impact?
- Does the activity relate to an existing incident?

Record the original alert details before making changes to the affected environment.

## Validate the alert

Determine whether the detection is:

- A true positive.
- A false positive.
- A benign but unusual activity.
- A duplicate alert.
- An inconclusive event requiring further investigation.

Do not close an alert simply because the activity is unfamiliar or because an endpoint tool reports no malware.

Correlate available evidence across multiple sources.

## Establish the scope

Identify potentially affected:

### Users and identities

- User accounts.
- Privileged accounts.
- Service accounts.
- API identities.
- Cloud roles and service principals.
- External or federated identities.
- Shared accounts and credentials.

### Endpoints and infrastructure

- Workstations.
- Servers.
- Virtual machines.
- Network devices.
- Mobile devices.
- Containers.
- Virtual desktop infrastructure.
- Backup systems.

### Applications and services

- Email platforms.
- Identity providers.
- SaaS applications.
- Web applications.
- Databases.
- Remote access services.
- Cloud management interfaces.
- Third-party integrations.

### Information

- Personal information.
- Authentication material.
- Financial information.
- Intellectual property.
- Business records.
- System configurations.
- Backups and archives.

## Build an investigation timeline

A timeline helps reconstruct the sequence of activity.

Record:

| Field | Description |
|---|---|
| Timestamp | Time of the observation |
| Timezone | Source timezone or normalised timezone |
| Source | Log, alert, endpoint, user report or other evidence |
| Entity | Account, host, application or IP address |
| Activity | What occurred |
| Interpretation | Why it matters |
| Confidence | Confirmed, probable or unconfirmed |
| Evidence reference | Link or identifier for supporting evidence |

Example:

| Time (UTC) | Source | Activity | Assessment |
|---|---|---|---|
| 09:12 | Identity logs | Unusual sign-in from a new location | Requires validation |
| 09:16 | Identity logs | MFA challenge approved | Potential account compromise |
| 09:21 | Cloud audit logs | New application consent granted | Suspicious privilege or access change |
| 09:28 | EDR | Unusual process execution on user endpoint | Investigate possible endpoint involvement |

This is an illustrative example, not a confirmed attack sequence.

## Investigation areas

### Authentication

Review:

- Successful and failed logins.
- New devices and locations.
- MFA challenges and outcomes.
- Session creation and revocation.
- Password and recovery method changes.
- New authentication methods.
- Privileged authentication.
- Conditional access decisions.
- Token and application consent activity.

### Endpoint activity

Review:

- Process creation and ancestry.
- Command-line arguments.
- File creation and modification.
- Registry changes.
- Scheduled tasks and services.
- Local account changes.
- Security tool alerts.
- Network connections.
- Script execution.
- Removable media activity.

### Network activity

Review:

- DNS requests.
- Proxy logs.
- Firewall connections.
- VPN activity.
- Unusual outbound traffic.
- Connections to suspicious infrastructure.
- Unexpected internal connections.
- Data transfer volume and timing.

### Cloud activity

Review:

- Control-plane audit logs.
- Role and policy changes.
- New access keys.
- New service principals or applications.
- Storage access.
- Security group and firewall changes.
- Snapshot and backup activity.
- Resource creation and deletion.
- Data export operations.

## Determine the attack path

Where evidence permits, establish:

1. Initial access.
2. Execution.
3. Persistence.
4. Privilege escalation.
5. Credential access.
6. Discovery.
7. Lateral movement.
8. Collection.
9. Exfiltration or impact.

Use a recognised framework such as MITRE ATT&CK to classify observed behaviours. Do not force incomplete evidence into an assumed attack narrative.

## Assess impact

Determine:

- Systems unavailable or degraded.
- Accounts accessed or controlled.
- Data accessed, altered, deleted or potentially exfiltrated.
- Privileges obtained.
- Business processes disrupted.
- Third parties affected.
- Potential safety implications.
- Recovery effort and dependencies.

Clearly distinguish confirmed data access from suspected exposure and confirmed exfiltration.

## Confidence and uncertainty

Use explicit confidence labels:

| Confidence | Meaning |
|---|---|
| Confirmed | Directly supported by reliable evidence |
| High | Strong supporting evidence, with limited uncertainty |
| Moderate | Plausible interpretation supported by some evidence |
| Low | Preliminary assessment with significant uncertainty |
| Unknown | Insufficient evidence to assess |

Document alternative explanations where appropriate.

## Escalation criteria

Escalate promptly when investigation identifies:

- Privileged account compromise.
- Active ransomware or destructive activity.
- Suspected data exfiltration.
- Widespread endpoint compromise.
- Compromise of identity infrastructure.
- Compromise of backup systems.
- Critical service disruption.
- Potential safety implications.
- Third-party or supply chain compromise.
- Potential legal or regulatory notification requirements.

## Investigation output

The initial analysis should produce:

- Incident classification.
- Current severity.
- Known affected assets and identities.
- Initial timeline.
- Confirmed findings.
- Working hypotheses.
- Outstanding questions.
- Evidence references.
- Recommended containment actions.
- Required escalations.

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
