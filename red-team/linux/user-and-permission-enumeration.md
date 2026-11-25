# Linux User and Permission Enumeration

User and permission enumeration identifies accounts, group memberships, file ownership, access controls and privilege boundaries.

The objective is to identify excessive permissions, insecure configurations and unintended access paths.

## 1. Current User Context

```bash
whoami
id
groups
```

Review:

- Current username and UID.
- Primary and supplementary groups.
- Administrative group membership.
- Service account context.

Check whether the current user has elevated privileges:

```bash
sudo -l
```

Do not assume group membership automatically grants access. Confirm the effective permissions and applicable configuration.

## 2. Local User Enumeration

Review local accounts:

```bash
cat /etc/passwd
```

Display usernames only:

```bash
cut -d: -f1 /etc/passwd
```

Review account identifiers and shells:

```bash
awk -F: '{print $1, $3, $6, $7}' /etc/passwd
```

Investigate:

- Unexpected accounts.
- UID 0 accounts other than root.
- Service accounts with interactive shells.
- Accounts with unusual home directories.
- Accounts that should have been disabled.

Identify accounts with UID 0:

```bash
awk -F: '$3 == 0 {print $1}' /etc/passwd
```

## 3. Group Enumeration

Review group definitions:

```bash
cat /etc/group
```

Inspect a specific group:

```bash
getent group sudo
getent group wheel
getent group docker
```

Commonly relevant groups include:

| Group | Security relevance |
|---|---|
| `sudo` | Administrative command execution on many Debian-based systems |
| `wheel` | Administrative privileges on many Red Hat-based systems |
| `docker` | Access to the Docker daemon may provide host-level control |
| `lxd` | Membership can grant powerful container-management capabilities |
| `disk` | May provide direct access to block devices |
| `adm` | May provide access to system logs |
| `shadow` | May provide access to password hashes |

Group names and privileges vary between distributions. Verify the actual configuration.

## 4. File Ownership and Permissions

Linux permissions are represented by:

- Owner permissions.
- Group permissions.
- Other permissions.

Example:

```text
-rwxr-xr--
```

This represents:

- Owner: read, write and execute.
- Group: read and execute.
- Other: read only.

Inspect permissions:

```bash
ls -lah
stat /path/to/file
```

Inspect recursively:

```bash
ls -lahR /path/to/directory
```

Review ownership:

```bash
find /path/to/directory -printf '%u:%g %m %p\n'
```

Look for:

- Sensitive files readable by unnecessary users.
- Executables writable by untrusted users.
- Configuration files with excessive permissions.
- Unexpected ownership of privileged scripts.
- Writable directories used by privileged services.

## 5. SUID and SGID

SUID executables run with the effective user ID of the file owner.

SGID executables run with the effective group ID of the file owner. SGID directories can also cause new files to inherit the directory's group.

Find SUID files:

```bash
find / -type f -perm -4000 -ls 2>/dev/null
```

Find SGID files:

```bash
find / -type f -perm -2000 -ls 2>/dev/null
```

Review each result for:

- Expected ownership.
- Package provenance.
- Whether the binary requires elevated privileges.
- Whether the executable is writable.
- Known security implications.

Do not assume every SUID or SGID binary is vulnerable.

## 6. Linux Capabilities

Capabilities divide traditional root privileges into smaller units.

Inspect capabilities:

```bash
getcap -r / 2>/dev/null
```

Particularly important capabilities include:

| Capability | Security relevance |
|---|---|
| `CAP_SETUID` | Can allow changing process UID |
| `CAP_SETGID` | Can allow changing process GID |
| `CAP_DAC_OVERRIDE` | Can bypass some discretionary file permission checks |
| `CAP_DAC_READ_SEARCH` | Can bypass certain file read and directory search permissions |
| `CAP_SYS_ADMIN` | Broad administrative capability |
| `CAP_NET_RAW` | Allows raw and packet socket operations |
| `CAP_SYS_PTRACE` | Allows process tracing operations |

Review whether capabilities are necessary and appropriately scoped.

## 7. ACL Enumeration

Access Control Lists provide permissions beyond standard owner, group and other permissions.

Inspect ACLs:

```bash
getfacl /path/to/file
getfacl -R /path/to/directory
```

Review:

- Additional named users.
- Additional named groups.
- Default directory ACLs.
- Unexpected write permissions.
- ACL masks that restrict or modify effective permissions.

Modify ACLs only when authorised and required by the engagement.

## 8. Writable Locations

Find world-writable directories:

```bash
find / -type d -perm -0002 -ls 2>/dev/null
```

Find files writable by the current user:

```bash
find / -type f -writable -ls 2>/dev/null
```

Review important locations:

```bash
ls -ld /tmp /var/tmp /dev/shm
```

Check mount options:

```bash
findmnt -o TARGET,OPTIONS
```

Look for writable directories used by:

- Root-owned scripts.
- Scheduled jobs.
- Application services.
- Executable search paths.
- Deployment processes.

## 9. Password and Account Configuration

Review password policy configuration:

```bash
cat /etc/login.defs
```

Review account ageing information:

```bash
sudo chage -l username
```

Check account status:

```bash
sudo passwd -S username
```

Access to `/etc/shadow` should be restricted. Do not copy password hashes into assessment notes unless explicitly required and approved.

## 10. Assessment Checklist

- [ ] Current user and group memberships recorded.
- [ ] Local accounts reviewed.
- [ ] UID 0 accounts checked.
- [ ] Administrative groups reviewed.
- [ ] File ownership and permissions assessed.
- [ ] SUID and SGID binaries reviewed.
- [ ] Linux capabilities enumerated.
- [ ] ACLs reviewed.
- [ ] Writable directories assessed.
- [ ] Account policy configuration reviewed.
- [ ] Findings supported by evidence.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
