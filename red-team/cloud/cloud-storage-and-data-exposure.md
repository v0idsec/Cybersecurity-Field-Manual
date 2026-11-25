# Cloud Storage and Data Exposure

## Overview

Cloud storage services frequently contain business-critical information, backups, application data and sensitive records.

Misconfigured access controls can expose data to unintended users or the public internet.

This guide covers storage security assessment across AWS, Azure and GCP.

## 1. Assessment Objectives

Determine:
- Which storage resources exist?
- Who can access them?
- Is anonymous access permitted?
- Are external identities trusted?
- Is encryption configured?
- Are backups protected?
- Is access logged?
- Are retention controls appropriate?
- Are storage resources exposed through public endpoints?

## 2. Common Storage Risks

| Risk | Potential impact |
|---|---|
| Public object access | Unauthorised data disclosure |
| Excessive permissions | Unnecessary data access |
| Weak access policies | Unintended external access |
| Exposed backups | Disclosure of historical information |
| Missing encryption controls | Increased data exposure risk |
| Inadequate logging | Reduced visibility into access |
| Weak retention controls | Unnecessary data retention |
| Shared credentials | Uncontrolled access to stored data |

## 3. AWS S3

### Review Buckets

```bash
aws s3api list-buckets
```

Review public access block settings:

```bash
aws s3api get-public-access-block --bucket BUCKET
```

Review bucket policy:

```bash
aws s3api get-bucket-policy --bucket BUCKET
```

Review bucket ACL:

```bash
aws s3api get-bucket-acl --bucket BUCKET
```

Review encryption:

```bash
aws s3api get-bucket-encryption --bucket BUCKET
```

Review versioning:

```bash
aws s3api get-bucket-versioning --bucket BUCKET
```

### Key Configuration Areas

- S3 Block Public Access.
- Bucket policies.
- Object ownership.
- Access control lists.
- Encryption.
- Versioning.
- Object Lock.
- Logging.
- Lifecycle policies.

### Assessment Considerations

Evaluate effective access rather than relying on a single setting.

For example, a bucket-level public access configuration should be considered alongside:
- Account-level public access blocks.
- Bucket policies.
- Access points.
- Object ownership settings.
- IAM permissions.

Do not download objects to prove exposure unless explicitly authorised.

## 4. Azure Storage

### Discover Storage Accounts

```bash
az storage account list --output table
```

Review an account:

```bash
az storage account show \
  --name STORAGE_ACCOUNT \
  --resource-group RESOURCE_GROUP
```

Review containers using an authorised identity:

```bash
az storage container list \
  --account-name STORAGE_ACCOUNT \
  --auth-mode login
```

### Key Configuration Areas

- Public network access.
- Anonymous blob access.
- Secure transfer requirement.
- Minimum TLS version.
- Shared key authorisation.
- Network restrictions.
- Private endpoints.
- Encryption.
- Soft delete.
- Versioning.
- Diagnostic logging.

### Assessment Considerations

Review whether:
- Anonymous blob access is enabled.
- Container access is intentionally public.
- Shared key access is required.
- Storage is reachable from untrusted networks.
- Access is restricted to approved identities.
- Sensitive data is protected by appropriate controls.

Do not retrieve sensitive blob contents unnecessarily.

## 5. Google Cloud Storage

### Discover Buckets

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

### Key Configuration Areas

- Public Access Prevention.
- Uniform bucket-level access.
- IAM bindings.
- Object ACLs, where applicable.
- Retention policies.
- Encryption.
- Versioning.
- Logging.
- Lifecycle policies.

### Public Principals

Review for unintended access granted to principals such as:

```text
allUsers
allAuthenticatedUsers
```

The presence of a public principal should be assessed against the intended purpose of the bucket.

## 6. Backup and Snapshot Exposure

Backups and snapshots can contain:
- Database records.
- Application configuration.
- User information.
- Authentication data.
- Infrastructure configuration.
- Historical files.

Review:
- Backup storage permissions.
- Snapshot sharing.
- Retention policies.
- Encryption.
- Cross-account access.
- Recovery access.
- Logging.

Examples of relevant resources:

| Provider | Resource |
|---|---|
| AWS | EBS snapshots, RDS snapshots, S3 backups |
| Azure | Managed disk snapshots, Recovery Services vaults |
| GCP | Persistent disk snapshots, Cloud Storage backups |

## 7. Data Classification

Storage configuration should be evaluated against the sensitivity of the data.

Example classification:

| Classification | Example |
|---|---|
| Public | Approved public website assets |
| Internal | Internal business documents |
| Confidential | Customer and commercial information |
| Restricted | Highly sensitive personal or regulated data |

An exposure finding should explain what type of data could be accessed without unnecessarily reproducing that data.

## 8. Encryption

Review:
- Encryption at rest.
- Encryption in transit.
- Customer-managed keys.
- Key access policies.
- Key rotation.
- Key separation.
- Encryption configuration for backups.

Encryption at rest does not compensate for excessive access permissions.

A user with authorised access to an object may still be able to retrieve decrypted content.

## 9. Access Logging

Review whether storage access is recorded.

Relevant services:

| Provider | Logging |
|---|---|
| AWS | CloudTrail data events, S3 server access logging |
| Azure | Storage diagnostic settings and Azure Monitor |
| GCP | Cloud Audit Logs and Cloud Logging |

Determine:
- Which operations are logged.
- Whether read access is covered.
- Where logs are stored.
- How long logs are retained.
- Who can modify or delete them.
- Whether alerts are generated for unusual access.

## 10. Controlled Validation

Use the least intrusive validation method.

Preferred approach:
1. Review access policies.
2. Review effective permissions.
3. Confirm whether anonymous access is configured.
4. Use an approved test object where necessary.
5. Avoid accessing real customer records.
6. Capture minimal evidence.
7. Report the exposure through approved channels.

## 11. Reporting

Document:
- Provider.
- Account, subscription or project.
- Storage resource identifier.
- Access configuration.
- Data classification, if known.
- Potential exposure.
- Evidence.
- Confidence.
- Remediation.

Do not include actual sensitive object contents in the report unless specifically required and securely approved.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
