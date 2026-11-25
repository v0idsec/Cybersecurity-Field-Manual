# Hardening Fundamentals

## Overview

System hardening reduces the number of ways an attacker can compromise, control or move through an environment.

It involves identifying unnecessary functionality, reducing exposure, enforcing security controls and continuously checking that systems remain in an approved state.

Hardening applies to more than operating systems. Applications, network devices, cloud services, identities, containers and management platforms all require appropriate security configurations.

## 1. Core principles

### Least functionality

Only enable the features, services, ports and applications required for the system's intended purpose.

Examples:

- Remove unused applications.
- Disable unnecessary services.
- Restrict administrative interfaces.
- Remove unused network listeners.
- Disable obsolete protocols.
- Avoid installing development tools on production systems unless required.

### Least privilege

Users, applications and services should receive only the permissions necessary to perform their tasks.

Examples:

- Standard user accounts for everyday activity.
- Separate administrative accounts.
- Role-based access control.
- Restricted service accounts.
- Just-in-time privilege elevation where supported.

### Defence in depth

Do not rely on a single security control.

A workstation should ideally have several complementary protections:

- Secure boot and firmware protections.
- Full-disk encryption.
- Endpoint protection.
- Application control.
- Host firewall.
- Restricted privileges.
- Security logging.
- Centralised monitoring.

### Secure defaults

Systems should begin in a secure configuration rather than relying on administrators to discover and disable insecure defaults.

Examples:

- MFA enabled.
- Public access disabled unless explicitly required.
- Default credentials removed.
- Unnecessary services disabled.
- Secure communication protocols enforced.

### Continuous verification

Configuration drift can gradually undermine a previously secure system.

Regularly compare actual configurations against approved baselines and investigate deviations.

## 2. Attack surface reduction

An attack surface consists of the interfaces, services, software, accounts and pathways that could be abused.

| Attack surface | Example reduction |
|---|---|
| Network | Restrict exposed ports and management interfaces |
| Applications | Remove unused applications and plugins |
| Identity | Enforce MFA and reduce privileged accounts |
| Operating system | Disable unnecessary services |
| Cloud | Disable public access and restrict IAM permissions |
| Data | Restrict access and encrypt sensitive information |
| Remote access | Require strong authentication and approved access paths |
| Firmware | Apply updates and enable supported security features |

## 3. Hardening lifecycle

A repeatable hardening process:

1. **Discover** — identify systems, software, services and dependencies.
2. **Assess** — compare the current configuration against approved requirements.
3. **Prioritise** — identify security gaps based on risk and exposure.
4. **Plan** — define changes, owners, testing and rollback.
5. **Implement** — apply approved configuration changes.
6. **Validate** — confirm that controls operate as expected.
7. **Monitor** — detect configuration drift and control failures.
8. **Review** — reassess requirements as systems and threats change.

## 4. Risk-based prioritisation

Not every configuration issue has equal importance.

Consider:

- Whether the system is internet-facing.
- Whether it stores sensitive or regulated information.
- Whether the weakness enables privilege escalation.
- Whether exploitation is known or practical.
- Whether compensating controls exist.
- Whether the system is business-critical.
- Whether the system is exposed to untrusted users or networks.

A useful prioritisation model:

| Priority | Typical characteristics |
|---|---|
| Critical | Directly exploitable exposure with severe potential impact |
| High | Significant weakness affecting sensitive or important systems |
| Medium | Meaningful weakness with limited exposure or compensating controls |
| Low | Defence-in-depth improvement or low-impact configuration gap |

Use the organisation's approved risk methodology rather than treating this table as a universal scoring system.

## 5. Configuration management

A secure environment needs a defined source of truth.

Maintain:

- Approved configuration baselines.
- System ownership records.
- Change management records.
- Exceptions and risk acceptances.
- Patch and update status.
- Configuration assessment results.
- Remediation evidence.

Exceptions should have an owner, justification, approval, compensating controls and review date.

## 6. Common hardening mistakes

- Applying benchmarks without understanding application dependencies.
- Disabling services that business applications rely on.
- Treating every recommendation as equally urgent.
- Making production changes without a rollback plan.
- Assuming antivirus alone provides endpoint security.
- Allowing permanent administrator access.
- Failing to monitor configuration drift.
- Ignoring legacy systems that cannot support modern controls.
- Treating compliance as proof that a system is secure.

## 7. Useful references

- [CIS Critical Security Controls](https://www.cisecurity.org/controls)
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)
- [NIST SP 800-123 — Guide to General Server Security](https://csrc.nist.gov/pubs/sp/800/123/final)
- [NIST SP 800-70 — Security Configuration Checklists](https://csrc.nist.gov/pubs/sp/800/70/r5/final)
- [Australian ISM](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
