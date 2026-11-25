# Linux User and Privilege Management

## User information

```bash
# Current user
whoami

# User and group IDs
id

# User account information
getent passwd username

# List all users
getent passwd

# List groups
getent group

# Current login sessions
who

# Recent login history
last

# Failed login history (where supported)
sudo lastb
```

## User management

```bash
# Create user
sudo useradd username

# Create user with home directory
sudo useradd -m username

# Create user with specified shell
sudo useradd -m -s /bin/bash username

# Set or change password
sudo passwd username

# Lock account
sudo passwd -l username

# Unlock account
sudo passwd -u username

# Delete user
sudo userdel username

# Delete user and home directory
sudo userdel -r username

# Modify user
sudo usermod -s /bin/bash username
```

## Group management

```bash
# Create group
sudo groupadd groupname

# Add user to supplementary group
sudo usermod -aG groupname username

# Remove user from group
sudo gpasswd -d username groupname

# List user's groups
groups username

# Inspect group
getent group groupname
```

Be careful when changing group membership. The `-a` option in `usermod -aG` preserves existing supplementary groups.

## sudo

```bash
# Execute command as root
sudo command

# Open root shell
sudo -i

# Execute as another user
sudo -u username command

# List current user's sudo permissions
sudo -l

# Validate sudoers syntax
sudo visudo -c

# Edit sudoers safely
sudo visudo
```

Sudoers example:

```text
username ALL=(ALL:ALL) ALL
```

Use the least privilege necessary. Avoid broad unrestricted sudo access where a narrower command or role is sufficient.

## Account investigation

```bash
# Find accounts with UID 0
awk -F: '$3 == 0 {print $1}' /etc/passwd

# Find accounts with interactive shells
grep -E '/(bash|sh|zsh)$' /etc/passwd

# Review password aging
sudo chage -l username

# Review password policy
sudo chage -l username

# Check locked accounts
sudo passwd -S username

# Review sudo group
getent group sudo

# Review wheel group
getent group wheel
```

Group names and account policy mechanisms vary between distributions.

## Authentication files

| File | Purpose |
|---|---|
| `/etc/passwd` | User account metadata |
| `/etc/shadow` | Password hashes and aging data |
| `/etc/group` | Group definitions |
| `/etc/gshadow` | Secure group information |
| `/etc/sudoers` | Sudo policy |
| `/etc/sudoers.d/` | Additional sudo policy |
| `/etc/login.defs` | Login defaults |
| `/etc/security/` | PAM security configuration |

Do not expose or distribute password hashes or authentication secrets.

## SSH authentication review

```bash
# Review SSH configuration
sudo sshd -T

# Review authorised keys
find /home -name authorized_keys -type f -print

# Review SSH host keys
sudo ls -l /etc/ssh/ssh_host_*

# Review recent SSH service logs
sudo journalctl -u ssh
```

## Privilege escalation assessment

For authorised security assessments, review:

- Sudo permissions.
- SUID and SGID binaries.
- File capabilities.
- Writable service files.
- Scheduled tasks.
- PATH configuration.
- Kernel and package versions.
- Credentials and secrets exposed in configuration.
- Group memberships.
- Service account privileges.

Useful commands:

```bash
# Sudo privileges
sudo -l

# SUID binaries
find / -type f -perm -4000 2>/dev/null

# SGID binaries
find / -type f -perm -2000 2>/dev/null

# File capabilities
getcap -r / 2>/dev/null

# Writable files in selected system paths
find /etc /usr/local -type f -writable 2>/dev/null
```

A finding requires context and validation. The presence of a SUID binary or writable file does not automatically mean privilege escalation is possible.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
