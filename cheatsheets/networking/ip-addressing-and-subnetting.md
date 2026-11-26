# IP Addressing & Subnetting

Quick-reference material for IPv4, IPv6, subnet masks and CIDR calculations.

## IPv4 addressing

IPv4 addresses are 32-bit addresses, normally represented as four decimal octets.

Example:

```text
192.168.1.10
```

Each octet ranges from 0 to 255.

## CIDR notation

CIDR represents the number of network bits in an IP address.

Example:

```text
192.168.1.0/24
```

The `/24` means 24 bits are used for the network portion.

## Common subnet masks

| CIDR | Subnet mask | Total addresses | Traditional usable hosts |
|---:|---|---:|---:|
| /8 | 255.0.0.0 | 16,777,216 | 16,777,214 |
| /16 | 255.255.0.0 | 65,536 | 65,534 |
| /20 | 255.255.240.0 | 4,096 | 4,094 |
| /21 | 255.255.248.0 | 2,048 | 2,046 |
| /22 | 255.255.252.0 | 1,024 | 1,022 |
| /23 | 255.255.254.0 | 512 | 510 |
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |
| /29 | 255.255.255.248 | 8 | 6 |
| /30 | 255.255.255.252 | 4 | 2 |
| /31 | 255.255.255.254 | 2 | Point-to-point use |
| /32 | 255.255.255.255 | 1 | Single address |

Traditional usable-host counts exclude the network and broadcast addresses. `/31` has a special point-to-point use defined by RFC 3021.

## Private IPv4 ranges

| Network | CIDR |
|---|---|
| 10.0.0.0/8 | Class A private range |
| 172.16.0.0/12 | Class B private range |
| 192.168.0.0/16 | Class C private range |

## Subnet calculation example

Given:

```text
192.168.10.45/24
```

The subnet is:

| Property | Value |
|---|---|
| Network | 192.168.10.0 |
| Subnet mask | 255.255.255.0 |
| First traditional host | 192.168.10.1 |
| Last traditional host | 192.168.10.254 |
| Broadcast | 192.168.10.255 |
| Total addresses | 256 |
| Traditional usable hosts | 254 |

## Subnet block sizes

For common subnet masks, calculate the block size using:

```text
256 - subnet mask octet
```

Example:

```text
255.255.255.192
```

```text
256 - 192 = 64
```

The subnet boundaries are:

```text
192.168.1.0
192.168.1.64
192.168.1.128
192.168.1.192
```

## Useful subnetting tools

Linux:

```bash
ipcalc 192.168.1.10/24
```

Python:

```python
import ipaddress

network = ipaddress.ip_network("192.168.1.0/24")

print("Network:", network.network_address)
print("Broadcast:", network.broadcast_address)
print("Netmask:", network.netmask)
print("Hosts:", network.num_addresses)
```

Python host iteration:

```python
for host in network.hosts():
    print(host)
```

## IPv6 basics

IPv6 addresses are 128 bits long.

Example:

```text
2001:db8:1234:1::10
```

Common ranges:

| Range | Purpose |
|---|---|
| `::1/128` | Loopback |
| `::/128` | Unspecified |
| `fe80::/10` | Link-local |
| `fc00::/7` | Unique local |
| `2000::/3` | Global unicast |
| `ff00::/8` | Multicast |
| `2001:db8::/32` | Documentation examples |

## IPv6 shorthand

These addresses are equivalent:

```text
2001:0db8:0000:0000:0000:0000:0000:0001
```

```text
2001:db8::1
```

Leading zeroes in each group may be removed, and consecutive zero groups may be compressed once using `::`.

## IPv6 commands

Linux:

```bash
ip -6 addr
ip -6 route
```

Windows:

```cmd
ipconfig
netsh interface ipv6 show address
netsh interface ipv6 show route
```

## Important notes

- Do not assume private IPv4 means trusted.
- IPv6 may be enabled even where the network primarily uses IPv4.
- Traditional IPv4 broadcast calculations do not apply to IPv6.
- Cloud and VPN networks may use overlapping address spaces.
- Validate routing and subnet boundaries before scanning or changing network configuration.

---

*Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
