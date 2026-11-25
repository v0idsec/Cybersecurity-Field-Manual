# Detection Maintenance and Lifecycle

## Overview

Detection rules require ongoing maintenance to remain accurate, relevant and operational.

Changes to infrastructure, applications, telemetry and attacker behaviour can reduce detection effectiveness over time.

A detection should have a defined lifecycle from initial development through retirement.

## Detection Lifecycle

Typical stages:

1. Proposed
2. Designed
3. Developed
4. Tested
5. Approved
6. Deployed
7. Monitored
8. Tuned
9. Retired

Each stage should have defined entry and exit criteria.

## Ownership

Every production detection should have an owner.

Responsibilities include:

- Maintaining detection logic
- Reviewing false positives
- Monitoring operational health
- Reviewing threat relevance
- Maintaining documentation
- Coordinating testing
- Managing changes
- Approving retirement

## Scheduled Reviews

Review detections periodically and after significant environmental changes.

Review:

- Detection objective
- Data source availability
- Query correctness
- Field mappings
- Severity
- ATT&CK mapping
- False-positive exclusions
- Investigation guidance
- Test results
- Performance

## Change-Driven Reviews

A detection may need immediate review when:

- A log source is removed.
- A SIEM connector changes.
- An operating system is upgraded.
- An application is replaced.
- A service account changes.
- A detection backend is migrated.
- A security incident reveals a gap.
- New threat intelligence changes the threat model.

## Detection Health Monitoring

Monitor for:

- Query failures
- Rule execution failures
- Missing telemetry
- Sudden alert volume changes
- Parsing failures
- Expired exceptions
- Broken data dependencies
- Unexpected performance degradation

A detection that silently stops executing can create a serious coverage gap.

## Version Management

Maintain:

- Unique detection identifiers
- Version history
- Change descriptions
- Approval records
- Test evidence
- Deployment history
- Rollback information

Use version control where possible.

## Documentation Maintenance

Keep the following information current:

- Detection purpose
- Required data sources
- Query logic
- Expected behaviour
- Known limitations
- False-positive considerations
- Investigation steps
- Response guidance
- Ownership
- Review date

## Detection Retirement

A detection may be retired when:

- The relevant system is decommissioned.
- The data source is no longer available.
- The threat is no longer relevant.
- A replacement detection provides equivalent or better coverage.
- The rule is technically obsolete.
- The detection cannot be maintained safely.

Before retirement:

1. Identify dependent workflows.
2. Assess coverage impact.
3. Confirm replacement coverage where required.
4. Obtain approval.
5. Archive the detection.
6. Update documentation.
7. Record the retirement reason.

Do not silently delete production detections.

## Lifecycle Status

Suggested status values:

| Status | Meaning |
|---|---|
| Proposed | Requirement identified |
| Development | Logic being written |
| Testing | Under validation |
| Production | Actively deployed |
| Tuning | Under adjustment |
| Review Required | Needs reassessment |
| Deprecated | Scheduled for retirement |
| Retired | No longer active |

## Continuous Improvement

Use feedback from:

- Security incidents
- Threat hunting
- Purple-team exercises
- Analyst investigations
- Threat intelligence
- Detection testing
- Telemetry reviews

Every incident should be considered an opportunity to assess whether existing detections worked as intended.

## Further Reading

- Sigma: https://sigmahq.io/
- MITRE ATT&CK: https://attack.mitre.org/
- Elastic Detection Rules: https://github.com/elastic/detection-rules
- NIST SP 800-61: https://csrc.nist.gov/pubs/sp/800/61/r2/final

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
