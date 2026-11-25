# Linux Security Tool & Command Reference

A practical reference for Linux reconnaissance, enumeration, privilege assessment, service analysis and defensive auditing.

Commands are grouped by tool and purpose.

Use only against systems within your authorised assessment scope.

---

## 1. Core Linux Commands

### System Information

| Command | Purpose |
|---|---|
| `uname -a` | Kernel and system information |
| `uname -r` | Kernel version |
| `hostname` | System hostname |
| `hostnamectl` | Host configuration |
| `cat /etc/os-release` | Distribution information |
| `lscpu` | CPU architecture and details |
| `free -h` | Memory usage |
| `df -h` | Filesystem usage |
| `lsblk` | Block device enumeration |
| `uptime` | System uptime |

### User Enumeration

| Command | Purpose |
|---|---|
| `whoami` | Current username |
| `id` | UID, GID and groups |
| `groups` | Group membership |
| `who` | Logged-in users |
| `w` | User activity |
| `getent passwd` | Account enumeration |
| `getent group` | Group enumeration |
| `sudo -l` | Current sudo permissions |
| `last` | Login history |
| `lastlog` | Last login information |

### Filesystem Enumeration

| Command | Purpose |
|---|---|
| `ls -lah` | Detailed directory listing |
| `stat FILE` | File metadata |
| `find PATH -type f` | Find files |
| `find PATH -type d` | Find directories |
| `find PATH -writable` | Find writable paths |
| `findmnt` | Mounted filesystems |
| `mount` | Mount information |
| `getfacl FILE` | ACL inspection |
| `du -sh PATH` | Directory size |

---

## 2. Permission Enumeration

### SUID Files

```bash
find / -type f -perm -4000 -ls 2>/dev/null
```

### SGID Files

```bash
find / -type f -perm -2000 -ls 2>/dev/null
```

### World-Writable Files

```bash
find / -type f -perm -0002 -ls 2>/dev/null
```

### World-Writable Directories

```bash
find / -type d -perm -0002 -ls 2>/dev/null
```

### Files Writable by Current User

```bash
find / -type f -writable -ls 2>/dev/null
```

### Linux Capabilities

```bash
getcap -r / 2>/dev/null
```

### ACLs

```bash
getfacl /path/to/file
```

---

## 3. Sudo

### Enumerate Permissions

```bash
sudo -l
```

### Inspect Configuration

```bash
sudo cat /etc/sudoers
sudo ls -lah /etc/sudoers.d/
```

### Validate Configuration Syntax

```bash
sudo visudo -c
```

### Check Version

```bash
sudo -V
```

Reference:

https://www.sudo.ws/

---

## 4. Process and Service Enumeration

### Processes

```bash
ps aux
ps -ef
ps -eo user,pid,ppid,cmd
top
```

### Systemd Services

```bash
systemctl list-units --type=service --all
systemctl list-unit-files --type=service
systemctl list-units --type=service --state=running
```

### Inspect a Service

```bash
systemctl status SERVICE
systemctl cat SERVICE
```

### Timers

```bash
systemctl list-timers --all
```

### Cron

```bash
cat /etc/crontab
ls -lah /etc/cron.d/
crontab -l
```

---

## 5. Network Enumeration

### Interfaces

```bash
ip addr
ip link
```

### Routing

```bash
ip route
ip neigh
```

### Listening Ports

```bash
ss -tulpen
```

### Established Connections

```bash
ss -antp
```

### UDP Sockets

```bash
ss -aunp
```

### Open Network Files

```bash
sudo lsof -i -P -n
```

### DNS

```bash
cat /etc/resolv.conf
cat /etc/hosts
```

---

## 6. SSH

### Effective Configuration

```bash
sudo sshd -T
```

### Configuration Files

```bash
cat /etc/ssh/sshd_config
ls -lah /etc/ssh/sshd_config.d/
```

### Authorised Keys

```bash
find /home -name authorized_keys -type f -ls 2>/dev/null
```

### SSH Connection

```bash
ssh USER@HOST
```

### SSH Debugging

```bash
ssh -vvv USER@HOST
```

Reference:

https://www.openssh.com/

---

## 7. LinPEAS

Repository:

https://github.com/peass-ng/PEASS-ng

LinPEAS automates Linux privilege escalation enumeration.

Useful assessment areas:

- System information.
- User and group configuration.
- Sudo permissions.
- SUID and SGID binaries.
- Linux capabilities.
- Scheduled tasks.
- Services.
- Writable files.
- Application configuration.
- Container indicators.

Run only within authorised environments and review findings manually.

---

## 8. Linux Smart Enumeration (LSE)

