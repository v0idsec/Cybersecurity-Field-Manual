# Windows Defence and Hardening

A reference for assessing Windows security controls, endpoint protection, application control, authentication protections, logging and operating system hardening.

This guide supports both offensive security assessments and defensive configuration reviews.

## 1. Security Baseline Assessment

Review the system against:

- Microsoft Security Baselines.
- Microsoft Defender recommendations.
- CIS Benchmarks.
- Organisational security policies.
- Relevant regulatory requirements.
- Application-specific security requirements.

References:

- https://learn.microsoft.com/windows/security/
- https://learn.microsoft.com/windows/security/operating-system-security/device-management/windows-security-configuration-framework/security-baselines
- https://www.cisecurity.org/cis-benchmarks

Do not apply baseline settings blindly. Consider system role, application compatibility and operational requirements.

## 2. Windows Defender

Inspect status:

```powershell
Get-MpComputerStatus
```

Review configuration:

```powershell
Get-MpPreference
```

Assess:

- Real-time protection.
- Behaviour monitoring.
- Cloud-delivered protection.
- Automatic sample submission.
- Potentially unwanted application protection.
- Exclusion configuration.
- Tamper protection.
- Signature update status.
- Endpoint detection capabilities.

### Exclusion Review

Defender exclusions can create significant blind spots.

Review:

- Path exclusions.
- Process exclusions.
- Extension exclusions.
- Security team approval.
- Business justification.
- Exclusion ownership and review dates.

Do not add exclusions during assessment unless explicitly authorised.

## 3. Microsoft Defender Firewall

Inspect profiles:

```powershell
Get-NetFirewallProfile
```

Review rules:

```powershell
Get-NetFirewallRule |
    Select-Object DisplayName, Enabled, Direction, Action, Profile
```

Assess:

- Domain profile.
- Private profile.
- Public profile.
- Default inbound behaviour.
- Default outbound behaviour.
- Broad allow rules.
- Unnecessary exposed services.
- Remote administration restrictions.
- Logging configuration.

Example logging review:

```powershell
Get-NetFirewallProfile |
    Select-Object Name, LogAllowed, LogBlocked, LogFileName
```

## 4. User Account Control

UAC helps control elevation of administrative processes.

Inspect:

```powershell
Get-ItemProperty `
    'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' |
    Select-Object EnableLUA, ConsentPromptBehaviorAdmin,
        ConsentPromptBehaviorUser, PromptOnSecureDesktop
```

Assess:

- Whether UAC is enabled.
- Administrative consent behaviour.
- Secure desktop configuration.
- Standard user elevation behaviour.
- Administrative account usage.

Do not treat UAC as a replacement for least privilege or application control.

## 5. Windows LAPS

Windows Local Administrator Password Solution manages local administrator passwords.

Assess:

- Whether LAPS is deployed.
- Whether managed accounts are configured.
- Password rotation policy.
- Password access permissions.
- Backup location.
- Directory permissions.
- Monitoring of password retrieval.

Avoid retrieving live administrator passwords during routine testing.

Reference:

- https://learn.microsoft.com/windows-server/identity/laps/laps-overview

## 6. Credential Protection

Review deployment of:

- Credential Guard.
- LSA protection.
- Secure Boot.
- Virtualisation-based security.
- Restricted administrative logon.
- Windows Hello for Business, where applicable.
- MFA for remote and privileged access.

Inspect Device Guard status:

```powershell
Get-CimInstance -Namespace root\Microsoft\Windows\DeviceGuard `
    -ClassName Win32_DeviceGuard
```

Assess the actual policy state and hardware support.

## 7. Application Control

Application control reduces the execution of untrusted software.

Relevant technologies:

- Windows Defender Application Control.
- AppLocker.
- Smart App Control.
- Software Restriction Policies.
- Microsoft Defender Attack Surface Reduction rules.

Review:

- Policy deployment.
- Enforcement mode.
- Policy exceptions.
- Administrative bypass paths.
- Script restrictions.
- Publisher rules.
- Audit events.

Do not assume audit mode provides the same protection as enforced mode.

## 8. Attack Surface Reduction

Microsoft Defender Attack Surface Reduction rules can reduce common attack techniques.

Assess applicable protections relating to:

- Office application child processes.
- Executable content from email.
- Script execution.
- Credential theft.
- Untrusted USB execution.
- Vulnerable signed drivers.
- WMI and process abuse.

Inspect configuration:

```powershell
Get-MpPreference |
    Select-Object AttackSurfaceReductionRules_Ids,
        AttackSurfaceReductionRules_Actions
```

