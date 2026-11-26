# VPNs & Remote Access

Quick-reference material for VPN technologies, remote access and tunnel troubleshooting.

## What is a VPN?

A Virtual Private Network creates an encrypted tunnel between endpoints or networks.

Common uses:

- Remote workforce access.
- Site-to-site connectivity.
- Secure administration.
- Access to internal applications.
- Network segmentation.

## VPN types

| Type | Purpose |
|---|---|
| Remote access VPN | Connects an individual device to a network |
| Site-to-site VPN | Connects two or more networks |
| Clientless VPN | Provides browser-based access |
| Full tunnel | Routes all supported traffic through the VPN |
| Split tunnel | Routes selected traffic through the VPN |

## Common VPN technologies

| Technology | Common use |
|---|---|
| IPsec | Site-to-site and remote access |
| IKEv2 | IPsec key exchange |
| OpenVPN | SSL/TLS-based VPN |
| WireGuard | Modern encrypted tunnel |
| SSTP | Microsoft VPN over TLS |
| L2TP/IPsec | Legacy remote access |
| SSL VPN | Vendor-specific remote access implementations |

## Common ports and protocols

| Port / Protocol | Service |
|---|---|
| UDP 500 | IKE |
| UDP 4500 | IPsec NAT Traversal |
| ESP (IP protocol 50) | IPsec Encapsulating Security Payload |
| AH (IP protocol 51) | IPsec Authentication Header |
| UDP 1194 | Common OpenVPN default |
| UDP 51820 | Common WireGuard default |
| TCP 443 | Common SSL VPN access |

Port numbers can be changed by administrators and vendors.

## Linux network tunnel inspection

List interfaces:

```bash
ip addr
```

List routes:

```bash
ip route
```

Show tunnel interfaces:

```bash
ip link
```

Show WireGuard status:

```bash
sudo wg show
```

Check IPsec status with strongSwan:

```bash
sudo ipsec statusall
```

## Windows VPN inspection

List VPN connections:

```powershell
Get-VpnConnection
```

List all users' VPN connections:

```powershell
Get-VpnConnection -AllUserConnection
```

Show network adapters:

```powershell
Get-NetAdapter
```

Display routes:

```powershell
Get-NetRoute
```

## Connectivity troubleshooting

Check:

- VPN client connection state.
- Authentication success.
- Assigned VPN address.
- DNS configuration.
- Routing table.
- Split-tunnel configuration.
- Firewall policy.
- MTU and fragmentation.
- Server-side tunnel status.

Test connectivity:

```bash
ping 10.10.0.1
```

Test a service:

```bash
nc -vz 10.10.0.10 443
```

Windows:

```powershell
Test-NetConnection 10.10.0.10 -Port 443
```

## Common problems

| Symptom | Possible cause |
|---|---|
| Authentication fails | Credentials, MFA or certificate issue |
| Connects but cannot access resources | Routing or firewall issue |
| Internal names fail | DNS configuration |
| Some websites fail | MTU or split-tunnel issue |
| Tunnel repeatedly disconnects | Network instability or timeout |
| Works on one network only | NAT, firewall or ISP filtering |
| No access to local devices | Full-tunnel routing or client policy |

## VPN security checklist

- [ ] Require MFA where supported.
- [ ] Use modern encryption configurations.
- [ ] Disable obsolete protocols and cipher suites.
- [ ] Restrict VPN access by role.
- [ ] Review split-tunnel policy.
- [ ] Monitor authentication logs.
- [ ] Remove inactive accounts.
- [ ] Patch VPN gateways.
- [ ] Restrict administrative interfaces.
- [ ] Review device compliance requirements.
- [ ] Monitor unusual access locations and times.

## Notes

- A VPN does not automatically make an endpoint trustworthy.
- VPN access should be subject to least privilege.
- Split tunnelling has both security and performance implications.
- A connected tunnel does not guarantee that internal DNS or routing is correct.

---

*Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
