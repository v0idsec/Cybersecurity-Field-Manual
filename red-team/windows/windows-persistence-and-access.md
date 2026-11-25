# Windows Persistence and Access

A reference for assessing Windows automatic execution mechanisms, remote access configuration, unauthorised persistence indicators and privileged access pathways.

The purpose of this guide is to identify, validate and document persistence-related security weaknesses and suspicious system changes.

## 1. Persistence Overview

Persistence describes mechanisms that allow software, users or processes to retain access across logons, reboots or other system lifecycle events.

Common persistence locations include:

- Windows services.
- Scheduled tasks.
- Startup folders.
- Registry autorun locations.
- WMI event subscriptions.
- Logon scripts.
- Service configuration.
- Remote management configuration.
- Application update mechanisms.
- Browser and application extensions.

## 2. Autorun Enumeration

Sysinternals Autoruns is a useful reference tool for identifying automatic execution mechanisms.

Reference:

- https://learn.microsoft.com/sysinternals/downloads/autoruns

Review:

- Logon entries.
- Services.
- Scheduled tasks.
- Drivers.
- Explorer extensions.
- Image hijacks.
- AppInit.
- Winsock providers.
- WMI entries.
- Other automatic execution locations.

Assess:

- File path.
- Publisher.
- Digital signature.
- Hash.
- Execution account.
- Startup trigger.
- File permissions.
- Business justification.

An unknown autorun entry is not automatically malicious. Validate its origin and behaviour.

## 3. Registry Autorun Locations

Common registry locations include:

```text
HKCU\Software\Microsoft\Windows\CurrentVersion\Run

HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce

HKLM\Software\Microsoft\Windows\CurrentVersion\Run

HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce
```

Inspect:

```powershell
Get-ItemProperty `
    'HKLM:\Software\Microsoft\Windows\CurrentVersion\Run'

Get-ItemProperty `
    'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run'
```

Also consider the 32-bit registry view where relevant.

Assess whether entries are expected, signed and appropriately permissioned.

## 4. Startup Folders

Common startup locations include:

```text
%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

%ProgramData%\Microsoft\Windows\Start Menu\Programs\Startup
```

Inspect:

```powershell
Get-ChildItem "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup" `
    -Force -ErrorAction SilentlyContinue
```

Review permissions and the legitimacy of referenced executables.

## 5. Scheduled Tasks

Scheduled tasks may execute scripts or applications at logon, startup or defined intervals.

Enumerate:

```powershell
Get-ScheduledTask
```

Review:

- Task principal.
- Execution level.
- Trigger.
- Action.
- Script location.
- File permissions.
- Task security descriptor.
- Creation and modification history.

See `services-and-scheduled-tasks.md`.

## 6. Services

Services can start automatically and run under privileged identities.

Review:

- Newly installed services.
- Unusual service names.
- Unknown executable paths.
- Unsigned binaries.
- Unexpected service accounts.
- Writable service directories.
- Unusual service recovery configuration.

Useful commands:

```powershell
Get-CimInstance Win32_Service |
    Select-Object Name, DisplayName, StartName, State, StartMode, PathName
```

Do not assume a service is malicious solely because its name or binary is unfamiliar.

## 7. WMI Event Subscriptions

Windows Management Instrumentation supports event subscriptions that can trigger actions when specified events occur.

Review:

- Event filters.
- Event consumers.
- Filter-to-consumer bindings.
- Consumer execution context.
- Associated script or command references.

Useful WMI classes include:

- `__EventFilter`
- `__EventConsumer`
- `__FilterToConsumerBinding`
- `CommandLineEventConsumer`
- `ActiveScriptEventConsumer`

Example read-only enumeration:

```powershell
Get-CimInstance -Namespace root\subscription -ClassName __EventFilter

Get-CimInstance -Namespace root\subscription -ClassName __EventConsumer

Get-CimInstance -Namespace root\subscription -ClassName __FilterToConsumerBinding
```

WMI subscriptions may have legitimate administrative purposes. Validate ownership and business justification before classifying them as suspicious.

## 8. Remote Access Configuration

Review remote access mechanisms such as:

- Remote Desktop Protocol.
- Windows Remote Management.
- PowerShell Remoting.
- OpenSSH Server.
- Remote assistance tools.
- Third-party remote administration software.
- Remote management agents.

Assess:

- Whether remote access is required.
- Network restrictions.
- Authentication requirements.
- MFA availability.
- Account permissions.
- Session logging.
- Encryption.
- Credential management.
- Access review processes.

## 9. Remote Desktop Assessment

Check configuration:

```powershell
Get-ItemProperty `
    'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server' |
    Select-Object fDenyTSConnections
```

Firewall rules:

```powershell
Get-NetFirewallRule |
    Where-Object DisplayGroup -Match 'Remote Desktop' |
    Select-Object DisplayName, Enabled, Profile, Direction, Action
```

Review:

- RDP exposure.
- Network-level authentication.
- MFA integration.
- Account restrictions.
- Session timeout.
- Logging.
- Unnecessary administrative access.

## 10. Windows Remote Management

Inspect service and listener configuration:

```powershell
Get-Service WinRM

winrm enumerate winrm/config/listener
```

Review:

- HTTP and HTTPS listeners.
- Trusted hosts configuration.
- Authentication methods.
- Firewall restrictions.
- Administrative group membership.
- Logging.
- Encryption requirements.

Avoid enabling remote management or changing listener configuration during assessment unless authorised.

## 11. OpenSSH

Where installed, review:

- SSH service status.
- Configuration file permissions.
- Authentication methods.
- Allowed users and groups.
- Key permissions.
- Port exposure.
- Logging.
- Account restrictions.

Typical configuration location:

```text
C:\ProgramData\ssh\sshd_config
```

## 12. Event Logging

Useful security event sources include:

| Event ID | Description |
|---|---|
| 4697 | Service installed |
| 7045 | Service installed in System log |
| 4698 | Scheduled task created |
| 4699 | Scheduled task deleted |
| 4700 | Scheduled task enabled |
| 4701 | Scheduled task disabled |
| 4702 | Scheduled task updated |
| 1102 | Security audit log cleared |
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4648 | Logon using explicit credentials |
| 4672 | Special privileges assigned to new logon |

Correlate events with process, account and system context.

## 13. Persistence Validation

For suspected persistence:

1. Identify the execution mechanism.
2. Establish when and how it triggers.
3. Identify the associated account.
4. Inspect the executable or script.
5. Verify digital signatures and file origin.
6. Review file and configuration permissions.
7. Determine whether the mechanism is authorised.
8. Collect relevant event and process evidence.
9. Assess business impact.

Do not create persistence mechanisms on production hosts simply to prove that a particular location is writable.

## 14. Cleanup and Remediation

Where assessment artefacts were explicitly approved:

- Record each artefact before removal.
- Obtain the required approval.
- Remove only assessment-created artefacts.
- Verify normal system operation.
- Document changes.
- Confirm no temporary access remains.

Do not remove suspicious artefacts that may be relevant to an incident investigation without coordination with the organisation's security team.

## 15. Reporting

Document:

- Persistence mechanism.
- Location.
- Associated account.
- Execution trigger.
- File or configuration details.
- Permission weaknesses.
- Evidence.
- Security impact.
- Recommended remediation.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
