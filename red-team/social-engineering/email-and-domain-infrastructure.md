# Email and Domain Infrastructure

## Overview

Email infrastructure is a major part of phishing resilience.

This guide covers the assessment of email authentication, domain configuration, sender protection and simulation infrastructure.

The objective is to determine whether an organisation can reduce email impersonation and detect suspicious messages.

## 1. Domain Discovery

For an authorised organisation, identify:
- Primary email domains.
- Approved sending domains.
- Third-party email providers.
- Marketing platforms.
- Support platforms.
- Transactional email services.
- Legacy domains.
- Subdomains used for email.

Confirm domain ownership and testing scope before conducting active checks.

## 2. SPF

Sender Policy Framework (SPF) identifies which sending hosts are authorised to send email for a domain.

Query an SPF record:

```bash
dig TXT example.com
```

Look for:
- Whether an SPF record exists.
- Whether multiple SPF records exist.
- Unexpected authorised senders.
- Excessive DNS lookups.
- Incorrect mechanisms.
- Inappropriate use of permissive qualifiers.

Common SPF mechanisms include:

```text
ip4:
ip6:
include:
a
mx
exists:
all
```

An SPF record ending in `~all` is a soft fail, while `-all` is a hard fail.

The correct policy depends on the organisation's sending infrastructure.

## 3. DKIM

DomainKeys Identified Mail (DKIM) uses cryptographic signatures to help verify that messages were authorised by a domain.

DKIM records are published using selectors.

Example query:

```bash
dig TXT selector1._domainkey.example.com
```

Assess:
- Whether DKIM is configured.
- Whether all legitimate sending services sign messages.
- Selector management.
- Key length and algorithm.
- Rotation procedures.
- Legacy selectors.
- Third-party sender configuration.

Do not assume that a single selector represents every email service used by an organisation.

## 4. DMARC

Domain-based Message Authentication, Reporting and Conformance (DMARC) builds on SPF and DKIM alignment.

Query the DMARC record:

```bash
dig TXT _dmarc.example.com
```

Common policies:

```text
p=none
p=quarantine
p=reject
```

Review:
- Policy strength.
- SPF alignment.
- DKIM alignment.
- Aggregate reporting.
- Forensic reporting configuration.
- Subdomain policy.
- Percentage-based enforcement.
- Third-party sender alignment.

A monitoring-only policy may be appropriate during deployment, but organisations should understand the risks of leaving enforcement indefinitely disabled.

## 5. DNS and Mail Routing

Review:
- MX records.
- SPF records.
- DKIM selectors.
- DMARC records.
- Relevant CNAME records.
- Email provider dependencies.
- Domain ownership.
- DNS change management.

Example:

```bash
dig MX example.com
dig TXT example.com
dig TXT _dmarc.example.com
```

## 6. Lookalike Domain Risk

Assess whether the organisation has obvious lookalike domains that could be used for impersonation.

Consider:
- Typographical variations.
- Character substitutions.
- Hyphenation.
- Similar domain extensions.
- Confusing subdomains.
- Internationalised domain names.

Use reputable domain intelligence and certificate transparency sources where appropriate.

Do not register or activate lookalike domains without explicit authorisation.

## 7. Certificate Transparency

Certificate transparency logs can reveal certificates issued for publicly visible domains.

Useful services:
- crt.sh
- Certificate Transparency search interfaces.
- Commercial attack surface management platforms.

Example:

```text
https://crt.sh/?q=%25.example.com
```

Review discovered hostnames against the authorised scope.

A hostname appearing in a certificate log does not prove that the service is active or vulnerable.

## 8. Simulation Infrastructure

A phishing simulation should use infrastructure controlled by the assessment team.

Requirements:
- Approved sending domain.
- Approved sender identity.
- Valid TLS configuration.
- Appropriate email authentication.
- Controlled landing page.
- Minimal event collection.
- Clear debrief process.
- Defined data retention.
- No real credential collection.

Do not use a third-party organisation's domain or email infrastructure without permission.

## 9. Email Security Controls

Review:
- Secure email gateway configuration.
- Anti-spoofing controls.
- External sender indicators.
- URL scanning.
- Attachment inspection.
- Impersonation protection.
- Mailbox reporting.
- Automated response workflows.
- DMARC reporting and enforcement.

## 10. Reporting

Document:
- Domain.
- DNS records.
- Authentication status.
- Sending infrastructure.
- Identified weaknesses.
- Potential impersonation risk.
- Evidence.
- Recommended remediation.

Avoid publishing sensitive internal email infrastructure details in public reports.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
