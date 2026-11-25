# Sigma Rule Development

## Overview

Sigma is an open detection rule format designed to describe security-relevant event patterns in a platform-independent way.

Rules can be converted into queries for supported SIEM platforms using compatible conversion tools.

Sigma is particularly useful for sharing detection logic across different environments.

## Rule Structure

A Sigma rule commonly includes:

- Title
- Unique identifier
- Status
- Description
- Log source
- Detection conditions
- False-positive notes
- Severity level
- Tags
- References

## Basic Rule Example

```yaml
title: Suspicious PowerShell Execution
id: 6e98e2bc-0a87-4b6c-9f6b-8c8f4d3b1e12
status: experimental
description: Detects PowerShell execution containing suspicious command-line patterns.
logsource:
    category: process_creation
    product: windows
detection:
    selection:
        Image|endswith:
            - '\powershell.exe'
            - '\pwsh.exe'
        CommandLine|contains:
            - 'EncodedCommand'
            - 'FromBase64String'
    condition: selection
falsepositives:
    - Approved administration scripts
    - Software deployment activity
level: medium
tags:
    - attack.execution
    - attack.t1059.001
```

This example is illustrative. Validate field names against the target event source and backend.

## Log Sources

Sigma uses log source definitions to describe the type of telemetry required.

Examples:

```yaml
logsource:
    product: windows
    category: process_creation
```

```yaml
logsource:
    product: windows
    service: security
```

```yaml
logsource:
    product: linux
    category: process_creation
```

The backend must support the relevant log source and field mappings.

## Detection Selections

Selections define matching conditions.

### Exact Match

```yaml
detection:
    selection:
        EventID: 4625
    condition: selection
```

### Multiple Conditions

```yaml
detection:
    selection:
        EventID: 4625
        LogonType: 10
    condition: selection
```

### Contains Matching

```yaml
detection:
    selection:
        CommandLine|contains: 'EncodedCommand'
    condition: selection
```

### Ends With Matching

```yaml
detection:
    selection:
        Image|endswith: '\powershell.exe'
    condition: selection
```

## Combining Conditions

Sigma supports logical conditions.

Example:

```yaml
detection:
    selection_process:
        Image|endswith: '\powershell.exe'
    selection_argument:
        CommandLine|contains:
            - 'EncodedCommand'
            - 'DownloadString'
    condition: selection_process and selection_argument
```

## Exclusions

Use exclusions carefully.

Example:

```yaml
detection:
    selection:
        EventID: 4625
    filter_expected_activity:
        IpAddress: '192.0.2.10'
    condition: selection and not filter_expected_activity
```

The IP address is from the documentation-only TEST-NET-1 range.

Exclusions should be justified and narrowly scoped.

## Metadata and ATT&CK Mapping

Use tags to describe relevant ATT&CK tactics and techniques.

Example:

```yaml
tags:
    - attack.credential_access
    - attack.t1110
```

Only assign mappings supported by the actual detection logic.

## Validation

Use the Sigma CLI to validate rules.

```bash
sigma check suspicious-powershell.yml
```

Convert a rule to a supported backend:

```bash
sigma convert -t splunk suspicious-powershell.yml
```

Backend names and options depend on the installed Sigma CLI version and available plugins.

## Rule Quality Checklist

- [ ] Unique rule identifier.
- [ ] Descriptive title.
- [ ] Correct log source.
- [ ] Valid detection logic.
- [ ] Appropriate condition.
- [ ] False positives documented.
- [ ] Severity justified.
- [ ] ATT&CK mapping reviewed.
- [ ] Rule validated.
- [ ] Backend compatibility checked.
- [ ] Test evidence recorded.

## Sigma Resources

- Sigma Documentation: https://sigmahq.io/docs/
- Sigma GitHub: https://github.com/SigmaHQ/sigma
- Sigma CLI: https://github.com/SigmaHQ/sigma-cli
- Sigma Rule Repository: https://github.com/SigmaHQ/sigma

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
