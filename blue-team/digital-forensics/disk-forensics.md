# Disk Forensics

## Overview

Disk forensics examines storage media to identify files, system activity, user activity, malware, deleted data and other relevant artefacts.

Common evidence sources include:

- Hard disk drives
- Solid-state drives
- USB storage
- Memory cards
- Virtual disk images
- RAID volumes
- Forensic disk images

## Disk Structure

A storage device may contain:

- Partition tables
- Partitions
- File systems
- Boot records
- Files and directories
- Metadata
- Unallocated space
- File-system journals

Understanding the storage layout is essential before interpreting artefacts.

## Partition Tables

Common partitioning schemes:

| Scheme | Description |
|---|---|
| MBR | Legacy Master Boot Record |
| GPT | GUID Partition Table |

Inspect a Linux device:

```bash
sudo fdisk -l
```

Inspect partitions:

```bash
lsblk -f
```

## File Systems

Common file systems:

| File system | Common environment |
|---|---|
| NTFS | Windows |
| FAT32 | Removable media |
| exFAT | Removable media |
| ext4 | Linux |
| XFS | Linux |
| APFS | macOS |
| HFS+ | Older macOS |

Each file system stores metadata differently.

## NTFS Artefacts

Important NTFS structures include:

- Master File Table (MFT)
- `$LogFile`
- `$UsnJrnl`
- `$Recycle.Bin`
- Alternate Data Streams
- Volume Shadow Copies
- NTFS timestamps

### Master File Table

The MFT contains records describing files and directories.

Potential information:
- File names
- File metadata
- File references
- Timestamps
- Data attributes

### USN Journal

The USN Journal records file-system change events.

It can assist with identifying:
- File creation
- File deletion
- File renaming
- File modification
- Directory changes

The journal is not a complete record of every action and may be truncated or unavailable.

### Alternate Data Streams

NTFS supports named data streams.

Inspect a file's streams:

```powershell
Get-Item .\example.txt -Stream *
```

An attacker may abuse alternate data streams to hide information, but their presence is not inherently malicious.

## Linux File-System Artefacts

Potential evidence sources:

- Inode metadata
- Directory entries
- Journal records
- File permissions
- Extended attributes
- Shell history
- System logs
- Application data

Useful commands:

```bash
stat suspicious-file
```

```bash
ls -la
```

```bash
find /path/to/evidence -type f -printf '%TY-%Tm-%Td %TH:%TM %p\n'
```

Run commands against forensic copies or mounted images using an appropriate read-only workflow.

## Deleted File Recovery

Deleted files may remain recoverable if their underlying data has not been overwritten.

Recovery depends on:
- File-system design
- Storage type
- TRIM
- Encryption
- Data overwriting
- File fragmentation
- Acquisition completeness

Do not assume deleted files are recoverable.

## Timeline Analysis

A disk timeline can help reconstruct activity.

Relevant timestamps may include:
- File creation
- Modification
- Access
- Metadata changes
- Journal events
- Application records

Be aware that timestamp semantics differ between file systems.

Windows NTFS commonly stores timestamps in UTC-based FILETIME representations, while Linux file systems commonly use Unix timestamps.

## File Hashing

Calculate hashes to identify known files or verify evidence.

```bash
sha256sum suspicious-file
```

PowerShell:

```powershell
Get-FileHash .\suspicious-file -Algorithm SHA256
```

Compare hashes against trusted reference datasets where available.

## File Type Identification

Do not rely exclusively on file extensions.

Linux:

```bash
file suspicious-file
```

PowerShell:

```powershell
Format-Hex .\suspicious-file | Select-Object -First 10
```

File signatures can help identify files whose extensions do not match their actual content.

## Useful Forensic Tools

| Tool | Purpose |
|---|---|
| Autopsy | Graphical digital forensic analysis |
| The Sleuth Kit | File-system and disk-image analysis |
| FTK Imager | Evidence acquisition and image examination |
| X-Ways Forensics | Commercial forensic examination |
| Arsenal Image Mounter | Mounting forensic images |
| bulk_extractor | Extracting features from forensic images |
| PhotoRec | File carving and recovery |
| Foremost | File carving |

## Examination Workflow

1. Confirm evidence ID and hash.
2. Identify image format.
3. Determine partition layout.
4. Identify file systems.
5. Examine relevant directories.
6. Identify suspicious files.
7. Review file metadata.
8. Examine deleted data where appropriate.
9. Build a timeline.
10. Correlate findings with other evidence.
11. Document conclusions and limitations.

## Common Mistakes

- Mounting original evidence read-write.
- Assuming file extensions prove file type.
- Treating file timestamps as definitive.
- Ignoring file-system journals.
- Assuming deleted files are recoverable.
- Ignoring SSD TRIM behaviour.
- Failing to account for encryption.
- Making conclusions from a single artefact.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
