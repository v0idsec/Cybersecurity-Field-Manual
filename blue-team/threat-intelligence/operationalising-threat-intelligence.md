# Operationalising Threat Intelligence

## Overview

Operationalising threat intelligence means turning analysed intelligence into practical improvements across security operations.

Intelligence should influence decisions, detections and defensive controls rather than simply accumulating in reports or feeds.

## Common Applications

| Team | Application |
|---|---|
| SOC | Alert enrichment and triage |
| Threat Hunting | Develop and test hypotheses |
| Incident Response | Identify related infrastructure and activity |
| Detection Engineering | Build and improve detections |
| Vulnerability Management | Prioritise actively exploited weaknesses |
| IT Operations | Review defensive controls |
| Management | Understand relevant business risks |

## Intelligence-to-Action Workflow

1. Receive intelligence.
2. Validate the source.
3. Assess relevance.
4. Enrich indicators.
5. Correlate against internal telemetry.
6. Determine risk and confidence.
7. Select an appropriate action.
8. Obtain approval where required.
9. Implement the action.
10. Measure effectiveness.

## Detection Engineering

Intelligence can support detection development.

Examples:

- Add validated indicators to threat matching.
- Develop detections for observed techniques.
- Create correlation rules.
- Identify telemetry gaps.
- Build threat hunting queries.

Prefer behavioural detections where possible, as static indicators can become outdated.

## SIEM Integration

Threat intelligence may be integrated into a SIEM using:

- TAXII feeds.
- STIX data.
- Vendor integrations.
- API-based ingestion.
- Approved CSV or JSON imports.
- Internal intelligence platforms.

Consider:

- Data normalisation.
- Deduplication.
- Indicator expiry.
- Confidence levels.
- Source tracking.
- Feed availability.
- False-positive handling.

## STIX and TAXII

**STIX (Structured Threat Information Expression)** is a language for representing cyber threat intelligence.

**TAXII (Trusted Automated Exchange of Intelligence Information)** is a protocol for exchanging cyber threat intelligence.

They are commonly used together to support structured intelligence sharing.

References:

- https://oasis-open.github.io/cti-documentation/
- https://oasis-open.github.io/cti-documentation/taxii/intro.html

## Automated Blocking

Automated blocking can reduce exposure but introduces operational risk.

Before blocking an indicator:

- Validate the indicator.
- Check its age and confidence.
- Assess potential business impact.
- Consider shared hosting or CDN infrastructure.
- Define expiry and review procedures.
- Obtain required approval.
- Maintain rollback capability.

Do not blindly block every indicator from an external feed.

## Intelligence Sharing

When sharing intelligence:

- Apply appropriate handling markings.
- Remove unnecessary sensitive information.
- Respect source licensing.
- Validate accuracy.
- Record provenance.
- Follow information-sharing agreements.

## Measuring Effectiveness

Useful measures include:

- Number of relevant detections created.
- Number of intelligence-led investigations.
- Time from intelligence receipt to operational use.
- Number of validated internal matches.
- Detection coverage improvements.
- False-positive rates.
- Intelligence requirements successfully answered.

## Key Takeaways

Threat intelligence becomes valuable when it leads to informed action.

Integrate it into existing security processes, maintain quality controls and regularly review whether it is improving defensive outcomes.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
