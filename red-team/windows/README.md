# Windows Penetration Testing

A practical reference for assessing Windows workstations, servers and standalone Windows environments during authorised security engagements.

This section covers host reconnaissance, local security boundaries, privilege escalation, service configuration, credential exposure, PowerShell, Windows utilities, persistence mechanisms and defensive controls.

Active Directory-specific assessment techniques are documented separately in `../active-directory/`.

## Guides

| Guide | Description |
|---|---|
| [Windows Reconnaissance](windows-reconnaissance.md) | Host, operating system, network and environment enumeration |
| [User and Group Enumeration](user-and-group-enumeration.md) | Local accounts, groups, privileges, sessions and access tokens |
| [Windows Privilege Escalation](windows-privilege-escalation.md) | Local privilege escalation methodology and common weaknesses |
| [Services and Scheduled Tasks](services-and-scheduled-tasks.md) | Service configuration, permissions, executable paths and scheduled tasks |
| [Credentials and Secrets](windows-credentials-and-secrets.md) | Credential exposure, stored secrets and credential protections |
| [Registry and ACLs](windows-registry-and-acls.md) | Registry permissions, filesystem ACLs and security boundaries |
| [PowerShell and LOLBins](powershell-and-lolbins.md) | PowerShell assessment, native utilities and LOLBAS references |
| [Persistence and Access](windows-persistence-and-access.md) | Persistence mechanisms, remote access and access auditing |
| [Defence and Hardening](windows-defence-and-hardening.md) | Defender, firewall, UAC, application control and logging |
| [Tool Command Reference](tool-command-reference.md) | PowerShell, CMD, Sysinternals and enumeration commands |

## Assessment Methodology

A Windows host assessment should generally follow this sequence:

1. Establish authorisation, scope and testing restrictions.
2. Identify the Windows version, edition, build and system role.
3. Enumerate local users, groups, privileges and active sessions.
4. Review network interfaces, routes and exposed services.
5. Assess filesystem and registry permissions.
6. Inspect services, scheduled tasks and startup mechanisms.
7. Review credential exposure and security configuration.
8. Identify privilege escalation opportunities.
9. Validate findings using controlled, minimally invasive techniques.
10. Review defensive controls and logging.
11. Collect evidence and document remediation.
12. Remove approved test artefacts and complete close-out.

## Scope Boundaries

This section primarily addresses:

- Windows client operating systems.
- Windows Server systems.
- Standalone Windows hosts.
- Local accounts and security groups.
- Local privilege boundaries.
- Windows services and scheduled tasks.
- Local security configuration.
- Windows-native administration and security utilities.

Domain-specific attack paths belong in the Active Directory section.

## Operational Considerations

- Only assess systems covered by written authorisation.
- Avoid modifying production security settings without approval.
- Do not extract or retain unnecessary credentials.
- Treat memory, registry and configuration data as potentially sensitive.
- Avoid destructive exploitation and uncontrolled service interruption.
- Use the least intrusive method that demonstrates impact.
- Record the exact host, account context and conditions associated with findings.
- Preserve evidence and follow the engagement's data handling requirements.

## Related Resources

- `../active-directory/`
- `../linux/`
- `../network-pentesting/`
- `../exploitation/` (if maintained as a future reference)
- `../../cheatsheets/windows/`
- `../../cheatsheets/active-directory/`
- `../../engagement-operations/`

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
