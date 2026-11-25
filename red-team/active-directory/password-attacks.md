
# Active Directory Password Security and Attacks

> Professional reference guide for assessing password policy, credential exposure, password spraying risks and authentication weaknesses in Active Directory environments.

## Contents

- [Overview](#overview)
- [Password Security Assessment](#password-security-assessment)
- [Password and Account Policies](#password-and-account-policies)
- [Password Spraying](#password-spraying)
- [Credential Exposure](#credential-exposure)
- [Password Reuse](#password-reuse)
- [Offline Password Assessment](#offline-password-assessment)
- [NTLM Considerations](#ntlm-considerations)
- [Privileged Account Protection](#privileged-account-protection)
- [Assessment Methodology](#assessment-methodology)
- [Detection and Monitoring](#detection-and-monitoring)
- [Mitigation](#mitigation)
- [Tools and References](#tools-and-references)
- [Assessment Checklist](#assessment-checklist)

---

## Overview

Weak, reused or exposed credentials remain a significant source of Active Directory compromise.

Password assessments examine whether authentication controls adequately protect domain identities and whether credentials can be obtained or abused through weaknesses in the environment.

Assessment areas include:

- Password policy.
- Account lockout policy.
- Password reuse.
- Service account credentials.
- Credential exposure.
- NTLM authentication.
- Password spraying.
- Offline password strength.
- Privileged account protection.
- Authentication monitoring.

Password testing must follow the engagement's explicit rules of engagement. Even low-volume authentication attempts can cause account lockouts or disrupt business operations.

## Password Security Assessment

Assess password security at both policy and implementation levels.

A strong domain password policy does not guarantee that every account is protected.

Consider:

- Fine-Grained Password Policies.
- Service account exceptions.
- Legacy accounts.
- Password expiration requirements.
- Password history.
- Minimum password length.
- Password complexity.
- Compromised password screening.
- Password reset procedures.
- Privileged account policies.

### Domain Password Policy

```powershell
Get-ADDefaultDomainPasswordPolicy
```

### Fine-Grained Password Policies

```powershell
Get-ADFineGrainedPasswordPolicy -Filter *
```

### Account Attributes

```powershell
Get-ADUser -Filter * -Properties `
    PasswordLastSet,PasswordNeverExpires,`
    PasswordNotRequired,Enabled,LockedOut
```

Review exceptions individually. A policy exception may be legitimate, but it should be documented and risk-assessed.

## Password and Account Policies

Important settings include:

| Setting | Assessment consideration |
|---|---|
| Minimum password length | Resistance to guessing |
| Password history | Prevention of immediate reuse |
| Lockout threshold | Balance between guessing resistance and denial-of-service risk |
| Lockout duration | Recovery from repeated failures |
| Observation window | Failed-attempt counting behaviour |
| Password complexity | Password composition requirements |
| Password expiration | Credential lifecycle and operational impact |
| Fine-Grained Policies | Differences between account groups |

Modern password policy should prioritise sufficient length, compromised-password screening, MFA and protection against common or reused passwords rather than relying solely on arbitrary complexity rules.

## Password Spraying

Password spraying attempts a small number of commonly used passwords across multiple accounts rather than attempting many passwords against one account.

The technique is relevant because it may avoid simplistic per-account lockout thresholds.

### Assessment Considerations

Before any authentication testing, establish:

- Written authorisation.
- Approved test accounts.
- Explicitly permitted target accounts.
- Maximum attempt limits.
- Lockout thresholds.
- Monitoring contacts.
- Approved testing windows.
- Emergency stop conditions.

Prefer dedicated assessment accounts.

Do not conduct broad password spraying against production users without explicit approval and a documented safety plan.

### Review Areas

Assess whether:

- MFA is enforced.
- Legacy authentication remains enabled.
- Smart lockout or equivalent controls are configured.
- Authentication attempts are monitored.
- Risk-based access controls are enforced.
- Password protection controls are deployed.
- Privileged accounts have stronger requirements.

### Validation

A password policy weakness should be validated through configuration review and approved test identities wherever possible.

Avoid using real employee passwords as proof of concept.

## Credential Exposure

Credentials may be exposed through:

- Scripts.
- Configuration files.
- Deployment pipelines.
- Shared folders.
- Backup files.
- Documentation.
- Application configuration.
- Log files.
- Memory dumps.
- Unattended installation files.
- Legacy administrative tooling.

Review the security of:

- Administrative scripts.
- Scheduled task configurations.
- Service definitions.
- Deployment shares.
- Software installation packages.
- Backup repositories.
- Management systems.

Credential discovery must remain within the agreed data-access scope.

## Password Reuse

Password reuse increases the impact of a single credential compromise.

Review whether:

- Service accounts share credentials.
- Local administrator passwords are reused.
- Administrative accounts use the same password across tiers.
- Application accounts share credentials.
- Legacy systems retain old credentials.
- Password rotation occurs after staff or supplier changes.

Where supported, use Windows LAPS to manage unique local administrator passwords.

## Offline Password Assessment

Offline password assessment evaluates the strength of credential material obtained through an approved assessment process.

Potential sources include:

- Approved password audit exports.
- Controlled test account material.
- Service ticket material.
- Approved password hash datasets.

The assessment should focus on password strength and exposure rather than unnecessary collection of credential material.

Consider:

- Password length.
- Common patterns.
- Dictionary exposure.
- Predictability.
- Reuse.
- Service account password age.
- Password generation practices.

Protect password audit data as highly sensitive material. Do not upload client credential material to public cracking services or third-party platforms.

## NTLM Considerations

NTLM is a legacy Windows authentication protocol that may remain in use for compatibility.

Assess:

- Whether NTLM is required.
- Which systems use NTLM.
- Whether NTLMv1 remains enabled.
- NTLM relay exposure.
- SMB signing.
- LDAP signing.
- Extended Protection for Authentication.
- Credential exposure through legacy protocols.

Where possible, migrate workloads towards Kerberos and modern authentication mechanisms.

## Privileged Account Protection

Privileged accounts should have stronger protections than ordinary user accounts.

Review:

- Separate administrative identities.
- MFA enforcement.
- Privileged access workstations.
- Tiered administration.
- Interactive logon restrictions.
- Credential Guard.
- Protected Users group suitability.
- Administrative account lifecycle.
- Just-in-time access.
- Emergency access procedures.

Avoid using highly privileged identities for routine workstation activity.

## Assessment Methodology

1. Establish password testing restrictions.
2. Enumerate domain and fine-grained password policies.
3. Review account-level password settings.
4. Identify privileged identities.
5. Review service account credential management.
6. Assess credential storage locations within scope.
7. Review NTLM usage and configuration.
8. Evaluate MFA and conditional access coverage.
9. Review authentication monitoring.
10. Validate weaknesses using approved test accounts.
11. Document risk and remediation.

## Detection and Monitoring

Useful Windows Security events include:

| Event ID | Description |
|---|---|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4740 | Account locked out |
| 4768 | Kerberos TGT requested |
| 4769 | Kerberos service ticket requested |
| 4771 | Kerberos pre-authentication failed |
| 4776 | NTLM credential validation |

Investigate:

- Repeated failures across multiple accounts.
- Authentication from unusual source systems.
- Successful authentication following repeated failures.
- Unusual privileged account logons.
- Legacy authentication usage.
- Unexpected service account activity.

Correlate events across domain controllers and endpoints.

## Mitigation

- Enforce MFA for privileged and remote access.
- Use long, unique passwords.
- Screen passwords against known compromised-password lists.
- Deploy Windows LAPS.
- Use gMSAs for supported services.
- Reduce NTLM usage.
- Disable NTLMv1.
- Protect credential storage.
- Restrict privileged logons.
- Implement tiered administration.
- Monitor authentication activity.
- Rotate credentials after confirmed exposure.
- Review legacy accounts and exceptions.
- Use risk-based authentication controls.

## Tools and References

### Tools

- Active Directory PowerShell.
- NetExec.
- Kerbrute.
- Impacket.
- Hashcat.
- John the Ripper.
- BloodHound.
- PingCastle.
- Windows Security Event Viewer.

### References

- [Microsoft — Password policy](https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-policy)
- [Microsoft — Account lockout policy](https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/account-lockout-policy)
- [Microsoft — Windows LAPS](https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-overview)
- [NIST SP 800-63B](https://pages.nist.gov/800-63-4/sp800-63b.html)
- [MITRE ATT&CK — Brute Force](https://attack.mitre.org/techniques/T1110/)

## Assessment Checklist

- [ ] Password policy reviewed.
- [ ] Fine-Grained Password Policies reviewed.
- [ ] Account-level exceptions identified.
- [ ] Privileged accounts assessed.
- [ ] Service account password management reviewed.
- [ ] Password reuse risks investigated.
- [ ] Credential storage reviewed within scope.
- [ ] NTLM usage assessed.
- [ ] MFA coverage reviewed.
- [ ] Password testing restrictions confirmed.
- [ ] Authentication monitoring assessed.
- [ ] Sensitive credential material securely handled.
- [ ] Remediation recommendations documented.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
