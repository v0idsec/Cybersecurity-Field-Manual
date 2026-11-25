# Physical Security Tools Reference

A practical reference to equipment, software and documentation resources used during authorised physical security assessments.

This page focuses on legitimate assessment, inspection, documentation and validation equipment rather than tools for covert entry or bypassing security systems.

## 1. Documentation and planning

| Tool | Purpose |
|---|---|
| Microsoft Excel | Asset inventories, access reviews and assessment records |
| Microsoft Visio | Facility and security architecture diagrams |
| draw.io | Site layouts and control diagrams |
| Obsidian | Assessment notes and knowledge management |
| Joplin | Structured assessment notes |
| Dradis | Security assessment evidence and reporting |
| PlexTrac | Assessment workflow and reporting |

## 2. Photography and documentation

| Equipment | Purpose |
|---|---|
| Digital camera | Approved site and equipment photography |
| Smartphone camera | General assessment documentation |
| Clipboard and notebook | Site observations and inspection records |
| Measuring tape | Approved physical measurements |
| Laser distance meter | Facility measurements where permitted |
| Inspection torch | Visual inspection of approved areas |
| Label printer | Labelling designated test equipment |

Follow client photography and privacy requirements.

## 3. Network and infrastructure assessment

Physical security assessments may include authorised reviews of network-connected physical security systems.

| Tool | Purpose |
|---|---|
| Nmap | Approved network discovery and service identification |
| Wireshark | Protocol analysis |
| tcpdump | Packet capture |
| arp-scan | Local network discovery |
| NetBox | Infrastructure inventory and documentation |
| Greenbone / OpenVAS | Vulnerability assessment |
| Nessus | Vulnerability assessment |

Network testing of CCTV, access-control or building management systems requires explicit approval and suitable operational safeguards.

## 4. Wireless and RF assessment

Wireless systems may support access-control, monitoring and facility operations.

Potential assessment areas:

- Wi-Fi infrastructure.
- Wireless access-control components.
- Wireless environmental sensors.
- Radio-based monitoring systems.
- Wireless alarm communications.

Tools may include:

| Tool | Purpose |
|---|---|
| Wireshark | Wireless protocol analysis where supported |
| Kismet | Wireless network discovery and monitoring |
| Aircrack-ng | Authorised wireless security assessment |
| SDR++ | Software-defined radio signal visualisation |
| GNU Radio | Radio signal processing and analysis |

Only assess frequencies, devices and systems within the authorised scope and applicable Australian regulatory requirements.

Do not interfere with operational radio services.

## 5. Access-control administration

Where access is provided by the client, review the relevant management platforms.

Assessment areas:

- Credential inventories.
- Access permission reports.
- Administrator roles.
- Door configuration.
- Access event logs.
- Alarm configuration.
- Visitor management.
- Audit history.

Use vendor documentation and client-provided administrative interfaces.

Do not attempt to extract credentials or manipulate production access systems outside the approved test plan.

## 6. CCTV and surveillance assessment

Review client-provided systems and documentation.

Assessment areas:

- Camera inventories.
- Camera placement.
- Recording retention.
- Video management permissions.
- Administrator accounts.
- Firmware versions.
- Remote access configuration.
- Event logging.

Use approved test footage and client-provided access.

## 7. Facility inspection equipment

Common inspection equipment includes:

- Inspection torch.
- Digital camera.
- Measuring tape.
- Laser distance meter.
- Notebook.
- Approved personal protective equipment.
- Site plans.
- Equipment inventory sheets.

Additional specialist equipment should only be used where the assessment requires it and the client has approved its use.

## 8. Standards and reference material

Useful references include:

| Resource | Relevance |
|---|---|
| AS/NZS 2201 series | Intruder alarm systems |
| AS 3745 | Planning for emergencies in facilities |
| AS 1428 series | Accessibility and access requirements |
| AS/NZS 3000 | Electrical installations |
| ISO/IEC 27001 | Information security management |
| ISO/IEC 27002 | Information security controls |
| ISO 22301 | Business continuity management |
| NIST SP 800-53 | Security and privacy controls |
| NIST SP 800-116 | PIV-based physical access control guidance |
| PSPF | Australian Government Protective Security Policy Framework |

Always confirm the current edition, applicability and licensing requirements of standards before relying on them.

## 9. Evidence handling

Useful evidence-handling practices:

- Assign unique evidence identifiers.
- Record timestamps and locations.
- Maintain an evidence register.
- Preserve original files.
- Calculate file hashes where appropriate.
- Restrict evidence access.
- Redact personal information where possible.
- Retain evidence according to the engagement agreement.

Example SHA-256 evidence hash:

```bash
sha256sum evidence-photo-001.jpg
```

PowerShell:

```powershell
Get-FileHash .\evidence-photo-001.jpg -Algorithm SHA256
```

## 10. Tool selection principles

Choose tools based on:

- Assessment objectives.
- Scope.
- Safety.
- Operational impact.
- Legal requirements.
- Compatibility.
- Evidence requirements.
- Client approval.

Do not introduce specialist equipment simply because it is available.

## Australian considerations

Physical security assessments in Australia may involve:

- State and territory surveillance legislation.
- Privacy requirements.
- Workplace health and safety obligations.
- Electrical safety requirements.
- Radiofrequency and telecommunications regulation.
- Building and fire safety requirements.
- Licensing requirements for certain security activities.

Confirm the applicable requirements for the jurisdiction and engagement.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
