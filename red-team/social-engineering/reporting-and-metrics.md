# Social Engineering Reporting and Metrics

## Overview

Social engineering reporting should explain how an organisation's people, processes and technical controls responded to the assessment.

A useful report identifies systemic weaknesses and provides practical improvements.

Avoid reducing the assessment to a single click rate or using results to shame individual employees.

## 1. Report Structure

A social engineering assessment report should include:

1. Executive summary.
2. Assessment objectives.
3. Scope and exclusions.
4. Rules of engagement.
5. Assessment methodology.
6. Scenarios performed.
7. Results and observations.
8. Metrics.
9. Findings.
10. Recommendations.
11. Limitations.
12. Post-engagement actions.

## 2. Useful Metrics

### Email Simulation

| Metric | Description |
|---|---|
| Delivery rate | Percentage of approved recipients receiving the message |
| Interaction rate | Percentage of recipients interacting with the simulation |
| Reporting rate | Percentage reporting the message through approved channels |
| Time to report | Time between delivery and first report |
| Escalation rate | Percentage reaching the appropriate security team |
| Verification rate | Percentage following required verification procedures |

### Voice and SMS

| Metric | Description |
|---|---|
| Response rate | Number of recipients responding |
| Verification rate | Percentage following identity verification |
| Escalation rate | Percentage escalating suspicious requests |
| Reporting rate | Percentage reporting suspicious calls or messages |
| Process adherence | Whether established procedures were followed |

### Physical Assessment

| Metric | Description |
|---|---|
| Challenge rate | Whether unauthorised access attempts were challenged |
| Visitor process adherence | Whether visitor procedures were followed |
| Badge control effectiveness | Whether badge controls operated as intended |
| Escalation rate | Whether suspicious activity was reported |
| Access outcome | Whether the approved test objective was achieved |

## 3. Metric Definitions

Define each metric before the assessment.

Example:

```text
Reporting Rate =
Number of unique recipients who reported the simulation
/
Number of recipients successfully delivered the simulation
× 100
```

Example:

```text
Interaction Rate =
Number of unique recipients who interacted with the simulation
/
Number of recipients successfully delivered the simulation
× 100
```

Define what counts as an interaction.

For example, automated security scanners may visit links and inflate click counts.

## 4. Interpret Results Carefully

Metrics require context.

Consider:
- Email security gateway behaviour.
- Automated link scanning.
- Duplicate reports.
- Message delivery failures.
- Role and workflow differences.
- Previous awareness training.
- Testing time and workload.
- Scenario difficulty.
- Reporting mechanism availability.

A high interaction rate does not automatically prove that employees are careless.

A low interaction rate does not prove that the organisation is secure.

## 5. Individual Versus Aggregate Results

Prefer aggregate reporting.

Individual-level results should only be retained where:
- Explicitly authorised.
- Necessary for the assessment objective.
- Consistent with organisational policy.
- Appropriately protected.

Do not publicly identify employees or create informal leaderboards.

## 6. Findings

Potential findings include:

| Finding | Example impact |
|---|---|
| Weak email reporting process | Suspicious messages may not reach security teams |
| Inconsistent identity verification | Unauthorised requests may be accepted |
| Poor supplier change controls | Payment redirection risk |
| Weak visitor management | Unauthorised physical access |
| Inadequate external sender indicators | Impersonation attempts may be harder to recognise |
| Unclear escalation procedures | Delayed incident response |

## 7. Severity Assessment

Consider:
- Likelihood of exploitation.
- Potential business impact.
- Sensitivity of affected processes.
- Existing technical controls.
- Frequency of the weakness.
- Ease of remediation.
- Potential for repeated exploitation.

A single simulation interaction should not automatically become a high-severity vulnerability.

## 8. Recommendations

Recommendations should address the underlying control weakness.

Examples:

| Weakness | Recommendation |
|---|---|
| Employees unsure how to report phishing | Improve reporting access and feedback |
| Supplier changes accepted through email alone | Require independent verification |
| Help desk verification inconsistent | Standardise identity verification |
| External sender identity unclear | Improve email security indicators |
| Visitors not consistently escorted | Strengthen visitor procedures |
| Suspicious calls not escalated | Provide clear reporting and escalation paths |
| Excessive trust in MFA prompts | Improve MFA fatigue awareness and authentication controls |

## 9. Evidence Handling

Retain only necessary evidence.

Examples:
- Approved simulation message.
- Campaign configuration.
- Aggregate results.
- Redacted screenshots.
- Relevant process observations.
- Approved access-control event references.
- Relevant incident or ticket references.

Avoid retaining:
- Passwords.
- MFA codes.
- Session tokens.
- Personal information unrelated to the objective.
- Unnecessary call recordings.
- Sensitive employee communications.

Define retention and deletion requirements before the engagement.

## 10. Debrief and Improvement

A debrief should:
- Explain what was tested.
- Explain the intended security behaviour.
- Identify positive outcomes.
- Discuss process weaknesses.
- Provide practical recommendations.
- Identify control owners.
- Establish follow-up actions.

Training should be constructive and relevant to the observed weaknesses.

## 11. Retesting

A follow-up assessment can determine whether improvements were effective.

Compare:
- Reporting behaviour.
- Verification adherence.
- Response times.
- Technical control effectiveness.
- Process consistency.

Use comparable scenarios and clearly document differences between assessments.

## 12. Final Quality Checklist

- [ ] Scope and authorisation documented.
- [ ] Assessment objective clearly stated.
- [ ] Scenarios described.
- [ ] Results validated.
- [ ] Metrics defined.
- [ ] Automated interactions considered.
- [ ] Individual data minimised.
- [ ] Findings linked to business impact.
- [ ] Recommendations are actionable.
- [ ] Evidence is appropriately redacted.
- [ ] Retention and deletion requirements addressed.
- [ ] Debrief completed.
- [ ] Follow-up actions assigned.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
