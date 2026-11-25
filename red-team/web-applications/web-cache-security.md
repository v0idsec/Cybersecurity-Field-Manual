
# Web Cache Security

> Professional reference guide for assessing cache configuration, cache key integrity, cache isolation and security controls across web applications and delivery infrastructure.

## Contents

- [Overview](#overview)
- [Caching Architecture](#caching-architecture)
- [Cache Security Principles](#cache-security-principles)
- [Cache Key Integrity](#cache-key-integrity)
- [Authenticated Content](#authenticated-content)
- [Sensitive Data Caching](#sensitive-data-caching)
- [Cache Invalidation](#cache-invalidation)
- [CDN and Reverse Proxy Security](#cdn-and-reverse-proxy-security)
- [Service Worker Caching](#service-worker-caching)
- [API Caching](#api-caching)
- [Assessment Methodology](#assessment-methodology)
- [Common Misconfigurations](#common-misconfigurations)
- [Mitigation](#mitigation)
- [Tools and References](#tools-and-references)
- [Assessment Checklist](#assessment-checklist)

---

## Overview

Caching is an important component of modern web architecture.

It reduces latency, improves application performance and reduces backend infrastructure load.

However, incorrect caching configuration can introduce security vulnerabilities even when the application itself implements appropriate authentication and authorisation controls.

This guide focuses on the security of caching systems and their interaction with web applications.

It complements the dedicated [Caching](caching.md) guide, which focuses on web cache poisoning and deception.

Areas of interest include:

- Cache isolation.
- Cache key integrity.
- Authenticated response handling.
- Sensitive information storage.
- Cache invalidation.
- CDN configuration.
- Reverse proxy behaviour.
- Browser caching.
- Service worker caching.
- API response caching.

## Caching Architecture

Identify every caching layer involved in delivering application content.

| Layer | Security considerations |
|---|---|
| Browser cache | Local storage of sensitive responses |
| Service worker | Application-controlled request and response caching |
| CDN | Shared caching across users and locations |
| Reverse proxy | Cache key and authentication handling |
| API gateway | Response caching and tenant separation |
| Application cache | User-specific and permission-sensitive data |
| Database cache | Data isolation and invalidation |

Caching behaviour may differ between environments.

Assess production-like infrastructure where possible, including:

- Public-facing applications.
- Internal applications.
- Administrative interfaces.
- APIs.
- Mobile application backends.
- Multi-tenant platforms.

## Cache Security Principles

A secure caching implementation should maintain the following properties.

### Confidentiality

Sensitive information must not be disclosed to users who are not authorised to access it.

### Integrity

Cached content must not be altered or incorrectly associated with another request.

### Isolation

Responses intended for one user or tenant must not be served to another.

### Freshness

Changes to sensitive information and permissions must be reflected appropriately.

### Predictability

Cache behaviour should be consistent across browsers, proxies, CDNs and application components.

## Cache Key Integrity

The cache key determines which requests share a cached response.

Review whether the key accounts for every request property that can influence the response.

Potential dimensions include:

- Host.
- Scheme.
- Path.
- Query parameters.
- Cookies.
- Authorisation context.
- Selected request headers.
- Content negotiation.
- Tenant identity.
- Locale.
- User-specific preferences.

### Key Integrity Questions

- Can different users receive the same cache entry?
- Are authentication cookies ignored?
- Are tenant identifiers included where required?
- Are query parameters normalised consistently?
- Are host and forwarding headers trusted?
- Are content-negotiation variations handled correctly?
- Can an attacker influence the cache key?
- Can two different application routes resolve to one cache entry?

### Cache Key Collisions

A cache key collision occurs when distinct requests are treated as equivalent by the cache.

This becomes security-relevant when the application generates different responses for those requests.

Investigate:

- Duplicate query parameters.
- Parameter ordering.
- URL encoding.
- Path normalisation.
- Case sensitivity.
- Header normalisation.
- Host handling.

## Authenticated Content

Authenticated content requires particular attention.

Examples include:

- User dashboards.
- Account details.
- Personal profiles.
- Transaction histories.
- Support conversations.
- Administrative interfaces.
- Organisation-specific resources.

Determine whether authenticated responses can be stored in:

- Browser caches.
- Shared proxy caches.
- CDN caches.
- Application caches.

### Authentication and Cache Behaviour

Compare responses using:

- No authentication.
- Valid authentication.
- Expired authentication.
- Different test accounts.
- Different roles.
- Different tenants.

Check whether the same cached response can be returned across different authentication contexts.

A response being served from a browser's private cache is not equivalent to a shared cache exposing it to another user.

Distinguish the caching layer when reporting an issue.

## Sensitive Data Caching

Identify responses containing:

- Personal information.
- Authentication tokens.
- Session identifiers.
- Financial information.
- Health information.
- Password reset data.
- Administrative information.
- Confidential business data.

Review relevant directives:

```http
Cache-Control: no-store
```

```http
Cache-Control: private, no-cache
```

```http
Cache-Control: public, max-age=3600
```

These directives have different meanings.

In particular:

- `no-store` instructs caches not to store the response.
- `private` restricts storage to private caches.
- `no-cache` requires revalidation before reuse; it does not mean the response cannot be stored.
- `public` permits shared caching.

Assess whether the chosen policy matches the sensitivity and intended use of the response.

## Cache Invalidation

Cache invalidation ensures outdated or unauthorised content is not served after application state changes.

Important events include:

- User logout.
- Password change.
- Session revocation.
- Account suspension.
- Role modification.
- Permission changes.
- Tenant membership changes.
- Resource deletion.
- Content updates.

### Invalidation Questions

- Are relevant cache entries invalidated after logout?
- Do permission changes affect cached responses?
- Can suspended accounts continue receiving cached content?
- Are deleted resources removed from caches?
- Are invalidation operations reliable?
- Do all CDN regions receive invalidation updates?
- Are stale responses served during revalidation?

### Stale Content

Stale content may be acceptable for public static resources but dangerous for:

- Permission-sensitive data.
- Account status.
- Financial transactions.
- Security settings.
- Administrative operations.

Assess whether stale responses create a meaningful security issue.

## CDN and Reverse Proxy Security

CDNs and reverse proxies often sit between users and application infrastructure.

Review:

- Origin access restrictions.
- Host header handling.
- Cache key configuration.
- Origin request policies.
- Forwarded headers.
- TLS termination.
- Cache bypass rules.
- Authentication-aware caching.
- Error response caching.
- Cache invalidation controls.

### Origin Exposure

Determine whether the backend origin can be accessed directly, bypassing the CDN or WAF.

Consider whether direct-origin access allows an attacker to bypass:

- WAF inspection.
- Rate limiting.
- Geographic restrictions.
- Authentication gateways.
- Request normalisation.
- Security headers.

Origin exposure is not automatically a vulnerability, but it may weaken controls that are expected to operate at the edge.

### Cache Bypass Rules

Review rules intended to bypass caching for:

- Authenticated requests.
- Dynamic routes.
- API endpoints.
- Administrative pages.
- Sensitive file types.

Misconfigured bypass rules can result in unexpected caching or inconsistent application behaviour.

## Service Worker Caching

Service workers can intercept browser requests and implement custom caching strategies.

Review:

- Cache storage contents.
- Cache matching behaviour.
- Cache update logic.
- Authentication-aware caching.
- Offline functionality.
- Cache versioning.
- Logout behaviour.
- User switching.

Potential weaknesses include:

- Sensitive responses retained after logout.
- User-specific data reused across sessions.
- Incorrect cache matching.
- Stale authorisation-sensitive content.
- Inadequate cache cleanup.

Inspect service worker scripts and browser Cache Storage where authorised.

## API Caching

APIs frequently return user-specific and tenant-specific data.

Review:

- `GET` response caching.
- Authenticated API responses.
- GraphQL response caching.
- API gateway policies.
- Query parameter handling.
- Tenant-specific responses.
- Rate-limit interactions.
- Error response caching.

### API Cache Isolation

Compare requests from separate test accounts.

Check whether:

- Account A receives Account B's cached response.
- Tenant-specific data is isolated.
- Role changes affect cached results.
- API keys or bearer tokens influence cache identity.
- Different query parameters produce the correct response.

### GraphQL Considerations

GraphQL applications may use:

- POST-based queries.
- GET-based queries.
- Persisted queries.
- CDN caching.
- Application-level caching.

Assess whether cache behaviour correctly reflects the operation, variables and authorisation context.

## Assessment Methodology

### 1. Map the Caching Architecture

Identify:

- Browser caching.
- Service workers.
- CDN.
- Reverse proxies.
- API gateways.
- Application caches.

Record relevant technologies and observable cache headers.

### 2. Identify Sensitive Responses

Prioritise:

- Authenticated pages.
- API responses.
- Personal data.
- Financial records.
- Administrative content.
- Tenant-specific information.

### 3. Review Cache Directives

Inspect:

- `Cache-Control`
- `Expires`
- `Age`
- `ETag`
- `Last-Modified`
- `Vary`
- Provider-specific cache headers.

Compare directives against the intended sensitivity of the response.

### 4. Test Cache Isolation

Using dedicated test accounts, compare responses across:

- Authenticated sessions.
- Unauthenticated sessions.
- Different user roles.
- Different tenants.
- Different browser sessions.

Use unique test records to make response differences identifiable.

### 5. Test State Changes

Assess cache behaviour after:

- Logout.
- Password changes.
- Permission changes.
- Account suspension.
- Resource modification.
- Resource deletion.

### 6. Assess Edge Infrastructure

Review CDN and proxy behaviour, including:

- Origin access.
- Cache key configuration.
- Cache bypass rules.
- Host handling.
- Header forwarding.

### 7. Validate Findings

Establish:

- Which caching layer is responsible.
- Whether the response is actually cached.
- Whether the behaviour is reproducible.
- Which users or contexts are affected.
- Whether sensitive information is exposed.

## Common Misconfigurations

| Misconfiguration | Potential consequence |
|---|---|
| Authenticated responses marked public | Cross-user information disclosure |
| Missing `Vary` header | Incorrect response reuse |
| Incomplete cache key | Cache collisions |
| Sensitive content stored in shared cache | Confidentiality breach |
| Incorrect logout invalidation | Continued access to stale content |
| Weak CDN bypass rules | Unexpected cache behaviour |
| Direct origin exposure | Edge security control bypass |
| Incorrect service worker logic | Local data exposure |
| Stale permission-sensitive responses | Authorisation inconsistency |
| Cached error responses | Unexpected application behaviour |

## Mitigation

Recommended controls:

- Define cache policies based on data sensitivity.
- Avoid shared caching of user-specific responses.
- Use `Cache-Control: no-store` where appropriate.
- Use `private` for responses intended only for private caches.
- Ensure cache keys include relevant response dimensions.
- Apply correct `Vary` headers.
- Separate tenant and user-specific cache entries.
- Invalidate sensitive responses after state changes.
- Restrict direct origin access where appropriate.
- Review CDN and reverse proxy policies.
- Secure service worker cache handling.
- Avoid caching sensitive API responses by default.
- Monitor unexpected cache hits on sensitive endpoints.
- Test cache behaviour as part of release validation.

## Tools and References

### Tools

- Burp Suite.
- Burp Repeater.
- Browser developer tools.
- curl.
- CDN diagnostic tools.
- Browser Cache Storage inspection.
- HTTP response comparison tools.

### References

- [RFC 9111 — HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111)
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP HTTP Headers Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html)
- [MDN — HTTP Caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)
- [PortSwigger — Web Cache Vulnerabilities](https://portswigger.net/web-security/web-cache-poisoning)

## Assessment Checklist

- [ ] Caching architecture mapped.
- [ ] Browser, CDN and proxy caching identified.
- [ ] Sensitive responses identified.
- [ ] Cache-Control directives reviewed.
- [ ] Cache keys assessed.
- [ ] Authenticated response handling tested.
- [ ] Cross-user cache isolation verified.
- [ ] Tenant isolation assessed.
- [ ] Cache invalidation tested.
- [ ] Service worker behaviour reviewed.
- [ ] API caching assessed.
- [ ] CDN and origin exposure reviewed.
- [ ] Findings validated and impact documented.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
