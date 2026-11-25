# Hardening Validation and Monitoring

## Overview

Hardening is only effective when security controls are correctly implemented, operating as intended and maintained over time.

Validation confirms whether approved configurations are present. Monitoring identifies changes, failures and suspicious activity that may undermine those configurations.

## 1. Validation objectives

A hardening assessment should establish:

- Whether required controls are enabled.
- Whether configurations match the approved baseline.
- Whether unnecessary exposure remains.
- Whether security controls function correctly.
- Whether exceptions are documented and approved.
- Whether monitoring can detect relevant changes.
- Whether remediation has been completed.

## 2. Validation methods

### Configuration review

Inspect system settings and compare them against approved requirements.

Examples:

- Windows Group Policy.
- Local Security Policy.
- Linux configuration files.
- Firewall rules.
- Cloud IAM policies.
- Application configuration.
- Endpoint security policies.

### Automated compliance assessment

Use approved tools to compare system configuration against a benchmark.

Examples:

- CIS-CAT.
- Microsoft Security Compliance Toolkit.
- OpenSCAP.
- Cloud security posture management platforms.

Automated results should be reviewed. A scanner may not understand application dependencies, approved exceptions or compensating controls.

### Exposure assessment

Review externally and internally reachable services.

Consider:

- Listening ports.
- Public IP addresses.
- Exposed management interfaces.
- Unnecessary services.
- Remote access pathways.
- Cloud storage exposure.
- Firewall rules.

Only conduct active scanning within the approved assessment scope.

### Functional testing

Confirm that controls work without disrupting legitimate operations.

Examples:

- Confirm MFA challenges are enforced.
- Verify endpoint protection reports healthy status.
- Confirm firewall restrictions block unauthorised access.
- Test application control using approved test applications.
- Confirm audit events reach the SIEM.
- Validate backup restoration.

## 3. Windows validation examples

```powershell
# Defender health
Get-MpComputerStatus

# Firewall profiles
Get-NetFirewallProfile

# BitLocker status
Get-BitLockerVolume

# Local administrator membership
Get-LocalGroupMember -Group "Administrators"

# Review running services
Get-Service | Where-Object Status -eq "Running"

# Review listening TCP connections
Get-NetTCPConnection -State Listen
```

Interpret results against the organisation's approved baseline.

## 4. Linux validation examples

```bash
# Operating system details
cat /etc/os-release

# Kernel version
uname -r

# Listening sockets
sudo ss -tulpn

# Running services
systemctl --type=service --state=running

# Firewall status (where UFW is used)
sudo ufw status verbose

# SELinux status
getenforce

# AppArmor status
sudo aa-status

# Failed services
systemctl --failed
```

Not every distribution uses the same firewall, MAC or logging implementation.

## 5. Cloud validation

Review cloud configuration for:

- Publicly exposed resources.
- Overly permissive IAM roles.
- Unused credentials.
- Unencrypted storage.
- Missing audit logging.
- Unrestricted security groups.
- Insecure network paths.
- Unapproved regions or services.
- Disabled security monitoring.
- Unprotected backup resources.

Use the cloud provider's native security posture tools and approved configuration assessment platforms.

## 6. Monitoring for configuration changes

Monitor changes to:

| Area | Events or changes to monitor |
|---|---|
| Accounts | New accounts, disabled accounts, privilege changes |
| Authentication | MFA changes, authentication policy changes |
| Endpoint | Defender changes, ASR exclusions, application control changes |
| Network | Firewall changes, new listeners, routing changes |
| Linux | SSH changes, sudoers modifications, service changes |
| Cloud | IAM changes, public access changes, audit logging changes |
| Storage | Encryption changes, access policy changes, retention changes |
| Logging | Disabled agents, modified retention, collection failures |

Prioritise changes that weaken a security control or expand access.

## 7. Configuration drift detection

Configuration drift should be detected and investigated.

A useful process:

1. Establish the approved baseline.
2. Collect the current configuration.
3. Compare current and expected states.
4. Identify differences.
5. Determine whether the change was authorised.
6. Assess the risk.
7. Remediate or approve an exception.
8. Record evidence and update the baseline if required.

Do not automatically revert every deviation. Some changes may be legitimate and necessary.

## 8. Monitoring health

A security control that silently stops working can create a false sense of protection.

Monitor:

- Endpoint agent health.
- Antivirus signature updates.
- SIEM ingestion failures.
- Log source availability.
- Firewall management status.
- Backup completion.
- Configuration assessment coverage.
- Policy deployment failures.
- Cloud audit log availability.

Define alerting thresholds and escalation procedures for important control failures.

## 9. Hardening assessment report

A useful assessment report should include:

### Assessment details

- Assessment name.
- Date and time.
- Assessor.
- Systems assessed.
- Approved scope.
- Baseline or framework used.

### Findings

For each finding, record:

- Finding ID.
- Affected system.
- Control requirement.
- Observed configuration.
- Expected configuration.
- Risk and business impact.
- Supporting evidence.
- Recommended remediation.
- Responsible owner.

### Summary

Include:

- Overall assessment outcome.
- Significant security gaps.
- Accepted exceptions.
- Remediation priorities.
- Outstanding risks.
- Recommended review date.

## 10. Validation checklist

- [ ] Assessment scope approved.
- [ ] Baseline version recorded.
- [ ] Required controls assessed.
- [ ] Automated results reviewed.
- [ ] Exceptions verified.
- [ ] Security controls functionally tested.
- [ ] Monitoring and log ingestion confirmed.
- [ ] Configuration drift detection considered.
- [ ] Findings assigned to owners.
- [ ] Remediation retested.
- [ ] Evidence retained.
- [ ] Assessment report completed.

## References

- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)
- [OpenSCAP](https://www.open-scap.org/)
- [Microsoft Security Compliance Toolkit](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
- [Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/defender-endpoint/)
- [AWS Security Hub](https://docs.aws.amazon.com/securityhub/)
- [Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
