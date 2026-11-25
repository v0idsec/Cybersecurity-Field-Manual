# Memory Forensics

## Overview

Memory forensics examines volatile memory (RAM) to identify activity and information that may not be available from persistent storage.

It is particularly useful when investigating:

- Fileless malware
- Process injection
- Credential theft indicators
- Suspicious processes
- Active network connections
- Malware executing only in memory
- Encryption keys
- Unusual system activity

Memory analysis is often an important part of incident response because shutting down a compromised device can destroy valuable evidence.

## What RAM Can Contain

Potential artefacts include:

- Running and terminated process information
- Loaded modules
- Network connections
- Open handles
- Command-line arguments
- Registry-related data
- Injected code
- In-memory executable content
- Kernel structures
- Cached credentials or secrets

The availability of these artefacts depends on the operating system, memory state and acquisition method.

## Memory Acquisition

Memory acquisition captures some or all of a system's physical memory.

Common tools include:

| Tool | Purpose |
|---|---|
| WinPmem | Windows memory acquisition |
| Magnet RAM Capture | Windows memory acquisition |
| DumpIt | Memory acquisition |
| AVML | Linux memory acquisition |
| LiME | Linux memory acquisition |
| Belkasoft RAM Capturer | Windows memory acquisition |

Use trusted acquisition tools and follow organisational approval requirements.

## Acquisition Considerations

Before acquisition, document:

- Device identifier
- Operating system and version
- Current power state
- Logged-in users
- Date and time
- Time zone
- Tool and version
- Acquisition destination
- Errors or warnings

Memory acquisition may alter system state and may be detected by security software.

Do not assume that a memory image is a perfect snapshot of every system structure.

## Volatility

Volatility is a memory-forensics framework used to analyse supported memory images.

The current major version uses a different command structure from older Volatility 2 examples.

Example commands:

```bash
vol -f memory.raw windows.info
```

List processes:

```bash
vol -f memory.raw windows.pslist
```

Examine process relationships:

```bash
vol -f memory.raw windows.pstree
```

List network-related artefacts:

```bash
vol -f memory.raw windows.netscan
```

List loaded modules:

```bash
vol -f memory.raw windows.modules
```

Plugin availability depends on the framework version and memory image compatibility.

## Process Analysis

Look for:

- Unexpected process names
- Suspicious parent-child relationships
- Processes executing from unusual locations
- Unexpected command-line arguments
- Unusual process privileges
- Abnormal memory regions
- Processes with suspicious network activity

Example investigation questions:

- Why did a document reader launch PowerShell?
- Why is a process running from a temporary directory?
- Is a process executing code from private memory?
- Does a process have unexpected network connections?

An unusual process is an investigative lead, not proof of compromise.

## Process Injection

Memory analysis can help identify indicators of process injection.

Potential indicators:
- Executable private memory regions
- Unusual memory permissions
- Unexpected mapped modules
- Thread start addresses outside normal module ranges
- Inconsistent process structures

Detection depends on operating system behaviour and the analysis tool.

## Network Artefacts

Memory may contain information about active or recently closed connections.

Investigate:
- Local and remote addresses
- Ports
- Process associations
- Connection state
- Known malicious infrastructure
- Related endpoint telemetry

Correlate network findings with firewall, proxy and DNS records.

## Credential Exposure

Memory may contain sensitive authentication material.

Examples include:
- Authentication tokens
- Password material
- Kerberos-related data
- Application secrets

Treat memory images as highly sensitive.

Do not extract or use credentials outside explicit investigative authority.

## Memory Image Integrity

After acquisition:

```bash
sha256sum memory.raw
```

Record:
- Hash algorithm
- Hash value
- Acquisition time
- Source device
- Acquisition tool
- Operator
- Storage location

Verify the hash before examination.

## Common Limitations

- Incomplete acquisition
- Unsupported operating system builds
- Missing symbols
- Memory corruption
- Acquisition artefacts
- Encryption
- Tool compatibility issues
- Incomplete process information

## Investigation Workflow

1. Confirm acquisition authority.
2. Assess whether live acquisition is appropriate.
3. Document system state.
4. Acquire memory.
5. Hash the resulting image.
6. Identify operating system and build.
7. Enumerate processes.
8. Examine process relationships.
9. Review network artefacts.
10. Investigate suspicious memory regions.
11. Correlate with disk and event-log evidence.
12. Document limitations and findings.

## Common Mistakes

- Shutting down a device before considering volatile evidence.
- Using incompatible memory-analysis plugins.
- Ignoring symbol requirements.
- Treating every unusual process as malicious.
- Failing to hash memory images.
- Storing memory dumps in unsecured locations.
- Extracting credentials without appropriate authority.
- Ignoring the impact of acquisition on system state.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
