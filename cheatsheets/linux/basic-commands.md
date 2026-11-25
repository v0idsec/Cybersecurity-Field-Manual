# Linux Basic Commands

## Navigation

| Command | Description |
|---|---|
| `pwd` | Print current working directory |
| `ls` | List directory contents |
| `ls -la` | List all files with details |
| `ls -lh` | Human-readable file sizes |
| `cd /path` | Change directory |
| `cd ..` | Move up one directory |
| `cd ~` | Return to home directory |
| `cd -` | Return to previous directory |
| `tree` | Display directory structure |

## File operations

| Command | Description |
|---|---|
| `touch file` | Create an empty file |
| `mkdir directory` | Create directory |
| `mkdir -p a/b/c` | Create nested directories |
| `cp source destination` | Copy file |
| `cp -r source destination` | Copy directory recursively |
| `mv source destination` | Move or rename |
| `rm file` | Remove file |
| `rm -r directory` | Remove directory recursively |
| `file filename` | Identify file type |
| `stat filename` | Display file metadata |

Be careful with recursive deletion commands, particularly when using elevated privileges.

## Reading files

| Command | Description |
|---|---|
| `cat file` | Display entire file |
| `less file` | View file interactively |
| `more file` | Paginated file viewing |
| `head file` | First 10 lines |
| `head -n 20 file` | First 20 lines |
| `tail file` | Last 10 lines |
| `tail -n 50 file` | Last 50 lines |
| `tail -f file` | Follow file updates |
| `nl -ba file` | Display numbered lines |

## Searching

```bash
# Find files by name
find /path -name "filename"

# Find files by extension
find /path -type f -name "*.log"

# Search file contents
grep "pattern" file

# Case-insensitive search
grep -i "pattern" file

# Recursive search
grep -R "pattern" /path

# Show matching line numbers
grep -n "pattern" file

# Search using extended regular expressions
grep -E "error|failed|denied" file

# Find recently modified files
find /var/log -type f -mmin -60
```

## Text processing

| Command | Description |
|---|---|
| `sort file` | Sort lines |
| `sort -u file` | Sort and remove duplicates |
| `uniq file` | Remove adjacent duplicate lines |
| `wc -l file` | Count lines |
| `wc -w file` | Count words |
| `cut -d: -f1 file` | Extract first colon-separated field |
| `awk '{print $1}' file` | Print first field |
| `sed 's/old/new/g' file` | Replace text in output |
| `tr 'a-z' 'A-Z'` | Convert lowercase to uppercase |
| `tee output.txt` | Write output to file and stdout |

## Archives and compression

```bash
# Create tar archive
tar -cvf archive.tar directory/

# Extract tar archive
tar -xvf archive.tar

# Create compressed tar archive
tar -czvf archive.tar.gz directory/

# Extract compressed tar archive
tar -xzvf archive.tar.gz

# List archive contents
tar -tzvf archive.tar.gz

# Compress with gzip
gzip file

# Decompress gzip
gunzip file

# Zip directory
zip -r archive.zip directory/

# Extract ZIP
unzip archive.zip
```

## System information

| Command | Description |
|---|---|
| `uname -a` | Kernel and system information |
| `hostname` | System hostname |
| `hostnamectl` | Hostname and operating system details |
| `cat /etc/os-release` | Distribution information |
| `uptime` | System uptime and load |
| `whoami` | Current username |
| `id` | User and group IDs |
| `date` | Current date and time |
| `timedatectl` | Time and synchronisation status |
| `env` | Environment variables |
| `printenv` | Display environment |

## Disk and memory

```bash
# Disk usage by filesystem
df -h

# Directory sizes
du -sh /path/*

# Memory usage
free -h

# Block devices
lsblk

# Disk partitions
sudo fdisk -l

# Mounted filesystems
findmnt

# Inode usage
df -i
```

## Useful command chaining

```bash
# Run second command only if first succeeds
command1 && command2

# Run second command only if first fails
command1 || command2

# Run commands sequentially
command1 ; command2

# Pipe output into another command
command1 | command2

# Redirect standard output
command > output.txt

# Append standard output
command >> output.txt

# Redirect standard error
command 2> error.txt

# Redirect stdout and stderr
command > output.txt 2>&1

# Discard output
command > /dev/null 2>&1
```

## Useful shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl + C` | Interrupt foreground process |
| `Ctrl + Z` | Suspend foreground process |
| `Ctrl + D` | Send EOF / exit shell input |
| `Ctrl + L` | Clear terminal |
| `Ctrl + R` | Search command history |
| `Ctrl + A` | Move to start of line |
| `Ctrl + E` | Move to end of line |
| `Alt + .` | Insert last argument from previous command |

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
