# Evidence Preservation and Handling

## Overview

Evidence preservation supports incident investigation, root cause analysis, internal reviews and potential legal proceedings.

Evidence may include logs, endpoint artefacts, memory captures, disk images, emails, cloud audit records, network captures, screenshots and witness accounts.

Collection and handling must be appropriate to the investigation, organisational policy and applicable legal requirements.

## Evidence handling principles

1. Preserve original evidence wherever possible.
2. Minimise changes to affected systems.
3. Record who collected each item and when.
4. Document collection methods and tools.
5. Maintain integrity checks where appropriate.
6. Store evidence securely.
7. Restrict access to authorised personnel.
8. Maintain a chain of custody when required.
9. Record any transformations or analysis performed.
10. Retain evidence according to approved policy.

## Common evidence sources

### Endpoint

- Disk images.
- Memory captures.
- Windows Event Logs.
- Sysmon logs.
- PowerShell logs.
- Linux system and authentication logs.
- EDR telemetry.
- Process and network information.
- Browser artefacts.
- Scheduled tasks and services.
- File system metadata.

### Network

- Firewall logs.
- DNS logs.
- Proxy logs.
- VPN logs.
- NetFlow or equivalent telemetry.
- Packet captures.
- Network device configuration.
- Intrusion detection alerts.

### Identity and cloud

- Sign-in logs.
- Audit logs.
- Role assignment history.
- Application consent records.
- Access key activity.
- Cloud resource changes.
- Storage access logs.
- Email audit records.

### User and business records

- Original emails with headers.
- User reports.
- Help desk tickets.
- Change records.
- Access approval records.
- Relevant communications.
- Third-party notifications.

## Volatile evidence

Some evidence is lost when a system is shut down or restarted.

Potential volatile information includes:

- Running processes.
- Active network connections.
- Logged-on users.
- Open files.
- Memory contents.
- Temporary credentials and tokens.
- In-memory malware.
- Active sessions.

Collection should be prioritised based on the incident, available capability and operational risk.

Do not delay urgent containment of a dangerous incident solely to collect every volatile artefact.

## Collection record

For each evidence item, record:

- Evidence ID.
- Incident ID.
- Description.
- Source system or account.
- Collection date and time.
- Timezone.
- Collector.
- Collection method.
- Tool and version, where relevant.
- Original location.
- File format and size.
- Hash value, where appropriate.
- Storage location.
- Handling restrictions.
- Related notes.

## Integrity verification

Cryptographic hashes can help demonstrate that a collected file has not changed since the hash was calculated.

Example using SHA-256:

```bash
sha256sum evidence-file.raw
```

PowerShell:

```powershell
Get-FileHash -Path .\evidence-file.raw -Algorithm SHA256
```

Record the hash alongside the evidence item.

A matching hash supports integrity verification between the compared copies. It does not independently prove that the original evidence was authentic or collected correctly.

## Chain of custody

A chain of custody records the handling and transfer of evidence.

| Field | Description |
|---|---|
| Evidence ID | Unique evidence identifier |
| Date and time | Transfer or handling timestamp |
| Released by | Person transferring the item |
| Received by | Person accepting the item |
| Purpose | Reason for transfer |
| Storage location | Location before and after transfer |
| Condition | Packaging or integrity observations |
| Signatures | Required acknowledgement |

Every transfer should be documented according to organisational procedure.

## Evidence storage

Use approved storage with:

- Access controls.
- Encryption where appropriate.
- Audit logging.
- Integrity protection.
- Backup and retention controls.
- Separation from general-purpose user storage.
- Documented access approvals.

Do not store sensitive evidence in personal cloud storage, public file-sharing services or unapproved removable media.

## Evidence preservation mistakes

Avoid:

- Rebooting or shutting down systems without considering volatile evidence.
- Running unnecessary tools on affected systems.
- Modifying original files.
- Exporting only screenshots when raw logs are available.
- Failing to record timezones.
- Overwriting original evidence with analysis output.
- Storing evidence without access controls.
- Sharing sensitive evidence through unapproved channels.
- Treating a hash as proof of the entire collection process.

## Legal and privacy considerations

Evidence may contain personal, confidential or commercially sensitive information.

Follow applicable privacy, employment, surveillance, retention and evidence-handling requirements. Involve legal counsel or an appropriate privacy officer when required.

Do not access unrelated personal information merely because it is technically available.

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
