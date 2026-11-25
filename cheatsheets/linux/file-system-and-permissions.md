# Linux Filesystem and Permissions

## Filesystem navigation

| Path | Purpose |
|---|---|
| `/` | Filesystem root |
| `/home` | User home directories |
| `/root` | Root user's home directory |
| `/etc` | System configuration |
| `/var` | Variable data and logs |
| `/var/log` | System and application logs |
| `/tmp` | Temporary files |
| `/opt` | Optional third-party software |
| `/usr` | Userland applications and libraries |
| `/bin` | Essential user commands |
| `/sbin` | System administration commands |
| `/dev` | Device files |
| `/proc` | Process and kernel information |
| `/sys` | Kernel and device information |
| `/mnt` | Temporary mount points |
| `/media` | Removable media mount points |

## Permission notation

Linux permissions are represented by three categories:

- User (owner).
- Group.
- Other.

| Permission | Symbol | Numeric value |
|---|---|---:|
| Read | `r` | 4 |
| Write | `w` | 2 |
| Execute | `x` | 1 |
| None | `-` | 0 |

Example:

```text
-rwxr-xr--
```

| Category | Permissions | Numeric |
|---|---|---:|
| Owner | rwx | 7 |
| Group | r-x | 5 |
| Other | r-- | 4 |

Result: `754`

## chmod

```bash
# Set permissions numerically
chmod 755 script.sh

# Owner full access, group read, other none
chmod 740 file.txt

# Remove write permission for others
chmod o-w file.txt

# Add execute permission for owner
chmod u+x script.sh

# Apply recursively
chmod -R 755 directory/

# Set permissions using symbolic notation
chmod u=rw,g=r,o= file.txt
```

## chown and chgrp

```bash
# Change owner
sudo chown user file.txt

# Change owner and group
sudo chown user:group file.txt

# Change group
sudo chgrp group file.txt

# Recursive ownership change
sudo chown -R user:group directory/
```

Use recursive ownership and permission changes carefully. They can break applications or expose sensitive files.

## Special permissions

| Permission | Numeric | Purpose |
|---|---:|---|
| SUID | 4000 | Execute with file owner's effective privileges |
| SGID | 2000 | Execute with file group's effective privileges; directories inherit group |
| Sticky bit | 1000 | Restricts deletion within shared directories |

Examples:

```bash
# Find SUID files
find / -type f -perm -4000 2>/dev/null

# Find SGID files
find / -type f -perm -2000 2>/dev/null

# Set SUID
chmod u+s file

# Set SGID
chmod g+s directory

# Set sticky bit
chmod +t directory
```

## File permissions investigation

```bash
# Detailed permissions
ls -l

# Metadata
stat file.txt

# Identify ownership
ls -ld directory/

# Find world-writable files
find / -type f -perm -0002 2>/dev/null

# Find world-writable directories
find / -type d -perm -0002 2>/dev/null

# Find files owned by a specific user
find / -user username 2>/dev/null

# Find files with no valid owner
find / -nouser -o -nogroup 2>/dev/null
```

## ACLs

Access Control Lists provide more granular permissions than standard owner/group/other permissions.

```bash
# View ACL
getfacl file.txt

# Grant user read/write
setfacl -m u:username:rw file.txt

# Grant group read
setfacl -m g:groupname:r file.txt

# Remove user ACL
setfacl -x u:username file.txt

# Remove all extended ACL entries
setfacl -b file.txt
```

## Mounts and filesystems

```bash
# Display mounted filesystems
mount

# Show filesystem usage
df -h

# Show block devices
lsblk -f

# Show mount configuration
cat /etc/fstab

# Show mount options
findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS
```

Security considerations:

- Review unnecessary executable mounts.
- Consider `nodev`, `nosuid` and `noexec` where appropriate.
- Restrict access to sensitive mount points.
- Ensure removable media policies are enforced.
- Protect backup and temporary storage.

Mount options must be assessed against application requirements.

## Symbolic and hard links

```bash
# Create symbolic link
ln -s /path/to/target linkname

# Create hard link
ln /path/to/file linkname

# Display link target
readlink linkname

# Resolve full path
readlink -f linkname
```

## File capabilities

Capabilities can grant specific privileged operations without requiring full root privileges.

```bash
# List file capabilities
getcap -r / 2>/dev/null

# Inspect a specific binary
getcap /path/to/binary

# Remove capabilities
sudo setcap -r /path/to/binary
```

Investigate unexpected capabilities, particularly on binaries that can affect networking, process control or system configuration.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
