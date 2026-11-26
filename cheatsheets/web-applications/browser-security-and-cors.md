# Browser Security and CORS

## Overview

Web browsers implement security controls to restrict how websites interact with other websites, local resources and sensitive user information.

These controls help reduce the impact of malicious websites and compromised applications.

## Same-Origin Policy

The Same-Origin Policy (SOP) is a browser security mechanism that restricts how documents and scripts from one origin interact with resources from another origin.

An origin consists of:

- Scheme
- Host
- Port

For example:

    https://example.com:443

The following URLs share an origin:

    https://example.com/page1
    https://example.com/page2

The following URLs have different origins:

    http://example.com
    https://example.com

    https://example.com
    https://api.example.com

    https://example.com:443
    https://example.com:8443

Differences in scheme, hostname or port result in different origins.

## Same-Origin vs Same-Site

These concepts are not interchangeable.

**Same-origin**

Requires matching scheme, hostname and port.

**Same-site**

Generally considers the registrable domain and scheme, rather than requiring an identical hostname and port.

For example:

    https://www.example.com
    https://api.example.com

These are different origins but can be considered same-site.

## Cross-Origin Resource Sharing (CORS)

CORS is a browser-enforced mechanism that allows servers to specify which origins may access resources through cross-origin requests.

Servers communicate CORS policies using HTTP response headers.

Example:

    Access-Control-Allow-Origin: https://trusted.example

This indicates that the specified origin is permitted to access the response through browser CORS mechanisms.

## Common CORS Headers

| Header | Purpose |
|---|---|
| Access-Control-Allow-Origin | Permitted origin |
| Access-Control-Allow-Methods | Permitted HTTP methods |
| Access-Control-Allow-Headers | Permitted request headers |
| Access-Control-Allow-Credentials | Whether credentials are supported |
| Access-Control-Expose-Headers | Response headers available to scripts |
| Access-Control-Max-Age | Preflight result cache duration |
| Origin | Origin initiating the request |

## CORS Preflight Requests

Some cross-origin requests require a preflight request.

A preflight is an HTTP OPTIONS request used by the browser to determine whether the actual request is permitted.

Example:

    OPTIONS /api/profile HTTP/1.1
    Host: api.example.com
    Origin: https://app.example.com
    Access-Control-Request-Method: PUT
    Access-Control-Request-Headers: content-type, authorization

The server may respond with:

    HTTP/1.1 204 No Content
    Access-Control-Allow-Origin: https://app.example.com
    Access-Control-Allow-Methods: GET, POST, PUT
    Access-Control-Allow-Headers: Content-Type, Authorization

If the preflight succeeds, the browser can proceed with the actual request.

Not every cross-origin request requires preflight.

## CORS and Credentials

When a browser request includes credentials, the server must explicitly allow credentialed access.

Example:

    Access-Control-Allow-Origin: https://app.example.com
    Access-Control-Allow-Credentials: true

A wildcard origin (`*`) cannot be used with credentialed CORS responses.

## Content Security Policy

Content Security Policy (CSP) is a browser security mechanism that restricts the sources from which certain resources may be loaded or executed.

It is commonly delivered through an HTTP response header.

Example:

    Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'

Common directives:

| Directive | Purpose |
|---|---|
| default-src | Default resource policy |
| script-src | Permitted JavaScript sources |
| style-src | Permitted stylesheet sources |
| img-src | Permitted image sources |
| font-src | Permitted font sources |
| connect-src | Permitted connection destinations |
| frame-src | Permitted iframe sources |
| object-src | Permitted plugin/object sources |
| base-uri | Restricts document base URLs |
| form-action | Restricts form submission destinations |
| frame-ancestors | Controls which sites may embed the page |

CSP can reduce the impact of certain cross-site scripting attacks, but it is not a replacement for secure application development.

## Clickjacking Protection

Clickjacking involves tricking a user into interacting with an interface they cannot clearly see or understand.

Common protections include:

### X-Frame-Options

    X-Frame-Options: DENY

Common values:

- DENY
- SAMEORIGIN

### Content-Security-Policy frame-ancestors

    Content-Security-Policy: frame-ancestors 'self'

CSP `frame-ancestors` is the more flexible modern control.

## Cross-Origin Isolation Headers

Additional headers can control how documents and resources interact across origins.

| Header | Purpose |
|---|---|
| Cross-Origin-Opener-Policy | Controls browsing context relationships |
| Cross-Origin-Embedder-Policy | Controls embedding of cross-origin resources |
| Cross-Origin-Resource-Policy | Controls which origins may load a resource |

These headers can be used together to establish cross-origin isolation.

## Other Browser Security Headers

| Header | Purpose |
|---|---|
| Strict-Transport-Security | Enforces HTTPS for future connections |
| X-Content-Type-Options | Prevents MIME type sniffing |
| Referrer-Policy | Controls referrer information |
| Permissions-Policy | Controls access to browser features |

## Key Takeaways

- An origin consists of scheme, host and port.
- Same-origin and same-site are different concepts.
- CORS controls browser access to cross-origin responses.
- Preflight requests use OPTIONS.
- CSP restricts permitted resource sources.
- Clickjacking protections restrict framing.
- Browser security headers should complement application-side controls.
