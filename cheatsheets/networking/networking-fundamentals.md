# Networking Fundamentals

A quick reference to core networking concepts, protocols and services.

## OSI model

| Layer | Name | Examples |
|---:|---|---|
| 7 | Application | HTTP, DNS, SMTP |
| 6 | Presentation | TLS, encoding, encryption |
| 5 | Session | Session management |
| 4 | Transport | TCP, UDP |
| 3 | Network | IPv4, IPv6, ICMP, routing |
| 2 | Data Link | Ethernet, MAC, VLAN |
| 1 | Physical | Cables, fibre, radio |

## TCP/IP model

| Layer | Examples |
|---|---|
| Application | HTTP, DNS, SSH, SMTP |
| Transport | TCP, UDP |
| Internet | IPv4, IPv6, ICMP |
| Network Access | Ethernet, Wi-Fi |

## TCP vs UDP

| Feature | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented | Connectionless |
| Reliability | Reliable delivery | No delivery guarantee |
| Ordering | Maintains order | No ordering guarantee |
| Handshake | Three-way handshake | No handshake |
| Overhead | Higher | Lower |
| Common uses | HTTP(S), SSH, SMTP | DNS, VoIP, streaming |

## TCP three-way handshake

1. Client sends SYN.
2. Server responds with SYN-ACK.
3. Client responds with ACK.

```text
Client                 Server
  |                       |
  |-------- SYN --------->|
  |<----- SYN-ACK --------|
  |-------- ACK --------->|
  |                       |
  |    Connection open    |
```

## Common ports

| Port | Protocol | Service |
|---:|---|---|
| 20/21 | TCP | FTP |
| 22 | TCP | SSH |
| 23 | TCP | Telnet |
| 25 | TCP | SMTP |
| 53 | TCP/UDP | DNS |
| 67/68 | UDP | DHCP |
| 69 | UDP | TFTP |
| 80 | TCP | HTTP |
| 88 | TCP/UDP | Kerberos |
| 110 | TCP | POP3 |
| 123 | UDP | NTP |
| 135 | TCP | MS RPC endpoint mapper |
| 137–139 | TCP/UDP | NetBIOS |
| 143 | TCP | IMAP |
| 161/162 | UDP | SNMP |
| 389 | TCP/UDP | LDAP |
| 443 | TCP | HTTPS |
| 445 | TCP | SMB |
| 465 | TCP | SMTPS |
| 514 | UDP | Syslog |
| 587 | TCP | SMTP submission |
| 636 | TCP | LDAPS |
| 993 | TCP | IMAPS |
| 995 | TCP | POP3S |
| 1433 | TCP | Microsoft SQL Server |
| 1521 | TCP | Oracle Database |
| 3306 | TCP | MySQL |
| 3389 | TCP | RDP |
| 5432 | TCP | PostgreSQL |
| 5900 | TCP | VNC |
| 5985 | TCP | WinRM HTTP |
| 5986 | TCP | WinRM HTTPS |
| 8080 | TCP | Common alternate HTTP |
| 8443 | TCP | Common alternate HTTPS |

Ports are conventional defaults, not guarantees of the service running on them.

## Important protocols

| Protocol | Purpose |
|---|---|
| ARP | IPv4 address-to-MAC resolution |
| ICMP | Network diagnostics and error reporting |
| DHCP | Automatic IP configuration |
| DNS | Name resolution |
| HTTP | Web communication |
| HTTPS | HTTP over TLS |
| SSH | Secure remote administration |
| SMB | Windows file and printer sharing |
| LDAP | Directory access |
| Kerberos | Network authentication |
| SNMP | Network device monitoring |
| NTP | Time synchronisation |
| TLS | Transport encryption |

## Private IPv4 ranges

| Range | CIDR |
|---|---|
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 |

## Special IPv4 addresses

| Range / Address | Purpose |
|---|---|
| 127.0.0.0/8 | Loopback |
| 169.254.0.0/16 | Link-local |
| 0.0.0.0 | Unspecified / all interfaces in some contexts |
| 255.255.255.255 | Limited broadcast |
| 100.64.0.0/10 | Shared address space / CGNAT |

## IPv6 basics

| Address | Purpose |
|---|---|
| `::1` | Loopback |
| `::` | Unspecified |
| `fe80::/10` | Link-local |
| `fc00::/7` | Unique local |
| `2000::/3` | Global unicast |
| `ff00::/8` | Multicast |

IPv6 does not use broadcast addresses.

## Useful commands

Linux:

```bash
ip addr
ip route
ip neigh
ss -tulnp
```

Windows:

```cmd
ipconfig /all
route print
arp -a
netstat -ano
```

Connectivity:

```bash
ping 192.0.2.10
traceroute example.com
```

Windows:

```cmd
ping 192.0.2.10
tracert example.com
```

## Security considerations

- Disable unnecessary services.
- Avoid insecure protocols such as Telnet and FTP where secure alternatives exist.
- Restrict management interfaces.
- Segment sensitive networks.
- Monitor unexpected listening services.
- Use encryption for sensitive traffic.
- Review exposed ports and firewall rules.

---

*Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
