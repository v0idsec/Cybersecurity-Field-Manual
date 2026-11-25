
# Active Directory Domain Privilege Escalation

> Professional reference guide for identifying and validating privilege escalation paths within Active Directory environments.

## Contents

- [Overview](#overview)
- [Privilege Boundaries](#privilege-boundaries)
- [Common Escalation Paths](#common-escalation-paths)
- [Credential and Identity Exposure](#credential-and-identity-exposure)
- [Group and ACL Abuse](#group-and-acl-abuse)
- [Group Policy Abuse](#group-policy-abuse)
- [Kerberos-Related Escalation](#kerberos-related-escalation)
- [Certificate-Based Escalation](#certificate-based-escalation)
- [Domain Controller Exposure](#domain-controller-exposure)
- [Assessment Methodology](#assessment-methodology)
- [Impact Validation](#impact-validation)
- [Detection and Defence](#detection-and-defence)
- [Tools and References](#tools-and-references)
- [Assessment Checklist](#assessment-checklist)

---

## Overview

Active Directory privilege escalation occurs when an identity obtains access beyond its intended permissions.

Escalation may be direct or achieved through a chain of relationships involving:

- Group membership.
- Object permissions.
- Service accounts.
- Credential exposure.
- Kerberos delegation.
- Group Policy.
- Certificate services.
- Administrative sessions.
- Trust relationships.
- Domain controller configuration.

A domain compromise does not necessarily result from one critical vulnerability. It may result from several individually overlooked weaknesses.

## Privilege Boundaries

Understand the difference between:

| Privilege level | Example |
|---|---|
| Standard user | Ordinary domain account |
| Local administrator | Administrative access to one endpoint |
| Server administrator | Administrative access to a server |
| Delegated administrator | Control over specific directory objects |
| Domain Admin | Broad control over a domain |
| Enterprise Admin | Forest-level administrative privileges |
| Domain controller control | Access to critical identity infrastructure |

These categories are simplified. Effective access depends on the environment and the specific permissions granted.

### Tiered Administration

Many environments separate administrative resources into tiers.

A common model is:

- Tier 0: Identity infrastructure and domain controllers.
- Tier 1: Servers and enterprise applications.
- Tier 2: User workstations and endpoints.

Assess whether credentials and administrative sessions cross these boundaries unnecessarily.

## Common Escalation Paths

### Group Membership

Review whether a low-privileged identity can:

- Add itself to a privileged group.
- Modify a group containing privileged identities.
- Control a nested group.
- Change a privileged group's ownership.
- Modify a group ACL.

### Object Permissions

Investigate:

- GenericAll.
- GenericWrite.
- WriteDACL.
- WriteOwner.
- WriteProperty.
- ForceChangePassword.
- AddMember.
- Replication-related extended rights.

See [ACL Abuse](acl-abuse.md).

### Service Accounts

Review:

- SPN-associated accounts.
- Weak or old credentials.
- Excessive privileges.
- Interactive logon permissions.
- Shared passwords.
- Service account ownership.
- Unnecessary local administrator access.

See [Kerberos](kerberos.md) and [Password Attacks](password-attacks.md).

### Local Administrator Relationships

Local administrative access may provide access to:

- Local configuration.
- Application secrets.
- Scheduled task configuration.
- Service configuration.
- Local security settings.
- Other users' sessions, depending on protections and privileges.

Assess whether local administrator access creates a route to more privileged identities.

### Group Policy

An account that can modify a GPO affecting privileged systems may have significant influence over those systems.

Review:

- GPO modification permissions.
- GPO links.
- OU hierarchy.
- Security filtering.
- WMI filtering.
- GPO ownership.
- SYSVOL access and integrity.

### Delegation

Review unconstrained, constrained and resource-based constrained delegation.

See [Delegation](delegation.md).

### Active Directory Certificate Services

Misconfigured certificate templates and enrollment permissions may allow an identity to obtain certificates that grant unintended authentication privileges.

See [AD CS](adcs.md).

## Credential and Identity Exposure

Investigate credential exposure within approved scope.

Potential locations include:

- Administrative scripts.
- Configuration files.
- Deployment shares.
- Backup systems.
- Service definitions.
- Scheduled tasks.
- Application configuration.
- Management platforms.
- Endpoint credential stores.

Assess the resulting access rather than simply counting discovered secrets.

## Group and ACL Abuse

Build a relationship map from the current identity to high-value objects.

For each relationship, establish:

1. Which identity has the permission.
2. Which object is affected.
3. Which access right is granted.
4. Whether it is effective.
5. Whether the target is privileged.
6. What action the permission enables.

Do not assume a graph relationship is automatically exploitable.

## Group Policy Abuse

Review GPOs that apply to:

- Domain controllers.
- Privileged servers.
- Management workstations.
- Administrative users.
- Broad workstation populations.

Assess whether an unprivileged principal can modify a policy that affects a more privileged security boundary.

Consider the GPO itself and the underlying SYSVOL permissions.

## Kerberos-Related Escalation

Relevant areas include:

- Kerberoasting.
- AS-REP Roasting.
- Delegation.
- Ticket security.
- Service account exposure.
- Encryption configuration.
- Privileged account authentication patterns.

Assess the complete authentication path and account privilege.

## Certificate-Based Escalation

Review:

- Certificate authority configuration.
- Certificate templates.
- Enrollment rights.
- Template modification rights.
- Subject and SAN configuration.
- Authentication EKUs.
- Issuance requirements.
- Certificate mapping.
- CA permissions.

A certificate configuration issue becomes particularly serious when it enables an unauthorised principal to authenticate as another identity.

## Domain Controller Exposure

Domain controllers are critical security assets.

Review:

- Administrative access.
- Remote management exposure.
- Patch status.
- Group Policy.
- Service configuration.
- Replication permissions.
- Backup access.
- Privileged logon restrictions.
- Certificate services hosted on domain controllers.
- Network segmentation.

Avoid destructive testing or direct modification of domain controller configuration during routine assessment.

## Assessment Methodology

### 1. Establish Initial Access

Document:

- Initial identity.
- Group memberships.
- Host context.
- Authentication method.
- Available network access.
- Privilege level.

### 2. Enumerate the Environment

Collect directory information, permissions, sessions, delegation and certificate services.

### 3. Identify High-Value Targets

Prioritise:

- Domain controllers.
- Privileged groups.
- Tier 0 identities.
- Certificate authorities.
- Backup infrastructure.
- Identity management systems.

### 4. Build Attack Paths

Use directory relationships and manual analysis to identify potential routes from the initial identity to high-value resources.

### 5. Validate Each Relationship

Confirm that permissions are effective and prerequisites are satisfied.

### 6. Assess Exploitability

Consider:

- Required access.
- Authentication.
- Network reachability.
- Existing sessions.
- Security controls.
- Operational constraints.

### 7. Demonstrate Impact

Use the least intrusive proof necessary.

Prefer a dedicated test object or controlled test account over modification of a production privileged identity.

### 8. Document and Remediate

Provide a clear path diagram, affected objects, required conditions and remediation steps.

## Impact Validation

Classify findings carefully:

| Validation level | Meaning |
|---|---|
| Observed configuration | Weakness identified in directory configuration |
| Potential path | Relationships indicate a possible escalation route |
| Validated capability | Permission or access has been confirmed |
| Demonstrated escalation | Approved test confirms higher privilege |
| Domain compromise | Domain-level control has been demonstrated |

Do not claim domain compromise based solely on a theoretical attack path.

## Detection and Defence

Review monitoring for:

- Privileged group changes.
- Directory ACL modifications.
- GPO changes.
- Unusual Kerberos activity.
- Authentication anomalies.
- Service account changes.
- Certificate template changes.
- Replication activity.
- Privileged logons from unexpected systems.

Useful event sources include:

- Windows Security logs.
- Directory Service logs.
- Kerberos operational telemetry.
- PowerShell logs.
- Endpoint detection telemetry.
- Identity provider audit logs.

## Tools and References

- BloodHound.
- SharpHound.
- Impacket.
- NetExec.
- PowerView.
- Rubeus.
- Certipy.
- PingCastle.
- Purple Knight.
- Active Directory PowerShell.

References:

- [SpecterOps](https://specterops.io/)
- [The Hacker Recipes](https://www.thehacker.recipes/)
- [AD Security](https://adsecurity.org/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [Microsoft Active Directory documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/)

## Assessment Checklist

- [ ] Initial identity and privileges documented.
- [ ] Privilege boundaries identified.
- [ ] High-value targets identified.
- [ ] Group membership paths assessed.
- [ ] ACL relationships reviewed.
- [ ] Local administrator paths assessed.
- [ ] Service account exposure reviewed.
- [ ] GPO permissions assessed.
- [ ] Kerberos weaknesses investigated.
- [ ] Delegation configuration reviewed.
- [ ] AD CS assessed.
- [ ] Domain controller exposure reviewed.
- [ ] Attack paths validated.
- [ ] Impact accurately classified.
- [ ] Remediation and retesting requirements documented.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
