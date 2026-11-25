# Linux Hardening

## Overview

Linux hardening reduces the attack surface of Linux servers, workstations and appliances through secure configuration, access restrictions, service management, patching and monitoring.

Exact recommendations vary between distributions, versions and workloads. Validate changes against the system's role before deployment.

## 1. Operating system maintenance

- Use a supported distribution and release.
- Apply security updates through trusted repositories.
- Remove obsolete packages and unused software.
- Keep the kernel and bootloader maintained.
- Review third-party repositories and package signing.
- Restrict access to boot and recovery environments.
- Maintain a tested backup and recovery process.

Example package maintenance commands:

```bash
# Debian / Ubuntu
sudo apt update
apt list --upgradable
sudo apt upgrade

# RHEL-family systems
sudo dnf check-update
sudo dnf upgrade
```

Review pending updates and test critical workloads before applying changes to production systems.

## 2. User and privilege management

Recommended controls:

- Avoid routine use of the root account.
- Use individual named user accounts.
- Restrict sudo access to approved administrators.
- Remove unused accounts.
- Review service account permissions.
- Use centrally managed identity where appropriate.
- Monitor changes to privileged groups.

Useful commands:

```bash
# List users
getent passwd

# Review groups
getent group

# Review sudo configuration
sudo visudo -c

# Identify users with UID 0
awk -F: '$3 == 0 {print $1}' /etc/passwd

# Review recent login history
last
```

Only the expected administrative identity should normally have UID 0.

## 3. SSH hardening

SSH is a common administrative access path and should be tightly controlled.

Consider:

- Disable direct root login where operationally appropriate.
- Prefer key-based authentication.
- Require MFA for sensitive access paths where supported.
- Restrict access to approved users and groups.
- Restrict source networks through firewalls or access gateways.
- Disable unused authentication methods.
- Monitor authentication failures.
- Keep OpenSSH updated.

Example configuration considerations for `/etc/ssh/sshd_config`:

```text
PermitRootLogin no
PubkeyAuthentication yes
AllowGroups ssh-admins
X11Forwarding no
```

These are examples, not a universal configuration. Confirm that the authentication design and access requirements are compatible before applying changes.

Validate configuration and reload safely:

```bash
# Check SSH configuration syntax
sudo sshd -t

# Review effective configuration
sudo sshd -T

# Reload the service after validation
sudo systemctl reload ssh
```

Keep an existing administrative session open while testing a new connection to avoid locking yourself out.

## 4. Service management

Disable services that are not required for the system's purpose.

```bash
# List running services
systemctl --type=service --state=running

# List enabled services
systemctl list-unit-files --type=service --state=enabled

# Review listening sockets
sudo ss -tulpn

# Review active network connections
sudo ss -tunap
```

Before disabling a service, identify dependencies and confirm that it is not required by applications or system management.

## 5. Firewall configuration

Use the firewall framework supported by the distribution.

Common options:

- `nftables`
- `ufw`
- `firewalld`

Example UFW review:

```bash
# Check firewall status
sudo ufw status verbose

# List numbered rules
sudo ufw status numbered
```

Example firewalld review:

```bash
# Check firewall state
sudo firewall-cmd --state

# List active zones
sudo firewall-cmd --get-active-zones

# Review rules in the default zone
sudo firewall-cmd --list-all
```

Apply a default-deny inbound policy where appropriate, with explicit allowances for required services. Ensure remote management access remains available before changing firewall rules.

## 6. Filesystem permissions

Review sensitive files and directories.

Examples:

```bash
# Review passwd permissions
stat /etc/passwd

# Review shadow permissions
stat /etc/shadow

# Review sudoers permissions
stat /etc/sudoers

# Find world-writable directories (may produce a large result)
sudo find / -xdev -type d -perm -0002 -print 2>/dev/null

# Find files with SUID or SGID bits
sudo find / -xdev -type f \( -perm -4000 -o -perm -2000 \) -print 2>/dev/null
```

Do not automatically change every discovered permission. Some applications legitimately require special permissions or writable directories.

Review:

- Ownership.
- Group membership.
- World-readable or writable files.
- SUID and SGID binaries.
- Capabilities.
- Sensitive application configuration.
- Backup and temporary directories.

## 7. Kernel and system settings

Review kernel parameters and security features relevant to the workload.

Areas to consider:

- Address Space Layout Randomisation (ASLR).
- Kernel pointer exposure.
- Core dump handling.
- Network forwarding.
- ICMP behaviour.
- Source routing.
- Reverse path filtering.
- Kernel module loading.
- Unprivileged user namespaces, where relevant to the threat model.

Review current settings:

```bash
# Kernel parameters
sysctl -a

# ASLR setting
sysctl kernel.randomize_va_space

# Review loaded modules
lsmod

# Review kernel version
uname -r
```

Kernel settings can affect networking, containers, virtualisation and application behaviour. Apply only tested changes.

## 8. Mandatory access control

Mandatory Access Control (MAC) can restrict what processes are allowed to access.

Common Linux implementations:

- SELinux.
- AppArmor.

Useful checks:

```bash
# SELinux status
getenforce
sestatus

# AppArmor status
sudo aa-status
```

Prefer enforcing policies where supported and tested. Investigate policy violations rather than immediately disabling the security mechanism.

## 9. Logging and monitoring

Useful log sources include:

| Source | Purpose |
|---|---|
| `journald` | System and service logs |
| `/var/log/auth.log` | Authentication events on common Debian-based systems |
| `/var/log/secure` | Authentication events on common RHEL-based systems |
| `auditd` | System audit events |
| SSH logs | Remote access activity |
| Package manager logs | Software installation and updates |
| Web server logs | HTTP access and errors |

Commands:

```bash
# Review recent system logs
journalctl -n 100

# Review authentication-related logs
sudo journalctl -u ssh

# Review failed systemd services
systemctl --failed

# Review audit service status
systemctl status auditd
```

Log paths and service names vary by distribution.

## 10. Time synchronisation

Accurate timestamps are important for incident investigation and event correlation.

- Use approved time sources.
- Monitor synchronisation status.
- Restrict unauthorised time source changes.
- Ensure systems use consistent time zones or clearly record their offsets.

Example:

```bash
timedatectl status
```

## 11. Validation checklist

- [ ] Supported Linux distribution and release.
- [ ] Security updates applied.
- [ ] Unused packages and services reviewed.
- [ ] Root access restricted.
- [ ] Sudo access reviewed.
- [ ] SSH configuration assessed.
- [ ] Firewall enabled and rules reviewed.
- [ ] Listening ports justified.
- [ ] Sensitive file permissions reviewed.
- [ ] SUID/SGID binaries assessed.
- [ ] MAC controls enabled where supported.
- [ ] Audit and system logging configured.
- [ ] Time synchronisation working.
- [ ] Backups and recovery tested.
- [ ] Configuration exceptions documented.

## References

- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)
- [Ubuntu Security Documentation](https://ubuntu.com/security)
- [Red Hat Security Hardening](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/)
- [OpenSSH Manual](https://www.openssh.com/manual.html)
- [Linux Audit Documentation](https://linux-audit.com/)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
