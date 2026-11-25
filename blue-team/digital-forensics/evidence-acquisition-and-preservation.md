# Evidence Acquisition and Preservation

## Overview

Evidence acquisition is the process of collecting digital information for examination.

The objective is to preserve relevant information while minimising changes to the original source.

Acquisition methods vary depending on the device, operating system, storage technology, investigation requirements and available authority.

## Acquisition Types

### Physical Acquisition

A physical acquisition captures storage media at a low level, including allocated and unallocated areas where supported.

Common uses:
- Deleted file recovery
- File-system examination
- Partition analysis
- Examination of unallocated space

Physical acquisition may be complicated by:
- Full-disk encryption
- Hardware failures
- SSD TRIM behaviour
- RAID configurations
- Device encryption
- Hardware-backed security

### Logical Acquisition

A logical acquisition collects selected files, directories or application data.

Common uses:
- Targeted incident investigations
- Application data collection
- Configuration review
- Log collection

Limitations:
- May omit deleted data.
- May omit unallocated space.
- May not preserve all file-system metadata.
- May be affected by access permissions.

### Live Acquisition

Live acquisition collects evidence from a running system.

Potential sources:
- RAM
- Running processes
- Active connections
- Mounted volumes
- Logged-in sessions
- Encryption state

Live acquisition changes system state to some degree. Document the tools and commands used.

### Offline Acquisition

Offline acquisition examines storage after the device has been powered down or otherwise isolated.

Advantages:
- Can reduce changes caused by a running operating system.
- May support write-blocked acquisition.

Limitations:
- Volatile evidence is lost.
- Encryption keys may no longer be available.
- Some systems may not be safely powered down.

## Acquisition Planning

Before collection, identify:

- Device make and model
- Device serial number
- Storage type
- Operating system
- Encryption status
- Power state
- Network connectivity
- Physical condition
- Available collection tools
- Destination storage
- Required retention period

Record the device's condition before collection.

## Write Protection

A write blocker prevents or restricts writes to source media during acquisition.

Hardware write blockers are commonly used for removable storage.

Software write protection may be appropriate in controlled environments, but must be validated for the specific workflow.

Do not assume mounting a drive read-only automatically guarantees forensic integrity.

## Forensic Image Formats

Common formats include:

| Format | Description |
|---|---|
| RAW / DD | Raw bit-for-bit image |
| E01 | Expert Witness format |
| AFF4 | Advanced Forensic Format |
| Logical container | Collection of selected files and metadata |

Choose a format compatible with the tools and evidence requirements.

## Example: Identify a Linux Device

```bash
lsblk -o NAME,SIZE,MODEL,SERIAL,TYPE,MOUNTPOINTS
```

Inspect block-device information:

```bash
sudo fdisk -l
```

Do not write to the source device during examination.

## Example: Create a RAW Image

The following is an illustrative workflow using `dd`.

**Warning:** Incorrect source and destination paths can destroy data. Confirm the device identity, destination and authorisation before execution.

```bash
sudo dd if=/dev/sdX \
  of=/evidence/device-image.dd \
  bs=4M \
  conv=noerror,sync \
  status=progress
```

Replace `/dev/sdX` with the verified source device.

This example does not provide a complete forensic acquisition workflow. Use validated acquisition tooling, appropriate write protection and documented procedures.

## Hashing Evidence

Calculate a SHA-256 hash:

```bash
sha256sum /evidence/device-image.dd
```

Record the result in the evidence register.

Verify the acquired image:

```bash
sha256sum /evidence/device-image.dd
```

A matching hash demonstrates that the examined copy matches the hashed reference, subject to the integrity of the original hashing process.

## Example: Image Metadata

Where supported, use forensic tooling to inspect image metadata.

```bash
file device-image.dd
```

```bash
stat device-image.dd
```

Record:
- Image format
- Image size
- Creation time
- Source device
- Acquisition operator
- Hash
- Tool and version

## Evidence Preservation

Recommended practices:

- Store original evidence securely.
- Use access-controlled evidence repositories.
- Encrypt sensitive evidence at rest.
- Restrict access to authorised personnel.
- Maintain a chain-of-custody record.
- Preserve original hashes.
- Use working copies for examination.
- Document transfers and access.
- Retain evidence according to policy.

## SSD Considerations

Solid-state drives introduce additional considerations.

TRIM and garbage collection may affect the availability of deleted data.

Other considerations:
- Controller behaviour
- Wear levelling
- Hardware encryption
- Firmware
- Background maintenance
- Device-specific acquisition limitations

Do not promise recovery of deleted SSD data.

## Cloud Evidence Acquisition

Cloud evidence may include:
- Audit logs
- Identity events
- Object access records
- Virtual machine snapshots
- Configuration exports
- API activity
- Email audit records

Consider:
- Provider retention periods
- Regional storage
- Legal jurisdiction
- API pagination
- Export completeness
- Service-specific timestamps
- Access permissions

Record query parameters, time ranges, filters and export metadata.

## Acquisition Record

For every acquisition, record:

| Field | Description |
|---|---|
| Evidence ID | Unique identifier |
| Source | Original device or data source |
| Collector | Person conducting acquisition |
| Date/time | Acquisition time and time zone |
| Tool | Tool and version |
| Method | Physical, logical, live or other |
| Destination | Evidence storage location |
| Hash | Cryptographic hash where applicable |
| Status | Complete, partial or failed |
| Notes | Errors, limitations and observations |

## Common Mistakes

- Selecting the wrong source device.
- Writing to original evidence.
- Failing to verify destination capacity.
- Omitting tool versions.
- Failing to hash acquired data.
- Ignoring encryption.
- Assuming a logical acquisition is a full disk image.
- Failing to document collection errors.
- Losing evidence during transfer.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
