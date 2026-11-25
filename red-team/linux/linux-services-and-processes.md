# Linux Services and Processes

Linux services and processes are common sources of security exposure. Misconfigured service permissions, insecure scheduled tasks and poorly protected sockets can create opportunities for unauthorised access or privilege escalation.

This guide covers service enumeration, process analysis and configuration assessment.

## 1. Process Enumeration

List running processes:

```bash
ps aux
ps -ef
```

Display process ownership and relationships:

```bash
ps -eo user,pid,ppid,stat,cmd
```

Inspect a specific process:

```bash
ps -fp PID
```

Review:

- Process owner.
- Parent process.
- Executable path.
- Command-line arguments.
- Runtime privileges.
- Unexpected child processes.

Command-line arguments can contain sensitive information. Avoid copying secrets into assessment reports.

## 2. Process Monitoring

Monitor processes:

```bash
top
```

Where installed:

```bash
htop
```

Inspect process details:

```bash
cat /proc/PID/status
cat /proc/PID/cmdline
readlink -f /proc/PID/exe
```

Access to process information may be restricted by system configuration.

## 3. Systemd Services

List active services:

```bash
systemctl list-units --type=service
```

List all installed service units:

```bash
systemctl list-unit-files --type=service
```

Inspect a service:

```bash
systemctl status service-name
systemctl cat service-name
```

Review:

- Service user and group.
- Executable path.
- Startup dependencies.
- Environment configuration.
- Writable configuration files.
- Restart behaviour.
- Privilege restrictions.

## 4. Systemd Service Files

Common locations:

```text
/etc/systemd/system/
/usr/lib/systemd/system/
/lib/systemd/system/
```

Review service definitions for:

- `User=`
- `Group=`
- `ExecStart=`
- `ExecStartPre=`
- `Environment=`
- `EnvironmentFile=`
- `WorkingDirectory=`
- `NoNewPrivileges=`
- `PrivateTmp=`
- `ProtectSystem=`
- `ProtectHome=`

A service running as root is not automatically vulnerable. Assess the privileges it genuinely requires and the trustworthiness of its executable and dependencies.

## 5. Cron Jobs

Review system-wide cron configuration:

```bash
cat /etc/crontab
ls -lah /etc/cron.d/
```

Review scheduled task directories:

```bash
ls -lah /etc/cron.hourly/
ls -lah /etc/cron.daily/
ls -lah /etc/cron.weekly/
ls -lah /etc/cron.monthly/
```

Review the current user's crontab:

```bash
crontab -l
```

Review other users' crontabs only where authorised.

Investigate:

- Scripts executed as root.
- Writable scripts.
- Writable parent directories.
- Unsafe executable paths.
- Unquoted variables.
- Sensitive arguments.
- Unexpected scheduled tasks.

## 6. Systemd Timers

List timers:

```bash
systemctl list-timers --all
```

Inspect a timer:

```bash
systemctl status timer-name.timer
systemctl cat timer-name.timer
```

Identify the associated service:

```bash
systemctl cat service-name.service
```

Review timer execution privileges and the permissions of all referenced files.

## 7. Network Services

List listening sockets:

```bash
ss -tulpen
```

List TCP connections:

```bash
ss -antp
```

List UDP sockets:

```bash
ss -aunp
```

Identify processes using network ports:

```bash
sudo lsof -i -P -n
```

Review:

- Services bound to all interfaces.
- Internal services exposed externally.
- Unnecessary listeners.
- Unexpected high ports.
- Services running with excessive privileges.

## 8. Unix Domain Sockets

List Unix sockets:

```bash
ss -lx
```

Alternative:

```bash
find /run /var/run -type s -ls 2>/dev/null
```

Investigate:

- Docker and container runtime sockets.
- Database sockets.
- Application control sockets.
- Service management interfaces.
- Socket permissions and ownership.

A socket may expose powerful functionality even when no TCP port is open.

## 9. Open Files

List open files:

```bash
lsof
```

Inspect a process:

```bash
lsof -p PID
```

Review network files:

```bash
lsof -i
```

Look for:

- Sensitive files opened by services.
- Unexpected log locations.
- Temporary files.
- Deleted files still held open.
- Unusual network connections.

## 10. Service Hardening

Defensive measures include:

- Run services as dedicated, unprivileged users.
- Restrict filesystem access.
- Remove unnecessary capabilities.
- Use systemd sandboxing where appropriate.
- Restrict network exposure.
- Protect service configuration.
- Validate service dependencies.
- Monitor changes to unit files.
- Remove unused services.

## 11. Assessment Checklist

- [ ] Running processes enumerated.
- [ ] Process ownership reviewed.
- [ ] Privileged processes investigated.
- [ ] Systemd services reviewed.
- [ ] Service unit files inspected.
- [ ] Cron jobs reviewed.
- [ ] Systemd timers reviewed.
- [ ] Listening network services identified.
- [ ] Unix sockets reviewed.
- [ ] Open files assessed.
- [ ] Service hardening recommendations documented.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
