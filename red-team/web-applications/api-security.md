# API Security Testing

## Overview

Application Programming Interfaces (APIs) allow applications, services and systems to communicate with one another.

Modern web applications often rely heavily on REST, GraphQL and other APIs. These interfaces can expose functionality and data that may not be accessible through the normal user interface.

API security testing focuses on identifying weaknesses in authentication, authorisation, input validation, data handling and business logic.

This guide covers API reconnaissance, common vulnerability classes, testing methodology, useful tools and remediation.

> **Authorisation:** Only test APIs and endpoints explicitly included in your engagement scope. Use approved test accounts and avoid accessing, modifying or deleting other users' data.

---

## Table of Contents

1. [API Fundamentals](#1-api-fundamentals)
2. [API Types](#2-api-types)
3. [API Reconnaissance](#3-api-reconnaissance)
4. [Authentication and Authorisation](#4-authentication-and-authorisation)
5. [Common API Vulnerabilities](#5-common-api-vulnerabilities)
6. [Testing Methodology](#6-testing-methodology)
7. [GraphQL Security](#7-graphql-security)
8. [API Documentation and Discovery](#8-api-documentation-and-discovery)
9. [Tools](#9-tools)
10. [Remediation](#10-remediation)
11. [Reporting](#11-reporting)
12. [Testing Checklist](#12-testing-checklist)
13. [References](#13-references)

---

## 1. API Fundamentals

An API provides a defined interface through which one system can request data or functionality from another.

A typical web API request contains:

- HTTP method.
- Endpoint or resource path.
- Headers.
- Authentication credentials or tokens.
- Query parameters.
- Request body.

### Example API request

```http
GET /api/v1/users/me HTTP/1.1
Host: example.com
Authorization: Bearer <ACCESS_TOKEN>
Accept: application/json
```

Example response:

```http
HTTP/1.1 200 OK
Content-Type: application/json
```

```json
{
  "id": 123,
  "username": "testuser",
  "role": "user"
}
```

### Common HTTP methods

| Method | Typical purpose |
|---|---|
| GET | Retrieve information |
| POST | Create resources or perform actions |
| PUT | Replace a resource |
| PATCH | Partially update a resource |
| DELETE | Delete a resource |
| OPTIONS | Discover supported communication options |
| HEAD | Retrieve response headers |

Do not assume that a method is safe simply because it is not commonly used by the frontend. Test actual behaviour within scope.

### Common response codes

| Status | Meaning |
|---|---|
| 200 | Successful request |
| 201 | Resource created |
| 204 | Successful request with no response body |
| 400 | Bad request |
| 401 | Unauthenticated |
| 403 | Forbidden |
| 404 | Resource not found |
| 405 | Method not allowed |
| 409 | Conflict |
| 422 | Unprocessable content |
| 429 | Rate limit exceeded |
| 500 | Internal server error |

---

## 2. API Types

### 2.1 REST APIs

REST APIs commonly use HTTP methods and resource-based URLs.

Example:

```text
GET    /api/users
GET    /api/users/123
POST   /api/users
PATCH  /api/users/123
DELETE /api/users/123
```

REST APIs frequently exchange JSON data.

### 2.2 GraphQL

GraphQL allows clients to request specific data through a query language.

A typical GraphQL endpoint may look like:

```text
POST /graphql
```

GraphQL commonly uses a single endpoint for multiple operations.

### 2.3 SOAP APIs

SOAP uses structured XML messages and commonly relies on a WSDL document to describe available operations.

SOAP implementations may introduce XML-specific security considerations.

### 2.4 WebSocket APIs

WebSockets provide persistent, bidirectional communication between clients and servers.

Security testing should consider:

- Connection authentication.
- Message authorisation.
- Origin validation.
- Session expiry.
- Message validation.
- Rate limiting.

### 2.5 Internal APIs

Internal APIs may connect backend services, microservices or infrastructure components.

They should not automatically be considered trusted. Internal services still require authentication, authorisation and appropriate network controls.

---

## 3. API Reconnaissance

API reconnaissance aims to identify endpoints, parameters, authentication mechanisms and available functionality.

### 3.1 Inspect browser traffic

Use Burp Suite Proxy or browser developer tools while interacting with the application.

Look for:

- `/api/` paths.
- JSON requests and responses.
- Authentication headers.
- Resource identifiers.
- Hidden application functionality.
- API version numbers.
- WebSocket connections.

### 3.2 Identify API endpoints

Common endpoint patterns include:

```text
/api/
/api/v1/
/api/v2/
/rest/
/graphql
/swagger/
/openapi.json
```

These are discovery leads, not guaranteed locations.

### 3.3 Review JavaScript

Frontend JavaScript can reveal API routes and expected request structures.

Useful search terms include:

```text
/api/
/graphql
fetch(
axios
Authorization
Bearer
baseURL
endpoint
```

Review discovered routes manually and confirm that they are in scope.

### 3.4 Inspect API documentation

Look for:

- OpenAPI specifications.
- Swagger UI.
- API reference documentation.
- GraphQL schema documentation.
- Developer portals.
- Public integration guides.

Documentation can reveal endpoints that are not obvious through normal application usage.

### 3.5 Build an API inventory

Maintain a structured record of discovered endpoints.

| Method | Endpoint | Authentication | Purpose | Notes |
|---|---|---|---|---|
| GET | `/api/v1/users/me` | Required | Current user | Profile |
| GET | `/api/v1/orders` | Required | List orders | Ownership check |
| POST | `/api/v1/orders` | Required | Create order | Input validation |
| PATCH | `/api/v1/users/me` | Required | Update profile | Mass assignment |

Record the expected role and permissions for each operation where known.

---

## 4. Authentication and Authorisation

Authentication establishes who a user is.

Authorisation determines what that user is allowed to do.

These are separate controls and should be assessed separately.

### 4.1 Authentication mechanisms

Common API authentication methods include:

- Session cookies.
- Bearer tokens.
- JWTs.
- API keys.
- OAuth 2.0 access tokens.
- Mutual TLS.

### 4.2 Missing authentication

Check whether sensitive API endpoints can be accessed without valid authentication.

Do not assume that an endpoint is protected because the frontend requires a login.

### 4.3 Broken authorisation

A user may be authenticated but still have access to resources or operations they should not be permitted to use.

Test using approved accounts with different roles and ownership boundaries.

### 4.4 Role-based access control

Review whether different user roles can access only their intended functionality.

Example roles:

| Role | Expected permissions |
|---|---|
| Anonymous | Public resources only |
| User | Own resources |
| Manager | Assigned organisational resources |
| Administrator | Administrative functionality |

The actual permission model depends on the application.

### 4.5 Token handling

Review:

- Token expiry.
- Token revocation.
- Token storage.
- Refresh token behaviour.
- Scope restrictions.
- Audience restrictions.
- Exposure through logs or URLs.

Avoid copying live credentials into reports or external tools.

---

## 5. Common API Vulnerabilities

The OWASP API Security Top 10 is a useful framework for organising API assessments.

### 5.1 Broken Object Level Authorisation (BOLA)

BOLA occurs when an API does not properly verify whether the authenticated user is allowed to access a particular object.

It is commonly associated with insecure direct object references.

Example endpoint:

```text
GET /api/v1/orders/1001
```

An order identifier may be supplied by the client.

**Assessment focus:**

- Can a user access only their own records?
- Are ownership checks performed server-side?
- Are nested resources checked independently?
- Are permissions enforced consistently across HTTP methods?

Use separate test accounts and test-owned records to demonstrate access-control boundaries safely.

### 5.2 Broken Function Level Authorisation (BFLA)

BFLA occurs when a user can access functionality intended for a different role.

Examples include:

- Standard users accessing administrative operations.
- Users modifying account settings reserved for administrators.
- Privileged API actions exposed without appropriate checks.

**Assessment focus:**

- Role restrictions.
- Administrative endpoints.
- Privileged operations.
- Backend enforcement independent of the frontend.

### 5.3 Broken Object Property Level Authorisation

This category includes weaknesses where an API exposes or permits modification of properties that a user should not control.

Two important patterns are:

**Excessive data exposure**

The API returns more information than the user needs.

**Mass assignment**

The API accepts properties that should be controlled exclusively by the server.

Example:

```json
{
  "display_name": "Test User",
  "role": "administrator"
}
```

The presence of a property in a request does not prove that it can be changed. Verify the application's actual behaviour using an approved test account.

### 5.4 Unrestricted Resource Consumption

APIs may expose expensive operations without suitable limits.

Potential issues include:

- Missing rate limits.
- Excessively large request bodies.
- Expensive search operations.
- Unbounded pagination.
- Resource-intensive file processing.
- Excessive concurrent requests.

Test limits conservatively. Do not deliberately exhaust production resources.

### 5.5 Broken Authentication

Potential weaknesses include:

- Weak session management.
- Inadequate token validation.
- Missing authentication on sensitive routes.
- Insecure password recovery.
- Improper token expiry.
- Inconsistent authentication across API versions.

### 5.6 Unrestricted Access to Sensitive Business Flows

An API may allow users to automate business operations that should have additional restrictions.

Examples:

- Repeated account creation.
- Excessive booking requests.
- Automated promotional claims.
- Repeated transaction initiation.

Assess whether the application applies appropriate business rules, rate limits and abuse protections.

### 5.7 Server-Side Request Forgery

An API may accept a URL or remote resource identifier that the backend retrieves.

Review URL-consuming functionality and refer to the [SSRF guide](ssrf.md).

### 5.8 Security Misconfiguration

Examples include:

- Debug endpoints exposed in production.
- Verbose error messages.
- Insecure CORS policies.
- Unnecessary HTTP methods.
- Missing security headers.
- Public API documentation exposing sensitive implementation details.

### 5.9 Improper Inventory Management

Organisations may operate undocumented, outdated or forgotten API versions.

Look for:

- Legacy API versions.
- Development endpoints.
- Deprecated functionality.
- Duplicate routes.
- Old authentication mechanisms.
- Unmaintained integrations.

### 5.10 Unsafe Consumption of APIs

Applications may trust data returned by third-party APIs without adequate validation.

Review how the application handles:

- External API responses.
- Third-party authentication.
- Data validation.
- Redirects.
- Unexpected response formats.
- External service failures.

---

## 6. Testing Methodology

### 6.1 Establish a baseline

For each endpoint:

1. Record the HTTP method and path.
2. Capture a normal request.
3. Record authentication requirements.
4. Record expected response behaviour.
5. Identify user-controlled parameters.
6. Document the expected permission level.

### 6.2 Test authentication

Using an authorised test account:

- Confirm protected endpoints reject unauthenticated requests.
- Check whether expired sessions are rejected.
- Review token refresh behaviour.
- Confirm logout invalidates the relevant session or token.
- Review access to sensitive endpoints.

### 6.3 Test object-level authorisation

Use two approved test accounts.

1. Create a test resource using account A.
2. Record the resource identifier.
3. Authenticate as account B.
4. Attempt to access the resource.
5. Confirm that access is denied unless explicitly permitted.

Repeat for relevant operations, such as reading, updating and deleting, using test-owned resources.

### 6.4 Test function-level authorisation

Compare the behaviour of accounts with different roles.

Check whether:

- Standard users can access administrative functions.
- Restricted operations are enforced server-side.
- Changing frontend parameters affects permissions.
- API versions enforce consistent role restrictions.

### 6.5 Test input validation

Review how the API handles:

- Missing fields.
- Unexpected fields.
- Incorrect data types.
- Null values.
- Empty strings.
- Excessively long values.
- Invalid JSON.
- Boundary values.

Use harmless inputs and avoid destructive operations.

### 6.6 Test HTTP methods

Check whether endpoints behave as documented.

Review:

- Supported methods.
- Unexpected methods.
- Method-specific authorisation.
- Consistency between GET, POST, PUT, PATCH and DELETE.

Do not assume that a hidden or undocumented method is vulnerable.

### 6.7 Test rate limiting

Assess whether sensitive or expensive endpoints enforce reasonable limits.

Record:

- Response behaviour.
- Rate-limit headers.
- HTTP 429 responses.
- Retry behaviour.
- Whether limits differ by account or endpoint.

Keep request volumes low and within engagement constraints.

### 6.8 Test error handling

Review whether errors expose:

- Stack traces.
- Internal paths.
- Database details.
- Framework versions.
- Debug information.
- Sensitive identifiers.

Document the minimum evidence needed to demonstrate the issue.

---

## 7. GraphQL Security

GraphQL requires some additional assessment considerations.

### 7.1 Schema discovery

Where schema introspection is enabled, it may reveal:

- Types.
- Queries.
- Mutations.
- Fields.
- Arguments.
- Relationships.

Introspection is not inherently a vulnerability. Its security impact depends on whether sensitive implementation details are exposed.

### 7.2 Query authorisation

Check whether authorisation is enforced at the resolver and object level.

A single GraphQL endpoint can expose many different operations, so endpoint-level authentication alone is insufficient.

### 7.3 Excessive query depth and complexity

Nested queries may consume significant application resources.

Review whether the application enforces:

- Query depth limits.
- Query complexity limits.
- Execution timeouts.
- Pagination limits.
- Rate limits.

### 7.4 Mutations

GraphQL mutations can modify application state.

Review:

- Authentication.
- Role restrictions.
- Object ownership.
- Input validation.
- Business logic.
- Audit logging.

Use test-owned records and avoid destructive mutations against real data.

### 7.5 Batching

Some GraphQL implementations support multiple operations in a single request.

Review whether batching creates opportunities to bypass rate limits or abuse expensive functionality.

---

## 8. API Documentation and Discovery

### OpenAPI

OpenAPI is a specification for describing HTTP APIs.

Common filenames include:

```text
openapi.json
openapi.yaml
swagger.json
swagger.yaml
```

A specification can reveal:

- Endpoint paths.
- HTTP methods.
- Parameters.
- Request schemas.
- Response schemas.
- Authentication requirements.

### Swagger UI

Swagger UI provides an interactive interface for API documentation.

Review whether it is publicly exposed and whether it reveals sensitive implementation information.

### Postman collections

Postman collections may contain:

- API endpoints.
- Example requests.
- Environment variables.
- Authentication workflows.
- Development and testing routes.

Treat any discovered secrets as sensitive. Do not use exposed credentials unless their use is explicitly authorised.

---

## 9. Tools

| Tool | Purpose |
|---|---|
| Burp Suite | Intercept and modify API traffic |
| OWASP ZAP | Automated and manual API testing |
| Postman | Build and organise API requests |
| Insomnia | API request testing |
| curl | Command-line HTTP requests |
| HTTPie | Readable HTTP requests |
| jq | Parse JSON responses |
| Kiterunner | API route discovery |
| ffuf | Content and endpoint discovery |
| Arjun | HTTP parameter discovery |
| mitmproxy | Intercept and inspect HTTP traffic |
| GraphQL Voyager | Visualise GraphQL schemas |
| InQL | GraphQL testing extension |
| Swagger UI | Inspect OpenAPI documentation |

### Useful command examples

Send a basic GET request:

```bash
curl -i https://example.com/api/v1/users/me
```

Send an authenticated request using a test token:

```bash
curl -i \
  -H "Authorization: Bearer <TEST_TOKEN>" \
  https://example.com/api/v1/users/me
```

Submit JSON:

```bash
curl -i -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TEST_TOKEN>" \
  -d '{"name":"Test User"}' \
  https://example.com/api/v1/users
```

Format JSON output:

```bash
curl -s https://example.com/api/v1/users/me | jq .
```

Inspect response headers:

```bash
curl -sSI https://example.com/api/v1/users/me
```

Replace example hosts and credentials with authorised engagement values. Never place real production tokens in shared command history or public documentation.

---

## 10. Remediation

### 10.1 Enforce object-level authorisation

Every operation involving a resource should verify that the authenticated user is permitted to access that specific resource.

Do not rely on unpredictable identifiers.

### 10.2 Enforce function-level authorisation

Use server-side role and permission checks for every privileged operation.

Hiding frontend controls is not a security boundary.

### 10.3 Use explicit property allowlists

Define which properties users can read and modify.

Avoid automatically binding arbitrary request fields to internal models.

### 10.4 Validate all input

Validate:

- Data types.
- Required fields.
- String lengths.
- Numeric ranges.
- Enumerated values.
- Nested objects.
- Unexpected properties.

Apply validation consistently across API versions.

### 10.5 Protect authentication tokens

- Use secure token storage.
- Enforce expiry.
- Validate issuer and audience where applicable.
- Support revocation where required.
- Avoid placing credentials in URLs.
- Prevent secrets from appearing in logs.

### 10.6 Apply rate limits

Use appropriate controls for:

- Authentication attempts.
- Resource-intensive operations.
- Account creation.
- Sensitive business workflows.
- Large requests.
- Expensive queries.

Consider account, user, IP and endpoint-level controls.

### 10.7 Limit returned data

Return only the information required for the requested operation.

Use response schemas and avoid exposing internal fields unnecessarily.

### 10.8 Maintain an API inventory

Document:

- Active API versions.
- Public endpoints.
- Internal endpoints.
- Authentication requirements.
- Data sensitivity.
- Owners.
- Deprecation status.

Remove or restrict unused interfaces.

### 10.9 Secure third-party integrations

Validate external responses and apply appropriate timeouts, authentication controls and failure handling.

Do not blindly trust data returned by external services.

---

## 11. Reporting

### Suggested report structure

**Title:** [API Vulnerability] in [Endpoint]

**Summary:**

Describe the affected API functionality and the security control that is missing or incorrectly implemented.

**Affected endpoint:**

```text
GET /api/v1/example/{id}
```

**Authentication context:**

Document the test account and role used, without including credentials.

**Steps to reproduce:**

1. Authenticate using an authorised test account.
2. Create or identify a test-owned resource.
3. Capture the relevant API request.
4. Repeat the request using the second authorised test account or role.
5. Record the resulting behaviour.

**Evidence:**

- Sanitised HTTP requests.
- Sanitised HTTP responses.
- Test account roles.
- Relevant resource identifiers.
- Screenshots where useful.

**Impact:**

Explain the demonstrated security consequence and affected trust boundary.

**Remediation:**

Recommend server-side authorisation, input validation, explicit property allowlists and appropriate rate limiting.

---

## 12. Testing Checklist

### Reconnaissance

- [ ] Identify API endpoints.
- [ ] Identify API versions.
- [ ] Review JavaScript for routes.
- [ ] Locate API documentation.
- [ ] Identify authentication mechanisms.
- [ ] Build an endpoint inventory.

### Authentication

- [ ] Check unauthenticated access.
- [ ] Review token expiry.
- [ ] Review session invalidation.
- [ ] Check authentication consistency across versions.

### Authorisation

- [ ] Test object-level access.
- [ ] Test function-level access.
- [ ] Compare different user roles.
- [ ] Review tenant boundaries.
- [ ] Check nested resource permissions.
- [ ] Test property-level permissions.

### Input and business logic

- [ ] Review input validation.
- [ ] Check unexpected properties.
- [ ] Review mass assignment protections.
- [ ] Check rate limits.
- [ ] Review pagination.
- [ ] Check business workflow restrictions.

### GraphQL

- [ ] Identify GraphQL endpoints.
- [ ] Review schema exposure.
- [ ] Check resolver-level authorisation.
- [ ] Review query depth and complexity limits.
- [ ] Assess mutation permissions.

### Reporting

- [ ] Capture sanitised evidence.
- [ ] Identify affected users and roles.
- [ ] Demonstrate impact safely.
- [ ] Avoid accessing unrelated user data.
- [ ] Provide actionable remediation.

---

## 13. References

- [OWASP API Security Top 10](https://owasp.org/API-Security/)
- [OWASP API Security Project](https://owasp.org/www-project-api-security/)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [Postman Learning Centre](https://learning.postman.com/)
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [GraphQL Documentation](https://graphql.org/learn/)
- [MITRE CWE](https://cwe.mitre.org/)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
