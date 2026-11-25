# EDR Fundamentals

## Overview

Endpoint Detection and Response (EDR) platforms monitor endpoint activity to identify suspicious behaviour, investigate threats and support incident response.

EDR provides visibility beyond traditional signature-based antivirus by collecting behavioural telemetry and enabling investigation across endpoint activity.

## EDR Capabilities

Common capabilities include:

- Process monitoring
- File activity monitoring
- Network connection monitoring
- Registry monitoring
- Behavioural detection
- Threat intelligence integration
- Endpoint isolation
- Process termination
- File quarantine
- Remote investigation
- Threat hunting
- Incident timelines

Capabilities vary between vendors and licensing tiers.

## EDR vs Traditional Antivirus

| Capability | Traditional Antivirus | EDR |
|---|---|---|
| Known malware detection | Yes | Yes |
| Behavioural detection | Varies | Common |
| Process telemetry | Limited | Extensive |
| Investigation timeline | Limited | Common |
| Threat hunting | Limited | Common |
| Remote response | Varies | Common |
| Endpoint isolation | Varies | Common |

EDR does not replace secure configuration, patching, identity controls or network security.

## Endpoint Telemetry

EDR platforms commonly collect:

### Process Activity

- Process name
- Executable path
- Process ID
- Parent process
- Command-line arguments
- User context
- Process hashes
- Execution timestamps

### File Activity

- File creation
- File modification
- File deletion
- File hashes
- File reputation
- File execution

### Network Activity

- Source and destination addresses
- Destination ports
- DNS requests
- Connection timestamps
- Associated processes

### User and Identity Activity

- Logon events
- User context
- Privilege changes
- Session activity
- Authentication behaviour

## Detection Approaches

### Signature-Based

Identifies known malicious indicators.

Examples:

- Malware hashes
- Known malicious domains
- Known malicious IP addresses
- Recognised malware signatures

### Behavioural

Identifies suspicious activity based on execution patterns.

Examples:

- Office application spawning a scripting interpreter
- Unexpected credential access
- Suspicious process injection
- Unusual persistence mechanisms
- Unexpected security control changes

### Machine Learning and Analytics

Some platforms use statistical or machine-learning techniques to identify unusual behaviour.

These detections require contextual investigation and should not automatically be treated as confirmed compromise.

## Endpoint Investigation

A typical investigation examines:

1. Alert details
2. Affected endpoint
3. User context
4. Process tree
5. File reputation
6. Network connections
7. Persistence mechanisms
8. Related alerts
9. Historical endpoint activity

## Process Trees

Process trees show parent-child execution relationships.

Example:

```text
WINWORD.EXE
└── powershell.exe
    └── rundll32.exe
```

This sequence may warrant investigation because an Office application spawning PowerShell and then another execution utility can be associated with malicious activity.

However, process ancestry alone is not proof of compromise.

Review:

- Parent process path
- Child process path
- Command-line arguments
- Digital signatures
- File hashes
- User context
- Execution time
- Related network activity

## Response Capabilities

EDR platforms may support:

| Action | Purpose |
|---|---|
| Isolate endpoint | Restrict network communication |
| Kill process | Stop suspicious execution |
| Quarantine file | Prevent further execution |
| Collect file | Preserve suspicious artefacts |
| Run investigation | Gather endpoint information |
| Block indicator | Prevent known malicious activity |
| Restore file | Recover quarantined content where appropriate |

Response actions should follow incident response procedures and consider operational impact.

## EDR Deployment Considerations

- Deploy to all supported endpoints.
- Monitor agent health.
- Protect agent configuration.
- Restrict administrative access.
- Prevent unauthorised tampering.
- Monitor sensor communication.
- Establish retention requirements.
- Test response actions.
- Document exclusions and exceptions.

## EDR Limitations

EDR is not a complete security solution.

Potential limitations include:

- Unmonitored endpoints
- Disabled or unhealthy agents
- Telemetry gaps
- Detection false positives
- Evasion techniques
- Limited visibility into unmanaged devices
- Incomplete cloud or identity visibility
- Licensing restrictions

## Common EDR Platforms

- Microsoft Defender for Endpoint
- CrowdStrike Falcon
- SentinelOne Singularity
- Sophos Intercept X
- Palo Alto Cortex XDR
- Elastic Defend

## Further Reading

- Microsoft Defender for Endpoint: https://learn.microsoft.com/defender-endpoint/
- CrowdStrike: https://www.crowdstrike.com/
- SentinelOne: https://www.sentinelone.com/
- Elastic Defend: https://www.elastic.co/guide/en/security/current/es-overview.html

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
