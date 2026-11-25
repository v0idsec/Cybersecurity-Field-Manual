# Configuration Baselines and Compliance

## Overview

A configuration baseline defines the approved security configuration for a system, application or service.

Baselines provide a consistent way to assess systems, identify deviations and demonstrate that security requirements are being maintained.

They should be tailored to the organisation's technology, risk profile and operational requirements.

## 1. What is a security baseline?

A security baseline is a documented set of configuration requirements.

Examples include:

- Operating system security settings.
- Account and authentication requirements.
- Firewall policies.
- Logging configuration.
- Encryption requirements.
- Application control policies.
- Cloud resource settings.
- Network device configuration.
- Browser security settings.

A baseline should specify both the expected state and how compliance will be measured.

## 2. Common baseline frameworks

### CIS Benchmarks

The Center for Internet Security publishes platform-specific security configuration recommendations.

Common coverage includes:

- Windows.
- Linux distributions.
- Cloud platforms.
- Databases.
- Network devices.
- Browsers.
- Containers.

CIS Benchmark profiles often distinguish between different levels of hardening. Select a profile that matches the system's purpose and operational constraints.

Reference: [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)

### Microsoft Security Baselines

Microsoft publishes security baseline recommendations for supported Microsoft products.

These can help organisations standardise:

- Windows workstation security.
- Windows Server configuration.
- Microsoft Edge.
- Microsoft 365 applications.
- Microsoft Defender.
- Microsoft Intune-managed devices.

Reference: [Microsoft Security Baselines](https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines)

### Australian Information Security Manual

The Australian Signals Directorate's Information Security Manual (ISM) provides guidance for protecting information and systems.

It covers areas such as:

- Governance and risk management.
- Personnel security.
- Physical security.
- ICT security.
- System administration.
- Access control.
- Incident management.

Reference: [Australian ISM](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism)

### Essential Eight

The Essential Eight is a prioritised set of mitigation strategies published by the Australian Signals Directorate.

Its strategies address:

1. Application control.
2. Patch applications.
3. Configure Microsoft Office macros.
4. User application hardening.
5. Restrict administrative privileges.
6. Patch operating systems.
7. Multi-factor authentication.
8. Regular backups.

Maturity levels describe progressively stronger implementation. Organisations should assess the official guidance and requirements rather than treating a maturity level as a simple checklist.

Reference: [Essential Eight](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight)

### NIST

Useful NIST publications include:

- SP 800-53 — Security and Privacy Controls.
- SP 800-70 — Security Configuration Checklists.
- SP 800-123 — Guide to General Server Security.
- SP 800-128 — Security-Focused Configuration Management.

References:
- [NIST Computer Security Resource Center](https://csrc.nist.gov/)
- [NIST SP 800-128](https://csrc.nist.gov/pubs/sp/800/128/upd1/final)

## 3. Selecting an appropriate baseline

Consider:

- Operating system and version.
- Server or workstation role.
- Business application dependencies.
- Regulatory requirements.
- Threat exposure.
- Existing security controls.
- Management tooling.
- Availability requirements.

A database server, developer workstation and public-facing web server should not necessarily share the same baseline.

## 4. Baseline implementation process

1. Identify the system and its owner.
2. Select an appropriate benchmark or framework.
3. Review each recommendation.
4. Identify operational dependencies.
5. Document approved settings.
6. Record exceptions and compensating controls.
7. Test the baseline in a representative environment.
8. Obtain change approval.
9. Deploy in controlled stages.
10. Validate and monitor compliance.

## 5. Compliance measurement

A useful baseline assessment records:

| Field | Description |
|---|---|
| Control ID | Unique identifier |
| Requirement | Expected configuration |
| Actual state | Observed configuration |
| Result | Pass, fail, not applicable or not assessed |
| Evidence | Command output, policy export or assessment record |
| Risk | Impact of the deviation |
| Owner | Responsible team |
| Remediation | Required action |
| Exception | Approved deviation, if applicable |

Avoid reporting a system as compliant when significant controls have not been assessed.

## 6. Exceptions and compensating controls

Not every benchmark recommendation can be applied universally.

Examples:

- Legacy applications require an older protocol.
- A vendor-supported service requires a specific permission.
- A business process relies on removable media.
- A production system cannot be restarted during the proposed maintenance window.

An exception should include:

- The control that cannot be met.
- A clear business justification.
- The associated risk.
- Compensating controls.
- An accountable owner.
- Approval.
- An expiry or review date.

Exceptions should not become permanent undocumented configuration.

## 7. Configuration drift

Configuration drift occurs when a system moves away from its approved baseline.

Possible causes:

- Manual administrator changes.
- Software installation.
- Application updates.
- Group Policy changes.
- Infrastructure automation changes.
- Cloud resource modifications.
- Emergency troubleshooting.

Detect drift through:

- Periodic configuration assessments.
- Centralised endpoint management.
- Infrastructure-as-code review.
- Cloud configuration monitoring.
- Change auditing.
- File integrity monitoring.

## 8. Compliance versus security

Compliance demonstrates alignment with a defined set of requirements.

It does not guarantee that a system is secure.

A compliant system may still contain:

- Unknown vulnerabilities.
- Misconfigured application logic.
- Weak business processes.
- Compromised credentials.
- Unmonitored attack paths.
- Newly discovered security weaknesses.

Use compliance as one part of a broader security programme.

## 9. Baseline review checklist

- [ ] System owner identified.
- [ ] Correct platform benchmark selected.
- [ ] Benchmark version recorded.
- [ ] Business dependencies reviewed.
- [ ] Baseline requirements documented.
- [ ] Test environment used.
- [ ] Change approval obtained.
- [ ] Compliance evidence retained.
- [ ] Exceptions approved.
- [ ] Compensating controls documented.
- [ ] Configuration drift monitored.
- [ ] Baseline reviewed periodically.

## References

- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)
- [Microsoft Security Baselines](https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines)
- [Australian ISM](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism)
- [Essential Eight](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight)
- [NIST SP 800-70](https://csrc.nist.gov/pubs/sp/800/70/r5/final)
- [NIST SP 800-128](https://csrc.nist.gov/pubs/sp/800/128/upd1/final)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
