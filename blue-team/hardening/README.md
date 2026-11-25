# Hardening

System hardening is the process of reducing the attack surface of systems, applications, identities and infrastructure through secure configuration, access controls, patch management and ongoing validation.

This section covers practical hardening principles and guidance for Windows, Linux, identity platforms, networks and cloud environments.

## Contents

| File | Description |
|---|---|
| [hardening-fundamentals.md](hardening-fundamentals.md) | Core principles, attack surface reduction and hardening lifecycle |
| [windows-hardening.md](windows-hardening.md) | Windows workstation and server security |
| [linux-hardening.md](linux-hardening.md) | Linux operating system security |
| [identity-and-access-hardening.md](identity-and-access-hardening.md) | Identity security, authentication and privilege management |
| [network-and-cloud-hardening.md](network-and-cloud-hardening.md) | Network infrastructure and cloud security controls |
| [configuration-baselines-and-compliance.md](configuration-baselines-and-compliance.md) | Security baselines, standards and compliance |
| [hardening-validation-and-monitoring.md](hardening-validation-and-monitoring.md) | Testing, monitoring and maintaining hardened systems |
| [hardening-tools-reference.md](hardening-tools-reference.md) | Tools for configuration assessment and validation |

## Core objectives

- Reduce unnecessary services, software and exposed functionality.
- Apply secure configuration baselines.
- Enforce least privilege and strong authentication.
- Maintain supported software and security patches.
- Protect sensitive data and credentials.
- Enable appropriate logging and security monitoring.
- Validate configurations and investigate deviations.
- Maintain change records and rollback procedures.

## Important considerations

Hardening is not a one-time activity. Systems change, vulnerabilities emerge and business requirements evolve.

Before applying changes:

1. Obtain the required approval.
2. Understand the system's business purpose and dependencies.
3. Assess compatibility and operational impact.
4. Back up relevant configurations and data.
5. Test changes in a representative environment.
6. Document the change and rollback procedure.
7. Validate the result after implementation.

A secure configuration that breaks a critical business service is not a successful outcome.

## Related references

- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)
- [Microsoft Security Baselines](https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines)
- [Australian Signals Directorate — Information Security Manual](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism)
- [Australian Signals Directorate — Essential Eight](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight)
- [NIST Security and Privacy Controls (SP 800-53)](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
