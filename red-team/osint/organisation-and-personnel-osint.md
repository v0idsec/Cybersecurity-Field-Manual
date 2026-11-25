# Organisation and Personnel OSINT

## Overview

Organisation and personnel OSINT examines publicly available information about a business, its structure, technology, operations and professional workforce.

This information can help security teams understand an organisation's operating environment and identify potential security exposure.

Personnel research must be explicitly authorised and limited to legitimate assessment objectives.

## 1. Organisation Research

Start with official and independently verifiable sources.

Useful sources include:
- Corporate websites.
- Annual reports.
- Public company registers.
- Regulatory filings.
- Press releases.
- Public procurement records.
- Job advertisements.
- Published policies and technical documentation.

### Organisation Details

Record relevant information such as:

| Category | Information |
|---|---|
| Legal identity | Registered company name |
| Trading names | Publicly documented trading identities |
| Subsidiaries | Confirmed corporate relationships |
| Locations | Public business locations |
| Industry | Business sector |
| Suppliers | Publicly documented service providers |
| Technology | Publicly disclosed platforms |
| Contact channels | Official contact information |

In Australia, useful public resources include:

- ASIC: https://asic.gov.au/
- ABN Lookup: https://abr.business.gov.au/
- Australian Government business information: https://business.gov.au/

Do not infer ownership or corporate control solely from similar names or shared addresses.

## 2. Technology and Supplier Intelligence

Public information can reveal an organisation's technology environment.

Sources include:
- Job advertisements.
- Engineering blogs.
- Public technical documentation.
- Vendor case studies.
- Conference presentations.
- Public Git repositories.
- Procurement notices.

Look for references to:
- Cloud providers.
- Identity platforms.
- Endpoint management.
- SIEM and EDR platforms.
- Development frameworks.
- Programming languages.
- Infrastructure providers.
- Security vendors.

A job advertisement mentioning a technology is an indicator, not proof that the technology is currently deployed.

## 3. Personnel Discovery

Where authorised, personnel research can help establish organisational structure and identify relevant business functions.

Useful sources:
- Public professional networking profiles.
- Official staff directories.
- Conference speaker biographies.
- Public company announcements.
- Published research.
- Professional portfolios.

Relevant information may include:
- Public job title.
- Department.
- Business responsibilities.
- Public professional contact details.
- Publicly documented technical specialisations.

Avoid collecting unnecessary personal details.

## 4. Professional Relationship Mapping

Map professional relationships only where they are relevant to the assessment.

Examples:
- Publicly documented reporting structures.
- Department leadership.
- Security and IT responsibilities.
- Publicly documented suppliers.
- Technology partnerships.
- Business-unit relationships.

Distinguish between confirmed relationships and inferred relationships.

## 5. Contact Information

Public contact information can help identify organisational communication patterns.

Examples:
- `security@example.com`
- `support@example.com`
- `firstname.lastname@example.com`

Potential sources:
- Official contact pages.
- Public documentation.
- Public conference material.
- Search engines.
- theHarvester.
- Approved commercial intelligence platforms.

Do not use collected addresses for unsolicited contact, phishing or credential attacks without explicit written authorisation.

## 6. Email Pattern Analysis

Where sufficient public evidence exists, an organisation may use a predictable email format.

Common examples:

```text
firstname.lastname@example.com
firstinitiallastname@example.com
firstname@example.com
```

Treat inferred addresses as unverified.

Do not attempt mailbox enumeration or send test messages unless specifically authorised.

## 7. Organisational Attack-Surface Context

Combine organisational intelligence with technical findings.

For example:

- Public job advertisements identify a cloud platform.
- Official documentation identifies the organisation's email provider.
- Public DNS records reveal related service names.
- Public profiles identify relevant business units.
- Technology relationships help prioritise further assessment.

The objective is to develop useful context, not build unnecessary personal dossiers.

## 8. Reporting

A useful organisation intelligence summary includes:

- Confirmed organisation identifiers.
- Publicly documented subsidiaries and relationships.
- Relevant technology indicators.
- Publicly documented suppliers.
- Relevant professional roles.
- Source URLs and collection dates.
- Confidence and limitations.

## Privacy and Ethical Considerations

- Obtain approval before conducting personnel-focused research.
- Collect only information relevant to the engagement.
- Do not target private individuals outside the agreed scope.
- Avoid sensitive personal information unless specifically required and lawfully authorised.
- Do not contact personnel without approval.
- Do not use collected information to impersonate individuals.
- Handle personal information according to applicable privacy requirements.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
