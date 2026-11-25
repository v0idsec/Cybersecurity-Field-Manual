# Detection Testing and Validation

## Overview

Detection testing confirms that security detections identify the intended activity and behave correctly under realistic conditions.

A detection that has never been tested should not be assumed to work.

Testing should establish both whether expected activity generates an alert and whether unrelated activity is handled appropriately.

## Testing Objectives

- Verify detection logic.
- Confirm telemetry availability.
- Validate field mappings.
- Identify false positives.
- Measure detection latency.
- Confirm alert enrichment.
- Validate investigation instructions.
- Identify coverage gaps.

## Testing Methods

### Unit Testing

Tests individual detection components against known input data.

Examples:

- Event ID matching
- Command-line matching
- Field extraction
- Threshold calculations
- Time-window logic

### Integration Testing

Tests whether the complete detection pipeline works.

Validate:

- Event generation
- Event collection
- Parsing
- Normalisation
- Detection execution
- Alert generation
- Notification and routing

### Regression Testing

Confirms that changes do not break previously working detections.

Run regression tests after:

- Rule changes
- SIEM migrations
- Connector changes
- Parser changes
- Exclusion updates
- Platform upgrades

### Adversary Emulation

Uses controlled simulations to validate detection coverage for known adversary behaviours.

Examples include:

- Process execution testing
- Authentication testing
- Scheduled task creation
- Service creation
- Controlled network activity

All testing must be authorised and performed within an approved scope.

## Positive and Negative Testing

### Positive Test

A positive test produces activity that should match the detection.

Example:

A controlled test event representing a failed authentication threshold is submitted to the detection pipeline.

Expected result:

- The event is ingested.
- The detection matches.
- An alert is generated.
- The alert contains the expected context.

### Negative Test

A negative test represents activity that should not match the detection.

Expected result:

- The event is ingested.
- The detection does not generate an alert.
- No unrelated activity is incorrectly classified.

## Testing Tools

### Atomic Red Team

Provides focused tests mapped to MITRE ATT&CK techniques.

https://github.com/redcanaryco/atomic-red-team

Use only approved tests within the intended environment.

### MITRE Caldera

Adversary emulation platform for controlled security testing.

https://github.com/mitre/caldera

### Prelude Operator

Adversary emulation and security control validation.

https://www.preludesecurity.com/

### Infection Monkey

Network security testing and lateral movement simulation.

https://github.com/guardicore/monkey

Evaluate operational impact before deploying emulation tools.

## Detection Test Plan

A test plan should document:

| Field | Description |
|---|---|
| Detection | Rule being tested |
| Objective | Expected behaviour |
| Environment | Test environment |
| Preconditions | Required configuration |
| Test activity | Activity being generated |
| Expected result | Expected detection outcome |
| Actual result | Observed outcome |
| Evidence | Supporting logs and alerts |
| Result | Pass, fail or inconclusive |

## Example Test Case

### Detection: New Windows Service Installation

Objective:

Identify unexpected service installation activity.

Test requirements:

- Approved test host.
- Appropriate Windows auditing.
- SIEM ingestion confirmed.
- Detection rule deployed.

Expected telemetry:

- Security Event ID 4697, where configured.
- System Event ID 7045.

Validation:

1. Confirm the test host is in scope.
2. Generate an approved service installation event.
3. Verify event collection.
4. Confirm detection execution.
5. Review generated alert.
6. Record evidence.
7. Confirm the test service is removed where appropriate.

Do not use an unapproved production system for this test.

## Detection Latency

Measure the time between:

1. Activity occurring.
2. Event generation.
3. Event ingestion.
4. Detection execution.
5. Alert availability.

Delays may result from:

- Agent buffering
- Network interruptions
- Ingestion queues
- Parsing delays
- Scheduled rule execution
- Query window configuration

## Test Results

Classify results as:

- Pass
- Fail
- Partial
- Inconclusive
- Not tested

A passing query syntax check does not demonstrate successful detection.

## Evidence

Preserve:

- Test activity details
- Event records
- Query results
- Alert output
- Timestamps
- Relevant configuration
- Test environment
- Validation outcome

## Safety Considerations

- Obtain written approval.
- Define the test scope.
- Use isolated environments where practical.
- Avoid destructive payloads.
- Avoid uncontrolled persistence.
- Avoid real credential theft or data exfiltration.
- Coordinate with operations teams.
- Have a rollback plan.

## Further Reading

- Atomic Red Team: https://github.com/redcanaryco/atomic-red-team
- MITRE Caldera: https://caldera.mitre.org/
- MITRE ATT&CK: https://attack.mitre.org/
- Purple Team: https://github.com/scythe-io/community-threats

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
