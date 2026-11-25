# Hypothesis Development

## Overview

A hunting hypothesis is a testable statement describing suspicious activity that may be occurring within an environment.

A well-defined hypothesis provides direction, identifies required telemetry and prevents investigations from becoming unfocused searches.

## Characteristics of a Good Hypothesis

A useful hypothesis should be:

- Specific
- Testable
- Relevant to the organisation
- Supported by a plausible threat scenario
- Connected to observable activity
- Achievable using available telemetry

## Hypothesis Structure

A practical format:

> An attacker may be performing [behaviour] against [target] using [method], which could be observed through [telemetry].

Example:

> An attacker may be using compromised administrative credentials to access workstations remotely, which could be observed through authentication and endpoint telemetry.

## Sources for Hypotheses

### Threat Intelligence

Use:

- Threat actor reports
- Malware analysis
- Campaign reporting
- Vulnerability advisories
- Industry threat intelligence

### MITRE ATT&CK

Identify techniques relevant to the organisation's technology and exposure.

Examples:

| Technique | Hunting Opportunity |
|---|---|
| T1078 - Valid Accounts | Unusual account usage |
| T1059.001 - PowerShell | Suspicious scripting activity |
| T1053.005 - Scheduled Task | Unexpected scheduled tasks |
| T1021.001 - Remote Desktop Protocol | Unusual remote desktop activity |
| T1547.001 - Registry Run Keys | Unexpected startup persistence |

### Previous Incidents

Previous incidents may reveal:

- Missed detections
- Weak logging coverage
- Common attacker behaviours
- Misconfigured security controls
- Unusual access patterns

### Environmental Changes

Consider hunts following:

- New system deployments
- Identity migrations
- Cloud adoption
- Security incidents
- Major software changes
- New internet-facing services

## Hypothesis Decomposition

Break a hypothesis into observable behaviours.

Example hypothesis:

> An attacker may be attempting to establish persistence through scheduled tasks.

Potential observations:

1. New scheduled task creation.
2. Unexpected task execution.
3. Task running under an unusual account.
4. Task launching an unusual executable.
5. Task configured to execute at logon or startup.

Each observation can become a separate query or investigation step.

## Define Expected Evidence

Before running the hunt, document:

- Events expected if the hypothesis is true.
- Events expected during normal operation.
- Required telemetry.
- Known visibility gaps.
- Evidence that would weaken the hypothesis.

This reduces confirmation bias.

## Prioritisation

Prioritise hypotheses using:

- Business risk
- Asset criticality
- Threat intelligence relevance
- Exposure
- Likelihood
- Available telemetry
- Investigation effort

## Example Hypothesis Library

### Identity

- A compromised account may be authenticating from unusual devices.
- A service account may be used interactively.
- An attacker may be abusing privileged group membership.

### Endpoint

- A compromised endpoint may be executing suspicious child processes.
- An attacker may be establishing persistence through services.
- A user may be executing unauthorised remote administration tools.

### Network

- An endpoint may be communicating with unusual external infrastructure.
- A compromised host may be scanning internal systems.
- Unusual DNS activity may indicate command-and-control behaviour.

### Cloud

- A compromised identity may be creating new access keys.
- An attacker may be modifying cloud audit settings.
- Unauthorised principals may be accessing sensitive storage.

## Hypothesis Tracking

Maintain a record of:

| Field | Description |
|---|---|
| ID | Unique hypothesis identifier |
| Hypothesis | Testable statement |
| Source | Intelligence, incident or risk |
| Priority | Investigation priority |
| Required telemetry | Data sources |
| Owner | Assigned analyst |
| Status | Planned, active or completed |
| Outcome | Findings and conclusion |

## Common Mistakes

- Writing hypotheses that cannot be tested.
- Assuming malicious activity is already occurring.
- Ignoring legitimate explanations.
- Using ATT&CK mappings without a clear detection objective.
- Hunting without confirming telemetry availability.
- Expanding the scope unnecessarily.

## Further Reading

- MITRE ATT&CK: https://attack.mitre.org/
- MITRE CAR: https://car.mitre.org/
- CISA: https://www.cisa.gov/

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
