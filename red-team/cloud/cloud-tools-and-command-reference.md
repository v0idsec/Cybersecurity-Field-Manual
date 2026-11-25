# Cloud Tools and Command Reference

## Overview

This document provides a practical reference to commonly used cloud security assessment tools and command-line utilities.

It covers:
- Provider-native command-line tools.
- Cloud security posture assessment.
- Configuration auditing.
- Identity analysis.
- Infrastructure discovery.
- Secret detection.
- Infrastructure-as-code security.

This is a professional reference, not an installation guide.

All commands must be executed against authorised accounts, subscriptions and projects.

---

# 1. Provider Command-Line Tools

## AWS CLI

Official documentation:

https://docs.aws.amazon.com/cli/

### Identity and Account

```bash
aws sts get-caller-identity
aws configure list-profiles
aws configure list
```

### IAM

```bash
aws iam list-users
aws iam list-groups
aws iam list-roles
aws iam list-policies --scope Local
```

### EC2 and Networking

```bash
aws ec2 describe-instances
aws ec2 describe-vpcs
aws ec2 describe-subnets
aws ec2 describe-security-groups
aws ec2 describe-route-tables
```

### S3

```bash
aws s3api list-buckets
aws s3api get-bucket-location --bucket BUCKET
aws s3api get-bucket-policy --bucket BUCKET
aws s3api get-bucket-acl --bucket BUCKET
aws s3api get-bucket-encryption --bucket BUCKET
```

### Logging and Security

```bash
aws cloudtrail describe-trails
aws guardduty list-detectors
aws securityhub describe-hubs
```

---

## Azure CLI

Official documentation:

https://learn.microsoft.com/cli/azure/

### Identity and Subscription

```bash
az account show
az account list --output table
az ad signed-in-user show
az ad user list --output table
az ad group list --output table
az ad sp list --all
```

### RBAC

```bash
az role assignment list --all --output table
az role definition list --output table
```

### Compute and Networking

```bash
az vm list --output table
az network vnet list --output table
az network nsg list --output table
az network public-ip list --output table
az network lb list --output table
```

### Storage and Key Vault

```bash
az storage account list --output table
az keyvault list --output table
```

### Monitoring

```bash
az monitor activity-log list --max-events 50
```

---

## Google Cloud CLI

Official documentation:

https://cloud.google.com/sdk/gcloud

### Identity and Project

```bash
gcloud auth list
gcloud config list
gcloud projects list
gcloud config get-value project
```

### IAM

```bash
gcloud projects get-iam-policy PROJECT_ID
gcloud iam roles list
gcloud iam service-accounts list
```

### Compute and Networking

```bash
gcloud compute instances list
gcloud compute networks list
gcloud compute firewall-rules list
gcloud compute networks subnets list
gcloud compute forwarding-rules list
```

### Storage and Secrets

```bash
gcloud storage buckets list
gcloud secrets list
```

---

# 2. Cloud Security Assessment Tools

## Prowler

https://github.com/prowler-cloud/prowler

<badge color="success">Cloud Security Auditing</badge>

Prowler performs security posture assessments across supported cloud providers.

### Common Use Cases

- Security configuration auditing.
- Identity and access review.
- Storage configuration checks.
- Logging and monitoring assessment.
- Compliance-oriented checks.
- Cloud security baseline reviews.

### AWS Examples

```bash
prowler aws
```

Run against a named profile:

```bash
prowler aws --profile assessment
```

Run selected checks:

```bash
prowler aws --checks CHECK_ID
```

### Azure Example

```bash
prowler azure
```

### GCP Example

```bash
prowler gcp
```

Exact command options and provider support depend on the installed release.

### Assessment Notes

- Review the current documentation for provider-specific arguments.
- Use approved identities.
- Review permissions required by the scanner.
- Treat findings as assessment leads.
- Validate important results manually.
- Review scan impact before executing against production.

---

## ScoutSuite

https://github.com/nccgroup/ScoutSuite

<badge>Multi-Cloud Security Auditing</badge>

ScoutSuite provides multi-cloud security posture assessment.

### Common Use Cases

- Cloud configuration review.
- IAM analysis.
- Public exposure identification.
- Storage configuration review.
- Security posture reporting.

### Examples

AWS:

```bash
scout aws
```

Azure:

```bash
scout azure
```

GCP:

```bash
scout gcp
```

Review the current project documentation for supported authentication methods and provider-specific options.

### Assessment Notes

- Scanner output can contain false positives.
- Confirm the active cloud account before execution.
- Review generated reports for sensitive information.
- Do not treat a single automated scan as a complete security assessment.

---

## Pacu

https://github.com/RhinoSecurityLabs/pacu

<badge color="warning">Controlled Adversarial Testing</badge>

Pacu is an AWS exploitation framework intended for authorised security testing.

It can assist with controlled assessment of:
- IAM permissions.
- Role relationships.
- Cloud attack paths.
- Resource access.
- Security control weaknesses.

### Operational Requirements

Use only when:
- AWS account ownership is confirmed.
- The engagement explicitly permits adversarial testing.
- The approved test identity is understood.
- Potential production impact is documented.
- Destructive and persistence-related capabilities are excluded unless separately authorised.

Pacu is not a substitute for read-only cloud configuration review.

Do not run arbitrary modules simply because they are available.

