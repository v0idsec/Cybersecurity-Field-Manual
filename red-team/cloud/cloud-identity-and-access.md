# Cloud Identity and Access

## Overview

Cloud identity and access management controls who can access cloud resources, what actions they can perform and which identities workloads can assume.

Identity compromise is a significant cloud security risk because cloud permissions often provide access to infrastructure, data, secrets and administrative control planes.

This guide covers identity assessment across AWS, Azure and GCP.

## 1. Identity Types

Cloud environments commonly use several identity types.

| Identity | Description |
|---|---|
| Human user | Person accessing cloud resources |
| Group | Collection of users assigned shared permissions |
| Role | Set of permissions that can be assigned or assumed |
| Service account | Non-human identity used by workloads |
| Service principal | Application identity in Microsoft Entra ID |
| Managed identity | Azure-managed workload identity |
| Workload identity | Identity assigned to an application or workload |
| Federated identity | Identity authenticated through an external identity provider |

Identify which identity types exist and how they are managed.

## 2. Permission Models

Cloud providers use different permission models.

| Provider | Primary model |
|---|---|
| AWS | IAM users, groups, roles and policies |
| Azure | Microsoft Entra ID and Azure RBAC |
| GCP | IAM principals, roles and policies |

Understand the distinction between:
- Authentication — establishing who or what is requesting access.
- Authorisation — determining which actions are permitted.
- Federation — trusting an external identity provider.
- Delegation — allowing one identity to act with another identity's permissions.

## 3. Excessive Permissions

Look for permissions that exceed operational requirements.

Examples:
- Full administrative access assigned unnecessarily.
- Wildcard actions across all resources.
- Subscription-wide or project-wide roles where resource-level access is sufficient.
- Unrestricted service account impersonation.
- Excessive application permissions.
- Broad cross-account trust.

### Permission Review Checklist

- [ ] Are privileged roles assigned only where required?
- [ ] Are permissions scoped to appropriate resources?
- [ ] Are unused roles removed?
- [ ] Are service identities restricted?
- [ ] Are cross-account relationships justified?
- [ ] Are administrative actions monitored?
- [ ] Are temporary permissions used where possible?

## 4. AWS IAM

### Important Concepts

- Identity-based policies.
- Resource-based policies.
- Trust policies.
- Permission boundaries.
- Service control policies.
- Session policies.
- Role assumption.

### Review Permissions

```bash
aws iam list-users
aws iam list-groups
aws iam list-roles
aws iam list-policies --scope Local
```

Review a role's trust policy:

```bash
aws iam get-role --role-name ROLE_NAME
```

Review attached policies:

```bash
aws iam list-attached-role-policies --role-name ROLE_NAME
```

Review inline policies:

```bash
aws iam list-role-policies --role-name ROLE_NAME
```

### High-Risk Permissions

Review permissions involving:
- IAM policy modification.
- Role creation and assumption.
- Access key creation.
- Trust policy modification.
- Security control modification.
- Resource policy modification.

A permission should be evaluated in combination with its resource scope and applicable conditions.

### Cross-Account Access

Review:
- Trusted account identifiers.
- External ID conditions.
- Federated principals.
- Service principals.
- Role session restrictions.

An overly broad trust policy can allow unintended identities to assume a role.

## 5. Microsoft Entra ID and Azure RBAC

### Important Concepts

- Users.
- Groups.
- Directory roles.
- Service principals.
- App registrations.
- Managed identities.
- Conditional Access.
- Azure RBAC.

Directory roles and Azure resource roles are different permission systems.

An identity may have substantial directory permissions without holding an Azure subscription role, or vice versa.

### Review Role Assignments

```bash
az role assignment list --all --output table
```

Review directory roles using Microsoft Graph PowerShell or the approved Entra administration interface.

Assess:
- Global Administrator assignments.
- Privileged Role Administrator assignments.
- Application Administrator assignments.
- Privileged Authentication Administrator assignments.
- Subscription Owner assignments.
- User Access Administrator assignments.

### Application Permissions

Review:
- Delegated API permissions.
- Application API permissions.
- Admin consent.
- Credential expiry.
- Service principal role assignments.

Application permissions can operate independently of an interactive user's privileges.

### Managed Identities

Review:
- System-assigned identities.
- User-assigned identities.
- Assigned Azure roles.
- Workload access requirements.

Avoid granting broad subscription-level access to workload identities when narrower resource permissions are sufficient.

## 6. GCP IAM

### Important Concepts

- Basic roles.
- Predefined roles.
- Custom roles.
- Service accounts.
- IAM policies.
- Service account impersonation.
- Workload Identity Federation.

### Review Project Permissions

```bash
gcloud projects get-iam-policy PROJECT_ID
```

List service accounts:

```bash
gcloud iam service-accounts list
```

Review service account IAM policies:

```bash
gcloud iam service-accounts get-iam-policy SERVICE_ACCOUNT_EMAIL
```

Assess:
- Owner and Editor assignments.
- Service Account Token Creator.
- Service Account User.
- Project IAM Admin.
- Broad custom roles.
- Unnecessary service account impersonation.

## 7. Privilege Escalation Assessment

Cloud privilege escalation occurs when an identity can obtain permissions beyond its intended access.

Potential risk areas include:
- Permission modification.
- Role assumption.
- Service account impersonation.
- Application credential management.
- Workload identity assignment.
- Trust relationship modification.
- Policy attachment.
- Administrative API access.

### Assessment Method

1. Identify the current identity.
2. Enumerate effective permissions.
3. Identify administrative capabilities.
4. Review trust and delegation relationships.
5. Identify identities and resources the principal can influence.
6. Determine whether those capabilities create an unintended privilege path.
7. Validate using policy analysis or an approved test identity.
8. Document the path and its limitations.

Do not modify production permissions or assume privileged roles merely to prove a theoretical escalation path.

## 8. Federation and External Identity Providers

Federation allows identities from another identity provider to access cloud resources.

Review:
- Trusted identity providers.
- Issuer and audience restrictions.
- Subject matching.
- Token lifetime.
- Conditional access requirements.
- Role assignment scope.
- External organisation trust.

Weak federation conditions may allow unintended external identities to obtain cloud access.

## 9. Credential Lifecycle

Review:
- Credential creation.
- Credential ownership.
- Last-used information.
- Rotation requirements.
- Expiry.
- Revocation procedures.
- Emergency access.
- Service account key management.

Prefer:
- Short-lived credentials.
- Managed identities.
- Workload identity federation.
- Hardware-backed authentication for privileged users.
- Strong MFA.
- Privileged access workflows.

Avoid unnecessary long-lived access keys and application secrets.

## 10. Reporting

For each identity finding, document:
- Principal identifier.
- Provider and account context.
- Assigned role or policy.
- Resource scope.
- Effective capability.
- Potential impact.
- Evidence.
- Recommended least-privilege remediation.

Never include passwords, private keys, tokens or complete credential material in reports.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
