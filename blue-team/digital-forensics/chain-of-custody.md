# Chain of Custody

## Overview

Chain of custody is the documented record of evidence possession, handling, transfer and storage.

It establishes who handled evidence, when they handled it, why they accessed it and what happened during that period.

A complete chain of custody helps demonstrate evidence accountability and supports the credibility of investigative findings.

## Objectives

A chain-of-custody process should:

- Identify evidence uniquely.
- Record its origin.
- Document collection.
- Track every transfer.
- Record examination access.
- Document storage locations.
- Record changes in condition.
- Preserve evidence integrity.
- Identify gaps or unexplained periods.

## Evidence Identification

Assign each evidence item a unique identifier.

Example:

```text
CASE-2026-0042-E001
CASE-2026-0042-E002
CASE-2026-0042-E003
```

Avoid using filenames as the only identifier.

Record:
- Evidence ID
- Case ID
- Description
- Source device
- Serial number where relevant
- Collection location
- Collection date and time
- Collector
- Initial condition
- Hash, where applicable

## Evidence Handling

Every interaction should be recorded.

Examples:
- Collection
- Packaging
- Transfer
- Storage
- Access
- Examination
- Copying
- Export
- Return
- Disposal

Record failed or interrupted transfers as well.

## Transfer Records

Each transfer should include:

| Field | Description |
|---|---|
| Evidence ID | Item being transferred |
| Released by | Current custodian |
| Received by | New custodian |
| Date/time | Transfer timestamp and time zone |
| Purpose | Reason for transfer |
| Condition | Condition at transfer |
| Seal number | Tamper-evident seal, if applicable |
| Location | Transfer destination |
| Signatures | Required approvals |

## Digital Evidence Integrity

For digital evidence, record cryptographic hashes.

Example:

```bash
sha256sum evidence.img
```

PowerShell:

```powershell
Get-FileHash .\evidence.img -Algorithm SHA256
```

When copying evidence:
1. Hash the source.
2. Copy the evidence.
3. Hash the destination.
4. Compare the values.
5. Record both results.

A matching hash supports integrity verification but does not replace chain-of-custody documentation.

## Storage Requirements

Evidence storage should provide:

- Access control
- Audit logging
- Encryption
- Backup where appropriate
- Integrity monitoring
- Restricted administrative access
- Documented retention
- Secure disposal procedures

Physical evidence should be stored in controlled facilities with suitable environmental protections.

## Chain-of-Custody Template

Use the following structure for each evidence item.

```text
CASE ID:
EVIDENCE ID:
DESCRIPTION:
SOURCE:
COLLECTION LOCATION:
COLLECTION DATE/TIME:
COLLECTOR:
INITIAL CONDITION:
HASH ALGORITHM:
HASH VALUE:
STORAGE LOCATION:

TRANSFER HISTORY:

1.
Released by:
Received by:
Date/time:
Purpose:
Condition:
Location:
Signatures:

2.
Released by:
Received by:
Date/time:
Purpose:
Condition:
Location:
Signatures:

EXAMINATION HISTORY:

Examiner:
Date/time:
Purpose:
Tools used:
Actions performed:
Changes or limitations:
Related report:

FINAL DISPOSITION:

Retention decision:
Approved by:
Date:
Disposal or return details:
```

## Chain-of-Custody Gaps

If a gap is identified:

1. Document the gap immediately.
2. Identify the last known custodian.
3. Establish the next known point of possession.
4. Investigate available access logs.
5. Verify evidence integrity where possible.
6. Record any uncertainty.
7. Escalate according to policy.

Never backdate records or invent missing transfer details.

## Common Mistakes

- Unlabelled evidence.
- Shared storage without access controls.
- Unrecorded transfers.
- Missing timestamps.
- Inconsistent evidence IDs.
- Hashes not recorded.
- Unexplained access.
- Missing disposal approval.
- Retrospective or incomplete documentation.

## Chain-of-Custody Checklist

- [ ] Unique evidence ID assigned.
- [ ] Source documented.
- [ ] Collector identified.
- [ ] Initial condition recorded.
- [ ] Hash calculated where appropriate.
- [ ] Secure storage established.
- [ ] Every transfer documented.
- [ ] Every examination documented.
- [ ] Access restricted.
- [ ] Final disposition recorded.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
