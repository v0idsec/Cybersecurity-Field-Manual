# BloodHound Reference

## Overview

BloodHound maps relationships and permissions in Active Directory and other supported identity environments.

It helps identify paths between users, groups, computers, permissions and high-value assets.

Official resources:

- https://github.com/SpecterOps/BloodHound
- https://bloodhound.specterops.io/

## SharpHound collection

SharpHound is a data collector used with BloodHound.

Example collection options vary by version. Check the help output for the installed release.

```powershell
# Display collector help
.\SharpHound.exe --help

# Common collection categories
.\SharpHound.exe -c Group,LocalAdmin,Session,Trusts,ACL

# Collect all supported categories
.\SharpHound.exe -c All
```

Collection can generate substantial network traffic and endpoint telemetry. Use only approved collection methods and scope.

## Common collection categories

| Category | Purpose |
|---|---|
| Group | Group membership |
| LocalAdmin | Local administrator relationships |
| Session | Logged-on user sessions |
| Trusts | Domain trust relationships |
| ACL | Directory permissions |
| ObjectProps | Additional object properties |
| Container | Organisational unit and container relationships |
| RDP | Remote Desktop relationships |
| DCOM | DCOM relationships |
| PSRemote | PowerShell remoting relationships |

Supported categories vary between collector versions.

## BloodHound analysis concepts

| Concept | Description |
|---|---|
| Node | User, group, computer, domain or other object |
| Edge | Relationship or permission |
| Path | Sequence of relationships between objects |
| High-value target | Sensitive or privileged asset |
| ACL | Access control list |
| Session | User session on a computer |
| Local admin | Local administrative relationship |
| Trust | Relationship between domains or forests |

## Common relationship types

Examples include:

- `MemberOf`
- `AdminTo`
- `HasSession`
- `GenericAll`
- `GenericWrite`
- `WriteDacl`
- `WriteOwner`
- `AddMember`
- `ForceChangePassword`
- `AllowedToDelegate`
- `TrustedBy`

Interpret relationship direction carefully. The source object and target object matter.

## Assessment workflow

1. Confirm the assessment scope.
2. Identify the relevant domain and collection boundaries.
3. Obtain approval for data collection.
4. Collect only required data.
5. Import data into the approved BloodHound environment.
6. Review high-value assets and privileged relationships.
7. Investigate potentially dangerous paths.
8. Validate findings against the underlying directory configuration.
9. Document evidence and remediation.
10. Securely remove collected data when retention requirements permit.

## Defensive review priorities

- Excessive group membership.
- Unnecessary local administrator access.
- Dangerous directory ACLs.
- Uncontrolled delegation.
- Service accounts with excessive privileges.
- Stale accounts and computers.
- Privileged sessions on lower-trust systems.
- Unnecessary domain trusts.
- Misconfigured high-value assets.

## Reporting a relationship

Record:

| Field | Description |
|---|---|
| Source object | Object with the relevant relationship |
| Target object | Object affected by the relationship |
| Relationship | Permission or relationship type |
| Evidence | Collection data and validation |
| Impact | Potential security consequence |
| Remediation | Permission or configuration change |
| Validation | Evidence that the issue is resolved |

BloodHound paths are investigation leads, not automatically confirmed vulnerabilities. Validate the actual permissions and operational impact before reporting.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
