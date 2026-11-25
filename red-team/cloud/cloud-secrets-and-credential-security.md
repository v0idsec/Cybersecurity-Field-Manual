# Cloud Secrets and Credential Security

## Overview

Cloud environments rely on credentials and secrets to authenticate users, applications, workloads and external integrations.

Poor credential management can expose cloud resources, sensitive data and administrative control planes.

This guide covers the assessment of:
- Access keys.
- Application secrets.
- API tokens.
- Certificates.
- Service account credentials.
- Managed identities.
- Secret vaults.
- Workload identity configuration.

## 1. Common Credential Types

| Credential | Description |
|---|---|
| Access key | Long-lived or temporary API authentication material |
| Client secret | Application authentication credential |
| API token | Token used to authenticate to an API |
| Private key | Cryptographic material used for authentication or signing |
| Certificate | Identity or encryption credential |
| Session token | Temporary authentication material |
| Service account key | Credential associated with a workload identity |
| Managed identity | Provider-managed workload identity |

## 2. Common Exposure Locations

Investigate whether secrets are unnecessarily stored in:

- Public Git repositories.
- Private source repositories with excessive access.
- CI/CD configuration.
- Application configuration files.
- Environment variables.
- Container images.
- Build artefacts.
- Deployment scripts.
- Infrastructure-as-code files.
- Log files.
- Backup archives.
- Developer workstations.

Do not copy or reproduce complete secrets in assessment evidence.

## 3. AWS Secrets and Credentials

### IAM Access Keys

List access keys for an approved assessment identity:

```bash
aws iam list-access-keys --user-name USERNAME
```

Review last-used information:

```bash
aws iam get-access-key-last-used --access-key-id ACCESS_KEY_ID
```

Assess:
- Key age.
- Last-used timestamp.
- Active status.
- Associated identity.
- Required permissions.
- Whether temporary credentials are a better option.

### Secrets Manager

List secrets:

```bash
aws secretsmanager list-secrets
```

Review secret metadata:

```bash
aws secretsmanager describe-secret --secret-id SECRET_NAME
```

Do not retrieve secret values unless explicitly required and approved.

### Systems Manager Parameter Store

List parameters by path:

```bash
aws ssm describe-parameters
```

Review:
- Parameter classification.
- Encryption.
- Access policies.
- Rotation.
- Application dependencies.

## 4. Microsoft Azure Secrets and Credentials

### Key Vault

List vaults:

```bash
az keyvault list --output table
```

Review vault metadata:

```bash
az keyvault show \
  --name VAULT_NAME \
  --resource-group RESOURCE_GROUP
```

Assess:
- Access model.
- RBAC assignments.
- Network restrictions.
- Private endpoints.
- Soft delete.
- Purge protection.
- Diagnostic logging.

### Application Credentials

Review application registrations for:
- Client secret expiry.
- Certificate expiry.
- Unnecessary credentials.
- Unclear credential ownership.
- Excessive API permissions.
- Unused service principals.

Use approved Entra administration interfaces or Microsoft Graph tooling to review metadata.

Do not expose credential values in reports.

## 5. Google Cloud Secrets and Credentials

### Secret Manager

List secrets:

```bash
gcloud secrets list
```

Review secret metadata:

```bash
gcloud secrets describe SECRET_NAME
```

Review access policy:

```bash
gcloud secrets get-iam-policy SECRET_NAME
```

### Service Account Keys

List keys:

```bash
gcloud iam service-accounts keys list \
  --iam-account SERVICE_ACCOUNT_EMAIL
```

Assess:
- Key age.
- Key ownership.
- Workload dependencies.
- Key rotation.
- Unnecessary long-lived credentials.
- Service account permissions.

Prefer Workload Identity Federation or other short-lived identity mechanisms where appropriate.

## 6. Source-Code Secret Exposure

Public and private source repositories may contain accidentally committed secrets.

Look for:
- API keys.
- Cloud access keys.
- Database credentials.
- OAuth client secrets.
- Private keys.
- Signing certificates.
- Connection strings.
- Service account configuration.

Common detection tools:
- Gitleaks.
- TruffleHog.
- GitHub secret scanning.
- GitLab secret detection.
- Provider-native repository scanning.

### Gitleaks

Scan an authorised local repository:

```bash
gitleaks detect --source . --redact
```

Generate a report:

```bash
gitleaks detect \
  --source . \
  --redact \
  --report-format json \
  --report-path gitleaks-report.json
```

### TruffleHog

Scan an authorised repository:

```bash
trufflehog git file://.
```

Review tool output carefully and avoid exposing discovered secret values in logs or reports.

## 7. Container and CI/CD Credentials

Review:
- Container image layers.
- Build arguments.
- Environment variables.
- CI/CD variables.
- Deployment manifests.
- Pipeline logs.
- Registry credentials.
- Runner permissions.
- Deployment identities.

Assess whether secrets are:
- Stored in plaintext.
- Accessible to unnecessary users.
- Exposed in build output.
- Reused across environments.
- Long-lived.
- Rotated after exposure.

A secret removed from the current source tree may still exist in repository history or previously published artefacts.

## 8. Credential Lifecycle Assessment

Review the complete lifecycle:

1. Creation.
2. Ownership.
3. Storage.
4. Distribution.
5. Usage.
6. Monitoring.
7. Rotation.
8. Revocation.
9. Incident response.

Questions to ask:
- Who owns the credential?
- Which systems depend on it?
- Is it still required?
- Is its permission scope appropriate?
- Is its use logged?
- How is it rotated?
- Can it be revoked without disrupting production?

## 9. Credential Exposure Response

If a genuine credential exposure is identified:

1. Stop unnecessary access to the exposed material.
2. Preserve minimal evidence.
3. Record the source and discovery time.
4. Notify the authorised client contact.
5. Recommend revocation or rotation.
6. Identify dependent services.
7. Review relevant authentication logs.
8. Assess potential unauthorised use.
9. Confirm remediation through the approved process.

Do not attempt to authenticate using the exposed credential to establish whether it works.

## 10. Reporting

Record:
- Credential type.
- Affected identity or application.
- Exposure location.
- Relevant permissions.
- Exposure timeframe, where known.
- Potential impact.
- Evidence with sensitive values redacted.
- Recommended remediation.

Never include complete passwords, access keys, tokens or private keys in a report.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
