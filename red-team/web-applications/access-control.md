# Access Control Security Testing

A practical guide to identifying broken authorisation, insecure direct object references (IDOR), privilege escalation and access control weaknesses in web applications and APIs.

Authentication establishes who a user is. Authorisation determines what that user is allowed to do.

A secure application must enforce authorisation on the server side, consistently across every relevant endpoint and operation.

> **Scope reminder:** Perform testing only against authorised applications and accounts. Use designated test accounts and data wherever possible. Do not access, modify or disclose other users' information.

---

## Contents

- [1. Access Control Fundamentals](#1-access-control-fundamentals)
- [2. Types of Access Control](#2-types-of-access-control)
- [3. Horizontal Privilege Escalation](#3-horizontal-privilege-escalation)
- [4. Vertical Privilege Escalation](#4-vertical-privilege-escalation)
- [5. IDOR and BOLA](#5-idor-and-bola)
- [6. Forced Browsing](#6-forced-browsing)
- [7. Parameter and Request Manipulation](#7-parameter-and-request-manipulation)
- [8. Multi-Tenant Authorisation](#8-multi-tenant-authorisation)
- [9. Common Access Control Vulnerabilities](#9-common-access-control-vulnerabilities)
- [10. Testing Tools](#10-testing-tools)
- [11. Testing Methodology](#11-testing-methodology)
- [12. Testing Checklist](#12-testing-checklist)
- [13. Further Reading](#13-further-reading)

---

## 1. Access Control Fundamentals

Access control determines whether a user, process or system can perform a particular action on a resource.

Examples include:

- Viewing a user profile
- Downloading a document
- Editing an account
- Deleting a record
- Accessing administrative functionality
- Managing organisation settings
- Viewing financial information

A common access control weakness occurs when an application relies on the frontend to restrict functionality instead of enforcing permissions on the backend.

### Authentication vs authorisation

| Concept | Question | Example |
|---|---|---|
| Authentication | Who are you? | Valid login |
| Authorisation | What can you access? | Permission to view a record |
| Session management | How is your authenticated state maintained? | Session cookie |

### Core security principle

Every sensitive operation should verify that the authenticated user is authorised to perform that specific action against that specific resource.

Do not assume that hiding a button, changing a URL or removing a menu item provides security.

---

## 2. Types of Access Control

### Discretionary Access Control (DAC)

Resource owners can determine who has access to their resources.

### Mandatory Access Control (MAC)

Access is determined by centrally enforced security policies and classifications.

### Role-Based Access Control (RBAC)

Permissions are assigned to roles, and users inherit permissions through their assigned roles.

Example:

| Role | Permissions |
|---|---|
| Guest | View public content |
| User | View and edit own profile |
| Manager | Manage team resources |
| Administrator | Manage application settings |

### Attribute-Based Access Control (ABAC)

Access decisions are based on attributes such as:

- User identity
- Department
- Resource ownership
- Location
- Resource classification
- Time or environmental conditions

### Testing considerations

- Are permissions enforced server-side?
- Are roles checked on every sensitive endpoint?
- Can users modify their own role?
- Are permissions consistent across API and frontend functionality?
- Are permissions inherited correctly?
- Are access decisions based on trusted server-side attributes?

---

## 3. Horizontal Privilege Escalation

Horizontal privilege escalation occurs when a user accesses another user's resources or functionality without having the appropriate permission.

Example:

Two ordinary users have separate accounts.

```text
User A: user_id=1001
User B: user_id=1002
```

User A should only be able to access their own profile.

A vulnerable application may allow access to another user's profile by changing an identifier.

### Example request

```http
GET /api/users/1001 HTTP/1.1
Host: example.com
Cookie: session=USER_A_SESSION
```

### Testing approach

Using two authorised test accounts:

1. Authenticate as User A.
2. Access a resource belonging to User A.
3. Record the request and response.
4. Authenticate as User B and identify an equivalent resource.
5. Return to User A's session.
6. Test whether User A can access User B's test resource.
7. Verify whether the server enforces ownership.

### Potential impact

- Exposure of personal information
- Unauthorised document access
- Disclosure of financial records
- Modification of another user's data
- Account-related information exposure

---

## 4. Vertical Privilege Escalation

Vertical privilege escalation occurs when a user gains access to functionality intended for a higher-privileged role.

Example:

An ordinary user attempts to access administrator functionality.

```text
User role: Standard
Target functionality: Administrator
```

### Common attack surfaces

- Administrative endpoints
- User management functionality
- Role management
- Organisation settings
- Billing and subscription management
- Privileged API operations
- Backend administrative actions

### Example request

```http
GET /admin/users HTTP/1.1
Host: example.com
Cookie: session=STANDARD_USER_SESSION
```

The important question is whether the server checks the user's permissions, not whether the frontend displays an administrator menu.

### Testing approach

Using approved accounts with different permission levels:

1. Identify functionality available to administrators.
2. Identify the corresponding backend requests.
3. Authenticate as a lower-privileged test account.
4. Attempt to access the same functionality.
5. Compare the server's responses.
6. Verify whether restricted operations are rejected server-side.

### Common weaknesses

- Missing role checks
- Incorrect role inheritance
- Client-controlled role values
- Unprotected administrative endpoints
- Inconsistent API authorisation
- Privileged actions exposed through alternate routes

---

## 5. IDOR and BOLA

### Insecure Direct Object Reference (IDOR)

IDOR occurs when an application exposes a direct reference to an object but fails to properly verify whether the requesting user is authorised to access it.

Examples of object identifiers:

- User IDs
- Invoice numbers
- Document IDs
- Order references
- Account numbers
- File identifiers
- Project IDs

### Broken Object Level Authorisation (BOLA)

BOLA is the API security terminology for an authorisation failure involving access to objects.

It is closely related to IDOR.

### Example

A user requests their own invoice:

```http
GET /api/invoices/INV-1001 HTTP/1.1
Host: example.com
Cookie: session=USER_A_SESSION
```

The application uses the invoice identifier to retrieve the record.

If the backend does not verify ownership, a user may be able to access an invoice belonging to another account.

### Common identifier formats

```text
/api/users/1001
/api/orders/ORD-1001
/api/invoices/INV-1001
/documents/550e8400-e29b-41d4-a716-446655440000
/download?id=12345
```

Identifiers may be:

- Sequential integers
- UUIDs
- Random strings
- Encoded values
- Composite identifiers

**Important:** UUIDs and unpredictable identifiers do not replace server-side authorisation checks.

### Testing methodology

Use two controlled test accounts and resources created specifically for the assessment.

1. Identify a resource owned by Account A.
2. Identify an equivalent resource owned by Account B.
3. Capture Account A's request.
4. Test access to Account B's test resource using Account A's session.
5. Check whether the server denies access.
6. Where permitted, assess whether the same weakness affects read, update and delete operations.
7. Document the impact without accessing unrelated customer data.

### Common IDOR locations

- Profile pages
- Document downloads
- Invoices
- Orders
- Support tickets
- Messaging systems
- User preferences
- Organisation resources
- Export functionality

### Remediation

- Enforce object-level authorisation on the server.
- Verify ownership or explicit access permissions.
- Apply consistent checks across all HTTP methods.
- Avoid relying on obscure identifiers.
- Use deny-by-default access policies.

---

## 6. Forced Browsing

Forced browsing involves attempting to access application resources directly rather than navigating through the normal user interface.

This can reveal endpoints that are hidden from ordinary users but not properly protected.

### Common locations

```text
/admin
/admin/users
/dashboard
/settings
/internal
/reports
/api/admin
/management
```

These are examples of paths to investigate within an authorised application.

### Testing approach

1. Identify restricted functionality through an authorised higher-privileged account.
2. Record the relevant routes.
3. Authenticate using a lower-privileged test account.
4. Request the same routes directly.
5. Verify that access is denied by the server.

### Important distinction

A hidden endpoint is not necessarily a vulnerability.

The vulnerability exists when a user can access or perform something they are not authorised to access or perform.

---

## 7. Parameter and Request Manipulation

Applications frequently use request parameters to identify users, resources, roles and actions.

### Common locations

- URL path parameters
- Query string parameters
- Form fields
- JSON request bodies
- HTTP headers
- Cookies
- GraphQL variables

### Example JSON request

```http
POST /api/profile/update HTTP/1.1
Host: example.com
Content-Type: application/json
Cookie: session=USER_A_SESSION

{
  "user_id": 1001,
  "display_name": "Example User"
}
```

### Testing considerations

Using test accounts and non-sensitive data:

- Does the server trust a client-supplied user ID?
- Can a user modify another user's resource?
- Are role and permission fields protected?
- Are ownership fields validated?
- Does the server derive identity from the authenticated session?
- Are all relevant properties subject to authorisation checks?

### Mass assignment

Mass assignment occurs when an application automatically binds client-supplied properties to internal objects without sufficient validation.

Potentially sensitive properties include:

```json
{
  "role": "administrator",
  "is_admin": true,
  "account_status": "active"
}
```

These are illustrative examples of fields to review, not a recommendation to modify production accounts.

### Remediation

- Allowlist writable properties.
- Validate sensitive fields server-side.
- Derive identity and permissions from trusted server-side context.
- Prevent users from modifying protected attributes.

---

## 8. Multi-Tenant Authorisation

Multi-tenant applications host multiple customers, organisations or teams within a shared platform.

A serious authorisation weakness can expose one tenant's information to another.

### Example

```text
Organisation A
  - User A1
  - User A2
  - Documents A1

Organisation B
  - User B1
  - User B2
  - Documents B1
```

Organisation A should not be able to access Organisation B's private resources without explicit permission.

### Testing areas

- Tenant ID validation
- Organisation membership
- Cross-tenant document access
- Shared resource permissions
- API tenant context
- Administrative boundaries
- Export and reporting functionality
- Background jobs and integrations

### Testing approach

Use separate test tenants provided for the assessment.

1. Identify resources belonging to each tenant.
2. Authenticate as a user in Tenant A.
3. Access Tenant A's resources.
4. Test whether Tenant A can access designated test resources in Tenant B.
5. Verify that the application enforces tenant boundaries server-side.
6. Record any cross-tenant access using only approved test data.

### Potential impact

- Cross-customer data exposure
- Unauthorised modification of tenant resources
- Confidential business information disclosure
- Regulatory and privacy consequences

---

## 9. Common Access Control Vulnerabilities

| Vulnerability | Description | Potential impact |
|---|---|---|
| IDOR | Direct object reference without ownership validation | Unauthorised data access |
| BOLA | API object-level authorisation failure | Cross-user data exposure |
| BFLA | API function-level authorisation failure | Unauthorised operations |
| Horizontal escalation | Access to another user's resources | Data exposure |
| Vertical escalation | Access to higher-privileged functionality | Administrative compromise |
| Forced browsing | Direct access to unprotected routes | Restricted functionality exposure |
| Mass assignment | Unsafe binding of user-controlled properties | Privilege or data modification |
| Tenant isolation failure | Missing tenant boundary enforcement | Cross-customer data exposure |
| Client-side enforcement | Permissions enforced only in the browser | Bypass of restrictions |

---

## 10. Testing Tools

| Tool | Purpose | Resource |
|---|---|---|
| Burp Suite | Intercept and manipulate HTTP requests | [Website](https://portswigger.net/burp) |
| AuthMatrix | Compare access across user roles | [GitHub](https://github.com/SecurityInnovation/AuthMatrix) |
| Autorize | Automated authorisation testing | [GitHub](https://github.com/Quitten/Autorize) |
| OWASP ZAP | Web application testing | [Website](https://www.zaproxy.org/) |
| Postman | API request testing | [Website](https://www.postman.com/) |
| Insomnia | API testing | [Website](https://insomnia.rest/) |
| Caido | Web security testing proxy | [Website](https://caido.io/) |

### Burp Suite extensions worth knowing

- Autorize
- AuthMatrix
- Logger++
- Param Miner
- JSON Web Tokens

Always verify automated results manually. Tools can identify suspicious behaviour but cannot reliably establish business impact on their own.

---

## 11. Testing Methodology

A reliable access control assessment should compare what different users can do with the same resources and operations.

### Step 1 — Establish test accounts

Ideally, obtain:

| Account | Role | Purpose |
|---|---|---|
| Account A | Standard user | Baseline |
| Account B | Standard user | Cross-user testing |
| Account C | Administrator | Privileged functionality comparison |

Use accounts supplied or approved by the organisation.

### Step 2 — Map application functionality

Document:

- Pages and endpoints
- Available actions
- User roles
- Resource ownership
- Organisation boundaries
- Sensitive operations

### Step 3 — Capture requests

Use Burp Suite or another intercepting proxy to capture representative requests for each role.

### Step 4 — Compare permissions

Evaluate whether each account can:

- View the resource
- Create a resource
- Modify a resource
- Delete a resource
- Perform administrative actions

### Step 5 — Validate server-side enforcement

Confirm that the backend rejects unauthorised requests, even when they are sent directly rather than through the frontend.

### Step 6 — Document findings

Record:

- Affected endpoint
- Required account role
- Resource ownership
- Expected behaviour
- Actual behaviour
- Supporting evidence
- Security impact
- Recommended remediation

---

## 12. Testing Checklist

### General authorisation
- [ ] Identify user roles and permissions
- [ ] Identify sensitive resources
- [ ] Check server-side authorisation
- [ ] Review direct endpoint access
- [ ] Compare permissions across roles

### Horizontal access
- [ ] Test ownership boundaries using controlled accounts
- [ ] Check profile access
- [ ] Check document access
- [ ] Check order and invoice access
- [ ] Check update and delete permissions

### Vertical access
- [ ] Identify privileged endpoints
- [ ] Test lower-privileged access to restricted routes
- [ ] Review administrative API functionality
- [ ] Check role management
- [ ] Review sensitive administrative actions

### API authorisation
- [ ] Review object-level permissions
- [ ] Review function-level permissions
- [ ] Check tenant context
- [ ] Review writable object properties
- [ ] Check authorisation across HTTP methods

### Multi-tenancy
- [ ] Identify tenant boundaries
- [ ] Test approved cross-tenant scenarios
- [ ] Review shared resources
- [ ] Check reporting and export functionality

### Reporting
- [ ] Record affected endpoints
- [ ] Capture safe evidence
- [ ] Demonstrate impact using test data
- [ ] Assign an appropriate severity
- [ ] Recommend server-side remediation

---

## 13. Further Reading

- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [PortSwigger Access Control](https://portswigger.net/web-security/access-control)
- [PortSwigger IDOR](https://portswigger.net/web-security/access-control/idor)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP Testing for IDOR](https://owasp.org/www-project-web-security-testing-guide/)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
