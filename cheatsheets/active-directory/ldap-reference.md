# LDAP Reference

## LDAP basics

LDAP (Lightweight Directory Access Protocol) provides a standard method for querying and modifying directory services.

Common ports:

| Port | Protocol |
|---|---|
| 389 | LDAP |
| 636 | LDAPS |
| 3268 | Global Catalog |
| 3269 | Global Catalog over TLS |

Use encrypted LDAP connections where supported and required by the environment.

## Distinguished names

Example:

```text
CN=John Smith,OU=Users,DC=example,DC=local
```

Components:

| Component | Meaning |
|---|---|
| CN | Common Name |
| OU | Organisational Unit |
| DC | Domain Component |
| DN | Distinguished Name |

## Useful LDAP attributes

| Attribute | Description |
|---|---|
| `cn` | Common name |
| `name` | Object name |
| `sAMAccountName` | Account name |
| `userPrincipalName` | User principal name |
| `distinguishedName` | Distinguished name |
| `objectClass` | Object class |
| `objectCategory` | Object category |
| `memberOf` | Direct group membership |
| `member` | Group membership objects |
| `servicePrincipalName` | Service principal names |
| `userAccountControl` | Account control flags |
| `pwdLastSet` | Password last-set timestamp |
| `lastLogonTimestamp` | Replicated approximate logon timestamp |
| `description` | Object description |

## LDAP filter syntax

| Operator | Meaning |
|---|---|
| `&` | AND |
| `\|` | OR |
| `!` | NOT |
| `=` | Equality |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |
| `*` | Wildcard |

## Common filters

All user objects:

```text
(objectCategory=person)
```

User objects with the user class:

```text
(&(objectCategory=person)(objectClass=user))
```

Enabled user accounts:

```text
(&(objectCategory=person)(objectClass=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))
```

Disabled user accounts:

```text
(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=2))
```

Accounts with an SPN:

```text
(&(objectCategory=person)(objectClass=user)(servicePrincipalName=*))
```

Computers:

```text
(objectCategory=computer)
```

Groups:

```text
(objectCategory=group)
```

## PowerShell LDAP queries

```powershell
# Search users with LDAP filter
Get-ADUser -LDAPFilter "(objectCategory=person)"

# Search enabled users
Get-ADUser -LDAPFilter "(&(objectCategory=person)(objectClass=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))"

# Search computers
Get-ADComputer -LDAPFilter "(objectCategory=computer)"

# Search accounts with SPNs
Get-ADUser -LDAPFilter "(servicePrincipalName=*)" -Properties ServicePrincipalName

# Search groups
Get-ADGroup -LDAPFilter "(objectCategory=group)"
```

## ldapsearch

Where OpenLDAP tools are available:

```bash
# Anonymous/root-DSE discovery where permitted
ldapsearch -x -H ldap://dc.example.local -s base -b "" namingContexts

# Authenticated query
ldapsearch -x -H ldap://dc.example.local \
  -D "analyst@example.local" -W \
  -b "DC=example,DC=local" \
  "(objectCategory=person)" \
  sAMAccountName

# Query group membership
ldapsearch -x -H ldap://dc.example.local \
  -D "analyst@example.local" -W \
  -b "DC=example,DC=local" \
  "(cn=Domain Admins)" member
```

Use LDAPS or StartTLS where supported. Avoid placing passwords directly in command history or scripts.

## LDAP investigation considerations

- Confirm the search base.
- Confirm the bind identity and permissions.
- Use narrow filters where possible.
- Avoid collecting unnecessary personal information.
- Consider referrals and Global Catalog behaviour.
- Validate attribute values against the source directory.
- Protect exported directory data.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
