# Packet Analysis Cheatsheet

Quick-reference material for capturing and analysing network traffic with Wireshark and tcpdump.

## What is packet analysis?

Packet analysis examines network traffic to understand communication between systems.

Common uses:

- Troubleshooting.
- Incident response.
- Protocol analysis.
- Malware investigation.
- Network performance analysis.
- Security monitoring.

## Wireshark

Wireshark is a graphical network protocol analyser.

Common capture interfaces:

- Ethernet.
- Wi-Fi.
- VPN adapters.
- Loopback interfaces.

## Wireshark display filters

| Filter | Purpose |
|---|---|
| `ip.addr == 192.0.2.10` | Traffic involving an IP |
| `ip.src == 192.0.2.10` | Source IP |
| `ip.dst == 192.0.2.10` | Destination IP |
| `tcp` | TCP traffic |
| `udp` | UDP traffic |
| `icmp` | ICMP traffic |
| `dns` | DNS traffic |
| `http` | HTTP traffic |
| `tls` | TLS traffic |
| `tcp.port == 443` | TCP port 443 |
| `udp.port == 53` | UDP port 53 |
| `tcp.flags.syn == 1` | TCP SYN packets |
| `tcp.flags.reset == 1` | TCP reset packets |
| `tcp.analysis.retransmission` | TCP retransmissions |
| `tcp.analysis.duplicate_ack` | Duplicate ACKs |
| `tcp.stream eq 0` | Specific TCP stream |

## Combine filters

AND:

```text
ip.addr == 192.0.2.10 && tcp.port == 443
```

OR:

```text
dns || http
```

NOT:

```text
!arp
```

Filter by subnet:

```text
ip.addr == 192.168.1.0/24
```

## tcpdump

List available interfaces:

```bash
tcpdump -D
```

Capture traffic:

```bash
sudo tcpdump -i eth0
```

Capture a host:

```bash
sudo tcpdump -i eth0 host 192.0.2.10
```

Capture a source or destination:

```bash
sudo tcpdump -i eth0 src host 192.0.2.10
sudo tcpdump -i eth0 dst host 192.0.2.10
```

Capture a port:

```bash
sudo tcpdump -i eth0 port 443
```

Capture DNS:

```bash
sudo tcpdump -i eth0 port 53
```

Capture TCP traffic:

```bash
sudo tcpdump -i eth0 tcp
```

Save a capture:

```bash
sudo tcpdump -i eth0 -w capture.pcap
```

Read a capture:

```bash
tcpdump -r capture.pcap
```

Show packet contents in ASCII:

```bash
sudo tcpdump -A -i eth0
```

Show packet contents in hexadecimal and ASCII:

```bash
sudo tcpdump -X -i eth0
```

Limit packet count:

```bash
sudo tcpdump -i eth0 -c 100
```

## Useful tcpdump filters

Host and port:

```bash
sudo tcpdump -i eth0 host 192.0.2.10 and port 443
```

Exclude a host:

```bash
sudo tcpdump -i eth0 not host 192.0.2.10
```

TCP SYN packets:

```bash
sudo tcpdump -i eth0 'tcp[tcpflags] & tcp-syn != 0'
```

DNS requests:

```bash
sudo tcpdump -i eth0 'udp port 53'
```

## Common protocol indicators

| Traffic | What to inspect |
|---|---|
| DNS | Query names, response codes, unusual volumes |
| HTTP | Methods, headers, response codes |
| TLS | Handshake, certificates, SNI where visible |
| TCP | Handshake, resets, retransmissions |
| ICMP | Echo requests, replies, error messages |
| DHCP | Discover, Offer, Request, Acknowledge |
| ARP | IP-to-MAC resolution and unexpected replies |
| SMB | File sharing and authentication activity |

## Common TCP indicators

| Indicator | Possible meaning |
|---|---|
| SYN without response | Filtering, unavailable host or packet loss |
| RST | Connection rejected or reset |
| Retransmission | Packet loss or network congestion |
| Duplicate ACK | Possible packet loss or reordering |
| Zero window | Receiver cannot currently accept more data |
| FIN | Graceful connection close |

These indicators require context; they are not automatically evidence of malicious activity.

## Follow TCP streams

In Wireshark:

1. Select a TCP packet.
2. Right-click the packet.
3. Select **Follow**.
4. Select **TCP Stream**.

This reconstructs the conversation where possible.

## Capture filters vs display filters

| Type | Applied when | Purpose |
|---|---|---|
| Capture filter | During capture | Controls which packets are collected |
| Display filter | After capture | Controls which packets are displayed |

Example capture filter:

```text
host 192.0.2.10 and port 443
```

Example display filter:

```text
ip.addr == 192.0.2.10 && tcp.port == 443
```

The syntax is different.

## Security considerations

- Packet captures may contain credentials, session tokens and personal information.
- Use approved capture locations and interfaces.
- Restrict access to PCAP files.
- Apply retention requirements.
- Avoid capturing unnecessary traffic.
- Encrypted traffic may limit payload visibility.
- TLS decryption requires appropriate authorised key material or session secrets.

---

*Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
