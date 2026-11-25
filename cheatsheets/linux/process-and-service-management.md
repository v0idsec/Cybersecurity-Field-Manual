# Linux Process and Service Management

## Process inspection

| Command | Description |
|---|---|
| `ps aux` | List running processes |
| `ps -ef` | Full process listing |
| `ps auxf` | Process tree |
| `top` | Interactive process monitor |
| `htop` | Enhanced process monitor |
| `pgrep name` | Find process by name |
| `pidof name` | Find process ID |
| `pstree` | Display process hierarchy |
| `lsof` | List open files |
| `lsof -i` | Network-related open files |

## Process filtering

```bash
# Search process list
ps aux | grep nginx

# Find process by name
pgrep -a nginx

# Display process tree
pstree -p

# Show process details
ps -p PID -o pid,ppid,user,%cpu,%mem,cmd

# List processes owned by a user
ps -u username
```

## Process control

```bash
# Send SIGTERM
kill PID

# Send SIGKILL
kill -9 PID

# Send SIGHUP
kill -HUP PID

# Terminate by process name
pkill processname

# Interactive process termination
killall processname

# Run process in background
command &

# Show background jobs
jobs

# Resume suspended job in background
bg

# Resume job in foreground
fg
```

Use SIGKILL only when normal termination fails. It does not allow the process to clean up resources.

## Process priority

```bash
# Start with adjusted priority
nice -n 10 command

# Change priority of running process
renice 10 -p PID

# View process priorities
ps -eo pid,ni,pri,cmd
```

Lower nice values generally indicate higher scheduling priority.

## systemd services

| Command | Description |
|---|---|
| `systemctl status service` | Service status |
| `systemctl start service` | Start service |
| `systemctl stop service` | Stop service |
| `systemctl restart service` | Restart service |
| `systemctl reload service` | Reload configuration |
| `systemctl enable service` | Enable at boot |
| `systemctl disable service` | Disable at boot |
| `systemctl is-active service` | Check active state |
| `systemctl is-enabled service` | Check boot enablement |
| `systemctl list-units` | List loaded units |
| `systemctl --failed` | List failed units |

## Service investigation

```bash
# List running services
systemctl --type=service --state=running

# List enabled services
systemctl list-unit-files --type=service --state=enabled

# List failed services
systemctl --failed

# Review service dependencies
systemctl list-dependencies service

# Review service configuration
systemctl cat service

# Show service properties
systemctl show service
```

## Scheduled tasks

### Cron

```bash
# Current user's crontab
crontab -l

# Edit current user's crontab
crontab -e

# Root crontab
sudo crontab -l

# System-wide cron configuration
cat /etc/crontab

# Review cron directories
ls -la /etc/cron.*
```

Cron syntax:

```text
* * * * * command
| | | | |
| | | | +--- Day of week
| | | +----- Month
| | +------- Day of month
| +--------- Hour
+----------- Minute
```

Examples:

```cron
# Every day at midnight
0 0 * * * /path/to/script.sh

# Every 15 minutes
*/15 * * * * /path/to/script.sh

# Every Monday at 09:00
0 9 * * 1 /path/to/script.sh
```

### systemd timers

```bash
# List timers
systemctl list-timers

# Inspect timer
systemctl status timer-name.timer

# Inspect timer unit
systemctl cat timer-name.timer
```

## Resource monitoring

```bash
# CPU and memory usage
top

# Memory summary
free -h

# Disk usage
df -h

# Directory size
du -sh /path

# System load
uptime

# I/O statistics
iostat

# Virtual memory statistics
vmstat

# Open files
lsof

# Processes using most CPU
ps aux --sort=-%cpu | head

# Processes using most memory
ps aux --sort=-%mem | head
```

## Investigation considerations

When investigating an unknown process, review:

- Executable path.
- Parent process.
- Effective user.
- Command-line arguments.
- Open files.
- Network connections.
- Start time.
- Associated service or scheduled task.
- File hash and signature where available.

Do not terminate suspicious processes before considering evidence preservation and incident response requirements.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
