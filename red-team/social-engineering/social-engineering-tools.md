# Social Engineering Tools

## Overview

This document lists commonly used tools for authorised social engineering assessments, phishing simulations, email analysis and human-factor testing.

Tools should support a defined assessment objective. They should not be used to collect real credentials, compromise accounts or conduct unauthorised impersonation.

---

# 1. GoPhish

https://github.com/gophish/gophish

<badge color="success">Phishing Simulation</badge>

GoPhish is an open-source phishing simulation platform.

### Common Use Cases

- Controlled email simulations.
- Landing page interaction measurement.
- Campaign management.
- Aggregate reporting.
- Security awareness exercises.

### Assessment Considerations

- Use an organisation-controlled sending domain.
- Use approved recipients only.
- Configure a safe landing page.
- Never retain real passwords.
- Avoid unnecessary personal tracking.
- Restrict access to campaign results.
- Retire infrastructure after the engagement.

GoPhish should be used as a simulation platform, not as a credential harvesting service.

---

# 2. Social-Engineer Toolkit (SET)

https://github.com/trustedsec/social-engineer-toolkit

<badge color="warning">Controlled Lab Use</badge>

SET is a framework for social engineering security testing.

### Common Use Cases

- Security awareness demonstrations.
- Controlled social engineering scenarios.
- Lab-based testing.
- Assessment research.

### Operational Considerations

SET includes capabilities that can interact with users and systems in potentially harmful ways.

Use only approved, isolated test environments and explicitly authorised scenarios.

Do not use it to capture real credentials, impersonate unrelated organisations or compromise production accounts.

---

# 3. King Phisher

https://github.com/rsmusllp/king-phisher

King Phisher is a phishing campaign toolkit historically used for security awareness testing.

### Common Use Cases

- Campaign management.
- Simulation tracking.
- Controlled landing pages.
- Awareness assessment.

### Assessment Considerations

Check the project's current maintenance and compatibility status before selecting it.

For many modern engagements, GoPhish is the more straightforward starting point.

---

# 4. Evilginx

https://github.com/kgretzky/evilginx2

<badge color="danger">High-Risk — Isolated Lab Only</badge>

Evilginx is an adversary-in-the-middle framework capable of intercepting authentication sessions.

This creates significant risk because it can capture session material rather than simply measure a simulation interaction.

### Appropriate Reference Context

- Understanding adversary-in-the-middle threats.
- Isolated security research.
- Controlled demonstrations using test identities.
- Evaluating phishing-resistant authentication concepts.

### Restrictions

Do not use this tool against real employee accounts or production authentication services as part of an ordinary phishing simulation.

Do not capture real session cookies, authentication tokens or MFA material.

Any live assessment involving adversary-in-the-middle techniques requires explicit written authorisation, test accounts, tightly controlled infrastructure and a separately approved test plan.

Prefer safer simulation methods when measuring employee awareness.

---

# 5. Microsoft Defender for Office 365

https://learn.microsoft.com/defender-office-365/

<badge>Defensive Validation</badge>

Relevant capabilities include:
- Attack Simulation Training.
- Anti-phishing policies.
- Safe Links.
- Safe Attachments.
- Threat Explorer.
- User reporting.
- Automated investigation and response.

Useful for evaluating both simulation outcomes and the organisation's email security controls.

---

# 6. Email Analysis Tools

## MXToolbox

https://mxtoolbox.com/

Useful for:
- MX record checks.
- SPF analysis.
- DKIM checks.
- DMARC checks.
- DNS diagnostics.
- Mail server configuration review.

## dig

DNS record lookup:

```bash
dig MX example.com
dig TXT example.com
dig TXT _dmarc.example.com
```

## nslookup

```bash
nslookup -type=MX example.com
nslookup -type=TXT example.com
```

---

# 7. Domain Intelligence

## crt.sh

https://crt.sh/

Certificate transparency search.

Useful for identifying publicly recorded certificates and associated hostnames.

## WHOIS / RDAP

Useful for reviewing domain registration metadata where publicly available.

Registration privacy and registry policies may limit the information returned.

## SpiderFoot

https://github.com/smicallef/spiderfoot

<badge color="success">OSINT and Reconnaissance</badge>

SpiderFoot automates open-source intelligence collection.

Potential uses in a social engineering assessment:
- Public domain discovery.
- Organisation footprint mapping.
- Public contact information discovery.
- Exposed infrastructure identification.
- External information exposure review.

Use only approved target organisations and avoid unnecessary collection of personal information.

## Maltego

https://www.maltego.com/

Useful for visualising relationships between:
- Domains.
- Organisations.
- Email addresses.
- Infrastructure.
- Public records.
- Other OSINT entities.

Use appropriate privacy controls and keep collection within the engagement scope.

---

# 8. Tool Selection

| Objective | Tools |
|---|---|
| Email phishing simulation | GoPhish |
| Controlled social engineering demonstrations | SET |
| Historical phishing simulation platform | King Phisher |
| Adversary-in-the-middle research | Evilginx, isolated lab only |
| Microsoft email security assessment | Defender for Office 365 |
| SPF, DKIM and DMARC review | MXToolbox, dig |
| Domain discovery | SpiderFoot, crt.sh |
| Relationship analysis | Maltego |
| DNS analysis | dig, nslookup |

---

# 9. Operational Checklist

- [ ] Tool use approved.
- [ ] Scope confirmed.
- [ ] Test infrastructure controlled.
- [ ] Recipient list approved.
- [ ] No real credential collection.
- [ ] No real authentication session capture.
- [ ] Data collection minimised.
- [ ] Results access restricted.
- [ ] Infrastructure retired after testing.
- [ ] Evidence handled securely.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
