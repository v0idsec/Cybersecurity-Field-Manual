# Threat Hunting Methodology

## Overview

A consistent methodology makes threat hunts repeatable, measurable and easier to communicate.

This guide provides a structured workflow for conducting investigations across endpoint, identity, network and cloud telemetry.

## Phase 1: Define the Objective

Identify what the hunt is intended to discover.

Examples:

- Identify potential credential compromise.
- Find unexpected remote administration.
- Detect suspicious persistence mechanisms.
- Identify unusual data access.
- Investigate possible lateral movement.

Avoid objectives that are too broad to investigate effectively.

## Phase 2: Develop the Hypothesis

Create a statement that can be tested against available evidence.

Example:

> A compromised endpoint may be attempting lateral movement through remote service creation.

Break this into observable behaviours:

- Unexpected remote authentication.
- Administrative access to another endpoint.
- New service creation.
- Unusual process execution.
- Connections between systems that do not normally communicate.

## Phase 3: Establish Scope

Define:

- Relevant systems
- Users and accounts
- Network segments
- Cloud subscriptions or tenants
- Time period
- Relevant applications
- Excluded systems
- Authorised investigation boundaries

A narrow, well-defined hunt is generally more productive than an unrestricted search.

## Phase 4: Identify Data Sources

Determine which telemetry can support the hypothesis.

| Behaviour | Potential Data Source |
|---|---|
| Authentication | Windows Security, Entra ID, Linux auth logs |
| Process execution | Sysmon, EDR, auditd |
| Network activity | Firewall, DNS, Zeek, proxy |
| Persistence | Endpoint telemetry, registry, services |
| Cloud changes | Cloud audit logs |
| File activity | EDR, filesystem auditing |

Confirm that the required data is available for the investigation period.

## Phase 5: Establish a Baseline

Understand expected behaviour before classifying anomalies.

Consider:

- Normal user activity
- Standard administrative workflows
- Common processes
- Known software deployments
- Expected network connections
- Scheduled tasks
- Service account behaviour

Document baseline limitations.

## Phase 6: Execute the Hunt

Use SIEM queries, endpoint investigation tools and supporting telemetry.

A useful process:

1. Search for broad indicators.
2. Narrow the results.
3. Identify related entities.
4. Correlate across data sources.
5. Examine supporting evidence.
6. Record findings.

## Phase 7: Validate Findings

For suspicious results, establish:

- What happened?
- When did it happen?
- Which system was involved?
- Which account was involved?
- What process or service was responsible?
- Was the activity expected?
- Is there supporting evidence?
- Could the activity represent compromise?

Do not rely on a single indicator when stronger contextual evidence is available.

## Phase 8: Escalate

Escalate when:

- Malicious activity is confirmed.
- Compromise is strongly suspected.
- Privileged accounts are involved.
- Sensitive information may be exposed.
- Multiple systems are affected.
- The activity is ongoing.

Follow the organisation's incident response process.

## Phase 9: Document Results

Record:

- Hunt objective
- Hypothesis
- Scope
- Timeframe
- Data sources
- Queries
- Results
- Evidence
- Limitations
- Conclusions
- Recommendations

## Phase 10: Improve Security

Translate useful findings into:

- New SIEM detections
- Improved EDR coverage
- Logging improvements
- Detection tuning
- Hardening recommendations
- Incident response playbooks
- Additional hunting hypotheses

## Repeatable Hunt Workflow

```text
Objective
   |
Hypothesis
   |
Scope and Data Sources
   |
Baseline
   |
Query and Investigate
   |
Correlate Findings
   |
Validate
   |
Escalate or Close
   |
Document and Improve
```

## Further Reading

- MITRE ATT&CK: https://attack.mitre.org/
- MITRE CAR: https://car.mitre.org/
- CISA: https://www.cisa.gov/
- Sigma: https://sigmahq.io/

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
