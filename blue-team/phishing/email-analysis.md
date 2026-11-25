# Email Analysis

## Overview

Email analysis is the process of examining suspicious messages to determine whether they are legitimate, unwanted, deceptive or malicious.

The investigation should consider the message's content, sender, delivery path, authentication results, URLs, attachments and surrounding activity.

## Initial Triage

Record the following:

| Field | Description |
|---|---|
| Sender | Displayed sender address |
| Reply-To | Address receiving replies |
| Recipient | Intended recipient |
| Subject | Message subject |
| Received time | Delivery timestamp |
| Message ID | Unique message identifier |
| Attachments | Names and file types |
| URLs | Embedded destinations |
| Authentication | SPF, DKIM and DMARC results |
| User interaction | Clicks, downloads or replies |

Preserve the original email before performing detailed analysis.

## Common Phishing Indicators

### Sender Anomalies

Look for:

- Lookalike domains
- Misspelled organisation names
- Unexpected external senders
- Display-name impersonation
- Mismatched Reply-To addresses
- Unusual sending infrastructure

Example:

```text
Display name: Microsoft Support
From: support@microsoft-security-example.com
Reply-To: account-help@example.net
```

The example is illustrative. A suspicious-looking address requires investigation rather than automatic classification.

### Message Content

Common indicators include:

- Urgent requests
- Threats of account suspension
- Unexpected invoices
- Password reset requests
- Requests for gift cards or payments
- Unexpected document sharing
- Requests to bypass normal procedures
- Unusual confidentiality demands

### Links

Look for:

- Mismatched link text and destination
- URL shorteners
- Unexpected domains
- Lookalike login pages
- Redirect chains
- Unusual URL paths
- Unexpected file downloads

Do not click suspicious links during initial triage.

### Attachments

Potentially suspicious file types include:

- Executables
- Scripts
- Macro-enabled Office documents
- ISO and disk image files
- Archive files
- HTML attachments
- Shortcut files

File type alone does not prove malicious intent.

## Email Authentication

Review SPF, DKIM and DMARC results.

| Control | What it checks |
|---|---|
| SPF | Whether the sending host is authorised by the domain's SPF policy |
| DKIM | Whether a message has a valid domain-associated cryptographic signature |
| DMARC | Whether SPF/DKIM results align with the visible From domain and domain policy |

A successful authentication result does not guarantee that an email is safe. A compromised legitimate account can send phishing messages.

## Message Context

Ask:

- Was the message expected?
- Does the sender normally communicate this way?
- Is the request consistent with established business processes?
- Does the message contain unexpected financial instructions?
- Is the recipient normally involved in this activity?
- Was the message sent to multiple employees?
- Are similar messages appearing elsewhere?

## User Interaction

Determine whether the recipient:

- Opened the email
- Clicked a link
- Entered credentials
- Approved an authentication request
- Downloaded an attachment
- Executed a file
- Replied to the sender
- Transferred money or disclosed information

Treat credential submission and financial transfers as high-priority escalation events.

## Classification

Suggested classifications:

| Classification | Meaning |
|---|---|
| Benign | Legitimate communication |
| Spam | Unwanted but not necessarily deceptive |
| Suspicious | Indicators require further investigation |
| Phishing | Deceptive communication |
| Malicious | Confirmed malicious content or delivery |
| BEC | Business email impersonation or account compromise |

## Reporting

Record:
- Message identifiers
- Relevant headers
- Sender and recipient
- Suspicious URLs
- Attachment hashes
- Authentication results
- User interaction
- Related security alerts
- Final classification
- Recommended actions

## Common Mistakes

- Trusting display names.
- Treating SPF success as proof of legitimacy.
- Ignoring Reply-To mismatches.
- Clicking links during initial triage.
- Opening attachments on production systems.
- Deleting the original email before preserving evidence.
- Failing to check whether other users received the same message.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
