
# Active Directory Security Assessment

> Professional reference material for assessing Active Directory environments, identifying attack paths, validating security weaknesses and understanding domain compromise risks.

## Overview

Active Directory (AD) is a central identity and access management platform in many Windows enterprise environments.

It manages:

- User and computer identities.
- Authentication and authorisation.
- Group membership.
- Group Policy.
- Domain services.
- Trust relationships.
- Service accounts.
- Certificate services.
- Privileged access.

An Active Directory assessment examines how identities, permissions, authentication protocols, infrastructure and administrative processes interact.

A seemingly low-privileged account may have an indirect path to significant privileges through misconfigured permissions, delegated access, service accounts or certificate templates.

## Assessment Areas

| Guide | Focus |
|---|---|
| [Enumeration](enumeration.md) | Domain discovery, users, groups, computers, trusts and policy |
| [BloodHound](bloodhound.md) | Attack path analysis and relationship mapping |
| [Kerberos](kerberos.md) | Kerberos authentication and common weaknesses |
| [Password Attacks](password-attacks.md) | Password security, spraying, cracking and credential exposure |
| [ACL Abuse](acl-abuse.md) | Object permissions, ownership and delegated control |
| [Delegation](delegation.md) | Kerberos delegation configurations and risks |
| [Domain Escalation](domain-escalation.md) | Privilege escalation paths and domain compromise conditions |
| [Active Directory Certificate Services](adcs.md) | Certificate templates, enrollment permissions and PKI risks |
| [Persistence and Defence](persistence-and-defence.md) | Persistence risks, detection opportunities and remediation |

## Assessment Methodology

A structured assessment should generally follow this sequence:

1. Confirm scope, authorisation and rules of engagement.
2. Identify domain architecture and available access.
3. Enumerate identities, groups, computers and policies.
4. Map relationships and permissions.
5. Review authentication protocols and service accounts.
6. Identify delegation and certificate service weaknesses.
7. Analyse attack paths.
8. Validate findings using controlled test accounts.
9. Assess impact and potential privilege boundaries.
10. Document evidence, remediation and retesting requirements.

## Important Assessment Considerations

### Scope and Safety

Before testing, confirm:

- Domains and forests in scope.
- Approved assessment accounts.
- Whether domain controllers are in scope.
- Whether production authentication testing is permitted.
- Password spraying and lockout restrictions.
- Whether credential material may be collected.
- Whether privilege escalation is permitted.
- Whether persistence testing is explicitly authorised.
- Approved testing windows and emergency contacts.

### Evidence Handling

Treat credentials, hashes, tickets, private keys and directory exports as sensitive assessment material.

Avoid collecting more than is required to demonstrate a finding. Protect evidence and follow the engagement's retention and disposal requirements.

### Validation

Distinguish between:

- A configuration weakness.
- A theoretically exploitable relationship.
- A confirmed attack path.
- Demonstrated privilege escalation.
- Actual access to sensitive resources.

Do not report an attack path as a confirmed compromise unless it has been validated to the appropriate level.

## Tools and References

Common assessment tools include:

- Active Directory PowerShell module.
- BloodHound and SharpHound.
- Impacket.
- NetExec.
- ldapsearch.
- Kerbrute.
- Rubeus.
- Certipy.
- PingCastle.
- Purple Knight.
- Windows Event Viewer.

Tool availability and permitted use depend on the engagement scope.

## Further Reading

- [Microsoft Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/)
- [MITRE ATT&CK — Enterprise](https://attack.mitre.org/)
- [SpecterOps](https://specterops.io/)
- [The Hacker Recipes](https://www.thehacker.recipes/)
- [AD Security](https://adsecurity.org/)
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
