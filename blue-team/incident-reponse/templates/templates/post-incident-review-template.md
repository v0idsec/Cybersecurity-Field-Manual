# Post-Incident Review / Post-Mortem

> **Incident reference:** [INC-YYYY-NNN]
>
> **Handling:** [Internal / Confidential / Restricted]
>
> **Review status:** [Draft / In Review / Approved / Final]
>
> **Review date:** [Date]
>
> **Review facilitator:** [Name / Role]

## 1. Review Overview

| Field | Details |
|---|---|
| Incident title | [Title] |
| Incident category | [Category] |
| Severity | [Critical / High / Medium / Low] |
| Incident start | [Date and time / Unknown] |
| Detection time | [Date and time] |
| Containment time | [Date and time] |
| Recovery time | [Date and time / Ongoing] |
| Review owner | [Name / Role] |
| Participants | [Names / Roles] |

### Purpose of review

[Explain why the review is being conducted and what it aims to establish.]

This review is intended to improve organisational resilience, security controls and incident response capability. It is not intended to assign personal blame.

## 2. Executive Summary

[Provide a concise summary of the incident, its impact, the response and the most important findings.]

Include:

- What happened.
- How it was detected.
- What was affected.
- How the incident was contained.
- Whether recovery was successful.
- The most significant lessons learned.

## 3. Incident Description

### What happened?

[Describe the incident in plain language.]

### How was it discovered?

[Describe the detection source and initial reporting.]

### What was the apparent attack path?

[Describe the known sequence of activity. Identify any uncertainty.]

### What was the root cause?

[State the confirmed root cause if established. Otherwise, document the leading hypothesis and what remains unknown.]

## 4. Impact Assessment

| Impact area | Assessment | Evidence / Notes |
|---|---|---|
| Confidentiality | [None / Limited / Significant / Unknown] | [Details] |
| Integrity | [None / Limited / Significant / Unknown] | [Details] |
| Availability | [None / Limited / Significant / Unknown] | [Details] |
| Financial | [Assessment] | [Details] |
| Operational | [Assessment] | [Details] |
| Customers | [Assessment] | [Details] |
| Third parties | [Assessment] | [Details] |
| Legal / Privacy | [Assessment] | [Details] |
| Reputation | [Assessment] | [Details] |

### Confirmed impact

[Document impact supported by evidence.]

### Potential impact

[Document plausible impact that could not be confirmed.]

### Unknowns

[Document outstanding uncertainty and any limitations in the investigation.]

## 5. Incident Timeline

| Timestamp | Event | Source | Significance |
|---|---|---|---|
| [Date and time] | [Event] | [Source] | [Explanation] |
| [Date and time] | [Event] | [Source] | [Explanation] |

**Timezone:** [UTC / Local timezone]

Include relevant detection, escalation, decision, containment, eradication and recovery events.

## 6. Root Cause Analysis

### Primary root cause

[Describe the underlying condition that allowed the incident to occur.]

### Contributing factors

| Factor | Description | Evidence |
|---|---|---|
| [Factor] | [How it contributed] | [Evidence reference] |
| [Factor] | [How it contributed] | [Evidence reference] |

### Control failures or gaps

[Identify controls that were absent, ineffective, misconfigured or bypassed.]

### Five Whys (optional)

**Problem statement:** [Describe the incident or failure being examined.]

1. **Why did this happen?**  
   [Answer]

2. **Why did that condition exist?**  
   [Answer]

3. **Why was the condition not prevented or detected?**  
   [Answer]

4. **Why did existing processes or controls not address it?**  
   [Answer]

5. **Why was the underlying weakness present?**  
   [Answer]

The Five Whys is a discussion aid, not proof that a single linear root cause exists. Use multiple causal paths where appropriate.

## 7. Detection Effectiveness

### What worked well?

- [Detection or monitoring capability]
- [Useful log source]
- [Effective alert or escalation]

### What could be improved?

- [Detection gap]
- [Missing telemetry]
- [Delayed alert or escalation]

### Detection metrics

