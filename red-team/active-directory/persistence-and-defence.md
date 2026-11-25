
# Active Directory Persistence and Defence

> Professional reference guide for assessing Active Directory persistence risks, identifying indicators of domain compromise and validating defensive controls.

## Contents

- [Overview](#overview)
- [Persistence Fundamentals](#persistence-fundamentals)
- [Identity-Based Persistence](#identity-based-persistence)
- [Kerberos Persistence](#kerberos-persistence)
- [Directory and Permission Persistence](#directory-and-permission-persistence)
- [Group Policy Persistence](#group-policy-persistence)
- [Certificate-Based Persistence](#certificate-based-persistence)
- [Endpoint and Service Persistence](#endpoint-and-service-persistence)
- [Detection Engineering](#detection-engineering)
- [Incident Response Considerations](#incident-response-considerations)
- [Assessment Methodology](#assessment-methodology)
- [Hardening](#hardening)
- [Tools and References](#tools-and-references)
- [Assessment Checklist](#assessment-checklist)

---

## Overview

Active Directory persistence refers to mechanisms that allow an attacker to retain or regain access to an environment after initial compromise.

Persistence can be established through:

- Additional accounts.
- Privileged group membership.
- Directory permissions.
- Kerberos-related credential material.
- Group Policy.
- Certificate services.
- Service configuration.
- Scheduled tasks.
- Administrative access.
- Identity federation or synchronisation systems.

A domain assessment should consider both the initial compromise path and the mechanisms that could allow continued access.

Persistence testing is high risk. Creating accounts, changing privileged permissions, modifying Group Policy or manipulating authentication infrastructure should only occur when explicitly authorised.

This guide focuses on identifying, validating and defending against persistence risks.

## Persistence Fundamentals

Persistence can exist at several layers:

| Layer | Examples |
|---|---|
| Identity | Unexpected accounts or group memberships |
| Directory | Modified ACLs or ownership |
| Authentication | Kerberos credential abuse |
| Policy | Malicious or unauthorised GPO changes |
| PKI | Unauthorised certificate issuance |
| Endpoint | Services, scheduled tasks and startup mechanisms |
| Infrastructure | Backup, management or identity synchronisation systems |

A robust assessment examines each layer rather than focusing only on user accounts.

## Identity-Based Persistence

Review:

- Unexpected user accounts.
- Recently created accounts.
- Privileged group membership changes.
- Accounts with unusual attributes.
- Accounts exempt from password requirements.
- Accounts with non-expiring passwords.
- Dormant accounts re-enabled unexpectedly.
- Service accounts with unexplained privileges.

### PowerShell Review

```powershell
# Recently created users
Get-ADUser -Filter * -Properties whenCreated |
    Sort-Object whenCreated -Descending |
    Select-Object -First 50 SamAccountName,whenCreated

# Accounts with non-expiring passwords
Get-ADUser -Filter * -Properties PasswordNeverExpires |
    Where-Object {$_.PasswordNeverExpires}

# Privileged group membership
Get-ADGroupMember -Identity "Domain Admins" -Recursive

# Recently modified users
Get-ADUser -Filter * -Properties whenChanged |
    Sort-Object whenChanged -Descending |
    Select-Object -First 50 SamAccountName,whenChanged
```

Timestamps are useful indicators but should be correlated with change records and audit logs.

## Kerberos Persistence

Kerberos-related persistence can involve compromised credential material or forged authentication tickets.

Examples include:

- Golden Tickets.
- Silver Tickets.
- Long-lived ticket abuse.
- Compromised service account secrets.
- Delegation abuse.
- Persistent access through privileged service identities.

### KRBTGT Security

The KRBTGT account is central to Kerberos ticket validation within a domain.

Compromise of its secret material can enable severe domain-wide authentication abuse.

Following confirmed KRBTGT compromise, recovery must follow Microsoft's documented procedure, including the required password rotation sequence and replication considerations.

Do not perform KRBTGT rotation as a routine proof-of-concept exercise.

### Detection Considerations

Review:

- Unusual Kerberos ticket activity.
- Unexpected encryption types.
- Abnormal ticket lifetimes.
- Unusual service ticket requests.
- Privileged authentication from unexpected systems.
- Authentication patterns inconsistent with normal account behaviour.

## Directory and Permission Persistence

Review directory objects for unauthorised changes.

Potential mechanisms include:

- Unexpected privileged group membership.
- Modified DACLs.
- Unexpected object ownership.
- Replication permissions granted to unusual principals.
- Delegation changes.
- Modified user account control flags.
- New or modified service accounts.

Focus on changes to high-value objects.

## Group Policy Persistence

Group Policy can influence large numbers of systems.

Review:

- Newly created GPOs.
- Recently modified GPOs.
- GPO ownership.
- GPO modification permissions.
- New GPO links.
- Changes to security filtering.
- Changes to startup and logon scripts.
- Changes to scheduled task deployment.
- Unexpected software deployment settings.

Correlate GPO changes with SYSVOL contents and change-management records.

## Certificate-Based Persistence

Certificates can remain valid beyond the lifetime of the original account or session.

Review:

- Unexpectedly issued certificates.
- Certificate template changes.
- CA configuration changes.
- Enrollment permissions.
- Privileged certificate issuance.
- Certificate validity periods.
- Certificate revocation status.
- Compromised CA private keys.

After confirmed certificate abuse, identify affected certificates and determine whether revocation and reissuance are necessary.

## Endpoint and Service Persistence

Domain compromise may be maintained through endpoint or server mechanisms.

Review authorised systems for:

- Unexpected services.
- Scheduled tasks.
- Startup scripts.
- Logon scripts.
- WMI permanent event subscriptions.
- Unusual local administrator accounts.
- Unexpected remote management configuration.
- Modified application services.
- Suspicious PowerShell execution.

Correlate endpoint findings with domain identity activity.

## Detection Engineering

Build detection around changes to critical identity infrastructure.

### Relevant Windows Events

| Event ID | Description |
|---|---|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4672 | Special privileges assigned to new logon |
| 4720 | User account created |
| 4722 | User account enabled |
| 4724 | Password reset attempted |
| 4728 | Member added to global security group |
| 4732 | Member added to local security group |
| 4756 | Member added to universal security group |
| 4738 | User account changed |
| 4740 | Account locked out |
| 4742 | Computer account changed |
| 4768 | Kerberos TGT requested |
| 4769 | Kerberos service ticket requested |
| 4771 | Kerberos pre-authentication failed |
| 5136 | Directory object modified |
| 5137 | Directory object created |
| 5139 | Directory object moved |
| 5141 | Directory object deleted |

Some events require specific audit policy settings. Validate event availability in the assessed environment.

### High-Value Monitoring Areas

Prioritise:

- Domain Admins and Enterprise Admins membership.
- Changes to privileged account attributes.
- Domain controller security configuration.
- GPO modifications.
- Replication permissions.
- Delegation changes.
- Certificate template changes.
- CA configuration changes.
- Unexpected privileged logons.
- Authentication from unusual endpoints.

### Baseline and Anomaly Detection

A useful detection programme should establish normal behaviour.

Consider:

- Typical privileged logon locations.
- Expected service account activity.
- Normal Kerberos request patterns.
- Approved GPO changes.
- Expected certificate issuance.
- Standard administrative workstations.
- Normal account creation processes.

Alert on deviations with sufficient context to reduce false positives.

## Incident Response Considerations

If domain compromise is suspected:

1. Establish incident scope and severity.
2. Preserve relevant domain controller and endpoint evidence.
3. Identify affected privileged identities.
4. Investigate account and group changes.
5. Review directory ACL modifications.
6. Examine Kerberos and authentication activity.
7. Investigate GPO and SYSVOL changes.
8. Review certificate issuance and CA integrity.
9. Identify compromised systems and credentials.
10. Coordinate containment with identity and infrastructure teams.
11. Revoke or rotate affected credentials and certificates.
12. Follow Microsoft's recovery guidance for compromised domain controllers or KRBTGT secrets.
13. Validate that persistence mechanisms have been removed.
14. Monitor for recurrence.

Avoid ad hoc domain-wide remediation. Incorrect recovery actions can cause authentication outages or compromise the integrity of the recovery process.

## Assessment Methodology

### 1. Establish a Baseline

Record known privileged accounts, groups, GPOs, CAs and service accounts.

### 2. Review Recent Changes

Examine account creation, group membership, ACL changes and configuration modifications.

### 3. Review Authentication Activity

Assess Kerberos, NTLM and privileged logon patterns.

### 4. Review Policy and Infrastructure

Inspect GPOs, SYSVOL, domain controllers, certificate authorities and management systems.

### 5. Investigate Anomalies

Correlate unusual changes with:

- Change-management records.
- Administrative activity.
- Endpoint telemetry.
- Authentication logs.
- Known assessment activity.

### 6. Validate Defensive Controls

Determine whether the organisation can detect and investigate the relevant changes.

### 7. Report Gaps

Document missing audit coverage, excessive privileges, unmonitored infrastructure and weak recovery procedures.

## Hardening

- Enforce least privilege.
- Implement tiered administration.
- Protect privileged identities.
- Use MFA.
- Deploy Windows LAPS.
- Use gMSAs where appropriate.
- Restrict delegation.
- Review privileged ACLs.
- Monitor GPO changes.
- Secure certificate authorities.
- Restrict domain controller access.
- Reduce legacy authentication.
- Enable appropriate auditing.
- Protect backup infrastructure.
- Maintain tested recovery procedures.
- Review identity changes regularly.

## Tools and References

### Tools

- BloodHound.
- Microsoft Defender for Identity.
- Microsoft Defender for Endpoint.
- Windows Event Viewer.
- PowerShell.
- PingCastle.
- Purple Knight.
- Sysmon.
- Microsoft Sentinel.
- Splunk.
- Certipy.
- Group Policy Management tools.

### References

- [Microsoft — Securing Active Directory](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/)
- [Microsoft — Defender for Identity](https://learn.microsoft.com/en-us/defender-for-identity/)
- [MITRE ATT&CK — Persistence](https://attack.mitre.org/tactics/TA0003/)
- [MITRE ATT&CK — Account Manipulation](https://attack.mitre.org/techniques/T1098/)
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)
- [SpecterOps](https://specterops.io/)

## Assessment Checklist

- [ ] Privileged accounts baselined.
- [ ] Unexpected accounts investigated.
- [ ] Privileged group changes reviewed.
- [ ] Directory ACL changes reviewed.
- [ ] Replication permissions reviewed.
- [ ] Kerberos activity assessed.
- [ ] KRBTGT security and recovery procedures reviewed.
- [ ] GPO changes investigated.
- [ ] SYSVOL integrity assessed.
- [ ] Certificate issuance reviewed.
- [ ] CA and template changes reviewed.
- [ ] Endpoint persistence indicators assessed.
- [ ] Privileged authentication monitoring reviewed.
- [ ] Incident response procedures assessed.
- [ ] Recovery and retesting requirements documented.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
