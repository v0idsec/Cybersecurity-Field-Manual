# Identity and Access Hardening

## Overview

Identity systems control who can access an organisation's resources and what actions they can perform.

A compromised identity can provide access to email, cloud services, internal applications, infrastructure and sensitive information.

Identity hardening focuses on authentication, authorisation, privileged access, account lifecycle management and monitoring.

## 1. Identity security principles

- Verify identity before granting access.
- Apply least privilege.
- Require strong authentication.
- Separate standard and administrative accounts.
- Remove access when it is no longer required.
- Monitor identity and authentication activity.
- Review permissions regularly.
- Treat service identities as security principals.

## 2. Multi-factor authentication

MFA adds an additional verification factor beyond a password.

Prioritise MFA for:

- Privileged accounts.
- Remote access.
- Cloud administration.
- Email and collaboration platforms.
- VPN and remote access gateways.
- Sensitive business applications.
- Financial and administrative systems.

Prefer phishing-resistant methods where supported, such as FIDO2 security keys or passkeys.

Avoid relying exclusively on SMS-based authentication for high-risk accounts where stronger options are available.

MFA should be supported by recovery procedures that do not create an easier route around the control.

## 3. Password security

Consider:

- Long passwords or passphrases.
- Blocklists for commonly used and compromised passwords.
- Password managers.
- Protection against password spraying.
- Secure password reset procedures.
- Unique credentials for different systems.
- Removal of default and shared credentials.

Avoid arbitrary password rotation schedules unless required by policy, regulation or evidence of compromise. Prioritise strong passwords, MFA and rapid response to exposed credentials.

## 4. Privileged access management

Administrative access should be limited, monitored and appropriately protected.

Recommended practices:

- Separate administrative and everyday accounts.
- Restrict privileged group membership.
- Use just-in-time access where possible.
- Require approval for sensitive elevation.
- Use dedicated privileged access workstations or controlled administration paths.
- Monitor privileged authentication.
- Review emergency or break-glass accounts.
- Remove standing privileges when they are no longer required.

Privileged accounts should not be used for routine email, web browsing or general productivity tasks.

## 5. Joiner, mover and leaver processes

Identity lifecycle management ensures that access matches a person's current responsibilities.

| Process | Security requirements |
|---|---|
| Joiner | Verify identity, assign approved access and enforce MFA |
| Mover | Review existing access and adjust permissions |
| Leaver | Disable accounts, revoke sessions and recover assets |
| Contractor | Apply expiry dates and sponsor ownership |
| Emergency access | Record justification, approval and review |

Deprovisioning should include:

- Interactive accounts.
- Cloud sessions and refresh tokens.
- VPN and remote access.
- Application access.
- API tokens and personal access tokens.
- Privileged group membership.
- Physical access credentials where applicable.

## 6. Service accounts and workload identities

Service accounts often have persistent access and may be overlooked during routine reviews.

Recommended controls:

- Use managed identities or managed service accounts where supported.
- Avoid interactive logon for service identities.
- Restrict permissions to the required resources.
- Avoid shared service credentials.
- Rotate secrets through approved mechanisms.
- Store credentials in a secrets management platform.
- Monitor authentication from unexpected systems.
- Document the application owner and business purpose.

Workload identities should receive narrowly scoped permissions and should not inherit broad human administrator privileges.

## 7. Conditional access and context-aware controls

Where supported, use contextual access policies to evaluate:

- User identity.
- Device compliance.
- Authentication strength.
- Sign-in risk.
- Location and network context.
- Application sensitivity.
- Session characteristics.

Examples:

- Require MFA for external access.
- Block legacy authentication where compatible.
- Require compliant devices for sensitive applications.
- Restrict administrative portals to approved access paths.
- Apply stronger controls to high-risk sign-ins.

Test policies in report-only or controlled modes where available. Maintain an emergency access strategy that is separately secured and monitored.

## 8. Account and permission reviews

Perform periodic reviews of:

- Privileged roles.
- Group membership.
- Guest accounts.
- Dormant accounts.
- Service accounts.
- Application registrations.
- OAuth grants and delegated permissions.
- API keys and access tokens.
- External collaboration permissions.

Useful questions:

1. Does the account still have a valid owner?
2. Is the access still required?
3. Is the permission broader than necessary?
4. Is the authentication method appropriate?
5. Is the account monitored?
6. Does the account have an expiry or review date?

## 9. Identity monitoring

Monitor for:

- Repeated authentication failures.
- Password spraying patterns.
- Unusual sign-in locations or devices.
- MFA fatigue or repeated MFA prompts.
- New privileged role assignments.
- New application credentials.
- Suspicious consent grants.
- Legacy authentication usage.
- Unusual service account activity.
- Dormant accounts becoming active.

Correlate identity events with endpoint, network and cloud activity where possible.

## 10. Example Microsoft Entra ID review areas

For organisations using Microsoft Entra ID, review:

- Authentication methods and registration.
- Conditional Access policies.
- Privileged Identity Management.
- Emergency access accounts.
- Enterprise application permissions.
- App registrations and secrets.
- Guest user access.
- Sign-in and audit log retention.
- Risk-based identity policies where licensed.

Use the Microsoft Entra admin centre and approved automation tools to assess configuration. Do not make tenant-wide changes without testing their impact.

## 11. Validation checklist

- [ ] MFA enabled for users.
- [ ] Phishing-resistant MFA used for privileged access where possible.
- [ ] Legacy authentication reviewed and restricted.
- [ ] Privileged roles reviewed.
- [ ] Administrative accounts separated.
- [ ] Break-glass accounts secured and monitored.
- [ ] Joiner/mover/leaver processes documented.
- [ ] Dormant accounts identified.
- [ ] Guest access reviewed.
- [ ] Service accounts have owners.
- [ ] Workload permissions follow least privilege.
- [ ] Application grants reviewed.
- [ ] Conditional Access policies tested.
- [ ] Identity events centrally monitored.
- [ ] Access reviews scheduled.

## References

- [Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/)
- [Microsoft Identity Secure Score](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-identity-secure-score)
- [NIST SP 800-63B — Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html)
- [CISA — Identity and Access Management](https://www.cisa.gov/)
- [Australian Essential Eight](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
