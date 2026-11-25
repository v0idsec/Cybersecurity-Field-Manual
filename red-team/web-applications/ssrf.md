# Server-Side Request Forgery (SSRF)

## Overview

Server-Side Request Forgery (SSRF) is a vulnerability that allows an attacker to influence requests made by a server.

Rather than making a request directly from their own device, an attacker manipulates an application into making a request on their behalf.

SSRF can expose internal services, bypass network boundaries, interact with cloud infrastructure and access resources that are not publicly reachable.

This guide covers SSRF identification, safe testing techniques, common attack surfaces and defensive controls.

> **Authorisation:** Only test systems explicitly included in your engagement scope. Use controlled endpoints and test infrastructure. Do not access internal services or sensitive metadata unless explicitly authorised.

---

## Table of Contents

1. [How SSRF Works](#how-ssrf-works)
2. [Common Attack Surfaces](#common-attack-surfaces)
3. [Types of SSRF](#types-of-ssrf)
4. [Reconnaissance and Discovery](#reconnaissance-and-discovery)
5. [Testing Methodology](#testing-methodology)
6. [Common SSRF Weaknesses](#common-ssrf-weaknesses)
7. [Cloud and Internal Network Risks](#cloud-and-internal-network-risks)
8. [Tools](#tools)
9. [Remediation](#remediation)
10. [Reporting](#reporting)
11. [Testing Checklist](#testing-checklist)
12. [References](#references)

---

## 1. How SSRF Works

An application may accept a URL from a user and retrieve its contents from the server.

For example:

1. A user submits a URL to an image import feature.
2. The application receives the URL.
3. The backend makes an HTTP request to retrieve the image.
4. The application returns or processes the response.

If the application does not properly validate the destination, a user may influence the server into requesting unintended resources.

### Basic example

Imagine an application has an image import feature:

```text
https://example.com/import-image?url=https://images.example.org/photo.png
```

The application retrieves the supplied URL from its backend.

During an authorised assessment, the objective is to determine whether the destination can be controlled beyond the application's intended use.

### Why it matters

Potential consequences include:

- Access to internal-only services.
- Exposure of information from unintended endpoints.
- Interaction with services behind network boundaries.
- Abuse of trusted server-side network access.
- Access to cloud infrastructure endpoints.
- Unauthorised actions against internal applications.

The actual impact depends on network architecture, application permissions and the response-handling behaviour.

---

## 2. Common Attack Surfaces

Look for application functionality that retrieves, imports, previews or processes remote resources.

| Feature | Potential SSRF surface |
|---|---|
| Webhooks | Server sends requests to configured destinations |
| Image import | Backend retrieves remote images |
| PDF generation | Renderer loads external resources |
| URL preview | Application fetches page metadata |
| File import | Backend downloads remote files |
| RSS feeds | Server retrieves feed URLs |
| Document conversion | Processing service loads remote content |
| Link checking | Backend checks destination availability |
| Integrations | Application communicates with third-party services |
| Avatar import | Application retrieves remote profile images |

### Parameters worth reviewing

Look for parameters that accept URLs, hostnames or remote resource identifiers.

Examples:

```text
url=
uri=
target=
dest=
destination=
redirect=
callback=
webhook=
image=
image_url=
file=
feed=
host=
endpoint=
```

These names are discovery hints, not proof of a vulnerability.

---

## 3. Types of SSRF

### 3.1 Basic SSRF

The application makes a server-side request to a user-controlled destination and exposes some of the response.

The response may be displayed directly, stored, or processed by another application component.

### 3.2 Blind SSRF

The application makes a request, but the response is not returned to the user.

Detection may rely on observing a request arrive at an external endpoint that you control.

Blind SSRF can still be significant, even when the application does not display the response.

### 3.3 Stored SSRF

A supplied URL is stored and retrieved later by a background process.

Examples include:

- Scheduled webhook delivery.
- Background image processing.
- Periodic feed retrieval.
- Asynchronous document processing.

A request may therefore occur long after the original user action.

### 3.4 Second-order SSRF

The application stores user-controlled data, which is later used in a server-side request by another component.

This can make the vulnerable input difficult to identify because the initial submission may appear harmless.

---

## 4. Reconnaissance and Discovery

### 4.1 Map URL-consuming functionality

Browse the application and identify features that retrieve external content.

Record:

- Feature name.
- Request method.
- Endpoint.
- Relevant parameters.
- Authentication requirements.
- Whether the response is visible.
- Whether processing happens immediately or asynchronously.

### 4.2 Review application requests

Use Burp Suite Proxy or browser developer tools to inspect requests.

Look for:

- URL parameters.
- JSON fields containing URLs.
- Webhook configuration.
- Import functionality.
- Redirect destinations.
- Remote resource references.

### 4.3 Review JavaScript

Search available client-side JavaScript for references to:

```text
fetch(
XMLHttpRequest
webhook
callback
image_url
import
preview
```

Client-side code may reveal functionality or API endpoints that are not immediately obvious through normal browsing.

### 4.4 Build an input inventory

Keep track of every potential URL input.

| Endpoint | Parameter | Method | Feature | Notes |
|---|---|---|---|---|
| `/api/preview` | `url` | POST | Link preview | Response visible |
| `/api/import` | `source` | POST | File import | Background processing |
| `/settings/webhook` | `callback` | POST | Webhook | Authenticated |

Use this as a working inventory, not as evidence that an endpoint is vulnerable.

---

## 5. Testing Methodology

### 5.1 Establish a baseline

Before testing, submit a normal, publicly accessible URL that is appropriate for the feature.

Record:

- The request.
- The response.
- Processing time.
- Any returned content.
- Any errors.
- Whether the application follows redirects.

This gives you a baseline for comparison.

### 5.2 Use a controlled callback endpoint

For blind SSRF testing, use an endpoint that you own or are explicitly authorised to use.

Suitable options include:

- Burp Collaborator.
- Interactsh.
- An engagement-controlled HTTP server.
- A dedicated test domain.

Submit the controlled URL through the suspected feature.

Observe whether the application makes a request to your endpoint.

Record:

- Whether a request arrived.
- Timestamp.
- HTTP method.
- Request headers.
- Source information exposed by the service.
- Whether the request was repeated.

A callback is evidence of server-side interaction, but it does not automatically establish access to internal resources or a particular severity.

### 5.3 Compare behaviour

Compare normal and controlled destinations.

Look for differences in:

- Response status.
- Response body.
- Error messages.
- Processing time.
- Redirect behaviour.
- Callback activity.

### 5.4 Test validation boundaries safely

Assess whether the application restricts destinations to an intended set of hosts.

Questions to investigate:

- Does it allow only approved domains?
- Are subdomains handled correctly?
- Are redirects validated?
- Does it reject unexpected URL schemes?
- Does it handle IPv4 and IPv6 consistently?
- Does it validate the final resolved destination?
- Are malformed URLs rejected safely?

Use controlled test infrastructure and avoid probing private or internal systems unless the engagement explicitly permits it.

### 5.5 Test asynchronous processing

For features that process URLs in the background:

1. Submit a controlled test URL.
2. Record the submission time.
3. Monitor your callback endpoint.
4. Check for delayed requests.
5. Repeat only as necessary to establish reproducibility.

Be mindful of queues, retries and scheduled jobs. Avoid creating excessive requests.

---

## 6. Common SSRF Weaknesses

### 6.1 Weak URL validation

Applications may validate a URL using incomplete string matching rather than a proper URL parser.

For example, checking whether a URL contains an approved domain name is not a reliable way to establish its actual destination.

**Assessment focus:**

- Exact hostname validation.
- Correct URL parsing.
- Normalisation before validation.
- Handling of unusual but valid URL representations.

### 6.2 Redirect handling

An application may validate the initial URL but automatically follow redirects.

If the redirect destination is not checked, the final request may go somewhere the original validation intended to prevent.

**Assessment focus:**

- Whether redirects are followed.
- Whether each redirect destination is validated.
- Whether redirect limits are enforced.
- Whether redirects can cross trust boundaries.

### 6.3 DNS resolution issues

An application may validate a hostname and later resolve it separately when making the request.

This can create inconsistencies between the address that was checked and the address that was contacted.

**Assessment focus:**

- DNS resolution behaviour.
- Whether validation and connection use consistent results.
- Whether private or reserved destinations are rejected.
- Whether DNS changes are handled safely.

### 6.4 Unrestricted URL schemes

Applications that accept arbitrary URL schemes may expose unexpected functionality in the underlying HTTP client or processing library.

**Assessment focus:**

- Whether only required schemes are accepted.
- Whether unsupported schemes are rejected.
- Whether the application uses a restricted HTTP client.

### 6.5 IPv4 and IPv6 handling

Destination validation must account for both IPv4 and IPv6.

A filter that checks only familiar IPv4 representations may be incomplete.

**Assessment focus:**

- IPv4 and IPv6 parsing.
- Loopback addresses.
- Private address ranges.
- Link-local addresses.
- IPv4-mapped IPv6 addresses.
- Normalisation and canonicalisation.

---

## 7. Cloud and Internal Network Risks

SSRF can be particularly serious in cloud environments.

### 7.1 Internal services

Applications often communicate with internal services that are not intended to be publicly accessible.

Examples include:

- Internal APIs.
- Monitoring services.
- Administrative interfaces.
- Service discovery systems.
- Database management interfaces.

A vulnerable server-side request feature may unintentionally expose access to these systems.

Do not probe internal services during an engagement unless the relevant targets and techniques are explicitly authorised.

### 7.2 Cloud metadata services

Cloud platforms may provide metadata services that expose information about the environment in which an application runs.

Depending on configuration and platform protections, metadata may contain sensitive information or temporary credentials.

**Assessment considerations:**

- Is metadata access restricted?
- Are platform-specific protections enabled?
- Are workloads using least-privilege identities?
- Is metadata access logged or monitored?
- Can application workloads reach metadata services unnecessarily?

Do not retrieve credentials, tokens or sensitive metadata as proof of impact. Use documented, non-sensitive evidence or a controlled cloud lab.

### 7.3 Network segmentation

SSRF can reveal weaknesses in network segmentation where an internet-facing application has broader internal network access than necessary.

Defenders should ensure that application servers can communicate only with the services they genuinely require.

---

## 8. Tools

| Tool | Purpose |
|---|---|
| Burp Suite | Intercept and modify application requests |
| Burp Collaborator | Observe out-of-band interactions |
| Interactsh | Controlled out-of-band interaction testing |
| OWASP ZAP | Web application assessment |
| curl | Inspect HTTP behaviour against authorised endpoints |
| Browser Developer Tools | Review requests and client-side behaviour |
| Wireshark | Analyse traffic in a controlled lab |
| Python | Build controlled test clients and validation scripts |

### Burp Suite

Useful functionality:

- Proxy: inspect application requests.
- Repeater: modify and resend requests.
- Logger: review request history.
- Collaborator: identify out-of-band interactions.

### Interactsh

Interactsh can provide controlled callback infrastructure for identifying blind interactions.

Use a dedicated test instance or an approved service according to the engagement's data-handling requirements.

Avoid submitting confidential application data to third-party callback services.

---

## 9. Remediation

### 9.1 Use destination allowlists

Where possible, define an explicit list of permitted destinations.

Prefer exact hostnames and approved ports over broad domain matching.

### 9.2 Parse and normalise URLs

Use a reputable URL parsing library.

Validate the parsed scheme, hostname, port and path rather than relying on string matching.

### 9.3 Restrict network destinations

Reject destinations that resolve to:

- Loopback addresses.
- Private network ranges.
- Link-local addresses.
- Reserved or otherwise prohibited address ranges.

Apply the policy to both IPv4 and IPv6.

### 9.4 Validate redirects

If redirects are required:

- Limit the number of redirects.
- Validate every redirect destination.
- Reapply destination restrictions after each redirect.
- Reject redirects to prohibited networks.

### 9.5 Protect DNS resolution

Ensure that destination validation and the actual connection cannot be separated by an unsafe DNS resolution process.

Use consistent resolution and connection handling, and account for DNS rebinding risks.

### 9.6 Apply network-level controls

Application validation should not be the only defence.

Use:

- Egress firewall rules.
- Network segmentation.
- Restricted outbound proxies.
- Explicit destination policies.
- Cloud metadata protections.

### 9.7 Restrict the HTTP client

Where practical:

- Allow only required protocols.
- Disable unnecessary features.
- Set connection and response timeouts.
- Limit response sizes.
- Restrict redirect behaviour.
- Avoid forwarding sensitive headers.
- Run URL-fetching processes with minimal privileges.

### 9.8 Monitor suspicious activity

Log and alert on:

- Unexpected outbound destinations.
- Requests to private or reserved address ranges.
- Repeated failed URL validations.
- Unusual redirect chains.
- Unexpected DNS resolution results.
- Unusual outbound traffic from application servers.

Ensure logs do not unnecessarily capture sensitive URL parameters or credentials.

---

## 10. Reporting

A useful SSRF report should demonstrate the server-side request without unnecessarily accessing sensitive systems.

### Suggested report structure

**Title:** Server-Side Request Forgery in [Feature / Endpoint]

**Summary:**

Describe the functionality that accepts a user-controlled URL and explain how the backend processes it.

**Affected endpoint:**

```text
POST /api/example
```

**Affected parameter:**

```text
url
```

**Steps to reproduce:**

1. Authenticate using an authorised test account, if required.
2. Navigate to the affected functionality.
3. Submit a URL pointing to an engagement-controlled callback endpoint.
4. Observe the request arriving at the controlled endpoint.
5. Include relevant application and callback evidence.

**Evidence:**

- Sanitised HTTP request.
- Sanitised HTTP response.
- Callback timestamp.
- Relevant callback request details.
- Screenshots where useful.

**Impact:**

Explain what the demonstrated behaviour allows an attacker to do, and distinguish confirmed impact from potential impact.

**Remediation:**

Recommend destination allowlisting, strict URL parsing, redirect validation, DNS protections and outbound network restrictions.

---

## 11. Testing Checklist

### Discovery

- [ ] Identify URL-consuming features.
- [ ] Review URL-related parameters.
- [ ] Inspect API requests.
- [ ] Review relevant JavaScript.
- [ ] Identify background processing functionality.

### Validation

- [ ] Establish normal application behaviour.
- [ ] Test with a controlled callback endpoint.
- [ ] Check for blind SSRF.
- [ ] Check whether requests are asynchronous.
- [ ] Review redirect handling.
- [ ] Review URL scheme restrictions.
- [ ] Assess IPv4 and IPv6 validation.
- [ ] Review DNS validation behaviour.

### Impact and evidence

- [ ] Confirm server-side interaction.
- [ ] Identify the affected application component.
- [ ] Avoid accessing sensitive internal resources.
- [ ] Capture reproducible evidence.
- [ ] Distinguish confirmed impact from theoretical impact.

### Reporting

- [ ] Document the affected endpoint.
- [ ] Include sanitised requests and responses.
- [ ] Include callback evidence where relevant.
- [ ] Explain realistic impact.
- [ ] Provide practical remediation guidance.

---

## 12. References

- [OWASP Web Security Testing Guide — Testing for SSRF](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
- [PortSwigger — Server-Side Request Forgery](https://portswigger.net/web-security/ssrf)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [Interactsh](https://github.com/projectdiscovery/interactsh)
- [MITRE CWE-918 — Server-Side Request Forgery](https://cwe.mitre.org/data/definitions/918.html)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
