# JSON Web Token (JWT) Security

## Overview

JSON Web Tokens (JWTs) are a common method of representing claims between systems. They are frequently used for authentication, authorisation and API access.

JWTs are often found in web application session workflows and API requests.

Although JWTs provide a standard token format, insecure implementation and validation can introduce serious vulnerabilities.

This guide covers JWT structure, reconnaissance, testing methodology, common weaknesses, useful tools and remediation.

> **Authorisation:** Only test tokens and applications within an approved engagement scope. Use accounts and tokens you are authorised to access. Never publish live tokens, signing secrets or private keys.

---

## Table of Contents

1. [JWT Fundamentals](#1-jwt-fundamentals)
2. [JWT Structure](#2-jwt-structure)
3. [JWT Claims](#3-jwt-claims)
4. [JWT Reconnaissance](#4-jwt-reconnaissance)
5. [Testing Methodology](#5-testing-methodology)
6. [Common JWT Vulnerabilities](#6-common-jwt-vulnerabilities)
7. [JWT Algorithms](#7-jwt-algorithms)
8. [Tools](#8-tools)
9. [Remediation](#9-remediation)
10. [Reporting](#10-reporting)
11. [Testing Checklist](#11-testing-checklist)
12. [References](#12-references)

---

## 1. JWT Fundamentals

A JSON Web Token is a compact, URL-safe format for transmitting claims.

JWTs are commonly used to:

- Authenticate users.
- Represent user identity.
- Carry authorisation claims.
- Authorise API requests.
- Support communication between services.

A typical application may issue a JWT after successful login and require it for subsequent API requests.

Example:

```http
GET /api/v1/profile HTTP/1.1
Host: example.com
Authorization: Bearer <JWT>
```

### Important security properties

A JWT is not automatically encrypted.

A typical signed JWT provides integrity and authenticity: the recipient can verify that the token was signed by a trusted party and has not been modified.

However, its contents are generally readable by anyone who obtains the token.

Never place passwords, API secrets or unnecessary sensitive personal information inside an ordinary signed JWT.

---

## 2. JWT Structure

A standard signed JWT consists of three Base64URL-encoded sections separated by periods.

```text
HEADER.PAYLOAD.SIGNATURE
```

### 2.1 Header

The header describes the token and its signing algorithm.

Example:

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

Common header fields include:

| Field | Purpose |
|---|---|
| `alg` | Signing algorithm |
| `typ` | Token type |
| `kid` | Key identifier |
| `cty` | Content type |
| `jku` | JSON Web Key Set URL |
| `x5u` | X.509 certificate URL |

### 2.2 Payload

The payload contains claims.

Example:

```json
{
  "sub": "12345",
  "name": "Test User",
  "role": "user",
  "iat": 1795600000,
  "exp": 1795603600
}
```

These claims describe the subject, role and token lifetime.

The payload is encoded, not encrypted, unless a separate encryption mechanism is used.

### 2.3 Signature

The signature protects the integrity of the token.

For a typical HMAC-signed JWT, the signature is generated using the encoded header, encoded payload and a shared secret.

Conceptually:

```text
HMAC(
  secret,
  base64url(header) + "." + base64url(payload)
)
```

The exact signing procedure depends on the selected algorithm.

A recipient must validate the signature before trusting the claims.

---

## 3. JWT Claims

JWT claims are statements about a subject or token.

### Registered claims

| Claim | Purpose |
|---|---|
| `iss` | Issuer |
| `sub` | Subject |
| `aud` | Intended audience |
| `exp` | Expiration time |
| `nbf` | Not valid before |
| `iat` | Issued at |
| `jti` | Unique token identifier |

### Private claims

Applications can define their own claims.

Examples:

```json
{
  "role": "user",
  "department": "support",
  "tenant_id": "tenant-123",
  "permissions": ["profile:read"]
}
```

Private claims must be validated and interpreted according to the application's security model.

A role or permission claim should never be trusted merely because it appears in the payload.

### Time-based claims

JWT timestamps are generally represented as NumericDate values: seconds since the Unix epoch.

Important considerations:

- Expired tokens should be rejected.
- Tokens should not be accepted before their `nbf` time.
- Clock tolerance should be limited.
- Token lifetimes should match the sensitivity of the application.

---

## 4. JWT Reconnaissance

The first step is identifying where and how the application uses JWTs.

### 4.1 Locate tokens

Inspect:

- Login responses.
- Browser storage.
- HTTP request headers.
- API responses.
- Mobile application traffic.
- WebSocket authentication.
- Third-party integration requests.

Common locations include:

```text
Authorization: Bearer <TOKEN>
```

And cookie values:

```text
Set-Cookie: access_token=<TOKEN>
```

### 4.2 Identify the token format

JWTs commonly have three dot-separated sections.

Example placeholder:

```text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.
eyJzdWIiOiIxMjM0NSIsInJvbGUiOiJ1c2VyIn0
.
<signature>
```

The presence of three sections is a useful indicator, but the format alone does not prove that a token is valid or securely implemented.

### 4.3 Decode the token

JWT payloads can be decoded without knowing the signing secret.

Inspect:

- Algorithm.
- Key identifier.
- Issuer.
- Audience.
- Subject.
- Expiration.
- Roles and permissions.
- Custom claims.

Do not confuse decoding with signature verification.

### 4.4 Build a token inventory

| Token | Location | Algorithm | Expiry | Notes |
|---|---|---|---|---|
| Access token | Authorization header | HS256 | Short-lived | API authentication |
| Refresh token | Secure cookie | N/A | Longer-lived | Session renewal |
| Integration token | Request header | RS256 | Unknown | Service integration |

Record only sanitised token metadata. Never store live token values in a public report or repository.

---

## 5. Testing Methodology

### 5.1 Establish a baseline

Capture a valid token from an authorised test account.

Record:

- Token location.
- Header contents.
- Payload claims.
- Expiry.
- Issuer.
- Audience.
- Algorithm.
- Normal API behaviour.

### 5.2 Test token expiry

Check whether an expired token is rejected.

Review:

- Access token lifetime.
- Refresh token lifetime.
- Behaviour after logout.
- Behaviour after password changes.
- Behaviour after account disablement.

Use controlled test accounts and avoid invalidating sessions belonging to other users.

### 5.3 Test claim validation

Review whether the application validates:

- `iss`.
- `aud`.
- `sub`.
- `exp`.
- `nbf`.
- Required application-specific claims.

Claims should be validated against the expected application context.

### 5.4 Test role enforcement

Using approved accounts with different roles:

1. Capture a normal user token.
2. Identify an operation restricted to a higher role.
3. Attempt the operation using the normal account.
4. Confirm whether the backend correctly denies access.
5. Compare with the authorised role's expected behaviour.

Do not attempt to gain unauthorised privileges by altering production tokens.

### 5.5 Review token revocation

JWTs are often designed to be self-contained, which can make immediate revocation more difficult.

Assess whether:

- Logout invalidates relevant sessions.
- Refresh tokens can be revoked.
- Password changes affect active sessions.
- Disabled accounts lose access.
- High-risk operations require fresh authentication.

### 5.6 Review token storage

Check whether tokens are stored in:

- Cookies.
- Local storage.
- Session storage.
- Application memory.

Consider whether the storage mechanism exposes tokens to cross-site scripting or other client-side compromise.

Secure, HttpOnly and appropriately configured SameSite cookies can reduce some browser-based risks.

### 5.7 Review signing key management

Determine whether signing keys are:

- Properly generated.
- Sufficiently strong.
- Stored securely.
- Restricted to authorised services.
- Rotated appropriately.
- Separated between environments.

Never attempt to obtain production signing keys outside the explicitly authorised scope.

---

## 6. Common JWT Vulnerabilities

### 6.1 Algorithm confusion

JWT implementations must enforce an explicit algorithm policy.

A verifier that accepts unexpected algorithms or confuses symmetric and asymmetric key handling may incorrectly validate tokens.

**Assessment focus:**

- Is the expected algorithm explicitly configured?
- Are symmetric and asymmetric keys handled correctly?
- Does the verifier reject unexpected algorithms?
- Are different token types validated independently?

### 6.2 Weak HMAC signing secrets

HMAC algorithms such as HS256 use a shared secret.

If the secret is weak or predictable, the integrity of signed tokens may be compromised.

**Assessment focus:**

- Is the secret sufficiently random?
- Is it stored securely?
- Is it shared across unrelated applications?
- Is key rotation supported?

Do not perform aggressive secret guessing against production systems. Use approved test environments and explicit engagement permissions.

### 6.3 Missing signature validation

An application may decode a JWT and trust its claims without properly verifying its signature.

This defeats the token's integrity protection.

**Assessment focus:**

- Is signature verification mandatory?
- Are invalid signatures rejected?
- Are unsigned tokens rejected?
- Are claims trusted only after verification?

### 6.4 Weak claim validation

A valid signature does not automatically make a token appropriate for every application or operation.

Examples of missing checks include:

- Incorrect issuer accepted.
- Incorrect audience accepted.
- Expired tokens accepted.
- Required claims missing.
- Unexpected token types accepted.

### 6.5 Token lifetime issues

Long-lived access tokens increase the impact of token theft.

Review:

- Access token duration.
- Refresh token duration.
- Revocation behaviour.
- Session invalidation.
- Reauthentication requirements.

### 6.6 Insecure key selection

JWT headers may contain key-selection information such as `kid`.

Applications must resolve keys from trusted, controlled sources.

**Assessment focus:**

- Is key selection restricted?
- Are unknown key identifiers rejected?
- Is key material isolated from user-controlled input?
- Are remote key references restricted to trusted sources?

### 6.7 Sensitive information disclosure

JWT payloads are commonly readable.

Do not include:

- Passwords.
- API secrets.
- Private keys.
- Unnecessary personal information.
- Sensitive internal configuration.

### 6.8 Token leakage

Tokens may leak through:

- Browser storage.
- Application logs.
- URLs.
- Referrer headers.
- Analytics systems.
- Browser extensions.
- Third-party scripts.

Review token handling throughout the application lifecycle.

---

## 7. JWT Algorithms

JWT supports multiple signing and encryption approaches.

### Common signing algorithms

| Algorithm | Description |
|---|---|
| HS256 | HMAC using SHA-256 |
| HS384 | HMAC using SHA-384 |
| HS512 | HMAC using SHA-512 |
| RS256 | RSA with SHA-256 |
| RS384 | RSA with SHA-384 |
| RS512 | RSA with SHA-512 |
| ES256 | ECDSA using P-256 and SHA-256 |
| ES384 | ECDSA using P-384 and SHA-384 |
| EdDSA | Edwards-curve digital signatures |

### Symmetric signing

With symmetric signing, the same secret is used to sign and verify tokens.

Advantages:

- Relatively simple.
- Efficient.
- Suitable for systems with controlled shared-secret distribution.

Risks:

- Every verifier that holds the secret can also create valid tokens.
- Secret distribution and rotation require care.

### Asymmetric signing

With asymmetric signing:

- The issuer signs using a private key.
- Verifiers validate using the corresponding public key.

This can reduce the number of systems that need access to signing material.

### Encryption

JWT is also used with JSON Web Encryption (JWE).

Unlike an ordinary signed JWT, JWE provides encryption of the token contents.

Do not assume that a token is encrypted simply because it is a JWT.

---

## 8. Tools

| Tool | Purpose |
|---|---|
| Burp Suite | Intercept and inspect JWTs |
| JWT Editor | Burp extension for JWT inspection and testing |
| jwt.io | Decode and inspect JWT structure |
| CyberChef | Decode Base64URL and inspect token components |
| jwt-tool | JWT analysis and testing utility |
| Python | Build controlled JWT validation tests |
| OpenSSL | Inspect and work with cryptographic keys |
| Postman | Test authenticated API requests |

### Burp Suite

Useful functionality:

- Proxy: capture authentication traffic.
- Repeater: resend requests with controlled changes.
- Decoder: inspect encoded token components.
- JWT Editor: inspect and assess JWT handling.

### jwt.io

Website:

https://jwt.io/

Useful for:

- Decoding headers.
- Viewing payload claims.
- Understanding JWT structure.
- Inspecting signing algorithm metadata.

Do not paste production tokens into public websites. Use synthetic or sanitised tokens.

### jwt-tool

Repository:

https://github.com/ticarpi/jwt_tool

A command-line utility for JWT analysis and security testing.

Use it in a controlled lab or against explicitly authorised targets. Review the tool's documentation and engagement rules before running active tests.

---

## 9. Remediation

### 9.1 Enforce algorithm allowlists

Configure the verifier to accept only explicitly approved algorithms.

Never allow the token header alone to determine which algorithms the verifier trusts.

### 9.2 Validate all required claims

Validate:

- Issuer.
- Audience.
- Expiry.
- Not-before time.
- Subject.
- Required application claims.

Reject tokens with missing or invalid required claims.

### 9.3 Use strong signing keys

For symmetric algorithms, use cryptographically random secrets with sufficient entropy.

For asymmetric algorithms:

- Protect private keys.
- Distribute public keys securely.
- Restrict signing permissions.
- Rotate keys appropriately.

### 9.4 Implement key rotation

Maintain a controlled key lifecycle.

Consider:

- Key identifiers.
- Current and previous verification keys.
- Rotation schedules.
- Emergency key replacement.
- Revocation procedures.

### 9.5 Use short-lived access tokens

Keep access token lifetimes appropriate to the application's risk.

Use securely managed refresh tokens where longer sessions are required.

### 9.6 Implement revocation controls

Consider:

- Refresh token revocation.
- Server-side session tracking.
- Token denylisting where justified.
- Account disablement handling.
- Reauthentication for sensitive actions.

### 9.7 Protect token storage

For browser applications:

- Prefer appropriately configured secure cookies where suitable.
- Use `HttpOnly` to prevent JavaScript access to cookies.
- Use `Secure` to require HTTPS.
- Configure `SameSite` appropriately.
- Protect state-changing operations against CSRF where relevant.

Avoid unnecessary exposure of bearer tokens to client-side scripts.

### 9.8 Minimise claims

Include only claims required by the application.

Do not use JWT payloads as a substitute for a secure database or authorisation system.

### 9.9 Use established libraries

Use maintained JWT libraries and secure default configurations.

Avoid implementing signing, verification or cryptographic primitives from scratch.

---

## 10. Reporting

### Suggested report structure

**Title:** Improper JWT Validation in [Application / Endpoint]

**Summary:**

Describe the JWT implementation weakness and explain how it affects authentication or authorisation.

**Affected endpoint:**

```text
GET /api/v1/example
```

**Authentication context:**

Document the authorised test account and token type. Do not include the token itself.

**Steps to reproduce:**

1. Authenticate using an approved test account.
2. Capture the issued JWT.
3. Inspect the header and payload.
4. Perform the approved validation test.
5. Record whether the application accepts or rejects the test token.
6. Compare the result with expected behaviour.

**Evidence:**

- Sanitised JWT header.
- Sanitised claims.
- HTTP request and response.
- Relevant application logs, if available.
- Reproduction details.

**Impact:**

Explain the demonstrated effect on authentication, authorisation or session integrity.

**Remediation:**

Recommend strict algorithm enforcement, signature verification, claim validation, secure key management and appropriate token lifetimes.

---

## 11. Testing Checklist

### Reconnaissance

- [ ] Identify JWT usage.
- [ ] Locate token storage.
- [ ] Identify token transport mechanisms.
- [ ] Decode token headers and payloads.
- [ ] Identify signing algorithms.
- [ ] Record relevant claims.

### Validation

- [ ] Confirm signatures are verified.
- [ ] Confirm unsupported algorithms are rejected.
- [ ] Review issuer validation.
- [ ] Review audience validation.
- [ ] Review expiration handling.
- [ ] Review not-before handling.
- [ ] Check required claims.

### Authentication and authorisation

- [ ] Review token lifetime.
- [ ] Review refresh token handling.
- [ ] Review logout behaviour.
- [ ] Review account disablement.
- [ ] Compare role-based permissions.
- [ ] Check token revocation controls.

### Key management

- [ ] Review key storage.
- [ ] Review key strength.
- [ ] Review key rotation.
- [ ] Review key identifier handling.
- [ ] Check environment separation.

### Reporting

- [ ] Remove live tokens from evidence.
- [ ] Sanitise sensitive claims.
- [ ] Document expected and actual behaviour.
- [ ] Demonstrate impact safely.
- [ ] Provide remediation guidance.

---

## 12. References

- [RFC 7519 — JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519)
- [RFC 8725 — JWT Best Current Practices](https://datatracker.ietf.org/doc/html/rfc8725)
- [RFC 7515 — JSON Web Signature](https://datatracker.ietf.org/doc/html/rfc7515)
- [RFC 7516 — JSON Web Encryption](https://datatracker.ietf.org/doc/html/rfc7516)
- [OWASP JSON Web Token Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html)
- [PortSwigger — JWT Attacks](https://portswigger.net/web-security/jwt)
- [JWT.io](https://jwt.io/)
- [JWT Tool](https://github.com/ticarpi/jwt_tool)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
