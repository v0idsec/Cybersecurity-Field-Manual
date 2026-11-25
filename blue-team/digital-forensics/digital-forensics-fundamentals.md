# Digital Forensics Fundamentals

## Overview

Digital forensics involves the systematic collection, preservation, examination and interpretation of digital information.

The objective is to produce reliable findings that can support incident response, internal investigations, legal proceedings, compliance activities and security improvements.

Digital evidence can originate from:

- Workstations and laptops
- Servers and virtual machines
- Mobile devices
- Network infrastructure
- Cloud platforms
- Email systems
- Web browsers
- Removable storage
- Applications and databases
- Identity and authentication systems

## Core Principles

### Preservation

Protect evidence from accidental or intentional modification.

Whenever practical:
- Preserve original devices and storage media.
- Work from verified forensic copies.
- Use write-blocking hardware or software where appropriate.
- Record every interaction with the evidence.
- Restrict access to authorised personnel.

### Integrity

Evidence integrity means being able to demonstrate that collected data has remained unchanged.

Common cryptographic hashing algorithms include:

- SHA-256
- SHA-512

Example:

```bash
sha256sum evidence.img
```

PowerShell:

```powershell
Get-FileHash .\evidence.img -Algorithm SHA256
```

Record hashes at acquisition and verify them before and after examination where appropriate.

### Repeatability

Another investigator should be able to understand the process and reproduce the examination using the documented methodology and available evidence.

Document:
- Tool names and versions
- Commands and parameters
- Acquisition methods
- Examination steps
- Time settings
- Relevant configuration
- Limitations and errors

### Documentation

Record investigative activities as they occur.

Avoid relying on memory or reconstructing an investigation after the fact.

## Types of Digital Evidence

| Evidence type | Examples |
|---|---|
| Volatile | RAM, running processes, active connections |
| Non-volatile | Disk images, files, registry hives |
| Network | PCAP files, firewall logs, DNS records |
| Application | Database records, application logs |
| Identity | Authentication logs, token activity |
| Cloud | Audit events, object access logs |
| Communication | Email, chat records, message metadata |

## Volatile and Non-Volatile Evidence

Volatile evidence can disappear when a system shuts down or changes state.

Examples:
- Running processes
- Active network connections
- Logged-in sessions
- In-memory malware
- Encryption keys held in memory
- Temporary execution state

Non-volatile evidence generally persists after shutdown.

Examples:
- Disk contents
- Event logs
- Registry data
- Browser history
- Stored application data

Collection priorities depend on the investigation, system state, operational risk and authorisation.

## Order of Volatility

A commonly used conceptual order is:

1. CPU registers and cache
2. RAM
3. Active network connections and routing state
4. Running processes and system state
5. Temporary file systems
6. Persistent storage
7. Remote logs and external records

This is a planning aid, not a universal mandatory collection sequence. Remote logs may expire quickly, and operational circumstances may change priorities.

## Evidence Artefacts

Common forensic artefacts include:

- File creation, modification and access timestamps
- File-system metadata
- Operating system event logs
- Registry keys
- Shell history
- Process execution records
- Browser databases
- Authentication events
- Scheduled tasks
- Services and startup entries
- DNS cache and network records

An artefact rarely proves an entire incident by itself. Correlate multiple independent sources wherever possible.

## Timestamp Considerations

Record:
- Original timestamp
- Original time zone
- Normalised UTC timestamp
- Source system clock
- Known clock drift
- Timestamp interpretation method

Be aware of:
- UTC versus local time
- Daylight saving changes
- Unix epoch timestamps
- File-system timestamp precision
- Clock synchronisation failures
- Different timestamp semantics across file systems

Do not assume every timestamp represents the moment an action occurred.

## Forensic Soundness

A forensic process should minimise changes to evidence and document unavoidable changes.

Consider:
- Whether the device was powered on
- Whether full-disk encryption was active
- Whether the system was connected to a network
- Whether collection required executing software
- Whether the acquisition process changed metadata
- Whether the evidence source was complete

## Common Mistakes

- Examining original evidence unnecessarily.
- Failing to record hashes.
- Ignoring time-zone differences.
- Treating timestamps as definitive proof.
- Failing to document tool versions.
- Overwriting evidence during acquisition.
- Collecting more personal information than necessary.
- Making conclusions unsupported by the artefacts.
- Failing to document unsuccessful collection attempts.

## Practical Checklist

- [ ] Confirm investigation authority.
- [ ] Define scope and objectives.
- [ ] Identify relevant evidence sources.
- [ ] Assess volatility.
- [ ] Document system state.
- [ ] Acquire evidence using an appropriate method.
- [ ] Calculate and record hashes.
- [ ] Maintain chain of custody.
- [ ] Analyse verified copies where practical.
- [ ] Document findings and limitations.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
