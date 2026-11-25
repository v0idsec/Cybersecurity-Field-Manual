# Incident Containment

## Overview

Containment limits the ability of an attacker or malicious process to continue operating.

The objective is to reduce further damage while preserving evidence and maintaining critical business operations where possible.

Containment is not eradication. A compromised account may be disabled while malicious sessions, tokens or persistence mechanisms remain active.

## Before containment

Where circumstances permit:

1. Confirm the incident and immediate risk.
2. Identify affected systems and business owners.
3. Preserve volatile or time-sensitive evidence where practical.
4. Confirm who can authorise the action.
5. Assess operational and safety implications.
6. Select the least disruptive effective action.
7. Record the decision and expected outcome.
8. Prepare a rollback or recovery approach where appropriate.

In an active destructive incident, immediate containment may take priority over comprehensive evidence collection. Document the trade-off.

## Endpoint containment

Possible actions:

- Isolate the endpoint through EDR.
- Disconnect network access.
- Restrict access to sensitive services.
- Disable local or domain accounts where justified.
- Block known malicious indicators.
- Remove the endpoint from critical trust relationships.
- Preserve forensic images or relevant artefacts.

Consider whether isolation will interrupt business-critical or safety-related functions.

Do not power off a system automatically. Volatile memory and active network state may contain useful evidence. Follow the incident plan and forensic advice.

## Identity containment

For suspected account compromise:

- Disable or restrict the affected account.
- Revoke active sessions and refresh tokens.
- Reset credentials through a trusted process.
- Review and remove unauthorised authentication methods.
- Review MFA registration and recovery methods.
- Remove suspicious application consents.
- Disable compromised access keys and secrets.
- Review privileged role assignments.
- Investigate related accounts and delegated access.

A password reset alone may not invalidate all existing sessions or tokens.

For service accounts and workload identities, identify dependent applications before disabling credentials. Coordinate rotation to avoid unintended outages.

## Network containment

Possible controls:

- Block malicious destinations.
- Restrict outbound access.
- Apply temporary firewall rules.
- Segment affected networks.
- Disable exposed services.
- Restrict remote access.
- Quarantine compromised network segments.
- Apply temporary access control restrictions.

Ensure temporary rules are documented, monitored and assigned an expiry or review date.

## Cloud containment

Possible actions:

- Revoke compromised access keys.
- Disable suspicious identities.
- Revoke sessions where supported.
- Remove malicious role assignments.
- Restrict access to affected storage.
- Disable compromised application credentials.
- Restrict public exposure.
- Preserve relevant audit logs.
- Suspend suspicious automation or integrations.

Avoid deleting suspicious cloud resources before collecting relevant configuration, metadata and audit evidence.

## Email containment

Possible actions:

- Disable or restrict a compromised mailbox.
- Revoke sessions.
- Remove malicious inbox rules.
- Remove unauthorised forwarding.
- Review delegated mailbox access.
- Block malicious sender infrastructure.
- Search for and remove malicious messages where authorised.
- Notify affected recipients.
- Investigate related accounts.

Preserve original message content and headers before modifying or deleting messages.

## Short-term and long-term containment

| Type | Purpose | Example |
|---|---|---|
| Short-term | Stop immediate activity | Isolate a compromised endpoint |
| Long-term | Maintain a controlled environment during remediation | Restrict a compromised service to a dedicated recovery segment |

Long-term containment should not become a permanent substitute for remediation.

## Containment validation

After action, verify:

- The affected asset or identity is restricted as intended.
- Malicious activity has stopped or materially reduced.
- No obvious alternate access path remains.
- Related systems have been assessed.
- Logging remains available.
- Business owners understand service impacts.
- The action is recorded in the incident timeline.

## Common mistakes

- Resetting a password without revoking sessions.
- Isolating one endpoint while ignoring lateral movement.
- Blocking a single IP address without investigating related infrastructure.
- Deleting suspicious files before preserving evidence.
- Disabling service accounts without assessing dependencies.
- Making broad firewall changes without change control.
- Assuming containment means the attacker has been removed.
- Failing to monitor after containment.

## Containment record

Record:

- Action performed.
- Asset or identity affected.
- Reason for the action.
- Authorising person.
- Person performing the action.
- Timestamp.
- Expected result.
- Actual result.
- Evidence collected beforehand.
- Business impact.
- Follow-up actions.

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
