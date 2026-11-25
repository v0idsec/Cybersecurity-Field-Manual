# Social Engineering Methodology

## Overview

A social engineering assessment evaluates the effectiveness of human processes and supporting technical controls when confronted with a defined manipulation scenario.

A professional engagement should be planned, measurable, proportionate and carefully controlled.

## 1. Define the Objective

Start with a specific security question.

Examples:
- Do employees report suspicious emails?
- Are unexpected payment requests independently verified?
- Does the help desk follow identity-verification procedures?
- Can unauthorised visitors enter controlled areas?
- Are employees comfortable challenging unfamiliar visitors?
- Are suspicious SMS messages reported?
- Do technical email controls identify simulation messages?

Avoid vague objectives such as "test employee awareness".

## 2. Establish Written Authorisation

The engagement must identify:

| Item | Required detail |
|---|---|
| Authorising party | Person or organisation approving the assessment |
| Assessment owner | Responsible engagement lead |
| Target population | Approved teams or employee groups |
| Channels | Email, phone, SMS or physical |
| Schedule | Approved testing window |
| Exclusions | Protected individuals, teams or locations |
| Data handling | Information that may be recorded |
| Emergency contact | Person able to stop the exercise |
| Stop conditions | Events requiring immediate suspension |

Approval for one channel does not automatically authorise another.

For example, approval for an email simulation does not authorise phone calls, physical access attempts or testing against suppliers.

## 3. Define Rules of Engagement

Document:
- Approved scenario types.
- Approved sender identities.
- Approved domains and phone numbers.
- Permitted delivery methods.
- Whether external recipients are excluded.
- Whether attachments are permitted.
- Whether landing pages are permitted.
- What events may be measured.
- Whether physical testing is permitted.
- Whether employees will be debriefed.
- Who receives individual-level results.

### Prohibited by Default

Unless separately approved and supported by appropriate safeguards, do not:
- Collect real passwords.
- Collect MFA codes.
- Access employee accounts.
- Install software on employee devices.
- Execute malware.
- Intercept live authentication sessions.
- Initiate payments or financial transfers.
- Request sensitive personal information.
- Threaten, harass or intimidate employees.
- Test emergency procedures in a way that could disrupt safety.

## 4. Select Assessment Scenarios

Choose scenarios that reflect realistic business risks.

| Scenario | Security control being assessed |
|---|---|
| Unexpected document notification | Email awareness and reporting |
| Password expiry message | Recognition of credential phishing |
| Supplier invoice change | Payment verification |
| Executive request | Authority and approval procedures |
| Unexpected phone call | Identity verification |
| Visitor requesting assistance | Physical access procedures |
| Unusual MFA notification | Authentication awareness |
| Unexpected parcel or delivery | Visitor and delivery procedures |

Scenarios should be relevant to the organisation's actual workflows.

## 5. Establish a Baseline

Before testing, understand existing controls.

Review:
- Security awareness training.
- Email filtering.
- External sender warnings.
- DMARC enforcement.
- Phishing-reporting mechanisms.
- Help desk verification procedures.
- Visitor management.
- Badge access controls.
- Incident escalation processes.

A simulation should assess the organisation as it operates, not an artificial environment with controls removed.

## 6. Prepare the Exercise

Define:
- Scenario.
- Audience.
- Delivery window.
- Expected employee behaviour.
- Measurement events.
- Technical dependencies.
- Safety controls.
- Response contacts.

Use a controlled simulation environment.

Where a landing page is used, it should not request or retain real credentials.

## 7. Execute the Assessment

During execution:
1. Confirm the approved window.
2. Confirm the target population.
3. Verify simulation infrastructure.
4. Confirm monitoring and stop contacts are available.
5. Deliver the approved scenario.
6. Monitor aggregate outcomes.
7. Stop immediately if unintended impact occurs.
8. Preserve relevant evidence.

Do not expand the target population or change the scenario without approval.

## 8. Measure Outcomes

Measure meaningful security behaviours.

Examples:
- Message delivery.
- Message opened, where reliably measurable.
- Link interaction.
- Reporting rate.
- Time to report.
- Help desk escalation.
- Verification procedure followed.
- Physical access challenge rate.
- Incident response time.

Avoid treating an email open or link click as proof that an employee lacks security awareness.

Tracking technologies can be affected by mail gateways, privacy controls and automated link scanning.

## 9. Debrief

A constructive debrief should:
- Explain the scenario.
- Identify warning signs.
- Explain the intended security behaviour.
- Provide a reporting route.
- Avoid naming and shaming individuals.
- Give teams an opportunity to ask questions.

## 10. Closeout

Confirm:
- Simulation infrastructure is disabled or retired.
- Test accounts and tokens are removed.
- Temporary access is revoked.
- Unneeded personal data is deleted.
- Evidence is retained according to the engagement agreement.
- Relevant stakeholders receive the results.

## 11. Assessment Quality

A strong engagement:
- Tests a defined security control.
- Uses realistic but proportionate scenarios.
- Protects employee privacy.
- Measures reporting and response, not just interaction.
- Includes technical and procedural context.
- Produces actionable recommendations.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
