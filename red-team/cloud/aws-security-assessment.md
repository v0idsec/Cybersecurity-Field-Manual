# AWS Security Assessment

## Overview

Amazon Web Services (AWS) provides a broad range of cloud infrastructure, identity, storage, networking and application services.

AWS assessments commonly focus on:
- IAM permissions and trust relationships.
- S3 storage configuration.
- EC2 instances and network exposure.
- VPC security controls.
- Lambda execution roles.
- Secrets management.
- CloudTrail and GuardDuty.
- Cross-account access.

All commands in this guide are intended for authorised assessment of approved AWS accounts.

## 1. Establish Account Context

Confirm the active identity and account.

```bash
aws sts get-caller-identity
```

This returns information including:
- Account ID.
- User ID.
- ARN.

Review configured CLI profiles:

```bash
aws configure list-profiles
```

Use an explicitly approved profile:

```bash
aws sts get-caller-identity --profile assessment
```

Do not assume that the currently configured account is the approved assessment account.

## 2. Account and Region Discovery

List enabled regions:

```bash
aws ec2 describe-regions
```

Review the current region:

```bash
aws configure get region
```

Account and region coverage should be established before concluding that an environment has no relevant resources.

## 3. IAM Assessment

IAM controls access to AWS resources.

Review users:

```bash
aws iam list-users
```

Review groups:

```bash
aws iam list-groups
```

Review roles:

```bash
aws iam list-roles
```

Review customer-managed policies:

```bash
aws iam list-policies --scope Local
```

Review attached user policies:

```bash
aws iam list-attached-user-policies --user-name USERNAME
```

Review inline policies:

```bash
aws iam list-user-policies --user-name USERNAME
```

### Access Key Review

```bash
aws iam list-access-keys --user-name USERNAME
```

Review:
- Key age.
- Last used information.
- Whether keys are active.
- Whether long-lived keys are necessary.
- Whether workloads should use temporary credentials instead.

Do not retrieve or use credentials belonging to other users.

### Policy Review

Look for:
- `Action: "*"`
- `Resource: "*"`
- Unnecessary administrative permissions.
- Broad trust relationships.
- Unrestricted role assumption.
- Excessive permissions across sensitive services.

Wildcard permissions are not automatically exploitable, but they warrant contextual review.

## 4. EC2 Assessment

List instances:

```bash
aws ec2 describe-instances
```

Review security groups:

```bash
aws ec2 describe-security-groups
```

Review network interfaces:

```bash
aws ec2 describe-network-interfaces
```

Review instance metadata configuration:

```bash
aws ec2 describe-instances \
  --query 'Reservations[].Instances[].{ID:InstanceId,Metadata:MetadataOptions,PublicIP:PublicIpAddress}'
```

Assess:
- Public IP exposure.
- Unrestricted inbound access.
- Management ports exposed to the internet.
- Instance metadata configuration.
- Security group reuse.
- Unnecessary network interfaces.
- Instance role permissions.

### Security Group Review

Commonly sensitive ports include:

| Port | Service |
|---|---|
| 22 | SSH |
| 3389 | RDP |
| 445 | SMB |
| 3306 | MySQL |
| 5432 | PostgreSQL |
| 1433 | Microsoft SQL Server |
| 6379 | Redis |
| 27017 | MongoDB |

Review the actual business requirement and source restrictions before classifying exposure.

## 5. S3 Assessment

List buckets:

```bash
aws s3api list-buckets
```

Review bucket location:

```bash
aws s3api get-bucket-location --bucket BUCKET
```

Review public access block configuration:

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

Review encryption configuration:

```bash
aws s3api get-bucket-encryption --bucket BUCKET
```

Review versioning:

```bash
aws s3api get-bucket-versioning --bucket BUCKET
```

A missing bucket-level public access block does not automatically mean that a bucket is public. Consider account-level controls, bucket policies and access points.

## 6. Lambda Assessment

List functions:

```bash
aws lambda list-functions
```

Review function configuration:

```bash
aws lambda get-function-configuration --function-name FUNCTION
```

Review:
- Execution role.
- Environment variable handling.
- Runtime version.
- Network configuration.
- Resource-based policies.
- Logging.
- Secret retrieval patterns.

Do not retrieve or disclose secret environment variables unnecessarily.

## 7. RDS Assessment

List database instances:

```bash
aws rds describe-db-instances
```

Review:
- Public accessibility.
- Encryption.
- Backup retention.
- Network security groups.
- Database logging.
- Multi-AZ configuration.
- Snapshot exposure.

Database availability to the public internet should be assessed against the intended architecture.

## 8. CloudTrail and GuardDuty

Review trails:

```bash
aws cloudtrail describe-trails
```

Review trail status:

```bash
aws cloudtrail get-trail-status --name TRAIL_NAME
```

Review GuardDuty detectors:

```bash
aws guardduty list-detectors
```

Review findings:

```bash
aws guardduty list-findings --detector-id DETECTOR_ID
```

Assess:
- Whether relevant regions are monitored.
- Whether logs are retained.
- Whether logs are protected from modification.
- Whether alerts are centrally monitored.
- Whether findings are investigated.

## 9. Cross-Account Access

Review role trust policies:

```bash
aws iam get-role --role-name ROLE_NAME
```

Inspect:
- Trusted AWS account principals.
- External ID requirements.
- Federated principals.
- Service principals.
- Conditions on role assumption.

A trust relationship should be evaluated in the context of the intended integration.

## 10. Common Security Issues

| Issue | Potential impact |
|---|---|
| Excessive IAM permissions | Unauthorised resource access or privilege escalation |
| Public S3 data | Information disclosure |
| Unrestricted security groups | Unnecessary network exposure |
| Long-lived access keys | Credential compromise risk |
| Weak role trust policies | Unauthorised role assumption |
| Missing audit logging | Reduced investigation capability |
| Exposed database services | Unauthorised database access |
| Overprivileged Lambda roles | Excessive workload permissions |

## 11. Assessment Tools

- AWS CLI
- Prowler
- ScoutSuite
- CloudSploit
- Pacu, where explicitly authorised for controlled adversarial testing
- CloudMapper

Use tools in read-only or audit modes where possible.

## Operational Considerations

- Confirm the AWS account ID before running commands.
- Confirm the active region.
- Use approved profiles and roles.
- Avoid resource modification unless authorised.
- Do not access customer data unnecessarily.
- Avoid running aggressive automated testing against production.
- Consider AWS policies and service-specific testing restrictions.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
