# Windows Registry and Access Control Lists

A reference for assessing Windows filesystem permissions, registry permissions, ownership, inheritance and security descriptors.

Incorrect access control can expose sensitive data, permit unauthorised configuration changes or create privilege escalation opportunities.

## 1. Windows Access Control Overview

Windows uses security descriptors to define access to securable objects.

A security descriptor can include:

- Owner SID.
- Primary group SID.
- Discretionary Access Control List (DACL).
- System Access Control List (SACL).

### 1.1 DACL

A DACL determines which principals are allowed or denied access to an object.

### 1.2 SACL

A SACL defines auditing rules for access to an object.

### 1.3 Access Control Entries

An Access Control Entry (ACE) specifies a principal and the permissions granted or denied.

Assessment must consider the effective access resulting from:

- User identity.
- Group membership.
- Explicit permissions.
- Inherited permissions.
- Deny entries.
- Object type.
- Mandatory integrity controls.

## 2. Filesystem Permission Enumeration

### 2.1 ICACLS

```cmd
icacls "C:\Program Files\Example"
```

### 2.2 Recursive Review

```cmd
icacls "C:\ProgramData\Example" /T
```

Use recursive enumeration selectively on large directories.

### 2.3 PowerShell

```powershell
Get-Acl 'C:\Program Files\Example' |
    Format-List Owner, AccessToString
```

### 2.4 Detailed Access Rules

```powershell
$acl = Get-Acl 'C:\Program Files\Example'

$acl.Access |
    Select-Object IdentityReference, FileSystemRights, AccessControlType,
        IsInherited, InheritanceFlags, PropagationFlags
```

## 3. Important Filesystem Permissions

Review the effective access granted to:

| Permission | Security Relevance |
|---|---|
| FullControl | Broad modification and permission control |
| Modify | Can modify object contents |
| Write | Can write to the object |
| WriteData | Can modify file contents |
| CreateFiles | Can create files in a directory |
| Delete | Can remove objects |
| ChangePermissions | Can alter access rules |
| TakeOwnership | Can take ownership |

The impact depends on the object and how privileged processes use it.

## 4. High-Value Locations

Review permissions on:

- `C:\Windows\System32`
- `C:\Program Files`
- `C:\Program Files (x86)`
- `C:\ProgramData`
- Service executable directories.
- Application update directories.
- Startup locations.
- Scheduled task script locations.
- Deployment directories.
- Shared application data.

Do not assume every writable directory is a vulnerability.

The relevant question is whether the directory contains or influences an object trusted by a more privileged process.

## 5. Ownership Assessment

Inspect ownership:

```powershell
(Get-Acl 'C:\Program Files\Example').Owner
```

Assess:

- Unexpected ownership.
- User-owned privileged executables.
- Inappropriate ownership of shared directories.
- Ability to change permissions.
- Whether ownership aligns with administrative responsibilities.

## 6. Inheritance

Windows ACLs can inherit permissions from parent directories.

Inspect:

```powershell
$acl = Get-Acl 'C:\Program Files\Example'

$acl.AreAccessRulesProtected

$acl.Access |
    Select-Object IdentityReference, FileSystemRights, IsInherited
```

Review whether:

- Inheritance is enabled appropriately.
- Parent permissions are overly broad.
- Explicit permissions override intended restrictions.
- Deny entries create unexpected access behaviour.
- Sensitive subdirectories have appropriate isolation.

## 7. Effective Access Assessment

Use Sysinternals AccessChk to inspect effective access.

Examples:

```cmd
accesschk.exe -d "C:\Program Files\Example"

accesschk.exe -w "C:\Program Files\Example"
```

For a particular account:

```cmd
accesschk.exe -d -w <account> "C:\Program Files\Example"
```

Verify syntax and output against the installed AccessChk version.

Effective access should be assessed in the context of the actual account and token.

## 8. Registry Overview

The Windows Registry stores system, application, user and security configuration.

Common hives:

| Hive | Description |
|---|---|
| HKEY_LOCAL_MACHINE | Machine-wide configuration |
| HKEY_CURRENT_USER | Current user configuration |
| HKEY_CLASSES_ROOT | Class and file association information |
| HKEY_USERS | Loaded user profiles |
| HKEY_CURRENT_CONFIG | Current hardware profile |

PowerShell provides registry drives such as `HKLM:` and `HKCU:`.

## 9. Registry Enumeration

```powershell
Get-ChildItem HKLM:\SOFTWARE

Get-ChildItem HKCU:\SOFTWARE

Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion'
```

Inspect a key's permissions:

```powershell
Get-Acl 'HKLM:\SOFTWARE\Example' |
    Format-List Owner, AccessToString
```

## 10. High-Value Registry Locations

Review permissions and configuration associated with:

- Service configuration.
- Startup execution.
- Application installation.
- Security policies.
- Windows Defender.
- UAC.
- Remote access.
- Installer behaviour.
- Application control.

Example service configuration location:

```text
HKLM\SYSTEM\CurrentControlSet\Services
```

Example machine-wide application configuration:

```text
HKLM\SOFTWARE
```

Do not modify security-sensitive registry values during routine assessment.

## 11. Registry Access Control

Assess:

- Whether standard users can modify privileged service configuration.
- Whether application configuration is writable.
- Whether security policy keys are protected.
- Whether startup configuration is appropriately restricted.
- Whether inheritance is correct.
- Whether unexpected principals have write permissions.

A writable registry key is only security-relevant when the affected value or object influences a privileged operation or security boundary.

## 12. File and Registry Permission Differences

Filesystem ACLs and registry ACLs use related Windows security concepts but different access masks and object models.

Do not assume that a permission name or numeric value has identical meaning across both object types.

Use the appropriate inspection tools for each.

## 13. Common Assessment Findings

Potential findings include:

- Standard users can modify privileged application binaries.
- Service directories are writable by unprivileged users.
- Scheduled task scripts have excessive write permissions.
- Registry keys permit unintended configuration changes.
- Sensitive configuration files are readable by broad groups.
- Inheritance exposes restricted data.
- Unexpected users own security-sensitive objects.
- Application update directories are insufficiently protected.

## 14. Validation

For each suspected issue:

1. Identify the object.
2. Identify the current account and groups.
3. Inspect explicit and inherited permissions.
4. Establish effective access.
5. Determine whether a privileged process trusts the object.
6. Validate the security impact in an approved environment.
7. Document the result.

Avoid modifying protected files or registry keys merely to demonstrate a suspected weakness.

## 15. Remediation

Recommended controls:

- Apply least-privilege ACLs.
- Remove unnecessary write permissions.
- Protect privileged executable directories.
- Correct ownership.
- Review inheritance.
- Restrict service and task configuration.
- Protect security-sensitive registry keys.
- Audit permission changes.
- Review application installation and update paths.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
