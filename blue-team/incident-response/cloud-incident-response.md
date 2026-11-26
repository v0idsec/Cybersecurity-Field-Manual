# Cloud Incident Response

## Overview

Cloud incidents may involve compromised identities, exposed storage, unauthorised resource creation, malicious configuration changes, data access or abuse of cloud services.

Cloud investigations require an understanding of the shared responsibility model. The provider, customer and third-party service providers may each have different responsibilities.

## Common cloud incident types

- Compromised cloud administrator accounts.
- Exposed access keys or secrets.
- Unauthorised role assignments.
- Publicly exposed storage.
- Malicious application consent.
- Unauthorised virtual machine deployment.
- Cryptomining.
- Data exfiltration.
- Security group or firewall changes.
- Logging or monitoring tampering.
- Compromised CI/CD credentials.
- Container or workload compromise.
- Third-party integration compromise.

## Initial assessment

Establish:

- Which cloud provider and services are involved?
- Which tenant, subscription, project or account is affected?
- Which identities are involved?
- Is the activity ongoing?
- Are privileged roles affected?
- What resources were accessed or modified?
- Is data potentially exposed?
- Are production workloads affected?
- Are logs available and retained?
- Is the incident limited to one account or spread across the environment?

## Identity investigation

Review:

- Sign-in activity.
- MFA changes.
- New access keys.
- Service principal activity.
- Role and policy changes.
- Privileged role activation.
- Application consent.
- Session activity.
- Federated identity configuration.
- Unusual API calls.

Identify whether credentials were exposed through source code, CI/CD pipelines, endpoints or third-party services.

## Control-plane investigation

Review audit events for:

- Resource creation.
- Resource deletion.
- Role changes.
- Policy changes.
- Network configuration changes.
- Storage permission changes.
- Logging configuration changes.
- Key and secret creation.
- Snapshot operations.
- Security control modifications.

Preserve audit logs before changing or disabling affected resources.

## Data access investigation

Determine:

- Which storage resources were accessed?
- Which identities accessed them?
- What operations were performed?
- Was data downloaded or exported?
- Were access permissions changed?
- Were public access settings enabled?
- Are there signs of bulk access?
- Are data access logs available?

Do not equate an access event with confirmed exfiltration. Establish what evidence supports the conclusion.

## Containment

Potential actions:

- Revoke compromised access keys.
- Disable compromised identities.
- Revoke sessions where supported.
- Remove malicious role assignments.
- Restrict storage access.
- Disable public exposure.
- Restrict suspicious network paths.
- Suspend compromised automation.
- Restrict application consent.
- Preserve affected resource metadata.

Coordinate with service owners to avoid unintended outages.

## Eradication

- Remove unauthorised resources.
- Rotate exposed secrets.
- Correct IAM policies.
- Remove malicious application registrations.
- Patch affected workloads.
- Review CI/CD credentials.
- Restore logging and monitoring.
- Correct storage exposure.
- Review trust relationships.
- Validate infrastructure-as-code repositories.

## Recovery

- Rebuild compromised workloads.
- Restore trusted configurations.
- Rotate credentials and secrets.
- Validate IAM and network controls.
- Confirm audit logging.
- Test application functionality.
- Review data integrity.
- Increase monitoring.
- Obtain service owner approval.

## Provider engagement

Contact the cloud provider when:

- Provider-side evidence is required.
- The incident may involve provider infrastructure.
- Logs or capabilities are unavailable.
- Service abuse or account recovery is required.
- Specialist support is needed.

Use approved support channels and preserve case references.

## Cloud-specific evidence

Capture where available:

- Tenant and account identifiers.
- Resource identifiers.
- Audit events.
- Sign-in logs.
- Role assignments.
- Policy versions.
- Resource configuration.
- Storage access records.
- Network flow records.
- Key creation and rotation events.
- Deployment history.
- Relevant source control changes.

## Closure criteria

- [ ] Affected cloud accounts and resources identified.
- [ ] Compromised identities contained.
- [ ] Exposed keys and secrets rotated.
- [ ] Unauthorised permissions removed.
- [ ] Data exposure assessed.
- [ ] Resource configurations validated.
- [ ] Logging restored and verified.
- [ ] Workloads recovered.
- [ ] Residual risks documented.
- [ ] Corrective actions assigned.

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
