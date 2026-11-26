# HTTP Requests, Responses and Headers

## Overview

HTTP communication consists of requests sent by clients and responses returned by servers.

Both messages contain structured information used to describe the communication.

## HTTP Request Structure

A typical HTTP/1.1 request:

    GET /account/profile HTTP/1.1
    Host: example.com
    User-Agent: Mozilla/5.0
    Accept: text/html
    Cookie: session=abc123

    [Optional request body]

The request contains:

| Component | Description |
|---|---|
| Method | Action being requested |
| Request target | Requested resource |
| HTTP version | Protocol version |
| Headers | Additional request information |
| Body | Optional data sent to the server |

## HTTP Response Structure

Example response:

    HTTP/1.1 200 OK
    Content-Type: text/html; charset=UTF-8
    Content-Length: 1256
    Server: nginx

    <html>
    <body>
    <h1>Welcome</h1>
    </body>
    </html>

The response contains:

| Component | Description |
|---|---|
| Status line | HTTP version and status code |
| Headers | Metadata about the response |
| Body | Returned content, if present |

## Common Request Headers

| Header | Purpose |
|---|---|
| Host | Identifies the requested hostname |
| User-Agent | Identifies the client application |
| Accept | Specifies acceptable response media types |
| Accept-Language | Indicates preferred languages |
| Accept-Encoding | Specifies supported compression formats |
| Authorization | Supplies authentication credentials |
| Cookie | Sends stored cookies |
| Content-Type | Describes the request body format |
| Content-Length | Indicates the message body length |
| Origin | Identifies the origin initiating a request |
| Referer | Identifies the referring URL |
| Cache-Control | Specifies caching behaviour |

## Common Response Headers

| Header | Purpose |
|---|---|
| Server | Identifies server software, if disclosed |
| Date | Indicates response generation time |
| Content-Type | Describes returned content |
| Content-Length | Indicates response body length |
| Set-Cookie | Instructs the client to store a cookie |
| Cache-Control | Controls caching behaviour |
| Location | Identifies a redirect destination |
| Content-Encoding | Indicates response compression |
| Content-Security-Policy | Defines browser content security rules |
| Strict-Transport-Security | Requests HTTPS-only access |
| X-Content-Type-Options | Controls MIME type sniffing |
| Referrer-Policy | Controls referrer information disclosure |
| Access-Control-Allow-Origin | Specifies permitted CORS origins |

## Content-Type

The Content-Type header describes the media type of a message body.

Common values:

| Content-Type | Description |
|---|---|
| text/html | HTML document |
| text/plain | Plain text |
| application/json | JSON data |
| application/xml | XML data |
| application/pdf | PDF document |
| application/octet-stream | Generic binary data |
| multipart/form-data | Multipart form submission |
| application/x-www-form-urlencoded | URL-encoded form data |
| image/png | PNG image |
| image/jpeg | JPEG image |

## Content-Encoding

Content-Encoding indicates how the message body has been encoded for transfer.

Common values:

- gzip
- br (Brotli)
- deflate
- zstd

Content-Encoding is different from Content-Type.

For example:

    Content-Type: application/json
    Content-Encoding: gzip

This indicates that the response contains JSON data compressed using gzip.

## Forwarding Headers

Reverse proxies and load balancers may add forwarding headers.

| Header | Purpose |
|---|---|
| Forwarded | Standardised proxy information |
| X-Forwarded-For | Original client IP address, as reported by a proxy |
| X-Forwarded-Host | Original requested hostname |
| X-Forwarded-Proto | Original request scheme |
| X-Real-IP | Client IP address, commonly used by Nginx configurations |

Forwarding headers are not inherently trustworthy.

Applications should only rely on these values when they are supplied or sanitised by trusted proxy infrastructure.

## Cache-Control

Controls how responses may be cached.

Common directives:

| Directive | Meaning |
|---|---|
| no-store | Do not store the response |
| no-cache | Revalidate before reuse |
| public | May be stored by shared caches |
| private | Intended for private caches |
| max-age=3600 | Fresh for 3600 seconds |
| must-revalidate | Revalidation required when stale |

Important distinction:

`no-cache` does not mean the response cannot be stored. It means the cached response must be revalidated before reuse.

## Header Security Considerations

Headers can influence browser behaviour and application security.

Examples of security-relevant headers:

- Strict-Transport-Security
- Content-Security-Policy
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy
- Cross-Origin-Opener-Policy
- Cross-Origin-Resource-Policy

Headers should be configured consistently with the application's architecture and security requirements.

## Key Takeaways

- Requests and responses have structured components.
- Headers provide metadata and influence application behaviour.
- Content-Type and Content-Encoding serve different purposes.
- Forwarding headers require trusted proxy configuration.
- Security headers help enforce browser-side protections.
