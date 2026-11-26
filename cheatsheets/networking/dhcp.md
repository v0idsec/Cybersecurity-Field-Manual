# DHCP Cheatsheet

Quick-reference material for Dynamic Host Configuration Protocol, DHCP operation and troubleshooting.

## What is DHCP?

DHCP automatically provides network configuration to clients.

Typical settings include:

- IP address.
- Subnet mask.
- Default gateway.
- DNS servers.
- Lease duration.
- Domain search suffix.

## DHCP operation

The common DHCPv4 allocation process is known as DORA:

1. Discover — Client broadcasts a DHCPDISCOVER.
2. Offer — Server responds with a DHCPOFFER.
3. Request — Client requests the offered address.
4. Acknowledge — Server confirms the lease with DHCPACK.

```text
Client                     DHCP Server
  |                             |
  |------ DISCOVER ------------>|
  |<----- OFFER ----------------|
  |------ REQUEST ------------->|
  |<----- ACK ------------------|
  |                             |
  |       Lease assigned        |
```

## Common DHCP ports

| Port | Protocol | Purpose |
|---:|---|---|
| 67 | UDP | DHCP server |
| 68 | UDP | DHCP client |

## DHCP options

| Option | Purpose |
|---:|---|
| 1 | Subnet mask |
| 3 | Router / default gateway |
| 6 | DNS servers |
| 15 | DNS domain name |
| 42 | NTP servers |
| 51 | IP address lease time |
| 53 | DHCP message type |
| 54 | DHCP server identifier |
| 66 | TFTP server name |
| 67 | Boot file name |
| 82 | Relay agent information |

## Windows client commands

Display DHCP configuration:

```cmd
ipconfig /all
```

Release current lease:

```cmd
ipconfig /release
```

Request a new lease:

```cmd
ipconfig /renew
```

PowerShell lease information:

```powershell
Get-NetIPConfiguration
```

Display interface DHCP status:

```powershell
Get-NetIPInterface
```

## Windows DHCP Server PowerShell

Requires the DHCP Server tools/module and appropriate permissions.

List DHCP servers:

```powershell
Get-DhcpServerInDC
```

List IPv4 scopes:

```powershell
Get-DhcpServerv4Scope -ComputerName dhcp01.example.com
```

List active leases:

```powershell
Get-DhcpServerv4Lease -ComputerName dhcp01.example.com -ScopeId 192.168.1.0
```

List reservations:

```powershell
Get-DhcpServerv4Reservation -ComputerName dhcp01.example.com -ScopeId 192.168.1.0
```

Display scope options:

```powershell
Get-DhcpServerv4OptionValue -ComputerName dhcp01.example.com -ScopeId 192.168.1.0
```

## Linux DHCP troubleshooting

Check address configuration:

```bash
ip addr
```

Check routes:

```bash
ip route
```

Check DHCP-related logs:

```bash
journalctl -u NetworkManager
```

Depending on the Linux distribution, DHCP may be managed by NetworkManager, systemd-networkd or another network service.

## DHCP troubleshooting

| Symptom | Possible cause |
|---|---|
| 169.254.x.x address | DHCP request failed; link-local address assigned |
| No default gateway | Missing or incorrect DHCP option |
| Incorrect DNS server | DHCP option 6 configuration |
| Duplicate IP | Reservation conflict or rogue/static assignment |
| Intermittent connectivity | Lease, relay or network issue |
| No DHCP response | Server, relay, VLAN or firewall issue |

## DHCP security considerations

- Use DHCP snooping on supported switches.
- Restrict trusted DHCP server ports.
- Monitor rogue DHCP servers.
- Review DHCP reservations.
- Protect management interfaces.
- Monitor unusual lease activity.
- Use network segmentation.
- Consider Dynamic ARP Inspection and IP Source Guard where supported.

## DHCP relay

A DHCP relay forwards client DHCP messages between different subnets.

This allows clients to reach a central DHCP server without placing a server on every subnet.

Review:

- Relay interface configuration.
- Server destination addresses.
- VLAN and subnet mappings.
- Firewall rules.
- Relay agent information.

## Security review checklist

- [ ] Identify authorised DHCP servers.
- [ ] Review DHCP scopes.
- [ ] Check scope exhaustion.
- [ ] Review reservations.
- [ ] Identify rogue DHCP activity.
- [ ] Review DHCP snooping.
- [ ] Check relay configuration.
- [ ] Review lease durations.
- [ ] Validate DNS and gateway options.

---

*Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
