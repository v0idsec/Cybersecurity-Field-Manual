# Incident Response Lifecycle

## Overview

An incident response lifecycle provides a repeatable structure for managing security incidents.

A practical lifecycle consists of:

1. Preparation
2. Detection and identification
3. Analysis
4. Containment
5. Eradication
6. Recovery
7. Post-incident improvement

These phases are not always strictly sequential. New evidence may require responders to revisit earlier decisions.

## 1. Preparation

Preparation should happen before an incident occurs.

Key activities:

- Establish an incident response policy and plan.
- Define incident categories and severity levels.
- Assign response roles and escalation paths.
- Maintain emergency contact information.
- Establish secure communication channels.
- Identify critical systems and business dependencies.
- Configure and retain relevant security logs.
- Establish evidence handling procedures.
- Prepare endpoint and network investigation capabilities.
- Maintain tested backups and recovery procedures.
- Establish relationships with external responders and service providers.
- Conduct tabletop exercises and technical simulations.

Preparation checklist:

- [ ] Incident response plan approved.
- [ ] Incident roles assigned.
- [ ] Escalation contacts current.
- [ ] Critical assets identified.
- [ ] Logging and retention reviewed.
- [ ] Backups tested.
- [ ] Evidence storage available.
- [ ] Emergency communication channels established.
- [ ] External support arrangements documented.
- [ ] Response exercises conducted.

## 2. Detection and identification

Identify suspicious activity and determine whether it represents a security incident.

Potential sources:

- SIEM alerts.
- EDR detections.
- Identity provider alerts.
- Firewall and network monitoring.
- Cloud audit logs.
- Vulnerability disclosures.
- User reports.
- External threat intelligence.
- Third-party service provider notifications.

Initial questions:

- What happened?
- When was it first observed?
- Which systems and accounts are involved?
- Is activity ongoing?
- Is there evidence of unauthorised access?
- Is sensitive information potentially affected?
- Are critical services impacted?
- Is the alert a duplicate or related to an existing incident?

Document the initial assessment and assign an incident owner.

## 3. Analysis

Establish the scope, timeline, cause and impact of the incident.

Investigate:

- Initial access.
- Authentication activity.
- Process execution.
- Network connections.
- File and registry changes.
- Privilege escalation.
- Persistence mechanisms.
- Lateral movement.
- Data access and exfiltration.
- Cloud control-plane activity.
- Third-party dependencies.

Separate confirmed observations from hypotheses.

Do not assume that the first affected system is the point of entry. Determine whether the activity is isolated or part of a larger compromise.

## 4. Containment

Limit further damage while preserving the ability to investigate.

Possible actions:

- Isolate affected endpoints.
- Disable or restrict compromised accounts.
- Revoke sessions and refresh tokens.
- Block malicious domains, IP addresses or URLs.
- Restrict exposed services.
- Disable compromised credentials or keys.
- Apply temporary network segmentation.
- Suspend affected integrations.
- Restrict access to sensitive resources.

Containment must be authorised and proportionate to the risk.

## 5. Eradication

Remove the threat and the conditions that allowed it to succeed.

Possible activities:

- Remove malware and persistence.
- Rebuild compromised endpoints.
- Patch exploited vulnerabilities.
- Remove unauthorised accounts.
- Rotate compromised credentials and secrets.
- Correct identity and access configuration.
- Remove malicious cloud resources.
- Review trust relationships and integrations.
- Validate that attacker access has been removed.

Do not rely solely on antivirus or EDR reporting that a malicious file was quarantined.

## 6. Recovery

Restore affected systems and services to a trusted operational state.

Recovery should include:

- Restore from known-good backups where appropriate.
- Rebuild systems from trusted sources.
- Validate system integrity.
- Confirm security controls are functioning.
- Reset credentials and restore access safely.
- Monitor for signs of reinfection or renewed access.
- Confirm business functionality with system owners.
- Record recovery approval.

Increase monitoring during the recovery period.

## 7. Post-incident improvement

After the incident is stable:

- Build a complete incident timeline.
- Confirm the root cause where possible.
- Identify contributing factors.
- Review detection and response effectiveness.
- Identify control failures and gaps.
- Record lessons learned.
- Assign corrective actions and owners.
- Set due dates and measurable completion criteria.
- Update playbooks and response procedures.
- Share relevant findings with stakeholders.

## Lifecycle exit criteria

An incident should not be closed merely because the immediate alert has disappeared.

Closure should consider:

- Threat activity has been contained.
- Known attacker access has been removed.
- Affected systems have been recovered or formally accepted as unavailable.
- Required evidence has been preserved.
- Business owners have accepted the recovery state.
- Required notifications and escalations have been addressed.
- Outstanding risks have owners and documented acceptance.
- Post-incident actions have been recorded.

## Further reading

- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
- [CISA Incident Response](https://www.cisa.gov/topics/cyber-threats-and-advisories/incident-response)

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
