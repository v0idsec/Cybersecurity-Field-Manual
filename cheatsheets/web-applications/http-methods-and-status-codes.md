# HTTP Methods and Status Codes

## Overview

HTTP methods describe the intended action for a request.

HTTP status codes communicate the result of processing that request.

## HTTP Methods

| Method | Purpose |
|---|---|
| GET | Retrieve a resource |
| POST | Submit data or trigger processing |
| PUT | Create or replace a resource |
| PATCH | Partially modify a resource |
| DELETE | Remove a resource |
| HEAD | Retrieve response headers without the response body |
| OPTIONS | Describe communication options |
| TRACE | Diagnostic loopback method |
| CONNECT | Establish a tunnel through a proxy |

## Safe Methods

A safe method is intended not to change the server's application state.

Safe methods include:

- GET
- HEAD
- OPTIONS
- TRACE

Safe does not mean risk-free.

For example, a GET request can still disclose sensitive information or trigger unintended behaviour if an application is incorrectly designed.

## Idempotent Methods

An idempotent method produces the same intended effect when the same request is repeated.

| Method | Idempotent |
|---|---|
| GET | Yes |
| HEAD | Yes |
| PUT | Yes |
| DELETE | Yes |
| OPTIONS | Yes |
| TRACE | Yes |
| POST | No |
| PATCH | Not guaranteed |

Idempotency does not mean that every response will be identical.

For example, the first DELETE request might return 204, while a repeated request returns 404. The intended resource state is still the same.

## HTTP Status Code Classes

| Range | Class | Description |
|---|---|---|
| 100–199 | Informational | Request processing continues |
| 200–299 | Success | Request successfully processed |
| 300–399 | Redirection | Further action required |
| 400–499 | Client Error | Problem with the request |
| 500–599 | Server Error | Server failed to fulfil the request |

## Common 1xx Responses

| Code | Name | Description |
|---|---|---|
| 100 | Continue | Client may continue sending request |
| 101 | Switching Protocols | Protocol switch accepted |
| 103 | Early Hints | Preliminary response headers |

## Common 2xx Responses

| Code | Name | Description |
|---|---|---|
| 200 | OK | Request succeeded |
| 201 | Created | Resource created |
| 202 | Accepted | Request accepted for processing |
| 204 | No Content | Successful response without content |
| 206 | Partial Content | Partial resource returned |

## Common 3xx Responses

| Code | Name | Description |
|---|---|---|
| 301 | Moved Permanently | Resource permanently moved |
| 302 | Found | Temporary redirect |
| 303 | See Other | Redirect using GET |
| 304 | Not Modified | Cached resource remains valid |
| 307 | Temporary Redirect | Temporary redirect preserving method |
| 308 | Permanent Redirect | Permanent redirect preserving method |

## Common 4xx Responses

| Code | Name | Description |
|---|---|---|
| 400 | Bad Request | Invalid or malformed request |
| 401 | Unauthorized | Valid authentication credentials are missing or invalid |
| 403 | Forbidden | Server refuses the request |
| 404 | Not Found | Resource not found |
| 405 | Method Not Allowed | Method not supported for resource |
| 406 | Not Acceptable | Cannot provide an acceptable representation |
| 408 | Request Timeout | Request timed out |
| 409 | Conflict | Conflict with current resource state |
| 410 | Gone | Resource is no longer available |
| 413 | Content Too Large | Request body exceeds allowed size |
| 415 | Unsupported Media Type | Unsupported request format |
| 422 | Unprocessable Content | Request understood but cannot be processed |
| 429 | Too Many Requests | Rate limit exceeded |

## Common 5xx Responses

| Code | Name | Description |
|---|---|---|
| 500 | Internal Server Error | Unexpected server failure |
| 501 | Not Implemented | Functionality not supported |
| 502 | Bad Gateway | Invalid response from upstream server |
| 503 | Service Unavailable | Server temporarily unavailable |
| 504 | Gateway Timeout | Upstream server did not respond in time |

## 401 vs 403

These two status codes are frequently confused.

**401 Unauthorized**

The request lacks valid authentication credentials.

Examples:

- Missing login token
- Expired session
- Invalid authentication credentials

**403 Forbidden**

The server understands the request but refuses to fulfil it.

Examples:

- Authenticated user lacks permission
- Access restricted by policy
- Resource access explicitly denied

## 301 vs 302 vs 307 vs 308

| Code | Redirect Type | Method Behaviour |
|---|---|---|
| 301 | Permanent | Historically may change POST to GET |
| 302 | Temporary | Historically may change POST to GET |
| 307 | Temporary | Must preserve method |
| 308 | Permanent | Must preserve method |

## 404 vs 410

- 404: The server cannot find the requested resource, or is unwilling to disclose whether it exists.
- 410: The resource is known to be permanently unavailable.

## Key Takeaways

- HTTP methods describe intended actions.
- Safe and idempotent are different concepts.
- Status codes communicate request outcomes.
- 401 relates to authentication.
- 403 relates to access refusal.
- 307 and 308 preserve the original request method.
