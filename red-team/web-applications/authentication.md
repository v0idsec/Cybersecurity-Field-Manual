# Authentication Security Testing

A practical guide to assessing authentication mechanisms in web applications during authorised security assessments.

Authentication vulnerabilities can allow attackers to impersonate users, bypass login requirements, compromise accounts or gain access to functionality intended for other users.

This guide covers authentication workflows, password security, multi-factor authentication, session management, account recovery and common implementation weaknesses.

> **Scope reminder:** Only test accounts and applications you are authorised to assess. Avoid password spraying, credential stuffing, account lockouts or testing real users unless explicitly permitted by the engagement rules.

---

## Contents

- [1. Authentication Fundamentals](#1-authentication-fundamentals)
- [2. Login Functionality](#2-login-functionality)
- [3. Username and Account Enumeration](#3-username-and-account-enumeration)
- [4. Password Security](#4-password-security)
- [5. Multi-Factor Authentication](#5-multi-factor-authentication)
- [6. Password Reset and Account Recovery](#6-password-reset-and-account-recovery)
- [7. Session Management](#7-session-management)
- [8. OAuth and SSO](#8-oauth-and-sso)
- [9. Common Authentication Vulnerabilities](#9-common-authentication-vulnerabilities)
- [10. Testing Tools](#10-testing-tools)
- [11. Testing Checklist](#11-testing-checklist)
- [12. Further Reading](#12-further-reading)

---

## 1. Authentication Fundamentals

Authentication verifies the identity of a user attempting to access an application.

It is important to distinguish between three related security concepts:

| Concept | Purpose | Example |
|---|---|---|
| Authentication | Establishes who a user is | Logging in with a password |
| Authorisation | Determines what a user can access | Accessing an administrator page |
| Session management | Maintains authenticated state | Session cookies |

A secure authentication implementation should:

- Verify user identity reliably.
- Protect credentials during transmission and storage.
- Enforce appropriate authentication requirements.
- Manage sessions securely.
- Prevent account recovery abuse.
- Avoid exposing sensitive authentication information.
- Apply consistent controls across application endpoints.

---

## 2. Login Functionality

The login process is often the first major authentication workflow to assess.

### Areas to investigate

- Username and email handling
- Password validation
- Authentication error messages
- Rate limiting
- Account lockout behaviour
- MFA enforcement
- Remember-me functionality
- Login persistence
- Alternate authentication endpoints
- Client-side versus server-side validation

### Manual testing

Using an authorised test account:

1. Submit valid credentials.
2. Submit an incorrect password.
3. Submit an invalid username.
4. Submit empty credentials.
5. Observe error messages and response differences.
6. Review session cookies after successful authentication.
7. Test logout and subsequent access to protected pages.
8. Check whether authentication requirements are consistent across endpoints.

### Inspect requests with Burp Suite

Intercept a login request using Burp Proxy.

Example request:

```http
POST /login HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded

username=test@example.com&password=ExamplePassword123
```

Things to examine:

- Are credentials transmitted over HTTPS?
- Are sensitive values exposed in URLs?
- Does the server enforce validation?
- Are authentication responses consistent?
- Are session identifiers regenerated after login?
- Is authentication state maintained securely?

Do not place real credentials in public logs, screenshots or repository examples.

---

## 3. Username and Account Enumeration

Account enumeration occurs when an application reveals whether a particular username, email address or account exists.

### Common indicators

Different responses for valid and invalid accounts:

```text
Invalid username
```

Compared with:

```text
Incorrect password
```

Other possible indicators:

- Different HTTP status codes
- Different response lengths
- Different redirect behaviour
- Different response timing
- Different password-reset messages
- Different registration responses

### Testing approach

Using approved test accounts:

1. Submit a known valid username with an incorrect password.
2. Submit a known invalid username.
3. Compare response bodies.
4. Compare status codes and response lengths.
5. Observe whether response timing differs consistently.
6. Repeat only within permitted testing limits.

### Why it matters

An attacker who can identify valid accounts may use that information to target users with phishing, password attacks or other account compromise attempts.

### Mitigation

- Use generic authentication error messages.
- Keep response behaviour consistent.
- Apply appropriate rate limiting.
- Avoid revealing account existence through recovery workflows.

---

## 4. Password Security

Password security covers both how passwords are accepted and how they are stored.

### Areas to assess

- Password policy enforcement
- Minimum password length
- Password complexity requirements
- Password reuse controls
- Compromised password screening
- Rate limiting
- Secure password storage
- Password change workflows
- Password reset invalidation

### Password storage

Passwords should never be stored in plaintext or reversibly encrypted for ordinary authentication.

Common password hashing algorithms:

| Algorithm | Notes |
|---|---|
| Argon2id | Strong modern password hashing choice |
| bcrypt | Widely used adaptive password hashing |
| scrypt | Memory-hard password hashing |
| PBKDF2 | Password-based key derivation function |

Fast general-purpose hashes such as MD5 and SHA-1 are unsuitable for password storage.

### Testing considerations

- Does the application enforce password requirements server-side?
- Are passwords transmitted securely?
- Are password changes protected by reauthentication where appropriate?
- Does changing a password invalidate existing sessions?
- Are password reset tokens single-use?
- Are password hashes protected from unauthorised access?

### References

- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [NIST Digital Identity Guidelines](https://pages.nist.gov/800-63-4/)

---

## 5. Multi-Factor Authentication

Multi-factor authentication (MFA) requires users to verify their identity using more than one factor.

Common factors include:

| Factor | Example |
|---|---|
| Something you know | Password or PIN |
| Something you have | Authenticator app or hardware security key |
| Something you are | Fingerprint or facial recognition |

### Common MFA implementations

- Time-based One-Time Passwords (TOTP)
- SMS verification codes
- Email verification codes
- Push notifications
- Hardware security keys
- Passkeys and WebAuthn

### MFA testing areas

#### MFA enforcement

- Is MFA required for accounts where policy requires it?
- Can MFA be skipped through alternate login paths?
- Is MFA consistently enforced across application endpoints?
- Does MFA apply to sensitive account actions?

#### MFA verification

- Are verification codes single-use?
- Do codes expire?
- Are attempts appropriately limited?
- Can an expired code be reused?
- Is the verification process bound to the correct login session?

#### MFA recovery

- Can recovery methods bypass the normal MFA process?
- Are backup codes single-use?
- Does removing MFA require appropriate verification?
- Are users notified when MFA settings change?

#### MFA state management

- Can an unauthenticated user access post-MFA functionality?
- Is authentication state updated correctly after successful verification?
- Are session identifiers handled securely throughout the MFA process?

### Common weaknesses

- MFA not enforced on alternate authentication endpoints
- Weak recovery workflows
- Reusable verification codes
- Missing rate limiting
- Poor session binding
- Insecure MFA removal procedures

### References

- [OWASP Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)
- [WebAuthn Guide](https://webauthn.guide/)

---

## 6. Password Reset and Account Recovery

Account recovery mechanisms are particularly sensitive because they can provide an alternative route into an account.

### Common recovery mechanisms

- Email reset links
- SMS verification
- Security questions
- Recovery codes
- Support-assisted recovery
- Identity verification workflows

### Testing areas

#### Reset token handling

- Are reset tokens generated securely?
- Are tokens sufficiently unpredictable?
- Do tokens expire?
- Are tokens single-use?
- Are tokens invalidated after a successful reset?
- Can a token be reused after password changes?

#### Reset workflow

- Is the recovery process bound to the correct account?
- Can the process be manipulated to affect another account?
- Does the application disclose account existence?
- Are users notified of password changes?
- Are existing sessions invalidated appropriately?

#### Reset link handling

- Is HTTPS enforced?
- Are reset tokens exposed through redirects or third-party resources?
- Does the application validate the reset request server-side?
- Are tokens protected against accidental disclosure?

### Common vulnerabilities

- Predictable reset tokens
- Reusable reset tokens
- Missing token expiry
- Account enumeration
- Insecure recovery questions
- Host header manipulation affecting generated reset links
- Weak support-assisted account recovery

### References

- [OWASP Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

---

## 7. Session Management

Once a user authenticates, applications typically maintain their identity through a session.

Session weaknesses can allow attackers to impersonate users or retain access after authentication should have ended.

### Session cookies

Review cookie attributes:

| Attribute | Security purpose |
|---|---|
| Secure | Restricts cookie transmission to HTTPS |
| HttpOnly | Prevents direct JavaScript access |
| SameSite | Helps control cross-site cookie sending |
| Domain | Defines applicable hosts |
| Path | Defines applicable URL paths |
| Expires / Max-Age | Defines cookie lifetime |

### Session testing

- Is the session identifier regenerated after login?
- Does logout invalidate the session server-side?
- Does password reset invalidate existing sessions?
- Are session identifiers unpredictable?
- Are session cookies protected by appropriate attributes?
- Do sessions expire after the expected inactivity period?
- Are concurrent sessions handled appropriately?
- Can sensitive actions be performed using stale sessions?

### Session fixation

Session fixation occurs when an attacker can cause a victim to authenticate using a session identifier known to the attacker.

Assess whether the application regenerates session identifiers after authentication and privilege changes.

### Session invalidation

A common testing scenario:

1. Log in using an authorised test account.
2. Record the session cookie.
3. Log out.
4. Attempt to access a protected resource using the old session.
5. Confirm that the server rejects the invalidated session.

### References

- [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)

---

## 8. OAuth and SSO

Applications frequently delegate authentication to external identity providers.

Examples include:

- Microsoft Entra ID
- Google Identity
- Okta
- Auth0
- Keycloak

### OAuth and OpenID Connect

OAuth 2.0 is primarily an authorisation framework. OpenID Connect (OIDC) adds an identity layer on top of OAuth 2.0.

### Testing areas

- Redirect URI validation
- State parameter validation
- Nonce validation in OIDC
- PKCE enforcement where appropriate
- Token audience validation
- Token issuer validation
- Token expiry
- Account linking
- Authentication callback handling
- Logout behaviour
- Identity provider configuration

### Common weaknesses

- Insecure redirect URI validation
- Missing or incorrect state validation
- Inadequate nonce validation
- Incorrect token validation
- Account linking weaknesses
- Misconfigured identity provider trust

### References

- [OAuth 2.0 Security Best Current Practice](https://datatracker.ietf.org/doc/html/rfc9700)
- [OpenID Connect](https://openid.net/developers/how-connect-works/)

---

## 9. Common Authentication Vulnerabilities

| Vulnerability | Description | Potential impact |
|---|---|---|
| Account enumeration | Application reveals valid accounts | Targeted attacks |
| Weak password policy | Inadequate password requirements | Account compromise |
| Missing MFA | Insufficient authentication protection | Unauthorised access |
| MFA bypass | Authentication flow can be circumvented | Account compromise |
| Session fixation | Attacker can influence a victim's session identifier | Session compromise |
| Session hijacking | Unauthorised use of a valid session | Account impersonation |
| Weak reset tokens | Predictable or reusable recovery tokens | Account takeover |
| Insecure OAuth configuration | Incorrect identity or redirect validation | Authentication compromise |
| Credential exposure | Sensitive credentials disclosed | Unauthorised access |
| Missing rate limiting | Excessive authentication attempts are permitted | Increased attack opportunity |

---

## 10. Testing Tools

| Tool | Purpose | Resource |
|---|---|---|
| Burp Suite | Intercept and inspect authentication requests | [Website](https://portswigger.net/burp) |
| OWASP ZAP | Web application security testing | [Website](https://www.zaproxy.org/) |
| Postman | API authentication testing | [Website](https://www.postman.com/) |
| JWT.io | Inspect JWT structure | [Website](https://jwt.io/) |
| jwt_tool | JWT security testing | [GitHub](https://github.com/ticarpi/jwt_tool) |
| Hydra | Authentication testing in explicitly authorised environments | [GitHub](https://github.com/vanhauser-thc/thc-hydra) |
| AuthMatrix | Authorisation testing in Burp Suite | [GitHub](https://github.com/SecurityInnovation/AuthMatrix) |

---

## 11. Testing Checklist

### Login
- [ ] Review login functionality
- [ ] Review authentication error messages
- [ ] Check for account enumeration
- [ ] Review rate limiting
- [ ] Verify server-side authentication enforcement
- [ ] Check alternate login endpoints

### Passwords
- [ ] Review password policy
- [ ] Review password change workflow
- [ ] Review password storage design where evidence is available
- [ ] Check password reset invalidation
- [ ] Review reauthentication requirements

### MFA
- [ ] Verify MFA enforcement
- [ ] Review MFA verification logic
- [ ] Check verification code expiry
- [ ] Review attempt limits
- [ ] Assess recovery and removal workflows
- [ ] Check alternate authentication paths

### Account recovery
- [ ] Review reset token generation
- [ ] Check token expiry
- [ ] Check token reuse
- [ ] Review account enumeration
- [ ] Check recovery workflow authorisation
- [ ] Verify notification behaviour

### Sessions
- [ ] Review session cookie attributes
- [ ] Check session regeneration after login
- [ ] Test logout invalidation
- [ ] Review session expiry
- [ ] Check password change session handling
- [ ] Review concurrent session behaviour

### OAuth and SSO
- [ ] Review redirect URI validation
- [ ] Check state validation
- [ ] Review nonce validation where applicable
- [ ] Check token issuer and audience validation
- [ ] Review account linking
- [ ] Check logout behaviour

### Documentation
- [ ] Capture relevant request and response evidence
- [ ] Document affected accounts and endpoints
- [ ] Demonstrate impact using approved test accounts
- [ ] Record remediation recommendations
- [ ] Avoid including real credentials or secrets in reports

---

## 12. Further Reading

- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
- [OWASP Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)
- [PortSwigger Authentication Vulnerabilities](https://portswigger.net/web-security/authentication)
- [PortSwigger Access Control](https://portswigger.net/web-security/access-control)
- [NIST Digital Identity Guidelines](https://pages.nist.gov/800-63-4/)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
