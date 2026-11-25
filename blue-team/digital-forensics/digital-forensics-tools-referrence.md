# Digital Forensics Tools Reference

## Overview

This reference lists common tools used for digital evidence acquisition, examination, analysis and reporting.

Tool selection should be based on the investigation requirements, supported evidence formats, validation, licensing and organisational policy.

## Disk and File-System Forensics

| Tool | Purpose |
|---|---|
| Autopsy | Graphical forensic analysis |
| The Sleuth Kit | File-system and disk-image analysis |
| FTK Imager | Evidence acquisition and image examination |
| X-Ways Forensics | Commercial forensic examination |
| Arsenal Image Mounter | Mounting forensic images |
| bulk_extractor | Extracting features from forensic images |
| PhotoRec | File recovery and carving |
| Foremost | File carving |
| ewf-tools | Working with E01 evidence images |

### The Sleuth Kit

List image partitions:

```bash
mmls evidence.dd
```

Display file-system information:

```bash
fsstat -o 2048 evidence.dd
```

The partition offset is illustrative. Obtain the actual offset from the image's partition layout.

List files:

```bash
fls -r -o 2048 evidence.dd
```

Extract a file by metadata address:

```bash
icat -o 2048 evidence.dd <metadata_address> > recovered-file
```

Confirm the relevant syntax and offsets against the installed version and image format.

## Memory Forensics

| Tool | Purpose |
|---|---|
| Volatility 3 | Memory image analysis |
| WinPmem | Windows memory acquisition |
| AVML | Linux memory acquisition |
| LiME | Linux memory acquisition |
| Magnet RAM Capture | Windows memory acquisition |
| Belkasoft RAM Capturer | Windows memory acquisition |

Example:

```bash
vol -f memory.raw windows.info
```

```bash
vol -f memory.raw windows.pslist
```

```bash
vol -f memory.raw windows.pstree
```

```bash
vol -f memory.raw windows.netscan
```

## Windows Forensics

| Tool | Purpose |
|---|---|
| Eric Zimmerman's Tools | Windows artefact examination |
| Registry Explorer | Registry analysis |
| EvtxECmd | Windows Event Log parsing |
| PECmd | Prefetch examination |
| AmcacheParser | Amcache analysis |
| MFTECmd | MFT and USN Journal analysis |
| Timeline Explorer | Timeline examination |
| KAPE | Targeted artefact collection and processing |

Examples:

```powershell
Get-WinEvent -LogName Security -MaxEvents 100
```

```powershell
Get-FileHash .\evidence.evtx -Algorithm SHA256
```

```powershell
Get-ScheduledTask
```

## Linux Forensics

| Tool | Purpose |
|---|---|
| Plaso | Timeline creation |
| log2timeline | Forensic timeline extraction |
| Sleuth Kit | File-system analysis |
| Autopsy | Graphical forensic analysis |
| Volatility 3 | Memory analysis |
| Journalctl | Systemd journal examination |
| ausearch | Linux audit log searches |

Examples:

```bash
journalctl --since "2026-11-24 00:00:00"
```

```bash
last
```

```bash
stat suspicious-file
```

## Network Forensics

| Tool | Purpose |
|---|---|
| Wireshark | Graphical packet analysis |
| TShark | Command-line packet analysis |
| Zeek | Network security monitoring |
| NetworkMiner | Network forensic analysis |
| Arkime | Large-scale packet capture search |
| tcpdump | Packet capture |
| Brim | Network evidence exploration |

Examples:

```bash
tcpdump -r capture.pcap
```

```bash
tshark -r capture.pcapng -Y dns
```

```bash
zeek -r capture.pcap
```

## Email and Browser Forensics

| Tool | Purpose |
|---|---|
| Hindsight | Chromium browser artefact analysis |
| Browser History Examiner | Browser history examination |
| Autopsy | Browser and file artefact examination |
| Aid4Mail | Email forensic analysis |
| Thunderbird | Email inspection |
| Microsoft Purview Audit | Microsoft 365 audit investigations |
| eDiscovery tools | Mailbox and content preservation |

Tool availability and capabilities vary by platform and licensing.

## Cloud Forensics

| Tool or service | Purpose |
|---|---|
| AWS CloudTrail | AWS API activity |
| AWS Config | Resource configuration history |
| Microsoft Purview | Microsoft 365 compliance and audit |
| Microsoft Entra audit logs | Identity administration events |
| Azure Activity Log | Azure control-plane activity |
| Google Cloud Audit Logs | Google Cloud activity |
| Cloud provider CLI tools | Evidence export and investigation |
| Cloud-native SIEM | Centralised audit analysis |

## Evidence Integrity

### Linux

```bash
sha256sum evidence.img
```

### Windows

```powershell
Get-FileHash .\evidence.img -Algorithm SHA256
```

### macOS

```bash
shasum -a 256 evidence.img
```

## Tool Validation

Before using a tool in a formal investigation:

1. Confirm the source and authenticity.
2. Review the supported evidence formats.
3. Confirm the installed version.
4. Validate expected behaviour.
5. Understand known limitations.
6. Preserve tool output.
7. Document parameters.
8. Record errors and warnings.

Where appropriate, compare results using independent tools.

## Tool Selection Considerations

| Requirement | Considerations |
|---|---|
| Disk imaging | Source compatibility, write protection, hashing |
| Memory acquisition | OS support, acquisition impact |
| Timeline analysis | Timestamp handling, artefact coverage |
| Event log analysis | EVTX support, parsing accuracy |
| Packet analysis | PCAP support, protocol coverage |
| Cloud investigation | Permissions, retention, API completeness |
| Reporting | Reproducibility, evidence references |

## Operational Warning

Forensic tools can modify systems, expose sensitive information or produce incomplete results.

Use them only within authorised investigations. Preserve original evidence, work from verified copies where practical and document all examination activity.

## Further Reading

- [The Sleuth Kit](https://www.sleuthkit.org/)
- [Autopsy](https://www.autopsy.com/)
- [Volatility Foundation](https://volatilityfoundation.org/)
- [Eric Zimmerman's Tools](https://ericzimmerman.github.io/)
- [Plaso](https://plaso.readthedocs.io/)
- [Wireshark](https://www.wireshark.org/)
- [Zeek](https://zeek.org/)
- [KAPE](https://www.kroll.com/en/insights/publications/cyber/kroll-artifact-parser-and-extractor-kape)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
