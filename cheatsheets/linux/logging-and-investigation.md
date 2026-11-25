# Linux Logging and Investigation

## Common log locations

| Location | Description |
|---|---|
| `/var/log/syslog` | General system logs on many Debian-based systems |
| `/var/log/messages` | General system logs on many RHEL-based systems |
| `/var/log/auth.log` | Authentication logs on common Debian-based systems |
| `/var/log/secure` | Authentication logs on common RHEL-based systems |
| `/var/log/kern.log` | Kernel messages on some distributions |
| `/var/log/dmesg` | Kernel ring buffer output on some systems |
| `/var/log/audit/` | Audit framework logs |
| `/var/log/nginx/` | Nginx logs |
| `/var/log/apache2/` | Apache logs on common Debian-based systems |

Log locations depend on distribution and logging configuration.

## journalctl

```bash
# Display all available journal entries
journalctl

# Show recent entries
journalctl -n 100

# Follow new entries
journalctl -f

# Show entries since boot
journalctl -b

# Show entries from previous boot
journalctl -b -1

# Filter by service
journalctl -u ssh

# Filter by priority
journalctl -p warning

# Filter by time
journalctl --since "1 hour ago"

# Show kernel messages
journalctl -k

# Show entries for a specific executable
journalctl /usr/sbin/sshd
```

## Authentication investigation

```bash
# Review recent logins
last

# Review failed login attempts
sudo lastb

# Search authentication logs
sudo grep -i "failed" /var/log/auth.log

# Search for accepted SSH logins
sudo grep "Accepted" /var/log/auth.log

# Review SSH service logs
sudo journalctl -u ssh

# Review sudo activity
sudo grep "sudo" /var/log/auth.log
```

Paths and messages differ between distributions.

## Search and filtering

```bash
# Search for authentication failures
grep -i "authentication failure" /var/log/*

# Search for failed logins
grep -i "failed password" /var/log/auth.log

# Search for account creation
grep -i "new user" /var/log/*

# Search for sudo usage
grep -i "sudo" /var/log/auth.log

# Extract unique source IPs from matching SSH logs
grep "Failed password" /var/log/auth.log | \
awk '{print $(NF-3)}' | sort -u
```

Always validate field positions against the actual log format before relying on extraction commands.

## auditd

```bash
# Check audit service
systemctl status auditd

# List active audit rules
sudo auditctl -l

# Search user login events
sudo ausearch -m USER_LOGIN

# Search events for a user ID
sudo ausearch -ua 1000

# Search events since today
sudo ausearch -ts today

# Generate audit report
sudo aureport

# Authentication report
sudo aureport -au
```

Audit event availability depends on configured rules and audit policy.

## Process and persistence investigation

```bash
# Running processes
ps auxf

# Listening ports
sudo ss -tulpn

# Scheduled tasks
crontab -l
sudo ls -la /etc/cron.*

# Enabled services
systemctl list-unit-files --type=service --state=enabled

# Systemd timers
systemctl list-timers

# Loaded kernel modules
lsmod

# Recently modified files
find /etc -type f -mmin -60 -ls
```

## File integrity

```bash
# Calculate SHA-256 hash
sha256sum file

# Calculate SHA-512 hash
sha512sum file

# Identify file type
file suspicious-file

# Inspect metadata
stat suspicious-file

# Review extended attributes
getfattr -d suspicious-file
```

## Incident investigation workflow

1. Confirm the affected system and time window.
2. Preserve relevant logs and evidence.
3. Record the system time and timezone.
4. Identify suspicious accounts and authentication events.
5. Review processes, services and scheduled tasks.
6. Inspect network connections.
7. Review modified files and persistence mechanisms.
8. Correlate events with endpoint and network telemetry.
9. Document findings and confidence.
10. Follow the incident response and evidence handling procedures.

Do not clear logs or modify suspicious artefacts during an investigation unless explicitly authorised and documented.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
