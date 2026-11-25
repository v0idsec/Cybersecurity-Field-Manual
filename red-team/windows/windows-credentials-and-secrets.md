# Windows Credentials and Secrets

A reference for assessing credential exposure and secret management across Windows workstations and servers.

The objective is to identify insecure credential storage, excessive access to secrets and weaknesses in authentication protections without unnecessarily collecting or exposing sensitive material.

## 1. Credential Security Overview

Windows environments may handle several types of authentication material:

- Passwords.
- NTLM password hashes.
- Kerberos tickets.
- Security tokens.
- Service account credentials.
- Application secrets.
- API keys.
- Certificates and private keys.
- Windows Credential Manager entries.
- DPAPI-protected data.
- Remote access credentials.

Different credential types have different security properties and exposure risks.

## 2. Common Credential Exposure Locations

Review authorised assessment targets for:

- Application configuration files.
- Deployment scripts.
- PowerShell scripts.
- Batch files.
- Scheduled task arguments.
- Service configuration.
- Installer artefacts.
- Backup files.
- Documentation.
- Source code.
- Environment variables.
- Development tooling configuration.
- Remote administration configuration.

Do not perform indiscriminate searches across user profiles or unrelated data repositories.

## 3. Configuration File Assessment

Common file types worth reviewing include:

| File Type | Potential Risk |
|---|---|
| `.config` | Application credentials and connection strings |
| `.xml` | Deployment and application secrets |
| `.ini` | Application configuration |
| `.ps1` | Embedded credentials or tokens |
| `.bat` / `.cmd` | Hardcoded passwords and command arguments |
| `.yml` / `.yaml` | API keys and service configuration |
| `.json` | Application secrets and tokens |
| `.env` | Environment-specific secrets |
| `.rdp` | Remote connection configuration |
| `.kdbx` | Password database exposure |

The presence of a configuration file is not a vulnerability. Assess its contents, access permissions and operational use.

## 4. Credential Search Considerations

Use targeted, approved searches.

Example PowerShell file inventory:

```powershell
Get-ChildItem 'C:\ProgramData\Example' -Recurse -File `
    -ErrorAction SilentlyContinue |
    Where-Object Extension -In '.config', '.xml', '.ini', '.ps1', '.json'
```

Review candidate files based on their purpose and permissions.

Avoid dumping matching file contents into terminal logs or reports. If a secret is discovered:

1. Stop unnecessary access.
2. Record its location and type.
3. Redact the value.
4. Assess who can access it.
5. Notify the appropriate contact where required.
6. Recommend rotation or revocation.

## 5. Service Credential Assessment

Enumerate service identities:

```powershell
Get-CimInstance Win32_Service |
    Select-Object Name, StartName, State, PathName
```

Assess:

- Service account privilege.
- Credential storage.
- Password rotation.
- Interactive logon rights.
- Shared identities.
- Unnecessary administrative membership.
- Service configuration permissions.

Do not retrieve stored service passwords simply to prove that a service uses a particular account.

## 6. Windows Credential Manager

Windows Credential Manager stores credentials for supported applications and services.

Review the existence and management of stored credentials through approved administrative interfaces.

Useful commands:

```cmd
cmdkey /list
```

Assess:

- Whether credentials are stored unnecessarily.
- Whether access is restricted to the appropriate user.
- Whether remote access credentials persist longer than required.
- Whether shared or privileged credentials are stored on endpoints.

Do not export or disclose credential values.

## 7. DPAPI

The Data Protection API (DPAPI) provides Windows applications with mechanisms for protecting sensitive data.

Security depends on:

- User or machine protection scope.
- Associated account context.
- System configuration.
- Access to relevant profile and system material.
- Backup and recovery controls.

Assessment considerations:

- Are applications using DPAPI appropriately?
- Are protected files accessible to unintended principals?
- Are backup files handled securely?
- Are secrets unnecessarily copied outside protected storage?
- Are applications relying on weak additional protection?

Do not attempt to decrypt unrelated user data.

## 8. LSA and Credential Isolation

Windows Local Security Authority components manage important authentication and security functions.

Relevant protections include:

- LSA protection.
- Credential Guard.
- Protected Process Light.
- Restricted administrative access.
- Secure Boot.
- Virtualisation-based security.

Assess whether protections are enabled and correctly configured for the system's role.

Example:

```powershell
Get-CimInstance -Namespace root\Microsoft\Windows\DeviceGuard `
    -ClassName Win32_DeviceGuard -ErrorAction SilentlyContinue
```

