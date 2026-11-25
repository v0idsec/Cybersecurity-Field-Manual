# Incident Response Plan

> **Incident reference:** [INC-YYYY-NNN]
>
> **Handling:** [Internal / Confidential / Restricted]
>
> **Plan version:** [Version]
>
> **Plan owner:** [Name / Role]

## 1. Situation

### Incident summary

[Describe the incident and why this response plan is required.]

### Current status

[Open / Investigating / Contained / Recovering]

### Severity

[Critical / High / Medium / Low]

### Known impact

[Summarise known technical and business impact.]

## 2. Response Objectives

List the objectives in priority order.

1. [Protect people and critical operations.]
2. [Contain active compromise.]
3. [Preserve evidence.]
4. [Determine scope.]
5. [Remove attacker access.]
6. [Restore services.]
7. [Reduce recurrence risk.]

## 3. Response Team

| Role | Assigned person | Contact method | Responsibility |
|---|---|---|---|
| Incident Commander | [Name] | [Contact] | Overall coordination |
| Technical Lead | [Name] | [Contact] | Technical investigation |
| Security Analyst | [Name] | [Contact] | Detection and analysis |
| IT Operations | [Name] | [Contact] | Infrastructure support |
| Business Owner | [Name] | [Contact] | Business impact and approvals |
| Legal / Privacy | [Name] | [Contact] | Legal and privacy advice |
| Communications | [Name] | [Contact] | Approved messaging |

## 4. Authority and Approvals

Document who can approve:

| Action | Authorised role | Approval status |
|---|---|---|
| Disable user accounts | [Role] | [Pending / Approved] |
| Isolate endpoints | [Role] | [Pending / Approved] |
| Disable critical services | [Role] | [Pending / Approved] |
| Modify firewall rules | [Role] | [Pending / Approved] |
| Restore systems | [Role] | [Pending / Approved] |
| Notify external parties | [Role] | [Pending / Approved] |

Follow existing emergency authority arrangements where immediate action is necessary.

## 5. Scope

### Affected systems

[List known affected systems.]

### Affected identities

[List accounts, roles and applications.]

### Affected services

[List affected business services.]

### Potentially affected information

[List relevant information categories.]

### Known exclusions

[Record areas assessed and excluded, with supporting rationale.]

## 6. Investigation Plan

| Task | Assigned to | Priority | Status |
|---|---|---|---|
| [Review authentication activity] | [Owner] | [Priority] | [Status] |
| [Review endpoint telemetry] | [Owner] | [Priority] | [Status] |
| [Review network activity] | [Owner] | [Priority] | [Status] |
| [Assess data exposure] | [Owner] | [Priority] | [Status] |

### Key questions

- What was the initial access method?
- Is attacker activity ongoing?
- Which systems and identities are affected?
- Was data accessed or removed?
- Is persistence present?
- Are backups affected?
- Are third parties involved?

## 7. Containment Plan

| Action | Target | Owner | Approval | Status |
|---|---|---|---|---|
| [Action] | [System / Identity] | [Owner] | [Approver] | [Status] |

### Operational considerations

[Document dependencies, business impact, safety considerations and rollback requirements.]

## 8. Eradication Plan

| Action | Target | Owner | Completion criteria |
|---|---|---|---|
| [Remove persistence] | [Target] | [Owner] | [Criteria] |
| [Rotate credentials] | [Target] | [Owner] | [Criteria] |
| [Patch vulnerability] | [Target] | [Owner] | [Criteria] |

## 9. Recovery Plan

| Service / System | Recovery sequence | Owner | Validation |
|---|---|---|---|
| [Service] | [Steps] | [Owner] | [Checks] |

### Recovery dependencies

[List backup, identity, network, application and third-party dependencies.]

### Recovery approval

[Required approver and approval process.]

## 10. Communications

| Audience | Responsible role | Channel | Frequency |
|---|---|---|---|
| Executive management | [Role] | [Channel] | [Frequency] |
| IT / Security | [Role] | [Channel] | [Frequency] |
| Employees | [Role] | [Channel] | [Frequency] |
| Customers | [Role] | [Channel] | [As approved] |
| External parties | [Role] | [Channel] | [As approved] |

## 11. Risks and Dependencies

| Risk / Dependency | Impact | Mitigation | Owner |
|---|---|---|---|
| [Item] | [Impact] | [Mitigation] | [Owner] |

## 12. Decision Log

| Timestamp | Decision | Reason | Approved by |
|---|---|---|---|
| [Date and time] | [Decision] | [Reason] | [Role] |

## 13. Exit Criteria

- [ ] Active threat contained.
- [ ] Investigation scope sufficiently established.
- [ ] Known persistence removed.
- [ ] Credentials and secrets addressed.
- [ ] Recovery validated.
- [ ] Business owner approval obtained.
- [ ] Residual risks documented.
- [ ] Post-incident review scheduled.

## 14. Plan Approval

| Role | Name | Approval | Date |
|---|---|---|---|
| Incident Commander | [Name] | [Approval] | [Date] |
| Business Owner | [Name] | [Approval] | [Date] |

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
