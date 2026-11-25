# Threat Intelligence Fundamentals

## Overview

Cyber threat intelligence is analysed information about threats, adversaries, infrastructure, capabilities and intentions that helps organisations make informed security decisions.

Raw indicators and security alerts are not automatically intelligence. Intelligence requires context, analysis and relevance to the organisation.

## Types of Threat Intelligence

| Type | Focus | Example |
|---|---|---|
| Strategic | Business risk and threat landscape | Ransomware trends affecting an industry |
| Operational | Campaigns and adversary activity | An active campaign targeting suppliers |
| Tactical | Adversary techniques and behaviour | Credential theft through phishing |
| Technical | Observable indicators | Malicious IP addresses and file hashes |

## Intelligence Requirements

Intelligence should answer specific questions.

Examples:

- Which threats are most relevant to our industry?
- Are our systems being targeted by a known campaign?
- Which adversary techniques should our detection team prioritise?
- Are any known malicious indicators present in our environment?
- What vulnerabilities are being actively exploited?

These requirements help prevent collecting large volumes of irrelevant information.

## Intelligence Versus Information

**Information:** A suspicious IP address appeared in a security report.

**Intelligence:** The IP address is associated with a recently observed campaign targeting organisations in our sector, and matching activity has been identified in our environment.

The second example provides context and supports a decision.

## Intelligence Confidence

Record confidence and source reliability.

Consider:

- Source reputation.
- Independent corroboration.
- Indicator age.
- Collection method.
- Supporting evidence.
- Potential false positives.
- Relevance to the organisation.

Avoid treating every published indicator as confirmed malicious activity.

## Common Applications

- SIEM detection development.
- Threat hunting.
- Incident investigation.
- Vulnerability prioritisation.
- Firewall and proxy controls.
- Security architecture decisions.
- Executive risk reporting.

## Limitations

Threat intelligence can be:

- Incomplete.
- Outdated.
- Incorrect.
- Biased towards certain industries.
- Focused on threats irrelevant to the organisation.
- Difficult to validate independently.

Intelligence should inform decisions, not replace investigation or risk assessment.

## Key Takeaways

Useful threat intelligence is relevant, timely, contextual and actionable.

Collecting more indicators does not necessarily improve security.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
