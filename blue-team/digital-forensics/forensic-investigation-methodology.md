# Forensic Investigation Methodology

## Overview

A structured forensic methodology helps investigators collect reliable evidence, minimise unnecessary changes and produce defensible conclusions.

This guide provides a general workflow for endpoint, server, network and cloud investigations.

## Phase 1: Establish Authority

Before collecting evidence, establish:

- Who authorised the investigation?
- What systems are in scope?
- What data may be collected?
- What is the investigation timeframe?
- Are personal or regulated records involved?
- Are third-party systems involved?
- Are there legal, contractual or privacy restrictions?
- Who can access the resulting evidence?

Record the authorisation and any restrictions.

Do not expand scope without approval.

## Phase 2: Define Objectives

Write down the questions the investigation must answer.

Examples:

- Was an unauthorised account used?
- Was malware executed?
- Was data accessed or exfiltrated?
- Did a user interact with a suspicious attachment?
- Was persistence established?
- Which systems were affected?
- What happened before and after the alert?

Distinguish investigative questions from assumptions.

## Phase 3: Identify Evidence Sources

Create an evidence source inventory.

| Source | Potential evidence |
|---|---|
| Endpoint disk | Files, logs, execution artefacts |
| RAM | Running processes, injected code, network state |
| Windows Event Logs | Logons, process activity, service creation |
| Linux logs | Authentication, sudo, SSH and system activity |
| Firewall | Allowed and denied connections |
| DNS | Domain lookups |
| Proxy | Web requests |
| EDR | Process trees and endpoint telemetry |
| Cloud audit logs | API calls and identity activity |
| Email gateway | Message delivery and attachment information |

Consider whether evidence is likely to expire or be overwritten.

## Phase 4: Assess Volatility

Identify evidence that may disappear.

Examples:
- RAM
- Running processes
- Active network connections
- Temporary files
- Short-retention security logs
- Cloud audit records with limited retention

Prioritise collection based on the investigation and operational circumstances.

For an active compromise, coordinate collection with incident response. Containment may be more important than preserving every volatile artefact.

## Phase 5: Acquire Evidence

Select a method appropriate to the evidence source.

Examples:

- Forensic disk imaging
- Memory acquisition
- Log export
- API-based cloud collection
- Packet capture export
- Email message export
- File-level collection

Record:
- Source identifier
- Collection operator
- Date and time
- Time zone
- Acquisition tool and version
- Collection parameters
- Destination
- Hashes
- Errors or limitations

## Phase 6: Verify Integrity

Calculate cryptographic hashes for acquired evidence.

Example:

```bash
sha256sum disk-image.E01
```

PowerShell:

```powershell
Get-FileHash .\disk-image.E01 -Algorithm SHA256
```

Compare hashes when validating copied evidence.

Maintain the original acquisition and create working copies where appropriate.

## Phase 7: Examination

Examine evidence using appropriate tools and documented procedures.

Possible activities:
- File-system analysis
- Event log analysis
- Registry examination
- Memory analysis
- Browser artefact analysis
- Email header examination
- Network traffic analysis
- Timeline construction
- Malware analysis

Record the artefacts that support each finding.

## Phase 8: Correlation

Correlate evidence from multiple sources.

Example:

| Time (UTC) | Source | Event |
|---|---|---|
| 02:10 | Email gateway | Suspicious message delivered |
| 02:13 | Endpoint | Attachment written to disk |
| 02:14 | Endpoint | Script interpreter launched |
| 02:15 | EDR | Suspicious child process detected |
| 02:16 | Firewall | Outbound connection observed |

The example is illustrative. Real investigations must use actual collected timestamps and account for clock differences.

## Phase 9: Develop Findings

For each finding, document:

- Observation
- Supporting evidence
- Relevant timestamps
- Interpretation
- Confidence
- Alternative explanations
- Limitations

Use confidence levels consistently.

Example:

- **High:** Multiple independent sources support the conclusion.
- **Moderate:** Evidence supports the conclusion but important gaps remain.
- **Low:** Limited or ambiguous evidence exists.

Confidence is not a substitute for explaining the evidence.

## Phase 10: Reporting

A forensic report should include:

1. Executive summary
2. Investigation authority
3. Scope and objectives
4. Evidence sources
5. Acquisition methodology
6. Tools and versions
7. Examination methodology
8. Findings
9. Timeline
10. Limitations
11. Conclusions
12. Evidence references
13. Appendices

Clearly separate facts, interpretations and conclusions.

## Phase 11: Evidence Retention

Follow the organisation's evidence retention policy.

Consider:
- Retention periods
- Access controls
- Encryption
- Secure storage
- Legal holds
- Disposal approval
- Chain-of-custody updates

Do not destroy evidence simply because an investigation has been closed.

## Investigation Quality Checklist

- [ ] Authority confirmed.
- [ ] Scope documented.
- [ ] Objectives defined.
- [ ] Evidence sources identified.
- [ ] Volatility assessed.
- [ ] Collection method documented.
- [ ] Evidence hashes recorded.
- [ ] Chain of custody maintained.
- [ ] Tool versions recorded.
- [ ] Findings linked to evidence.
- [ ] Alternative explanations considered.
- [ ] Limitations documented.
- [ ] Report reviewed before distribution.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
