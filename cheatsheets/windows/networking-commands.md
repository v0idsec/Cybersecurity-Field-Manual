# Windows Networking Commands

## IP configuration

```powershell
# IP configuration
Get-NetIPConfiguration

# All network interfaces
Get-NetAdapter

# IP addresses
Get-NetIPAddress

# Routing table
Get-NetRoute

# DNS client configuration
Get-DnsClientServerAddress

# ARP and neighbour information
Get-NetNeighbor
```

## Traditional commands

```cmd
ipconfig
ipconfig /all
ipconfig /displaydns
ipconfig /flushdns
ipconfig /renew
ping 192.0.2.1
tracert example.com
nslookup example.com
route print
arp -a
```

## Connectivity testing

```powershell
# ICMP test
Test-Connection example.com

# TCP port test
Test-NetConnection example.com -Port 443

# Detailed network test
Test-NetConnection example.com -InformationLevel Detailed

# DNS resolution
Resolve-DnsName example.com

# Trace route
Test-NetConnection example.com -TraceRoute
```

## Connections and listening ports

```powershell
# TCP connections
Get-NetTCPConnection

# Listening TCP connections
Get-NetTCPConnection -State Listen

# Established connections
Get-NetTCPConnection -State Established

# UDP endpoints
Get-NetUDPEndpoint

# Find process associated with connection
Get-NetTCPConnection |
    Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State, OwningProcess

# Resolve process IDs
Get-Process -Id 1234
```

## netstat

```cmd
:: All connections and listening ports
netstat -ano

:: Listening ports
netstat -an | findstr LISTENING

:: Established connections
netstat -an | findstr ESTABLISHED

:: Show executable names (requires suitable privileges)
netstat -ab
```

## DNS

```powershell
# Resolve hostname
Resolve-DnsName example.com

# Query A record
Resolve-DnsName example.com -Type A

# Query MX record
Resolve-DnsName example.com -Type MX

# Query TXT record
Resolve-DnsName example.com -Type TXT

# Query specific DNS server
Resolve-DnsName example.com -Server 8.8.8.8

# Flush DNS cache
Clear-DnsClientCache
```

## Firewall

```powershell
# Firewall profiles
Get-NetFirewallProfile

# All firewall rules
Get-NetFirewallRule

# Enabled rules
Get-NetFirewallRule -Enabled True

# Inbound rules
Get-NetFirewallRule -Direction Inbound

# Outbound rules
Get-NetFirewallRule -Direction Outbound

# Firewall rule details
Get-NetFirewallRule -DisplayName "Rule Name" |
    Get-NetFirewallPortFilter
```

## Windows HTTP and TLS troubleshooting

```powershell
# Request a URL
Invoke-WebRequest https://example.com

# HTTP headers
(Invoke-WebRequest https://example.com).Headers

# Test TCP connectivity
Test-NetConnection example.com -Port 443

# Inspect certificate using .NET
$tcp = [System.Net.Sockets.TcpClient]::new("example.com", 443)
$tcp.Close()
```

For detailed TLS certificate inspection, use an approved browser, certificate utility or TLS diagnostic tool.

## Network troubleshooting checklist

1. Confirm adapter state.
2. Check IP address and subnet.
3. Confirm default gateway.
4. Test gateway connectivity.
5. Test external IP connectivity.
6. Confirm DNS resolution.
7. Review routing table.
8. Review listening ports.
9. Inspect active connections.
10. Review Windows Firewall rules.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
