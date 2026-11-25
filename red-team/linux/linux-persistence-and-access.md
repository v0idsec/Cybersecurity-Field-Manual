# Linux Persistence and Access Mechanisms

Linux systems provide several legitimate mechanisms for maintaining access across sessions and reboots. These include user accounts, SSH authentication, scheduled tasks and service configuration.

During an assessment, these mechanisms should be reviewed for unauthorised changes, excessive privileges and insecure access controls.

This guide focuses on identifying and auditing persistence mechanisms, rather than establishing covert access.

## 1. Local Account Persistence

Review local accounts:

```bash
cat /etc/passwd
```

Identify UID 0 accounts:

```bash
awk -F: '$3 == 0 {print $1}' /etc/passwd
```

Review account status:

```bash
sudo passwd -S username
sudo chage -l username
```

Investigate:

- Unexpected accounts.
- Accounts created outside approved processes.
- Accounts with administrative group membership.
- Service accounts with interactive shells.
- Accounts with unusual password or expiry settings.

## 2. SSH Authentication

Review SSH configuration:

```bash
sudo sshd -T
```

Inspect the configuration files:

```bash
sudo cat /etc/ssh/sshd_config
sudo ls -lah /etc/ssh/sshd_config.d/
```

Important settings include:

| Setting | Security consideration |
|---|---|
| `PermitRootLogin` | Controls direct root login |
| `PasswordAuthentication` | Controls password-based authentication |
| `PubkeyAuthentication` | Controls public key authentication |
| `AllowUsers` | Restricts permitted login accounts |
| `AllowGroups` | Restricts permitted login groups |
| `AuthorizedKeysFile` | Defines authorised public key locations |
| `MaxAuthTries` | Limits authentication attempts |

Evaluate the effective configuration, including included configuration files and distribution defaults.

## 3. SSH Authorised Keys

Review authorised key files:

```bash
find /home -name authorized_keys -type f -ls 2>/dev/null
```

Common locations:

```text
~/.ssh/authorized_keys
/etc/ssh/authorized_keys/
```

Inspect file permissions:

```bash
ls -lah ~/.ssh/
stat ~/.ssh/authorized_keys
```

Investigate:

- Unknown public keys.
- Keys associated with departed personnel.
- Unexpected key options.
- Insecure ownership or permissions.
- Keys permitting access beyond intended accounts.

Public keys are not private credentials, but their presence can still reveal unauthorised access.

## 4. SSH Private Key Exposure

Identify potentially sensitive SSH files:

```bash
find /home /root -type f \( -name "id_rsa" -o -name "id_ed25519" -o -name "id_ecdsa" \) -ls 2>/dev/null
```

Review permissions and ownership without unnecessarily copying private key material.

Private keys should:

- Be protected by restrictive filesystem permissions.
- Use passphrases where appropriate.
- Be rotated when exposure is suspected.
- Be removed when no longer required.

## 5. Cron-Based Persistence Auditing

Review scheduled tasks:

```bash
cat /etc/crontab
ls -lah /etc/cron.d/
```

Inspect user crontabs where authorised:

```bash
crontab -l
```

Investigate unexpected entries, especially those that:

- Execute scripts from writable directories.
- Run with elevated privileges.
- Download or execute external content.
- Have unexplained schedules.
- Reference unknown executables.

## 6. Systemd Persistence Auditing

Review enabled services:

```bash
systemctl list-unit-files --state=enabled
```

Review active services:

```bash
systemctl list-units --type=service --state=running
```

Review timers:

```bash
systemctl list-timers --all
```

Inspect unfamiliar units:

```bash
systemctl cat service-name
systemctl status service-name
```

Investigate unexpected service definitions, executable paths and ownership.

## 7. Shell Initialisation Files

Shell initialisation files execute commands when users start particular shell sessions.

Common locations include:

```text
/etc/profile
/etc/bash.bashrc
/etc/profile.d/
/etc/zsh/
/home/USER/.profile
/home/USER/.bashrc
/home/USER/.bash_profile
```

Review relevant files:

```bash
ls -lah /etc/profile.d/
```

Look for unexpected commands, unfamiliar environment configuration and modifications that are inconsistent with approved administration.

## 8. Other Execution Mechanisms

Depending on the distribution and environment, investigate:

- `at` scheduled jobs.
- User-level systemd services.
- System-wide systemd units.
- Init scripts.
- Application startup scripts.
- Desktop autostart entries.
- Configuration management agents.
- Package manager hooks.
- Container restart policies.

Do not assume every unfamiliar scheduled task or service is malicious. Compare findings against known system and application baselines.

## 9. Log and Audit Review

Review authentication events:

Debian-based systems:

```bash
grep -E "Accepted|Failed|Invalid user|sudo" /var/log/auth.log
```

RHEL-based systems:

```bash
grep -E "Accepted|Failed|Invalid user|sudo" /var/log/secure
```

Review systemd journal:

```bash
journalctl -u ssh
journalctl --since "24 hours ago"
```

Look for:

- Unexpected successful logins.
- Repeated authentication failures.
- New account activity.
- Changes to SSH configuration.
- Unusual service execution.
- Unexpected privileged command execution.

Log locations and service names vary by distribution.

## 10. Defensive Recommendations

- Enforce centralised account lifecycle management.
- Remove obsolete accounts and SSH keys.
- Restrict SSH access to approved users and groups.
- Disable unnecessary authentication methods.
- Protect private keys.
- Monitor changes to scheduled tasks.
- Audit systemd services and timers.
- Restrict write access to startup files.
- Centralise authentication and system logs.
- Establish a baseline of approved services and accounts.

## 11. Assessment Checklist

- [ ] Local accounts reviewed.
- [ ] UID 0 accounts checked.
- [ ] SSH effective configuration reviewed.
- [ ] Authorised keys inventoried.
- [ ] Private key exposure assessed.
- [ ] Cron jobs reviewed.
- [ ] Systemd services and timers reviewed.
- [ ] Shell initialisation files assessed.
- [ ] Other startup mechanisms considered.
- [ ] Authentication logs reviewed.
- [ ] Unauthorised access mechanisms documented.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
