# Network Troubleshooting Cheatsheet

A practical diagnostic reference for identifying and resolving common network problems.

## Troubleshooting methodology

Use a consistent process:

1. Identify the affected user, device or service.
2. Determine the scope of the issue.
3. Check physical and wireless connectivity.
4. Inspect IP configuration.
5. Verify local network reachability.
6. Verify gateway and routing.
7. Test DNS.
8. Test the destination service.
9. Inspect firewall and security controls.
10. Review logs and packet captures.
11. Record findings and confirm resolution.

## Layer-by-layer troubleshooting

| Layer | What to check |
|---|---|
| Physical | Cable, link lights, Wi-Fi signal, adapter state |
| Data Link | VLAN, MAC address, ARP, switching |
| Network | IP address, subnet, gateway, routing |
| Transport | TCP/UDP ports, connection state, firewall |
| Application | DNS, HTTP, TLS, service availability |

## Basic connectivity tests

Ping loopback:

```bash
ping 127.0.0.1
```

Ping local gateway:

```bash
ping 192.168.1.1
```

Ping a known external IP:

```bash
ping 1.1.1.1
```

Test DNS:

```bash
dig example.com
```

Test HTTPS:

```bash
curl -I https://example.com
```

Windows:

```cmd
ping 127.0.0.1
ping 192.168.1.1
ping 1.1.1.1
nslookup example.com
```

## Route diagnostics

Linux:

```bash
ip route
traceroute example.com
```

Windows:

```cmd
route print
tracert example.com
pathping example.com
```

A missing response from an intermediate hop does not necessarily indicate a routing failure. Routers may filter or deprioritise diagnostic traffic.

## Port testing

Linux:

```bash
nc -vz 192.0.2.10 443
```

Windows:

```powershell
Test-NetConnection 192.0.2.10 -Port 443
```

Check listening services on Linux:

```bash
sudo ss -tulnp
```

Check listening services on Windows:

```cmd
netstat -ano | findstr LISTENING
```

## DNS troubleshooting

Check configured DNS servers:

Linux:

```bash
cat /etc/resolv.conf
```

Windows:

```cmd
ipconfig /all
```

Query a specific server:

```bash
dig @192.0.2.53 example.com
```

Windows:

```powershell
Resolve-DnsName example.com -Server 192.0.2.53
```

## Common symptoms

| Symptom | Possible cause |
|---|---|
| No network connection | Adapter, cable, Wi-Fi or switch issue |
| 169.254.x.x address | DHCP failure |
| Can ping IP but not hostname | DNS issue |
| Can access LAN but not internet | Gateway, routing or upstream issue |
| Can resolve DNS but cannot connect | Firewall, routing or service issue |
| Connection refused | Destination reachable but service not accepting connection |
| Connection timeout | Filtering, routing or unavailable host |
| Intermittent packet loss | Congestion, wireless interference or physical issue |
| Slow file transfers | Throughput, latency, duplex or storage issue |
| VPN connected but no access | DNS, routes or access policy |

## Packet loss and latency

Ping statistics:

```bash
ping -c 20 192.0.2.10
```

Continuous monitoring:

```bash
ping 192.0.2.10
```

Route and latency monitoring:

```bash
mtr example.com
```

Windows:

```cmd
pathping example.com
```

## Check local network state

Linux:

```bash
ip -br addr
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

## Check firewall configuration

Linux:

```bash
sudo ufw status verbose
sudo nft list ruleset
```

Windows:

```powershell
Get-NetFirewallProfile
Get-NetFirewallRule -Enabled True
```

## Evidence collection

When troubleshooting, record:

- Date and time.
- Affected device and user.
- Source and destination IP addresses.
- Hostnames.
- Relevant ports and protocols.
- DNS server.
- Default gateway.
- Error messages.
- Test results.
- Recent network or configuration changes.
- Packet capture or logs where appropriate.

## Escalation checklist

Before escalating:

- [ ] Confirm the issue is reproducible.
- [ ] Identify whether one or multiple devices are affected.
- [ ] Record IP configuration.
- [ ] Test gateway reachability.
- [ ] Test DNS resolution.
- [ ] Test the destination port.
- [ ] Check firewall and VPN state.
- [ ] Capture relevant error messages.
- [ ] Document actions already taken.

## Important notes

- ICMP may be blocked even when a service is reachable.
- DNS failures can appear as application failures.
- A successful ping does not prove that a TCP service is available.
- Avoid changing multiple variables simultaneously.
- Preserve evidence when troubleshooting a suspected security incident.

---

*Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
