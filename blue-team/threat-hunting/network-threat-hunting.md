# Network Threat Hunting

## Overview

Network threat hunting examines network telemetry to identify suspicious communication, lateral movement, command-and-control activity and potential data exfiltration.

Network hunting is particularly valuable when endpoint visibility is incomplete or when investigating communication across multiple systems.

## Hunting Objectives

- Identify suspicious outbound communication.
- Detect unusual internal scanning.
- Investigate unexpected remote access.
- Identify possible command-and-control activity.
- Detect unusual DNS behaviour.
- Investigate potential data exfiltration.

## Useful Data Sources

- Firewall logs
- DNS logs
- Proxy logs
- VPN logs
- NetFlow
- IPFIX
- Zeek
- Suricata
- Packet capture
- Cloud network flow logs

## DNS Hunting

Investigate:

- High-volume DNS queries
- Rare domains
- Newly registered domains
- Unusual query types
- Long or unusual subdomains
- Repeated failed lookups
- Unexpected DNS resolvers

### Example Zeek DNS Fields

Common fields include:

- `ts`
- `uid`
- `id.orig_h`
- `id.resp_h`
- `query`
- `qtype_name`
- `rcode_name`

Field availability depends on the Zeek log format and configuration.

### Splunk DNS Query Example

```spl
index=dns
| stats count dc(src_ip) AS unique_sources by query
| where count > 100
| sort - count
```

Adjust index and field names to the deployed environment.

## Outbound Connection Hunting

Look for:

- Rare destinations
- Unexpected ports
- Unusual connection frequency
- Connections from sensitive servers
- Unexpected direct-to-IP communication
- Long-lived connections
- Unusual data volumes

### Example Splunk Query

```spl
index=firewall action=allowed
| stats count sum(bytes_out) AS outbound_bytes by src_ip, dest_ip, dest_port
| sort - outbound_bytes
```

Field names and byte semantics depend on the firewall integration.

## Internal Scanning

Potential indicators:

- One source contacting many internal systems.
- Sequential port connections.
- Connections to unusual administrative ports.
- Unexpected host discovery.
- Repeated connection failures.

Distinguish authorised vulnerability scanning and asset discovery from suspicious activity.

## Lateral Movement

Investigate unusual connections involving:

- RDP
- SMB
- SSH
- WinRM
- Remote management services
- Database administration ports

Correlate network activity with authentication and endpoint process telemetry.

## Possible Command-and-Control Activity

Investigate:

- Periodic outbound connections
- Unusual DNS patterns
- Rare destinations
- Unexpected encrypted communication
- Connections from unusual processes
- Unusual beacon-like timing

No single characteristic confirms command-and-control activity.

## Possible Data Exfiltration

Look for:

- Large outbound transfers
- Unusual upload destinations
- Unexpected cloud storage access
- Unusual transfer times
- Abnormal activity from sensitive systems
- Unusual archive or compression activity

Correlate network data with user, application and endpoint activity.

## Zeek

Zeek provides detailed network security monitoring.

Useful logs include:

| Log | Purpose |
|---|---|
| `conn.log` | Network connections |
| `dns.log` | DNS queries |
| `http.log` | HTTP activity |
| `ssl.log` | TLS connection metadata |
| `files.log` | Observed file transfers |
| `notice.log` | Zeek notices |
| `ssh.log` | SSH activity |

Official documentation:

https://docs.zeek.org/

## Suricata

Suricata provides network threat detection through signatures and protocol analysis.

Useful outputs include:

- Alert events
- DNS events
- HTTP events
- TLS events
- Flow records
- File information

Official documentation:

https://docs.suricata.io/

## Investigation Workflow

1. Identify the suspicious source or destination.
2. Establish the timeframe.
3. Review connection frequency.
4. Examine DNS and proxy activity.
5. Identify associated processes where possible.
6. Correlate authentication events.
7. Assess destination reputation.
8. Identify affected systems.
9. Preserve relevant network evidence.
10. Document conclusions.

## Limitations

- Encryption limits payload visibility.
- NAT can complicate attribution.
- Proxies can obscure original source addresses.
- Incomplete flow records may hide activity.
- Shared infrastructure can produce misleading indicators.
- Network activity requires endpoint and identity context.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
