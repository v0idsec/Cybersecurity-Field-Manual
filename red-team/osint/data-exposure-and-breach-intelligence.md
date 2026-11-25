# Data Exposure and Breach Intelligence

## Overview

Data exposure and breach intelligence examines publicly available information that may indicate an organisation's data, credentials or systems have been exposed.

This can help identify risks associated with:
- Historical data breaches.
- Credential exposure.
- Public source-code repositories.
- Accidental document publication.
- Exposed cloud storage.
- Third-party data incidents.
- Publicly disclosed security events.

This activity must be conducted using lawful, authorised sources and appropriate data-handling procedures.

## 1. Breach Intelligence

Breach intelligence platforms aggregate information about publicly reported incidents and exposed accounts.

Useful sources include:

- Have I Been Pwned: https://haveibeenpwned.com/
- Flare: https://flare.io/
- DeHashed: https://dehashed.com/
- Intelligence X: https://intelx.io/

Availability, access requirements and permitted use vary by platform.

### Have I Been Pwned

Have I Been Pwned can help determine whether an email address or domain appears in supported breach datasets.

Useful capabilities:
- Email address exposure checks.
- Domain verification and monitoring.
- Breach notifications.
- Public breach context.

A breach listing does not prove that an account is currently compromised.

## 2. Flare

Flare provides digital risk protection and external threat intelligence capabilities.

https://flare.io/

Depending on the subscribed service and available features, investigations may cover:
- Exposed credentials.
- Infostealer-related exposure.
- Dark web intelligence.
- Brand impersonation.
- Third-party exposure.
- Corporate domain monitoring.
- Threat actor activity.

Potential assessment use cases:
- Identifying exposed corporate accounts.
- Reviewing historical exposure.
- Monitoring relevant organisation identifiers.
- Identifying third-party exposure affecting the organisation.
- Correlating intelligence with known assets.

### Investigation Considerations

For each result, record:
- Source platform.
- Observation date.
- Affected organisation or domain.
- Exposure type.
- Whether the information is historical or current.
- Confidence and validation status.
- Potential business impact.

Do not attempt to authenticate using discovered credentials.

## 3. SpiderFoot

SpiderFoot can automate the collection and correlation of information from multiple OSINT sources.

It can help identify:
- Domains and subdomains.
- Email addresses.
- IP addresses.
- Public infrastructure relationships.
- Breach-related references.
- Publicly indexed information.
- Technology indicators.

SpiderFoot results should be treated as intelligence leads.

Automated correlation can produce false positives, outdated records and incorrectly attributed information.

## 4. Public Source-Code Exposure

Public repositories can accidentally disclose:
- API keys.
- Access tokens.
- Passwords.
- Internal hostnames.
- Configuration details.
- Database connection strings.
- Infrastructure identifiers.

Relevant sources include:
- GitHub.
- GitLab.
- Bitbucket.
- Public package registries.
- Developer documentation.

Search only within the agreed scope and follow the engagement's evidence-handling requirements.

If a potential secret is discovered:
1. Record the repository and file location.
2. Capture minimal evidence.
3. Do not use the secret.
4. Do not test it against a service.
5. Notify the client through the agreed reporting channel.
6. Recommend rotation and review of associated access.

## 5. Exposed Cloud Storage

Publicly accessible cloud storage can result from misconfiguration or accidental publication.

Common platforms include:
- Amazon S3.
- Azure Blob Storage.
- Google Cloud Storage.

Potential indicators:
- Public bucket references.
- Public storage URLs.
- Exposed object listings.
- Public documentation containing storage endpoints.

Do not attempt to enumerate, download or modify data unless explicitly authorised.

A public URL does not necessarily indicate a security vulnerability. Some storage is intentionally public.

## 6. Third-Party Exposure

An organisation's data may be exposed through:
- Managed service providers.
- SaaS platforms.
- Marketing services.
- External development providers.
- Data processors.
- Former suppliers.

Validate the relationship before attributing an incident to the target organisation.

## 7. Exposure Classification

| Classification | Description |
|---|---|
| Public information | Intentionally available information |
| Accidental disclosure | Information made public unintentionally |
| Historical breach | Information associated with a past incident |
| Credential exposure | Credentials reported in an intelligence source |
| Active exposure | Current, independently verified exposure |
| Unverified intelligence | Potential exposure requiring confirmation |

## 8. Credential Handling

Credentials are sensitive security material.

During an OSINT engagement:
- Do not authenticate with discovered credentials unless explicitly authorised.
- Do not test credentials against external services.
- Do not copy complete credential datasets into reports.
- Redact passwords, tokens and session material.
- Notify the client promptly through approved channels.
- Recommend rotation and investigation where appropriate.

## 9. Reporting

A useful exposure report includes:
- Exposure category.
- Affected organisation or system.
- Source platform.
- Relevant dates.
- Minimal supporting evidence.
- Confidence.
- Business impact.
- Recommended remediation.
- Whether the exposure has been independently validated.

## Important Limitations

Breach intelligence sources may contain:
- Incorrect attribution.
- Recycled credentials.
- Duplicated records.
- Historical information.
- Incomplete datasets.
- Unverified claims.

Never present an intelligence-platform result as proof of an active compromise without supporting evidence.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
