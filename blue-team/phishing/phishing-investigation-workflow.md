# Phishing Investigation Workflow

## Overview

This guide provides a repeatable process for investigating suspected phishing messages and determining whether users, endpoints or business systems were affected.

## Phase 1: Intake

Record:
- Reporter
- Affected user
- Date and time reported
- Original message
- Subject
- Sender
- Recipient
- Message ID
- Suspicious URLs
- Attachments
- Initial user interaction

Preserve the original message in its native format where possible.

## Phase 2: Initial Classification

Determine whether the message is:

- Benign
- Spam
- Suspicious
- Phishing
- Malicious
- Business Email Compromise

Assign an initial severity based on potential impact and user interaction.

## Phase 3: Determine Exposure

Ask the recipient:

- Did you open the message?
- Did you click a link?
- Did you enter credentials?
- Did you approve an authentication request?
- Did you download an attachment?
- Did you execute a file?
- Did you reply?
- Did you provide payment or confidential information?

Do not assume that opening an email means the endpoint is compromised.

## Phase 4: Analyse the Message

Review:
- Sender identity
- Reply-To
- Return-Path
- Received headers
- SPF, DKIM and DMARC
- Subject and message body
- URLs
- Attachments
- Similar messages

See:
- [Email Analysis](email-analysis.md)
- [Header Analysis](header-analysis.md)
- [URL and Attachment Analysis](url-and-attachment-analysis.md)

## Phase 5: Identify Campaign Scope

Determine whether other recipients were targeted.

Search relevant mail systems for:
- Sender address
- Subject
- Message ID
- Attachment hashes
- URL domains
- Similar message content

Preserve search parameters and results.

## Phase 6: Investigate Endpoint Activity

If a user interacted with the message, review:
- Browser history
- Download records
- Process creation
- EDR detections
- File creation
- PowerShell activity
- DNS queries
- Network connections

Determine whether suspicious content executed or additional activity occurred.

## Phase 7: Investigate Identity Activity

If credentials may have been disclosed, investigate:
- Sign-in history
- Failed and successful authentication
- MFA prompts
- New devices
- New authentication methods
- Password resets
- Token activity
- OAuth grants
- Privileged actions

Treat suspected credential disclosure as a priority.

## Phase 8: Containment

Depending on evidence and severity:

- Remove or quarantine malicious messages.
- Block confirmed malicious indicators.
- Isolate affected endpoints.
- Revoke sessions.
- Reset compromised credentials.
- Disable compromised accounts temporarily.
- Remove malicious mailbox rules.
- Restrict suspicious application grants.
- Escalate financial fraud.

Coordinate actions with incident response and business owners.

## Phase 9: Eradication and Recovery

Potential activities:
- Remove malicious files.
- Rebuild affected systems where necessary.
- Restore trusted configurations.
- Re-enable accounts after verification.
- Review authentication methods.
- Remove unauthorised forwarding rules.
- Validate endpoint security controls.
- Monitor for recurrence.

## Phase 10: Reporting

Record:
- Incident summary
- Scope
- Affected users
- Message identifiers
- Indicators
- Evidence
- User interaction
- Confirmed impact
- Containment actions
- Recovery actions
- Outstanding risks
- Recommendations

## Escalation Criteria

Escalate immediately if:
- Credentials were submitted.
- MFA was approved unexpectedly.
- An attachment executed.
- Malware was detected.
- An account performed suspicious actions.
- Sensitive information was disclosed.
- A financial transfer was requested or completed.
- Privileged accounts were targeted.
- Multiple users are affected.

## Closure Criteria

An investigation may be closed when:
- Scope has been assessed.
- Relevant evidence has been preserved.
- Affected users and systems have been identified.
- Necessary containment is complete.
- Outstanding risks are documented.
- Required stakeholders have been informed.
- Findings and recommendations are recorded.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
