# Phishing Triage Template

## Case Information

| Field | Value |
|---|---|
| Case ID | `[CASE-ID]` |
| Analyst | `[ANALYST]` |
| Date/time | `[DATE/TIME/TIMEZONE]` |
| Source | `[USER REPORT / ALERT / OTHER]` |
| Priority | `[P1 / P2 / P3 / P4]` |
| Status | `[OPEN / IN PROGRESS / ESCALATED / CLOSED]` |

## Message Information

- Sender:
- Recipient:
- Subject:
- Message ID:
- Received time:
- Reply-To:
- Attachments:
- URLs:

## Initial Indicators

- [ ] Sender/domain anomaly
- [ ] Display-name impersonation
- [ ] Reply-To mismatch
- [ ] Suspicious URL
- [ ] Suspicious attachment
- [ ] SPF failure
- [ ] DKIM failure
- [ ] DMARC failure
- [ ] Unexpected urgency
- [ ] Payment or credential request
- [ ] Unexpected external sharing
- [ ] Other

## User Exposure

| Question | Result |
|---|---|
| Email opened? | `[YES / NO / UNKNOWN]` |
| Link clicked? | `[YES / NO / UNKNOWN]` |
| Credentials submitted? | `[YES / NO / UNKNOWN]` |
| MFA approved? | `[YES / NO / UNKNOWN]` |
| Attachment opened? | `[YES / NO / UNKNOWN]` |
| File executed? | `[YES / NO / UNKNOWN]` |
| Information disclosed? | `[YES / NO / UNKNOWN]` |
| Payment action? | `[YES / NO / UNKNOWN]` |

## Scope Assessment

- Number of recipients:
- Other affected users:
- Related messages:
- Related endpoints:
- Related accounts:
- Related alerts:

## Initial Severity

**Severity:** `[LOW / MEDIUM / HIGH / CRITICAL]`

**Rationale:**

`[EXPLAIN THE POTENTIAL IMPACT]`

## Immediate Actions

- [ ] Preserve message
- [ ] Search mail environment
- [ ] Quarantine confirmed malicious messages
- [ ] Review endpoint telemetry
- [ ] Review identity activity
- [ ] Contact affected user
- [ ] Escalate to incident response
- [ ] Notify finance or management if relevant

## Escalation Decision

**Escalate:** `[YES / NO]`

**Reason:**

`[RATIONALE]`

## Triage Outcome

**Classification:** `[BENIGN / SPAM / SUSPICIOUS / PHISHING / MALICIOUS / BEC]`

**Next action:**

`[NEXT ACTION]`

**Analyst:** `[NAME]`

**Date/time:** `[DATE/TIME/TIMEZONE]`

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
