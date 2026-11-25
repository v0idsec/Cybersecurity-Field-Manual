
# Active Directory Certificate Services (AD CS)

> Professional reference guide for assessing Active Directory Certificate Services, certificate authorities, templates, enrollment permissions and certificate-based authentication risks.

## Contents

- [Overview](#overview)
- [AD CS Architecture](#ad-cs-architecture)
- [Certificate Fundamentals](#certificate-fundamentals)
- [Certificate Authorities](#certificate-authorities)
- [Certificate Templates](#certificate-templates)
- [Enrollment and Permissions](#enrollment-and-permissions)
- [Certificate-Based Authentication](#certificate-based-authentication)
- [Common Misconfiguration Categories](#common-misconfiguration-categories)
- [Template and CA Assessment](#template-and-ca-assessment)
- [Assessment Methodology](#assessment-methodology)
- [Detection and Monitoring](#detection-and-monitoring)
- [Mitigation](#mitigation)
- [Tools and References](#tools-and-references)
- [Assessment Checklist](#assessment-checklist)

---

## Overview

Active Directory Certificate Services (AD CS) provides public key infrastructure (PKI) capabilities within Windows environments.

It allows organisations to issue and manage certificates used for:

- User authentication.
- Computer authentication.
- TLS.
- Smart cards.
- Code signing.
- Document signing.
- Device identity.
- Application authentication.

Misconfigured certificate authorities or templates can allow users to obtain certificates with unintended privileges.

In some circumstances, certificate-based authentication can provide a route to impersonate another identity.

AD CS should be treated as a critical identity infrastructure component.

## AD CS Architecture

Common components include:

| Component | Purpose |
|---|---|
| Certification Authority | Issues and manages certificates |
| Certificate Template | Defines certificate properties and requirements |
| Enrollment Services | Allows clients to request certificates |
| Enrollment Agent | Requests certificates on behalf of other identities |
| Certificate Revocation List | Identifies revoked certificates |
| Authority Information Access | Provides CA certificate and related information |
| Web Enrollment | Web-based certificate request functionality |
| Certificate Enrollment Web Services | Supports remote certificate enrollment |

Assess the architecture and identify which components are exposed to domain users, administrators and external networks.

## Certificate Fundamentals

A certificate typically contains:

- Subject.
- Subject Alternative Name (SAN).
- Public key.
- Issuer.
- Validity period.
- Key usage.
- Extended Key Usage (EKU).
- Signature algorithm.
- Serial number.

Important properties include:

| Property | Assessment relevance |
|---|---|
| Subject | Identity represented by certificate |
| SAN | Additional identity information |
| EKU | Permitted certificate purposes |
| Key Usage | Cryptographic operations permitted |
| Validity | Certificate lifetime |
| Issuer | Issuing CA |
| Template | Policy governing issuance |

## Certificate Authorities

Enumerate:

- Enterprise CAs.
- Standalone CAs.
- CA host systems.
- Published templates.
- Enrollment endpoints.
- CA administrators.
- CA configuration permissions.
- Web enrollment services.
- Revocation infrastructure.

Assess whether the CA is appropriately protected and whether its management permissions are restricted.

A compromised enterprise CA can have broad implications for domain identity security.

## Certificate Templates

Certificate templates define the conditions under which certificates may be issued.

Review:

- Template name.
- Template purpose.
- Subject name settings.
- SAN configuration.
- EKUs.
- Key usage.
- Enrollment permissions.
- Template modification permissions.
- Issuance requirements.
- Manager approval.
- Validity period.
- Renewal period.
- Compatibility settings.

### Important Template Attributes

| Attribute | Purpose |
|---|---|
| `msPKI-Certificate-Name-Flag` | Subject and SAN construction behaviour |
| `msPKI-Enrollment-Flag` | Enrollment and issuance behaviour |
| `pKIExtendedKeyUsage` | Extended key usages |
| `nTSecurityDescriptor` | Template access permissions |
| `msPKI-RA-Signature` | Required registration authority signatures |
| `pKIExpirationPeriod` | Certificate validity period |

The meaning of a configuration depends on its interaction with other template properties.

## Enrollment and Permissions

Review who can:

- Enrol in a template.
- Auto-enrol.
- Modify a template.
- Modify CA configuration.
- Manage CA permissions.
- Approve certificate requests.
- Issue certificates.
- Manage revocation.

Pay particular attention to broad enrollment groups and unexpected template modification rights.

A user being able to enrol in a certificate template is not automatically a vulnerability. The template's identity and authentication properties determine the risk.

## Certificate-Based Authentication

Certificates may be used for domain authentication.

Assess:

- Whether the certificate supports authentication.
- Which identity the certificate represents.
- Whether SAN values are controlled by the requester.
- Whether certificate mapping is secure.
- Whether strong certificate mapping is enforced.
- Whether the certificate is valid and trusted.
- Whether the issuing CA is trusted for authentication.

Certificate identity mapping has evolved across Windows versions and security updates. Assess the target environment's actual behaviour rather than assuming all certificate mapping configurations work identically.

## Common Misconfiguration Categories

AD CS assessment frameworks commonly classify issues by combinations of template and CA configuration.

The following are useful categories to investigate:

| Category | General weakness |
|---|---|
| ESC1-style | Enrolment and subject configuration may permit unintended identity representation |
| ESC2-style | Broad certificate purposes or authentication capabilities |
| ESC3-style | Misuse of enrollment agent functionality |
| ESC4-style | Excessive template modification permissions |
| ESC5-style | Weak permissions over PKI-related objects or infrastructure |
| ESC6-style | Risky CA-level subject/SAN configuration |
| ESC7-style | Excessive CA management permissions |
| ESC8-style | Insecure web enrollment or NTLM relay exposure |
| ESC9-style | Risky certificate mapping or security extension handling |
| ESC10-style | Weak certificate mapping configuration |
| ESC11-style | Insecure RPC enrollment interface protection |
| ESC13-style | Certificate issuance conditions involving group-linked issuance policy |
| ESC15-style | Vulnerable certificate template schema or processing behaviour |

These labels are shorthand categories, not proof of exploitability. Their applicability depends on the AD CS configuration, Windows version, patch level and certificate mapping behaviour.

## Template and CA Assessment

### Identify Published Templates

Review all published certificate templates and determine which are available to ordinary domain users.

### Review Enrollment Permissions

Identify:

- Authenticated Users.
- Domain Users.
- Domain Computers.
- Broad application groups.
- Custom delegated groups.

Determine whether the enrollment scope is justified.

### Review Subject and SAN Behaviour

Assess whether requesters can influence identity attributes in certificates.

This is particularly important for certificates used in authentication.

### Review EKUs

Investigate templates that include:

- Client Authentication.
- Smart Card Logon.
- PKINIT Client Authentication.
- Any Purpose.
- Certificate Request Agent.

Review combinations of EKUs and enrollment rights rather than considering each property independently.

### Review Template Modification Rights

Determine who can modify:

- Enrollment permissions.
- Subject name flags.
- EKUs.
- Issuance requirements.
- Validity settings.
- Other security-sensitive template attributes.

### Review CA Permissions

Identify who can manage CA configuration, issue certificates and modify CA security settings.

## Assessment Methodology

1. Identify AD CS infrastructure.
2. Enumerate enterprise and standalone CAs.
3. Identify published certificate templates.
4. Review template properties.
5. Review enrollment permissions.
6. Review template modification permissions.
7. Assess subject and SAN configuration.
8. Review EKUs and key usage.
9. Assess issuance and approval requirements.
10. Review CA-level permissions.
11. Assess web enrollment and RPC interfaces.
12. Review certificate mapping behaviour.
13. Correlate certificate relationships with privileged identities.
14. Validate using approved test identities and controlled certificates.
15. Document affected templates, permissions and impact.

## Detection and Monitoring

Monitor:

- Certificate requests.
- Certificate issuance.
- Certificate template changes.
- CA configuration changes.
- Enrollment permission changes.
- CA administrative activity.
- Unexpected certificate authentication.
- Certificate revocation.
- Changes to PKI-related directory objects.

Relevant event sources include:

- Certification Authority operational logs.
- Windows Security logs.
- Directory Service changes.
- CA database records.
- Domain controller authentication logs.

Commonly relevant CA events include certificate request, issuance and denial records. Exact event availability depends on CA configuration and audit policy.

## Mitigation

- Restrict certificate enrollment permissions.
- Remove unnecessary templates.
- Require approval for sensitive certificate issuance.
- Restrict template modification rights.
- Restrict CA administration.
- Remove unnecessary enrollment agent permissions.
- Review EKUs and subject name configuration.
- Enforce appropriate certificate mapping protections.
- Secure web enrollment endpoints.
- Protect RPC enrollment interfaces.
- Reduce NTLM relay exposure.
- Monitor certificate issuance.
- Revoke certificates issued through confirmed abuse.
- Protect CA private keys.
- Maintain a documented certificate lifecycle.

## Tools and References

### Tools

- Certipy.
- Certify.
- PSPKIAudit.
- BloodHound.
- Active Directory PowerShell.
- certutil.
- Microsoft Certificate Services management tools.

### References

- [SpecterOps — Certified Pre-Owned](https://specterops.io/wp-content/uploads/sites/3/2022/06/Certified_Pre-Owned.pdf)
- [Certipy](https://github.com/ly4k/Certipy)
- [PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)
- [Microsoft — Active Directory Certificate Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-cs/active-directory-certificate-services-overview)
- [Microsoft — Certificate Templates](https://learn.microsoft.com/en-us/windows-server/identity/ad-cs/certificate-template-concepts)
- [MITRE ATT&CK — Steal or Forge Authentication Certificates](https://attack.mitre.org/techniques/T1649/)

## Assessment Checklist

- [ ] AD CS infrastructure identified.
- [ ] Enterprise CAs enumerated.
- [ ] Published templates enumerated.
- [ ] Enrollment permissions reviewed.
- [ ] Template modification permissions reviewed.
- [ ] Subject and SAN settings assessed.
- [ ] EKUs and key usage reviewed.
- [ ] Issuance requirements reviewed.
- [ ] CA administrative permissions assessed.
- [ ] Enrollment endpoints assessed.
- [ ] Certificate mapping behaviour reviewed.
- [ ] Privileged identity exposure assessed.
- [ ] Findings validated safely.
- [ ] Remediation and revocation requirements documented.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
