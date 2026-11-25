# Network Forensics

## Overview

Network forensics examines network traffic and related telemetry to reconstruct communications, identify suspicious activity and investigate security incidents.

Evidence sources include:

- Packet captures
- Firewall logs
- DNS logs
- Proxy logs
- NetFlow and IPFIX
- VPN records
- IDS/IPS alerts
- Network access control logs
- Cloud network flow logs

## Packet Capture

A packet capture (PCAP) records network packets observed at a collection point.

Common capture formats:
- PCAP
- PCAPNG

A capture may contain:
- Source and destination IP addresses
- Ports
- Protocols
- DNS requests
- HTTP metadata
- TLS handshake metadata
- Application-layer content where visible

Encrypted traffic limits the visibility of application content.

## Wireshark

Wireshark is a graphical packet-analysis tool.

Useful display filters:

```text
dns
```

```text
http
```

```text
tls
```

```text
tcp.flags.syn == 1 && tcp.flags.ack == 0
```

Filter traffic involving an IP:

```text
ip.addr == 192.0.2.10
```

Filter a specific destination port:

```text
tcp.dstport == 443
```

Display filters do not alter the original PCAP.

## TShark

TShark provides command-line packet analysis.

Read a capture:

```bash
tshark -r capture.pcapng
```

Display DNS packets:

```bash
tshark -r capture.pcapng -Y dns
```

Extract selected fields:

```bash
tshark -r capture.pcapng \
  -T fields \
  -e frame.time \
  -e ip.src \
  -e ip.dst \
  -e dns.qry.name
```

## DNS Forensics

DNS records can help identify:
- Malware command-and-control lookups
- Suspicious newly observed domains
- DNS tunnelling indicators
- Domain generation activity
- Unusual query volumes
- Unexpected external services

Investigate:
- Query name
- Query type
- Client address
- Response code
- Returned records
- Resolver
- Timestamp

DNS activity alone does not prove a successful connection.

## Firewall Logs

Firewall records may provide:
- Source and destination addresses
- Ports
- Protocol
- Action
- Rule identifier
- Interface
- Timestamp
- Connection state

Investigate unusual outbound connections and unexpected inbound access.

## Proxy Logs

Proxy records can provide:
- Requested URL
- User identity
- Client IP
- HTTP method
- Response status
- User agent
- Destination domain
- Bytes transferred

Consider privacy and retention requirements when collecting web activity.

## NetFlow and IPFIX

Flow telemetry provides metadata about network conversations rather than full packet contents.

Common fields:
- Source and destination addresses
- Source and destination ports
- Protocol
- Packet count
- Byte count
- Flow duration
- Interface

Flow records are useful for identifying traffic patterns and potential data movement.

## TLS Analysis

Encrypted traffic can still expose some metadata depending on protocol and configuration.

Potential indicators:
- Destination IP
- Port
- Certificate information
- TLS version
- Handshake characteristics
- SNI where visible
- Connection timing and volume

Encrypted Client Hello and other privacy technologies can reduce visible metadata.

Do not assume TLS traffic is harmless simply because the payload is encrypted.

## Investigating Data Exfiltration

Potential indicators:
- Large outbound transfers
- Unusual destinations
- Repeated uploads
- Unexpected cloud storage access
- Unusual transfer timing
- Abnormal DNS activity
- Long-lived outbound connections

Correlate network evidence with:
- Endpoint file access
- User activity
- Cloud audit logs
- DLP events
- Proxy records

## Example: Extract HTTP Requests

```bash
tshark -r capture.pcapng \
  -Y http.request \
  -T fields \
  -e frame.time \
  -e ip.src \
  -e http.host \
  -e http.request.uri
```

## Evidence Integrity

Hash packet captures:

```bash
sha256sum capture.pcapng
```

Record:
- Capture point
- Interface
- Capture filter
- Start and end times
- Time zone
- Capture tool and version
- Packet drops
- File hash

## Investigation Workflow

1. Identify relevant network evidence sources.
2. Preserve original captures and logs.
3. Record collection metadata.
4. Verify integrity.
5. Establish the relevant time range.
6. Identify key hosts and identities.
7. Review DNS and connection activity.
8. Examine suspicious sessions.
9. Investigate unusual data volumes.
10. Correlate with endpoint and cloud evidence.
11. Document limitations and findings.

## Common Mistakes

- Assuming a PCAP contains all traffic.
- Ignoring packet loss.
- Failing to document capture filters.
- Treating DNS lookups as successful connections.
- Assuming encrypted traffic is benign.
- Ignoring NAT and proxy infrastructure.
- Failing to account for clock drift.
- Drawing conclusions from flow metadata alone.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
