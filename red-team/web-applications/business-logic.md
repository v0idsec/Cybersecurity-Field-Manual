# Business Logic Vulnerability Testing

## Overview

Business logic vulnerabilities occur when an application fails to correctly enforce the rules, assumptions or workflows that govern its intended operation.

Unlike conventional injection vulnerabilities, business logic flaws often involve entirely valid requests processed in an unintended way.

An application may correctly authenticate users, validate input and enforce access controls while still allowing users to manipulate transactions, bypass workflow requirements or obtain benefits they should not receive.

Business logic testing requires understanding how an application is supposed to operate, identifying its underlying assumptions and determining whether those assumptions can be violated.

> **Testing requirement:** Conduct business logic testing using authorised accounts and controlled data. Avoid manipulating real financial transactions, customer records or production workflows without explicit approval.

---

## Table of Contents

1. [Core Concepts](#1-core-concepts)
2. [Reconnaissance and Workflow Mapping](#2-reconnaissance-and-workflow-mapping)
3. [Trust Boundaries and Assumptions](#3-trust-boundaries-and-assumptions)
4. [Workflow Manipulation](#4-workflow-manipulation)
5. [Transaction and Payment Logic](#5-transaction-and-payment-logic)
6. [Account and Identity Logic](#6-account-and-identity-logic)
7. [Input and Parameter Manipulation](#7-input-and-parameter-manipulation)
8. [Race Conditions and Concurrency](#8-race-conditions-and-concurrency)
9. [Abuse of Application Features](#9-abuse-of-application-features)
10. [Business Logic Testing Methodology](#10-business-logic-testing-methodology)
11. [Common Vulnerability Patterns](#11-common-vulnerability-patterns)
12. [Evidence and Validation](#12-evidence-and-validation)
13. [Risk and Impact Assessment](#13-risk-and-impact-assessment)
14. [Remediation Guidance](#14-remediation-guidance)
15. [Testing Checklist](#15-testing-checklist)
16. [References](#16-references)

---

## 1. Core Concepts

### 1.1 What makes a business logic vulnerability?

A business logic vulnerability exists when an application allows an action that violates its intended business rules or security requirements.

Examples include:

- Purchasing an item for an unintended price.
- Applying a discount multiple times.
- Completing a workflow without required approval.
- Accessing benefits intended for another account.
- Reusing a one-time operation.
- Modifying transaction details after approval.
- Performing an action more times than permitted.

The underlying issue is often not that the application accepts invalid input, but that it fails to recognise an invalid sequence of otherwise valid actions.

### 1.2 Business rules versus security controls

Business rules define how an application should behave.

Security controls enforce restrictions around that behaviour.

For example:

| Business rule | Security requirement |
|---|---|
| A coupon can only be redeemed once | Enforce redemption limits server-side |
| Only managers can approve expenses | Verify the user's role and authority |
| Orders cannot be modified after dispatch | Enforce transaction state |
| A user can only view their own invoices | Verify object ownership |
| Refunds require an eligible transaction | Validate transaction history |

Testing should identify where business rules are missing, inconsistently implemented or enforced only by the client.

### 1.3 Why these vulnerabilities are difficult to detect

Business logic vulnerabilities often:

- Require knowledge of application workflows.
- Depend on specific account states.
- Require multiple requests.
- Involve multiple users or roles.
- Produce legitimate-looking responses.
- Do not trigger conventional scanner findings.
- Exist across several application components.

Manual testing and application understanding are essential.

---

## 2. Reconnaissance and Workflow Mapping

Before testing business logic, understand the intended behaviour of the application.

### 2.1 Identify important workflows

Look for functionality involving:

- Registration.
- Account verification.
- Account recovery.
- Subscription management.
- Payments.
- Purchases.
- Refunds.
- Promotions.
- Approvals.
- Document processing.
- User invitations.
- Organisation management.
- Resource allocation.

Prioritise workflows involving money, sensitive information, privileges or irreversible actions.

### 2.2 Map state transitions

Document how an object changes over time.

Example: order lifecycle.

```text
Created
   |
   v
Pending Payment
   |
   v
Paid
   |
   v
Processing
   |
   v
Dispatched
   |
   v
Completed
```

Questions to investigate:

- Can a state be skipped?
- Can a previous state be restored?
- Can an action be repeated?
- Can a user modify a completed transaction?
- Are state transitions validated server-side?
- Can multiple users influence the same object?

### 2.3 Identify application actors

Map the different actors involved in each workflow.

| Actor | Potential permissions |
|---|---|
| Anonymous user | Browse, register |
| Standard user | Manage own account |
| Premium user | Access additional features |
| Manager | Approve selected operations |
| Administrator | Manage application configuration |
| External integration | Submit or update application data |

Consider whether permissions change depending on the current state of an object.

### 2.4 Establish expected behaviour

For every workflow, document:

1. Starting conditions.
2. Required permissions.
3. Expected input.
4. Expected sequence.
5. Valid state transitions.
6. Expected result.
7. Restrictions and limits.

Without a baseline, it is difficult to distinguish an actual vulnerability from intended functionality.

---

## 3. Trust Boundaries and Assumptions

Business logic vulnerabilities frequently arise when an application trusts information supplied by an untrusted party.

### 3.1 Client-side trust

Never assume that a value is trustworthy simply because it is generated or validated by the frontend.

Potentially sensitive values include:

- Prices.
- Discounts.
- Quantities.
- Account roles.
- User identifiers.
- Organisation identifiers.
- Approval states.
- Subscription levels.
- Transaction statuses.

Determine whether the backend independently validates these values.

### 3.2 Identity and ownership assumptions

Review whether the application assumes that:

- A user owns a resource because they know its identifier.
- A user belongs to an organisation because they supplied its ID.
- A request is authorised because it originated from a visible interface.
- A previous authentication step guarantees current permissions.

These assumptions should be enforced through server-side checks.

### 3.3 State assumptions

Applications may assume that a user will follow the intended workflow.

For example:

```text
Step 1: Create application
Step 2: Submit application
Step 3: Receive approval
Step 4: Access approved functionality
```

Determine whether the backend independently verifies the required state at each step.

### 3.4 Time and expiry assumptions

Review workflows involving:

- Temporary access.
- Verification links.
- One-time offers.
- Session expiry.
- Reservation windows.
- Approval deadlines.
- Time-limited transactions.

Determine whether expiry and validity are enforced consistently.

---

## 4. Workflow Manipulation

Workflow manipulation occurs when an attacker changes the expected order or conditions of application operations.

### 4.1 Out-of-order execution

Assess whether later workflow actions can be performed before earlier requirements are satisfied.

Examples:

- Submitting an application without completing mandatory fields.
- Accessing a confirmation endpoint before approval.
- Completing an order before payment.
- Invoking an administrative action before a required verification step.

### 4.2 Skipping workflow steps

Identify whether intermediate steps enforce security requirements or merely provide frontend navigation.

A workflow may appear sequential while the backend exposes independent endpoints for each operation.

### 4.3 Repeating completed actions

Review whether operations intended to happen once can be repeated.

Examples:

- Redeeming a single-use promotion.
- Claiming a one-time reward.
- Submitting a refund request.
- Completing an account verification action.
- Activating an invitation.

### 4.4 Reversing workflow state

Assess whether completed operations can be reversed or modified in ways the business process does not permit.

Examples:

- Reopening a completed transaction.
- Modifying an approved application.
- Cancelling a dispatched order.
- Reverting an account verification state.

### 4.5 Workflow validation matrix

| Test | Expected control |
|---|---|
| Skip required step | Backend rejects invalid transition |
| Repeat completed action | Duplicate operation prevented |
| Reverse completed state | Transition restricted |
| Submit incomplete workflow | Required conditions enforced |
| Change workflow owner | Ownership revalidated |
| Change actor role | Permissions revalidated |

---

## 5. Transaction and Payment Logic

Transaction-related vulnerabilities can have significant financial consequences.

Only perform these tests using approved test environments, test payment methods and explicitly authorised accounts.

### 5.1 Price manipulation

Assess whether transaction values are calculated and validated by the backend.

Potentially relevant fields:

- Unit price.
- Quantity.
- Discount.
- Shipping cost.
- Tax.
- Currency.
- Total amount.

The server should derive authoritative values from trusted records rather than accept client-supplied totals.

### 5.2 Discount and promotion abuse

Review:

- Single-use restrictions.
- Eligibility conditions.
- Expiry enforcement.
- User-specific restrictions.
- Stacking rules.
- Minimum purchase requirements.
- Promotion ownership.

Determine whether restrictions are enforced consistently across the relevant endpoints.

### 5.3 Payment state validation

Assess whether the application correctly distinguishes:

- Payment initiated.
- Payment pending.
- Payment authorised.
- Payment captured.
- Payment failed.
- Payment refunded.

A frontend success message is not proof that the backend has verified a successful payment.

### 5.4 Refund logic

Review:

- Refund eligibility.
- Refund limits.
- Duplicate refund handling.
- Original transaction ownership.
- Partial refund calculations.
- Refund approval requirements.

Use test transactions and do not trigger actual financial transfers without explicit approval.

### 5.5 Currency and rounding

Assess whether currency conversion, rounding and decimal precision are handled consistently.

Potential issues include:

- Different rounding between frontend and backend.
- Incorrect decimal precision.
- Currency mismatch.
- Negative values.
- Integer overflow or unexpected numeric types.

### 5.6 Transaction integrity

Verify that important transaction attributes cannot be changed after the relevant approval or payment state has been established.

---

## 6. Account and Identity Logic

### 6.1 Account linking

Review workflows that link multiple identities or external accounts.

Potential issues:

- Incorrect ownership verification.
- Linking an account already associated with another user.
- Email address trust assumptions.
- Insecure account merging.
- Inconsistent identity provider validation.

### 6.2 Email change workflows

Assess:

- Re-authentication requirements.
- Verification of the new address.
- Notification of the previous address.
- Session invalidation.
- Recovery implications.

### 6.3 User invitation workflows

Review:

- Invitation expiry.
- Invitation reuse.
- Organisation membership.
- Inviter permissions.
- Role assignment.
- Acceptance by a different identity.

### 6.4 Subscription and entitlement logic

Determine whether premium functionality is controlled by authoritative server-side entitlement checks.

Review:

- Subscription status.
- Trial expiry.
- Cancellation.
- Upgrade and downgrade transitions.
- Account ownership.
- Feature entitlement consistency.

### 6.5 Role and privilege assignment

Assess whether users can influence role assignment through:

- Registration parameters.
- Profile updates.
- Invitation acceptance.
- Organisation membership.
- Account recovery.
- Administrative workflows.

---

## 7. Input and Parameter Manipulation

Business logic testing should include values that are syntactically valid but semantically unexpected.

### 7.1 Numeric values

Review how the application handles:

- Zero.
- Negative numbers.
- Large numbers.
- Decimal values.
- Unexpected precision.
- Boundary values.
- Missing values.

### 7.2 Identifiers

Assess whether changing identifiers affects:

- Ownership.
- Organisation membership.
- Transaction relationships.
- Resource permissions.
- Workflow participants.

Identifier manipulation should be considered alongside authorisation testing.

### 7.3 Boolean and state values

Review client-supplied flags such as:

- `isAdmin`
- `isApproved`
- `isVerified`
- `isPaid`
- `isActive`
- `isPremium`

These values must not be trusted as proof of server-side state.

### 7.4 Mass assignment

Assess whether unexpected properties supplied during object updates are accepted and persisted.

Examples include role, ownership, approval or entitlement attributes.

### 7.5 Duplicate and conflicting parameters

Review whether repeated or conflicting values are interpreted differently by:

- Reverse proxies.
- Application frameworks.
- Backend services.
- Validation layers.

---

## 8. Race Conditions and Concurrency

Race conditions occur when application behaviour depends on the timing or ordering of concurrent operations.

### 8.1 Common targets

- Single-use coupons.
- Inventory reservations.
- Account balance operations.
- One-time rewards.
- Transaction approval.
- Ticket allocation.
- Registration limits.

### 8.2 Time-of-check to time-of-use

A TOCTOU issue occurs when an application checks a condition and later uses the result without ensuring the condition remains valid.

For example:

```text
Request A: Check available inventory
Request B: Check available inventory
Request A: Reserve final item
Request B: Reserve final item
```

If the application does not perform an atomic reservation, both requests may succeed.

### 8.3 Testing considerations

Review:

- Atomicity.
- Transaction isolation.
- Duplicate request handling.
- Idempotency.
- Locking.
- State revalidation.
- Concurrent request behaviour.

Use isolated test resources and approved concurrency limits.

**Related reference:** `race-conditions.md`

---

## 9. Abuse of Application Features

Not all business logic weaknesses involve bypassing a direct security control. Some involve using legitimate functionality in unintended ways.

### 9.1 Resource consumption

Review whether functionality can be abused to consume disproportionate:

- Storage.
- Processing capacity.
- API quota.
- Email delivery.
- Third-party service usage.

Avoid testing in ways that cause service disruption.

### 9.2 Referral and reward systems

Assess:

- Referral eligibility.
- Reward issuance.
- Duplicate account restrictions.
- Self-referral controls.
- Reward expiry.
- Referral ownership.

### 9.3 Search and filtering

Review whether filters, sorting and search parameters can expose information beyond intended access boundaries.

### 9.4 Export and reporting

Assess whether generated reports respect the same ownership and permission rules as the underlying records.

### 9.5 Notifications and messaging

Review whether users can:

- Trigger messages to unintended recipients.
- Manipulate notification ownership.
- Abuse invitation or recovery workflows.
- Cause sensitive information to be disclosed.

---

## 10. Business Logic Testing Methodology

A repeatable approach makes business logic testing more effective.

### Step 1: Understand the feature

Use the application normally and document its expected behaviour.

### Step 2: Identify assumptions

Determine what the application appears to trust.

Examples:

- The user owns the requested object.
- The transaction has been paid.
- The user is eligible for a discount.
- The workflow has been approved.

### Step 3: Identify enforcement points

Determine where each requirement should be checked.

Consider whether the control is enforced:

- In the frontend.
- At the API gateway.
- In the application backend.
- In the database.
- By an external service.

### Step 4: Form a test hypothesis

Example:

> The application may allow a user to repeat a one-time reward claim because the backend does not enforce unique redemption.

### Step 5: Establish preconditions

Use controlled accounts and test-owned resources.

Record the expected initial state.

### Step 6: Perform a controlled test

Change one relevant condition at a time.

Avoid combining multiple variables unless investigating an interaction between them.

### Step 7: Observe the result

Compare the actual behaviour with the expected business rule.

### Step 8: Validate impact

Determine whether the behaviour creates a meaningful security or business impact.

### Step 9: Capture evidence

Preserve the minimum evidence needed to demonstrate the issue.

### Step 10: Document remediation

Identify the underlying control that should enforce the business rule.

---

## 11. Common Vulnerability Patterns

| Pattern | Description | Potential impact |
|---|---|---|
| Workflow bypass | Required steps can be skipped | Unauthorised actions |
| State manipulation | Application state can be changed improperly | Transaction abuse |
| Duplicate action | One-time operation can be repeated | Financial or resource loss |
| Price manipulation | Transaction values are not independently validated | Financial impact |
| Discount abuse | Promotion restrictions are inconsistently enforced | Financial impact |
| Race condition | Concurrent requests bypass a limit | Duplicate allocation or transaction |
| Trust boundary failure | Client-controlled data is treated as authoritative | Privilege or integrity compromise |
| Entitlement bypass | Premium functionality is accessible without eligibility | Unauthorised access |
| Invitation abuse | Membership or role assignment can be manipulated | Unauthorised access |
| Account linking flaw | Identities can be incorrectly associated | Account compromise |
| Approval bypass | Required approval is not enforced | Unauthorised transactions |
| Resource abuse | Legitimate functionality can be used excessively | Cost or availability impact |

---

## 12. Evidence and Validation

### 12.1 Required evidence

A business logic finding should demonstrate:

- The intended business rule.
- The initial application state.
- The test account and role.
- The relevant request or workflow.
- The unexpected outcome.
- The security or business impact.

### 12.2 Reproduction template

```text
Finding ID:

Feature / Workflow:

Affected Endpoint:

Business Rule:

Expected Behaviour:

Actual Behaviour:

Initial State:

Test Account / Role:

Preconditions:

Reproduction Steps:

Evidence:

Impact:

Remediation:
```

### 12.3 Evidence quality

Avoid reporting findings based only on:

- An unexpected HTTP status.
- A changed frontend value.
- A theoretical workflow bypass.
- An unverified assumption about business rules.

Where possible, confirm the resulting state through an independent application view or authorised test account.

### 12.4 Demonstrating impact

Use the least intrusive method that proves the issue.

For example, demonstrate access to a second test account's synthetic record rather than attempting to access real customer information.

---

## 13. Risk and Impact Assessment

Business logic vulnerabilities can have impacts beyond conventional technical compromise.

Consider:

| Impact category | Example |
|---|---|
| Financial | Unauthorised discounts or refunds |
| Confidentiality | Access to another user's records |
| Integrity | Unauthorised modification of transactions |
| Availability | Excessive resource allocation |
| Privilege | Unauthorised role or entitlement changes |
| Compliance | Exposure of regulated information |
| Operational | Bypassing required business approvals |

### Severity considerations

Assess:

- Whether exploitation requires authentication.
- Whether a specific role is required.
- Whether the attack can be repeated.
- Whether exploitation requires user interaction.
- Whether the impact is limited to one account or affects multiple users.
- Whether exploitation creates direct financial consequences.
- Whether the issue can be exploited remotely.

A business logic issue should not automatically be rated Critical or High simply because it involves money or workflow manipulation. Base severity on the demonstrated impact and realistic exploitation conditions.

---

## 14. Remediation Guidance

### 14.1 Enforce business rules server-side

Never rely on frontend validation for security-critical decisions.

### 14.2 Validate state transitions

Implement explicit state machines where appropriate.

Only permit transitions that are valid for the current state and actor.

### 14.3 Use authoritative data

Calculate prices, discounts, permissions and entitlements using trusted server-side records.

### 14.4 Enforce ownership and authorisation

Validate access to every object and operation independently.

### 14.5 Implement transaction integrity

Use appropriate database transactions and atomic operations for sensitive workflows.

### 14.6 Prevent duplicate operations

Use idempotency controls, unique constraints and server-side operation tracking where appropriate.

### 14.7 Apply limits consistently

Enforce quotas, redemption limits and eligibility requirements at the backend.

### 14.8 Log security-relevant activity

Record important events such as:

- Role changes.
- Approval actions.
- Refunds.
- Account linking.
- Entitlement changes.
- Sensitive workflow transitions.

Logs should support investigation without unnecessarily storing secrets or sensitive personal data.

---

## 15. Testing Checklist

### Workflow analysis

- [ ] Identify important business workflows.
- [ ] Document expected state transitions.
- [ ] Identify actors and permissions.
- [ ] Identify sensitive operations.
- [ ] Identify one-time actions.
- [ ] Identify approval requirements.

### Trust boundaries

- [ ] Identify client-controlled security values.
- [ ] Review server-side validation.
- [ ] Review ownership assumptions.
- [ ] Review tenant boundaries.
- [ ] Review state enforcement.

### Workflow manipulation

- [ ] Test out-of-order execution.
- [ ] Test skipped steps.
- [ ] Test repeated operations.
- [ ] Test invalid state transitions.
- [ ] Test workflow reversal.
- [ ] Test ownership changes.

### Transaction logic

- [ ] Review price calculations.
- [ ] Review discount restrictions.
- [ ] Review payment state handling.
- [ ] Review refund logic.
- [ ] Review transaction modification.
- [ ] Review currency and rounding.

### Identity and entitlement

- [ ] Review account linking.
- [ ] Review email changes.
- [ ] Review invitations.
- [ ] Review role assignment.
- [ ] Review subscription state.
- [ ] Review entitlement enforcement.

### Concurrency and abuse

- [ ] Identify race condition opportunities.
- [ ] Review duplicate request handling.
- [ ] Review idempotency.
- [ ] Review resource consumption limits.
- [ ] Review referral and reward systems.
- [ ] Review export and reporting permissions.

### Reporting

- [ ] Establish the intended business rule.
- [ ] Confirm the actual control failure.
- [ ] Reproduce using test data.
- [ ] Demonstrate realistic impact.
- [ ] Capture minimal evidence.
- [ ] Provide actionable remediation.

---

## 16. References

### OWASP Web Security Testing Guide

https://owasp.org/www-project-web-security-testing-guide/

### OWASP Application Security Verification Standard

https://owasp.org/www-project-application-security-verification-standard/

### OWASP Business Logic Abuse

https://owasp.org/www-community/vulnerabilities/Business_logic_vulnerability

### OWASP API Security Top 10

https://owasp.org/API-Security/

### PortSwigger Web Security Academy — Business Logic Vulnerabilities

https://portswigger.net/web-security/logic-flaws

### CWE — Common Weakness Enumeration

https://cwe.mitre.org/

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
