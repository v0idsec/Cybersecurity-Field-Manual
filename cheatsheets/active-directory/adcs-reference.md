# Active Directory Certificate Services Reference

## Overview

Active Directory Certificate Services (AD CS) provides certificate-based identity and authentication services in Windows environments.

Security reviews should consider:

- Certificate authorities.
- Certificate templates.
- Enrollment permissions.
- Subject and SAN configuration.
- Certificate purposes and EKUs.
- Certificate validity periods.
- Private key protection.
- Certificate mapping and authentication behaviour.

## Native administration commands

```powershell
# List enterprise certificate authorities
certutil -config - -ping

# Display CA configuration
certutil -getconfig

# Display certificate stores
Get-ChildItem Cert:\LocalMachine

# Local machine personal certificates
Get-ChildItem Cert:\LocalMachine\My

# Current user personal certificates
Get-ChildItem Cert:\CurrentUser\My

# Display certificate details
Get-ChildItem Cert:\LocalMachine\My |
    Format-List Subject, Issuer, NotBefore, NotAfter, Thumbprint
```

## Certificate inspection

```cmd
:: Display certificate information
certutil -dump certificate.cer

:: Display certificate stores
certutil -store -user My

:: Display local machine personal store
certutil -store My

:: Verify certificate chain
certutil -verify certificate.cer

:: Display CA configuration
certutil -getconfig
```

## Certificate templates

The AD CS PowerShell module may be available on systems with the appropriate administrative tools.

```powershell
# Import AD CS administration module
Import-Module ADCSAdministration

# View available CA configuration
Get-CATemplate

# View certificate authority information
Get-CertificationAuthority
```

Module availability and cmdlet support vary by installed Windows components and management tools.

## Certificate template review

Review the following properties:

| Property | Security consideration |
|---|---|
| Enrollment permissions | Who can request certificates? |
| Template permissions | Who can modify the template? |
| Subject name | Can requesters supply subject information? |
| SAN configuration | Can requesters influence alternate names? |
| EKU | What purposes can the certificate be used for? |
| Authentication EKUs | Can certificates be used for authentication? |
| Manager approval | Is approval required? |
| Authorized signatures | Are additional signatures required? |
| Validity period | How long are certificates valid? |
| Private key settings | Can private keys be exported? |

## AD CS security terminology

| Term | Description |
|---|---|
| CA | Certificate Authority |
| CSR | Certificate Signing Request |
| EKU | Enhanced Key Usage |
| SAN | Subject Alternative Name |
| PKI | Public Key Infrastructure |
| Enrollment | Requesting a certificate |
| Autoenrolment | Automatic certificate enrolment |
| NTAuth store | Trusted certificate authority store for certain AD authentication scenarios |

## Common security review areas

- Overly broad certificate enrolment permissions.
- Unnecessary template modification rights.
- Unsafe subject or SAN configuration.
- Authentication-capable templates exposed to inappropriate users.
- Weak CA administration controls.
- Poor private key protection.
- Excessive certificate validity periods.
- Inadequate certificate revocation processes.
- Unmonitored CA configuration changes.

## Useful references

- [Microsoft AD CS documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-cs/)
- [Microsoft certutil documentation](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil)

Perform AD CS testing only with explicit authorisation. Avoid issuing, exporting or using authentication certificates outside the agreed test scope.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
