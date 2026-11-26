# HTTP Fundamentals

## Overview

HTTP (Hypertext Transfer Protocol) is an application-layer protocol used for communication between clients and servers.

It is the foundation of data exchange on the World Wide Web.

Common uses include:

- Loading websites
- Submitting forms
- Retrieving API data
- Uploading and downloading files
- Communicating with web applications

## Client-Server Model

HTTP generally follows a request-response model.

1. A client initiates a request.
2. The request is sent to a web server.
3. The server processes the request.
4. The server returns a response.
5. The client processes the response.

Common clients include:

- Web browsers
- Mobile applications
- Command-line applications
- API clients
- Automated services

Common servers include:

- Apache HTTP Server
- Nginx
- Microsoft IIS
- Application servers
- Cloud-hosted web services

## HTTP vs HTTPS

| Protocol | Default Port | Encryption |
|---|---:|---|
| HTTP | 80 | No |
| HTTPS | 443 | Yes, using TLS |

HTTP transmits application data without providing transport encryption.

HTTPS uses TLS (Transport Layer Security) to protect communications between the client and server.

HTTPS provides:

- Confidentiality
- Integrity
- Server authentication

HTTPS does not automatically guarantee that a website is trustworthy or free from vulnerabilities.

## HTTP Versions

| Version | Key Characteristics |
|---|---|
| HTTP/0.9 | Original, extremely limited protocol |
| HTTP/1.0 | Introduced headers and broader response support |
| HTTP/1.1 | Persistent connections and widespread adoption |
| HTTP/2 | Binary framing, multiplexing and header compression |
| HTTP/3 | Uses QUIC over UDP instead of TCP |

### HTTP/1.1

- Text-based protocol.
- Supports persistent connections.
- Commonly uses TCP.
- Multiple requests can reuse a connection.

### HTTP/2

- Uses binary framing.
- Supports multiplexing multiple streams over one connection.
- Uses HPACK header compression.
- Reduces some of the overhead associated with HTTP/1.1.

### HTTP/3

- Uses QUIC.
- Runs over UDP.
- Incorporates TLS 1.3 into the QUIC handshake.
- Supports independent streams to reduce transport-level head-of-line blocking.

## URLs

A URL (Uniform Resource Locator) identifies a resource.

Example:

    https://example.com:443/account/profile?id=123#settings

| Component | Value | Description |
|---|---|---|
| Scheme | https | Protocol |
| Host | example.com | Server hostname |
| Port | 443 | Destination port |
| Path | /account/profile | Requested resource |
| Query | id=123 | Additional parameters |
| Fragment | settings | Client-side resource fragment |

Fragments are generally processed by the client and are not included in the HTTP request sent to the server.

## DNS and HTTP

DNS (Domain Name System) translates domain names into IP addresses.

A simplified connection sequence:

1. Client requests the IP address for a hostname.
2. DNS resolution returns an address.
3. Client establishes a connection to the destination.
4. TLS negotiation occurs when HTTPS is used.
5. Client sends an HTTP request.
6. Server returns an HTTP response.

DNS resolution and HTTP communication are separate processes.

## Stateless Protocol

HTTP is fundamentally stateless.

Each request is independent from the perspective of the protocol. The server does not inherently remember previous requests.

Applications implement state using mechanisms such as:

- Cookies
- Session identifiers
- Authentication tokens
- Server-side session storage
- Application databases

## Common Related Technologies

| Technology | Purpose |
|---|---|
| HTML | Structures web content |
| CSS | Controls presentation and styling |
| JavaScript | Adds client-side functionality |
| JSON | Data interchange format |
| XML | Structured data format |
| REST | Architectural style for networked APIs |
| WebSocket | Persistent, bidirectional communication |
| DNS | Resolves domain names |
| TLS | Protects network communications |

## Key Takeaways

- HTTP is an application-layer protocol.
- HTTPS is HTTP protected by TLS.
- HTTP is stateless by design.
- DNS resolution occurs separately from HTTP requests.
- HTTP/2 and HTTP/3 improve communication efficiency through different transport and framing mechanisms.
