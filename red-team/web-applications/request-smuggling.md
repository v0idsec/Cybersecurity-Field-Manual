
# HTTP Request Smuggling

> Professional reference guide for assessing HTTP request desynchronisation and inconsistent request parsing across HTTP infrastructure.

## Contents

- [Overview](#overview)
- [HTTP Message Framing](#http-message-framing)
- [Infrastructure and Trust Boundaries](#infrastructure-and-trust-boundaries)
- [Request Smuggling Classes](#request-smuggling-classes)
- [HTTP/2 Request Smuggling](#http2-request-smuggling)
- [Assessment Methodology](#assessment-methodology)
- [Validation Techniques](#validation-techniques)
- [Potential Impact](#potential-impact)
- [False Positives and Limitations](#false-positives-and-limitations)
- [Mitigation](#mitigation)
- [Evidence Collection](#evidence-collection)
- [Tools and References](#tools-and-references)
- [Assessment Checklist](#assessment-checklist)

---

## Overview

HTTP Request Smuggling occurs when two or more HTTP components interpret the boundaries of HTTP requests differently.

A typical architecture may contain:

1. Client
2. CDN or edge proxy
3. Web application firewall
4. Load balancer
5. Reverse proxy
6. Backend application server

If these components disagree about where one request ends and another begins, an attacker may be able to influence how subsequent requests are interpreted.

The vulnerability is particularly relevant to systems that reuse HTTP connections between infrastructure components.

Potential consequences include:

- Request queue poisoning.
- Front-end and back-end desynchronisation.
- Access control bypass.
- Web cache poisoning.
- Request routing manipulation.
- Credential or session exposure.
- Cross-user request interference.

Request smuggling is an infrastructure-level issue that can have application-level consequences.

## HTTP Message Framing

HTTP/1.1 uses message framing to determine where a request body ends.

Two important headers are:

| Header | Purpose |
|---|---|
| `Content-Length` | Specifies the length of the message body in bytes |
| `Transfer-Encoding` | Specifies the transfer coding applied to the message body |

Disagreement between these mechanisms can result in inconsistent request interpretation.

### Content-Length

```http
POST /submit HTTP/1.1
Host: example.com
Content-Length: 12

hello=world
```

The receiving component uses the declared length to determine the end of the body.

### Transfer-Encoding

```http
POST /submit HTTP/1.1
Host: example.com
Transfer-Encoding: chunked

5
hello
0
```

Chunked transfer encoding uses explicit chunk lengths and a terminating zero-length chunk.

### Ambiguous Framing

The presence of conflicting or inconsistently interpreted framing information can create a desynchronisation condition.

Assessment should consider:

- Duplicate `Content-Length` headers.
- Conflicting `Content-Length` values.
- Multiple `Transfer-Encoding` headers.
- Invalid transfer coding.
- Header normalisation differences.
- Whitespace and formatting differences.
- Intermediary behaviour when receiving malformed requests.

Do not assume that every unusual framing response represents an exploitable vulnerability.

## Infrastructure and Trust Boundaries

Map the HTTP request path before testing.

Consider:

| Component | Assessment considerations |
|---|---|
| CDN | HTTP protocol support, request normalisation |
| WAF | Header inspection and forwarding behaviour |
| Load balancer | Connection reuse and request parsing |
| Reverse proxy | Protocol translation and framing |
| Application server | HTTP parser implementation |
| API gateway | Routing and request transformation |

Important questions:

- Does the edge terminate HTTP connections?
- Is HTTP/2 translated into HTTP/1.1?
- Are backend connections reused?
- Are multiple users sharing backend connections?
- Do different application routes use different infrastructure?
- Are there multiple proxy layers?
- Does the infrastructure normalise malformed requests?

The objective is to identify where request interpretation changes.

## Request Smuggling Classes

### CL.TE

The front-end component prioritises `Content-Length`, while the back-end component prioritises `Transfer-Encoding`.

This disagreement can cause the components to identify different request boundaries.

### TE.CL

The front-end component prioritises `Transfer-Encoding`, while the back-end component prioritises `Content-Length`.

The resulting discrepancy can produce request desynchronisation.

### TE.TE

Both components support `Transfer-Encoding`, but interpret or process the header differently.

Differences may arise from:

- Header obfuscation.
- Duplicate headers.
- Whitespace handling.
- Header normalisation.
- Invalid transfer coding.

### Related Desynchronisation Issues

Not every desynchronisation vulnerability is a conventional CL.TE or TE.CL issue.

Also consider:

- Response queue desynchronisation.
- Client-side desynchronisation.
- HTTP/2 downgrade issues.
- Connection state inconsistencies.
- Incorrect handling of malformed requests.

## HTTP/2 Request Smuggling

HTTP/2 uses binary framing rather than HTTP/1.1's textual message framing.

However, request smuggling can still occur when HTTP/2 traffic is translated into HTTP/1.1 by an intermediary.

Relevant scenarios include:

| Class | Description |
|---|---|
| H2.CL | HTTP/2 request translated into HTTP/1.1 with conflicting length information |
| H2.TE | HTTP/2 to HTTP/1.1 translation introduces inconsistent transfer coding |
| H2 downgrade | Different protocol handling between front-end and back-end |
| HTTP/2 normalisation | Intermediary transforms headers or request framing inconsistently |

Assessment considerations:

- HTTP/2 pseudo-header handling.
- `:authority` and `Host` consistency.
- Header translation.
- Invalid or unexpected header handling.
- Content-length validation.
- Protocol downgrade behaviour.
- Connection reuse after protocol translation.

HTTP/2 support alone does not establish that a target is vulnerable.

## Assessment Methodology

### 1. Establish Scope

Confirm:

- Explicit authorisation for protocol-level testing.
- Approved domains and infrastructure.
- Whether CDN and proxy infrastructure are in scope.
- Permitted request rates.
- Approved test windows.
- Whether shared production connections may be affected.

Request smuggling testing can affect unrelated requests when backend connections are shared.

### 2. Identify the HTTP Architecture

Determine:

- Supported HTTP versions.
- CDN and reverse proxy technologies.
- Server and framework fingerprints.
- Connection reuse behaviour.
- Whether HTTP/2 is supported.
- Whether protocol translation occurs.

Use response headers, TLS information, application behaviour and available architecture documentation.

### 3. Establish Baseline Behaviour

Capture normal requests and responses.

Record:

- Protocol version.
- HTTP method and path.
- Response status.
- Response headers.
- Connection behaviour.
- Timing.
- Request identifiers.

Establish a baseline before testing malformed or ambiguous framing.

### 4. Form a Test Hypothesis

Examples:

- Front-end and back-end components interpret duplicate length headers differently.
- HTTP/2 translation produces inconsistent HTTP/1.1 framing.
- A proxy reuses a backend connection after rejecting a malformed request.
- Different routes use inconsistent HTTP parsing behaviour.

Document the expected observation before conducting a test.

### 5. Perform Controlled Validation

Use a dedicated test host or isolated environment wherever possible.

Prefer:

- Single-user test environments.
- Dedicated test accounts.
- Controlled request sequences.
- Minimal request volume.
- Non-destructive validation.
- Explicitly approved protocol tests.

Avoid tests that could contaminate shared request queues or cause another user's request to be processed incorrectly.

Do not use blind or indiscriminate request-smuggling payloads against shared production infrastructure.

### 6. Confirm the Behaviour

A meaningful finding should demonstrate an actual parsing discrepancy or desynchronisation condition.

Consider:

- Differential responses.
- Repeatable timing differences.
- Connection behaviour.
- Request identifiers.
- Controlled test requests.
- Correlation between front-end and back-end behaviour.

A timeout by itself is not sufficient proof.

## Validation Techniques

### Differential Response Analysis

Compare how the target responds to:

- Valid requests.
- Requests with ambiguous framing.
- Requests with duplicate framing headers.
- Requests containing malformed transfer coding.
- Requests sent over different HTTP versions.

Record differences in response status, timing and connection behaviour.

### Timing-Based Validation

Timing differences can provide an indication of desynchronisation.

However, timing results can also be influenced by:

- Network latency.
- Backend processing time.
- Rate limiting.
- Connection pooling.
- WAF inspection.
- Load balancing.
- Application instability.

Use repeated controlled observations and compare against a baseline.

### Connection Behaviour

Where permitted, observe:

- Whether connections remain open after malformed requests.
- Whether subsequent requests are processed normally.
- Whether responses are associated with the expected requests.
- Whether connection reuse changes after an error.

Do not attempt to demonstrate cross-user impact on a shared production system.

## Potential Impact

| Impact | Description |
|---|---|
| Access control bypass | Requests may reach back-end routes differently from how the front-end evaluates them |
| Cache poisoning | A desynchronised request may influence cached responses |
| Request routing manipulation | Requests may be interpreted as belonging to another route |
| Credential exposure | Responses may become associated with an unintended request |
| Session interference | Request processing may affect another user's application interaction |
| WAF bypass | Front-end inspection may not match back-end interpretation |

Impact depends heavily on infrastructure architecture and the specific desynchronisation condition.

## False Positives and Limitations

Common sources of false positives:

- Timing differences without confirmed parsing discrepancies.
- WAF-generated responses.
- Proxy connection resets.
- Duplicate headers rejected consistently by all components.
- Scanner-only detection without manual confirmation.
- HTTP/2 support without evidence of unsafe translation.
- Behaviour that cannot be reproduced.

A vulnerability should not be reported solely because a tool identifies a potential CL.TE or TE.CL condition.

## Mitigation

Recommended controls:

- Use consistent HTTP parsing implementations across infrastructure.
- Reject ambiguous or conflicting message framing.
- Reject invalid duplicate `Content-Length` headers.
- Reject conflicting `Content-Length` and `Transfer-Encoding` information.
- Normalise requests before forwarding.
- Close connections when invalid framing is detected.
- Avoid unsafe backend connection reuse.
- Ensure HTTP/2 downgrade behaviour is consistent and secure.
- Keep proxies, gateways and application servers patched.
- Monitor for malformed framing and unexpected connection behaviour.
- Validate infrastructure changes with regression testing.

Where possible, minimise the number of independent HTTP parsers handling the same request.

## Evidence Collection

Record:

- Target hostname and endpoint.
- Date and time of testing.
- HTTP version.
- Raw request and response.
- Relevant framing headers.
- Observed timing differences.
- Connection behaviour.
- Request identifiers.
- Infrastructure components involved, where known.
- Reproduction conditions.
- Potential impact.
- Testing limitations.

Avoid including real user data or evidence obtained through unintended cross-user interference.

## Tools and References

### Tools

- Burp Suite Professional.
- Burp Repeater.
- Burp HTTP Request Smuggler extension.
- Turbo Intruder.
- curl.
- HTTP protocol inspection tools.
- Browser developer tools.

### References

- [PortSwigger Web Security Academy — HTTP Request Smuggling](https://portswigger.net/web-security/request-smuggling)
- [RFC 9112 — HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112)
- [RFC 9113 — HTTP/2](https://www.rfc-editor.org/rfc/rfc9113)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE-444 — Inconsistent Interpretation of HTTP Requests](https://cwe.mitre.org/data/definitions/444.html)

## Assessment Checklist

- [ ] Testing is explicitly authorised.
- [ ] Infrastructure scope is understood.
- [ ] HTTP versions have been identified.
- [ ] Proxy and backend architecture has been considered.
- [ ] Baseline behaviour has been recorded.
- [ ] Framing discrepancies have been assessed.
- [ ] HTTP/2 translation has been considered.
- [ ] Validation has been conducted in a controlled environment.
- [ ] Cross-user impact has not been unnecessarily introduced.
- [ ] False positives have been ruled out.
- [ ] Evidence is reproducible.
- [ ] Impact and remediation are documented.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
