# Windows Cheatsheets

Quick-reference commands and syntax for Windows administration, troubleshooting, security assessments and incident investigation.

## Contents

| File | Description |
|---|---|
| [powershell-reference.md](powershell-reference.md) | PowerShell commands, syntax and pipelines |
| [cmd-reference.md](cmd-reference.md) | Traditional Windows Command Prompt |
| [system-information-and-enumeration.md](system-information-and-enumeration.md) | System, hardware, software and account enumeration |
| [process-and-service-management.md](process-and-service-management.md) | Processes, services, scheduled tasks and startup |
| [networking-commands.md](networking-commands.md) | Interfaces, connections, DNS and firewall |
| [event-logs-and-investigation.md](event-logs-and-investigation.md) | Windows Event Logs, filtering and investigation |
| [registry-and-filesystem.md](registry-and-filesystem.md) | Registry, files, permissions and hashes |
| [active-directory-commands.md](active-directory-commands.md) | Domain discovery and Active Directory administration |

## Usage

Commands are provided as quick references. Check command help and validate changes before using unfamiliar options on production systems.

PowerShell:

```powershell
Get-Help Command-Name -Full
Get-Command
```

Command Prompt:

```cmd
command /?
```

Only perform security testing and administrative actions on systems you own or are authorised to assess.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
