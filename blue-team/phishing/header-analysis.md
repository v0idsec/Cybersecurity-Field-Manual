# Email Header Analysis

## Overview

Email headers contain routing and authentication information that can help investigators understand where a message originated and how it travelled through mail infrastructure.

Header analysis is useful for investigating:

- Sender spoofing
- Phishing
- Business Email Compromise
- Suspicious mail relays
- Authentication failures
- Message routing anomalies

## Obtaining Headers

Common email platforms provide an option to view the original message or full headers.

Examples:

- Gmail: Show original
- Outlook: View message details or view source
- Microsoft 365: Download or export the original message where supported

Preserve the original message in addition to copying header text.

## Important Headers

| Header | Purpose |
|---|---|
| From | Visible sender address |
| To | Recipient address |
| Reply-To | Address used for replies |
| Return-Path | Envelope sender information |
| Received | Mail server routing history |
| Message-ID | Message identifier |
| Date | Sender-provided message date |
| Authentication-Results | SPF, DKIM and DMARC results |
| MIME-Version | MIME message format version |
| Content-Type | Message content format |
| X-Originating-IP | Potential originating IP, if present |

Headers are not all equally trustworthy. Some can be supplied or manipulated by the sender.

## Received Headers

Mail servers commonly append `Received` headers as a message moves through the delivery chain.

Example:

```text
Received: from mail.example.net
 (mail.example.net [192.0.2.10])
 by mx.organisation.example
 with ESMTPS id ABC123
 for <user@organisation.example>;
 Tue, 25 Nov 2026 04:00:00 +0000
```

Investigate:

- Sending host
- Receiving host
- IP address
- Transport protocol
- Timestamp
- Message identifiers

Read the chain from the receiving side towards the originating side.

The earliest entries may not be trustworthy because an external sender can insert forged headers before the message reaches trusted infrastructure.

## Sender and Reply-To Mismatches

Example:

```text
From: Accounts Department <accounts@example.com>
Reply-To: payment-review@example.net
```

A mismatch may be legitimate, but unexpected reply destinations should be investigated.

## SPF Analysis

SPF evaluates whether the connecting mail server is authorised by the sender domain's SPF policy.

Common results:

- pass
- fail
- softfail
- neutral
- none
- temperror
- permerror

Consider the evaluated domain and authentication context.

## DKIM Analysis

DKIM uses a cryptographic signature associated with a domain.

Relevant header:

```text
DKIM-Signature:
```

Important fields include:

- `d=` signing domain
- `s=` selector
- `h=` signed headers
- `bh=` body hash
- `b=` signature

A valid signature does not prove the sender is trustworthy.

## DMARC Analysis

DMARC evaluates alignment between the visible From domain and SPF or DKIM authentication.

Possible results include:

- pass
- fail
- none
- temperror
- permerror

Review the domain's policy and authentication results rather than relying only on a pass/fail label.

## Header Inspection with Command-Line Tools

Save a message as `.eml`.

Extract selected headers:

```bash
grep -Ei \
'^(From|To|Reply-To|Return-Path|Received|Message-ID|Date|Authentication-Results):' \
message.eml
```

Inspect the full message:

```bash
less message.eml
```

This is basic text extraction, not a complete parser.

## Python Header Extraction

```python
from email import policy
from email.parser import BytesParser

with open("message.eml", "rb") as file:
    message = BytesParser(policy=policy.default).parse(file)

headers = [
    "From",
    "To",
    "Reply-To",
    "Return-Path",
    "Subject",
    "Date",
    "Message-ID",
    "Authentication-Results",
]

for header in headers:
    print(f"{header}: {message.get(header)}")
```

This example reads a local message file and prints selected header values.

## Timestamp Analysis

Consider:
- Time zone offsets
- UTC conversion
- Server clock drift
- Sender-provided Date values
- Mail server receipt timestamps
- Message delivery delays

Do not assume the `Date` header represents the actual delivery time.

## Investigative Checklist

- [ ] Original message preserved.
- [ ] From and Reply-To reviewed.
- [ ] Return-Path reviewed.
- [ ] Received chain examined.
- [ ] Sending infrastructure identified.
- [ ] SPF result reviewed.
- [ ] DKIM result reviewed.
- [ ] DMARC result reviewed.
- [ ] Timestamps normalised.
- [ ] Message ID recorded.
- [ ] Findings correlated with mail gateway logs.

## Common Mistakes

- Trusting every Received header.
- Reading the Received chain in the wrong direction.
- Treating SPF pass as proof of legitimacy.
- Ignoring domain alignment.
- Failing to account for forwarding.
- Assuming every message has an originating IP header.
- Ignoring time zones.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
