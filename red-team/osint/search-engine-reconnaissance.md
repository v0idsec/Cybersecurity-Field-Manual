# Search Engine Reconnaissance

## Overview

Search engine reconnaissance uses search engines and indexed public content to discover information about an organisation.

Search engines can expose:
- Public documents.
- Forgotten subdomains.
- Development references.
- Public contact information.
- Technical documentation.
- Error messages.
- Publicly indexed directories.
- Historical or cached references.

Search operators help narrow results and identify information that may otherwise be difficult to locate.

## 1. Google Search Operators

| Operator | Purpose |
|---|---|
| `site:` | Restrict results to a domain |
| `filetype:` | Search for a specific file type |
| `intitle:` | Search page titles |
| `inurl:` | Search URLs |
| `intext:` | Search page content |
| `-` | Exclude a term |
| `OR` | Match either term |
| `" "` | Exact phrase |
| `before:` | Restrict results before a date |
| `after:` | Restrict results after a date |

### Domain Discovery

```text
site:example.com
site:*.example.com
site:example.com -www
```

### Document Discovery

```text
site:example.com filetype:pdf
site:example.com filetype:docx
site:example.com filetype:xlsx
site:example.com filetype:pptx
```

### Technology References

```text
site:example.com "powered by"
site:example.com "Microsoft Azure"
site:example.com "WordPress"
site:example.com "Jenkins"
```

### Public Development References

```text
site:example.com "staging"
site:example.com "development"
site:example.com "test environment"
site:example.com "internal"
```

These queries identify indexed references only. They do not establish that a system is accessible or vulnerable.

## 2. Bing Search Operators

Bing supports several useful search operators.

Examples:

```text
site:example.com
filetype:pdf site:example.com
intitle:login site:example.com
inurl:admin site:example.com
```

Search operator support and behaviour can change.

## 3. Public Document Discovery

Documents can disclose information that is not obvious from an organisation's website.

Potentially relevant document types:

- PDF.
- DOCX.
- XLSX.
- PPTX.
- CSV.
- TXT.

Review documents for:
- Publicly exposed contact details.
- Technology references.
- Internal project names.
- Document metadata.
- Historical organisational information.
- Accidental publication of non-public information.

Do not assume that an indexed document is intended for unrestricted distribution.

## 4. Publicly Indexed Technical Content

Search for references to:
- API documentation.
- Developer portals.
- Public source-code repositories.
- Technical support pages.
- Error messages.
- Public service endpoints.
- Configuration examples.

Example queries:

```text
site:example.com "api"
site:example.com "swagger"
site:example.com "openapi"
site:example.com "github.com"
site:example.com "connection string"
```

Treat discovered secrets or credentials as sensitive. Do not test them or use them to access systems without explicit authorisation.

## 5. Search Engine Result Limitations

Search results may be:
- Outdated.
- Cached.
- Incomplete.
- Incorrectly attributed.
- Duplicated.
- Removed from the source but still temporarily indexed.

A search result is not proof that the underlying content is currently available.

Visit the original source where appropriate and permitted. Record the original URL and collection time.

## 6. Search Automation

Tools such as theHarvester and SpiderFoot can automate portions of public information collection.

Automation should be configured to respect:
- Scope.
- Rate limits.
- API terms.
- Data handling requirements.
- Collection objectives.

Avoid large, indiscriminate searches that generate irrelevant personal information.

## 7. Reporting

For each relevant result, capture:

| Field | Description |
|---|---|
| Search engine | Google, Bing or other source |
| Query | Exact search query |
| Result URL | Original destination |
| Title | Indexed page title |
| Collection date | Date and time |
| Observation | Relevant information |
| Validation | Whether the source was checked |
| Confidence | Reliability of the finding |

## Operational Considerations

Search engine reconnaissance is generally passive, but opening results may directly interact with the destination website.

Do not download, execute or redistribute exposed files unnecessarily. If potentially sensitive information is discovered, preserve minimal evidence and follow the engagement's reporting and handling procedures.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
