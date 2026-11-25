
# Kerberos Security Assessment

> Professional reference guide for assessing Kerberos authentication, service tickets, delegation and common Active Directory Kerberos weaknesses.

## Contents

- [Overview](#overview)
- [Kerberos Fundamentals](#kerberos-fundamentals)
- [Authentication Flow](#authentication-flow)
- [Service Principal Names](#service-principal-names)
- [Kerberoasting](#kerberoasting)
- [AS-REP Roasting](#as-rep-roasting)
- [Kerberos Delegation](#kerberos-delegation)
- [Ticket Security](#ticket-security)
- [Encryption Types](#encryption-types)
- [Assessment Methodology](#assessment-methodology)
- [Detection Opportunities](#detection-opportunities)
- [Mitigation](#mitigation)
- [Tools and References](#tools-and-references)
- [Assessment Checklist](#assessment-checklist)

---

## Overview

Kerberos is the primary authentication protocol used by Active Directory in many Windows domain environments.

It provides ticket-based authentication and supports single sign-on across domain resources.

Kerberos security assessments focus on:

- Ticket issuance.
- Service account configuration.
- Encryption types.
- Pre-authentication requirements.
- Delegation.
- Ticket lifetime.
- Privileged account exposure.
- Service Principal Names.
- Authentication monitoring.

## Kerberos Fundamentals

Kerberos relies on a trusted Key Distribution Centre (KDC), typically hosted on a domain controller.

The KDC contains two primary logical services:

| Component | Function |
|---|---|
| Authentication Service (AS) | Initial client authentication |
| Ticket Granting Service (TGS) | Issues service tickets |

Important concepts:

- Ticket Granting Ticket (TGT).
- Ticket Granting Service (TGS) ticket.
- Service Principal Name (SPN).
- Session key.
- Realm.
- Principal.
- Ticket lifetime.
- Pre-authentication.

## Authentication Flow

A simplified authentication sequence:

1. Client requests initial authentication.
2. KDC validates the client.
3. KDC issues a Ticket Granting Ticket.
4. Client requests access to a service.
5. KDC issues a service ticket.
6. Client presents the ticket to the service.
7. Service validates the ticket.

The process allows clients to access domain services without repeatedly transmitting their password.

## Service Principal Names

An SPN identifies a service instance associated with an account.

Examples include:

```text
HTTP/web.example.local
MSSQLSvc/sql01.example.local:1433
CIFS/fileserver.example.local
HOST/server01.example.local
```

Review SPNs associated with user accounts.

```powershell
Get-ADUser -Filter * -Properties ServicePrincipalName |
    Where-Object {$_.ServicePrincipalName} |
    Select-Object SamAccountName,ServicePrincipalName
```

Important considerations:

- SPN ownership.
- Account type.
- Password strength.
- Password age.
- Privileged group membership.
- Service account lifecycle.
- Duplicate SPNs.
- Whether managed service accounts are used.

## Kerberoasting

Kerberoasting is an attack technique involving service tickets associated with accounts that have SPNs.

The security concern is that certain service ticket material can be obtained by an authenticated domain user and subjected to offline password guessing.

Risk increases when service accounts use:

- Weak passwords.
- Predictable passwords.
- Reused passwords.
- Excessively privileged identities.
- Long-lived credentials.

### Assessment Considerations

Review:

- User accounts with SPNs.
- Password age.
- Password policy.
- Account privileges.
- Service account ownership.
- Whether gMSAs are available.
- Whether service accounts have unnecessary interactive logon rights.

A service account having an SPN is not itself a vulnerability.

### Risk Factors

| Factor | Significance |
|---|---|
| Weak password | Increases offline guessing risk |
| High privileges | Increases potential impact |
| Long password age | May indicate poor credential hygiene |
| Password reuse | Increases cross-system exposure |
| Legacy service account | May indicate unmanaged credentials |

## AS-REP Roasting

AS-REP Roasting targets accounts that do not require Kerberos pre-authentication.

In certain configurations, authentication material can be obtained without first proving knowledge of the account password.

Review accounts with pre-authentication disabled.

```powershell
Get-ADUser -Filter * -Properties DoesNotRequirePreAuth |
    Where-Object {$_.DoesNotRequirePreAuth} |
    Select-Object SamAccountName,Enabled
```

Assess:

- Whether the configuration is required.
- Whether the account is enabled.
- Account privilege level.
- Password strength.
- Password age.
- Whether the setting is inherited from legacy requirements.

Do not assume that every account with pre-authentication disabled is immediately exploitable.

## Kerberos Delegation

Delegation allows a service to act on behalf of a user when accessing other services.

Types include:

- Unconstrained delegation.
- Constrained delegation.
- Resource-based constrained delegation.

Each has different security implications.

See [Delegation](delegation.md) for detailed assessment guidance.

## Ticket Security

Review:

- TGT lifetime.
- Service ticket lifetime.
- Renewal settings.
- Ticket encryption.
- Ticket protection.
- Account revocation behaviour.
- Privileged account logon patterns.

### Golden Ticket

A Golden Ticket refers to a forged Kerberos Ticket Granting Ticket created using the KRBTGT account's secret material.

It represents a serious domain compromise scenario.

### Silver Ticket

A Silver Ticket refers to a forged service ticket created using a service account's secret material.

It may provide access to a specific service without requiring a normal TGS request to the domain controller.

Both are high-impact techniques and should be treated as controlled validation scenarios, not routine production tests.

## Encryption Types

Review supported Kerberos encryption types.

Common types include:

| Encryption type | Notes |
|---|---|
| AES128 | Modern Kerberos encryption |
| AES256 | Modern Kerberos encryption |
| RC4-HMAC | Legacy encryption with weaker security characteristics |
| DES | Obsolete and should not be used |

Assess:

- Whether legacy encryption is enabled.
- Whether service accounts support AES.
- Whether applications require older encryption.
- Whether exceptions are documented.
- Whether migration plans exist.

Do not assume that the presence of RC4 alone proves a directly exploitable vulnerability. Assess the full configuration and exposure.

## Assessment Methodology

1. Identify domain controllers and Kerberos infrastructure.
2. Enumerate SPNs.
3. Identify service accounts.
4. Review pre-authentication settings.
5. Assess encryption types.
6. Review delegation settings.
7. Examine privileged account usage.
8. Assess ticket lifetime and policy.
9. Correlate findings with directory relationships.
10. Validate findings using approved test accounts.
11. Document exposure and defensive controls.

## Detection Opportunities

Defenders should monitor:

| Event ID | Relevance |
|---|---|
| 4768 | Kerberos TGT requested |
| 4769 | Kerberos service ticket requested |
| 4770 | Kerberos service ticket renewed |
| 4771 | Kerberos pre-authentication failed |
| 4776 | NTLM credential validation |

Useful indicators include:

- Unusual service ticket request volume.
- Unusual encryption types.
- Requests for uncommon SPNs.
- Authentication from unexpected systems.
- Repeated pre-authentication failures.
- Unusual activity involving privileged identities.

Event interpretation depends on operating system version, audit configuration and available telemetry.

## Mitigation

- Use long, random service account passwords.
- Prefer Group Managed Service Accounts where supported.
- Reduce service account privileges.
- Enable Kerberos pre-authentication.
- Remove unnecessary SPNs.
- Disable obsolete encryption types where compatible.
- Restrict delegation.
- Protect privileged identities.
- Monitor Kerberos events.
- Review service account ownership and lifecycle.
- Rotate exposed credentials.
- Protect KRBTGT material and follow Microsoft's recovery guidance after confirmed compromise.

## Tools and References

- Impacket.
- Rubeus.
- NetExec.
- Active Directory PowerShell.
- Wireshark.
- BloodHound.
- Microsoft Kerberos documentation.

References:

- [Microsoft — Kerberos authentication overview](https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview)
- [MITRE ATT&CK — Kerberoasting](https://attack.mitre.org/techniques/T1558/003/)
- [MITRE ATT&CK — AS-REP Roasting](https://attack.mitre.org/techniques/T1558/004/)
- [The Hacker Recipes](https://www.thehacker.recipes/)
- [AD Security](https://adsecurity.org/)

## Assessment Checklist

- [ ] Kerberos infrastructure identified.
- [ ] SPNs enumerated.
- [ ] Service account ownership reviewed.
- [ ] Service account privileges assessed.
- [ ] Pre-authentication settings reviewed.
- [ ] Encryption types assessed.
- [ ] Delegation configuration reviewed.
- [ ] Ticket policies reviewed.
- [ ] Privileged identity exposure assessed.
- [ ] Kerberos logging reviewed.
- [ ] Findings validated safely.
- [ ] Remediation and monitoring recommendations documented.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
