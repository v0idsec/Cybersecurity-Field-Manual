# Identity and Authentication Hunting

## Overview

Identity infrastructure is a high-value target because compromised accounts can provide access to systems, applications and sensitive information.

Identity-focused threat hunting looks for unusual authentication, account manipulation, privilege abuse and suspicious access patterns.

## Hunting Objectives

- Identify potentially compromised accounts.
- Detect unusual authentication patterns.
- Identify suspicious MFA activity.
- Discover unexpected privilege changes.
- Investigate service account misuse.
- Identify unauthorised application access.

## Active Directory Hunting

### Authentication

Review:

- Event ID 4624 — Successful logon
- Event ID 4625 — Failed logon
- Event ID 4648 — Explicit credentials
- Event ID 4672 — Special privileges assigned
- Event ID 4768 — Kerberos TGT request
- Event ID 4769 — Kerberos service ticket request
- Event ID 4771 — Kerberos pre-authentication failure
- Event ID 4776 — NTLM credential validation

Investigate unusual account, source host, logon type and authentication patterns.

### Account Changes

Monitor:

- Event ID 4720 — User created
- Event ID 4722 — User enabled
- Event ID 4724 — Password reset attempted
- Event ID 4728 — Added to global security group
- Event ID 4732 — Added to local security group
- Event ID 4740 — Account locked out
- Event ID 4738 — User account changed

### Privileged Group Changes

Review changes to:

- Domain Admins
- Enterprise Admins
- Schema Admins
- Administrators
- Backup Operators
- Other organisation-specific privileged groups

Validate changes against approved administrative activity.

## Kerberos Hunting

Potential areas of investigation:

- Unusual service ticket requests
- Unexpected encryption types
- High-volume ticket activity
- Requests for unusual service principal names
- Unusual account behaviour

Kerberos events must be interpreted in context. A high ticket count alone does not prove an attack.

## Microsoft Entra ID Hunting

Investigate:

- Sign-ins from unusual locations
- New device registrations
- Unusual authentication methods
- MFA registration changes
- Unexpected MFA failures
- Risky sign-ins
- Application consent
- Service principal credential changes
- Privileged role assignments

## Example: Failed Sign-ins

### KQL

```kql
SigninLogs
| where TimeGenerated > ago(24h)
| where ResultType != "0"
| summarize
    Attempts = count(),
    Applications = make_set(AppDisplayName)
    by UserPrincipalName, IPAddress
| order by Attempts desc
```

## Example: Successful Sign-ins from Multiple Locations

```kql
SigninLogs
| where TimeGenerated > ago(24h)
| where ResultType == "0"
| summarize
    Locations = make_set(Location),
    IPAddresses = make_set(IPAddress),
    SignInCount = count()
    by UserPrincipalName
| where array_length(Locations) > 1
| order by SignInCount desc
```

Multiple locations do not automatically indicate impossible travel or compromise. Account for VPNs, proxies, mobile networks and legitimate travel.

## Service Account Hunting

Investigate:

- Interactive logons
- Unexpected source systems
- Password changes
- New privileges
- Unusual application access
- New authentication methods

Service accounts should have documented purposes and expected authentication patterns.

## MFA Hunting

Review:

- Unexpected MFA method registration
- Repeated MFA failures
- Unusual MFA approvals
- Authentication method removal
- New device enrolment
- Changes to Conditional Access policies

## Application and OAuth Hunting

Investigate:

- Unusual application consent
- New service principals
- New application credentials
- Unexpected delegated permissions
- Application role assignments
- Unusual API access

## Investigation Workflow

1. Identify the account or identity.
2. Review recent authentication.
3. Establish expected behaviour.
4. Investigate source devices and addresses.
5. Review MFA and authentication methods.
6. Inspect role and group changes.
7. Correlate endpoint activity.
8. Assess possible compromise.
9. Escalate where appropriate.

## Further Reading

- Microsoft Entra Sign-in Logs: https://learn.microsoft.com/entra/identity/monitoring-health/concept-sign-ins
- Microsoft Entra Audit Logs: https://learn.microsoft.com/entra/identity/monitoring-health/concept-audit-logs
- Windows Security Auditing: https://learn.microsoft.com/windows/security/threat-protection/auditing/

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
