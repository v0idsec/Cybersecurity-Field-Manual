# Detection Engineering Fundamentals

## Overview

Detection Engineering is the process of translating security requirements, threat intelligence and observed attack behaviour into reliable detection capabilities.

A detection should identify activity that warrants investigation and provide analysts with enough context to determine what happened.

A detection is not simply a query that returns suspicious-looking events. It is an operational capability that must be tested, maintained and understood.

## Detection Engineering Lifecycle

1. Identify a threat or security requirement.
2. Define the behaviour to detect.
3. Identify required telemetry.
4. Develop detection logic.
5. Test against representative activity.
6. Evaluate false positives.
7. Deploy the detection.
8. Monitor operational performance.
9. Review and improve.

## Detection Types

### Indicator-Based Detection

Matches known indicators of compromise.

Examples:

- Malicious file hashes
- Known malicious domains
- Suspicious IP addresses
- Known malware filenames
- Certificate fingerprints

Advantages:
- Straightforward to implement.
- Useful for known threats.
- Can support rapid blocking and alerting.

Limitations:
- Indicators change frequently.
- Attackers can modify infrastructure.
- Known indicators may have limited context.

### Signature-Based Detection

Identifies known patterns or characteristics.

Examples:

- Known malware signatures
- Recognised exploit patterns
- Specific command-line patterns
- Known malicious file structures

### Behaviour-Based Detection

Identifies activity associated with suspicious behaviour.

Examples:

- Office applications spawning scripting interpreters.
- Unusual credential access.
- Unexpected service creation.
- Suspicious remote administration.
- Unusual administrative account activity.

### Anomaly-Based Detection

Identifies deviations from expected behaviour.

Examples:

- Unusual login times.
- Unexpected data transfer volumes.
- Unusual geographic access.
- Abnormal authentication frequency.

Anomalies require context. Unusual activity is not automatically malicious.

### Correlation-Based Detection

Combines multiple events to identify a broader activity pattern.

Example:

1. Multiple authentication failures.
2. Successful authentication.
3. Privileged group membership modification.
4. Unusual administrative activity.

## Detection Quality

A useful detection should have:

| Attribute | Description |
|---|---|
| Accuracy | Identifies the intended behaviour |
| Coverage | Detects relevant activity |
| Reliability | Works consistently |
| Context | Provides useful investigation information |
| Timeliness | Alerts within an appropriate period |
| Maintainability | Can be updated as environments change |
| Efficiency | Does not create unnecessary processing overhead |

## Detection vs Prevention

Detection identifies suspicious activity.

Prevention attempts to stop it.

Examples:

| Control | Primary Function |
|---|---|
| Firewall block | Prevention |
| EDR behavioural alert | Detection |
| Antivirus quarantine | Prevention and response |
| SIEM correlation rule | Detection |
| Account disablement | Containment |
| MFA | Prevention and risk reduction |

Detection Engineering should complement preventative controls rather than replace them.

## Data Requirements

Before developing a detection, identify:

- Required event sources
- Required event fields
- Event collection frequency
- Timestamp reliability
- Retention requirements
- Normalisation requirements
- Known telemetry gaps

A detection cannot reliably identify activity that is not being collected.

## Detection Documentation

Every production detection should document:

- Detection name and identifier
- Threat or behaviour addressed
- Data sources
- Detection logic
- Severity
- ATT&CK mapping, where applicable
- Expected false positives
- Testing results
- Investigation guidance
- Response recommendations
- Owner
- Review date

## Common Challenges

- Incomplete telemetry
- Poor event normalisation
- Excessive false positives
- Inconsistent timestamps
- Alert fatigue
- Detection logic that is too broad
- Over-reliance on indicators
- Undocumented exclusions
- Rules that become outdated

## Further Reading

- MITRE ATT&CK: https://attack.mitre.org/
- Sigma: https://sigmahq.io/
- MITRE CAR: https://car.mitre.org/
- Elastic Detection Rules: https://github.com/elastic/detection-rules

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
