# Google Cloud Platform Security Assessment

## Overview

Google Cloud Platform (GCP) assessments examine the security of projects, identities, infrastructure, storage and managed services.

Common assessment areas include:
- Cloud IAM.
- Service accounts.
- Compute Engine.
- Cloud Storage.
- VPC firewall rules.
- Cloud SQL.
- Secret Manager.
- Cloud Audit Logs.
- Security Command Centre.

All assessment activity must be limited to approved organisations, folders, projects and resources.

## 1. Establish Project Context

Review the active account:

```bash
gcloud auth list
```

Review the active project:

```bash
gcloud config get-value project
```

List accessible projects:

```bash
gcloud projects list
```

Select an approved project:

```bash
gcloud config set project PROJECT_ID
```

Confirm the active configuration before continuing.

## 2. IAM Assessment

Review project IAM policy:

```bash
gcloud projects get-iam-policy PROJECT_ID
```

List service accounts:

```bash
gcloud iam service-accounts list
```

Review service account details:

```bash
gcloud iam service-accounts describe SERVICE_ACCOUNT_EMAIL
```

Review IAM roles:

```bash
gcloud iam roles list
```

Assess:
- Primitive roles.
- Custom roles.
- Excessive project permissions.
- Service account privileges.
- Unnecessary service account keys.
- Cross-project access.
- External identity federation.

### High-Risk Roles

Review assignments involving:
- Owner.
- Editor.
- Service Account Admin.
- Service Account Token Creator.
- Service Account User.
- Project IAM Admin.
- Organization Admin.

These roles have different capabilities and should be assessed in context.

## 3. Service Account Assessment

Service accounts allow applications and workloads to access GCP resources.

Review:
- Attached roles.
- Key usage.
- Key age.
- Workload identity configuration.
- Cross-project access.
- Service account impersonation permissions.

List service account keys:

```bash
gcloud iam service-accounts keys list \
  --iam-account SERVICE_ACCOUNT_EMAIL
```

Do not retrieve private key material or use discovered credentials.

Prefer workload identity and short-lived credentials over unmanaged long-lived keys.

## 4. Compute Engine Assessment

List instances:

```bash
gcloud compute instances list
```

Review a specific instance:

```bash
gcloud compute instances describe INSTANCE_NAME \
  --zone ZONE
```

Assess:
- External IP addresses.
- Network tags.
- Service account attachments.
- Disk encryption.
- Firewall exposure.
- Metadata configuration.
- OS Login.
- Shielded VM configuration.
- Logging and monitoring.

## 5. VPC and Firewall Assessment

List VPC networks:

```bash
gcloud compute networks list
```

List firewall rules:

```bash
gcloud compute firewall-rules list
```

Review a specific rule:

```bash
gcloud compute firewall-rules describe RULE_NAME
```

Look for:
- Unrestricted ingress.
- Broad source ranges.
- Public management access.
- Unnecessary exposed ports.
- Excessive target tags.
- Overly broad service account targeting.

Assess effective connectivity rather than relying solely on an individual firewall rule.

## 6. Cloud Storage Assessment

List buckets:

```bash
gcloud storage buckets list
```

Review bucket configuration:

```bash
gcloud storage buckets describe gs://BUCKET_NAME
```

Review IAM policy:

```bash
gcloud storage buckets get-iam-policy gs://BUCKET_NAME
```

Assess:
- Public principals.
- Uniform bucket-level access.
- Public access prevention.
- Retention policies.
- Encryption configuration.
- Logging.
- Cross-project access.

Do not list or download sensitive objects unless explicitly authorised.

## 7. Cloud SQL Assessment

List database instances:

```bash
gcloud sql instances list
```

Review an instance:

```bash
gcloud sql instances describe INSTANCE_NAME
```

Assess:
- Public IP configuration.
- Authorised networks.
- Private IP connectivity.
- Backup configuration.
- Encryption.
- Database flags.
- Maintenance settings.
- Logging.

## 8. Secret Manager

List secrets:

```bash
gcloud secrets list
```

Review secret metadata:

```bash
gcloud secrets describe SECRET_NAME
```

Review IAM policy:

```bash
gcloud secrets get-iam-policy SECRET_NAME
```

Assess:
- Who can access secret versions.
- Whether workload identities have excessive access.
- Secret rotation practices.
- Audit logging.
- Cross-project access.

Do not access secret payloads unless the engagement explicitly requires it.

## 9. Audit Logging and Security Monitoring

Review project audit configuration:

```bash
gcloud projects get-iam-policy PROJECT_ID
```

Audit logging is configured through IAM audit configurations and Cloud Logging.

Review:
- Admin Activity logs.
- Data Access logs.
- System Event logs.
- Policy Denied logs.
- Log sinks.
- Retention settings.
- Security Command Centre findings.

Data Access logging may not be enabled for every service by default.

## 10. Common Security Issues

| Issue | Potential impact |
|---|---|
| Excessive project roles | Broad resource access |
| Overprivileged service accounts | Workload compromise |
| Public storage buckets | Data exposure |
| Unrestricted firewall rules | Network exposure |
| Long-lived service account keys | Credential compromise |
| Public database access | Unauthorised database access |
| Missing audit logs | Reduced investigation capability |
| Unrestricted service account impersonation | Unauthorised identity use |

## 11. Assessment Tools

- Google Cloud CLI
- ScoutSuite
- Prowler, where supported by the current version
- GCP IAM recommender
- Forseti Security, where maintained and applicable
- Security Command Centre
- Cloud Asset Inventory

## Operational Considerations

- Confirm the active project before running commands.
- Establish organisation and folder boundaries.
- Avoid broad organisation-level operations unless explicitly authorised.
- Do not retrieve secret values.
- Avoid modifying IAM policies during read-only assessments.
- Consider the impact of changes to production workloads.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
