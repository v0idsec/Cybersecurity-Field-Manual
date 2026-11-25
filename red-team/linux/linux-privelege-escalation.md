# Linux Privilege Escalation

Linux privilege escalation assessments identify weaknesses that could allow a user or process to obtain permissions beyond those intended by the system owner.

The objective is to determine whether privilege boundaries are correctly enforced and whether local misconfigurations expose administrative access.

## 1. Methodology

Use a structured process:

1. Establish the current user context.
2. Identify operating system and kernel versions.
3. Review sudo permissions.
4. Enumerate users and groups.
5. Inspect SUID and SGID binaries.
6. Review Linux capabilities.
7. Inspect scheduled tasks and services.
8. Review writable files and directories.
9. Investigate application and container boundaries.
10. Validate suspected weaknesses safely.

Do not jump directly to exploit execution. Many apparent privilege escalation paths are false positives or depend on environmental conditions.

## 2. Initial Enumeration

```bash
whoami
id
hostname
uname -a
cat /etc/os-release
```

Review sudo permissions:

```bash
sudo -l
```

Review running processes:

```bash
ps aux
```

Review listening services:

```bash
ss -tulpen
```

## 3. Automated Enumeration

Automated enumeration tools can identify potential weaknesses and reduce manual effort.

### LinPEAS

Repository:

https://github.com/peass-ng/PEASS-ng

LinPEAS identifies potential privilege escalation vectors, including:

- System configuration weaknesses.
- Interesting files and directories.
- SUID and SGID binaries.
- Linux capabilities.
- Scheduled tasks.
- Installed software.
- Credential exposure indicators.

Review findings manually before treating them as vulnerabilities.

### Linux Smart Enumeration

Repository:

https://github.com/diego-treitos/linux-smart-enumeration

LSE provides structured system enumeration and highlights potentially relevant configuration weaknesses.

### pspy

Repository:

https://github.com/DominicBreuker/pspy

pspy monitors process execution without requiring root privileges.

Useful for identifying:

- Scheduled jobs.
- Periodic scripts.
- Unexpected process execution.
- Service activity.
- Processes that run too briefly to appear in manual snapshots.

Use monitoring tools within the engagement's approved scope and duration.

## 4. Sudo Misconfigurations

Inspect allowed commands:

```bash
sudo -l
```

Review:

- Commands executable as root.
- Wildcard arguments.
- Environment variable handling.
- `NOPASSWD` entries.
- Executables that permit arbitrary file access or command execution.
- Scripts writable by the current user.

A permitted command is not automatically exploitable. Assess its actual functionality and configuration.

## 5. SUID and SGID Weaknesses

Enumerate SUID binaries:

```bash
find / -type f -perm -4000 -ls 2>/dev/null
```

Enumerate SGID binaries:

```bash
find / -type f -perm -2000 -ls 2>/dev/null
```

Review unexpected binaries and compare them with trusted package contents.

Reference:

https://gtfobins.github.io/

GTFOBins documents security-relevant behaviour in common Unix binaries, including file operations, command execution and privilege boundaries.

## 6. Linux Capabilities

Enumerate capabilities:

```bash
getcap -r / 2>/dev/null
```

Pay particular attention to capabilities that can bypass file permissions, alter process identities or provide broad system administration functionality.

Validate whether the capability is:

- Assigned to the correct executable.
- Required for normal operation.
- Available to an untrusted execution context.
- Combined with other weaknesses.

## 7. Scheduled Tasks

Review cron configuration:

```bash
cat /etc/crontab
ls -lah /etc/cron.d
ls -lah /etc/cron.daily
ls -lah /etc/cron.hourly
```

Review user crontabs where authorised:

```bash
crontab -l
```

Inspect systemd timers:

```bash
systemctl list-timers --all
```

Investigate privileged scheduled tasks that execute scripts or binaries writable by lower-privileged users.

## 8. Services and Processes

Review services:

```bash
systemctl list-units --type=service --all
```

Inspect a specific service:

```bash
systemctl cat service-name
systemctl status service-name
```

Investigate:

- Root-owned services.
- Writable service executables.
- Writable configuration files.
- Unsafe environment variables.
- Weak service dependencies.
- Insecure temporary file handling.

## 9. Credential Exposure

Review common configuration locations:

```bash
find /etc /opt /var/www /home -type f -readable 2>/dev/null
```

Look for potential secrets in:

- Application configuration.
- Deployment scripts.
- Backup files.
- Environment files.
- SSH configuration.
- Service definitions.

Do not indiscriminately dump credentials or attempt to reuse discovered secrets. Confirm the authorised scope and document exposure without unnecessary disclosure.

## 10. Kernel Vulnerabilities

Record kernel information:

```bash
uname -r
cat /proc/version
```

Compare findings with:

- Distribution security advisories.
- Vendor CVE information.
- Known affected version ranges.
- Relevant configuration prerequisites.

Kernel exploits can crash systems, corrupt data or destabilise production environments.

Do not execute kernel exploits against production systems without explicit approval and a suitable recovery plan.

## 11. Container Boundaries

Identify possible container environments:

```bash
systemd-detect-virt
cat /proc/1/cgroup
```

Review Docker access:

```bash
docker ps
docker info
```

Assess:

- Privileged containers.
- Host filesystem mounts.
- Exposed container sockets.
- Dangerous capabilities.
- Host namespace sharing.
- Container runtime permissions.

Container breakout testing should be separately authorised.

## 12. Validation and Reporting

A successful privilege escalation finding should establish:

- Initial user context.
- Vulnerable configuration or weakness.
- Required conditions.
- Resulting permission boundary violation.
- Actual security impact.
- Reproducible evidence.

Prefer a harmless proof of access over obtaining or retaining a privileged shell.

Do not modify accounts, install persistence or change system configuration merely to demonstrate impact.

## 13. Assessment Checklist

- [ ] Initial user context established.
- [ ] OS and kernel information recorded.
- [ ] Sudo permissions reviewed.
- [ ] SUID and SGID binaries assessed.
- [ ] Capabilities reviewed.
- [ ] Scheduled tasks inspected.
- [ ] Services and processes reviewed.
- [ ] Writable paths identified.
- [ ] Credential exposure assessed.
- [ ] Kernel vulnerabilities researched.
- [ ] Container boundaries reviewed.
- [ ] Suspected weaknesses safely validated.
- [ ] Evidence and remediation documented.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
