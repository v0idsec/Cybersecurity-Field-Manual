# URL and Attachment Analysis

## Overview

Phishing messages frequently use links and attachments to deliver malicious content, collect information or redirect users to fraudulent services.

This guide covers safe defensive analysis.

## URL Analysis

Record:

- Original URL
- Displayed link text
- Hostname
- Domain registration information
- URL path
- Query parameters
- Redirect destinations
- Reputation results
- First and last observed times

Do not visit suspicious URLs directly from a production workstation.

## URL Structure

Example:

```text
https://login.example.com/account/verify?ref=123
```

Components:

| Component | Value |
|---|---|
| Scheme | `https` |
| Hostname | `login.example.com` |
| Path | `/account/verify` |
| Query | `ref=123` |

Pay attention to:

- Lookalike domains
- Homograph characters
- Unexpected subdomains
- URL shorteners
- IP-based URLs
- Encoded parameters
- Unusual ports
- Redirect parameters

## Defanged Indicators

Defanging makes indicators safer to display in reports.

Example:

```text
https://malicious.example/path
```

Becomes:

```text
hxxps://malicious[.]example/path
```

Defanging is a reporting technique, not a substitute for safe handling.

## Reputation Services

Common defensive services include:

- VirusTotal
- URLhaus
- Google Safe Browsing
- Cisco Talos Intelligence
- urlscan.io
- AbuseIPDB

Consider privacy before submitting URLs or files to public services. Submissions may expose sensitive information or become publicly accessible.

## Redirect Analysis

A URL may redirect through several destinations.

Record:
- Initial URL
- Redirect status codes
- Intermediate hosts
- Final destination
- Timestamp
- Analysis method

Do not follow suspicious redirects from a normal workstation.

Use an approved isolated analysis environment.

## Attachment Analysis

### Initial Inspection

Record:
- Filename
- Extension
- File size
- Actual file type
- Hash
- Embedded links
- Archive contents
- Metadata

Do not trust file extensions.

### File Identification

Linux:

```bash
file suspicious-file
```

PowerShell:

```powershell
Get-Item .\suspicious-file |
    Select-Object Name, Length, CreationTime, LastWriteTime
```

### Hashing

```bash
sha256sum suspicious-file
```

PowerShell:

```powershell
Get-FileHash .\suspicious-file -Algorithm SHA256
```

### Archive Inspection

List archive contents without executing extracted files:

```bash
7z l suspicious-archive.zip
```

Be alert to:
- Nested archives
- Password-protected archives
- Double extensions
- Unusual filenames
- Path traversal names
- Executables inside archives

### Office Documents

Potential indicators:
- Macros
- Embedded objects
- External relationships
- Suspicious hyperlinks
- Unexpected templates
- Script-like content

Useful tools include:

- oletools
- olevba
- mraptor

Example:

```bash
olevba suspicious-document.docm
```

Tool output is an investigative lead and should be interpreted in context.

## Safe Analysis Environment

Use a dedicated, isolated environment for suspicious files.

Recommended safeguards:
- No access to production networks.
- No personal accounts.
- No shared clipboard unless required.
- Controlled network access.
- Snapshots or disposable virtual machines.
- Monitoring enabled.
- Evidence preservation.
- No uncontrolled file sharing.

Do not upload confidential files to public scanning services without approval.

## Sandbox Analysis

A sandbox may provide:
- Process activity
- File-system changes
- Registry changes
- Network connections
- Dropped files
- Execution behaviour

Examples:
- CAPE Sandbox
- ANY.RUN
- Hybrid Analysis
- Joe Sandbox

Only submit files through approved channels and consider provider data-handling policies.

## Investigation Workflow

1. Preserve the original message.
2. Extract URLs and attachments safely.
3. Record hashes and metadata.
4. Identify actual file types.
5. Review URL reputation.
6. Examine redirect chains in isolation.
7. Perform static analysis.
8. Use sandbox analysis where authorised.
9. Correlate with endpoint telemetry.
10. Document indicators and confidence.

## Common Mistakes

- Opening suspicious attachments on production devices.
- Clicking links during initial triage.
- Assuming HTTPS means safe.
- Trusting file extensions.
- Uploading confidential documents to public services.
- Ignoring redirect chains.
- Treating one reputation result as definitive.
- Failing to preserve the original attachment.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
