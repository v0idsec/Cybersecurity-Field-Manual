# Suspicious Email Analysis

## 1. Case Details

| Field | Value |
|---|---|
| Case ID | `[CASE-ID]` |
| Analyst | `[ANALYST]` |
| Analysis date | `[DATE/TIME/TIMEZONE]` |
| Source | `[REPORT / ALERT / OTHER]` |
| Related incident | `[INCIDENT ID]` |

## 2. Message Metadata

| Field | Value |
|---|---|
| From | `[ADDRESS]` |
| To | `[ADDRESS]` |
| Reply-To | `[ADDRESS]` |
| Return-Path | `[ADDRESS]` |
| Subject | `[SUBJECT]` |
| Date | `[DATE]` |
| Message ID | `[MESSAGE-ID]` |
| Received time | `[TIME]` |

## 3. Header Analysis

**Received chain:**

`[SUMMARY]`

**SPF:**

`[RESULT AND DOMAIN]`

**DKIM:**

`[RESULT AND DOMAIN]`

**DMARC:**

`[RESULT AND DOMAIN]`

**Additional observations:**

`[OBSERVATIONS]`

## 4. Content Analysis

**Message summary:**

`[SUMMARY]`

**Social engineering indicators:**

`[INDICATORS]`

**Brand or identity impersonation:**

`[DETAILS]`

## 5. URL Analysis

| URL (defanged) | Destination | Reputation | Notes |
|---|---|---|---|
| `[URL]` | `[DESTINATION]` | `[RESULT]` | `[NOTES]` |

## 6. Attachment Analysis

| Filename | File type | SHA-256 | Result |
|---|---|---|---|
| `[FILENAME]` | `[TYPE]` | `[HASH]` | `[RESULT]` |

## 7. User Exposure

- Message opened:
- Link clicked:
- Credentials submitted:
- Attachment downloaded:
- Attachment executed:
- Information disclosed:
- Payment action:

## 8. Related Evidence

| Evidence ID | Description | Location |
|---|---|---|
| `[ID]` | `[DESCRIPTION]` | `[LOCATION]` |

## 9. Assessment

**Classification:**

`[BENIGN / SPAM / SUSPICIOUS / PHISHING / MALICIOUS / BEC]`

**Confidence:**

`[LOW / MODERATE / HIGH]`

**Rationale:**

`[EVIDENCE-BASED EXPLANATION]`

## 10. Recommended Actions

`[ACTIONS]`

## 11. Analyst Conclusion

`[FINAL SUMMARY AND LIMITATIONS]`

**Analyst:**

`[NAME]`

**Date:**

`[DATE]`

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
