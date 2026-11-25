# Technology and Asset Discovery

## Overview

Technology and asset discovery identifies an organisation's publicly visible technologies, services and internet-facing assets.

The objective is to understand the external attack surface and identify assets that may require further assessment.

This guide covers passive discovery and controlled validation. Active scanning and testing must be explicitly authorised.

## 1. Technology Fingerprinting

Technology fingerprinting uses observable information to identify the platforms and services used by a website or application.

Potential indicators include:
- HTTP response headers.
- HTML source.
- JavaScript references.
- Cookies.
- URL structures.
- Public documentation.
- Certificate information.
- Error pages.
- Public technology profiles.

### Browser-Based Inspection

Review:
- Page source.
- Loaded JavaScript.
- CSS references.
- HTTP response headers.
- Cookie names and attributes.
- Publicly exposed framework information.

### HTTP Headers

Where direct requests are authorised:

```bash
curl -I https://example.com
```

Verbose response:

```bash
curl -sS -D - -o /dev/null https://example.com
```

Headers may disclose:
- Web server software.
- Framework information.
- CDN or proxy providers.
- Security headers.
- Caching behaviour.

Header values can be modified or hidden, so they are indicators rather than definitive proof.

## 2. Technology Identification Tools

### Wappalyzer

Identifies technologies used by websites.

https://www.wappalyzer.com/

Useful for:
- Content management systems.
- JavaScript frameworks.
- Analytics platforms.
- Web servers.
- E-commerce platforms.
- Hosting and infrastructure indicators.

### WhatWeb

Command-line technology fingerprinting.

```bash
whatweb https://example.com
```

Detailed output:

```bash
whatweb -v https://example.com
```

Only run against authorised targets.

### BuiltWith

https://builtwith.com/

Useful for:
- Historical technology information.
- Website technology profiles.
- Hosting and analytics indicators.
- Technology relationships.

Technology profiles may be historical or incomplete.

## 3. Internet-Facing Asset Discovery

External assets may include:

- Websites.
- APIs.
- VPN portals.
- Remote access gateways.
- Mail services.
- Authentication portals.
- Cloud-hosted applications.
- Development environments.
- Public infrastructure.

Useful discovery sources:
- Shodan.
- Censys.
- SecurityTrails.
- Certificate transparency.
- Amass.
- SpiderFoot.
- Flare.

## 4. Shodan

Shodan indexes internet-connected services and devices.

https://www.shodan.io/

Useful search examples:

```text
hostname:example.com
domain:example.com
org:"Example Corporation"
ssl.cert.subject.cn:example.com
```

Other useful filters:

```text
port:443 hostname:example.com
port:22 hostname:example.com
product:"nginx" hostname:example.com
```

Search syntax and available filters may change.

Shodan results are observations from its own scanning infrastructure. They may not reflect the current state of a service.

## 5. Censys

Censys provides internet infrastructure and certificate intelligence.

https://search.censys.io/

Useful search concepts:
- Hostname.
- IP address.
- Certificate subject.
- Certificate Subject Alternative Names.
- Service ports.
- TLS configuration.
- Autonomous system information.

Use the current Censys search language and documentation for query syntax.

## 6. Attack-Surface Mapping

Build an asset inventory that distinguishes confirmed assets from potential relationships.

Suggested structure:

| Asset | Type | Source | Ownership confidence | Status |
|---|---|---|---|---|
| www.example.com | Website | DNS | High | Confirmed |
| api.example.com | API | Certificate transparency | Medium | Unverified |
| 203.0.113.10 | IP | DNS resolution | Medium | Third-party hosted |
| vpn.example.com | Remote access | Search result | Medium | Requires validation |

Use a consistent status model:

- Confirmed.
- Probable.
- Historical.
- Unverified.
- Out of scope.
- Third-party managed.

## 7. Asset Validation

Before conducting active testing:

1. Confirm the asset is within scope.
2. Establish ownership or an approved testing relationship.
3. Confirm the asset is currently active.
4. Identify third-party hosting dependencies.
5. Check the rules of engagement.
6. Determine whether scanning is permitted.
7. Record the validation method.

Do not scan shared cloud or hosting infrastructure simply because a target domain resolves to an address within it.

## 8. Prioritisation

Prioritise assets based on:
- Internet exposure.
- Business criticality.
- Authentication requirements.
- Data sensitivity.
- Known vulnerabilities.
- Technology age.
- External accessibility.
- Confidence in ownership.

An exposed service is not automatically a vulnerability.

## 9. Reporting

Useful deliverables include:
- External asset inventory.
- Technology profile.
- Hosting and provider map.
- Potentially forgotten services.
- Publicly visible authentication portals.
- Unverified assets requiring client confirmation.
- Relevant security observations.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