---

## CloudMapper

https://github.com/duo-labs/cloudmapper

CloudMapper helps visualise AWS network and account relationships.

### Common Use Cases

- Network architecture review.
- Security group analysis.
- Account relationship visualisation.
- External exposure review.
- Network segmentation assessment.

Use current project documentation for supported commands and data collection requirements.

---

## CloudSploit

https://github.com/aquasecurity/cloudsploit

CloudSploit provides cloud security configuration scanning capabilities.

### Common Use Cases

- Configuration auditing.
- Security baseline review.
- Cloud resource assessment.
- Identification of insecure configurations.

Check current project maintenance status, provider support and available plugins before selecting it for an engagement.

---

# 3. Identity and Access Analysis

## ROADtools

https://github.com/dirkjanm/ROADtools

ROADtools provides tooling for Microsoft Entra ID research and authorised security assessment.

### Common Use Cases

- Entra ID directory analysis.
- Application and service principal review.
- Role and permission analysis.
- Tenant relationship investigation.

Use approved tenant access and current documentation.

Avoid broad collection of personal directory information that is not required for the engagement.

## Azure Resource Graph

https://learn.microsoft.com/azure/governance/resource-graph/

Azure Resource Graph can query Azure resource metadata across accessible subscriptions.

Example:

```bash
az graph query -q "Resources | project name, type, location"
```

Useful for:
- Resource inventory.
- Public IP discovery.
- Resource type analysis.
- Configuration review.
- Subscription-wide visibility.

---

# 4. Secret Detection

## Gitleaks

https://github.com/gitleaks/gitleaks

Scan an authorised repository:

```bash
gitleaks detect --source . --redact
```

Generate JSON output:

```bash
gitleaks detect \
  --source . \
  --redact \
  --report-format json \
  --report-path report.json
```

## TruffleHog

https://github.com/trufflesecurity/trufflehog

Scan an authorised Git repository:

```bash
trufflehog git file://.
```

Review output carefully and ensure sensitive findings are redacted.

---

# 5. Infrastructure-as-Code Security

Cloud infrastructure is frequently deployed using declarative configuration.

Common formats include:
- Terraform.
- CloudFormation.
- Bicep.
- ARM templates.
- Kubernetes manifests.

Misconfiguration in these files can introduce weaknesses before infrastructure is deployed.

## Checkov

https://github.com/bridgecrewio/checkov

Scan a Terraform directory:

```bash
checkov -d .
```

Scan a specific file:

```bash
checkov -f main.tf
```

## Trivy

https://github.com/aquasecurity/trivy

Scan infrastructure-as-code:

```bash
trivy config .
```

## KICS

https://github.com/Checkmarx/kics

Scan infrastructure-as-code:

```bash
kics scan -p .
```

### Common Issues to Look For

- Public storage access.
- Unrestricted network rules.
- Excessive IAM permissions.
- Hardcoded secrets.
- Unencrypted storage.
- Public database access.
- Missing logging.
- Insecure container configuration.

---

# 6. Tool Selection Guide

| Assessment objective | Recommended tools |
|---|---|
| AWS security posture | Prowler, ScoutSuite |
| Azure security posture | Prowler, ScoutSuite |
| GCP security posture | Prowler, ScoutSuite |
| AWS adversarial assessment | Pacu, where authorised |
| AWS network visualisation | CloudMapper |
| Entra ID analysis | ROADtools |
| Azure resource inventory | Azure Resource Graph |
| Secret discovery | Gitleaks, TruffleHog |
| Infrastructure-as-code review | Checkov, Trivy, KICS |
| Provider-native enumeration | AWS CLI, Azure CLI, gcloud |

---

# 7. General Assessment Checklist

## Scope and Context

- [ ] Correct cloud provider identified.
- [ ] Account, tenant or project confirmed.
- [ ] Approved regions identified.
- [ ] Third-party dependencies documented.
- [ ] Testing permissions confirmed.

## Identity

- [ ] Privileged roles reviewed.
- [ ] Excessive permissions identified.
- [ ] Service identities reviewed.
- [ ] Federation configuration reviewed.
- [ ] Long-lived credentials assessed.
- [ ] Cross-account access reviewed.

## Infrastructure

- [ ] Public-facing resources identified.
- [ ] Network security controls reviewed.
- [ ] Unnecessary public IPs identified.
- [ ] Segmentation reviewed.
- [ ] Management interfaces assessed.
- [ ] Metadata service protections reviewed.

## Storage and Secrets

- [ ] Public storage configuration reviewed.
- [ ] Backup access reviewed.
- [ ] Encryption configuration reviewed.
- [ ] Secret vault permissions reviewed.
- [ ] Source-code secret exposure assessed.
- [ ] Sensitive evidence appropriately redacted.

## Monitoring

- [ ] Audit logging reviewed.
- [ ] Identity events monitored.
- [ ] Network logging reviewed.
- [ ] Security alerts assessed.
- [ ] Log retention and protection reviewed.

## Reporting and Cleanup

- [ ] Findings independently validated.
- [ ] False positives removed.
- [ ] Resource identifiers recorded.
- [ ] Remediation guidance included.
- [ ] Temporary permissions revoked.
- [ ] Temporary resources removed.
- [ ] Sensitive evidence securely handled.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
