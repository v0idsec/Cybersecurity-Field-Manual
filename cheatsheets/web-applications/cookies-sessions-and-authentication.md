# Cookies, Sessions and Authentication

## Overview

Web applications need mechanisms to identify users, maintain state and control access to resources.

Common mechanisms include:

- HTTP cookies
- Server-side sessions
- Authentication tokens
- JSON Web Tokens (JWTs)
- Multi-factor authentication

## Cookies

Cookies are small pieces of data stored by a browser and associated with a website.

Servers commonly create cookies using the Set-Cookie response header.

Example:

    Set-Cookie: sessionid=abc123; Secure; HttpOnly; SameSite=Lax

The browser can subsequently include the cookie in matching requests.

    Cookie: sessionid=abc123

Cookies are commonly used for:

- Session management
- Authentication
- User preferences
- Shopping carts
- Tracking

## Important Cookie Attributes

| Attribute | Purpose |
|---|---|
| Secure | Only send over secure connections |
| HttpOnly | Prevent JavaScript access through document.cookie |
| SameSite | Controls cross-site cookie sending |
| Domain | Controls which hosts can receive the cookie |
| Path | Restricts the URL paths for which the cookie is sent |
| Expires | Defines an absolute expiration time |
| Max-Age | Defines cookie lifetime in seconds |
| Partitioned | Enables partitioned cookie storage |

## SameSite Values

| Value | Behaviour |
|---|---|
| Strict | Restricts cookies to same-site contexts |
| Lax | Allows cookies in certain cross-site top-level navigations |
| None | Allows cross-site cookie use, subject to browser requirements |

Cookies using `SameSite=None` must also include the `Secure` attribute in modern browsers.

Browser behaviour can vary depending on privacy settings and cookie policies.

## HttpOnly

The HttpOnly attribute prevents client-side JavaScript from reading the cookie through browser cookie APIs.

It helps reduce the risk of session cookie theft through certain cross-site scripting scenarios.

It does not prevent the browser from automatically sending the cookie with applicable requests.

## Secure

The Secure attribute restricts cookie transmission to secure connections.

It helps prevent session cookies from being sent over unencrypted HTTP.

## Session Management

HTTP is stateless, so applications commonly implement sessions to maintain user state.

A typical session workflow:

1. User authenticates.
2. Server creates a session.
3. Server generates a session identifier.
4. Identifier is returned to the browser, commonly in a cookie.
5. Browser sends the identifier with subsequent requests.
6. Server uses the identifier to retrieve session information.

Session information is commonly stored in:

- Memory
- Databases
- Redis
- Distributed session stores

## Session Security

Important session security practices include:

- Generate unpredictable session identifiers.
- Use HTTPS.
- Set Secure and HttpOnly cookie attributes.
- Apply an appropriate SameSite policy.
- Rotate session identifiers after authentication or privilege changes.
- Invalidate sessions during logout.
- Enforce idle and absolute session timeouts.
- Avoid exposing session identifiers in URLs.
- Protect against session fixation.
- Revoke sessions when necessary.

## Authentication vs Authorisation

| Concept | Meaning |
|---|---|
| Authentication | Verifying who someone is |
| Authorisation | Determining what someone can access |
| Accounting | Recording actions and activity |

Example:

A user successfully logs into an application.

- Authentication confirms their identity.
- Authorisation determines whether they can access administrative features.
- Accounting records relevant activity.

## Common Authentication Factors

| Factor | Example |
|---|---|
| Something you know | Password or PIN |
| Something you have | Hardware security key or authenticator device |
| Something you are | Fingerprint or facial recognition |

Multi-factor authentication (MFA) combines two or more different factor categories.

Using two passwords is not MFA because both are knowledge factors.

## Authentication Tokens

Tokens are commonly used to represent authenticated users or authorised clients.

Common examples:

- Session identifiers
- Bearer tokens
- OAuth access tokens
- OpenID Connect ID tokens
- JSON Web Tokens

### Bearer Tokens

A bearer token grants access to whoever possesses it, subject to the token's scope, validity and server-side policy.

Commonly transmitted using:

    Authorization: Bearer <token>

Bearer tokens should be protected like credentials.

### JSON Web Tokens (JWT)

JWTs are a compact token format used to represent claims.

A signed JWT commonly contains three Base64URL-encoded components:

    header.payload.signature

The components are:

1. Header: Token type and signing algorithm.
2. Payload: Claims about the subject and token.
3. Signature: Cryptographic protection against unauthorised modification.

Important JWT claims include:

| Claim | Purpose |
|---|---|
| iss | Issuer |
| sub | Subject |
| aud | Audience |
| exp | Expiration time |
| nbf | Not valid before |
| iat | Issued at |
| jti | Unique token identifier |

A signed JWT is not necessarily encrypted.

Its payload can generally be decoded by anyone who possesses the token.

## OAuth 2.0 vs OpenID Connect

| Technology | Purpose |
|---|---|
| OAuth 2.0 | Delegated authorisation |
| OpenID Connect | Authentication layer built on OAuth 2.0 |

OAuth 2.0 allows an application to obtain limited access to resources without directly receiving the user's password.

OpenID Connect provides an identity layer and standardised authentication information.

## Password Storage

Passwords should never be stored as plaintext.

Recommended password storage approaches use purpose-built password hashing algorithms.

Common choices include:

- Argon2id
- bcrypt
- scrypt
- PBKDF2

Password hashing should use unique salts and appropriate work factors.

Fast general-purpose hashes such as MD5 and SHA-1 are unsuitable for password storage.

## Key Takeaways

- Cookies allow browsers to maintain state.
- Sessions commonly use unpredictable identifiers.
- HttpOnly and Secure protect cookies in different ways.
- Authentication and authorisation are separate concepts.
- Bearer tokens must be treated as sensitive credentials.
- Signed JWTs are not automatically encrypted.
- OAuth 2.0 is an authorisation framework; OpenID Connect adds authentication.
