# IOC Enrichment and Analysis

## Overview

IOC enrichment adds context to observable indicators so analysts can make better decisions.

A suspicious IP address, domain or file hash becomes more useful when supported by reputation, infrastructure, historical observations and internal telemetry.

## Enrichment Objectives

Determine:

- What is the indicator associated with?
- Has it been observed in known campaigns?
- When was it first and last observed?
- Is it shared with legitimate services?
- Does it appear in internal telemetry?
- Is there sufficient confidence to take action?

## Common Enrichment Sources

| Indicator | Enrichment |
|---|---|
| IP address | ASN, hosting provider, reputation, geolocation |
| Domain | WHOIS/RDAP, DNS, passive DNS, registration age |
| URL | Redirect chain, domain reputation, page behaviour |
| File hash | Malware family, sandbox results, signature information |
| Email address | Domain reputation, sender history, related infrastructure |
| Certificate | Issuer, validity, subject and related domains |

## Basic Workflow

### 1. Record the Indicator

Capture:

- Indicator value.
- Indicator type.
- Original source.
- Observation date.
- Initial context.

### 2. Validate the Format

Check that the indicator is syntactically valid.

Examples:

- IPv4 or IPv6 address.
- Fully qualified domain name.
- SHA-256 hash.
- URL.

### 3. Enrich the Indicator

Use appropriate reputation and analysis sources.

Examples:

- VirusTotal.
- AbuseIPDB.
- URLhaus.
- ThreatFox.
- WHOIS/RDAP.
- Internal DNS and proxy logs.

### 4. Correlate with Internal Telemetry

Look for related activity in:

- DNS logs.
- Proxy logs.
- Firewall logs.
- EDR telemetry.
- Email security logs.
- SIEM events.

### 5. Assess Confidence

Consider source quality, age, corroboration and false-positive risk.

### 6. Determine Action

Possible outcomes:

- No action.
- Continue monitoring.
- Create a detection.
- Start a threat hunt.
- Escalate for incident investigation.
- Block or quarantine through an approved process.

## Example Investigation

**Indicator:** `suspicious-example.invalid`

Investigation:

1. Identify the original source.
2. Check domain registration and DNS history.
3. Review reputation services.
4. Check whether the domain appears in internal DNS logs.
5. Identify associated endpoints and users.
6. Review any related web requests.
7. Assess whether the activity indicates compromise.

The `.invalid` domain is reserved for documentation and should not be treated as a real malicious indicator.

## Common Mistakes

- Treating reputation scores as definitive.
- Ignoring indicator age.
- Blocking shared hosting infrastructure without validation.
- Uploading sensitive files to public services.
- Assuming geolocation identifies an attacker.
- Failing to preserve source information.
- Confusing an IOC match with confirmed compromise.

## Documentation

Record:

- Indicator.
- Enrichment sources.
- Collection time.
- Findings.
- Confidence.
- Internal matches.
- False-positive considerations.
- Recommended action.
- Analyst.

## Key Takeaways

Enrichment turns isolated indicators into useful investigative context.

Correlate external intelligence with internal evidence before making operational decisions.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
