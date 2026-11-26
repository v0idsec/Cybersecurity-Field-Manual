# Linux Networking Cheatsheet

Quick-reference commands for configuring, inspecting and troubleshooting Linux networking.

## Interface information

List interfaces and addresses:

```bash
ip addr
```

Short output:

```bash
ip -br addr
```

Show link state:

```bash
ip link
```

Show a specific interface:

```bash
ip addr show eth0
```

Bring an interface up or down:

```bash
sudo ip link set eth0 up
sudo ip link set eth0 down
```

## IP configuration

Add an address temporarily:

```bash
sudo ip addr add 192.168.1.50/24 dev eth0
```

Remove an address:

```bash
sudo ip addr del 192.168.1.50/24 dev eth0
```

Display routing table:

```bash
ip route
```

Display IPv6 routes:

```bash
ip -6 route
```

Add a temporary default route:

```bash
sudo ip route add default via 192.168.1.1
```

## DNS

Display resolver configuration:

```bash
cat /etc/resolv.conf
```

Query DNS:

```bash
dig example.com
```

Query a specific DNS server:

```bash
dig @192.0.2.53 example.com
```

Check name resolution:

```bash
getent hosts example.com
```

## Connectivity testing

Ping:

```bash
ping -c 4 192.0.2.10
```

Trace route:

```bash
traceroute example.com
```

Alternative:

```bash
tracepath example.com
```

Test a TCP port:

```bash
nc -vz 192.0.2.10 443
```

Test HTTPS connectivity:

```bash
curl -I https://example.com
```

## Listening ports and connections

Show listening TCP and UDP sockets:

```bash
ss -tuln
```

Show process information:

```bash
sudo ss -tulnp
```

Show established connections:

```bash
ss -tn state established
```

Alternative:

```bash
sudo netstat -tulnp
```

## ARP and neighbour discovery

Display neighbour table:

```bash
ip neigh
```

Show ARP cache:

```bash
arp -a
```

Flush neighbour cache:

```bash
sudo ip neigh flush all
```

## Network interface statistics

```bash
ip -s link
```

```bash
ethtool eth0
```

Check interface counters:

```bash
cat /proc/net/dev
```

## Firewall inspection

### UFW

```bash
sudo ufw status verbose
```

List numbered rules:

```bash
sudo ufw status numbered
```

### nftables

```bash
sudo nft list ruleset
```

### iptables

```bash
sudo iptables -L -n -v
```

## Packet capture

Capture traffic on an interface:

```bash
sudo tcpdump -i eth0
```

Capture traffic for a host:

```bash
sudo tcpdump -i eth0 host 192.0.2.10
```

Capture a specific port:

```bash
sudo tcpdump -i eth0 port 443
```

Save a capture:

```bash
sudo tcpdump -i eth0 -w capture.pcap
```

Read a capture:

```bash
tcpdump -r capture.pcap
```

## Network configuration services

Check NetworkManager:

```bash
systemctl status NetworkManager
```

List NetworkManager connections:

```bash
nmcli connection show
```

Display device status:

```bash
nmcli device status
```

Show active network configuration:

```bash
nmcli device show
```

## Quick troubleshooting workflow

1. Check interface state.
2. Confirm the assigned IP address.
3. Confirm subnet mask and gateway.
4. Check the routing table.
5. Test gateway connectivity.
6. Test an external IP address.
7. Test DNS resolution.
8. Check firewall rules.
9. Inspect listening services.
10. Capture traffic if the issue remains unclear.

## Useful paths

| Path | Purpose |
|---|---|
| `/etc/hosts` | Local hostname mappings |
| `/etc/resolv.conf` | Resolver configuration |
| `/etc/hostname` | System hostname |
| `/etc/NetworkManager/` | NetworkManager configuration |
| `/proc/net/` | Kernel network information |

## Notes

- `ip` is preferred over older `ifconfig` commands on modern Linux systems.
- Temporary `ip` configuration changes may disappear after reboot.
- Packet captures can contain sensitive information.
- Use `sudo` only where elevated privileges are necessary.

---

*Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
