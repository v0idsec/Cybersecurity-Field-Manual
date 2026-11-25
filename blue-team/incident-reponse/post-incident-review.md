# Post-Incident Review

## Overview

A post-incident review evaluates how an incident occurred, how effectively it was handled and what improvements are required.

The purpose is organisational learning and risk reduction, not assigning personal blame.

A useful review examines both technical causes and the wider conditions that allowed the incident to occur or increased its impact.

## When to conduct a review

Conduct a review after:

- A major security incident.
- A confirmed compromise.
- A significant data exposure.
- A ransomware event.
- A prolonged service disruption.
- A near miss with meaningful security implications.
- An incident that exposed a major control weakness.

Smaller incidents may be reviewed collectively to identify recurring trends.

## Review principles

### Blameless, not accountability-free

A blameless review does not mean ignoring responsibilities or decisions.

It means examining:

- What information was available at the time.
- What assumptions were made.
- What processes and controls existed.
- What pressures or constraints affected decisions.
- What system conditions contributed.
- How the organisation can reduce recurrence.

Avoid framing the review around individual fault when the objective is to understand systemic weaknesses.

### Evidence-based

Clearly separate:

- Confirmed facts.
- Supported conclusions.
- Probable explanations.
- Unresolved questions.

Do not present assumptions as established root causes.

## Review structure

### 1. Incident summary

Document:

- Incident identifier.
- Incident category.
- Severity.
- Detection date.
- Start and end dates, where known.
- Affected services.
- Business impact.
- Current status.

### 2. What happened?

Describe the incident in chronological order.

Include:

- Initial access or trigger, if known.
- Attacker or malicious activity.
- Systems and accounts affected.
- Detection and escalation.
- Containment.
- Eradication.
- Recovery.

### 3. Impact assessment

Assess:

- Service availability.
- Data confidentiality.
- Data integrity.
- Financial impact.
- Operational disruption.
- Customer impact.
- Third-party impact.
- Legal and regulatory considerations.
- Recovery effort.

Distinguish confirmed impact from potential impact.

### 4. Root cause analysis

Identify the underlying conditions that allowed the incident to occur.

Possible contributing factors:

- Missing or ineffective security controls.
- Unpatched vulnerabilities.
- Weak authentication.
- Excessive privileges.
- Inadequate monitoring.
- Poor asset visibility.
- Insufficient segmentation.
- Misconfiguration.
- Incomplete processes.
- Third-party dependencies.
- Human or workflow factors.

A root cause should explain why the incident was possible, not merely restate the attacker's final action.

### 5. Detection review

Evaluate:

- Was the activity detected?
- How long did detection take?
- Which alert or report identified it?
- Were relevant logs available?
- Were detections correctly prioritised?
- Were alerts investigated promptly?
- Could earlier detection have reduced impact?

### 6. Response review

Evaluate:

- Was the response plan followed?
- Were roles and authority clear?
- Were escalation paths effective?
- Were containment decisions timely?
- Was evidence preserved?
- Were communications appropriate?
- Were business owners involved?
- Were external specialists engaged when needed?

### 7. Recovery review

Evaluate:

- Were systems restored safely?
- Were backups reliable?
- Were credentials and secrets rotated?
- Were security controls restored?
- Was monitoring increased?
- Were residual risks documented?
- Was business approval obtained?

### 8. What went well?

Record effective controls, decisions, processes and collaboration.

### 9. What could be improved?

Identify specific weaknesses without assigning unsupported blame.

### 10. Corrective actions

Every action should have:

- A clear description.
- A priority.
- An accountable owner.
- A due date.
- A measurable completion criterion.
- A verification method.
- A status.

## Review meeting

Suggested attendees:

- Incident Commander.
- Security and IT responders.
- Relevant system owners.
- Business stakeholders.
- Legal or privacy representatives where appropriate.
- External specialists where relevant.

The meeting should focus on evidence, decisions, system conditions and improvement opportunities.

## Review outputs

The review should produce:

- A final incident summary.
- A confirmed or qualified root cause assessment.
- An incident timeline.
- An impact assessment.
- Detection and response findings.
- Lessons learned.
- A prioritised corrective action register.
- Updates to policies, procedures and playbooks.
- Any required risk acceptance or escalation.

## Follow-through

A post-incident review is incomplete until corrective actions are tracked.

Assign owners and deadlines. Escalate overdue high-priority actions. Verify that completed actions have actually improved the relevant control.

Use the companion templates:

- `templates/post-incident-review-template.md`
- `templates/lessons-learned-action-register-template.md`

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