Confirm the meaning of the returned values and whether rules are configured in audit or block mode.

## 9. Windows Update and Patch Management

Review:

- Update installation status.
- Supported OS lifecycle.
- Security update coverage.
- Update deployment policy.
- Reboot management.
- Third-party software patching.
- Vulnerability remediation processes.

Example:

```powershell
Get-HotFix |
    Sort-Object InstalledOn -Descending
```

Patch assessment should use the applicable Microsoft update catalogue and security advisories rather than relying exclusively on a list of installed hotfixes.

## 10. BitLocker and Data Protection

Assess:

- BitLocker deployment.
- Encryption coverage.
- Recovery key management.
- TPM requirements.
- Removable storage encryption.
- Recovery key access permissions.
- Encryption policy compliance.

Inspect:

```powershell
Get-BitLockerVolume
```

Do not expose recovery keys in assessment reports or evidence.

## 11. Secure Boot and Firmware

Assess:

- Secure Boot status.
- TPM availability.
- Firmware update practices.
- Boot configuration protection.
- External boot restrictions.
- Firmware password policy, where applicable.
- Device lifecycle management.

Example:

```powershell
Confirm-SecureBootUEFI

Get-Tpm
```

Some commands may be unavailable on unsupported hardware or virtual machines.

## 12. Remote Access Hardening

Review:

- RDP exposure.
- Network-level authentication.
- MFA integration.
- WinRM configuration.
- OpenSSH configuration.
- Remote administration group membership.
- Firewall restrictions.
- Administrative jump-host controls.

Remote access should be restricted to approved users and networks.

## 13. Windows Auditing

Inspect audit policy:

```cmd
auditpol /get /category:*
```

Important audit areas include:

- Account logon.
- Logon and logoff.
- Account management.
- Privilege use.
- Process creation.
- Object access.
- Policy changes.
- System events.
- Detailed tracking.

### Useful Event IDs

| Event ID | Description |
|---|---|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4634 | Logoff |
| 4648 | Explicit credentials used |
| 4672 | Special privileges assigned |
| 4688 | Process creation |
| 4697 | Service installation |
| 4698 | Scheduled task creation |
| 4720 | User account created |
| 4722 | User account enabled |
| 4724 | Password reset attempt |
| 4728 | Member added to security-enabled global group |
| 4732 | Member added to security-enabled local group |
| 1102 | Security audit log cleared |

Event availability depends on audit policy and operating system configuration.

## 14. Sysmon

Sysmon provides detailed system activity telemetry.

Useful event categories include:

- Process creation.
- Network connections.
- Image loading.
- Process access.
- File creation.
- Registry modification.
- DNS queries.
- Named pipes.

Reference:

- https://learn.microsoft.com/sysinternals/downloads/sysmon

Assess:

- Whether Sysmon is installed.
- Configuration coverage.
- Event forwarding.
- Log retention.
- Alerting.
- Configuration maintenance.

Sysmon is a telemetry source, not a complete security solution by itself.

## 15. Windows Event Forwarding and Centralised Logging

Review whether important security events are:

- Collected.
- Forwarded.
- Retained.
- Protected from unauthorised modification.
- Monitored.
- Correlated with endpoint telemetry.

Assess coverage across workstations, servers and privileged systems.

## 16. PowerShell Security

Review:

- Script block logging.
- Module logging.
- Transcription.
- Execution restrictions.
- Application control integration.
- Module trust.
- Administrative execution.
- Centralised log collection.

Execution policy should not be relied upon as the primary control preventing malicious script execution.

## 17. Services and Scheduled Tasks

Assess:

- Unnecessary services.
- Service account privileges.
- Service binary permissions.
- Scheduled task permissions.
- Unapproved automatic execution.
- Service and task change monitoring.

See `services-and-scheduled-tasks.md`.

## 18. Hardening Priorities

Suggested priority order:

1. Maintain supported and patched operating systems.
2. Restrict local administrative privileges.
3. Deploy endpoint protection and tamper protection.
4. Enforce MFA for privileged and remote access.
5. Protect credentials using supported Windows security features.
6. Apply application control.
7. Restrict unnecessary remote access.
8. Harden firewall configuration.
9. Centralise security logging.
10. Review local accounts and permissions.
11. Encrypt sensitive devices and data.
12. Monitor privileged configuration changes.

## 19. Reporting

For each weakness, document:

- Security control.
- Current configuration.
- Expected configuration.
- Scope of affected systems.
- Evidence.
- Business impact.
- Remediation.
- Validation method.

Distinguish between a missing control, a misconfiguration and a confirmed exploitable vulnerability.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
