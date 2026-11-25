# Cloud Security Assessment

## Overview

Cloud security assessments evaluate the security posture of cloud-hosted infrastructure, applications, identities, data and services.

Cloud environments introduce security considerations that differ from traditional on-premises infrastructure, including:
- Identity-based access control.
- Publicly exposed storage and services.
- Cloud-specific network controls.
- API-driven infrastructure management.
- Temporary credentials and workload identities.
- Misconfigured security services.
- Shared responsibility between provider and customer.

This section covers security assessment techniques for AWS, Microsoft Azure and Google Cloud Platform (GCP).

## Contents

| Resource | Description |
|---|---|
| [Cloud Assessment Methodology](cloud-assessment-methodology.md) | Engagement planning, discovery, assessment and validation |
| [AWS Security Assessment](aws-security-assessment.md) | AWS account, services, IAM and infrastructure assessment |
| [Azure Security Assessment](azure-security-assessment.md) | Azure resources, Entra ID and infrastructure assessment |
| [GCP Security Assessment](gcp-security-assessment.md) | GCP projects, IAM and cloud infrastructure assessment |
| [Cloud Identity and Access](cloud-identity-and-access.md) | Roles, permissions, service identities and privilege analysis |
| [Cloud Storage and Data Exposure](cloud-storage-and-data-exposure.md) | Public storage, data access and exposure assessment |
| [Cloud Networking and External Exposure](cloud-networking-and-external-exposure.md) | Cloud networks, security controls and exposed services |
| [Cloud Secrets and Credential Security](cloud-secrets-and-credential-security.md) | Keys, secrets, tokens and credential management |
| [Cloud Tools and Command Reference](cloud-tools-and-command-reference.md) | Common cloud security tools and CLI references |

## Cloud Providers

| Provider | Core services |
|---|---|
| AWS | IAM, EC2, S3, Lambda, CloudTrail, GuardDuty, VPC |
| Microsoft Azure | Entra ID, Virtual Machines, Storage Accounts, Key Vault, NSGs, Defender for Cloud |
| Google Cloud | IAM, Compute Engine, Cloud Storage, Secret Manager, VPC, Cloud Logging |

## Assessment Areas

### Identity and Access
- Excessive permissions.
- Privilege escalation paths.
- Overly permissive roles.
- Service identities.
- Long-lived credentials.
- External identity federation.

### Infrastructure
- Publicly exposed services.
- Insecure network rules.
- Unrestricted administrative access.
- Misconfigured firewalls.
- Insecure management interfaces.

### Data Security
- Public storage.
- Excessive data access.
- Weak encryption configuration.
- Exposed backups.
- Inadequate retention controls.

### Monitoring and Detection
- Audit logging.
- Security alerting.
- Identity activity monitoring.
- Cloud threat detection.
- Centralised log collection.

### Workload Security
- Virtual machines.
- Containers.
- Serverless functions.
- Managed databases.
- Application identities.
- Secrets management.

## Core Assessment Principles

1. Confirm the account, subscription or project is in scope.
2. Establish the authorised level of access.
3. Begin with read-only discovery wherever possible.
4. Avoid modifying production resources without approval.
5. Do not access or extract customer data unnecessarily.
6. Validate findings with minimal impact.
7. Record the exact resource, identity and configuration involved.
8. Include provider-specific remediation guidance.

## Shared Responsibility

Cloud providers secure the underlying cloud platform, but customers remain responsible for many aspects of their deployments.

The exact division of responsibility depends on the service model.

For example:
- AWS manages the underlying infrastructure, while customers configure IAM, workloads and data access.
- Azure manages the cloud platform, while customers configure identities, subscriptions, resources and workloads.
- GCP manages the underlying platform, while customers configure projects, IAM, workloads and data.

Never assume that a managed cloud service automatically provides secure customer configuration.

## Authorisation

Cloud assessments can affect production systems and third-party infrastructure.

Before testing, confirm:
- Approved accounts, subscriptions and projects.
- Permitted regions.
- Approved resource types.
- Whether identity testing is authorised.
- Whether exploitation is permitted.
- Whether data access is permitted.
- Whether changes to cloud configuration are allowed.
- Provider-specific testing requirements.

Cloud provider policies and testing restrictions must be considered alongside the engagement rules of engagement.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
