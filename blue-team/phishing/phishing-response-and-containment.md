# Phishing Response and Containment

## Overview

Phishing response focuses on reducing the impact of malicious messages, limiting account or endpoint compromise and preventing further exposure.

Response should be coordinated with the organisation's incident response process.

## Response Priorities

1. Protect people and critical business operations.
2. Prevent further credential disclosure.
3. Contain affected accounts and endpoints.
4. Remove malicious messages and content.
5. Preserve evidence.
6. Determine the extent of compromise.
7. Recover affected systems.
8. Improve controls.

## Scenario 1: User Received a Suspicious Email

Actions:

- Preserve the original message.
- Collect headers.
- Review sender and recipient.
- Analyse URLs and attachments safely.
- Search for other recipients.
- Classify the message.
- Remove or quarantine confirmed malicious messages.
- Notify affected users where appropriate.

## Scenario 2: User Clicked a Suspicious Link

Determine:
- Which URL was accessed?
- When was it accessed?
- Did it redirect?
- Was a file downloaded?
- Were credentials entered?
- Did the browser trigger security alerts?

Actions may include:
- Preserve browser and endpoint evidence.
- Review EDR telemetry.
- Inspect DNS and proxy activity.
- Block confirmed malicious destinations.
- Assess account exposure.
- Escalate if credentials were submitted.

A link click alone does not prove compromise.

## Scenario 3: Credentials Were Submitted

Treat as a potential identity compromise.

Actions may include:
- Reset credentials using an approved process.
- Revoke active sessions.
- Review authentication logs.
- Review MFA registrations.
- Investigate OAuth grants.
- Check mailbox rules and forwarding.
- Review privileged actions.
- Monitor for suspicious sign-ins.

Do not assume a password reset alone resolves session or token compromise.

## Scenario 4: Attachment Was Executed

Actions may include:
- Preserve relevant endpoint evidence.
- Isolate the endpoint where justified.
- Review process trees.
- Examine dropped files.
- Review persistence mechanisms.
- Inspect network activity.
- Acquire memory where appropriate.
- Escalate to malware analysis or incident response.

Avoid powering down a potentially compromised system before considering volatile evidence and operational requirements.

## Scenario 5: Business Email Compromise

Actions may include:
- Contact finance through a verified channel.
- Stop or recall payments where possible.
- Notify the relevant bank or financial institution.
- Secure affected accounts.
- Revoke sessions.
- Review mailbox access and forwarding.
- Examine sent and deleted messages.
- Identify affected correspondents.
- Preserve evidence.

Do not use contact details supplied in the suspicious message to verify payment instructions.

## Message Removal

Use approved mail administration tools to:
- Search by message ID.
- Identify recipients.
- Quarantine or remove confirmed malicious messages.
- Record the action.
- Preserve evidence before deletion where possible.

Avoid broad deletion based only on a sender display name or subject.

## Blocking Indicators

Potential indicators:
- Sender addresses
- Domains
- URLs
- IP addresses
- Attachment hashes
- File names
- Certificate information

Use confidence and scope when implementing blocks.

A shared hosting IP or legitimate cloud service may serve unrelated customers. Avoid broad blocking without impact assessment.

## User Communication

Notify users using approved channels.

A notification should explain:
- What happened
- What action is required
- Whether the user needs to change credentials
- How to report further activity
- Where to obtain support

Avoid blame or embarrassment.

## Recovery

Validate:
- Credentials and authentication methods
- Mailbox rules
- Account permissions
- Endpoint health
- Security tooling
- User access
- Business processes
- Monitoring

## Post-Incident Review

Review:
- Initial detection
- User reporting
- Mail filtering
- Response time
- Containment effectiveness
- Scope assessment
- Communication
- Root cause
- Control improvements

## Common Mistakes

- Deleting evidence before collection.
- Resetting a password without revoking sessions.
- Ignoring OAuth application grants.
- Blocking shared infrastructure too broadly.
- Failing to check other recipients.
- Failing to investigate mailbox rules.
- Blaming the affected user.
- Closing an incident without validating recovery.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
