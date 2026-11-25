# Race Condition Vulnerability Testing

## Overview

Race conditions occur when an application's behaviour depends on the timing or ordering of multiple operations.

They commonly arise when an application performs a check and a subsequent action without ensuring that the underlying state remains valid throughout the operation.

In web applications, race conditions can allow multiple requests to interact with shared resources in unexpected ways.

Potential consequences include:

- Bypassing transaction limits.
- Redeeming single-use promotions multiple times.
- Allocating the same resource more than once.
- Performing duplicate financial operations.
- Bypassing account restrictions.
- Modifying data during concurrent processing.
- Violating workflow state requirements.

Race conditions are particularly important in applications involving payments, inventory, reservations, account balances, rewards and multi-user workflows.

> **Testing requirement:** Use authorised test accounts, isolated test resources and approved concurrency levels. Do not perform uncontrolled concurrent testing against shared production systems.

---

## Table of Contents

1. [Race Condition Fundamentals](#1-race-condition-fundamentals)
2. [Common Race Condition Types](#2-common-race-condition-types)
3. [How Race Conditions Occur](#3-how-race-conditions-occur)
4. [Identifying Potential Targets](#4-identifying-potential-targets)
5. [Testing Methodology](#5-testing-methodology)
6. [Practical Testing Scenarios](#6-practical-testing-scenarios)
7. [HTTP Request Synchronisation](#7-http-request-synchronisation)
8. [Advanced Race Condition Analysis](#8-advanced-race-condition-analysis)
9. [Common Testing Challenges](#9-common-testing-challenges)
10. [Evidence and Validation](#10-evidence-and-validation)
11. [Impact Assessment](#11-impact-assessment)
12. [Remediation](#12-remediation)
13. [Testing Checklist](#13-testing-checklist)
14. [References](#14-references)

---

## 1. Race Condition Fundamentals

### 1.1 What is a race condition?

A race condition occurs when the result of an operation depends on the relative timing of concurrent events.

Consider an application that allows a user to claim a reward once.

The intended logic might be:

```text
1. Check whether the reward has already been claimed.
2. If not claimed, issue the reward.
3. Mark the reward as claimed.
```

If two requests execute concurrently, both may check the reward before either request updates its status.

```text
Request A                 Request B
---------                 ---------
Check: Not claimed
                          Check: Not claimed
Issue reward
                          Issue reward
Mark as claimed
                          Mark as claimed
```

Both requests may succeed even though the business rule permits only one claim.

The vulnerability exists because the check and update are not performed as one atomic operation.

### 1.2 Concurrency versus race conditions

Concurrency is not inherently a vulnerability.

Modern applications routinely process multiple requests simultaneously.

A vulnerability exists when concurrent execution causes a violation of an application invariant or security requirement.

Examples of invariants:

- A coupon can only be redeemed once.
- An account balance cannot become negative.
- An inventory item cannot be sold twice.
- A refund cannot exceed the original payment.
- An approval can only be completed by an authorised user.

### 1.3 Atomicity

An operation is atomic when it behaves as one indivisible unit.

For security-sensitive operations, related checks and state changes should be performed atomically where required.

Without atomicity, another request may modify the underlying state between validation and execution.

---

## 2. Common Race Condition Types

### 2.1 Time-of-check to time-of-use (TOCTOU)

TOCTOU vulnerabilities occur when an application checks a condition and later uses the result without ensuring the condition is still valid.

Example:

```text
Check: User has sufficient balance
          |
          v
Process transaction
          |
          v
Deduct transaction amount
```

Two concurrent requests may both pass the balance check before either deduction occurs.

### 2.2 Limit bypass

Applications frequently enforce limits on:

- Coupon redemption.
- Password recovery.
- Account creation.
- Reward claims.
- Ticket reservations.
- API operations.

If the limit check and operation are not atomic, concurrent requests may exceed the intended limit.

### 2.3 Duplicate execution

A single operation may be processed more than once.

Examples:

- Duplicate payments.
- Duplicate orders.
- Repeated refunds.
- Duplicate account credits.
- Repeated invitation acceptance.

### 2.4 State transition races

Two requests may attempt to modify the same object simultaneously.

For example:

```text
Initial state: Pending

Request A: Approve
Request B: Reject

Possible result: Inconsistent final state
```

The application should ensure that only valid transitions can occur.

### 2.5 Resource allocation races

Two users or requests may attempt to reserve the same limited resource.

Examples:

- Event tickets.
- Hotel rooms.
- Inventory.
- Appointment slots.
- Unique usernames.
- Limited-access resources.

### 2.6 Asynchronous processing races

Applications may delegate work to background jobs, queues or external services.

Race conditions can occur when:

- Jobs execute more than once.
- Events arrive out of order.
- Retries overlap with original operations.
- State changes occur before a job completes.
- Multiple workers process the same resource.

---

## 3. How Race Conditions Occur

### 3.1 Non-atomic check and update

A common vulnerable implementation:

```sql
SELECT balance
FROM accounts
WHERE account_id = 1001;

-- Application checks that balance is sufficient.

UPDATE accounts
SET balance = balance - 100
WHERE account_id = 1001;
```

The application separates the validation and update into different operations.

A safer approach is to combine the condition and update:

```sql
UPDATE accounts
SET balance = balance - 100
WHERE account_id = 1001
AND balance >= 100;
```

The application must then verify that exactly one row was updated.

This is a simplified illustration. Real financial operations also require appropriate transaction handling, concurrency controls and audit records.

### 3.2 Missing uniqueness constraints

An application may check whether a record exists before creating another.

If multiple requests pass the check simultaneously, duplicate records may be created.

A database uniqueness constraint provides an additional enforcement layer.

### 3.3 Insufficient transaction isolation

Database isolation determines how concurrent transactions interact.

Weak or inappropriate isolation can allow inconsistent reads or updates.

Relevant concepts include:

- Dirty reads.
- Non-repeatable reads.
- Phantom reads.
- Lost updates.
- Write skew.

The correct isolation strategy depends on the application's data model and consistency requirements.

### 3.4 Missing idempotency controls

An operation is idempotent when repeating it produces the same intended result as performing it once.

For example, a client retrying a payment request should not create multiple independent charges.

Where operations may be retried, applications should use appropriate idempotency controls.

### 3.5 Distributed system timing

Applications built from multiple services may have additional consistency challenges.

Examples include:

- Separate payment and order services.
- Event-driven workflows.
- Message queues.
- Distributed caches.
- Replicated databases.
- External identity providers.

A successful update in one component does not necessarily mean every other component has received or processed the change.

---

## 4. Identifying Potential Targets

Race condition testing should focus on operations that involve shared state or limited resources.

### 4.1 High-value functionality

| Functionality | Potential issue |
|---|---|
| Payments | Duplicate charges |
| Refunds | Multiple refunds |
| Coupons | Multiple redemptions |
| Inventory | Overselling |
| Reservations | Duplicate allocation |
| Rewards | Repeated claims |
| Account balances | Lost updates |
| Password recovery | Repeated token use |
| Invitations | Duplicate membership |
| Approvals | Conflicting state transitions |
| File processing | Duplicate processing |
| Account registration | Unique identifier conflicts |

### 4.2 Identify the critical operation

Review the normal request sequence.

Look for:

- A validation request followed by an update.
- A read followed by a write.
- A request that creates a record.
- A request that consumes a limited resource.
- A request that changes an object's state.
- A request that triggers an external operation.

### 4.3 Identify shared state

Determine what data is shared between concurrent requests.

Examples:

- Account balance.
- Coupon redemption count.
- Inventory quantity.
- Transaction status.
- User entitlement.
- Reservation availability.

### 4.4 Establish the expected invariant

Write down what must remain true regardless of request timing.

Examples:

```text
A coupon must never be redeemed more than once per eligible account.

An account balance must never become negative.

A completed refund must never exceed the original payment.

A resource must never be allocated to two owners simultaneously.
```

These invariants provide the basis for testing.

---

## 5. Testing Methodology

### Step 1: Establish a baseline

Perform the operation normally using an authorised test account.

Record:

- Initial application state.
- Request and response.
- Resulting state.
- Relevant resource identifiers.
- Expected operation limits.

### Step 2: Identify the concurrency window

Determine where two operations could overlap.

For example:

```text
Request A: Validate eligibility
Request A: Process operation
Request A: Update state
```

The critical area is between validation and state modification.

### Step 3: Prepare controlled requests

Capture the relevant request and identify which values must remain consistent.

Avoid changing unrelated parameters during initial testing.

### Step 4: Synchronise requests

Where supported, issue multiple requests with minimal separation so that their execution overlaps.

The objective is to test concurrency, not to generate unnecessary traffic.

### Step 5: Observe responses

Record:

- HTTP status.
- Response body.
- Response timing.
- Application state.
- Transaction identifiers.
- Side effects.

A successful HTTP response alone does not prove that a race condition occurred.

### Step 6: Verify resulting state

Check the authoritative application state through an approved test account or application interface.

For example:

- Was the reward issued once or twice?
- Was the coupon consumed more than once?
- Was the resource allocated to multiple accounts?
- Was the balance updated correctly?

### Step 7: Repeat carefully

Race conditions can be timing-sensitive.

Repeat only enough times to establish reliable reproduction, while respecting the approved testing limits.

### Step 8: Document the finding

Capture the sequence, initial state, resulting state and demonstrated impact.

---

## 6. Practical Testing Scenarios

The following scenarios describe controlled assessment patterns. Use test data and avoid triggering real financial or operational consequences.

### 6.1 Single-use coupon redemption

**Business rule:** A coupon can only be redeemed once per eligible account.

Assessment:

1. Create or obtain an authorised test account.
2. Identify the coupon redemption request.
3. Confirm the coupon is initially valid.
4. Capture the normal redemption response.
5. Restore an approved test state if necessary.
6. Test overlapping redemption requests.
7. Verify the final redemption count and resulting account state.

**Expected behaviour:** Only one redemption succeeds.

**Potential vulnerability:** Multiple requests are accepted because redemption is not enforced atomically.

### 6.2 Inventory reservation

**Business rule:** A limited inventory item can only be allocated once.

Assessment:

1. Identify a test item with limited availability.
2. Record its initial availability.
3. Identify the reservation operation.
4. Submit controlled concurrent reservation requests.
5. Verify allocation ownership and remaining inventory.

**Expected behaviour:** The application allocates no more items than are available.

**Potential vulnerability:** Multiple reservations succeed against the same remaining inventory.

### 6.3 Account balance update

**Business rule:** Transactions must not allow an account to exceed its permitted balance constraints.

Assessment:

1. Use an isolated test account.
2. Record the initial balance.
3. Identify a permitted test transaction.
4. Review concurrent transaction handling.
5. Verify the final balance and transaction ledger.

**Expected behaviour:** All transactions are accounted for exactly once and all balance constraints remain satisfied.

**Potential vulnerability:** Lost updates, duplicate processing or an invalid balance.

### 6.4 One-time reward claim

**Business rule:** A reward may only be claimed once.

Assessment:

1. Obtain an eligible test account.
2. Record the initial reward state.
3. Identify the claim operation.
4. Test overlapping claim requests.
5. Verify reward issuance and claim history.

**Expected behaviour:** One successful claim.

**Potential vulnerability:** Multiple rewards are issued.

### 6.5 Approval workflow

**Business rule:** A transaction can only transition from pending to an authorised final state once.

Assessment:

1. Create a test transaction.
2. Identify the approval and rejection operations.
3. Review the permitted state transitions.
4. Assess how simultaneous state changes are handled.
5. Verify the authoritative final state and audit history.

**Expected behaviour:** The application enforces valid transitions and preserves a consistent audit trail.

**Potential vulnerability:** Conflicting transitions result in inconsistent or unauthorised state.

---

## 7. HTTP Request Synchronisation

Synchronisation is important because ordinary sequential requests may never overlap during execution.

### 7.1 Why timing matters

Consider two requests:

```text
Request A -------------------->
                    Request B -------------------->
```

If Request B reaches the application after Request A has completed its critical operation, the test may not expose the underlying race condition.

A synchronised test attempts to align requests around the same execution window.

### 7.2 Burp Suite

Burp Suite includes functionality for sending multiple requests concurrently.

Relevant features include:

- Repeater.
- Parallel request sending.
- Request groups.
- Response comparison.
- Timing analysis.

For race condition testing, the important capability is coordinating requests rather than merely sending them quickly.

### 7.3 Turbo Intruder

Turbo Intruder is a Burp Suite extension designed for advanced HTTP request testing.

It provides more control over request scheduling and concurrency.

Relevant capabilities include:

- High-speed request generation.
- Connection management.
- Request synchronisation.
- Response analysis.
- Timing-sensitive testing.

Use conservative concurrency levels and engagement-approved limits.

### 7.4 Response analysis

Compare responses for:

- Multiple successful operations.
- Conflicting transaction identifiers.
- Unexpected state changes.
- Duplicate records.
- Inconsistent status messages.
- Differences between response and authoritative state.

### 7.5 HTTP/2 considerations

HTTP/2 supports multiplexing multiple streams over a single connection.

This can affect how requests are scheduled and processed.

However, HTTP/2 multiplexing does not automatically create a vulnerability. The application must still contain a concurrency or state-management weakness.

---

## 8. Advanced Race Condition Analysis

### 8.1 Multi-endpoint races

A race condition may involve different endpoints that modify the same resource.

For example:

```text
Endpoint A: Update account status
Endpoint B: Complete transaction
```

Assess whether both endpoints enforce the same underlying business rules.

### 8.2 Multi-user races

Some issues require two different authenticated users.

Examples:

- Two users reserving the same resource.
- Two administrators approving the same transaction.
- A user modifying a resource while another user processes it.

Use separate authorised test accounts and clearly document each actor.

### 8.3 Retry behaviour

Review how the application handles:

- Client retries.
- Network timeouts.
- Gateway retries.
- Background job retries.
- Duplicate event delivery.

A retry should not unintentionally create a second independent operation.

### 8.4 Event ordering

In event-driven applications, assess whether the system correctly handles events arriving:

- Out of order.
- More than once.
- After a state change.
- After a resource has been deleted.
- After an operation has expired.

### 8.5 Distributed consistency

Where an application uses multiple services, identify whether consistency is immediate or eventually consistent.

A temporary delay between services is not automatically a vulnerability.

Determine whether an attacker can exploit that delay to violate an intended security or business invariant.

---

## 9. Common Testing Challenges

### 9.1 False positives

Multiple successful HTTP responses do not necessarily mean multiple operations were completed.

An application may return success for duplicate requests while processing only one operation.

Always verify the final state.

### 9.2 Timing sensitivity

A vulnerability may only occur within a narrow timing window.

Testing results may vary because of:

- Network latency.
- Application load.
- Database contention.
- Thread scheduling.
- Request processing order.

### 9.3 Application-level locking

The application may already implement locking or duplicate-operation protection.

A test that fails to reproduce a race condition does not prove every related operation is safe.

### 9.4 Rate limiting

Rate limits may prevent a controlled test from reaching the relevant concurrency window.

Do not attempt to bypass production protections without explicit approval.

### 9.5 Eventual consistency

Different application components may temporarily report different states.

Determine whether the inconsistency resolves correctly or creates a lasting security impact.

### 9.6 External service dependencies

Payment providers, messaging services and other external integrations may have their own idempotency and transaction handling.

Do not assume a weakness in one component proves a weakness in another.

---

## 10. Evidence and Validation

### 10.1 Evidence requirements

Capture:

- Initial application state.
- Relevant request details.
- Number of concurrent requests.
- Request timing or synchronisation method.
- Individual responses.
- Final authoritative state.
- Relevant transaction or resource identifiers.

### 10.2 Reproduction template

```text
Finding ID:

Title:

Affected Endpoint:

Affected Feature:

Business Rule:

Initial State:

Test Account:

Concurrency Method:

Number of Requests:

Request Details:

Response Details:

Final Application State:

Expected Behaviour:

Actual Behaviour:

Demonstrated Impact:

Evidence References:

Remediation:
```

### 10.3 Demonstrating a valid finding

A strong race condition finding should demonstrate all of the following:

1. A specific application invariant exists.
2. Concurrent execution violates that invariant.
3. The unexpected result is reproducible.
4. The result has a meaningful impact.
5. The finding is not simply a response-handling artefact.

### 10.4 Avoid unnecessary impact

Do not demonstrate financial impact through actual charges or refunds unless explicitly authorised.

Use test payment environments, synthetic balances and isolated resources wherever possible.

---

## 11. Impact Assessment

Race conditions can affect several security properties.

| Impact | Example |
|---|---|
| Financial integrity | Duplicate refunds or charges |
| Data integrity | Lost or inconsistent updates |
| Authorisation | Repeated privileged operations |
| Resource allocation | Multiple owners assigned to one resource |
| Confidentiality | Incorrect access resulting from inconsistent state |
| Availability | Excessive resource consumption |
| Business process | Approval or transaction state corruption |

Severity depends on:

- The affected operation.
- Required authentication and privileges.
- Reproducibility.
- Exploitation complexity.
- Financial or operational consequences.
- Number of affected users.
- Whether the impact is persistent.

---

## 12. Remediation

### 12.1 Atomic database operations

Perform security-sensitive validation and state changes atomically where possible.

Avoid separate application-level checks that can become stale before the update occurs.

### 12.2 Database constraints

Use appropriate database constraints, including:

- Unique constraints.
- Foreign keys.
- Check constraints.
- Appropriate isolation.
- Transaction boundaries.

Application-level checks should not be the only protection against duplicate or invalid state.

### 12.3 Locking

Use appropriate concurrency controls, such as:

- Row-level locking.
- Optimistic concurrency control.
- Pessimistic locking.
- Version columns.
- Compare-and-swap operations.

The appropriate method depends on the application's architecture and workload.

### 12.4 Idempotency

For operations that may be retried, implement idempotency keys or equivalent operation tracking.

Ensure that duplicate requests return the original result rather than repeating the side effect.

### 12.5 State validation

Validate the current state immediately before performing a state-changing operation.

Reject invalid transitions.

### 12.6 Transaction integrity

Use database transactions to ensure related updates either complete together or fail together.

### 12.7 Distributed systems

For multi-service workflows, consider:

- Idempotent consumers.
- Unique event identifiers.
- Transactional outbox patterns.
- Deduplication.
- Explicit state machines.
- Compensating transactions.

Ensure that retries and delayed events cannot violate business rules.

### 12.8 Monitoring

Log security-relevant events and monitor for:

- Duplicate operations.
- Conflicting state changes.
- Repeated failed transitions.
- Unexpected transaction volumes.
- Inconsistent resource allocation.

---

## 13. Testing Checklist

### Identification

- [ ] Identify operations involving shared state.
- [ ] Identify single-use operations.
- [ ] Identify limited resources.
- [ ] Identify financial workflows.
- [ ] Identify state transitions.
- [ ] Identify background processing.

### Preparation

- [ ] Confirm explicit testing authorisation.
- [ ] Obtain isolated test accounts.
- [ ] Establish initial application state.
- [ ] Identify expected business invariants.
- [ ] Confirm concurrency limits.
- [ ] Confirm external service restrictions.

### Testing

- [ ] Assess check-then-update operations.
- [ ] Assess duplicate request handling.
- [ ] Assess limit enforcement.
- [ ] Assess transaction integrity.
- [ ] Assess resource allocation.
- [ ] Assess conflicting state transitions.
- [ ] Assess multi-user concurrency.
- [ ] Assess retry handling.
- [ ] Assess asynchronous processing.

### Validation

- [ ] Verify final application state.
- [ ] Confirm duplicate side effects.
- [ ] Confirm reproducibility.
- [ ] Rule out response-only false positives.
- [ ] Establish realistic impact.
- [ ] Preserve minimal evidence.

### Reporting

- [ ] Document the violated invariant.
- [ ] Document concurrency conditions.
- [ ] Include request and response evidence.
- [ ] Explain the business impact.
- [ ] Recommend appropriate concurrency controls.
- [ ] Retest remediation.

---

## 14. References

### PortSwigger Web Security Academy — Race Conditions

https://portswigger.net/web-security/race-conditions

### PortSwigger Research — Smashing the State Machine

https://portswigger.net/research/smashing-the-state-machine

### OWASP Web Security Testing Guide

https://owasp.org/www-project-web-security-testing-guide/

### OWASP API Security Top 10

https://owasp.org/API-Security/

### CWE-362 — Concurrent Execution Using Shared Resource with Improper Synchronization

https://cwe.mitre.org/data/definitions/362.html

### CWE-367 — Time-of-check Time-of-use Race Condition

https://cwe.mitre.org/data/definitions/367.html

### PostgreSQL — Transaction Isolation

https://www.postgresql.org/docs/current/transaction-iso.html

### Burp Suite Documentation

https://portswigger.net/burp/documentation

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
