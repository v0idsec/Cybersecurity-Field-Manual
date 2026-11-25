# Web Application Penetration Testing Methodology

## Overview

A structured web application penetration test should systematically assess the application's attack surface, trust boundaries, authentication mechanisms, authorisation controls, input handling, business logic and supporting infrastructure.

This methodology provides a repeatable framework for conducting authorised web application security assessments.

It is designed as a professional field reference rather than a beginner's introduction to individual tools.

The methodology draws on established industry frameworks, including OWASP WSTG, OWASP ASVS, OWASP API Security Top 10 and PTES.

> **Engagement requirement:** All testing must remain within the agreed scope, Rules of Engagement (RoE), testing windows and approved impact limitations.

---

## Table of Contents

1. [Assessment Lifecycle](#1-assessment-lifecycle)
2. [Pre-Engagement](#2-pre-engagement)
3. [Scope and Attack Surface Mapping](#3-scope-and-attack-surface-mapping)
4. [Application Reconnaissance](#4-application-reconnaissance)
5. [Authentication Testing](#5-authentication-testing)
6. [Session Management](#6-session-management)
7. [Authorisation Testing](#7-authorisation-testing)
8. [Input Validation and Injection](#8-input-validation-and-injection)
9. [Client-Side Security](#9-client-side-security)
10. [API Security Assessment](#10-api-security-assessment)
11. [Business Logic Testing](#11-business-logic-testing)
12. [Server-Side Vulnerabilities](#12-server-side-vulnerabilities)
13. [Configuration and Infrastructure](#13-configuration-and-infrastructure)
14. [Advanced Testing Areas](#14-advanced-testing-areas)
15. [Evidence Collection](#15-evidence-collection)
16. [Finding Validation and Risk Assessment](#16-finding-validation-and-risk-assessment)
17. [Reporting](#17-reporting)
18. [Post-Engagement](#18-post-engagement)
19. [Assessment Checklist](#19-assessment-checklist)
20. [Reference Frameworks](#20-reference-frameworks)

---

## 1. Assessment Lifecycle

A professional assessment should follow a consistent lifecycle.

| Phase | Objective | Typical activities |
|---|---|---|
| 1. Preparation | Establish authorisation and boundaries | Scope, RoE, contacts |
| 2. Reconnaissance | Understand the target | Asset discovery, fingerprinting |
| 3. Mapping | Identify application functionality | Routes, parameters, roles |
| 4. Assessment | Identify security weaknesses | Authentication, access control, injection |
| 5. Validation | Confirm findings | Reproduction, impact assessment |
| 6. Evidence | Preserve supporting information | Requests, responses, screenshots |
| 7. Reporting | Communicate results | Risk ratings, remediation |
| 8. Closure | Complete engagement activities | Retesting, evidence handling |

### Core principles

- Understand normal application behaviour before testing abnormal behaviour.
- Test security controls at the server side, not just the frontend.
- Treat authentication and authorisation as separate assessment areas.
- Validate findings before assigning severity.
- Prefer minimal-impact proof of concept techniques.
- Maintain a clear record of testing activities.
- Distinguish confirmed vulnerabilities from theoretical attack paths.

---

## 2. Pre-Engagement

Before interacting with a target, establish the engagement boundaries.

### 2.1 Scope definition

Record all authorised assets.

| Scope item | Example |
|---|---|
| Primary domain | `app.example.com` |
| API hostname | `api.example.com` |
| Environment | Production / Staging |
| Application type | Web application |
| Authentication | Test accounts supplied |
| Exclusions | Third-party integrations |
| Testing window | Agreed engagement period |

Clarify whether the following are included:

- Subdomains.
- Related API endpoints.
- Mobile application backends.
- Third-party integrations.
- Cloud-hosted assets.
- Administrative interfaces.
- Authentication providers.
- External identity providers.

Do not assume that a related hostname, IP address or third-party service is in scope.

### 2.2 Rules of Engagement

Confirm:

- Permitted testing techniques.
- Prohibited activities.
- Rate limits.
- Testing windows.
- Data access restrictions.
- Destructive testing restrictions.
- Social engineering permissions.
- Denial-of-service restrictions.
- Escalation contacts.
- Emergency stop procedures.

### 2.3 Test accounts

Where possible, obtain accounts representing different application roles.

For example:

| Account | Role | Purpose |
|---|---|---|
| Account A | Standard user | Baseline permissions |
| Account B | Standard user | Cross-account testing |
| Account C | Manager | Privileged functionality |
| Account D | Administrator | Administrative controls |

Use synthetic data and test-owned resources wherever possible.

---

## 3. Scope and Attack Surface Mapping

The objective is to understand the application's externally reachable components and internal functionality.

### 3.1 Asset identification

Identify:

- Primary application domains.
- API hosts.
- Authentication endpoints.
- Static content hosts.
- CDN infrastructure.
- File storage endpoints.
- WebSocket endpoints.
- Administrative interfaces.
- Development and staging environments.

Maintain a record of the evidence supporting asset ownership and scope inclusion.

### 3.2 Technology fingerprinting

Identify relevant technologies:

- Web server.
- Application framework.
- Programming language.
- CMS.
- Frontend framework.
- Authentication provider.
- CDN or reverse proxy.
- API gateway.
- Third-party integrations.

Fingerprinting results should be treated as hypotheses until independently validated.

### 3.3 Attack surface inventory

Build a structured inventory.

| Component | Information to capture |
|---|---|
| Pages | Accessible routes |
| Parameters | Query, path and body parameters |
| Forms | Input fields and validation |
| APIs | Methods, paths and schemas |
| Authentication | Login, recovery, MFA |
| Sessions | Cookies and token behaviour |
| Uploads | File handling and storage |
| Integrations | External services |
| WebSockets | Connections and message types |
| Administrative features | Privileged operations |

### 3.4 Entry point identification

Pay particular attention to:

- User-controlled input.
- Resource identifiers.
- Redirect destinations.
- URL-fetching functionality.
- File processing.
- Search functionality.
- Export and import features.
- Account management.
- Payment and transaction workflows.

Every input is a potential assessment point, but prioritise based on exposure, sensitivity and application functionality.

---

## 4. Application Reconnaissance

### 4.1 Manual application mapping

Browse the application as a normal user.

Document:

- Available functionality.
- Navigation structure.
- User workflows.
- Role-specific features.
- Hidden or conditional functionality.
- State-changing operations.
- Error handling.

Do not rely exclusively on automated crawling.

### 4.2 HTTP request analysis

Review application traffic for:

- HTTP methods.
- Request parameters.
- Headers.
- Cookies.
- Authentication tokens.
- Content types.
- Response codes.
- Redirect behaviour.
- Caching behaviour.

Identify differences between frontend expectations and backend enforcement.

### 4.3 JavaScript analysis

Review client-side code for:

- API endpoints.
- Route definitions.
- Feature flags.
- Client-side access restrictions.
- Sensitive configuration.
- Source maps.
- Hardcoded test references.
- Unintended information disclosure.

Client-side restrictions should not be treated as security controls unless enforced by the backend.

### 4.4 Error analysis

Review errors for unintended disclosure of:

- Stack traces.
- Internal file paths.
- Framework details.
- Database information.
- Debug output.
- Internal service names.
- Sensitive identifiers.

### 4.5 Reconnaissance deliverable

Produce an application map containing:

- In-scope hosts.
- Technology observations.
- Endpoint inventory.
- User roles.
- Authentication flows.
- Identified integrations.
- High-value functionality.
- Areas requiring further investigation.

---

## 5. Authentication Testing

Authentication testing determines whether the application correctly establishes user identity.

### 5.1 Registration

Assess:

- Account creation controls.
- Email verification.
- Duplicate account handling.
- Password requirements.
- Account activation.
- User enumeration.
- Registration abuse controls.

### 5.2 Login

Assess:

- Authentication enforcement.
- Username and email enumeration.
- Password policy.
- Rate limiting.
- Account lockout behaviour.
- MFA enforcement.
- Error message consistency.
- Authentication workflow logic.

### 5.3 Password recovery

Assess:

- Recovery token generation.
- Token expiry.
- Token reuse.
- Account enumeration.
- Recovery request throttling.
- Identity verification.
- Password reset session invalidation.

### 5.4 Multi-factor authentication

Assess:

- MFA enrolment.
- MFA removal.
- Recovery mechanisms.
- Backup codes.
- Session behaviour after MFA changes.
- MFA enforcement across sensitive workflows.
- Alternate authentication paths.

### 5.5 Single Sign-On

Where applicable, review:

- OAuth 2.0.
- OpenID Connect.
- SAML.
- Identity provider configuration.
- Redirect URI validation.
- State and nonce handling.
- Account linking.
- Token audience and issuer validation.

**Related reference:** `authentication.md`

---

## 6. Session Management

Session management testing assesses how authenticated sessions are created, maintained and invalidated.

### 6.1 Session creation

Review:

- Session identifiers.
- Cookie attributes.
- Token generation.
- Session fixation protections.
- Session rotation after authentication.

### 6.2 Session transport and storage

Review:

- HTTPS enforcement.
- `Secure` cookie attribute.
- `HttpOnly` cookie attribute.
- `SameSite` configuration.
- Token exposure in browser storage.
- Session leakage through URLs or logs.

### 6.3 Session lifecycle

Assess:

- Idle timeout.
- Absolute session lifetime.
- Logout invalidation.
- Password change behaviour.
- Account disablement.
- Concurrent sessions.
- Privilege changes.
- Session renewal.

### 6.4 Session integrity

Check whether sessions remain valid after security-relevant changes.

For example, an administrator disabling an account should result in the expected loss of access.

---

## 7. Authorisation Testing

Authorisation is one of the highest-value areas of web application security testing.

A user should only be able to access the resources and operations permitted by the application's security model.

### 7.1 Horizontal privilege escalation

Assess whether one user can access another user's resources.

Examples:

- Profile information.
- Documents.
- Orders.
- Support tickets.
- Uploaded files.
- Account settings.

### 7.2 Vertical privilege escalation

Assess whether a lower-privileged user can perform operations intended for a higher-privileged role.

Examples:

- Administrative functions.
- User management.
- Permission changes.
- Billing administration.
- Security configuration.

### 7.3 Object-level authorisation

For every resource identifier, assess whether the backend verifies ownership and permissions.

Consider:

- Direct object references.
- Nested resources.
- Resource relationships.
- Export endpoints.
- Download endpoints.
- Bulk operations.

### 7.4 Function-level authorisation

Review whether privileged operations are protected independently of frontend visibility.

### 7.5 Multi-tenant isolation

For multi-tenant applications, assess whether users can cross tenant boundaries.

Review:

- Tenant identifiers.
- Organisation identifiers.
- Shared resources.
- Administrative interfaces.
- Background processing.
- Export and reporting functionality.

### 7.6 Authorisation matrix

Maintain an expected permission matrix.

| Function | Anonymous | User | Manager | Admin |
|---|---:|---:|---:|---:|
| View public content | Yes | Yes | Yes | Yes |
| View own profile | No | Yes | Yes | Yes |
| View another user's profile | No | No | Limited | Yes |
| Manage users | No | No | Limited | Yes |
| Change system settings | No | No | No | Yes |

Adapt the matrix to the application's actual requirements.

**Related reference:** `access-control.md`

---

## 8. Input Validation and Injection

Assess how user-controlled data is parsed, validated, stored and used.

### 8.1 SQL injection

Review input that may influence database queries.

Potential locations:

- Search fields.
- Filters.
- Sorting parameters.
- Login forms.
- API parameters.
- Reporting functionality.

Consider:

- Error-based behaviour.
- Boolean-based behaviour.
- Time-based behaviour.
- UNION-based behaviour.
- Second-order injection.

Use non-destructive validation and avoid accessing unrelated records.

**Related reference:** `sql-injection.md`

### 8.2 Cross-site scripting

Assess:

- Reflected XSS.
- Stored XSS.
- DOM-based XSS.
- HTML injection.
- Attribute injection.
- JavaScript context handling.
- Output encoding.
- Content Security Policy.

**Related reference:** `xss.md`

### 8.3 Server-side template injection

Review functionality that dynamically renders:

- User-controlled templates.
- Email templates.
- Document templates.
- Custom reports.
- Notification content.

Determine whether untrusted input is interpreted as template syntax.

### 8.4 Command injection

Review application functionality that invokes operating system processes.

Potential areas include:

- File conversion.
- Image processing.
- Diagnostics.
- Import/export operations.
- Administrative utilities.

Avoid executing destructive commands or accessing sensitive host resources.

### 8.5 XML external entity processing

Where XML is accepted, review parser configuration and external entity handling.

Consider:

- External entity resolution.
- External DTD processing.
- Local file access risks.
- Server-side request risks.
- Parser resource consumption.

### 8.6 Path traversal

Review user-controlled file paths, filenames and resource references.

### 8.7 Server-side request forgery

Assess URL-consuming functionality and destination validation.

**Related references:**

- `sql-injection.md`
- `xss.md`
- `ssrf.md`

---

## 9. Client-Side Security

Client-side security testing assesses weaknesses in browser-executed code and the interaction between the browser and backend.

### 9.1 DOM security

Review:

- Untrusted data sources.
- Dangerous DOM sinks.
- HTML insertion.
- Dynamic script execution.
- Client-side templating.
- URL handling.

### 9.2 Cross-origin resource sharing

Assess whether CORS policies expose sensitive responses to unintended origins.

Review:

- Allowed origins.
- Credential support.
- Wildcard policies.
- Origin reflection.
- Preflight behaviour.
- Header restrictions.

### 9.3 Content Security Policy

Review:

- Script source restrictions.
- Inline script handling.
- Unsafe directives.
- Trusted script origins.
- Reporting configuration.
- Policy consistency.

### 9.4 Clickjacking

Review framing restrictions and whether sensitive workflows can be embedded in unintended contexts.

### 9.5 Client-side storage

Inspect:

- Local storage.
- Session storage.
- IndexedDB.
- Cookies.
- Cached application data.

Look for sensitive information that is unnecessarily exposed to client-side scripts or retained beyond its intended lifetime.

### 9.6 Open redirects

Assess whether user-controlled redirect destinations can send users to untrusted locations.

---

## 10. API Security Assessment

API testing should be treated as a core part of modern web application assessment.

### 10.1 Endpoint inventory

Identify:

- REST endpoints.
- GraphQL endpoints.
- WebSocket interfaces.
- API versions.
- Internal-facing routes exposed through the application.
- Authentication mechanisms.

### 10.2 Authentication

Review token validation, expiry, revocation and identity binding.

### 10.3 Authorisation

Prioritise:

- BOLA.
- BFLA.
- Property-level authorisation.
- Tenant isolation.
- Nested resource access.

### 10.4 Input and schema validation

Review:

- Unexpected properties.
- Type confusion.
- Missing required fields.
- Excessive request sizes.
- Nested JSON structures.
- Parameter pollution.
- Schema enforcement.

### 10.5 Rate limiting

Assess protections for:

- Login.
- Password recovery.
- Expensive searches.
- Account creation.
- Sensitive business operations.
- Bulk endpoints.

### 10.6 API inventory management

Identify undocumented, deprecated and older API versions.

**Related references:**

- `api-security.md`
- `jwt-security.md`

---

## 11. Business Logic Testing

Business logic vulnerabilities arise when an application correctly processes technically valid requests but fails to enforce its intended business rules.

These issues frequently require manual investigation.

### 11.1 Workflow manipulation

Assess whether workflows can be completed out of sequence.

Examples:

- Skipping required approval.
- Accessing later workflow stages prematurely.
- Reusing completed transactions.
- Modifying records after finalisation.

### 11.2 Trust boundary violations

Identify where the application trusts:

- Client-supplied prices.
- User-controlled roles.
- Organisation identifiers.
- Account status.
- Transaction state.
- Approval status.

Sensitive decisions should be made and validated server-side.

### 11.3 Race conditions

Assess whether concurrent requests can produce inconsistent application state.

Potential areas:

- Coupon redemption.
- Account balance changes.
- Inventory reservations.
- One-time actions.
- Transaction processing.

Use controlled test data and low-impact concurrency testing.

### 11.4 State manipulation

Review whether application state can be changed without satisfying the required business conditions.

### 11.5 Abuse cases

Think beyond individual vulnerabilities.

Ask:

- Can a user repeat an operation beyond its intended limit?
- Can a workflow be manipulated to obtain an unintended benefit?
- Can multiple legitimate actions combine into an unintended result?
- Can a user influence another user's transaction?
- Can an operation be replayed?

**Recommended approach:** Model the intended workflow, identify security-relevant state transitions, then test whether each transition is enforced server-side.

---

## 12. Server-Side Vulnerabilities

Assess the server-side processing and integration layer.

### 12.1 File upload

Review:

- Extension validation.
- MIME type validation.
- File signatures.
- Storage location.
- Access controls.
- File processing.
- Metadata exposure.
- Archive extraction.

**Related reference:** `file-upload.md`

### 12.2 SSRF

Review server-side URL retrieval and outbound request restrictions.

### 12.3 Deserialisation

Identify components that deserialize untrusted data.

Review:

- Accepted formats.
- Type restrictions.
- Parser configuration.
- Object construction behaviour.
- Dependency versions.

### 12.4 Server-side request handling

Review:

- Redirect behaviour.
- Proxy handling.
- Header forwarding.
- Request parsing.
- URL normalisation.
- Outbound network restrictions.

### 12.5 Cache security

Review whether shared caching introduces data exposure or response manipulation.

Consider:

- Cache key construction.
- User-specific responses.
- Authentication handling.
- Cache-control directives.
- Host and forwarding headers.

---

## 13. Configuration and Infrastructure

### 13.1 TLS

Review:

- HTTPS enforcement.
- Certificate validity.
- Protocol versions.
- Cipher configuration.
- HTTP-to-HTTPS redirects.
- Mixed content.

### 13.2 Security headers

Review:

| Header | Purpose |
|---|---|
| Content-Security-Policy | Restrict resource loading |
| Strict-Transport-Security | Enforce HTTPS |
| X-Content-Type-Options | Reduce MIME sniffing |
| Referrer-Policy | Control referrer information |
| Permissions-Policy | Restrict browser capabilities |
| Cache-Control | Control caching behaviour |

Header presence alone does not establish effective protection. Assess whether the values are appropriate.

### 13.3 CORS

Review whether cross-origin access is restricted to intended origins.

### 13.4 Debugging and information disclosure

Identify:

- Debug interfaces.
- Verbose error responses.
- Exposed source maps.
- Backup files.
- Environment information.
- Public configuration.
- Unintended documentation.

### 13.5 Third-party dependencies

Review known vulnerable dependencies where version evidence is available.

Distinguish confirmed vulnerable versions from speculative fingerprinting.

### 13.6 Infrastructure boundaries

Assess whether the application exposes unintended access to:

- Internal services.
- Administrative interfaces.
- Cloud resources.
- Storage services.
- Supporting APIs.

Remain within authorised network boundaries.

---

## 14. Advanced Testing Areas

These areas may require specialist knowledge or explicit additional scope.

### 14.1 HTTP request smuggling

Assess inconsistencies in HTTP request parsing between front-end and back-end components.

Consider:

- HTTP/1.1 request framing.
- HTTP/2 translation.
- Reverse proxy behaviour.
- Content-Length handling.
- Transfer-Encoding handling.
- Connection reuse.

Testing can affect other users when shared infrastructure is involved. Use controlled environments or explicit low-impact testing approval.

### 14.2 Web cache poisoning

Assess whether untrusted request inputs influence cached responses.

Review:

- Cache keys.
- Unkeyed inputs.
- Host handling.
- Forwarding headers.
- Cache variation.
- Shared response behaviour.

### 14.3 WebSocket security

Review:

- Handshake authentication.
- Origin validation.
- Message-level authorisation.
- Session expiry.
- Message validation.
- Rate limiting.

### 14.4 Prototype pollution

Assess JavaScript applications and server-side JavaScript components for unsafe handling of object properties and dynamic object merging.

### 14.5 HTTP parameter pollution

Review how applications interpret repeated parameters across:

- Query strings.
- Form data.
- Headers.
- JSON structures.

Look for inconsistent parsing between proxies, frameworks and application components.

### 14.6 Third-party integration security

Review trust relationships between the application and external services.

Consider:

- Webhooks.
- OAuth integrations.
- Payment providers.
- Identity providers.
- File storage services.
- Analytics platforms.

---

## 15. Evidence Collection

A finding should be reproducible, understandable and supported by sufficient evidence.

### 15.1 Evidence types

| Evidence | Purpose |
|---|---|
| HTTP request | Demonstrates test input |
| HTTP response | Demonstrates application behaviour |
| Screenshot | Shows relevant application state |
| Callback record | Demonstrates out-of-band interaction |
| Test account comparison | Demonstrates permission boundaries |
| Timestamp | Establishes event sequence |
| Application log | Supports server-side behaviour |

### 15.2 Evidence standards

Evidence should be:

- Relevant.
- Reproducible.
- Minimal.
- Sanitised.
- Clearly labelled.
- Associated with the affected endpoint.
- Stored securely.

### 15.3 Sensitive information

Do not include:

- Live passwords.
- Session tokens.
- API keys.
- Private signing keys.
- Unnecessary personal information.
- Unrelated customer records.

Where sensitive evidence is required, use an approved secure transfer method.

### 15.4 Reproduction records

Maintain a record for each potential finding:

```text
Finding ID:
Title:
Affected asset:
Endpoint:
HTTP method:
Authentication context:
Prerequisites:
Reproduction steps:
Expected behaviour:
Actual behaviour:
Evidence references:
Impact:
Remediation:
```

---

## 16. Finding Validation and Risk Assessment

### 16.1 Validate before reporting

Before raising a finding:

1. Reproduce the behaviour.
2. Confirm the affected asset is in scope.
3. Establish the expected security control.
4. Identify the actual control failure.
5. Determine realistic impact.
6. Rule out false positives.
7. Capture sufficient evidence.

### 16.2 Distinguish vulnerability from observation

Not every unexpected response is a vulnerability.

Examples:

| Observation | Additional validation |
|---|---|
| Verbose error | Does it expose sensitive information? |
| Missing security header | Does it create a meaningful security weakness? |
| Public API documentation | Does it expose sensitive functionality or information? |
| Predictable identifier | Is authorisation actually missing? |
| Old software version | Is the component vulnerable and reachable? |
| Unexpected HTTP method | Does it enable an unauthorised action? |

### 16.3 Severity assessment

Consider:

- Exploitability.
- Required privileges.
- User interaction.
- Confidentiality impact.
- Integrity impact.
- Availability impact.
- Scope of affected users.
- Business consequences.

Use the client's requested severity model where specified.

Otherwise, CVSS can provide a consistent technical severity framework.

### 16.4 Finding quality

A strong finding explains:

- What is vulnerable.
- Where it is vulnerable.
- How it was validated.
- What an attacker could achieve.
- Which security boundary failed.
- How to remediate it.

Avoid overstating impact beyond demonstrated evidence.

---

## 17. Reporting

A professional report should communicate technical findings in a way that supports remediation.

### 17.1 Executive summary

Include:

- Assessment objective.
- Scope.
- Overall security posture.
- Key risks.
- Significant business impacts.
- Priority remediation areas.

Avoid unnecessary technical detail in this section.

### 17.2 Technical findings

Use a consistent structure.

```text
Finding ID:
Title:
Severity:
Affected asset:
Affected endpoint:

Description:

Technical impact:

Business impact:

Prerequisites:

Steps to reproduce:

Evidence:

Remediation:

References:
```

### 17.3 Risk prioritisation

| Severity | General interpretation |
|---|---|
| Critical | Severe compromise with major impact |
| High | Significant compromise or sensitive access |
| Medium | Meaningful security weakness with limitations |
| Low | Limited impact or constrained exposure |
| Informational | Observation or improvement opportunity |

Severity should be based on evidence and the agreed assessment methodology.

### 17.4 Remediation recommendations

Recommendations should be:

- Specific.
- Actionable.
- Technically accurate.
- Prioritised.
- Appropriate to the application's architecture.

Where possible, identify the underlying control failure rather than recommending a superficial workaround.

---

## 18. Post-Engagement

### 18.1 Retesting

For remediation validation:

- Revisit the original reproduction steps.
- Confirm the vulnerability is no longer reproducible.
- Check for alternate affected endpoints.
- Verify that the underlying control has been corrected.
- Record remaining limitations.

### 18.2 Evidence handling

Follow the engagement's retention and deletion requirements.

Ensure:

- Temporary test accounts are handled appropriately.
- Test data is removed where agreed.
- Sensitive evidence is securely transferred.
- Local copies are deleted according to the agreed process.
- Engagement access is revoked where appropriate.

### 18.3 Lessons learned

Document:

- Common application weaknesses.
- Repeated control failures.
- Testing coverage gaps.
- Tooling limitations.
- Recommendations for future assessments.

---

## 19. Assessment Checklist

### Preparation

- [ ] Confirm written authorisation.
- [ ] Review scope.
- [ ] Review Rules of Engagement.
- [ ] Confirm testing windows.
- [ ] Confirm emergency contacts.
- [ ] Obtain appropriate test accounts.
- [ ] Identify excluded systems.

### Reconnaissance

- [ ] Map in-scope assets.
- [ ] Identify application technologies.
- [ ] Enumerate application routes.
- [ ] Identify API endpoints.
- [ ] Review JavaScript.
- [ ] Identify authentication flows.
- [ ] Identify third-party integrations.

### Authentication and sessions

- [ ] Test registration.
- [ ] Test login.
- [ ] Test password recovery.
- [ ] Review MFA.
- [ ] Review SSO.
- [ ] Assess session creation.
- [ ] Assess session expiry.
- [ ] Assess logout and revocation.

### Authorisation

- [ ] Test horizontal access controls.
- [ ] Test vertical access controls.
- [ ] Review object-level permissions.
- [ ] Review function-level permissions.
- [ ] Test tenant isolation.
- [ ] Review nested resource access.

### Input handling

- [ ] Assess SQL injection.
- [ ] Assess XSS.
- [ ] Assess SSRF.
- [ ] Assess file upload.
- [ ] Assess path traversal.
- [ ] Review XML processing.
- [ ] Review template processing.
- [ ] Review command execution boundaries.

### Client-side security

- [ ] Review DOM security.
- [ ] Review CORS.
- [ ] Review CSP.
- [ ] Review clickjacking protections.
- [ ] Review client-side storage.
- [ ] Review open redirects.

### API security

- [ ] Inventory API versions.
- [ ] Assess authentication.
- [ ] Assess object-level authorisation.
- [ ] Assess function-level authorisation.
- [ ] Review property-level controls.
- [ ] Assess rate limiting.
- [ ] Review GraphQL where applicable.

### Business logic

- [ ] Map important workflows.
- [ ] Review state transitions.
- [ ] Assess transaction handling.
- [ ] Review replay protections.
- [ ] Assess race conditions.
- [ ] Review abuse cases.

### Infrastructure and configuration

- [ ] Review TLS.
- [ ] Review security headers.
- [ ] Review caching.
- [ ] Review error handling.
- [ ] Review dependency exposure.
- [ ] Review debug interfaces.
- [ ] Assess relevant trust boundaries.

### Reporting and closure

- [ ] Validate all findings.
- [ ] Remove sensitive information from evidence.
- [ ] Assign justified severity.
- [ ] Document reproducible steps.
- [ ] Provide actionable remediation.
- [ ] Complete retesting where required.
- [ ] Close out engagement access and evidence.

---

## 20. Reference Frameworks

### OWASP Web Security Testing Guide (WSTG)

A comprehensive framework for web application penetration testing.

https://owasp.org/www-project-web-security-testing-guide/

### OWASP Application Security Verification Standard (ASVS)

A structured set of application security verification requirements.

https://owasp.org/www-project-application-security-verification-standard/

### OWASP API Security Top 10

A reference for common API security risks.

https://owasp.org/API-Security/

### Penetration Testing Execution Standard (PTES)

A framework covering the stages of a penetration test.

http://www.pentest-standard.org/

### NIST SP 800-115

Technical guidance for information security testing and assessment.

https://csrc.nist.gov/pubs/sp/800/115/final

### MITRE CWE

A catalogue of common software weaknesses.

https://cwe.mitre.org/

### FIRST CVSS

A standardised framework for assessing vulnerability severity.

https://www.first.org/cvss/

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
