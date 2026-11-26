# Firewalls & Network Security

Quick-reference material for firewall configuration, network access controls and segmentation.

## Firewall fundamentals

A firewall controls network traffic according to defined rules.

Common filtering criteria:

- Source IP address.
- Destination IP address.
- Source port.
- Destination port.
- Protocol.
- Interface.
- Connection state.
- Application identity.
- User identity.

## Firewall types

| Type | Description |
|---|---|
| Stateless | Filters individual packets |
| Stateful | Tracks connection state |
| Application-layer | Inspects application traffic |
| Next-generation firewall | Adds advanced inspection and security features |
| Host-based | Runs on an endpoint or server |
| Network-based | Protects network segments |

## Common rule actions

| Action | Purpose |
|---|---|
| Allow | Permit matching traffic |
| Deny | Block matching traffic |
| Reject | Block and optionally return an error |
| Log | Record matching traffic |

## Linux UFW

Check status:

```bash
sudo ufw status verbose
```

Allow SSH:

```bash
sudo ufw allow 22/tcp
```

Allow HTTPS:

```bash
sudo ufw allow 443/tcp
```

Allow a source subnet:

```bash
sudo ufw allow from 192.168.1.0/24
```

Allow a specific source to a port:

```bash
sudo ufw allow from 192.168.1.50 to any port 22 proto tcp
```

Delete a rule:

```bash
sudo ufw delete allow 443/tcp
```

Enable UFW:

```bash
sudo ufw enable
```

Be careful when enabling or modifying a firewall over a remote connection. You may lock yourself out.

## Linux nftables

Display rules:

```bash
sudo nft list ruleset
```

List tables:

```bash
sudo nft list tables
```

List chains:

```bash
sudo nft list chains
```

nftables syntax and rule structure depend on the existing ruleset. Do not blindly replace production firewall configuration.

## Linux iptables

List rules:

```bash
sudo iptables -L -n -v
```

List NAT rules:

```bash
sudo iptables -t nat -L -n -v
```

Show rule numbers:

```bash
sudo iptables -L --line-numbers
```

## Windows Defender Firewall

Show profiles:

```powershell
Get-NetFirewallProfile
```

Show enabled rules:

```powershell
Get-NetFirewallRule -Enabled True
```

Show inbound rules:

```powershell
Get-NetFirewallRule -Direction Inbound
```

Show outbound rules:

```powershell
Get-NetFirewallRule -Direction Outbound
```

Enable firewall profiles:

```powershell
Set-NetFirewallProfile -Profile Domain,Private,Public -Enabled True
```

Create an inbound allow rule:

```powershell
New-NetFirewallRule -DisplayName "Allow HTTPS" -Direction Inbound -Protocol TCP -LocalPort 443 -Action Allow
```

## Network Access Control Lists

ACLs can restrict traffic between network segments or devices.

Example policy:

| Source | Destination | Service | Action |
|---|---|---|---|
| User VLAN | DNS servers | TCP/UDP 53 | Allow |
| User VLAN | Internet | HTTPS | Allow |
| Guest VLAN | Internal servers | Any | Deny |
| Management VLAN | Network devices | Approved management ports | Allow |
| Internet | Internal management interfaces | Any | Deny |

## Network segmentation

Useful segmentation boundaries include:

- User workstations.
- Servers.
- Domain controllers.
- Management systems.
- Guest wireless.
- IoT devices.
- Backup infrastructure.
- Security monitoring systems.

Use explicit inter-segment rules and avoid unnecessary flat networks.

## Firewall logging

Review:

- Denied inbound connections.
- Unexpected outbound traffic.
- Repeated connection attempts.
- Unusual destination ports.
- Connections to known malicious infrastructure.
- Traffic crossing unexpected network boundaries.
- Changes to firewall rules.

## Security review checklist

- [ ] Apply least privilege to network rules.
- [ ] Remove unused rules.
- [ ] Restrict administrative access.
- [ ] Review inbound and outbound traffic.
- [ ] Enable appropriate logging.
- [ ] Review overly broad source ranges.
- [ ] Restrict management interfaces.
- [ ] Validate segmentation.
- [ ] Document rule owners and business purpose.
- [ ] Review firewall changes regularly.

## Notes

- A firewall allow rule does not guarantee application availability.
- Stateful firewalls can treat return traffic differently from new inbound connections.
- NAT and firewall filtering are separate functions.
- Avoid broad `any-to-any` rules.
- Test rule changes in a controlled manner.

---

*Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
