# Cross-Origin Resource Sharing (CORS) Security Testing

## Overview

Cross-Origin Resource Sharing (CORS) is a browser security mechanism that controls whether a web application can make cross-origin requests and access responses from another origin.

CORS misconfigurations can expose sensitive application data when a browser is permitted to read responses from an untrusted origin.

Common weaknesses include:

- Arbitrary origin reflection.
- Insecure wildcard configurations.
- Credentialed requests to untrusted origins.
- Trust in overly broad subdomain patterns.
- Incorrect handling of the `Origin` header.
- Misconfigured preflight responses.
- Trust relationships with compromised or abandoned subdomains.

CORS vulnerabilities are particularly relevant to applications that rely on browser-based authentication, session cookies and cross-origin API access.

> **Important:** CORS is primarily a browser-enforced response access policy. It is not an authentication or authorisation mechanism, and it does not prevent direct requests from non-browser clients.

---

## Table of Contents

1. [CORS Fundamentals](#1-cors-fundamentals)
2. [Browser Same-Origin Policy](#2-browser-same-origin-policy)
3. [CORS Headers](#3-cors-headers)
4. [Simple and Preflight Requests](#4-simple-and-preflight-requests)
5. [Credentialed Requests](#5-credentialed-requests)
6. [Common CORS Misconfigurations](#6-common-cors-misconfigurations)
7. [Origin Validation Weaknesses](#7-origin-validation-weaknesses)
8. [Subdomain Trust Issues](#8-subdomain-trust-issues)
9. [Practical Testing Methodology](#9-practical-testing-methodology)
10. [Browser-Based Validation](#10-browser-based-validation)
11. [Exploitation Considerations](#11-exploitation-considerations)
12. [False Positives and Common Misunderstandings](#12-false-positives-and-common-misunderstandings)
13. [Evidence Collection](#13-evidence-collection)
14. [Remediation](#14-remediation)
15. [Testing Checklist](#15-testing-checklist)
16. [References](#16-references)

---

## 1. CORS Fundamentals

### 1.1 What is CORS?

CORS allows a server to specify which external origins are permitted to access its responses through browser-based cross-origin requests.

For example:

```text
Application:
https://app.example.com

API:
https://api.example.com

External origin:
https://attacker.example
```

The browser treats these as different origins because their hostnames differ.

The API can return CORS headers indicating whether the requesting origin is permitted to read the response.

### 1.2 What constitutes an origin?

An origin consists of three components:

- Scheme.
- Hostname.
- Port.

For example:

```text
https://app.example.com
https://app.example.com:8443
http://app.example.com
```

These represent different origins.

The following are also different origins:

```text
https://app.example.com
https://admin.example.com
https://example.com
```

A difference in path does not create a different origin.

### 1.3 CORS and the same-origin policy

The Same-Origin Policy (SOP) restricts how documents and scripts from one origin interact with resources from another.

CORS provides a controlled mechanism for relaxing certain restrictions.

A server's CORS response determines whether the browser permits requesting JavaScript to access the response.

### 1.4 CORS is not server-side access control

CORS does not prevent an attacker from sending requests using:

- `curl`.
- Burp Suite.
- Custom HTTP clients.
- Server-side scripts.

It also does not replace authentication or authorisation.

An API must independently enforce access controls regardless of its CORS configuration.

---

## 2. Browser Same-Origin Policy

### 2.1 Same-origin comparison

| URL A | URL B | Same origin? |
|---|---|---|
| `https://example.com` | `https://example.com` | Yes |
| `https://example.com` | `http://example.com` | No |
| `https://example.com` | `https://api.example.com` | No |
| `https://example.com` | `https://example.com:8443` | No |
| `https://example.com/app` | `https://example.com/admin` | Yes |
| `https://example.com` | `https://example.net` | No |

### 2.2 Cross-origin requests

Browsers can send certain cross-origin requests even when the requesting script is not permitted to read the response.

This distinction is important.

A failed CORS check does not necessarily mean the request was never sent.

For example, a browser may send a request to an API but prevent JavaScript from accessing the returned data.

### 2.3 CORS and CSRF

CORS and Cross-Site Request Forgery (CSRF) are separate security concerns.

CORS controls whether browser scripts can access cross-origin responses.

CSRF concerns whether an attacker can cause a victim's browser to perform an unwanted authenticated action.

An application can have:

- Secure CORS configuration but be vulnerable to CSRF.
- Insecure CORS configuration but have effective CSRF protections.
- Both vulnerabilities.
- Neither vulnerability.

Assess them independently.

---

## 3. CORS Headers

The following headers are central to CORS assessment.

### 3.1 Access-Control-Allow-Origin

Specifies which origin is permitted to access the response.

Example:

```http
Access-Control-Allow-Origin: https://app.example.com
```

Wildcard:

```http
Access-Control-Allow-Origin: *
```

The wildcard permits non-credentialed cross-origin response access, subject to browser CORS rules.

It cannot be combined with credentialed access in the standard way.

### 3.2 Access-Control-Allow-Credentials

Indicates whether the browser may expose the response to JavaScript when credentials are included.

Example:

```http
Access-Control-Allow-Credentials: true
```

When credentialed access is permitted, the server must return an explicit allowed origin rather than `*`.

### 3.3 Access-Control-Allow-Methods

Specifies the methods permitted for cross-origin requests.

Example:

```http
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
```

This header does not itself enforce server-side authorisation or restrict direct HTTP clients.

### 3.4 Access-Control-Allow-Headers

Specifies which request headers may be used in cross-origin requests.

Example:

```http
Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With
```

### 3.5 Access-Control-Expose-Headers

Specifies which response headers browser JavaScript may access.

Example:

```http
Access-Control-Expose-Headers: X-Request-ID, Content-Disposition
```

Only permitted response headers are exposed to requesting scripts.

### 3.6 Access-Control-Max-Age

Specifies how long the browser may cache the result of a preflight request.

Example:

```http
Access-Control-Max-Age: 600
```

### 3.7 Vary: Origin

When a server dynamically selects CORS responses based on the request origin, it should generally include:

```http
Vary: Origin
```

This helps prevent shared caches from incorrectly reusing a response generated for a different origin.

---

## 4. Simple and Preflight Requests

### 4.1 Simple requests

Some cross-origin requests can be sent without a preflight request.

The browser evaluates whether a request qualifies under the CORS safelisted method, header and content-type requirements.

Common examples include certain:

- `GET` requests.
- `HEAD` requests.
- `POST` requests using safelisted content types.

A simple request can still trigger a CORS failure when the response is not permitted to be read.

### 4.2 Preflight requests

A browser sends a preflight request when the proposed cross-origin request does not qualify as a simple request.

The browser uses an `OPTIONS` request to ask the server whether the intended request is permitted.

Example:

```http
OPTIONS /api/profile HTTP/1.1
Host: api.example.com
Origin: https://app.example.com
Access-Control-Request-Method: PUT
Access-Control-Request-Headers: authorization,content-type
```

Example response:

```http
HTTP/1.1 204 No Content
Access-Control-Allow-Origin: https://app.example.com
Access-Control-Allow-Methods: GET, POST, PUT
Access-Control-Allow-Headers: Authorization, Content-Type
Access-Control-Max-Age: 600
```

The browser uses this response to determine whether it can send the intended request.

### 4.3 Preflight testing

Assess:

- Whether unauthorised origins receive approval.
- Whether allowed methods are overly broad.
- Whether sensitive headers are permitted.
- Whether credential requirements are handled correctly.
- Whether the application applies consistent policies across endpoints.

### 4.4 OPTIONS handling

Do not assume that an `OPTIONS` response demonstrates a vulnerability.

A server may respond successfully to `OPTIONS` while still enforcing authentication and authorisation on the actual operation.

Assess the complete browser interaction.

---

## 5. Credentialed Requests

Credentialed CORS requests are particularly important because they can involve the victim's authenticated session.

### 5.1 What are credentials?

Depending on the request and browser behaviour, credentials can include:

- Cookies.
- HTTP authentication credentials.
- Client certificates.

JavaScript can request credential inclusion using:

```javascript
fetch("https://api.example.com/account", {
    credentials: "include"
});
```

The browser still applies its credential, cookie and CORS rules.

### 5.2 Required response headers

A credentialed cross-origin response generally requires both:

```http
Access-Control-Allow-Origin: https://trusted.example
Access-Control-Allow-Credentials: true
```

The origin must be explicitly permitted.

This is not a valid credentialed CORS configuration:

```http
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
```

Browsers reject credentialed access with a wildcard origin.

### 5.3 Cookie restrictions

Even when CORS allows credentialed access, cookies may not be sent.

Consider:

- `SameSite` attributes.
- `Secure`.
- Domain and path restrictions.
- Third-party cookie restrictions.
- Browser privacy protections.

An origin and a site are not the same concept. Two subdomains can be cross-origin while still being same-site under relevant cookie rules.

### 5.4 Authentication context

Determine whether the affected endpoint relies on:

- Session cookies.
- Bearer tokens.
- HTTP authentication.
- Client certificates.
- Other browser-managed credentials.

A CORS misconfiguration is significantly more concerning when it exposes sensitive responses using ambient browser credentials.

---

## 6. Common CORS Misconfigurations

### 6.1 Arbitrary origin reflection

The server copies the supplied `Origin` header into its response without validating it.

Request:

```http
GET /api/account HTTP/1.1
Host: api.example.com
Origin: https://untrusted.example
```

Vulnerable response:

```http
HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://untrusted.example
Access-Control-Allow-Credentials: true
```

If the response contains sensitive account data and a browser can send the victim's credentials, this may enable cross-origin data disclosure.

### 6.2 Substring matching

A server may validate origins using insecure substring matching.

For example, a check intended to trust:

```text
example.com
```

may also accept:

```text
example.com.attacker.example
```

The trusted domain is present as a substring, but the origin is controlled by another party.

### 6.3 Suffix validation errors

A poorly implemented suffix check may accept unintended hostnames.

For example, a check for hosts ending in `example.com` might incorrectly accept:

```text
notexample.com
```

Correct validation must distinguish DNS label boundaries.

### 6.4 Null origin trust

Browsers can send:

```http
Origin: null
```

This can occur in certain opaque-origin contexts.

Trusting `null` without a specific security requirement can expose sensitive responses to unintended contexts.

### 6.5 Wildcard configuration

Example:

```http
Access-Control-Allow-Origin: *
```

This is not automatically a vulnerability.

The impact depends on the data being exposed and whether credentials are involved.

Public, non-sensitive resources may legitimately use wildcard CORS.

### 6.6 Inconsistent CORS policies

Different endpoints may use different policies.

For example:

```text
/api/public       - wildcard
/api/profile      - reflected origin
/api/admin        - fixed trusted origin
/api/export       - no CORS restrictions
```

Assess the actual behaviour of sensitive endpoints individually.

### 6.7 Duplicate or conflicting headers

Multiple CORS headers may produce inconsistent behaviour between:

- Reverse proxies.
- Application frameworks.
- Browsers.
- Intermediate caches.

Review the final response as received by the browser.

---

## 7. Origin Validation Weaknesses

### 7.1 Origin reflection

Determine whether the application dynamically reflects the supplied origin.

Test with an authorised target using representative origins:

```http
Origin: https://untrusted.example
```

```http
Origin: https://example.com.attacker.example
```

```http
Origin: https://notexample.com
```

```http
Origin: null
```

Record whether the response:

- Rejects the origin.
- Omits the CORS header.
- Returns a fixed origin.
- Reflects the supplied origin.

Reflection alone does not establish exploitability. Assess the complete credentialed browser context.

### 7.2 Protocol validation

Check whether the application distinguishes between:

```text
http://trusted.example
https://trusted.example
```

Trusting an insecure origin can create exposure if an attacker can control or intercept that origin.

### 7.3 Port validation

Check whether origin validation correctly considers ports.

For example:

```text
https://trusted.example
https://trusted.example:8443
```

These are different origins.

### 7.4 Case and normalisation

Review how the application handles:

- Hostname case.
- Default ports.
- Trailing dots.
- Internationalised domain names.
- URL parsing and normalisation.

Avoid relying on ad hoc string comparisons for security decisions.

### 7.5 Multiple origin values

The `Origin` header has defined syntax and should be parsed accordingly.

Assess whether the application or intermediary components handle malformed or duplicate origin headers inconsistently.

---

## 8. Subdomain Trust Issues

### 8.1 Broad subdomain trust

Applications sometimes trust every subdomain of a parent domain.

Example:

```text
https://*.example.com
```

This may create risk when subdomains are:

- User-controlled.
- Hosted by third parties.
- Abandoned.
- Vulnerable to takeover.
- Operated with weaker security controls.

### 8.2 Subdomain takeover considerations

A trusted CORS origin may become attacker-controlled if a subdomain points to an unclaimed third-party resource.

Assess:

- DNS ownership.
- Hosting configuration.
- Subdomain lifecycle.
- Third-party service dependencies.
- Whether the origin is actually trusted by sensitive APIs.

Do not attempt to claim or modify third-party resources unless explicitly authorised.

### 8.3 Same-site versus same-origin

A trusted subdomain can still be cross-origin.

For example:

```text
https://app.example.com
https://legacy.example.com
```

These origins differ, even though they share a registrable domain.

This distinction matters when evaluating CORS and cookie behaviour together.

### 8.4 Trust relationship mapping

Document:

- Trusted origins.
- Sensitive API endpoints.
- Authentication mechanisms.
- Subdomain ownership.
- Third-party dependencies.
- Whether trusted origins can be influenced by users.

---

## 9. Practical Testing Methodology

### Step 1: Identify cross-origin functionality

Map API endpoints accessed by frontend applications hosted on different origins.

Look for:

- Account information.
- Profile data.
- Administrative functions.
- Financial information.
- Export endpoints.
- Sensitive application records.

### Step 2: Establish baseline behaviour

Capture a normal request from the intended frontend.

Record:

- Request origin.
- Authentication context.
- Response headers.
- Response body.
- Endpoint functionality.

### Step 3: Modify the Origin header

Repeat the request using controlled, representative origins.

Compare the resulting CORS headers.

### Step 4: Review credential support

Determine whether the application returns:

```http
Access-Control-Allow-Credentials: true
```

Assess whether the browser can actually send the relevant credentials.

### Step 5: Review preflight behaviour

Where required, test the `OPTIONS` response and compare the allowed methods and headers with the intended application policy.

### Step 6: Identify sensitive response data

Determine whether the affected endpoint returns information that should not be available to arbitrary origins.

### Step 7: Validate in a browser

Use an authorised test account and a controlled origin to establish whether browser JavaScript can read the sensitive response.

### Step 8: Assess realistic impact

Consider whether the issue enables:

- Account information disclosure.
- Personal information exposure.
- Sensitive API response access.
- Cross-origin access to administrative data.
- Disclosure of confidential application records.

### Step 9: Capture evidence

Preserve the relevant request, response headers, browser result and affected data classification.

---

## 10. Browser-Based Validation

A raw HTTP response is not sufficient to prove a browser-enforced CORS vulnerability.

A browser-based test helps establish whether JavaScript can actually access the response.

### 10.1 Controlled test page

The following example is intended for a controlled assessment origin and an authorised test account.

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>CORS Assessment</title>
</head>
<body>
    <h1>CORS Assessment</h1>
    <pre id="result">Waiting...</pre>

    <script>
        const target = "https://api.example.com/api/profile";

        fetch(target, {
            method: "GET",
            credentials: "include"
        })
        .then(async response => {
            const body = await response.text();

            document.getElementById("result").textContent =
                `Status: ${response.status}\n${body}`;
        })
        .catch(error => {
            document.getElementById("result").textContent =
                `Request blocked or failed: ${error}`;
        });
    </script>
</body>
</html>
```

Replace the target with an authorised test endpoint.

The page should be hosted on a separate controlled origin to reproduce a genuine cross-origin browser request.

### 10.2 Interpreting results

| Result | Interpretation |
|---|---|
| Browser exposes sensitive response | Potentially exploitable CORS issue |
| Browser reports CORS failure | Response not available to requesting JavaScript |
| Request is unauthenticated | Does not establish credentialed exposure |
| Request succeeds but response is public | May be intended behaviour |
| HTTP client receives response | Does not prove browser CORS access |

### 10.3 Testing limitations

A failed browser request may result from:

- CORS policy.
- Cookie restrictions.
- Authentication failure.
- Network errors.
- TLS errors.
- Content Security Policy.
- Browser privacy protections.

Identify the actual cause before reporting.

---

## 11. Exploitation Considerations

### 11.1 Conditions for meaningful impact

A credentialed CORS vulnerability generally requires several conditions:

1. A sensitive endpoint is accessible through a browser.
2. The victim has an authenticated session or other relevant credentials.
3. The browser sends the required credentials.
4. The server permits the attacker's origin.
5. The response contains sensitive information.
6. The browser exposes that response to attacker-controlled JavaScript.

Failure of one or more conditions may significantly reduce impact.

### 11.2 Data sensitivity

Prioritise endpoints returning:

- Personal information.
- Account details.
- Financial records.
- Authentication-related information.
- Organisation data.
- Sensitive documents.
- Administrative information.

### 11.3 Read versus write impact

CORS primarily governs browser access to responses.

A CORS misconfiguration may allow sensitive data to be read, but it does not automatically demonstrate the ability to perform arbitrary authenticated actions.

Assess state-changing operations separately, including CSRF protections and server-side authorisation.

### 11.4 Minimal proof of concept

Use the smallest amount of synthetic data necessary to demonstrate the issue.

Do not collect unrelated user records or sensitive production information.

---

## 12. False Positives and Common Misunderstandings

| Observation | Why it may not be a vulnerability |
|---|---|
| `Access-Control-Allow-Origin: *` | May be appropriate for public resources |
| Origin is reflected | May not permit credentials or sensitive access |
| `OPTIONS` returns 200 | Does not prove the actual operation is accessible |
| API responds to `curl` | CORS is enforced by browsers |
| CORS headers are missing | Browser may correctly block response access |
| Credentials are enabled | Does not establish sensitive data exposure |
| API accepts cross-origin requests | Server-side authorisation may still be effective |
| Subdomain is trusted | It may be securely controlled and intended |

### Important distinction

A CORS misconfiguration should be reported based on demonstrated security impact, not simply because a header differs from a preferred configuration.

---

## 13. Evidence Collection

### 13.1 Required evidence

Capture:

- Affected endpoint.
- Request origin.
- Authentication context.
- Relevant request headers.
- Relevant response headers.
- Response content classification.
- Browser validation result.
- Reproduction conditions.

### 13.2 Finding template

```text
Finding ID:

Title:

Affected Host:

Affected Endpoint:

Request Origin:

Authentication Context:

Access-Control-Allow-Origin:

Access-Control-Allow-Credentials:

Other Relevant Headers:

Expected Behaviour:

Actual Behaviour:

Browser Validation:

Sensitive Data Exposed:

Reproduction Steps:

Impact:

Remediation:

References:
```

### 13.3 Evidence handling

Sanitise:

- Session cookies.
- Bearer tokens.
- API keys.
- Personal information.
- Unrelated application records.

Use test accounts and synthetic records wherever possible.

---

## 14. Remediation

### 14.1 Explicit origin allowlists

Maintain an explicit list of approved origins.

Avoid reflecting arbitrary values from the request.

### 14.2 Exact origin validation

Validate the complete origin, including:

- Scheme.
- Hostname.
- Port.

Avoid substring matching and simplistic suffix checks.

### 14.3 Restrict credentialed access

Only enable credentialed CORS where required.

Do not combine wildcard origins with credentialed access.

### 14.4 Minimise exposed methods and headers

Allow only the methods and request headers required by the application.

### 14.5 Validate subdomain trust

Only trust subdomains that are controlled, maintained and required.

Review third-party dependencies and abandoned DNS records.

### 14.6 Apply appropriate cache variation

Where responses vary according to the requesting origin, return:

```http
Vary: Origin
```

Ensure shared caches cannot serve a response generated for one origin to another.

### 14.7 Maintain server-side authorisation

CORS must never be the only control protecting sensitive data or operations.

Every API endpoint must independently validate authentication and authorisation.

### 14.8 Review policy changes

CORS policies should be tested as part of application security regression testing.

---

## 15. Testing Checklist

### Discovery

- [ ] Identify cross-origin application functionality.
- [ ] Identify API endpoints.
- [ ] Identify sensitive response data.
- [ ] Identify authentication mechanisms.
- [ ] Map trusted frontend origins.

### Header assessment

- [ ] Review `Access-Control-Allow-Origin`.
- [ ] Review `Access-Control-Allow-Credentials`.
- [ ] Review `Access-Control-Allow-Methods`.
- [ ] Review `Access-Control-Allow-Headers`.
- [ ] Review `Access-Control-Expose-Headers`.
- [ ] Review `Access-Control-Max-Age`.
- [ ] Review `Vary: Origin`.

### Origin validation

- [ ] Test an untrusted origin.
- [ ] Test a trusted origin.
- [ ] Test a lookalike domain.
- [ ] Test a misleading suffix.
- [ ] Test `null` origin handling.
- [ ] Review protocol validation.
- [ ] Review port validation.
- [ ] Review subdomain trust.

### Browser validation

- [ ] Confirm the endpoint is sensitive.
- [ ] Establish the authenticated context.
- [ ] Review cookie restrictions.
- [ ] Test credentialed browser requests.
- [ ] Confirm whether JavaScript can read the response.
- [ ] Distinguish CORS from CSRF.
- [ ] Assess realistic impact.

### Reporting

- [ ] Capture request and response headers.
- [ ] Capture browser validation.
- [ ] Sanitise sensitive evidence.
- [ ] Document affected data.
- [ ] Confirm exploitability.
- [ ] Provide specific remediation.

---

## 16. References

### PortSwigger Web Security Academy — CORS

https://portswigger.net/web-security/cors

### OWASP Web Security Testing Guide

https://owasp.org/www-project-web-security-testing-guide/

### OWASP Cross-Origin Resource Sharing Cheat Sheet

https://cheatsheetseries.owasp.org/cheatsheets/Cross_Origin_Resource_Sharing_Cheat_Sheet.html

### MDN — Cross-Origin Resource Sharing

https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

### MDN — Same-Origin Policy

https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy

### Fetch Standard

https://fetch.spec.whatwg.org/

### PortSwigger Research

https://portswigger.net/research

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
