# PowerShell and LOLBins

A professional reference for assessing PowerShell execution, Windows-native utilities, legitimate operating system binaries and their potential security implications.

Windows includes extensive scripting and administration capabilities. These can support legitimate administration, but may also be abused by attackers.

This guide focuses on assessment, detection and controlled validation.

## 1. PowerShell Overview

PowerShell is a command-line shell and scripting environment built on the .NET platform.

Relevant capabilities include:

- System administration.
- Process management.
- Service management.
- Registry interaction.
- Filesystem operations.
- Network communication.
- Windows Management Instrumentation (WMI).
- Common Information Model (CIM).
- Remote administration.
- Security configuration management.

## 2. PowerShell Environment Reconnaissance

```powershell
# PowerShell version
$PSVersionTable

# Current execution policy
Get-ExecutionPolicy -List

# Available modules
Get-Module -ListAvailable

# Current session configuration
Get-PSSessionConfiguration

# Current language mode
$ExecutionContext.SessionState.LanguageMode

# PowerShell host
$Host
```

Assess:

- PowerShell version.
- Installed modules.
- Execution policy.
- Language mode.
- Remoting configuration.
- Logging configuration.
- Application control restrictions.

Execution policy is not a security boundary. It primarily controls script execution behaviour and should not be treated as an effective substitute for application control.

## 3. PowerShell Execution Context

Assess:

- Current user.
- Integrity level.
- Token privileges.
- Process architecture.
- Elevated status.
- Language mode.
- Session configuration.

```powershell
whoami /all

[Environment]::Is64BitProcess

[Environment]::Is64BitOperatingSystem

$ExecutionContext.SessionState.LanguageMode
```

## 4. Script and Module Assessment

Review:

- Script permissions.
- Module installation locations.
- Module trust.
- Signed scripts.
- Dependency integrity.
- Hardcoded credentials.
- External downloads.
- Script logging.
- Administrative execution.

Potential risks include:

- User-writable scripts executed by privileged tasks.
- Untrusted modules imported into administrative sessions.
- Scripts containing credentials.
- Unrestricted execution of downloaded content.
- Excessive permissions on shared script directories.

## 5. PowerShell Logging

Important logging mechanisms include:

### Script Block Logging

Records script blocks processed by PowerShell.

Relevant event log:

```text
Microsoft-Windows-PowerShell/Operational
```

Common event ID:

- 4104 — Script block logging.

### Module Logging

Can record pipeline execution details for configured modules.

### Transcription

Can record PowerShell session input and output.

Assess:

- Whether logging is enabled.
- Whether logs are centralised.
- Whether sensitive values are exposed in logs.
- Whether log retention is sufficient.
- Whether administrators can modify or clear local logs.

## 6. Constrained Language Mode

Constrained Language Mode restricts certain PowerShell language features.

Inspect:

```powershell
$ExecutionContext.SessionState.LanguageMode
```

Common modes include:

- FullLanguage.
- ConstrainedLanguage.
- RestrictedLanguage.
- NoLanguage.

Assess whether application control policies enforce the intended restrictions.

Do not assume that seeing ConstrainedLanguage in one session proves the entire host is protected.

## 7. Windows Native Utilities

Windows includes many legitimate binaries that can interact with processes, services, files, network resources and system configuration.

Examples include:

| Utility | Purpose |
|---|---|
| `cmd.exe` | Command interpreter |
| `powershell.exe` | Windows PowerShell |
| `pwsh.exe` | PowerShell 7+ |
| `wmic.exe` | Legacy WMI command-line utility |
| `wscript.exe` | Windows Script Host |
| `cscript.exe` | Console Script Host |
| `mshta.exe` | HTML Application host |
| `rundll32.exe` | DLL function execution utility |
| `regsvr32.exe` | COM registration utility |
| `certutil.exe` | Certificate administration |
| `bitsadmin.exe` | Background Intelligent Transfer Service administration |
| `schtasks.exe` | Scheduled task management |
| `sc.exe` | Service control |
| `reg.exe` | Registry management |
| `msiexec.exe` | Windows Installer |
| `installutil.exe` | .NET installation utility |
| `forfiles.exe` | File selection and command execution |

These binaries are not inherently malicious. Their use must be evaluated in context.

## 8. LOLBAS

LOLBAS stands for Living Off The Land Binaries, Scripts and Libraries.

The project documents legitimate Windows components that can be abused for security-relevant purposes.

Reference:

- https://lolbas-project.github.io/

Relevant categories include:

- Execution.
- Download.
- Upload.
- Persistence.
- UAC bypass.
- Credential theft.
- Discovery.
- Lateral movement.
- Proxy execution.

Use LOLBAS as a research and detection reference, not as a list of techniques to run indiscriminately against production systems.

## 9. Assessing Suspicious Native Binary Usage

For each suspicious process, review:

- Parent process.
- Command line.
- User identity.
- Integrity level.
- Executable path.
- Digital signature.
- File hash.
- Network activity.
- Child processes.
- Execution frequency.
- Business justification.

Example process inventory:

```powershell
Get-CimInstance Win32_Process |
    Select-Object ProcessId, ParentProcessId, Name, ExecutablePath, CommandLine
```

Command-line data may contain credentials or other sensitive information. Redact before storing evidence.

## 10. Application Control

Assess controls designed to restrict execution:

- AppLocker.
- Windows Defender Application Control (WDAC).
- Smart App Control, where applicable.
- Microsoft Defender Attack Surface Reduction rules.
- PowerShell Constrained Language Mode.
- Software restriction policies, where still deployed.

Review:

- Policy coverage.
- Enforcement mode.
- Exceptions.
- Administrative bypass paths.
- Logging.
- Policy maintenance.

## 11. Detection Opportunities

Potential detection areas include:

- Unusual PowerShell parent processes.
- Encoded command-line arguments.
- Unexpected script execution.
- Suspicious LOLBin usage.
- Script execution from temporary directories.
- Unusual network connections.
- Unexpected child processes.
- Unsigned modules.
- PowerShell logging gaps.

Useful Windows telemetry:

- Security Event Log.
- PowerShell Operational Log.
- Sysmon.
- Microsoft Defender telemetry.
- EDR process and network events.

## 12. Useful Sysmon Events

| Event ID | Description |
|---|---|
| 1 | Process creation |
| 3 | Network connection |
| 7 | Image loaded |
| 10 | Process access |
| 11 | File creation |
| 12–14 | Registry events |
| 22 | DNS query |

Event collection depends on Sysmon configuration. Not every event is necessarily enabled.

## 13. Safe Assessment Methodology

When assessing PowerShell and LOLBin exposure:

1. Identify the binary or scripting mechanism.
2. Establish whether the behaviour is legitimate.
3. Review the execution context.
4. Inspect parent-child relationships.
5. Determine whether application controls apply.
6. Review logging and detection coverage.
7. Validate using benign test activity.
8. Document the security implications.

Avoid executing untrusted payloads or using native utilities to bypass controls on production systems without explicit approval.

## 14. Reporting

Document:

- Binary or scripting mechanism.
- Executing account.
- Command or behaviour.
- Parent process.
- Relevant security controls.
- Observed logging.
- Potential impact.
- Evidence.
- Recommended restrictions or detections.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
