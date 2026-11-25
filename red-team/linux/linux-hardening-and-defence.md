# Linux Hardening and Defence

Linux hardening reduces the attack surface, limits the impact of compromise and improves the ability to detect suspicious activity.

This guide provides a practical reference for assessing and improving Linux security controls.

## 1. Security Baseline

Establish the current system configuration:

```bash
uname -a
cat /etc/os-release
hostnamectl
```

Record:

- Distribution and release.
- Kernel version.
- Installed software.
- Running services.
- Network exposure.
- User and group configuration.
- Security enforcement mechanisms.

Use an established baseline appropriate to the operating system and workload.

Useful references:

- CIS Benchmarks: https://www.cisecurity.org/cis-benchmarks
- DISA STIGs: https://public.cyber.mil/stigs/
- OpenSCAP: https://www.open-scap.org/

## 2. Patch Management

Identify installed package updates.

Debian-based systems:

```bash
apt list --upgradable
```

RHEL-based systems:

```bash
dnf check-update
```

Review kernel version:

```bash
uname -r
```

Hardening recommendations:

- Apply security updates promptly.
- Use supported operating system releases.
- Track vendor security advisories.
- Validate updates before production deployment.
- Establish a kernel update and reboot process.
- Remove obsolete packages.

## 3. User and Account Security

Review local accounts:

```bash
getent passwd
```

Review administrative groups:

```bash
getent group sudo
getent group wheel
```

Recommended controls:

- Remove unnecessary accounts.
- Disable unused accounts.
- Restrict administrative group membership.
- Use individual accounts.
- Avoid shared administrative credentials.
- Apply least privilege.
- Enforce account lifecycle procedures.

## 4. SSH Hardening

Review effective SSH configuration:

```bash
sudo sshd -T
```

Common hardening considerations:

| Setting | Recommended consideration |
|---|---|
| `PermitRootLogin` | Disable direct root login where practical |
| `PasswordAuthentication` | Prefer key-based authentication where suitable |
| `PubkeyAuthentication` | Enable approved public key authentication |
| `AllowUsers` | Restrict access to approved accounts |
| `AllowGroups` | Restrict access to approved groups |
| `MaxAuthTries` | Limit authentication attempts |
| `X11Forwarding` | Disable if not required |

Changes should be tested before closing an existing administrative session to avoid accidental lockout.

## 5. Firewall Configuration

Inspect firewall rules:

```bash
sudo ufw status verbose
sudo nft list ruleset
sudo iptables -L -n -v
```

Recommended controls:

- Default-deny inbound traffic where appropriate.
- Allow only required services.
- Restrict administrative interfaces.
- Limit management access to trusted networks.
- Review IPv4 and IPv6 rules.
- Document approved network flows.

Do not apply generic firewall rules without understanding the system's required connectivity.

## 6. Mandatory Access Control

Linux commonly uses SELinux or AppArmor to enforce additional access restrictions.

SELinux:

```bash
getenforce
sestatus
```

AppArmor:

```bash
sudo aa-status
```

Recommendations:

- Keep enforcement enabled where supported.
- Use appropriate profiles and policies.
- Investigate denials rather than disabling enforcement.
- Review policy exceptions.
- Monitor changes to security profiles.

## 7. Filesystem Security

Review mount configuration:

```bash
findmnt
cat /etc/fstab
```

Consider appropriate mount restrictions for temporary and user-writable filesystems:

- `nodev`
- `nosuid`
- `noexec`

These options have operational implications and should be applied according to workload requirements.

Review sensitive file permissions:

```bash
ls -l /etc/passwd /etc/shadow /etc/sudoers
```

Restrict access to:

- SSH private keys.
- Application configuration.
- Service credentials.
- Backup archives.
- Administrative scripts.

## 8. Service Hardening

List active services:

```bash
systemctl list-units --type=service --state=running
```

Disable unnecessary services through approved change management.

For systemd services, consider:

- Dedicated service accounts.
- `NoNewPrivileges=`
- `PrivateTmp=`
- `ProtectSystem=`
- `ProtectHome=`
- `ReadOnlyPaths=`
- `ReadWritePaths=`
- Restricted capabilities.

Validate service compatibility before applying restrictions.

## 9. Audit and Logging

Check logging services:

```bash
systemctl status rsyslog
systemctl status systemd-journald
```

Review recent logs:

```bash
journalctl --since "24 hours ago"
```

Authentication logs may be found at:

```text
/var/log/auth.log
/var/log/secure
```

Useful audit tooling:

- auditd.
- journald.
- rsyslog.
- Wazuh.
- osquery.
- Elastic Agent.

Monitor:

- Authentication events.
- Privileged command execution.
- Account creation and modification.
- SSH configuration changes.
- Sudoers modifications.
- Service installation and modification.
- Sensitive file access.

## 10. Auditd

Check audit service status:

```bash
sudo systemctl status auditd
```

Review audit status:

```bash
sudo auditctl -s
```

List loaded rules:

```bash
sudo auditctl -l
```

Review audit logs:

```bash
sudo ausearch -m USER_AUTH
```

Audit policy should be designed around system requirements and event volume. Excessive logging can create operational overhead.

## 11. Vulnerability and Configuration Assessment

Useful tools:

| Tool | Purpose |
|---|---|
| Lynis | Linux security auditing |
| OpenSCAP | Compliance and configuration assessment |
| Trivy | Vulnerability and configuration scanning |
| osquery | Host visibility and querying |
| auditd | Security event auditing |
| Wazuh | Host monitoring and security detection |

References:

- https://github.com/CISOfy/lynis
- https://www.open-scap.org/
- https://trivy.dev/
- https://osquery.io/
- https://wazuh.com/

## 12. Backup and Recovery

Security controls should include recovery capability.

Assess:

- Backup frequency.
- Backup encryption.
- Access restrictions.
- Offline or immutable copies.
- Retention policy.
- Restoration testing.
- Configuration backup.
- Recovery time objectives.

Backups should not be permanently accessible using the same credentials as the production system.

## 13. Hardening Checklist

- [ ] Supported operating system release.
- [ ] Security updates applied.
- [ ] Unnecessary packages removed.
- [ ] Unnecessary services disabled.
- [ ] Administrative accounts restricted.
- [ ] SSH configuration hardened.
- [ ] Firewall rules reviewed.
- [ ] SELinux or AppArmor enforced.
- [ ] Sensitive file permissions secured.
- [ ] Service privileges minimised.
- [ ] Audit logging enabled.
- [ ] Logs centrally collected where appropriate.
- [ ] Vulnerability scanning implemented.
- [ ] Backups protected and restoration tested.
- [ ] Configuration baseline documented.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
