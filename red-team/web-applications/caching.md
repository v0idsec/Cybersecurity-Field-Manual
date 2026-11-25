
# Web Cache Poisoning and Deception

> Professional reference guide for assessing HTTP caching behaviour, cache key weaknesses and cache-related application security issues.

## Contents

- [Overview](#overview)
- [Caching Fundamentals](#caching-fundamentals)
- [Cache Architecture](#cache-architecture)
- [Cache Key Analysis](#cache-key-analysis)
- [Web Cache Poisoning](#web-cache-poisoning)
- [Unkeyed Inputs](#unkeyed-inputs)
- [Web Cache Deception](#web-cache-deception)
- [Cache-Control Assessment](#cache-control-assessment)
- [Cache Variation and Normalisation](#cache-variation-and-normalisation)
- [Assessment Methodology](#assessment-methodology)
- [Validation and Impact](#validation-and-impact)
- [Mitigation](#mitigation)
- [Tools and References](#tools-and-references)
- [Assessment Checklist](#assessment-checklist)

---

## Overview

HTTP caching improves performance by storing responses for reuse.

Caching may occur at several layers:

- Browser.
- Reverse proxy.
- CDN.
- Load balancer.
- API gateway.
- Application framework.
- Service worker.

Incorrect caching behaviour can expose sensitive information or cause malicious content to be served to other users.

Two important vulnerability classes are:

| Vulnerability | Description |
|---|---|
| Web Cache Poisoning | An attacker influences a cached response that is subsequently served to other users |
| Web Cache Deception | An attacker causes sensitive content to be stored or treated as a publicly cacheable resource |

Other cache-related weaknesses include:

- Sensitive response caching.
- Incorrect cache key construction.
- Unkeyed header influence.
- Cache variation errors.
- Cache normalisation discrepancies.
- Cache invalidation failures.

## Caching Fundamentals

HTTP caching behaviour is influenced by request and response headers.

Important response headers include:

| Header | Purpose |
|---|---|
| `Cache-Control` | Defines caching directives |
| `Expires` | Specifies an expiry date |
| `ETag` | Provides a representation validator |
| `Last-Modified` | Indicates resource modification time |
| `Vary` | Identifies request headers that influence response variation |
| `Age` | Indicates time spent in a cache |

Important request headers include:

| Header | Purpose |
|---|---|
| `Cache-Control` | Provides request caching directives |
| `If-None-Match` | Conditional request using an entity tag |
| `If-Modified-Since` | Conditional request using modification time |
| `Pragma` | Legacy cache directive |

### Common Cache-Control Directives

| Directive | Meaning |
|---|---|
| `public` | Response may be stored by shared caches |
| `private` | Response is intended for private caches |
| `no-store` | Response should not be stored |
| `no-cache` | Stored response must be revalidated before reuse |
| `max-age` | Maximum freshness lifetime |
| `s-maxage` | Freshness lifetime for shared caches |
| `must-revalidate` | Requires revalidation after becoming stale |

The presence of a cache-related header does not alone prove that a response is cached by an intermediary.

## Cache Architecture

Identify the caching layers involved in the request path.

Consider:

- Browser cache.
- Service worker.
- CDN.
- Reverse proxy.
- Application cache.
- API gateway.
- Backend response cache.

Determine which component is responsible for storing and returning a response.

Useful indicators include:

- `Age`
- `Via`
- `X-Cache`
- `CF-Cache-Status`
- `X-Cache-Hits`
- Provider-specific cache headers.

These headers are implementation-specific and may be absent, modified or misleading.

## Cache Key Analysis

A cache key determines which requests are treated as equivalent for caching purposes.

A typical cache key may include:

- Scheme.
- Host.
- Path.
- Query string.
- Selected request headers.
- Cookies, depending on configuration.

The critical question is:

**Can two requests that should receive different responses be treated as the same cache entry?**

### Cache Key Components

Assess whether the cache distinguishes:

| Component | Potential issue |
|---|---|
| Host | Host-based response differences |
| Path | Normalisation or extension handling |
| Query string | Ignored or inconsistently processed parameters |
| Cookies | User-specific response variations |
| Headers | Missing variation dimensions |
| Protocol | HTTP/HTTPS differences |
| Encoding | Inconsistent path or character normalisation |

### Cache Normalisation

Compare how different infrastructure components interpret:

- URL encoding.
- Repeated slashes.
- Path case.
- Dot segments.
- Trailing slashes.
- Query parameter ordering.
- Duplicate parameters.
- Encoded path separators.

Differences between the cache and application can create unexpected response reuse.

## Web Cache Poisoning

Web cache poisoning occurs when an attacker influences a response that is stored and subsequently served to other users.

A common pattern is:

1. A request contains an input that influences the response.
2. The input is not included in the cache key.
3. The response is stored.
4. Another user receives the modified response.

### Potential Unkeyed Inputs

Investigate whether the application uses request values that the cache does not distinguish.

Examples include:

- `X-Forwarded-Host`
- `X-Forwarded-Scheme`
- `X-Forwarded-Proto`
- `X-Original-URL`
- `X-Rewrite-URL`
- `X-Forwarded-Prefix`
- Custom application headers.

These headers are not inherently dangerous. Their significance depends on whether they influence the response and how the cache handles them.

### Common Outcomes

Potential impact includes:

- Stored XSS.
- Malicious redirects.
- Incorrect resource URLs.
- Content manipulation.
- Cached error responses.
- Information disclosure.
- Application-specific logic manipulation.

A cache poisoning finding should demonstrate that the affected response is actually stored and served to another request context.

## Web Cache Deception

Web cache deception occurs when an attacker causes an application to return sensitive content for a URL that a cache incorrectly considers publicly cacheable.

A common architectural pattern involves:

1. A sensitive endpoint.
2. A cache that applies path-based caching rules.
3. Application routing that ignores or interprets a path suffix differently.
4. A response that is incorrectly stored.

For example, an application may return account content for a path that an intermediary treats as a static resource.

### Assessment Considerations

Investigate:

- Static file extension handling.
- Path routing.
- URL normalisation.
- Trailing path segments.
- Application route matching.
- Cache rules.
- Authentication cookies.
- Response cache directives.

Never use another real user's account to demonstrate data exposure.

Use dedicated test accounts and controlled content.

## Cache-Control Assessment

Review caching directives on:

- Authenticated pages.
- Account dashboards.
- API responses.
- Password reset pages.
- Personal data.
- Administrative interfaces.
- Financial or transaction pages.
- Error responses.

Sensitive content should not be stored in shared caches unless a deliberate, secure design requires it.

Consider whether:

- `private` is appropriate.
- `no-store` is required.
- Shared caches respect `s-maxage`.
- Authenticated responses are cached.
- Cache invalidation occurs after sensitive state changes.
- Responses vary correctly by user or tenant.

## Cache Variation and Normalisation

### Vary Header

The `Vary` header indicates which request headers influence a response representation.

Example:

```http
Vary: Accept-Encoding
```

If an application varies its response based on a header but the cache does not account for that variation, different users may receive the wrong representation.

### Host and Forwarding Headers

Applications may generate absolute URLs using host or proxy headers.

Determine whether untrusted values can influence:

- Password reset links.
- Redirect URLs.
- Canonical URLs.
- Static asset references.
- Email links.
- Application metadata.

### Cache Invalidation

Assess whether sensitive changes invalidate relevant cache entries.

Examples:

- Logout.
- Password change.
- Permission change.
- Account suspension.
- Resource deletion.
- Tenant membership change.

## Assessment Methodology

### 1. Identify Cache Layers

Determine which components may cache responses.

Record relevant headers, DNS/CDN information and application behaviour.

### 2. Establish a Baseline

Request representative resources repeatedly.

Record:

- Status code.
- Response body.
- Cache-related headers.
- `Age` values.
- Response timing.
- Cookies.
- User authentication state.

### 3. Identify Cacheable Responses

Determine which responses are:

- Public.
- Private.
- Authenticated.
- Static.
- Dynamic.
- Explicitly non-cacheable.

### 4. Map Cache Keys

Compare responses when changing one request attribute at a time.

Examples:

- Query parameter.
- Host-related header.
- Forwarding header.
- Cookie.
- Path variation.
- Accepted content type.

Do not change multiple variables simultaneously unless investigating an identified interaction.

### 5. Identify Unkeyed Inputs

Determine whether an input affects the response without affecting cache identity.

Use harmless, unique marker values.

### 6. Validate Cache Storage

Check whether:

- The response is stored.
- The response is served on subsequent requests.
- The response survives across sessions.
- The response is shared between test accounts.

Use dedicated test accounts and controlled test data.

### 7. Assess Impact

Determine whether the behaviour can expose sensitive data or affect other users.

Avoid poisoning shared production cache entries.

## Validation and Impact

A strong finding should demonstrate:

- A controllable input.
- A response influenced by that input.
- The relevant cache key behaviour.
- Evidence that the response was stored.
- Evidence that a subsequent request received the stored response.
- The security impact.

Do not report a cache vulnerability based only on the presence of `X-Cache: HIT` or `Age`.

## Mitigation

Recommended controls:

- Define cache keys explicitly.
- Ensure cache keys include all response-relevant inputs.
- Avoid trusting unvalidated forwarding headers.
- Use `Cache-Control: no-store` for sensitive responses where appropriate.
- Use `private` for user-specific content.
- Apply consistent URL normalisation.
- Ensure CDN and application routing agree.
- Avoid caching authenticated responses unintentionally.
- Configure appropriate `Vary` headers.
- Invalidate cache entries after sensitive state changes.
- Separate public and private caching policies.
- Test cache behaviour after infrastructure changes.

## Tools and References

### Tools

- Burp Suite.
- Burp Repeater.
- Burp Param Miner.
- Browser developer tools.
- curl.
- CDN-specific diagnostic headers.
- HTTP response comparison tools.

### References

- [PortSwigger — Web Cache Poisoning](https://portswigger.net/web-security/web-cache-poisoning)
- [PortSwigger — Web Cache Deception](https://portswigger.net/web-security/web-cache-deception)
- [RFC 9111 — HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111)
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)

## Assessment Checklist

- [ ] Cache architecture identified.
- [ ] Cache-related response headers reviewed.
- [ ] Authenticated and unauthenticated responses compared.
- [ ] Cache key components investigated.
- [ ] Unkeyed inputs identified.
- [ ] Host and forwarding headers assessed.
- [ ] URL normalisation differences investigated.
- [ ] Cache-Control directives reviewed.
- [ ] Sensitive responses assessed for shared caching.
- [ ] Cache storage behaviour confirmed.
- [ ] Cross-user impact validated safely.
- [ ] Remediation documented.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
