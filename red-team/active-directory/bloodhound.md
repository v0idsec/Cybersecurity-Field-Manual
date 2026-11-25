
# BloodHound and Active Directory Attack Path Analysis

> Professional reference guide for modelling Active Directory relationships, identifying privilege escalation paths and prioritising directory security weaknesses.

## Contents

- [Overview](#overview)
- [BloodHound Concepts](#bloodhound-concepts)
- [Directory Data Collection](#directory-data-collection)
- [Graph Structure](#graph-structure)
- [Important Relationships](#important-relationships)
- [Attack Path Analysis](#attack-path-analysis)
- [High-Value Targets](#high-value-targets)
- [Path Validation](#path-validation)
- [Common Analysis Mistakes](#common-analysis-mistakes)
- [Defensive Applications](#defensive-applications)
- [Tools and References](#tools-and-references)
- [Assessment Checklist](#assessment-checklist)

---

## Overview

BloodHound is a graph-based platform for analysing Active Directory relationships and identifying potential attack paths.

It represents directory objects as nodes and relationships as edges.

This allows assessors to identify indirect paths between low-privileged identities and high-value resources.

BloodHound is particularly useful because privilege escalation in Active Directory frequently depends on combinations of permissions, group membership, sessions and configuration rather than a single obvious weakness.

## BloodHound Concepts

### Nodes

Common node types include:

- Users.
- Groups.
- Computers.
- Domains.
- Organisational Units.
- Group Policy Objects.
- Certificate templates.
- Containers.

### Edges

Edges represent relationships or permissions.

Examples include:

- MemberOf.
- AdminTo.
- HasSession.
- GenericAll.
- GenericWrite.
- WriteDACL.
- WriteOwner.
- AllExtendedRights.
- AddMember.
- ForceChangePassword.
- AllowedToDelegate.
- ReadGMSAPassword.

The exact relationships available depend on the BloodHound version and collected data.

## Directory Data Collection

SharpHound is commonly used to collect Active Directory relationship data.

Collection scope should be agreed before execution.

Consider:

- Domain size.
- Collection methods.
- Network impact.
- Domain controller load.
- Endpoint visibility.
- Session collection.
- Local group collection.
- ACL collection.
- Trust collection.

Some collection methods may generate additional endpoint or network activity.

Avoid collecting unnecessary data, especially from systems outside the engagement scope.

### Collection Considerations

Document:

- Collection identity.
- Collection time.
- Target domain.
- Collection methods.
- Excluded systems.
- Data limitations.
- Tool version.

Collection data is a snapshot and may become stale as sessions, memberships and permissions change.

## Graph Structure

A BloodHound graph represents potential relationships rather than guaranteed exploitation.

For example:

```text
User A
  |
  | MemberOf
  v
Group B
  |
  | GenericAll
  v
Computer C
  |
  | AdminTo
  v
Server D
```

This illustrates a possible chain of relationships.

Each edge must be understood in context before assigning security impact.

## Important Relationships

| Relationship | Assessment significance |
|---|---|
| MemberOf | Group membership |
| AdminTo | Local administrative access |
| HasSession | User session observed on a computer |
| GenericAll | Broad control over an object |
| GenericWrite | Ability to modify object attributes |
| WriteDACL | Ability to modify object permissions |
| WriteOwner | Ability to change object ownership |
| AddMember | Ability to modify group membership |
| ForceChangePassword | Ability to reset a user's password |
| AllExtendedRights | Broad extended rights |
| AllowedToDelegate | Delegation relationship |
| ReadGMSAPassword | Access to managed service account password material |

Permissions must be interpreted alongside object type, inheritance and applicable access control rules.

## Attack Path Analysis

### Identify High-Value Targets

Prioritise:

- Domain Admins.
- Enterprise Admins.
- Domain controllers.
- Tier 0 systems.
- Privileged service accounts.
- Certificate authorities.
- Backup infrastructure.
- Identity management systems.

### Analyse Shortest Paths

Shortest paths can help identify relationships between a standard user and a privileged target.

However, shortest does not necessarily mean most practical.

Consider:

- Required privileges.
- Authentication requirements.
- Network reachability.
- Endpoint access.
- Existing sessions.
- Operational risk.
- Whether the relationship is current.

### Analyse Permission Chains

Look for combinations of:

- Group membership.
- Object control.
- Password reset rights.
- GPO modification.
- Local administrative access.
- Delegation.
- Certificate enrollment.
- Trust relationships.

A single permission may be low risk in isolation but significant when combined with another relationship.

### Session-Based Paths

Session information can identify where privileged users have logged in.

Assess:

- Whether the session is current.
- Whether the host is in scope.
- Whether the account is privileged.
- Whether the session represents an active logon.
- Whether the collection data is recent.

Do not treat historical or stale session information as proof of current access.

## High-Value Targets

### Domain Controllers

Domain controllers are critical identity infrastructure.

Review:

- Administrative access.
- GPO control.
- Delegated permissions.
- Service accounts.
- Replication permissions.
- Local security configuration.

### Privileged Groups

Review all direct and nested memberships.

Identify who can modify:

- Group membership.
- Group ownership.
- Group ACLs.
- Relevant parent objects.

### Group Policy Objects

Assess whether an unprivileged principal can modify a GPO that applies to privileged systems.

### Certificate Services

Identify certificate templates and enrollment permissions that may provide a path to privileged identities.

## Path Validation

BloodHound identifies relationships that may create attack paths.

Validation should determine:

1. Whether the relationship exists.
2. Whether it is current.
3. Whether the relevant permission is effective.
4. Whether prerequisites are satisfied.
5. Whether the path crosses a security boundary.
6. Whether the path is exploitable in the assessed environment.
7. What the resulting access would permit.

Use controlled accounts and non-destructive validation wherever possible.

Do not assume that every graph edge represents a directly exploitable vulnerability.

## Common Analysis Mistakes

- Treating every edge as exploitable.
- Relying on stale collection data.
- Ignoring inherited permissions.
- Ignoring object ownership.
- Overlooking nested group membership.
- Confusing local administration with domain administration.
- Ignoring network segmentation.
- Assuming a session is still active.
- Treating a theoretical path as confirmed compromise.
- Failing to assess the impact of each relationship.

## Defensive Applications

BloodHound can support defensive identity reviews.

Use it to:

- Identify excessive permissions.
- Review privileged access paths.
- Find unexpected local administrators.
- Identify dangerous group relationships.
- Review GPO control.
- Assess delegation exposure.
- Identify paths to Tier 0 assets.
- Track remediation progress.

Repeat collection after remediation to confirm that the path has been removed.

## Tools and References

- [BloodHound](https://github.com/SpecterOps/BloodHound)
- [SharpHound](https://github.com/SpecterOps/SharpHound)
- [SpecterOps](https://specterops.io/)
- [The Hacker Recipes](https://www.thehacker.recipes/)
- [MITRE ATT&CK](https://attack.mitre.org/)

## Assessment Checklist

- [ ] Collection scope approved.
- [ ] Collection identity documented.
- [ ] Data collection methods recorded.
- [ ] High-value targets identified.
- [ ] Privileged group relationships reviewed.
- [ ] Dangerous ACL relationships reviewed.
- [ ] Session information assessed for freshness.
- [ ] GPO relationships investigated.
- [ ] Delegation paths reviewed.
- [ ] AD CS relationships investigated.
- [ ] Attack paths manually validated.
- [ ] Theoretical paths distinguished from confirmed access.
- [ ] Remediation paths documented.
- [ ] Follow-up collection planned.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
