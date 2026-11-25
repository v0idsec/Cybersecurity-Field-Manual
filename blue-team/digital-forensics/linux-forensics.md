# Linux Forensics

## Overview

Linux forensic investigations examine system logs, authentication records, process information, file-system artefacts, user activity and persistence mechanisms.

Evidence sources vary significantly between distributions and system configurations.

## Common Evidence Locations

| Location | Description |
|---|---|
| `/var/log/` | System and application logs |
| `/etc/` | System configuration |
| `/home/` | User data |
| `/root/` | Root user's data |
| `/tmp/` | Temporary files |
| `/var/tmp/` | Persistent temporary files |
| `/var/spool/cron/` | Cron-related data |
| `/etc/systemd/` | Systemd configuration |
| `/proc/` | Kernel process information |
| `/run/` | Runtime system data |

## Authentication Logs

Common files include:

```text
/var/log/auth.log
/var/log/secure
```

The location depends on the distribution and logging configuration.

Search for SSH activity:

```bash
grep -i ssh /var/log/auth.log
```

Search for failed authentication:

```bash
grep -i "failed password" /var/log/auth.log
```

Search for successful authentication:

```bash
grep -i "accepted" /var/log/auth.log
```

## Journal Logs

Systems using systemd commonly use journald.

Display recent logs:

```bash
journalctl
```

Show logs for a time range:

```bash
journalctl --since "2026-11-25 00:00:00" \
  --until "2026-11-25 23:59:59"
```

Show SSH-related service logs:

```bash
journalctl -u ssh
```

The service may be named `sshd` on some distributions.

## User Activity

Useful commands include:

```bash
last
```

```bash
lastlog
```

```bash
who
```

```bash
w
```

These tools rely on records that may be incomplete, rotated, altered or unavailable.

## Shell History

Potential locations:

```text
~/.bash_history
~/.zsh_history
~/.local/share/fish/fish_history
```

Inspect history carefully:

```bash
cat ~/.bash_history
```

Shell history is not a complete audit trail.

Commands may not have been written to disk, may have been disabled or may have been modified.

## Process Information

On a live system:

```bash
ps auxf
```

```bash
ps -eo pid,ppid,user,lstart,cmd
```

Review process details:

```bash
cat /proc/<PID>/status
```

Inspect process command line:

```bash
tr '\0' ' ' < /proc/<PID>/cmdline
```

Live `/proc` data changes as the system runs. Record the collection time.

## Network Connections

```bash
ss -tulpn
```

```bash
ip addr
```

```bash
ip route
```

Review available connection information and correlate it with firewall, DNS and network records.

## Persistence Mechanisms

Investigate:

### Cron

```bash
crontab -l
```

```bash
ls -la /etc/cron*
```

### Systemd

```bash
systemctl list-unit-files --type=service
```

Inspect a service:

```bash
systemctl cat suspicious.service
```

### SSH Authorised Keys

```bash
find /home /root -name authorized_keys -type f 2>/dev/null
```

Review unexpected keys and account changes.

### Startup Scripts

Investigate:
- `/etc/rc.local`
- `/etc/profile`
- `/etc/profile.d/`
- User shell initialisation files

## File-System Examination

Useful commands:

```bash
stat suspicious-file
```

```bash
find /path/to/evidence -type f -mtime -7
```

```bash
find /path/to/evidence -type f -perm /6000
```

The last example identifies files with set-user-ID or set-group-ID permissions.

Use these commands against forensic copies or through a documented read-only workflow where practical.

## Package and Software Artefacts

Depending on distribution, inspect:

Debian-based systems:

```bash
cat /var/log/dpkg.log
```

RPM-based systems:

```bash
dnf history
```

Package records may help identify software installation and update activity.

## Log Rotation

Investigate:
- Current logs
- Rotated logs
- Compressed archives
- Journald retention
- Remote logging systems

Example:

```bash
ls -lah /var/log/
```

Log absence does not prove an event did not occur.

## Investigation Workflow

1. Identify distribution and version.
2. Preserve relevant disk and memory evidence.
3. Review authentication records.
4. Examine user accounts and privileges.
5. Review shell history.
6. Examine process and network information.
7. Investigate scheduled tasks and systemd services.
8. Review package installation records.
9. Examine suspicious files.
10. Correlate events with network and identity logs.
11. Document findings and limitations.

## Common Mistakes

- Assuming all Linux distributions use the same log paths.
- Treating shell history as a complete record.
- Ignoring log rotation.
- Failing to account for system clock differences.
- Assuming `/proc` data is persistent.
- Ignoring remote logging.
- Treating suspicious filenames as proof of compromise.
- Running investigative commands on original evidence without documenting changes.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
