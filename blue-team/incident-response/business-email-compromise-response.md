# Business Email Compromise Response

## Overview

Business email compromise (BEC) involves the abuse of email accounts, identities or communication processes to facilitate fraud, data theft or unauthorised access.

Common scenarios include:

- Compromised employee mailboxes.
- Executive impersonation.
- Supplier or invoice redirection fraud.
- Payroll diversion.
- Unauthorised mailbox forwarding.
- Malicious OAuth application consent.
- Conversation hijacking.
- Domain spoofing.

BEC may occur without malware or obvious endpoint compromise.

## Immediate priorities

1. Determine whether an account or communication process is compromised.
2. Identify financial transactions or payment instructions affected.
3. Contact relevant financial institutions promptly where fraud is suspected.
4. Contain compromised accounts and sessions.
5. Preserve original email evidence.
6. Identify recipients and related conversations.
7. Escalate to finance, management, legal and relevant external parties.

Where funds may have been transferred, speed matters. Contact the relevant bank or payment provider through verified contact details.

## Account investigation

Review:

- Successful and failed sign-ins.
- Unusual IP addresses and locations.
- New devices.
- MFA changes.
- Password resets.
- Session activity.
- Application consent grants.
- Mailbox delegation.
- Inbox rules.
- Forwarding settings.
- Sent and deleted messages.
- Unusual mailbox access.

Look for activity that predates the first reported fraudulent email.

## Email investigation

Preserve original messages, including headers.

Review:

- Sender and reply-to addresses.
- Return-Path.
- Received headers.
- Authentication results.
- SPF, DKIM and DMARC results.
- Message-ID.
- Sending infrastructure.
- URLs and attachments.
- Thread history.
- Changes to payment instructions.
- Display name impersonation.

Do not rely on the display name or visible sender address alone.

## Mailbox persistence

Investigate:

- Inbox rules.
- Hidden or unusual rules.
- Automatic forwarding.
- Delegated access.
- Shared mailbox permissions.
- OAuth application permissions.
- Suspicious connected applications.
- Unusual mail clients or protocols.

Preserve relevant configuration and audit records before removing malicious rules where practical.

## Containment

Possible actions:

- Disable or restrict the compromised account.
- Reset credentials through a trusted process.
- Revoke sessions and tokens.
- Review MFA registration.
- Remove malicious forwarding rules.
- Remove unauthorised delegates.
- Revoke malicious application consent.
- Block malicious sender infrastructure.
- Search for related messages.
- Notify affected recipients through approved channels.

Consider other accounts with similar access or shared credentials.

## Financial fraud response

If payment fraud is suspected:

- Contact the bank or payment provider immediately.
- Request a recall, hold or investigation where available.
- Preserve payment instructions and transaction details.
- Notify finance and management.
- Record the time fraud was identified and reported.
- Follow internal fraud and law enforcement reporting procedures.

Do not assume a payment can be recovered.

## Scope assessment

Determine:

- Which mailboxes were accessed?
- What messages were read or sent?
- Were attachments accessed?
- Were personal or financial records exposed?
- Were payment instructions changed?
- Which recipients received fraudulent messages?
- Were external suppliers or customers affected?
- Were other accounts compromised?

## Recovery

- Validate account security.
- Confirm malicious access has been removed.
- Review mailbox rules and delegation.
- Confirm MFA and recovery methods.
- Notify affected users and contacts.
- Monitor for renewed suspicious activity.
- Validate payment and supplier processes.

## Prevention opportunities

- Phishing-resistant MFA where feasible.
- Strong identity monitoring.
- Mailbox rule alerting.
- External sender indicators.
- DMARC enforcement appropriate to the environment.
- Out-of-band verification of bank detail changes.
- Dual approval for payment changes.
- Supplier contact verification.
- Staff awareness and reporting processes.
- Restricted application consent.

## Closure criteria

- [ ] Compromised accounts identified.
- [ ] Sessions and credentials secured.
- [ ] Malicious rules and permissions removed.
- [ ] Related messages identified.
- [ ] Recipients notified where required.
- [ ] Financial institutions contacted where applicable.
- [ ] Potential data exposure assessed.
- [ ] Recovery validated.
- [ ] Corrective actions assigned.

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
