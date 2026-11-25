# Linux Reconnaissance

Linux reconnaissance involves identifying the operating system, system configuration, network interfaces, running services and accessible resources.

The objective is to establish an accurate picture of the target before investigating potential weaknesses.

## 1. Operating System Identification

### Kernel Information

```bash
uname -a
uname -r
uname -m
```

Useful information:

- Kernel version.
- Architecture.
- Hostname.
- Operating system identification.
- Kernel build information.

### Distribution Information

```bash
cat /etc/os-release
cat /etc/issue
hostnamectl
```

Identify:

- Distribution and version.
- Release information.
- System architecture.
- Virtualisation environment.

### Kernel Version Assessment

```bash
uname -r
cat /proc/version
```

Kernel versions can help identify potentially relevant vulnerabilities.

Do not assume an outdated-looking kernel is vulnerable. Distribution maintainers frequently backport security fixes.

## 2. System Information

```bash
hostname
uptime
date
whoami
id
```

Review system information:

```bash
lscpu
free -h
lsblk
df -h
mount
```

## 3. User Enumeration

```bash
who
w
users
id
groups
```

Review local accounts:

```bash
cat /etc/passwd
```

Review password database permissions:

```bash
ls -l /etc/passwd /etc/shadow
```

Investigate:

- Unexpected accounts.
- Service accounts with interactive shells.
- Unusual account identifiers.
- Unexpected home directories.
- Accounts with unnecessary privileges.

## 4. Network Enumeration

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

### DNS Configuration

```bash
cat /etc/resolv.conf
cat /etc/hosts
```

### Listening Services

```bash
ss -tulpen
```

Alternative:

```bash
netstat -tulpen
```

Review:

- Listening ports.
- Bound interfaces.
- Process ownership.
- Internal-only services.
- Unexpected exposed services.

## 5. Process Enumeration

```bash
ps aux
ps -ef
top
```

Review process ownership:

```bash
ps -eo user,pid,ppid,cmd
```

Identify:

- Services running as root.
- Unexpected processes.
- Applications running under service accounts.
- Unusual parent-child relationships.

## 6. Filesystem Enumeration

```bash
ls -lah /
ls -lah /home
ls -lah /tmp
ls -lah /var/tmp
ls -lah /opt
ls -lah /var/www
```

Review mounted filesystems:

```bash
findmnt
mount
```

Identify:

- Writable directories.
- Unusual mount options.
- Shared storage.
- Application directories.
- Sensitive configuration locations.

## 7. Installed Software

### Debian / Ubuntu

```bash
dpkg -l
apt list --installed
```

### Red Hat / Fedora

```bash
rpm -qa
dnf list installed
```

### Alpine

```bash
apk list --installed
```

Review software versions against vendor security advisories.

## 8. Security Controls

Check firewall status:

```bash
sudo ufw status verbose
sudo nft list ruleset
sudo iptables -L -n -v
```

Check security modules:

```bash
getenforce
sestatus
aa-status
```

Some commands may not be installed or accessible.

## 9. Virtualisation and Container Indicators

```bash
systemd-detect-virt
```

Review:

```bash
cat /proc/1/cgroup
ls -la /.dockerenv
```

These indicators can help identify virtualised or containerised environments, but should not be treated as definitive individually.

## 10. Evidence Collection

Record:

- Hostname.
- IP addresses.
- Distribution and version.
- Kernel version.
- User context.
- Running services.
- Listening ports.
- Relevant security controls.

Avoid collecting unnecessary sensitive information.

## Assessment Checklist

- [ ] Operating system identified.
- [ ] Kernel version recorded.
- [ ] Hostname and architecture recorded.
- [ ] User context identified.
- [ ] Network interfaces reviewed.
- [ ] Routing and DNS reviewed.
- [ ] Listening services enumerated.
- [ ] Running processes reviewed.
- [ ] Installed software reviewed.
- [ ] Security controls identified.
- [ ] Evidence securely retained.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
