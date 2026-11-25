
# Active Directory ACLs and Permission Abuse

> Professional reference guide for assessing Active Directory access control lists, object ownership, delegated permissions and privilege escalation risks.

## Contents

- [Overview](#overview)
- [Active Directory Permissions](#active-directory-permissions)
- [Security Descriptors](#security-descriptors)
- [Important Rights](#important-rights)
- [Object Ownership](#object-ownership)
- [Inheritance](#inheritance)
- [High-Risk Permissions](#high-risk-permissions)
- [Common Abuse Scenarios](#common-abuse-scenarios)
- [Assessment Methodology](#assessment-methodology)
- [Validation](#validation)
- [Detection and Defence](#detection-and-defence)
- [Tools and References](#tools-and-references)
- [Assessment Checklist](#assessment-checklist)

---

## Overview

Active Directory uses discretionary access control lists (DACLs) to determine which security principals can access or modify directory objects.

Misconfigured permissions can allow an ordinary domain user to modify accounts, groups, organisational units, Group Policy Objects or other sensitive objects.

The impact depends on:

- Object type.
- Granted access rights.
- Inheritance.
- Effective permissions.
- Object ownership.
- Security principal privileges.
- The relationship between the affected object and privileged resources.

ACL analysis is a critical part of identifying indirect privilege escalation paths.

## Active Directory Permissions

An Active Directory object has a security descriptor containing security-related information.

Important components include:

| Component | Purpose |
|---|---|
| Owner | Security principal that owns the object |
| DACL | Defines access permissions |
| ACE | Individual access control entry |
| SACL | Defines auditing rules |

A DACL contains Access Control Entries (ACEs) that grant or deny specific rights to security principals.

## Security Descriptors

When reviewing an object, consider:

- Owner.
- Inherited permissions.
- Explicit permissions.
- Allow entries.
- Deny entries.
- Object-specific permissions.
- Inheritance flags.
- Effective access.

Do not interpret a single ACE in isolation. Effective access depends on the complete security descriptor and the security context of the requesting principal.

## Important Rights

| Right | Significance |
|---|---|
| GenericAll | Broad control over an object |
| GenericWrite | Ability to modify object attributes |
| WriteDACL | Ability to modify the object's DACL |
| WriteOwner | Ability to change object ownership |
| WriteProperty | Ability to modify specified properties |
| ExtendedRight | Permission to perform an extended operation |
| CreateChild | Ability to create child objects |
| DeleteChild | Ability to delete child objects |
| Delete | Ability to delete an object |
| ReadProperty | Ability to read specified attributes |

### Extended Rights

Some permissions grant access to specific operations rather than general property modification.

Examples include:

- Reset Password.
- Replicating Directory Changes.
- Replicating Directory Changes All.
- Validated writes.

Review the exact right and object type rather than relying on broad permission labels.

## Object Ownership

Object ownership can be security-relevant because owners may have the ability to modify an object's DACL under applicable Windows security rules.

Assess:

- Who owns privileged groups?
- Who owns sensitive user accounts?
- Who owns GPOs?
- Who owns organisational units?
- Can unprivileged users change ownership?
- Are object owners appropriately restricted?

Ownership does not automatically grant unrestricted control in every situation. Validate effective permissions.

## Inheritance

Permissions may be inherited from parent containers.

Review:

- Domain-level permissions.
- Organisational Unit permissions.
- Container permissions.
- Inheritance enabled or disabled.
- Explicit ACEs.
- Inherited ACEs.
- Protected objects.

A permission assigned to a parent OU may affect many descendant objects.

Consider the full scope of an inherited permission before assessing impact.

## High-Risk Permissions

Prioritise permissions that provide control over:

- Privileged user accounts.
- Privileged groups.
- Domain controllers.
- Group Policy Objects.
- Organisational Units containing sensitive systems.
- Service accounts.
- Certificate templates.
- Domain root objects.

Examples of concerning relationships include:

- Ability to reset a privileged user's password.
- Ability to add members to a privileged group.
- Ability to modify a GPO applied to domain controllers.
- Ability to change ACLs on a sensitive object.
- Replication rights granted to an untrusted principal.

## Common Abuse Scenarios

### Password Reset Rights

A principal with effective password reset rights over another account may be able to take control of that account.

Assess:

- Target account privilege.
- Whether the permission is inherited.
- Whether the account is protected.
- Whether password changes trigger monitoring.
- Whether the operation is permitted by the engagement.

### Group Membership Control

A principal able to modify a privileged group's membership may be able to grant themselves or another identity elevated access.

Review:

- Direct group permissions.
- Nested group relationships.
- Group ownership.
- Delegated membership management.
- Administrative tier boundaries.

### WriteDACL

A principal with WriteDACL may be able to modify an object's permissions.

The risk depends on the target object and resulting effective access.

### WriteOwner

A principal with WriteOwner may be able to change the object's owner, potentially creating a route to further permission changes.

Validate the exact ownership and DACL behaviour in a controlled environment.

### Group Policy Control

Permissions over a GPO may provide control over systems where that policy applies.

Assess both:

- Who can modify the GPO.
- Which computers and users receive the GPO.

A GPO linked to a sensitive OU can have substantial impact.

### Replication Rights

Directory replication permissions can expose highly sensitive domain credential material.

Review principals granted replication-related extended rights, particularly outside approved domain controller and identity infrastructure roles.

Treat confirmed unauthorised replication permissions as high-risk.

## Assessment Methodology

1. Identify high-value directory objects.
2. Enumerate object owners.
3. Review explicit and inherited ACEs.
4. Identify dangerous permissions.
5. Determine effective access.
6. Map permissions to privileged targets.
7. Review GPO and OU control.
8. Investigate replication-related rights.
9. Correlate relationships in BloodHound.
10. Validate with controlled test accounts.
11. Document the complete permission chain.

## Validation

A strong finding should establish:

- The principal receiving the permission.
- The affected object.
- The exact access right.
- Whether the permission is effective.
- Whether the permission is inherited.
- The resulting security capability.
- The privilege level of the affected object.

Do not modify privileged group memberships, reset production administrator passwords or alter domain-wide ACLs merely to prove theoretical access.

Where possible, use an isolated lab or a dedicated test object with equivalent permissions.

## Detection and Defence

Review:

- Changes to privileged object ACLs.
- Unexpected ownership changes.
- Privileged group membership changes.
- GPO modifications.
- Delegation changes.
- Replication permission changes.

Relevant Windows Security events may include:

| Event ID | Relevance |
|---|---|
| 4662 | Operation performed on an object |
| 4670 | Permissions on an object changed |
| 4728 | Member added to a security-enabled global group |
| 4732 | Member added to a security-enabled local group |
| 4756 | Member added to a security-enabled universal group |
| 5136 | Directory object modified |
| 5137 | Directory object created |
| 5139 | Directory object moved |
| 5141 | Directory object deleted |

Event availability depends on audit policy and directory service auditing configuration.

## Mitigation

- Apply least privilege.
- Review delegated administration.
- Remove unnecessary ACEs.
- Restrict ownership of privileged objects.
- Review inherited permissions.
- Protect privileged groups.
- Restrict GPO modification rights.
- Audit replication permissions.
- Use tiered administration.
- Monitor privileged directory changes.
- Review permissions after organisational changes.
- Maintain an approved delegation model.

## Tools and References

### Tools

- BloodHound.
- SharpHound.
- Active Directory PowerShell.
- AD ACL inspection utilities.
- PowerView.
- dsacls.
- Impacket.
- PingCastle.

### References

- [Microsoft — Access Control](https://learn.microsoft.com/en-us/windows-server/security/windows-security)
- [Microsoft — Access Control Lists](https://learn.microsoft.com/en-us/windows/win32/secauthz/access-control-lists)
- [SpecterOps](https://specterops.io/)
- [The Hacker Recipes](https://www.thehacker.recipes/)
- [MITRE ATT&CK](https://attack.mitre.org/)

## Assessment Checklist

- [ ] High-value objects identified.
- [ ] Object ownership reviewed.
- [ ] Explicit ACEs reviewed.
- [ ] Inherited ACEs reviewed.
- [ ] Effective permissions assessed.
- [ ] Privileged group control assessed.
- [ ] Password reset permissions reviewed.
- [ ] WriteDACL and WriteOwner relationships reviewed.
- [ ] GPO permissions assessed.
- [ ] Replication rights reviewed.
- [ ] Findings validated without unnecessary production changes.
- [ ] Remediation and monitoring recommendations documented.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
