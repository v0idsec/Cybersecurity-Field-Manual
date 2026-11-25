# Linux Logging

## Overview

Linux systems generate logs through system services, authentication mechanisms, applications and the kernel.

Centralised collection of these logs provides visibility into authentication, privilege escalation, process activity, persistence and system changes.

## Common Log Locations

| Log | Typical Location | Purpose |
|---|---|---|
| Authentication | `/var/log/auth.log` | Debian/Ubuntu authentication |
| Authentication | `/var/log/secure` | RHEL-based authentication |
| System | `/var/log/syslog` | General system messages |
| System | `/var/log/messages` | General system messages |
| Kernel | `/var/log/kern.log` | Kernel messages |
| Boot | `/var/log/boot.log` | Boot activity |
| Cron | `/var/log/cron` | Scheduled task activity |
| Audit | `/var/log/audit/audit.log` | Linux audit events |

Log locations vary by distribution and configuration.

## systemd Journal

Systems using systemd commonly collect events through journald.

### Useful Commands

View recent logs:

```bash
journalctl -n 100
```

Follow logs in real time:

```bash
journalctl -f
```

View logs from the current boot:

```bash
journalctl -b
```

View logs from a specific service:

```bash
journalctl -u ssh
```

Filter by time:

```bash
journalctl --since "24 hours ago"
```

View kernel messages:

```bash
journalctl -k
```

View logs for a specific executable:

```bash
journalctl /usr/bin/sudo
```

## Authentication Monitoring

Authentication logs are particularly valuable for identifying suspicious access.

Monitor:

- Successful SSH logins
- Failed SSH authentication
- Invalid usernames
- Root login attempts
- sudo execution
- Account lockouts
- New user creation
- Password changes
- Authentication configuration changes

### Search Authentication Logs

```bash
grep -i "failed password" /var/log/auth.log
```

```bash
grep -i "accepted" /var/log/auth.log
```

```bash
grep -i "sudo" /var/log/auth.log
```

For RHEL-based systems, substitute `/var/log/secure` where appropriate.

## auditd

Linux Audit provides detailed security-related event collection.

It can record:

- System calls
- File access
- Permission changes
- Account modifications
- Executable execution
- Security configuration changes

### Useful Commands

Check audit service status:

```bash
systemctl status auditd
```

Search audit events:

```bash
ausearch -ts today
```

Search authentication-related events:

```bash
ausearch -m USER_LOGIN
```

Search executable execution events:

```bash
ausearch -m EXECVE
```

Generate a summary:

```bash
aureport
```

Review audit rules:

```bash
auditctl -l
```

Audit rules should be designed around investigation and detection requirements. Excessive collection can generate substantial volume.

## Important Monitoring Areas

### SSH

Monitor:

- Authentication failures
- Successful logins from unusual addresses
- Root login attempts
- Changes to `sshd_config`
- Changes to authorised keys
- Unexpected SSH services

### sudo

Monitor:

- Unusual sudo usage
- Privilege escalation
- Unexpected administrative commands
- Changes to sudoers files
- New sudo group membership

### User and Group Management

Monitor:

- User creation
- User deletion
- Group membership changes
- UID or GID changes
- Password changes
- Changes to account expiry

### Persistence

Monitor changes to:

- Cron jobs
- systemd services
- systemd timers
- SSH authorised keys
- Shell startup files
- `/etc/passwd`
- `/etc/shadow`
- `/etc/sudoers`
- `/etc/ld.so.preload`

## Log Integrity and Collection

Consider:

- Centralised forwarding
- Restricted log permissions
- Remote log retention
- Time synchronisation
- Audit configuration monitoring
- Disk capacity monitoring
- Log rotation
- Protection against unauthorised deletion

## Investigation Workflow

1. Identify the affected host.
2. Establish the incident time window.
3. Review authentication activity.
4. Identify suspicious accounts and source addresses.
5. Review sudo and privilege escalation activity.
6. Examine process and service changes.
7. Inspect persistence locations.
8. Correlate activity with network and endpoint telemetry.
9. Preserve relevant logs and evidence.
10. Document findings.

## Further Reading

- Linux Audit: https://linux-audit.com/
- systemd Journal: https://www.freedesktop.org/software/systemd/man/latest/journalctl.html
- Red Hat Security Hardening: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
