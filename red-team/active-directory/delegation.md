
# Kerberos Delegation Assessment

> Professional reference guide for assessing unconstrained, constrained and resource-based constrained delegation in Active Directory.

## Contents

- [Overview](#overview)
- [Delegation Fundamentals](#delegation-fundamentals)
- [Unconstrained Delegation](#unconstrained-delegation)
- [Constrained Delegation](#constrained-delegation)
- [Resource-Based Constrained Delegation](#resource-based-constrained-delegation)
- [Protocol Transition](#protocol-transition)
- [Enumeration](#enumeration)
- [Assessment Methodology](#assessment-methodology)
- [Risk Analysis](#risk-analysis)
- [Detection](#detection)
- [Mitigation](#mitigation)
- [Tools and References](#tools-and-references)
- [Assessment Checklist](#assessment-checklist)

---

## Overview

Kerberos delegation allows a service to act on behalf of a user when accessing another service.

It is used in multi-tier application architectures where a front-end service needs to access a back-end resource using the user's identity.

Delegation is security-sensitive because it can allow one service or computer account to exercise access using another identity.

The three major delegation models are:

1. Unconstrained delegation.
2. Constrained delegation.
3. Resource-Based Constrained Delegation (RBCD).

## Delegation Fundamentals

Delegation is intended to solve a specific authentication problem.

For example:

```text
User
  |
  v
Web Application
  |
  v
Database Server
```

The web application may need to access the database on behalf of the authenticated user.

Delegation determines whether and how that identity can be forwarded.

The security question is:

**Which service can act on behalf of which users, and which resources can it access?**

## Unconstrained Delegation

Unconstrained delegation allows a service or computer configured for delegation to receive delegated Kerberos credentials under applicable conditions.

This is a broad delegation model and can create significant risk if a privileged user authenticates to the delegated system.

### Assessment Considerations

Identify:

- Computers with unconstrained delegation enabled.
- User accounts with unconstrained delegation.
- Privileged users who may authenticate to those systems.
- Whether domain controllers are involved.
- Whether the configuration is operationally required.
- Whether the system is appropriately secured.

### Enumeration

```powershell
Get-ADComputer -Filter * -Properties TrustedForDelegation |
    Where-Object {$_.TrustedForDelegation} |
    Select-Object Name,TrustedForDelegation
```

Review user objects as well:

```powershell
Get-ADUser -Filter * -Properties TrustedForDelegation |
    Where-Object {$_.TrustedForDelegation} |
    Select-Object SamAccountName,TrustedForDelegation
```

Unconstrained delegation should be treated as a high-priority review item, especially on systems that are not tightly controlled.

## Constrained Delegation

Constrained delegation limits the services to which an identity may delegate.

The configuration is commonly represented through the `msDS-AllowedToDelegateTo` attribute.

### Enumeration

```powershell
Get-ADUser -Filter * -Properties msDS-AllowedToDelegateTo |
    Where-Object {$_.'msDS-AllowedToDelegateTo'} |
    Select-Object SamAccountName,msDS-AllowedToDelegateTo

Get-ADComputer -Filter * -Properties msDS-AllowedToDelegateTo |
    Where-Object {$_.'msDS-AllowedToDelegateTo'} |
    Select-Object Name,msDS-AllowedToDelegateTo
```

Review:

- Delegating principal.
- Permitted SPNs.
- Target service.
- Target host.
- Account privilege.
- Business requirement.
- Whether the target service is sensitive.

Constrained delegation reduces the scope of delegation but does not make the configuration automatically safe.

## Resource-Based Constrained Delegation

RBCD allows the resource service to control which principals may delegate to it.

The relevant security configuration is stored in the target object's `msDS-AllowedToActOnBehalfOfOtherIdentity` attribute.

### Assessment Considerations

Review:

- Which principals are allowed to delegate.
- Who can modify the RBCD configuration.
- Whether the resource is sensitive.
- Whether the delegating principal is appropriately trusted.
- Whether the configuration is documented.
- Whether unnecessary delegation entries exist.

### Enumeration

```powershell
Get-ADComputer -Filter * -Properties `
    msDS-AllowedToActOnBehalfOfOtherIdentity |
    Where-Object {$_.'msDS-AllowedToActOnBehalfOfOtherIdentity'} |
    Select-Object Name
```

The security descriptor should be inspected to identify the actual principals granted delegation.

## Protocol Transition

Protocol transition allows a service to transition from a non-Kerberos authentication mechanism to Kerberos when accessing another service.

The `TRUSTED_TO_AUTH_FOR_DELEGATION` account control flag is relevant to this configuration.

Review:

- Whether protocol transition is enabled.
- Which services are permitted.
- Whether the application requires the capability.
- Whether the service account is privileged.
- Whether the configuration follows least privilege.

## Enumeration

Useful account attributes include:

| Attribute | Purpose |
|---|---|
| `TrustedForDelegation` | Indicates unconstrained delegation |
| `TrustedToAuthForDelegation` | Indicates protocol transition configuration |
| `msDS-AllowedToDelegateTo` | Lists constrained delegation targets |
| `msDS-AllowedToActOnBehalfOfOtherIdentity` | Stores RBCD security descriptor |
| `userAccountControl` | Contains relevant account control flags |

Use directory queries, PowerShell and graph analysis to identify delegation relationships.

## Assessment Methodology

### 1. Identify Delegation Configuration

Enumerate user and computer objects with delegation-related attributes.

### 2. Map Delegation Relationships

Identify:

- Delegating principal.
- Target service.
- Target computer.
- Permitted users or identities.
- Configuration owner.

### 3. Assess Privilege

Determine whether the delegating principal or target resource is privileged.

### 4. Review Trust Boundaries

Assess whether the configuration crosses:

- Administrative tiers.
- Domain boundaries.
- Forest boundaries.
- Tenant or business unit boundaries.

### 5. Validate Business Requirement

Confirm whether delegation is required and whether its scope is appropriate.

### 6. Validate Effective Permissions

Review who can modify the relevant account or computer object and its delegation attributes.

### 7. Assess Impact

Determine what access could be obtained if the delegation relationship were abused.

Use isolated environments or explicitly approved test identities for active validation.

## Risk Analysis

| Configuration | Risk considerations |
|---|---|
| Unconstrained delegation | Broad credential delegation exposure |
| Constrained delegation | Risk depends on permitted services and principal privilege |
| RBCD | Risk depends on who can configure the target and which principal is trusted |
| Protocol transition | Risk depends on service scope and authentication design |

A delegation setting is not automatically a vulnerability. Its security impact depends on the principal, target, permissions and operational context.

## Detection

Monitor:

- Changes to delegation-related attributes.
- Changes to computer account configuration.
- Changes to user account control flags.
- Unusual Kerberos service ticket requests.
- Privileged account logons to delegated systems.
- Unexpected service account activity.

Relevant events include:

- 4768 — Kerberos TGT requested.
- 4769 — Kerberos service ticket requested.
- 5136 — Directory object modified.
- 4742 — Computer account changed.
- 4738 — User account changed.

## Mitigation

- Remove unnecessary unconstrained delegation.
- Prefer constrained delegation where appropriate.
- Review RBCD entries.
- Restrict who can modify delegation configuration.
- Protect privileged accounts from delegation.
- Use the Protected Users group where compatible.
- Apply tiered administration.
- Restrict privileged logons to delegated systems.
- Monitor delegation changes.
- Document business justification.
- Review delegation periodically.

## Tools and References

- Active Directory PowerShell.
- BloodHound.
- SharpHound.
- Rubeus.
- Impacket.
- PowerView.
- Microsoft Kerberos documentation.

References:

- [Microsoft — Kerberos authentication overview](https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview)
- [MITRE ATT&CK — Steal or Forge Kerberos Tickets](https://attack.mitre.org/techniques/T1558/)
- [SpecterOps](https://specterops.io/)
- [The Hacker Recipes](https://www.thehacker.recipes/)

## Assessment Checklist

- [ ] Unconstrained delegation enumerated.
- [ ] Constrained delegation enumerated.
- [ ] RBCD configuration reviewed.
- [ ] Protocol transition assessed.
- [ ] Delegating principals identified.
- [ ] Target services identified.
- [ ] Privileged account exposure assessed.
- [ ] Delegation modification permissions reviewed.
- [ ] Business justification confirmed.
- [ ] Detection coverage reviewed.
- [ ] Unnecessary delegation identified.
- [ ] Remediation documented.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