| Metric | Result | Notes |
|---|---|---|
| Time to detect (TTD) | [Duration / Unknown] | [Start and end definitions] |
| Time to acknowledge | [Duration / Unknown] | [Details] |
| Time to escalate | [Duration / Unknown] | [Details] |
| Time to contain | [Duration / Unknown] | [Details] |
| Time to recover | [Duration / Unknown] | [Details] |

Document how each metric was calculated. Do not compare metrics across incidents unless their definitions are consistent.

## 8. Response Effectiveness

Evaluate the following:

| Area | Assessment | Findings |
|---|---|---|
| Initial triage | [Effective / Needs Improvement] | [Details] |
| Severity classification | [Effective / Needs Improvement] | [Details] |
| Escalation | [Effective / Needs Improvement] | [Details] |
| Investigation | [Effective / Needs Improvement] | [Details] |
| Evidence preservation | [Effective / Needs Improvement] | [Details] |
| Containment | [Effective / Needs Improvement] | [Details] |
| Eradication | [Effective / Needs Improvement] | [Details] |
| Recovery | [Effective / Needs Improvement] | [Details] |
| Communications | [Effective / Needs Improvement] | [Details] |
| Stakeholder coordination | [Effective / Needs Improvement] | [Details] |

## 9. What Went Well?

Record the controls, decisions, processes and collaboration that helped reduce impact.

- [Example]
- [Example]
- [Example]

## 10. What Could Be Improved?

Describe weaknesses and opportunities for improvement.

Focus on the process, systems, tools, information and operating conditions involved.

- [Improvement opportunity]
- [Improvement opportunity]
- [Improvement opportunity]

Avoid statements that simply blame an individual or team without identifying the underlying conditions.

## 11. Lessons Learned

| Lesson | Why it matters | Proposed improvement |
|---|---|---|
| [Lesson] | [Impact] | [Improvement] |
| [Lesson] | [Impact] | [Improvement] |

## 12. Corrective and Preventive Actions

Link the detailed action register.

| Action ID | Action | Priority | Owner | Due date | Status |
|---|---|---|---|---|---|
| [ACT-001] | [Description] | [Priority] | [Owner] | [Date] | [Status] |

Actions should address the underlying weakness rather than merely the symptoms observed during the incident.

## 13. Risk Acceptance and Outstanding Issues

| Outstanding issue | Risk | Owner | Decision / Treatment |
|---|---|---|---|
| [Issue] | [Risk description] | [Owner] | [Treatment] |

Document any residual risks that management has accepted, including the approving authority and review date.

## 14. Improvements to Security and Response Capability

Consider whether updates are required to:

- [ ] Incident response policy.
- [ ] Incident response playbooks.
- [ ] SIEM detection rules.
- [ ] EDR configuration.
- [ ] Identity and access controls.
- [ ] Network segmentation.
- [ ] Vulnerability management.
- [ ] Backup and recovery procedures.
- [ ] Logging and retention.
- [ ] Asset inventory.
- [ ] Security awareness.
- [ ] Third-party risk management.
- [ ] Incident escalation procedures.
- [ ] Staff training and exercises.

## 15. Review Conclusion

[Summarise the overall effectiveness of the response and the most important improvements required.]

### Final assessment

[What should the organisation take away from this incident?]

### Review approval

| Role | Name | Decision | Date |
|---|---|---|---|
| Review Facilitator | [Name] | [Approved / Pending] | [Date] |
| Incident Commander | [Name] | [Approved / Pending] | [Date] |
| Security Lead | [Name] | [Approved / Pending] | [Date] |
| Business Owner | [Name] | [Approved / Pending] | [Date] |

## 16. Follow-up

- [ ] Findings shared with relevant stakeholders.
- [ ] Corrective actions entered into the action register.
- [ ] Action owners assigned.
- [ ] Deadlines agreed.
- [ ] High-priority risks escalated.
- [ ] Playbooks and procedures reviewed.
- [ ] Follow-up review scheduled.
- [ ] Final review stored in the approved location.

**Next review date:** [Date]

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