Repository:

https://github.com/diego-treitos/linux-smart-enumeration

LSE provides structured Linux enumeration.

Useful for:

- System information.
- User enumeration.
- File permissions.
- Sudo configuration.
- SUID and SGID files.
- Scheduled tasks.
- Services.
- Potential privilege escalation paths.

Its staged enumeration approach can help control the amount of information collected.

---

## 9. pspy

Repository:

https://github.com/DominicBreuker/pspy

pspy monitors process execution without requiring root privileges.

Useful for identifying:

- Cron activity.
- Short-lived processes.
- Scheduled scripts.
- Service execution.
- Unexpected process relationships.

Use monitoring within the engagement's approved scope and duration.

---

## 10. GTFOBins

Reference:

https://gtfobins.github.io/

GTFOBins documents security-relevant behaviour in common Unix binaries.

Useful categories:

- SUID.
- Sudo.
- Capabilities.
- Shell.
- Command execution.
- File read.
- File write.
- Library load.

Use it to investigate whether an exposed binary can undermine an intended privilege boundary.

---

## 11. lsof

List open files:

```bash
lsof
```

Inspect a process:

```bash
lsof -p PID
```

Inspect network connections:

```bash
lsof -i
```

Useful for identifying:

- Open configuration files.
- Unexpected file access.
- Network connections.
- Application dependencies.
- Deleted files still held open.

---

## 12. Docker

### Container Enumeration

```bash
docker ps
docker ps -a
docker images
```

### Container Inspection

```bash
docker inspect CONTAINER
docker stats
docker port CONTAINER
```

### Network Enumeration

```bash
docker network ls
docker network inspect NETWORK
```

### Runtime Information

```bash
docker info
docker version
```

Assess privileged mode, capabilities, mounts, socket exposure and container network configuration.

---

## 13. Podman

### Container Enumeration

```bash
podman ps -a
podman images
```

### Inspection

```bash
podman inspect CONTAINER
podman info
```

Podman supports rootless container operation and is frequently used in environments that do not rely on the Docker daemon.

---

## 14. Vulnerability and Hardening Tools

| Tool | Primary use | Reference |
|---|---|---|
| Lynis | Linux security auditing | https://github.com/CISOfy/lynis |
| OpenSCAP | Security compliance assessment | https://www.open-scap.org/ |
| Trivy | Vulnerability and configuration scanning | https://trivy.dev/ |
| osquery | Host visibility and querying | https://osquery.io/ |
| auditd | Linux security auditing | https://github.com/linux-audit/audit-userspace |
| Wazuh | Host monitoring and detection | https://wazuh.com/ |
| Nmap | Network and service discovery | https://nmap.org/ |

---

## 15. Useful Log Locations

| Location | Purpose |
|---|---|
| `/var/log/auth.log` | Debian authentication events |
| `/var/log/secure` | RHEL authentication events |
| `/var/log/syslog` | General system logging on some distributions |
| `/var/log/messages` | General system logging on some distributions |
| `/var/log/audit/audit.log` | auditd events |
| `/var/log/kern.log` | Kernel messages on some distributions |
| `/var/log/journal/` | Persistent systemd journal data |

### journalctl

```bash
journalctl -xe
journalctl --since "24 hours ago"
journalctl -u SERVICE
journalctl -p warning
```

### Authentication Log Review

```bash
grep -E "Accepted|Failed|Invalid user|sudo" /var/log/auth.log
```

---

## 16. Quick Enumeration Sequence

A basic sequence for initial host assessment:

```bash
# Identity
whoami
id
sudo -l

# Operating system
uname -a
cat /etc/os-release

# Users and groups
getent passwd
getent group

# Network
ip addr
ip route
ss -tulpen

# Processes
ps aux

# Services
systemctl list-units --type=service --all

# Scheduled tasks
cat /etc/crontab
systemctl list-timers --all

# SUID and SGID
find / -type f -perm -4000 -ls 2>/dev/null
find / -type f -perm -2000 -ls 2>/dev/null

# Capabilities
getcap -r / 2>/dev/null

# Writable directories
find / -type d -writable -ls 2>/dev/null
```

This sequence is a starting point, not a complete assessment.

---

## 17. Operational Considerations

- Confirm scope before scanning or monitoring.
- Prefer read-only enumeration.
- Avoid commands that modify permissions or system configuration.
- Treat process arguments and configuration output as potentially sensitive.
- Avoid copying credentials into reports.
- Consider system performance when running recursive filesystem searches.
- Document commands, timestamps and relevant output.
- Validate automated tool findings manually.
- Coordinate intrusive testing with system owners.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