## 9. LSASS Protection

The Local Security Authority Subsystem Service (LSASS) is a high-value security process.

Assess:

- Whether LSASS protection is enabled.
- Whether Credential Guard is deployed where appropriate.
- Whether endpoint security detects suspicious process access.
- Whether administrative privileges are appropriately restricted.
- Whether security event monitoring is configured.

Do not dump LSASS memory or extract authentication material during routine assessment. Such activity requires explicit authorisation and a specific test plan.

## 10. Cached Authentication Material

Windows may maintain cached authentication-related information to support logon scenarios.

Review:

- Whether cached logon configuration is appropriate.
- Whether privileged accounts are used on untrusted endpoints.
- Whether administrative access is restricted.
- Whether Credential Guard and related protections are deployed.
- Whether endpoints are appropriately secured.

Do not extract cached hashes or attempt offline cracking without explicit authorisation.

## 11. Unattended Installation and Deployment Artefacts

Potentially sensitive locations include:

- Unattended installation files.
- Deployment directories.
- Provisioning scripts.
- Software installation packages.
- Configuration management files.
- Imaging and build systems.

Review file permissions, secret storage and retention practices.

Remove or securely dispose of temporary deployment artefacts when no longer required.

## 12. Certificates and Private Keys

Assess:

- Certificate store permissions.
- Private key permissions.
- Certificate validity.
- Key protection.
- Certificate enrolment policies.
- Machine and user certificate usage.
- Unnecessary exportability.
- Expired or unused certificates.

Useful commands:

```cmd
certutil -store My
```

PowerShell:

```powershell
Get-ChildItem Cert:\LocalMachine\My |
    Select-Object Subject, Issuer, NotAfter, Thumbprint, HasPrivateKey
```

Do not export private keys or certificate secrets unless explicitly required and approved.

Certificate-based domain attack paths are covered in the Active Directory ADCS guide.

## 13. PowerShell Secret Handling

Assess scripts and automation for:

- Plaintext passwords.
- Hardcoded API keys.
- Tokens in command arguments.
- Secrets written to transcripts.
- Insecure logging.
- Inappropriate use of environment variables.
- Unprotected configuration files.

Prefer:

- Windows-managed secret storage.
- Managed identities where available.
- Restricted service identities.
- Approved enterprise secret vaults.
- Short-lived credentials.
- Proper secret rotation.

## 14. Remote Access Credentials

Review:

- RDP credential storage.
- Remote management configuration.
- SSH private key permissions.
- VPN configuration.
- Saved remote connections.
- Administrative jump-host practices.

Assess whether remote access is:

- Restricted to approved systems.
- Protected by MFA where supported.
- Logged and monitored.
- Managed through least privilege.
- Revoked when no longer required.

## 15. Validation and Evidence

For a confirmed credential exposure, record:

- Secret type.
- Storage location.
- File or object permissions.
- Account context required to access it.
- Intended application or service.
- Whether the secret is active, where this can be safely established.
- Potential impact.
- Remediation.

Do not include the secret value in the report.

Example:

```text
Finding: Application configuration exposes a service credential.

Location: C:\ProgramData\Example\application.config

Access: Readable by the local Users group.

Secret: Redacted.

Impact: An unprivileged local user can access authentication material
associated with a service account.
```

## 16. Remediation

Recommended controls:

- Remove hardcoded credentials.
- Rotate exposed secrets.
- Restrict file and registry permissions.
- Use managed service identities where appropriate.
- Enable Credential Guard where supported.
- Enable appropriate LSA protections.
- Protect private keys.
- Restrict privileged logons.
- Review saved remote access credentials.
- Secure deployment and backup artefacts.
- Implement secret scanning in development pipelines.
- Monitor suspicious access to sensitive authentication components.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
