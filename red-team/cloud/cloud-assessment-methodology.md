# Cloud Assessment Methodology

## Overview

A cloud security assessment evaluates the security configuration, access controls, infrastructure and monitoring capabilities of a cloud environment.

The assessment should establish how the environment is structured, who can access it, what is exposed externally and whether security controls are appropriately configured.

## 1. Engagement Preparation

Before beginning, establish the assessment boundaries.

### Scope

Record:

| Item | Description |
|---|---|
| Provider | AWS, Azure or GCP |
| Account / tenant / project | Approved identifiers |
| Subscriptions | Azure subscription scope |
| Regions | Approved geographic regions |
| Workloads | VMs, containers, serverless and databases |
| Identity systems | IAM, Entra ID or Cloud Identity |
| External services | Approved public-facing assets |
| Third parties | Explicitly approved integrations |
| Testing level | Read-only, configuration changes or controlled exploitation |

### Confirm Testing Permissions

Cloud environments often contain production systems and shared services.

Obtain explicit approval before:
- Modifying IAM policies.
- Creating or deleting resources.
- Changing network security rules.
- Accessing sensitive data.
- Testing credential validity.
- Executing code within workloads.
- Performing denial-of-service testing.
- Conducting phishing or identity-based attacks.
- Testing cross-account or cross-tenant access.

Provider policies may impose additional restrictions.

## 2. Establish the Assessment Context

Identify:
- Cloud provider.
- Account, tenant or project identifiers.
- Organisation structure.
- Administrative contacts.
- Identity provider.
- Primary regions.
- Known workloads.
- Security monitoring services.
- Existing cloud security documentation.

Determine whether the environment is:
- Single-account or multi-account.
- Centrally managed.
- Hybrid cloud.
- Federated with an external identity provider.
- Integrated with on-premises Active Directory.

## 3. Initial Discovery

Begin with read-only enumeration.

Identify:
- Accounts and subscriptions.
- Projects and resource groups.
- Regions in use.
- Virtual machines.
- Storage services.
- Managed databases.
- Network resources.
- Serverless services.
- Container platforms.
- Identity and access configuration.
- Logging and security services.

Build an inventory of resources and their relationships.

## 4. Identity and Access Assessment

Identity is a major control plane for cloud environments.

Review:
- Users and groups.
- Roles and policies.
- Administrative privileges.
- Service accounts.
- Managed identities.
- Federation.
- Cross-account access.
- Temporary credentials.
- Access key age and usage.
- Privilege boundaries.

Identify:
- Excessive permissions.
- Unnecessary administrators.
- Unused identities.
- Overly broad trust relationships.
- Long-lived credentials.
- Weak separation of duties.

Refer to [Cloud Identity and Access](cloud-identity-and-access.md).

## 5. Infrastructure Assessment

Review cloud resources for insecure configuration.

Examples:
- Publicly accessible management services.
- Unrestricted inbound firewall rules.
- Exposed databases.
- Insecure load balancer configuration.
- Unnecessary public IP addresses.
- Weak segmentation.
- Unprotected management endpoints.
- Insecure metadata service configuration.

Refer to [Cloud Networking and External Exposure](cloud-networking-and-external-exposure.md).

## 6. Storage and Data Assessment

Review:
- Public access settings.
- Bucket and container policies.
- Access control lists.
- Encryption configuration.
- Data retention.
- Backup exposure.
- Cross-account access.
- Logging and access monitoring.

Do not download or inspect sensitive customer data unless explicitly authorised.

Refer to [Cloud Storage and Data Exposure](cloud-storage-and-data-exposure.md).

## 7. Secrets and Credential Assessment

Review:
- API keys.
- Access keys.
- Service principal secrets.
- Application credentials.
- Certificates.
- Tokens.
- Secret vault permissions.
- Workload identity configuration.

Look for:
- Long-lived credentials.
- Secrets embedded in source code.
- Secrets stored in environment variables.
- Excessive secret access.
- Missing rotation.
- Inadequate audit logging.

Refer to [Cloud Secrets and Credential Security](cloud-secrets-and-credential-security.md).

## 8. Logging and Detection

Determine whether security-relevant activity is recorded and monitored.

Review:
- Control-plane audit logs.
- Identity events.
- Authentication activity.
- Resource changes.
- Network flow logs.
- Storage access logs.
- Threat detection alerts.
- Centralised log collection.
- Retention and access controls.

Examples of relevant services:

| Provider | Logging / Detection |
|---|---|
| AWS | CloudTrail, GuardDuty, Security Hub |
| Azure | Azure Monitor, Activity Log, Defender for Cloud |
| GCP | Cloud Audit Logs, Security Command Centre, Cloud Logging |

## 9. Controlled Validation

Validate findings using the least intrusive method available.

Preferred order:

1. Review configuration.
2. Compare against provider security guidance.
3. Confirm effective permissions.
4. Validate exposure through approved metadata or test resources.
5. Perform a controlled proof of concept only where required.

Avoid using real customer data as proof.

A finding should demonstrate the security weakness without creating unnecessary impact.

## 10. Risk Assessment

Consider:

- Resource criticality.
- Data sensitivity.
- External accessibility.
- Required privileges.
- Exploitability.
- Potential business impact.
- Blast radius.
- Existing security controls.
- Confidence in the finding.

A publicly accessible resource is not automatically vulnerable. Assess whether access is intentional and whether the exposed data or service creates risk.

## 11. Reporting

Each finding should contain:

- Title.
- Severity.
- Affected account, subscription or project.
- Resource identifier.
- Relevant configuration.
- Evidence.
- Impact.
- Reproduction steps.
- Remediation.
- References.
- Validation limitations.

Include provider-specific resource identifiers so administrators can locate the affected configuration.

## 12. Post-Assessment

Confirm:
- Temporary test resources have been removed, where applicable.
- Temporary permissions have been revoked.
- Test credentials have been invalidated.
- Configuration changes have been reversed.
- Evidence has been securely retained.
- Sensitive data has been handled appropriately.
- Findings have been delivered through approved channels.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
