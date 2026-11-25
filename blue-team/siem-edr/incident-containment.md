# Incident Containment

## Overview

Incident containment limits the spread and impact of a security incident while preserving the ability to investigate and recover.

Containment decisions should be based on incident severity, business impact, operational requirements and the available evidence.

## Containment Objectives

- Stop ongoing malicious activity.
- Prevent further unauthorised access.
- Limit lateral movement.
- Protect sensitive information.
- Preserve evidence.
- Maintain essential business operations where possible.

## Before Containment

Establish:

- Incident severity
- Affected systems
- Affected accounts
- Current threat activity
- Business criticality
- Potential operational impact
- Available response capabilities
- Required approvals

Where practical, preserve volatile evidence before taking disruptive action.

Do not delay urgent containment when ongoing activity presents an immediate risk.

## Endpoint Containment

Possible actions:

- Isolate affected endpoints using EDR.
- Disable suspicious processes.
- Quarantine malicious files.
- Restrict endpoint network access.
- Remove compromised devices from sensitive segments.

Considerations:

- Isolation may disrupt business operations.
- Servers may support critical services.
- Remote access may be required for investigation.
- Evidence may be lost if systems are powered off.

Avoid shutting down systems unless justified by the incident and response procedures.

## Account Containment

Possible actions:

- Disable compromised accounts.
- Revoke active sessions.
- Revoke refresh tokens.
- Reset credentials.
- Require MFA re-registration where appropriate.
- Remove unauthorised group membership.
- Disable compromised service principals.
- Restrict suspicious application consent.

Before changing credentials, identify dependencies such as service accounts, scheduled tasks and integrations.

## Network Containment

Possible actions:

- Block malicious IP addresses.
- Restrict suspicious domains.
- Disable compromised VPN access.
- Apply firewall restrictions.
- Isolate affected network segments.
- Restrict access to exposed services.

Validate that proposed blocks will not disrupt legitimate business traffic.

## Cloud Containment

Possible actions:

- Disable compromised access keys.
- Revoke compromised sessions.
- Remove unauthorised role assignments.
- Disable suspicious applications.
- Restrict exposed storage.
- Review security group and firewall rules.
- Restrict affected workloads.

Preserve cloud audit logs and configuration history.

## Email Containment

Possible actions:

- Remove malicious messages from mailboxes.
- Block malicious sender infrastructure.
- Block malicious URLs and attachments.
- Disable compromised mail accounts.
- Revoke active sessions.
- Review forwarding rules and mailbox permissions.

Where possible, identify all recipients before removing messages.

## Containment Prioritisation

| Priority | Example | Response |
|---|---|---|
| Critical | Active ransomware or widespread compromise | Immediate coordinated containment |
| High | Compromised privileged account | Urgent account and access containment |
| Medium | Isolated suspicious endpoint | Investigate and contain as appropriate |
| Low | Blocked low-confidence activity | Monitor and validate |

Severity should be adjusted based on actual business and security impact.

## Evidence Preservation

Before or during containment, where practical:

- Record system state.
- Preserve relevant logs.
- Capture process and network information.
- Export EDR investigation data.
- Record account and configuration changes.
- Hash acquired files.
- Maintain chain-of-custody records where required.

Document all response actions and timestamps.

## Validation

After containment:

1. Confirm the affected account or endpoint is restricted.
2. Confirm malicious activity has stopped.
3. Check for related compromised systems.
4. Review authentication activity.
5. Confirm persistence has been addressed.
6. Monitor for attempted re-entry.
7. Verify that logging remains operational.

## Recovery Considerations

Containment is not the same as eradication or recovery.

Before restoring normal operations:

- Identify the initial access method.
- Remove malicious persistence.
- Remediate exploited vulnerabilities.
- Rotate affected credentials.
- Restore from trusted sources where necessary.
- Validate system integrity.
- Increase monitoring.
- Obtain recovery approval.

## Documentation

Record:

- Incident identifier
- Containment decision
- Approving authority
- Affected assets
- Actions performed
- Timestamps
- Evidence preserved
- Business impact
- Validation results
- Remaining risks

## Operational Warning

Containment actions can cause significant disruption.

Do not disable accounts, isolate critical systems, modify firewall rules or remove cloud resources without appropriate authority and consideration of operational impact, except where an established emergency procedure explicitly permits immediate action.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
