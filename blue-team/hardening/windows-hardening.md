# Windows Hardening

## Overview

Windows hardening involves securing workstations and servers through operating system configuration, identity controls, endpoint protection, application restrictions and centralised monitoring.

The appropriate configuration depends on the Windows edition, system role, application requirements and management platform.

## 1. Operating system maintenance

- Use supported Windows releases.
- Apply security updates through an approved patching process.
- Remove unsupported applications and components.
- Keep drivers and firmware updated through trusted vendor channels.
- Enable Secure Boot where supported and operationally appropriate.
- Review installed optional features.
- Restrict access to recovery and administrative environments.

Maintain an inventory of operating system versions and end-of-support dates.

## 2. Account and privilege management

Recommended controls:

- Use standard accounts for everyday activity.
- Separate administrative and standard user accounts.
- Restrict membership of local Administrators.
- Use Windows LAPS or an equivalent managed local administrator password solution.
- Disable or remove unused accounts.
- Review service account permissions.
- Use privileged access management for sensitive administration.
- Monitor privileged group membership changes.

Useful Windows commands:

```powershell
# List local users
Get-LocalUser

# List local administrators
Get-LocalGroupMember -Group "Administrators"

# List local groups
Get-LocalGroup

# Review local account status
Get-LocalUser | Select-Object Name, Enabled, LastLogon
```

Review the output before making account changes.

## 3. Authentication and credential protection

Consider:

- Windows Hello for Business where supported.
- MFA for remote and cloud-based access.
- Credential Guard on supported systems.
- Restricting NTLM where compatibility allows.
- Reducing unnecessary credential caching.
- Protecting privileged accounts from interactive logon on lower-trust systems.
- Monitoring authentication failures and unusual logons.

Do not disable authentication protocols or credential mechanisms without assessing application and domain dependencies.

## 4. Microsoft Defender and endpoint protection

Where Microsoft Defender is deployed:

- Enable real-time protection.
- Enable cloud-delivered protection where permitted.
- Configure tamper protection.
- Review potentially unwanted application protection.
- Configure attack surface reduction rules.
- Monitor endpoint health and security intelligence updates.
- Ensure endpoint alerts reach the central security platform.

Example PowerShell checks:

```powershell
# Review Defender configuration
Get-MpComputerStatus

# Review Defender preferences
Get-MpPreference

# Review detected threats
Get-MpThreatDetection
```

Configuration should be managed through the organisation's approved platform, such as Group Policy, Intune or Microsoft Defender security management.

## 5. Attack Surface Reduction

Attack Surface Reduction (ASR) rules help reduce common attack techniques.

Examples of areas addressed by ASR rules include:

- Office applications creating child processes.
- Executable content launched from email clients.
- Credential theft from the Windows Local Security Authority Subsystem Service (LSASS).
- Scripts and executables exhibiting suspicious behaviour.
- Abuse of vulnerable signed drivers.

Deployment approach:

1. Inventory application and business dependencies.
2. Review available ASR rules.
3. Begin with audit mode where appropriate.
4. Analyse audit events and application compatibility.
5. Pilot selected rules.
6. Move to block mode after validation.
7. Monitor exclusions and exceptions.

Avoid broad exclusions. Every exclusion should have a documented justification and review date.

## 6. Application control

Application control reduces the ability to execute unapproved software.

Options include:

- Windows Defender Application Control (App Control for Business).
- AppLocker, where supported and appropriate.
- Microsoft Intune application control policies.
- Software restriction policies in legacy environments.

A sensible rollout:

1. Inventory installed and executed software.
2. Establish an approved application policy.
3. Test in audit mode.
4. Review blocked or unrecognised applications.
5. Pilot enforcement.
6. Expand enforcement in controlled stages.

## 7. Windows Firewall

Recommended practices:

- Enable the host firewall for all applicable profiles.
- Apply a default-deny inbound policy where compatible.
- Permit only required inbound services.
- Restrict management access to approved networks.
- Review outbound restrictions based on organisational risk.
- Remove obsolete firewall rules.
- Log dropped traffic where useful and proportionate.

Review current configuration:

```powershell
# Firewall profile status
Get-NetFirewallProfile

# List firewall rules
Get-NetFirewallRule

# Show enabled rules
Get-NetFirewallRule -Enabled True
```

Do not blindly replace existing firewall policies on production systems.

## 8. PowerShell security

Consider:

- PowerShell Script Block Logging.
- Module Logging where appropriate.
- Transcription for suitable administrative environments.
- Constrained Language Mode where supported by the security design.
- Signed scripts and controlled execution policies.
- Restricting administrative PowerShell access.
- Monitoring suspicious PowerShell activity.

Execution policy is not a security boundary by itself.

Relevant event channel:

`Microsoft-Windows-PowerShell/Operational`

Commonly useful event:

- 4104 — Script Block Logging, when enabled.

## 9. Windows logging and auditing

Useful telemetry includes:

| Event ID | Description |
|---|---|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4634 | Logoff |
| 4648 | Logon using explicit credentials |
| 4672 | Special privileges assigned to new logon |
| 4688 | Process creation |
| 4697 | Service installed in the Security log |
| 4720 | User account created |
| 4728 | Member added to a security-enabled global group |
| 4732 | Member added to a security-enabled local group |
| 4740 | User account locked out |
| 4768 | Kerberos authentication ticket requested |
| 4769 | Kerberos service ticket requested |
| 4776 | NTLM credential validation |
| 7045 | Service installed in the System log |

Event availability depends on audit policy, Windows version and logging configuration.

Consider Sysmon for additional endpoint telemetry where justified.

## 10. Remote access

- Restrict Remote Desktop to approved users and networks.
- Require Network Level Authentication where appropriate.
- Use MFA through an approved access solution.
- Avoid exposing RDP directly to the internet.
- Monitor remote interactive logons.
- Review Remote Desktop Users membership.
- Use secure administrative access paths.

## 11. Disk and data protection

- Enable BitLocker on supported devices.
- Store recovery keys in an approved, access-controlled system.
- Validate recovery key escrow.
- Restrict removable storage where required.
- Apply data loss prevention controls where appropriate.
- Protect sensitive temporary files and backups.

## 12. Validation checklist

- [ ] Supported Windows version.
- [ ] Security updates current.
- [ ] Secure Boot enabled where supported.
- [ ] BitLocker enabled and recovery keys escrowed.
- [ ] Local administrator membership reviewed.
- [ ] Local administrator passwords managed.
- [ ] Defender healthy and reporting.
- [ ] ASR rules assessed and deployed appropriately.
- [ ] Application control requirements assessed.
- [ ] Windows Firewall enabled.
- [ ] PowerShell logging configured.
- [ ] Security audit policy reviewed.
- [ ] Remote access restricted.
- [ ] Endpoint telemetry centrally collected.
- [ ] Exceptions documented.

## References

- [Microsoft Security Baselines](https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines)
- [Microsoft Defender Antivirus](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-antivirus-in-windows)
- [Attack Surface Reduction Rules](https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference)
- [App Control for Business](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/)
- [Windows Security Auditing](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/basic-audit-policy-recommendations)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
