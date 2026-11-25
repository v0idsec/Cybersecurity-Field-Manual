# Cross-Site Scripting (XSS)

A practical guide to identifying, validating and understanding Cross-Site Scripting vulnerabilities during authorised web application security assessments.

Cross-Site Scripting occurs when an application handles untrusted data in a way that allows attacker-controlled content to execute as script in another user's browser.

Depending on the context and application, XSS can expose sensitive information, perform actions as the victim, manipulate application content or compromise user sessions.

> **Scope reminder:** Only test applications where you have explicit authorisation. Use harmless proof-of-concept payloads and designated test accounts. Never collect real users' credentials, session tokens or private information.

---

## Contents

- [1. XSS Fundamentals](#1-xss-fundamentals)
- [2. Types of XSS](#2-types-of-xss)
- [3. Identifying Injection Points](#3-identifying-injection-points)
- [4. HTML Context](#4-html-context)
- [5. Attribute Context](#5-attribute-context)
- [6. JavaScript Context](#6-javascript-context)
- [7. DOM-Based XSS](#7-dom-based-xss)
- [8. Useful Test Payloads](#8-useful-test-payloads)
- [9. XSS Filter and WAF Behaviour](#9-xss-filter-and-waf-behaviour)
- [10. Content Security Policy](#10-content-security-policy)
- [11. Testing with Burp Suite](#11-testing-with-burp-suite)
- [12. XSS Tools](#12-xss-tools)
- [13. Prevention and Remediation](#13-prevention-and-remediation)
- [14. Testing Checklist](#14-testing-checklist)
- [15. Further Reading](#15-further-reading)

---

## 1. XSS Fundamentals

XSS is an injection vulnerability involving the execution of untrusted content in a browser.

It commonly occurs when applications:

- Insert untrusted input into HTML without appropriate encoding.
- Construct HTML using unsafe JavaScript operations.
- Place user-controlled values into executable JavaScript contexts.
- Render untrusted content using dangerous DOM APIs.
- Trust client-side sanitisation without adequate server-side controls.

### Potential impact

Depending on the application and browser context:

- Perform actions using the victim's authenticated session.
- Read sensitive information accessible to JavaScript.
- Modify application content.
- Redirect users to malicious websites.
- Capture information entered into vulnerable application forms.
- Impersonate application functionality.
- Affect other users who view stored content.

XSS does not automatically provide access to every cookie or browser resource. Controls such as HttpOnly, SameSite and Content Security Policy can limit particular attack paths.

---

## 2. Types of XSS

There are three major categories of XSS.

### Reflected XSS

Reflected XSS occurs when untrusted input is included in an application's immediate response without appropriate handling.

Example workflow:

1. A user submits a search query.
2. The application includes the query in its response.
3. The response is interpreted as executable browser content.
4. A victim visits a crafted URL or submits a crafted request.

Example vulnerable functionality:

```text
https://example.com/search?q=hello
```

The key question is whether the application safely encodes the search value before rendering it.

### Stored XSS

Stored XSS occurs when untrusted content is saved by an application and later rendered to other users without appropriate handling.

Common locations:

- User profiles
- Comments
- Product reviews
- Support tickets
- Discussion forums
- Messaging systems
- Shared documents
- Administrative dashboards

Example workflow:

1. A user submits content.
2. The application stores it.
3. Another user views the content.
4. The browser interprets unsafe content as executable script.

Stored XSS can have significant impact because the vulnerable content may affect multiple users.

### DOM-Based XSS

DOM-based XSS occurs when client-side JavaScript processes untrusted data and uses it in an unsafe browser DOM operation.

The vulnerable operation may occur entirely in the browser without the server directly reflecting the input into HTML.

Common sources:

- `location.search`
- `location.hash`
- `document.referrer`
- `window.name`
- `postMessage` data
- Client-side storage

Common dangerous sinks:

- `innerHTML`
- `outerHTML`
- `document.write()`
- `insertAdjacentHTML()`
- `eval()`
- `setTimeout()` with string arguments

### Comparison

| Type | Where the vulnerable behaviour occurs | Typical trigger |
|---|---|---|
| Reflected | Server response | Crafted request |
| Stored | Stored application content | Another user views content |
| DOM-based | Client-side JavaScript | Manipulated browser input |

---

## 3. Identifying Injection Points

Begin by identifying where user-controlled data enters the application and where it is eventually rendered.

### Common injection points

| Location | Example |
|---|---|
| Search fields | Search query |
| Profile fields | Display name or biography |
| Comments | User-generated content |
| Support tickets | Ticket descriptions |
| URL parameters | Query strings |
| URL fragments | Hash values |
| HTTP headers | Referrer or user-agent values |
| API responses | JSON values rendered by frontend code |
| File metadata | Uploaded filenames |
| Messaging | User-generated messages |

### Initial testing workflow

1. Identify an input field or parameter.
2. Submit a unique harmless marker.
3. Find where the marker appears in the response.
4. Inspect the surrounding HTML or JavaScript context.
5. Determine whether the value is encoded, sanitised or inserted unsafely.
6. Use a context-appropriate proof of concept in an authorised environment.
7. Verify the browser behaviour.
8. Document the result.

### Harmless marker

```text
XSS_TEST_92741
```

Search for this marker in:

- HTTP responses
- Rendered page source
- Browser developer tools
- JavaScript-generated DOM elements

A value appearing in a response does not automatically indicate XSS. Its rendering context matters.

---

## 4. HTML Context

HTML context occurs when untrusted input is inserted into an HTML document.

### Example vulnerable code

```javascript
element.innerHTML = userInput;
```

The browser parses the supplied value as HTML rather than treating it purely as text.

### Safer alternative

```javascript
element.textContent = userInput;
```

`textContent` treats the value as text rather than parsing it as HTML.

### Testing considerations

- Is input rendered as text or HTML?
- Is HTML encoding applied?
- Can user input create new HTML elements?
- Does the application use a trusted HTML sanitisation library?
- Is the same content rendered differently in other pages?

### Important distinction

HTML encoding must be appropriate for the output context. Encoding suitable for HTML text is not necessarily sufficient for JavaScript, CSS or URL contexts.

---

## 5. Attribute Context

Untrusted input may be inserted into HTML attributes.

Example:

```html
<input value="USER_INPUT">
```

Testing should establish whether the application correctly handles quotation marks, special characters and attribute boundaries.

### Areas to investigate

- Input values
- Link destinations
- Image attributes
- Event-handler attributes
- Data attributes
- Form actions

### Dangerous attributes

Some HTML attributes can execute JavaScript or initiate unexpected browser behaviour.

Examples include event-handler attributes such as:

```html
onerror
onclick
onload
```

### Defensive approach

- Apply context-appropriate attribute encoding.
- Avoid inserting untrusted values into event-handler attributes.
- Validate URL schemes when handling link destinations.
- Prefer safe DOM property assignment over HTML string construction.

---

## 6. JavaScript Context

JavaScript context occurs when untrusted values are inserted into executable JavaScript.

### Example vulnerable code

```javascript
const username = 'USER_INPUT';
```

If user input is directly concatenated into JavaScript source, it may alter the intended script structure.

### Testing considerations

- Is input inserted into inline JavaScript?
- Is JSON generated safely?
- Are string delimiters handled correctly?
- Is untrusted data passed to `eval()`?
- Are dynamically generated scripts used?
- Is data separated from executable code?

### Safer approach

Avoid building executable JavaScript by concatenating untrusted strings.

Use safe data serialization and pass values through appropriate APIs instead.

Example:

```javascript
const username = document.getElementById("username").value;
document.getElementById("greeting").textContent = username;
```

---

## 7. DOM-Based XSS

DOM-based XSS is particularly important in modern single-page applications.

The application may retrieve data from the browser environment and pass it into a dangerous DOM sink.

### Common sources

| Source | Description |
|---|---|
| `location.search` | URL query parameters |
| `location.hash` | URL fragment |
| `document.referrer` | Referring page |
| `window.name` | Window-associated data |
| `localStorage` | Browser local storage |
| `sessionStorage` | Browser session storage |
| `postMessage` | Cross-window messages |

### Common sinks

| Sink | Risk |
|---|---|
| `innerHTML` | Parses HTML |
| `outerHTML` | Replaces an element using HTML |
| `document.write()` | Writes HTML into a document |
| `insertAdjacentHTML()` | Inserts parsed HTML |
| `eval()` | Executes JavaScript |
| `Function()` | Constructs executable functions |

### Example vulnerable code

```javascript
const params = new URLSearchParams(window.location.search);
const message = params.get("message");

document.getElementById("output").innerHTML = message;
```

The application places URL-controlled data directly into an HTML parsing sink.

### Safer implementation

```javascript
const params = new URLSearchParams(window.location.search);
const message = params.get("message");

document.getElementById("output").textContent = message;
```

### Source-to-sink analysis

When reviewing JavaScript:

1. Identify untrusted sources.
2. Trace how values move through the application.
3. Identify dangerous sinks.
4. Determine whether sanitisation or safe APIs are used.
5. Validate the behaviour in a controlled browser environment.

### Useful references

- [OWASP DOM Based XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
- [PortSwigger DOM-Based XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based)

---

## 8. Useful Test Payloads

The purpose of initial XSS testing is to determine whether user-controlled input is interpreted as executable content.

Use harmless proof-of-concept values in an authorised test environment.

### Unique marker

```text
XSS_TEST_92741
```

### Basic HTML rendering test

```html
<b>XSS_TEST_92741</b>
```

This checks whether HTML is being interpreted rather than rendered as ordinary text.

### JavaScript execution proof of concept

```html
<script>alert(document.domain)</script>
```

This is a simple demonstration payload for controlled training environments.

### Event-handler proof of concept

```html
<img src=x onerror=alert(document.domain)>
```

### What to record

- Whether the input is reflected.
- Whether HTML is interpreted.
- Whether JavaScript executes.
- The execution context.
- Whether authentication is required.
- Whether another user must view the content.
- Whether the behaviour persists after refreshing the page.

### Payload repositories

- [PayloadsAllTheThings – XSS](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection)
- [PortSwigger XSS Cheat Sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)
- [OWASP XSS Filter Evasion Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html)

Payloads should be selected based on the actual injection context. Randomly trying large payload lists is inefficient and can generate unnecessary traffic.

---

## 9. XSS Filter and WAF Behaviour

Applications may implement filtering, sanitisation and browser-side protections to reduce XSS risk.

### Common controls

- HTML output encoding
- Input validation
- HTML sanitisation
- Content Security Policy
- Web Application Firewalls
- Trusted Types
- Framework-specific escaping

### Testing considerations

- Is input encoded before rendering?
- Is sanitisation applied consistently?
- Does the application use different rendering paths?
- Are protections implemented server-side?
- Does the frontend use unsafe DOM operations?
- Is the same content rendered in email templates or administrative views?

### Important distinction

A WAF blocking a particular payload does not prove the underlying application is secure.

Likewise, bypassing a filter does not automatically establish XSS. The browser must interpret the content in an executable context.

---

## 10. Content Security Policy

Content Security Policy (CSP) is a browser security mechanism that restricts where certain resources can be loaded from and which scripts may execute.

### Example policy

```http
Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self'
```

### Important directives

| Directive | Purpose |
|---|---|
| `default-src` | Default resource loading policy |
| `script-src` | Controls script sources |
| `style-src` | Controls stylesheet sources |
| `img-src` | Controls image sources |
| `connect-src` | Controls connection destinations |
| `object-src` | Controls plugin object sources |
| `base-uri` | Restricts base element URLs |
| `frame-ancestors` | Controls which sites may embed the page |

### Testing CSP

Review the response headers and determine:

- Is CSP present?
- Is it enforced or report-only?
- Are broad wildcard sources used?
- Is `unsafe-inline` permitted?
- Is `unsafe-eval` permitted?
- Are script nonces or hashes used appropriately?
- Are third-party script sources trusted?

### Important note

CSP is defence in depth. It should not replace safe output encoding, sanitisation or secure DOM programming.

### Reference

[MDN – Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)

---

## 11. Testing with Burp Suite

Burp Suite provides useful functionality for identifying and validating XSS.

### Basic workflow

1. Configure the browser to use Burp Proxy.
2. Browse the authorised application.
3. Identify potential input fields and parameters.
4. Capture the relevant HTTP request.
5. Send the request to Repeater.
6. Insert a unique marker.
7. Inspect the response.
8. Determine the rendering context.
9. Validate any suspected execution in the browser.
10. Record evidence.

### Useful Burp features

| Feature | Purpose |
|---|---|
| Proxy | Capture application traffic |
| Repeater | Modify and replay requests |
| Intruder | Controlled parameter testing |
| Decoder | Encode and decode values |
| Comparer | Compare responses |
| DOM Invader | Identify DOM-based XSS sources and sinks |
| Scanner | Automated vulnerability detection in supported editions |

### DOM Invader

DOM Invader is a Burp browser tool designed to assist with DOM-based vulnerability analysis.

It can help identify:

- Sources of untrusted data
- Dangerous DOM sinks
- Data flow through client-side JavaScript
- Potential DOM-based XSS issues

Resource: [Burp DOM Invader Documentation](https://portswigger.net/burp/documentation/desktop/tools/dom-invader)

---

## 12. XSS Tools

| Tool | Purpose | Resource |
|---|---|---|
| Burp Suite | Intercepting proxy and web testing | [Website](https://portswigger.net/burp) |
| OWASP ZAP | Web application security testing | [Website](https://www.zaproxy.org/) |
| Dalfox | XSS parameter analysis and testing | [GitHub](https://github.com/hahwul/dalfox) |
| XSStrike | XSS detection and analysis | [GitHub](https://github.com/s0md3v/XSStrike) |
| DOM Invader | DOM-based vulnerability analysis | [Documentation](https://portswigger.net/burp/documentation/desktop/tools/dom-invader) |
| Retire.js | Identify vulnerable JavaScript libraries | [Website](https://retirejs.github.io/retire.js/) |

### Tool usage considerations

Automated XSS tools can generate false positives and may submit large numbers of requests.

Always:

- Confirm testing is authorised.
- Use appropriate rate limits.
- Review findings manually.
- Validate execution in the browser.
- Avoid payloads that affect other users.

---

## 13. Prevention and Remediation

### Context-aware output encoding

Encode untrusted data according to the context in which it is rendered.

Different contexts require different protections:

- HTML text
- HTML attributes
- JavaScript strings
- CSS values
- URL parameters

### Use safe DOM APIs

Prefer:

```javascript
element.textContent = userInput;
```

Avoid unsafe HTML insertion when it is unnecessary:

```javascript
element.innerHTML = userInput;
```

### HTML sanitisation

When applications genuinely need to render user-supplied HTML, use a maintained sanitisation library with an appropriate allowlist.

Example:

- [DOMPurify](https://github.com/cure53/DOMPurify)

### Additional controls

- Apply context-aware output encoding.
- Avoid unsafe JavaScript evaluation.
- Validate URLs and permitted schemes.
- Use Content Security Policy.
- Consider Trusted Types for supported applications.
- Keep frontend dependencies updated.
- Review third-party JavaScript.
- Avoid relying exclusively on WAF filtering.

### Framework considerations

Modern frameworks often provide automatic escaping, but unsafe escape hatches can reintroduce XSS vulnerabilities.

Review how the application uses:

- React `dangerouslySetInnerHTML`
- Vue `v-html`
- Angular bypass security APIs
- Direct DOM manipulation

---

## 14. Testing Checklist

### Discovery
- [ ] Identify user-controlled inputs
- [ ] Identify reflected parameters
- [ ] Review stored user-generated content
- [ ] Inspect JavaScript files
- [ ] Identify DOM sources and sinks

### Reflected XSS
- [ ] Test relevant query parameters
- [ ] Review HTML response contexts
- [ ] Check context-aware output encoding
- [ ] Validate browser interpretation

### Stored XSS
- [ ] Review profile fields
- [ ] Review comments and messages
- [ ] Review support tickets
- [ ] Check administrative views
- [ ] Verify persistence across sessions

### DOM-Based XSS
- [ ] Identify client-side sources
- [ ] Identify dangerous sinks
- [ ] Trace source-to-sink data flow
- [ ] Review sanitisation
- [ ] Validate in a controlled browser

### Browser protections
- [ ] Review CSP
- [ ] Review security headers
- [ ] Check framework escaping
- [ ] Review third-party scripts

### Reporting
- [ ] Identify the vulnerable input
- [ ] Identify the XSS type
- [ ] Record the execution context
- [ ] Demonstrate impact safely
- [ ] Include reproducible evidence
- [ ] Recommend context-aware remediation

---

## 15. Further Reading

### Learning resources

- [PortSwigger Web Security Academy – XSS](https://portswigger.net/web-security/cross-site-scripting)
- [OWASP Cross-Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [OWASP DOM Based XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
- [MDN Web Security](https://developer.mozilla.org/en-US/docs/Web/Security)
- [HackTricks – XSS](https://book.hacktricks.wiki/)

### Practice environments

- [PortSwigger XSS Labs](https://portswigger.net/web-security/all-labs#cross-site-scripting)
- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)
- [DVWA](https://github.com/digininja/DVWA)
- [WebGoat](https://owasp.org/www-project-webgoat/)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
