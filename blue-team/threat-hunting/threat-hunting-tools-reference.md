# Threat Hunting Tools Reference

## Overview

A reference of commonly used tools for proactive threat hunting across endpoints, networks, identity infrastructure and cloud environments.

Tools should be selected based on the investigation objective, available telemetry and authorised access.

## SIEM Platforms

| Tool | Purpose |
|---|---|
| Microsoft Sentinel | Cloud SIEM and threat hunting |
| Splunk | Log analysis and correlation |
| Elastic Security | SIEM and endpoint security |
| IBM QRadar | SIEM and event analysis |
| Wazuh | Security monitoring and endpoint telemetry |

## Endpoint Investigation

| Tool | Purpose |
|---|---|
| Microsoft Defender for Endpoint | EDR and advanced hunting |
| CrowdStrike Falcon | Endpoint detection and investigation |
| SentinelOne | EDR and endpoint response |
| Velociraptor | Endpoint collection and hunting |
| osquery | SQL-based endpoint querying |
| Sysmon | Windows telemetry |
| Autoruns | Windows autostart inspection |
| Process Explorer | Windows process investigation |
| Process Monitor | Windows activity monitoring |

## Network Hunting

| Tool | Purpose |
|---|---|
| Zeek | Network security monitoring |
| Suricata | IDS and network threat detection |
| Wireshark | Packet analysis |
| tcpdump | Packet capture |
| Arkime | Network traffic investigation |
| RITA | Network traffic analysis and beacon detection |

## Linux Investigation

| Tool | Purpose |
|---|---|
| auditd | Linux audit telemetry |
| journalctl | systemd log investigation |
| ausearch | Audit event searching |
| ss | Socket investigation |
| lsof | Open file and network inspection |
| ps | Process inspection |

## Threat Intelligence

| Tool | Purpose |
|---|---|
| MITRE ATT&CK | Adversary behaviour knowledge base |
| MISP | Threat intelligence sharing |
| OpenCTI | Threat intelligence management |
| VirusTotal | File and URL intelligence |
| AbuseIPDB | IP reputation |
| URLhaus | Malicious URL intelligence |
| AlienVault OTX | Open threat intelligence |

Use external intelligence as supporting context. Validate indicators before making containment decisions.

## Adversary Emulation and Validation

| Tool | Purpose |
|---|---|
| Atomic Red Team | Focused ATT&CK-mapped tests |
| MITRE Caldera | Adversary emulation |
| Prelude Operator | Security control validation |
| Infection Monkey | Network security testing |

Use only within approved test environments and authorised scope.

## Useful Commands

### Windows Process Inspection

```powershell
Get-CimInstance Win32_Process |
    Select-Object ProcessId, ParentProcessId, Name, ExecutablePath
```

### Windows Network Connections

```powershell
Get-NetTCPConnection
```

### Windows File Hash

```powershell
Get-FileHash -Algorithm SHA256 "C:\Path\file.exe"
```

### Linux Process Inspection

```bash
ps auxf
```

### Linux Network Connections

```bash
ss -plant
```

### Linux Authentication Logs

```bash
journalctl -u ssh --since "24 hours ago"
```

### Linux File Hash

```bash
sha256sum /path/to/file
```

## Further Reading

- Velociraptor: https://docs.velociraptor.app/
- osquery: https://osquery.io/
- Zeek: https://docs.zeek.org/
- Suricata: https://docs.suricata.io/
- Wireshark: https://www.wireshark.org/docs/
- MITRE ATT&CK: https://attack.mitre.org/
- Atomic Red Team: https://github.com/redcanaryco/atomic-red-team

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
