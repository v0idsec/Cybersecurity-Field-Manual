# Incident Response Tool Reference

## Overview

This document lists common tools used during incident response.

Tool selection should reflect the environment, incident type, available telemetry, organisational policy and evidence requirements.

A tool's output is not automatically conclusive. Validate findings against other sources where possible.

## Endpoint investigation

| Tool | Purpose |
|---|---|
| Microsoft Defender for Endpoint | Endpoint detection, investigation and response |
| Velociraptor | Endpoint collection, hunting and forensic investigation |
| KAPE | Targeted forensic artefact collection |
| Eric Zimmerman's tools | Windows artefact parsing |
| Sysinternals Suite | Windows process, service and system investigation |
| osquery | SQL-based endpoint visibility and investigation |
| GRR Rapid Response | Remote endpoint collection and investigation |
| Autopsy | Digital forensic analysis |
| Volatility 3 | Memory forensic analysis |

## Network investigation

| Tool | Purpose |
|---|---|
| Wireshark | Packet capture analysis |
| Zeek | Network security monitoring and protocol metadata |
| Suricata | Network intrusion detection and prevention |
| Arkime | Large-scale packet capture indexing and investigation |
| tcpdump | Command-line packet capture |
| NetworkMiner | Network forensic analysis |
| RITA | Network traffic analysis and beacon detection |

## Log analysis and SIEM

| Tool | Purpose |
|---|---|
| Microsoft Sentinel | Cloud SIEM and security analytics |
| Splunk Enterprise Security | SIEM and security investigation |
| Elastic Security | SIEM, endpoint and security analytics |
| Wazuh | Security monitoring and endpoint detection |
| Graylog | Centralised log management |
| Sigma | Generic detection rule format |
| Hayabusa | Windows event log threat hunting and analysis |
| Chainsaw | Windows event log analysis |

## Identity and cloud

| Tool | Purpose |
|---|---|
| Microsoft Entra audit and sign-in logs | Identity investigation |
| Microsoft Defender XDR | Cross-domain security investigation |
| AWS CloudTrail | AWS API activity investigation |
| AWS GuardDuty | AWS threat detection |
| Microsoft Defender for Cloud | Cloud security posture and threat detection |
| Google Cloud Audit Logs | Google Cloud activity investigation |
| Cloud provider native consoles | Resource, identity and audit investigation |

## Malware and file analysis

| Tool | Purpose |
|---|---|
| YARA | Pattern-based malware identification |
| capa | Capability identification from executable files |
| Ghidra | Reverse engineering |
| Detect It Easy | File format and packer identification |
| FLOSS | Extraction of obfuscated strings |
| CyberChef | Data transformation and analysis |
| ClamAV | Malware scanning |
| REMnux | Malware analysis environment |

## Evidence and forensic handling

| Tool | Purpose |
|---|---|
| SHA256 utilities | File integrity verification |
| FTK Imager | Disk image acquisition and examination |
| Guymager | Disk imaging |
| Autopsy | Forensic examination |
| Volatility 3 | Memory analysis |
| Plaso / log2timeline | Timeline creation |
| Timesketch | Collaborative timeline analysis |

## Useful command references

### Windows process inspection

```powershell
Get-Process |
    Sort-Object CPU -Descending |
    Select-Object -First 20
```

### Windows services

```powershell
Get-CimInstance Win32_Service |
    Select-Object Name, State, StartMode, StartName
```

### Windows network connections

```powershell
Get-NetTCPConnection |
    Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

### Windows logged-on sessions

```cmd
quser
```

### Windows event log export

```powershell
wevtutil epl Security C:\Evidence\Security.evtx
```

Export logs only to an approved evidence location and follow evidence handling procedures.

### Linux active processes

```bash
ps auxf
```

### Linux network connections

```bash
ss -tulpn
```

### Linux logged-in users

```bash
who
w
```

### Linux authentication logs

Common locations vary by distribution:

```bash
sudo journalctl -u ssh
sudo journalctl --since "24 hours ago"
```

### File hash

```bash
sha256sum suspicious-file
```

PowerShell:

```powershell
Get-FileHash .\suspicious-file -Algorithm SHA256
```

## Tool selection considerations

Before using a tool, consider:

- Is it approved for use in the environment?
- Could it modify evidence?
- Does it require elevated privileges?
- Does it transmit data externally?
- Does it collect personal or sensitive information?
- Is its output reproducible?
- Is the tool version recorded?
- Can the results be independently validated?

## Further reading

- [Velociraptor](https://docs.velociraptor.app/)
- [KAPE](https://ericzimmerman.github.io/)
- [Volatility Foundation](https://volatilityfoundation.org/)
- [Sysinternals](https://learn.microsoft.com/sysinternals/)
- [Sigma](https://sigmahq.io/)
- [Wireshark](https://www.wireshark.org/docs/)
- [Zeek](https://docs.zeek.org/)
- [Suricata](https://docs.suricata.io/)

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
