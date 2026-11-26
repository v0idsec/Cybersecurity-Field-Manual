# Routing & Switching Cheatsheet

Quick-reference commands and concepts for network routing, switching, VLANs and traffic forwarding.

## Routing fundamentals

Routing determines how traffic moves between IP networks.

A router forwards packets based on its routing table.

Important terms:

| Term | Description |
|---|---|
| Default gateway | Router used when no more specific route matches |
| Routing table | List of known network routes |
| Next hop | Next router or destination for a packet |
| Static route | Manually configured route |
| Dynamic routing | Routes learned through routing protocols |
| Metric | Value used to compare routes |
| Longest prefix match | Most specific matching route is preferred |

## Common routing protocols

| Protocol | Purpose |
|---|---|
| RIP | Distance-vector routing |
| OSPF | Link-state routing |
| EIGRP | Advanced distance-vector routing |
| BGP | Inter-domain routing |
| IS-IS | Link-state routing |

## Linux routing commands

Display routes:

```bash
ip route
```

Display IPv6 routes:

```bash
ip -6 route
```

Show route to a destination:

```bash
ip route get 192.0.2.10
```

Add a route:

```bash
sudo ip route add 10.10.0.0/16 via 192.168.1.1
```

Delete a route:

```bash
sudo ip route del 10.10.0.0/16
```

## Windows routing commands

Display routes:

```cmd
route print
```

Add a route:

```cmd
route add 10.10.0.0 mask 255.255.0.0 192.168.1.1
```

Delete a route:

```cmd
route delete 10.10.0.0
```

PowerShell:

```powershell
Get-NetRoute
```

## Switching fundamentals

A switch forwards Ethernet frames based on MAC addresses.

Important concepts:

- MAC address table.
- VLANs.
- Trunk ports.
- Access ports.
- Spanning Tree Protocol.
- Link aggregation.
- Port security.

## VLANs

A Virtual LAN separates a switched network into logical broadcast domains.

Example:

| VLAN | Purpose | Example subnet |
|---:|---|---|
| 10 | Management | 192.168.10.0/24 |
| 20 | Workstations | 192.168.20.0/24 |
| 30 | Servers | 192.168.30.0/24 |
| 40 | Guest Wi-Fi | 192.168.40.0/24 |
| 50 | VoIP | 192.168.50.0/24 |

VLANs alone do not provide complete security isolation. Inter-VLAN routing and firewall policy must also be considered.

## Access vs trunk ports

| Feature | Access port | Trunk port |
|---|---|---|
| VLAN membership | Usually one VLAN | Multiple VLANs |
| Common use | End devices | Switch-to-switch links |
| Tagging | Typically untagged | Typically 802.1Q tagged |
| Configuration | Access VLAN | Allowed VLAN list and native VLAN |

## Spanning Tree Protocol

STP prevents Layer 2 switching loops.

Common variants include:

- STP.
- RSTP.
- MSTP.
- Rapid PVST+.

Security controls may include:

- BPDU Guard.
- Root Guard.
- Loop Guard.
- PortFast or equivalent edge-port configuration.

## Cisco IOS reference

These examples use Cisco IOS-style syntax. Commands vary by platform and software release.

Display interfaces:

```text
show interfaces status
```

Display VLANs:

```text
show vlan brief
```

Display trunk ports:

```text
show interfaces trunk
```

Display MAC address table:

```text
show mac address-table
```

Display routes:

```text
show ip route
```

Display spanning tree:

```text
show spanning-tree
```

Display running configuration:

```text
show running-config
```

## Troubleshooting network paths

Check:

1. Local interface status.
2. VLAN assignment.
3. IP configuration.
4. Default gateway.
5. Routing table.
6. Inter-VLAN routing.
7. Firewall rules.
8. Destination service availability.

Useful commands:

```bash
ip route get 192.0.2.10
traceroute 192.0.2.10
```

Windows:

```cmd
route print
tracert 192.0.2.10
```

## Security review checklist

- [ ] Review VLAN segmentation.
- [ ] Restrict trunk allowed VLANs.
- [ ] Disable unused switch ports.
- [ ] Review management VLAN access.
- [ ] Secure switch administration.
- [ ] Review STP protections.
- [ ] Check for unexpected MAC addresses.
- [ ] Review routing configuration.
- [ ] Restrict inter-VLAN traffic.
- [ ] Monitor routing changes.

---

*Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
