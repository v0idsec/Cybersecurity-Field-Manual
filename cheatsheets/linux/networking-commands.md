# Linux Networking Commands

## Interface information

```bash
# Display interfaces and addresses
ip addr

# Show link status
ip link

# Show routing table
ip route

# Show neighbour table
ip neigh

# Display interface statistics
ip -s link

# Show DNS configuration
cat /etc/resolv.conf
```

## Connectivity testing

| Command | Description |
|---|---|
| `ping host` | Test ICMP connectivity |
| `traceroute host` | Trace network route |
| `tracepath host` | Trace path and path MTU |
| `mtr host` | Continuous route diagnostics |
| `curl URL` | HTTP request |
| `wget URL` | Retrieve URL |
| `nc -vz host port` | Test TCP connectivity |
| `ss -tuln` | Show listening sockets |

## DNS lookups

```bash
# Basic lookup
dig example.com

# Query A record
dig example.com A

# Query MX records
dig example.com MX

# Query TXT records
dig example.com TXT

# Query NS records
dig example.com NS

# Query all available record types
dig example.com ANY

# Reverse DNS lookup
dig -x 192.0.2.10

# Query a specific DNS server
dig @8.8.8.8 example.com

# Short output
dig +short example.com

# Alternative lookup
nslookup example.com

# Host lookup
host example.com
```

## Ports and connections

```bash
# Show listening TCP and UDP sockets
ss -tuln

# Show process information
sudo ss -tulpn

# Show established connections
ss -tn state established

# Show listening TCP ports
ss -tln

# Show listening UDP ports
ss -uln

# Legacy socket listing
sudo netstat -tulpn

# Identify processes using network sockets
sudo lsof -i -P -n
```

## curl reference

```bash
# GET request
curl https://example.com

# Show response headers
curl -I https://example.com

# Show request and response details
curl -v https://example.com

# Save response to file
curl -o output.html https://example.com

# Follow redirects
curl -L https://example.com

# Specify HTTP method
curl -X POST https://example.com

# Add request header
curl -H "Content-Type: application/json" https://example.com

# Send form data
curl -d "user=test" https://example.com

# Send JSON
curl -H "Content-Type: application/json" \
-d '{"user":"test"}' https://example.com

# Include response headers
curl -i https://example.com
```

## Netcat

```bash
# TCP connection test
nc -vz 192.0.2.10 443

# Connect to a host and port
nc 192.0.2.10 80

# Listen on a TCP port
nc -lv 4444

# UDP connection test
nc -vzu 192.0.2.10 53

# Send text to a remote service
echo "test" | nc 192.0.2.10 80
```

Use listeners and network connections only in controlled environments and within approved scope.

## Packet capture

```bash
# List capture interfaces
sudo tcpdump -D

# Capture traffic on an interface
sudo tcpdump -i eth0

# Capture traffic to a file
sudo tcpdump -i eth0 -w capture.pcap

# Read capture file
tcpdump -r capture.pcap

# Capture TCP traffic
sudo tcpdump -i eth0 tcp

# Capture traffic for a host
sudo tcpdump -i eth0 host 192.0.2.10

# Capture traffic on a port
sudo tcpdump -i eth0 port 443

# Display packet contents in ASCII
sudo tcpdump -A -i eth0

# Display packet contents in hex and ASCII
sudo tcpdump -XX -i eth0
```

## Routing

```bash
# Display routing table
ip route

# Show route to destination
ip route get 8.8.8.8

# Display routing rules
ip rule

# Display neighbour table
ip neigh
```

## Network troubleshooting checklist

1. Check interface state.
2. Confirm IP address and subnet.
3. Check default gateway.
4. Test gateway connectivity.
5. Test external IP connectivity.
6. Check DNS resolution.
7. Review routes.
8. Check firewall rules.
9. Inspect listening services.
10. Capture traffic if required.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
