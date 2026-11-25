# Cloud Threat Hunting

## Overview

Cloud threat hunting investigates suspicious activity across cloud infrastructure, identity services, applications and workloads.

Cloud environments introduce additional challenges because infrastructure is dynamic, identity is often centralised and control-plane activity can have significant impact.

## Hunting Objectives

- Identify compromised cloud identities.
- Detect suspicious administrative activity.
- Investigate unauthorised resource changes.
- Identify exposed storage.
- Detect unexpected credential creation.
- Investigate changes to security controls.
- Identify unusual workload communication.

## AWS Hunting

### CloudTrail

CloudTrail records AWS API activity.

Investigate:

- Unusual console logins
- IAM policy changes
- New access keys
- Role assumption
- Security group modifications
- Logging configuration changes
- Storage policy changes
- Unexpected resource creation

### GuardDuty

Review findings involving:

- Credential compromise
- Suspicious API activity
- Malware
- Unusual network communication
- Reconnaissance
- Potential data exfiltration

### Example AWS CLI

List recent CloudTrail events:

```bash
aws cloudtrail lookup-events \
  --max-results 50
```

Filter for IAM-related events:

```bash
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=EventSource,AttributeValue=iam.amazonaws.com \
  --max-results 50
```

Commands require appropriate permissions and AWS CLI configuration.

## Microsoft Azure Hunting

### Azure Activity Logs

Investigate:

- Role assignments
- Resource creation
- Network security changes
- Key Vault access
- Diagnostic settings changes
- Resource deletion
- Subscription-level changes

### Microsoft Entra ID

Investigate:

- Risky sign-ins
- Unusual application consent
- Service principal modifications
- New credentials
- Privileged role changes
- Authentication method changes

### Example KQL

```kql
AzureActivity
| where TimeGenerated > ago(24h)
| where ActivityStatusValue =~ "Success"
| summarize Operations = count()
    by Caller, OperationNameValue, ResourceGroup
| order by Operations desc
```

Field availability depends on the connected Azure data source.

## Google Cloud Hunting

Relevant sources:

- Cloud Audit Logs
- VPC Flow Logs
- Cloud DNS logs
- Security Command Center
- IAM activity
- Cloud Logging

Investigate:

- IAM policy modifications
- New service account keys
- Unexpected service account usage
- Public resource exposure
- Firewall changes
- Logging configuration changes
- Unusual API activity

## Identity and Credential Hunting

Cloud identity compromise may involve:

- Stolen access keys
- Refresh token abuse
- Compromised service principals
- Unusual role assumptions
- Suspicious OAuth consent
- New service account credentials

Correlate identity activity with source address, device, application and resource access.

## Cloud Persistence

Investigate:

- New IAM users
- New access keys
- Modified trust policies
- New service principals
- Unexpected role assignments
- Scheduled cloud functions
- Startup scripts
- New automation credentials

## Cloud Logging Tampering

Monitor for:

- Disabled audit logging
- Modified diagnostic settings
- Deleted log destinations
- Changed retention policies
- Modified security monitoring configuration

Logging changes should be treated as important events, particularly when they occur alongside suspicious administrative activity.

## Cloud Network Hunting

Review:

- VPC flow logs
- Network security group changes
- Unexpected outbound traffic
- Public IP assignments
- New ingress rules
- Unusual inter-service communication
- Access to sensitive storage

## Investigation Workflow

1. Identify the affected tenant, account or subscription.
2. Establish the timeframe.
3. Review identity activity.
4. Examine control-plane events.
5. Review resource and permission changes.
6. Inspect network activity.
7. Correlate with endpoint and application telemetry.
8. Assess potential data exposure.
9. Preserve relevant audit evidence.
10. Escalate and document findings.

## Further Reading

- AWS CloudTrail: https://docs.aws.amazon.com/awscloudtrail/
- AWS GuardDuty: https://docs.aws.amazon.com/guardduty/
- Azure Monitor: https://learn.microsoft.com/azure/azure-monitor/
- Microsoft Entra: https://learn.microsoft.com/entra/
- Google Cloud Audit Logs: https://cloud.google.com/logging/docs/audit

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
