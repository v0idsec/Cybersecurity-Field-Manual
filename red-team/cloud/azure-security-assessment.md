# Microsoft Azure Security Assessment

## Overview

Microsoft Azure assessments examine cloud resources, identity configuration, network security, storage, applications and monitoring.

Azure security is closely integrated with Microsoft Entra ID, making identity and access configuration a central part of the assessment.

Common assessment areas:
- Entra ID users, groups and roles.
- Azure RBAC.
- Service principals and managed identities.
- Virtual machines and network security groups.
- Storage accounts.
- Key Vault.
- App registrations.
- Activity Logs.
- Defender for Cloud.

All commands must be run against approved tenants and subscriptions.

## 1. Establish Tenant and Subscription Context

Sign in using the approved assessment identity:

```bash
az login
```

Review the current account:

```bash
az account show
```

List available subscriptions:

```bash
az account list --output table
```

Select the approved subscription:

```bash
az account set --subscription SUBSCRIPTION_ID
```

Confirm the active subscription again:

```bash
az account show --output table
```

Do not assume that the first available subscription is in scope.

## 2. Tenant and Identity Discovery

Review signed-in identity and tenant context:

```bash
az ad signed-in-user show
```

List users, where permitted:

```bash
az ad user list --output table
```

List groups:

```bash
az ad group list --output table
```

List service principals:

```bash
az ad sp list --all
```

Review application registrations:

```bash
az ad app list --all
```

Assess:
- Privileged accounts.
- Guest accounts.
- Unused identities.
- Service principal permissions.
- Application credentials.
- External identity relationships.
- Conditional Access coverage.

Directory enumeration capabilities depend on the permissions of the signed-in identity and the current CLI version.

## 3. Azure RBAC

Azure RBAC controls access to Azure resources.

List role assignments:

```bash
az role assignment list --all --output table
```

Review role definitions:

```bash
az role definition list --output table
```

Look for:
- Owner assignments.
- Contributor assignments.
- User Access Administrator.
- Custom roles with broad permissions.
- Excessive subscription-level access.
- Unnecessary inherited permissions.

### Scope Matters

Azure RBAC can be assigned at:
- Management group.
- Subscription.
- Resource group.
- Individual resource.

A role assigned at a higher scope may affect many downstream resources.

Review both direct and inherited assignments.

## 4. Virtual Machine Assessment

List virtual machines:

```bash
az vm list --output table
```

Review VM details:

```bash
az vm show \
  --resource-group RESOURCE_GROUP \
  --name VM_NAME
```

Review public IP addresses:

```bash
az network public-ip list --output table
```

Assess:
- Public management access.
- Disk encryption.
- Managed identities.
- Network security groups.
- Backup configuration.
- Patch management.
- Monitoring agents.
- Administrative access methods.

## 5. Network Security Groups

List NSGs:

```bash
az network nsg list --output table
```

Review rules:

```bash
az network nsg rule list \
  --resource-group RESOURCE_GROUP \
  --nsg-name NSG_NAME \
  --output table
```

Look for:
- Unrestricted inbound rules.
- Public management access.
- Unnecessary open ports.
- Broad source ranges.
- Conflicting or redundant rules.

Commonly sensitive ports include SSH, RDP, SMB, database services and administrative interfaces.

## 6. Storage Account Assessment

List storage accounts:

```bash
az storage account list --output table
```

Review configuration:

```bash
az storage account show \
  --name STORAGE_ACCOUNT \
  --resource-group RESOURCE_GROUP
```

Review key properties:
- Public network access.
- Anonymous blob access.
- Secure transfer requirement.
- Minimum TLS version.
- Network restrictions.
- Encryption configuration.
- Shared key access.
- Private endpoint usage.

Review blob containers using an authorised identity:

```bash
az storage container list \
  --account-name STORAGE_ACCOUNT \
  --auth-mode login
```

Do not enumerate or download sensitive objects unless explicitly authorised.

## 7. Key Vault

List vaults:

```bash
az keyvault list --output table
```

Review vault configuration:

```bash
az keyvault show \
  --name VAULT_NAME \
  --resource-group RESOURCE_GROUP
```

Assess:
- RBAC or access policy model.
- Network restrictions.
- Private endpoint configuration.
- Soft delete.
- Purge protection.
- Diagnostic logging.
- Administrative access.

Review permissions without retrieving secret values.

Do not access secret contents merely to prove that a vault contains secrets.

## 8. Application Registrations and Service Principals

Applications can hold permissions that extend beyond the access of individual users.

Review:
- API permissions.
- Application roles.
- Delegated permissions.
- Admin consent.
- Client secret expiry.
- Certificate expiry.
- Credential ownership.
- Service principal assignments.

Look for:
- Unused application credentials.
- Excessive Graph API permissions.
- Broad application permissions.
- Credentials without a clear owner.
- Unnecessary tenant-wide consent.

Credential values should never be copied into assessment reports.

## 9. Logging and Detection

Review Azure Activity Logs:

```bash
az monitor activity-log list --max-events 50
```

List diagnostic settings:

```bash
az monitor diagnostic-settings list \
  --resource RESOURCE_ID
```

Review:
- Activity Log retention.
- Entra ID sign-in logs.
- Audit logs.
- Resource diagnostic settings.
- Log Analytics integration.
- Defender for Cloud recommendations.
- Security alert routing.

## 10. Common Security Issues

| Issue | Potential impact |
|---|---|
| Excessive Owner assignments | Broad control over Azure resources |
| Overprivileged service principals | Unauthorised application access |
| Public storage access | Data exposure |
| Unrestricted NSGs | Network exposure |
| Weak Key Vault permissions | Secret disclosure |
| Unprotected application credentials | Application compromise |
| Missing diagnostic logging | Reduced visibility |
| Unnecessary public IPs | Increased attack surface |

## 11. Assessment Tools

- Azure CLI
- Microsoft Graph PowerShell
- ScoutSuite
- Prowler, where supported by the assessment scope and current version
- ROADtools, for authorised Entra ID assessment
- Azure Resource Graph Explorer
- Microsoft Defender for Cloud

## Operational Considerations

- Confirm tenant and subscription context before every assessment.
- Use read-only permissions where practical.
- Do not modify RBAC or Conditional Access policies without approval.
- Avoid retrieving secret values.
- Consider the impact of changes to production identity systems.
- Confirm whether Entra ID tenant-wide testing is explicitly in scope.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
