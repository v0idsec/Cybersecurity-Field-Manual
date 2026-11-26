# Windows Networking Cheatsheet

Quick-reference commands for inspecting and troubleshooting Windows network configuration.

## IP configuration

Display network configuration:

```cmd
ipconfig
```

Show full configuration:

```cmd
ipconfig /all
```

Release DHCP lease:

```cmd
ipconfig /release
```

Renew DHCP lease:

```cmd
ipconfig /renew
```

Clear DNS cache:

```cmd
ipconfig /flushdns
```

Display DNS cache:

```cmd
ipconfig /displaydns
```

Register DNS records:

```cmd
ipconfig /registerdns
```

## PowerShell network commands

List network adapters:

```powershell
Get-NetAdapter
```

List IP addresses:

```powershell
Get-NetIPAddress
```

Display IP configuration:

```powershell
Get-NetIPConfiguration
```

Display routing table:

```powershell
Get-NetRoute
```

Display DNS server configuration:

```powershell
Get-DnsClientServerAddress
```

Display ARP and neighbour information:

```powershell
Get-NetNeighbor
```

## Connectivity testing

Ping:

```cmd
ping 192.0.2.10
```

Trace route:

```cmd
tracert example.com
```

Path diagnostics:

```cmd
pathping example.com
```

Test a TCP port:

```powershell
Test-NetConnection 192.0.2.10 -Port 443
```

Test DNS resolution:

```powershell
Resolve-DnsName example.com
```

Test a specific DNS server:

```powershell
Resolve-DnsName example.com -Server 192.0.2.53
```

## Listening ports and connections

Display active connections:

```cmd
netstat -ano
```

Display listening ports:

```cmd
netstat -ano | findstr LISTENING
```

Find the process using a PID:

```cmd
tasklist /FI "PID eq 1234"
```

PowerShell:

```powershell
Get-NetTCPConnection
```

Show listening TCP connections:

```powershell
Get-NetTCPConnection -State Listen
```

Show process information:

```powershell
Get-Process -Id 1234
```

## DNS commands

```cmd
nslookup example.com
```

Query a specific DNS server:

```cmd
nslookup example.com 192.0.2.53
```

PowerShell:

```powershell
Resolve-DnsName example.com -Type A
Resolve-DnsName example.com -Type AAAA
Resolve-DnsName example.com -Type MX
Resolve-DnsName example.com -Type TXT
```

## Firewall inspection

Display firewall profiles:

```powershell
Get-NetFirewallProfile
```

List firewall rules:

```powershell
Get-NetFirewallRule
```

Find enabled inbound rules:

```powershell
Get-NetFirewallRule -Enabled True -Direction Inbound
```

Display firewall configuration:

```cmd
netsh advfirewall show allprofiles
```

## Routing

Display routing table:

```cmd
route print
```

Display ARP cache:

```cmd
arp -a
```

Add a route:

```cmd
route add 10.10.0.0 mask 255.255.0.0 192.168.1.1
```

Delete a route:

```cmd
route delete 10.10.0.0
```

Use `-p` with `route add` to create a persistent route. Administrative privileges are generally required.

## Network adapter troubleshooting

Disable an adapter:

```powershell
Disable-NetAdapter -Name "Ethernet" -Confirm:$false
```

Enable an adapter:

```powershell
Enable-NetAdapter -Name "Ethernet"
```

Restart an adapter:

```powershell
Restart-NetAdapter -Name "Ethernet"
```

These commands can interrupt connectivity. Confirm access and change approval before using them remotely.

## Useful commands

| Command | Purpose |
|---|---|
| `ipconfig /all` | Full IP configuration |
| `ping` | Basic reachability test |
| `tracert` | Route tracing |
| `pathping` | Route and packet-loss diagnostics |
| `nslookup` | DNS lookup |
| `netstat -ano` | Connection and PID listing |
| `arp -a` | ARP cache |
| `route print` | Routing table |
| `netsh` | Network configuration and diagnostics |
| `Test-NetConnection` | PowerShell connectivity testing |

## Troubleshooting workflow

1. Run `ipconfig /all`.
2. Confirm the correct adapter is connected.
3. Check IP address and subnet.
4. Check default gateway.
5. Test the gateway with `ping`.
6. Test an external IP.
7. Test DNS resolution.
8. Test the required service port.
9. Inspect firewall configuration.
10. Review event logs and packet captures if necessary.

---

*Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
