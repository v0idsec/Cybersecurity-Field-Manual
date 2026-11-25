# Business Email Compromise (BEC)

## Overview

Business Email Compromise is a form of fraud involving the impersonation or compromise of business communications to manipulate people into transferring money, disclosing information or changing business processes.

BEC incidents can involve compromised legitimate accounts or carefully crafted impersonation messages.

## Common BEC Scenarios

### Executive Impersonation

An attacker impersonates an executive and requests an urgent payment, confidential information or unusual action.

### Invoice Fraud

An attacker impersonates a supplier and requests that payment details be changed.

### Supplier Account Compromise

A legitimate supplier mailbox is compromised and used to send fraudulent instructions.

### Payroll Diversion

An attacker requests a change to an employee's bank details.

### Lawyer or Professional Services Impersonation

An attacker impersonates a solicitor, accountant or other professional to influence a financial transaction.

### Account Takeover

An attacker gains access to a legitimate mailbox and uses it to manipulate ongoing conversations.

## Warning Signs

- Urgent payment requests
- Unusual confidentiality demands
- Unexpected bank detail changes
- Requests to bypass normal approval processes
- New contact details
- Unexpected changes to invoice formats
- Unusual sender or Reply-To addresses
- Unexpected external forwarding
- Suspicious mailbox rules

## Investigation

### Email Evidence

Collect:
- Original messages
- Full headers
- Message IDs
- Sender and recipient
- Attachments
- Related conversation history
- Mail gateway records

### Identity Evidence

Review:
- Successful and failed sign-ins
- Unusual IP addresses
- New devices
- MFA activity
- Password resets
- New authentication methods
- OAuth grants
- Session activity

### Mailbox Evidence

Investigate:
- Inbox rules
- Forwarding settings
- Delegated access
- Sent messages
- Deleted messages
- Mailbox access logs
- Unusual message searches

### Financial Evidence

Where a financial transaction is involved, coordinate with finance and relevant external institutions.

Record:
- Payment amount
- Currency
- Beneficiary
- Destination account
- Payment time
- Transaction reference
- Approval history
- Recovery attempts

## Containment

Potential actions:

- Secure compromised accounts.
- Revoke sessions.
- Reset credentials.
- Review MFA methods.
- Remove unauthorised forwarding.
- Remove malicious inbox rules.
- Revoke suspicious application grants.
- Notify affected correspondents.
- Contact financial institutions through verified channels.
- Stop or recall payments where possible.

## Payment Verification

Organisations should establish a trusted process for verifying payment changes.

Recommended controls:

- Independently verify changes using a known phone number.
- Require dual approval for high-value payments.
- Do not rely on contact details in the change request.
- Maintain an approved supplier record.
- Record verification.
- Apply additional checks to urgent or unusual requests.

## Example Investigation Timeline

| Event | Evidence |
|---|---|
| Initial compromise | Identity sign-in records |
| Mailbox access | Mail audit events |
| Rule creation | Mailbox configuration audit |
| Fraudulent message | Message trace and headers |
| Payment instruction | Email and finance records |
| Response | Account and payment actions |

Use actual timestamps and preserve the relevant source records.

## Recovery

- Verify account ownership.
- Reset credentials.
- Revoke active sessions.
- Review authentication methods.
- Remove unauthorised rules and forwarding.
- Confirm legitimate payment details independently.
- Monitor for further activity.
- Notify relevant parties.

## Prevention

- Enforce MFA.
- Use phishing-resistant authentication where practical.
- Apply conditional access.
- Monitor suspicious sign-ins.
- Alert on mailbox forwarding changes.
- Protect privileged accounts.
- Require independent payment verification.
- Train finance and procurement teams.
- Monitor OAuth application grants.

## Escalation

Escalate immediately if:
- Money has been transferred.
- Payment details were changed.
- A supplier account is suspected compromised.
- An executive mailbox is affected.
- Sensitive information was disclosed.
- Multiple accounts are involved.

## Common Mistakes

- Treating BEC as only an email-filtering problem.
- Failing to investigate account compromise.
- Trusting a familiar email conversation.
- Verifying payment changes using details from the suspicious message.
- Resetting passwords without revoking sessions.
- Failing to involve finance promptly.
- Delaying contact with the bank.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
