# Phishing

Phishing is a social engineering technique used to deceive people into disclosing information, transferring money, opening malicious files or performing unauthorised actions.

This section covers defensive phishing analysis, investigation, response, threat intelligence and security awareness.

## Contents

| File | Description |
|---|---|
| [Email Analysis](email-analysis.md) | Analyse suspicious messages and identify phishing indicators |
| [Header Analysis](header-analysis.md) | Examine email headers and authentication results |
| [URL and Attachment Analysis](url-and-attachment-analysis.md) | Investigate suspicious links and files safely |
| [Phishing Investigation Workflow](phishing-investigation-workflow.md) | Structured investigation methodology |
| [Phishing Response and Containment](phishing-response-and-containment.md) | Contain phishing incidents and reduce impact |
| [Business Email Compromise](business-email-compromise.md) | Investigate account compromise and payment fraud |
| [Phishing Infrastructure and Indicators](phishing-infrastructure-and-indicators.md) | Identify infrastructure and indicators of compromise |
| [Phishing Tools Reference](phishing-tools-reference.md) | Common defensive investigation tools |

## Templates

The `templates/` directory contains reusable defensive documentation:

- Phishing report
- Phishing triage
- Phishing incident report
- Phishing awareness exercise
- Phishing simulation plan
- Suspicious email analysis
- User notification

## Investigation Principles

- Preserve the original message.
- Avoid opening suspicious attachments on production systems.
- Do not click suspicious links during initial triage.
- Record message headers and authentication results.
- Analyse URLs and files in controlled environments.
- Correlate email activity with endpoint and identity telemetry.
- Escalate suspected account compromise immediately.
- Document findings and evidence.
- Notify affected users using approved communication channels.

## Important Distinction

A suspicious email is not automatically a confirmed phishing incident.

Classify findings carefully:

- **Spam:** Unwanted or unsolicited communication.
- **Phishing:** Deceptive communication intended to manipulate recipients.
- **Malicious email:** A message containing or delivering malicious content.
- **Business Email Compromise (BEC):** Fraud involving impersonation or compromised business communications.
- **Confirmed compromise:** Evidence indicates an account, endpoint or other resource was accessed or affected.

## Authorisation

Phishing simulations and awareness exercises must have written approval, defined scope, appropriate safeguards and a clear process for handling participants who report or interact with simulated messages.

This section is intended for defensive investigation and authorised security awareness activities.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
