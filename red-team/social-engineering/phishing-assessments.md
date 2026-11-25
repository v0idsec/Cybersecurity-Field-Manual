# Phishing Assessments

## Overview

Phishing assessments evaluate how employees and technical controls respond to suspicious email messages.

A controlled simulation can assess:
- Recognition of suspicious messages.
- Email reporting behaviour.
- Email security controls.
- Security awareness.
- Incident escalation.
- Response capability.

The objective is to test organisational resilience without collecting real credentials or compromising employee accounts.

## 1. Assessment Types

| Type | Description |
|---|---|
| General phishing | Broad simulation sent to an approved population |
| Spear phishing | Scenario tailored to a specific role or team |
| Credential phishing simulation | Controlled landing page measures interaction without retaining passwords |
| Attachment simulation | Safe, non-executable document or attachment scenario |
| Business email compromise | Tests verification of unusual business requests |
| Supplier impersonation | Tests external sender and supplier verification processes |

## 2. Planning

Before sending a simulation, establish:
- Written approval.
- Approved recipients.
- Sender identity.
- Sending domain.
- Testing window.
- Message content.
- Landing page behaviour.
- Measurement requirements.
- Exclusions.
- Incident escalation contacts.

Do not send simulations to customers, suppliers or other third parties unless they are explicitly included in scope.

## 3. Scenario Design

Use realistic business scenarios.

Examples:
- Document-sharing notification.
- Internal policy update.
- Meeting invitation.
- Unexpected invoice.
- Shared file notification.
- Delivery notification.
- Account security notification.

A scenario should test a defined behaviour rather than rely on extreme threats or distressing content.

## 4. Email Indicators

Evaluate whether recipients identify:
- Unexpected sender addresses.
- Lookalike domains.
- Unusual reply-to addresses.
- Unexpected attachments.
- Unexpected links.
- Urgent requests.
- Requests for credentials.
- Unusual payment instructions.
- Inconsistent branding.
- Unexpected authentication prompts.

## 5. Technical Email Controls

Review the organisation's ability to identify and manage suspicious messages.

Relevant controls:
- SPF.
- DKIM.
- DMARC.
- Secure email gateway.
- Attachment inspection.
- URL rewriting and scanning.
- External sender indicators.
- Mailbox reporting add-ins.
- Anti-phishing policies.
- Domain impersonation protection.

A simulation should not deliberately bypass production security controls unless that is an explicitly approved objective.

## 6. Safe Landing Pages

A simulation landing page should:
- Clearly operate within the approved exercise.
- Avoid requesting real passwords.
- Avoid collecting MFA codes.
- Avoid capturing authentication cookies.
- Record only necessary interaction events.
- Avoid unnecessary personal information.
- Provide an appropriate debrief.

A simulated credential form can record that a participant attempted to submit the form, but must not store the entered value.

Prefer a page that records an interaction event without accepting or transmitting user-entered credentials.

## 7. Safe Attachment Testing

If attachments are part of the assessment:
- Use harmless documents.
- Avoid executable payloads.
- Avoid macros.
- Avoid scripts.
- Avoid weaponised document formats.
- Do not bypass endpoint security without explicit approval.

A document interaction can be measured through a controlled link or other non-invasive event.

## 8. Delivery and Monitoring

Monitor:
- Delivery success.
- Mail gateway actions.
- Reported messages.
- Link interactions.
- Landing page interactions.
- Time to report.
- Help desk escalation.
- Security team response.

Account for automated mail scanners and link-preview systems.

A security gateway may visit links before the recipient does, producing misleading click data.

## 9. Reporting Behaviour

Evaluate whether employees:
- Use the official reporting mechanism.
- Forward suspicious messages appropriately.
- Notify the service desk or security team.
- Avoid replying to suspicious senders.
- Avoid entering credentials.
- Report suspicious MFA prompts.

The ability to report suspicious activity is often more valuable than whether an employee can identify every phishing indicator.

## 10. Analysis

Compare results by:
- Department.
- Business function.
- Location.
- Role type.
- Scenario.
- Delivery channel.

Use aggregated reporting where possible.

Avoid ranking individual employees or publishing identifiable results outside the authorised assessment team.

## 11. Remediation

Potential improvements:
- Improve email reporting mechanisms.
- Strengthen external sender indicators.
- Review DMARC enforcement.
- Improve suspicious link handling.
- Introduce payment verification procedures.
- Provide targeted awareness training.
- Improve incident escalation.
- Review mail gateway detections.

## 12. Reporting Requirements

Include:
- Assessment objective.
- Scope and exclusions.
- Scenario description.
- Delivery details.
- Technical controls observed.
- Aggregate outcomes.
- Reporting behaviour.
- Limitations.
- Recommendations.

A click rate alone is not a meaningful measure of organisational security.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
