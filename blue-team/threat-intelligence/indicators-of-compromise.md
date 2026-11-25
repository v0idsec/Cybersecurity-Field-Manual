# Indicators of Compromise

## Overview

Indicators of Compromise (IOCs) are observable artefacts that may indicate malicious activity or system compromise.

IOCs are useful for investigation and detection, but individual indicators rarely provide complete context.

## Common IOC Types

| Type | Example |
|---|---|
| IP address | Known malicious infrastructure |
| Domain | Phishing or command-and-control domain |
| URL | Malicious download location |
| File hash | SHA-256 hash of a known malware sample |
| Email address | Known malicious sender |
| File path | Suspicious persistence location |
| Registry key | Unexpected autorun configuration |
| Mutex | Malware-associated execution artefact |
| Certificate | Certificate associated with suspicious infrastructure |
| User-Agent | Unusual or known malicious HTTP client identifier |

## IOC Limitations

An indicator may be:

- Reused by unrelated organisations.
- Shared by legitimate and malicious services.
- Changed by an attacker.
- Outdated.
- Incorrectly attributed.
- Associated with compromised legitimate infrastructure.

For example, a malicious IP address may later be reassigned to a legitimate hosting customer.

## IOC Quality

Record the following where available:

| Field | Purpose |
|---|---|
| Indicator | Actual observable value |
| Type | IP, domain, hash, URL, etc. |
| Source | Where it was obtained |
| First Seen | Initial observation |
| Last Seen | Most recent observation |
| Confidence | Confidence in malicious association |
| Context | Related campaign or activity |
| Expiry | When the indicator should be reviewed |
| Action | Proposed operational response |

## Indicator Handling

Before using an IOC:

1. Validate its format.
2. Identify its source.
3. Check when it was observed.
4. Review supporting context.
5. Check for false-positive risk.
6. Determine organisational relevance.
7. Select an appropriate response.

## Detection Considerations

Avoid relying exclusively on static indicators.

Where possible, combine IOCs with:

- Behavioural analytics.
- Process execution context.
- Network telemetry.
- Authentication events.
- Endpoint activity.
- Threat hunting hypotheses.

## Handling and Sharing

- Follow organisational information-sharing policies.
- Avoid publishing sensitive internal indicators.
- Apply appropriate handling restrictions.
- Respect licensing and redistribution requirements.
- Record confidence and provenance.
- Review indicators before allowing automated blocking.

## Key Takeaways

IOCs are useful investigative clues, not proof of compromise.

Always consider context, confidence, age and potential operational impact.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
