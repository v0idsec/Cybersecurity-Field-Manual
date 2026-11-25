
# WebSocket Security

> Professional reference guide for assessing WebSocket implementations, persistent connections and real-time application communication.

## Contents

- [Overview](#overview)
- [WebSocket Fundamentals](#websocket-fundamentals)
- [Architecture and Attack Surface](#architecture-and-attack-surface)
- [Handshake Assessment](#handshake-assessment)
- [Authentication and Session Management](#authentication-and-session-management)
- [Authorisation Testing](#authorisation-testing)
- [Message-Level Testing](#message-level-testing)
- [Cross-Site WebSocket Hijacking](#cross-site-websocket-hijacking)
- [Input Validation](#input-validation)
- [Connection and Resource Management](#connection-and-resource-management)
- [Assessment Methodology](#assessment-methodology)
- [Impact Analysis](#impact-analysis)
- [Mitigation](#mitigation)
- [Tools and References](#tools-and-references)
- [Assessment Checklist](#assessment-checklist)

---

## Overview

WebSockets provide persistent, bidirectional communication between clients and servers.

Unlike traditional HTTP request-response interactions, WebSocket connections remain open and allow either party to send messages independently.

They are commonly used for:

- Chat applications.
- Notifications.
- Collaborative platforms.
- Trading interfaces.
- Real-time dashboards.
- Multiplayer applications.
- Administrative interfaces.
- Live support systems.
- API event streams.

WebSocket implementations introduce additional security considerations around authentication, authorisation, message handling and connection lifecycle management.

Potential vulnerabilities include:

- Cross-Site WebSocket Hijacking (CSWSH).
- Missing message-level authorisation.
- Insecure session handling.
- Injection vulnerabilities.
- Information disclosure.
- Cross-tenant data exposure.
- Denial of service.
- Insecure origin validation.

## WebSocket Fundamentals

A WebSocket connection generally begins with an HTTP handshake.

Example:

```http
GET /socket HTTP/1.1
Host: example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: <random-value>
Sec-WebSocket-Version: 13
Origin: https://example.com
```

A successful handshake typically returns:

```http
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: <calculated-value>
```

Once established, the connection carries WebSocket frames rather than ordinary HTTP requests.

### WebSocket Schemes

| Scheme | Description |
|---|---|
| `ws://` | WebSocket over an unencrypted connection |
| `wss://` | WebSocket over TLS |

Production applications should generally use `wss://`.

## Architecture and Attack Surface

Map the WebSocket architecture before testing.

Consider:

- Browser or client application.
- WebSocket endpoint.
- API gateway.
- Reverse proxy.
- Authentication service.
- Message broker.
- Backend application.
- Database.
- Other connected clients.

Identify:

- Connection establishment.
- Authentication mechanism.
- Message formats.
- Message routing.
- Subscription handling.
- User and tenant boundaries.
- Connection termination behaviour.

A WebSocket endpoint may expose functionality that is not visible through ordinary HTTP navigation.

## Handshake Assessment

Review the initial handshake for:

- Authentication requirements.
- Cookie handling.
- Origin validation.
- Protocol negotiation.
- Endpoint access controls.
- Session binding.
- Rate limiting.

### Origin Validation

The `Origin` header identifies the origin initiating a browser WebSocket connection.

Check whether the server:

- Validates the expected origin.
- Uses an explicit allowlist.
- Rejects untrusted origins.
- Handles absent origins appropriately.
- Avoids weak substring matching.

Origin validation is particularly important when authentication relies on browser cookies.

### Subprotocol Negotiation

Review `Sec-WebSocket-Protocol` handling.

Determine whether:

- Only expected subprotocols are accepted.
- Unsupported protocols are rejected.
- Protocol selection influences authorisation.
- Client-supplied values are trusted incorrectly.

## Authentication and Session Management

Determine how a WebSocket connection is authenticated.

Common mechanisms include:

- Session cookies.
- Bearer tokens.
- Short-lived connection tokens.
- Authentication during the handshake.
- Application-level authentication messages.

Test the following:

| Test | Objective |
|---|---|
| Unauthenticated connection | Determine whether authentication is required |
| Expired session | Assess session expiry handling |
| Invalid token | Determine whether invalid credentials are rejected |
| Logged-out session | Confirm connection invalidation |
| Session rotation | Determine whether existing connections remain valid |
| Cross-account session | Check connection identity binding |

### Long-Lived Sessions

WebSocket connections can outlive the original authentication context.

Investigate whether:

- Sessions are periodically revalidated.
- Logout closes active connections.
- Token expiry is enforced.
- Privilege changes take effect immediately.
- Revoked users retain access through existing connections.

## Authorisation Testing

Authentication during the handshake does not guarantee that individual messages are authorised.

Test every sensitive message type.

Examples include:

- `subscribe`
- `unsubscribe`
- `join`
- `leave`
- `send`
- `update`
- `delete`
- `admin`
- `export`

### Horizontal Access Control

Determine whether a user can access another user's data by modifying:

- User IDs.
- Account IDs.
- Conversation IDs.
- Channel IDs.
- Room identifiers.
- Subscription identifiers.

### Vertical Access Control

Test whether lower-privileged users can invoke administrative message types or privileged operations.

### Multi-Tenant Isolation

Where applicable, assess whether messages can cross tenant boundaries.

Test:

- Tenant identifiers.
- Organisation identifiers.
- Workspace identifiers.
- Resource ownership.
- Subscription membership.

Use accounts and test data belonging to the assessment environment.

## Message-Level Testing

WebSocket messages are application inputs and should be assessed like ordinary API requests.

Review:

- JSON structure.
- Message types.
- Required fields.
- Optional fields.
- Data types.
- Identifiers.
- Nested objects.
- Client-supplied roles.
- State transitions.

Example message:

```json
{
  "type": "message",
  "conversation_id": "12345",
  "content": "Hello"
}
```

Investigate whether the server validates:

- Message type.
- Conversation ownership.
- Sender identity.
- Content length.
- Content encoding.
- Message sequence.
- Application state.

### Mass Assignment

Determine whether the server accepts unexpected fields.

For example, an application may unintentionally accept client-supplied properties that should be controlled by the server.

### Message Replay

Assess whether previously valid messages can be replayed.

Consider:

- Duplicate transactions.
- Repeated state changes.
- Replayed authorisation actions.
- Missing sequence validation.
- Missing idempotency controls.

## Cross-Site WebSocket Hijacking

Cross-Site WebSocket Hijacking occurs when an attacker-controlled website can initiate a WebSocket connection to a vulnerable application using a victim's authenticated browser session.

This is particularly relevant where:

- Authentication uses cookies.
- The server accepts untrusted origins.
- The browser automatically attaches authentication cookies.
- The application exposes sensitive functionality through the connection.

### Assessment Considerations

Review:

- Origin validation.
- Cookie `SameSite` attributes.
- Cookie domain and path.
- Authentication requirements.
- Sensitive message operations.
- Whether the connection can be established cross-origin.

A successful WebSocket handshake from an untrusted origin does not automatically prove exploitable CSWSH.

Confirm that the connection provides access to meaningful authenticated functionality.

## Input Validation

Assess WebSocket messages for common application vulnerabilities.

Relevant categories include:

| Category | Testing considerations |
|---|---|
| SQL injection | Message fields reaching database queries |
| XSS | Messages rendered into browser content |
| Command injection | Message values reaching system commands |
| Path traversal | File-related message parameters |
| Deserialisation | Complex or structured message processing |
| SSRF | Messages that trigger server-side requests |
| XML injection | XML-based message formats |
| Template injection | Message values reaching rendering engines |

Also assess:

- Unicode handling.
- Null bytes.
- Unexpected data types.
- Oversized messages.
- Nested object depth.
- Binary frames.
- Invalid JSON.
- Malformed message structures.

## Connection and Resource Management

Persistent connections introduce resource-management risks.

Assess:

- Maximum connection limits.
- Idle connection timeouts.
- Message size limits.
- Message frequency limits.
- Subscription limits.
- Authentication timeouts.
- Heartbeat handling.
- Reconnection behaviour.
- Cleanup after disconnect.

Potential weaknesses include:

- Unbounded connection creation.
- Excessive message processing.
- Unrestricted subscriptions.
- Resource exhaustion.
- Missing cleanup of disconnected clients.

Avoid conducting high-volume denial-of-service testing against production systems without explicit approval and a controlled test plan.

## Assessment Methodology

### 1. Identify WebSocket Endpoints

Review:

- JavaScript source.
- Browser network activity.
- Application documentation.
- API specifications.
- Mobile application traffic.
- Known real-time functionality.

Record endpoint URLs and expected protocols.

### 2. Map Message Types

Capture representative application interactions.

Build a message inventory:

| Message | Purpose | Sensitive operation |
|---|---|---|
| Subscribe | Join a channel | Potentially |
| Send | Submit content | Yes |
| Update | Modify a resource | Yes |
| Delete | Remove a resource | Yes |
| Admin | Administrative action | Yes |

### 3. Identify Trust Boundaries

Determine which values are controlled by:

- The authenticated user.
- The client application.
- The server.
- Other connected users.
- External systems.

Never assume that a client-provided identifier establishes ownership.

### 4. Test Authentication

Assess connection establishment, session expiry, logout and revocation.

### 5. Test Authorisation

Replay legitimate message structures using:

- Different test accounts.
- Different roles.
- Different resource identifiers.
- Different tenant contexts.

### 6. Test Message Handling

Assess validation, injection, state transitions and unexpected message properties.

### 7. Test Connection Management

Review rate limits, connection lifecycle and resource controls.

### 8. Validate Findings

Confirm server-side impact rather than relying solely on client-side behaviour.

## Impact Analysis

Potential impact includes:

- Unauthorised access to private messages.
- Cross-user data disclosure.
- Cross-tenant information exposure.
- Unauthorised administrative actions.
- Session abuse.
- Stored or reflected XSS.
- Transaction manipulation.
- Resource exhaustion.

Severity should reflect the sensitivity of accessible data and the operations available to an attacker.

## Mitigation

Recommended controls:

- Use `wss://`.
- Enforce strict origin validation.
- Require authentication.
- Bind connections to authenticated identities.
- Revalidate long-lived sessions.
- Close connections after logout or revocation.
- Enforce message-level authorisation.
- Validate all message fields server-side.
- Avoid trusting client-supplied roles or ownership.
- Implement message size and rate limits.
- Limit subscriptions and concurrent connections.
- Validate tenant and resource boundaries.
- Encode untrusted content before rendering.
- Monitor abnormal connection and message activity.

## Evidence Collection

Record:

- WebSocket endpoint.
- Handshake request and response.
- Authentication mechanism.
- Origin behaviour.
- Message type.
- Relevant message payload.
- User role and account context.
- Server response.
- Demonstrated impact.
- Reproduction steps.
- Connection and session state.

Redact authentication tokens and sensitive message contents.

## Tools and References

### Tools

- Burp Suite.
- Burp Repeater.
- Burp WebSocket message history.
- Browser developer tools.
- WebSocket command-line clients.
- Custom WebSocket test scripts.

### References

- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP WebSocket Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [RFC 6455 — The WebSocket Protocol](https://www.rfc-editor.org/rfc/rfc6455)
- [CWE-1385 — Missing Origin Validation in WebSockets](https://cwe.mitre.org/)

## Assessment Checklist

- [ ] All WebSocket endpoints identified.
- [ ] Message types documented.
- [ ] Handshake authentication assessed.
- [ ] Origin validation assessed.
- [ ] Session expiry and logout behaviour tested.
- [ ] Message-level authorisation tested.
- [ ] Horizontal and vertical access control assessed.
- [ ] Tenant isolation verified.
- [ ] Input validation tested.
- [ ] Replay behaviour assessed.
- [ ] Connection and resource limits reviewed.
- [ ] Evidence captured and sensitive data redacted.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
