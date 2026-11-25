# Cloud Networking and External Exposure

## Overview

Cloud networking controls how workloads communicate with each other, external networks and the public internet.

Misconfigured network controls can expose administrative interfaces, databases, applications and internal services.

This guide covers network security assessment across AWS, Azure and GCP.

## 1. Assessment Objectives

Identify:
- Publicly exposed resources.
- Unrestricted inbound access.
- Unnecessary public IP addresses.
- Weak network segmentation.
- Exposed management services.
- Insecure load balancer configuration.
- Unintended inter-network connectivity.
- Unnecessary outbound access.
- Misconfigured private connectivity.

## 2. Cloud Network Components

| Component | Purpose |
|---|---|
| Virtual network | Logical network boundary |
| Subnet | Network segmentation |
| Security group / NSG / firewall | Traffic filtering |
| Route table | Network path selection |
| NAT gateway | Outbound connectivity |
| Internet gateway | Public internet connectivity |
| Load balancer | Traffic distribution |
| Private endpoint | Private access to managed services |
| VPN gateway | Encrypted network connectivity |
| Peering | Connectivity between networks |

## 3. Common Exposure Risks

| Exposure | Potential risk |
|---|---|
| Public SSH | Unnecessary remote administration exposure |
| Public RDP | Unnecessary Windows management exposure |
| Public databases | Unauthorised database access |
| Public management interfaces | Increased attack surface |
| Overly broad source ranges | Unrestricted network access |
| Flat network architecture | Increased lateral movement potential |
| Unrestricted outbound traffic | Reduced egress control |
| Misconfigured peering | Unintended network connectivity |

## 4. AWS Networking

### Discover VPCs

```bash
aws ec2 describe-vpcs
```

List subnets:

```bash
aws ec2 describe-subnets
```

List route tables:

```bash
aws ec2 describe-route-tables
```

Review security groups:

```bash
aws ec2 describe-security-groups
```

Review network ACLs:

```bash
aws ec2 describe-network-acls
```

Review internet gateways:

```bash
aws ec2 describe-internet-gateways
```

### Assessment Areas

- Public subnet design.
- Security group ingress and egress.
- Network ACL restrictions.
- Route table configuration.
- VPC peering.
- Transit Gateway connectivity.
- VPN and Direct Connect paths.
- PrivateLink configuration.
- Public IP allocation.

A subnet's route table and attached security controls should be evaluated together.

## 5. Azure Networking

### Discover Virtual Networks

```bash
az network vnet list --output table
```

List subnets:

```bash
az network vnet subnet list \
  --resource-group RESOURCE_GROUP \
  --vnet-name VNET_NAME
```

List NSGs:

```bash
az network nsg list --output table
```

List public IP addresses:

```bash
az network public-ip list --output table
```

List load balancers:

```bash
az network lb list --output table
```

### Assessment Areas

- Network security groups.
- Effective security rules.
- Subnet segmentation.
- Public IP exposure.
- Azure Firewall.
- Application Security Groups.
- Virtual network peering.
- Private endpoints.
- VPN gateways.
- Network Watcher configuration.

Review effective access rather than assuming that one NSG represents the complete network security posture.

## 6. GCP Networking

### Discover VPC Networks

```bash
gcloud compute networks list
```

List subnets:

```bash
gcloud compute networks subnets list
```

List firewall rules:

```bash
gcloud compute firewall-rules list
```

List instances:

```bash
gcloud compute instances list
```

List forwarding rules:

```bash
gcloud compute forwarding-rules list
```

### Assessment Areas

- VPC firewall rules.
- Subnet configuration.
- External IP addresses.
- Private Google Access.
- Cloud NAT.
- VPC peering.
- Shared VPC.
- Private Service Connect.
- Load balancer exposure.
- Hierarchical firewall policies.

## 7. Public Service Exposure

Identify services that should not be directly reachable from the internet.

Examples:
- SSH.
- RDP.
- SMB.
- Database services.
- Administrative dashboards.
- Container management interfaces.
- Internal APIs.
- Monitoring interfaces.

Exposure should be assessed against the intended architecture and approved access model.

A service may be intentionally public but still require authentication, rate limiting and appropriate security controls.

## 8. Network Segmentation

Review whether workloads are separated according to business function and sensitivity.

Example architecture:

```text
Internet
   |
   v
Public Load Balancer
   |
   v
Application Subnet
   |
   v
Private Database Subnet
```

Consider:
- Public versus private subnets.
- Production versus development.
- Application versus database tiers.
- Administrative access paths.
- Management networks.
- Shared services.
- Cross-account or cross-project connectivity.

## 9. Metadata Services

Cloud instance metadata services provide workloads with information about their execution environment and, in some configurations, access to temporary credentials.

Review provider-specific protections.

### AWS

Assess:
- Instance Metadata Service version.
- Whether IMDSv2 is required.
- Hop limit configuration.
- Workload access to instance credentials.

Read-only configuration review:

```bash
aws ec2 describe-instances \
  --query 'Reservations[].Instances[].{ID:InstanceId,Metadata:MetadataOptions}'
```

### Azure

Assess:
- Workload access to the Azure Instance Metadata Service.
- Managed identity exposure.
- Application access to metadata endpoints.
- Network controls around workloads.

### GCP

Assess:
- Workload access to metadata endpoints.
- Service account attachment.
- Service account permissions.
- Workload isolation.

Metadata access should be considered alongside workload permissions and application security.

Do not attempt credential extraction from production workloads unless explicitly authorised.

## 10. Controlled Validation

Preferred validation sequence:

1. Review cloud network configuration.
2. Identify public endpoints.
3. Confirm asset ownership and scope.
4. Review effective security rules.
5. Validate using approved test resources.
6. Conduct active scanning only where permitted.
7. Document exposure and limitations.

Avoid scanning provider infrastructure or unrelated shared hosting resources.

## 11. Reporting

Record:
- Cloud provider.
- Account, subscription or project.
- Network resource identifiers.
- Relevant security rules.
- Affected service.
- Source and destination ranges.
- Potential impact.
- Evidence.
- Recommended remediation.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
