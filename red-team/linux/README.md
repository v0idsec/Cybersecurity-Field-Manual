# Linux Penetration Testing

A practical reference for assessing Linux hosts, identifying security weaknesses, validating privilege escalation paths and evaluating Linux system security.

## Contents

| File | Description |
|---|---|
| [Linux Reconnaissance](linux-reconnaissance.md) | Host discovery, operating system identification and system enumeration |
| [User and Permission Enumeration](user-and-permission-enumeration.md) | Users, groups, file permissions, SUID, SGID and capabilities |
| [Linux Privilege Escalation](linux-privilege-escalation.md) | Privilege escalation methodology and common weaknesses |
| [Sudo and SUID](sudo-and-suid.md) | Sudo configuration, SUID binaries and GTFOBins |
| [Linux Services and Processes](linux-services-and-processes.md) | Services, processes, scheduled tasks and exposed sockets |
| [Linux Persistence and Access](linux-persistence-and-access.md) | SSH keys, accounts, scheduled execution and access mechanisms |
| [Linux Credentials and Secrets](linux-credentials-and-secrets.md) | Credential storage, configuration files and exposed secrets |
| [Linux Container Security](linux-container-security.md) | Docker, Podman, LXC and container security |
| [Linux Hardening and Defence](linux-hardening-and-defence.md) | Defensive configuration, auditing and remediation |
| [Tool Command Reference](tool-command-reference.md) | Linux enumeration and assessment commands |

## Assessment Methodology

A typical Linux assessment follows this workflow:

1. Identify the target host and operating system.
2. Enumerate users, groups and privileges.
3. Identify running processes and exposed services.
4. Review filesystem permissions and sensitive files.
5. Inspect sudo rules, SUID binaries and capabilities.
6. Examine scheduled tasks and service configurations.
7. Identify credentials and secrets exposure.
8. Review container and virtualisation boundaries.
9. Validate privilege escalation opportunities safely.
10. Document evidence, impact and remediation.

## Scope and Authorisation

Before testing:

- Confirm written authorisation.
- Identify approved hosts and IP ranges.
- Confirm permitted testing techniques.
- Establish testing windows.
- Identify production-critical services.
- Confirm whether privilege escalation is permitted.
- Avoid destructive changes or unauthorised persistence.

## Assessment Principles

- Prefer read-only enumeration initially.
- Validate findings rather than relying on automated tool output.
- Avoid modifying system configuration without approval.
- Do not access unrelated user data.
- Protect credentials and sensitive evidence.
- Record exact commands and timestamps.
- Clearly distinguish confirmed vulnerabilities from potential weaknesses.

## Useful References

- [GTFOBins](https://gtfobins.github.io/)
- [HackTricks - Linux Privilege Escalation](https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/)
- [Linux man-pages](https://man7.org/linux/man-pages/)
- [Linux Security](https://www.kernel.org/doc/html/latest/admin-guide/)
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
