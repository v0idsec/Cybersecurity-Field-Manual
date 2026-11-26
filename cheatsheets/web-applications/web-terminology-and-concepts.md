# Web Terminology and Concepts

## Overview

This document provides a quick reference for common terminology encountered when working with web applications, infrastructure and application security.

## Web Architecture

| Term | Description |
|---|---|
| Client | Application making a request |
| Server | System processing requests |
| Frontend | User-facing application interface |
| Backend | Server-side application logic |
| Web server | Software handling HTTP communication |
| Application server | Executes application logic |
| Reverse proxy | Receives requests and forwards them to backend services |
| Forward proxy | Acts on behalf of clients |
| Load balancer | Distributes traffic across multiple servers |
| CDN | Content Delivery Network |
| Origin server | Server hosting the original resource |
| Middleware | Software operating between application components |
| Microservices | Architecture consisting of independently deployable services |

## Data Formats

| Format | Description |
|---|---|
| HTML | Hypertext Markup Language |
| CSS | Cascading Style Sheets |
| JavaScript | Programming language used extensively in web development |
| JSON | JavaScript Object Notation |
| XML | Extensible Markup Language |
| YAML | Human-readable data serialisation format |
| CSV | Comma-Separated Values |
| URL-encoded | Form data encoded using URL encoding |
| Base64 | Binary-to-text encoding scheme |

Encoding is not encryption.

For example, Base64 does not provide confidentiality or meaningful protection for sensitive data.

## APIs

| Term | Description |
|---|---|
| API | Application Programming Interface |
| REST | Architectural style for networked applications |
| RESTful API | API designed around REST principles |
| SOAP | Protocol for structured web service messaging |
| GraphQL | Query language and runtime for APIs |
| RPC | Remote Procedure Call |
| gRPC | High-performance RPC framework |
| Endpoint | Addressable API resource or operation |
| Payload | Data carried by a request or response |
| Schema | Definition of data structure |
| Rate limiting | Restricts request frequency |
| Pagination | Splits large result sets into smaller responses |

## Authentication and Identity

| Term | Description |
|---|---|
| Authentication | Verifying identity |
| Authorisation | Determining access permissions |
| Session | State associated with a user or client |
| Cookie | Browser-stored data associated with a website |
| Token | Data representing an authentication or authorisation grant |
| JWT | JSON Web Token |
| OAuth 2.0 | Delegated authorisation framework |
| OpenID Connect | Identity layer built on OAuth 2.0 |
| MFA | Multi-Factor Authentication |
| SSO | Single Sign-On |
| RBAC | Role-Based Access Control |
| ABAC | Attribute-Based Access Control |

## Web Infrastructure

| Term | Description |
|---|---|
| DNS | Domain Name System |
| IP address | Network address identifying an interface |
| TCP | Transmission Control Protocol |
| UDP | User Datagram Protocol |
| TLS | Transport Layer Security |
| HTTPS | HTTP protected by TLS |
| WAF | Web Application Firewall |
| CDN | Content Delivery Network |
| Cache | Temporary storage of data |
| Reverse proxy | Intermediary between clients and backend services |
| Origin | Scheme, hostname and port combination |
| Subdomain | A hostname beneath a parent domain |

## Application Concepts

| Term | Description |
|---|---|
| DOM | Document Object Model |
| SPA | Single-Page Application |
| SSR | Server-Side Rendering |
| CSR | Client-Side Rendering |
| Hydration | Attaching client-side functionality to server-rendered content |
| WebSocket | Persistent, bidirectional communication protocol |
| Webhook | HTTP callback triggered by an event |
| Service worker | Browser script operating in the background |
| Local storage | Browser storage mechanism |
| Session storage | Browser storage limited to a page session |
| IndexedDB | Browser-based database |
| Iframe | HTML element embedding another browsing context |

## Common Security Terminology

| Term | Description |
|---|---|
| XSS | Cross-Site Scripting |
| CSRF | Cross-Site Request Forgery |
| SSRF | Server-Side Request Forgery |
| SQLi | SQL Injection |
| IDOR | Insecure Direct Object Reference |
| XXE | XML External Entity |
| CSP | Content Security Policy |
| CORS | Cross-Origin Resource Sharing |
| SOP | Same-Origin Policy |
| HSTS | HTTP Strict Transport Security |
| Clickjacking | Tricking users into interacting with an unintended interface |
| Deserialisation | Reconstructing objects from stored or transmitted data |
| Input validation | Checking supplied data against expected requirements |
| Output encoding | Transforming data before rendering it in a particular context |

## Common Web Vulnerability Concepts

| Vulnerability | High-Level Description |
|---|---|
| Cross-Site Scripting | Untrusted content executes as script in a browser |
| Cross-Site Request Forgery | A user's browser is induced to make an unwanted authenticated request |
| SQL Injection | Untrusted input influences SQL query execution |
| Server-Side Request Forgery | Server is manipulated into making unintended requests |
| Broken Access Control | Users can perform actions or access resources beyond their permissions |
| Authentication Bypass | Authentication controls can be circumvented |
| Path Traversal | File paths are manipulated to access unintended locations |
| File Upload Vulnerability | Unsafe file handling creates security exposure |
| Insecure Deserialisation | Untrusted serialized data is processed unsafely |
| Security Misconfiguration | Incorrect settings expose application functionality or data |

## Important Distinctions

### Encoding vs Encryption vs Hashing

| Concept | Purpose | Reversible? |
|---|---|---|
| Encoding | Changes data representation | Yes |
| Encryption | Protects confidentiality using keys | Yes, with the appropriate key |
| Hashing | Produces a fixed-size digest | Not designed to be reversed |

### Authentication vs Authorisation

- Authentication establishes identity.
- Authorisation determines permissions.

### Frontend vs Backend

- Frontend code runs in the user's environment, usually a browser.
- Backend code runs on servers or other infrastructure.

Never assume frontend validation is sufficient to protect backend resources.

### Client-Side vs Server-Side

| Client-Side | Server-Side |
|---|---|
| Executes in the browser | Executes on server infrastructure |
| Handles user interface behaviour | Handles application logic and data |
| Can be inspected by users | Not normally directly exposed |
| Cannot be trusted for access control | Must enforce access control |

## Key Takeaways

- Web applications consist of multiple interacting components.
- APIs enable communication between software systems.
- Authentication, authorisation and session management are distinct concepts.
- Encoding, encryption and hashing serve different purposes.
- Client-side controls should never replace server-side security enforcement.
- Understanding web terminology makes technical documentation and security assessments easier to follow.
