# Linux Credentials and Secrets

Credentials and secrets are frequently exposed through configuration files, application deployments, environment variables, backups and insecure permissions.

This guide covers the identification and assessment of sensitive information during authorised security assessments.

The objective is to establish whether secrets are exposed, who can access them and what systems or services may be affected.

Do not copy, export or reuse discovered credentials unnecessarily.

## 1. Common Credential Locations

Potentially sensitive locations include:

| Location | Potential contents |
|---|---|
| `/etc/shadow` | Password hashes |
| `/etc/passwd` | Local account information |
| `/etc/ssh/` | SSH server configuration and host keys |
| `~/.ssh/` | User SSH keys and configuration |
| `/etc/environment` | System-wide environment variables |
| `/etc/profile` | Shell environment configuration |
| `/var/www/` | Web application configuration |
| `/opt/` | Application and deployment files |
| `/root/` | Root account configuration and scripts |
| `/var/backups/` | Backup files |
| `/etc/` | Service and application configuration |

Access should be limited to the authorised scope.

## 2. Password Database Permissions

Inspect password database permissions:

```bash
ls -l /etc/passwd /etc/shadow
```

Review account metadata:

```bash
getent passwd
```

The `/etc/shadow` file contains password hashes and should be accessible only to appropriately privileged users and processes.

Do not include password hashes in reports unless explicitly required and approved.

## 3. SSH Key Exposure

Identify SSH key files:

```bash
find /home /root -type f \( -name "id_rsa" -o -name "id_ed25519" -o -name "id_ecdsa" \) -ls 2>/dev/null
```

Review permissions:

```bash
find /home /root -type d -name ".ssh" -ls 2>/dev/null
```

Assess:

- File ownership.
- Filesystem permissions.
- Key age and rotation practices.
- Whether keys are encrypted with passphrases.
- Whether keys belong to active personnel.
- Whether keys are unnecessarily accessible.

Avoid displaying private key contents in terminal recordings or assessment evidence.

## 4. Environment Variables

Review the current environment:

```bash
env
printenv
```

Review process environment permissions where authorised:

```bash
ps aux
```

Environment variables may contain:

- API tokens.
- Database credentials.
- Cloud access configuration.
- Application secrets.
- Service endpoints.
- Authentication configuration.

Avoid capturing complete environment dumps in reports because they may contain live credentials.

## 5. Application Configuration

Common application configuration files include:

```text
.env
config.php
config.yml
config.yaml
settings.py
application.properties
database.yml
wp-config.php
```

Identify likely configuration files:

```bash
find /var/www /opt -type f \( -name ".env" -o -name "config.php" -o -name "settings.py" -o -name "application.properties" \) -ls 2>/dev/null
```

Review file permissions and ownership before inspecting contents.

Assess:

- Whether secrets are stored in plaintext.
- Whether configuration files are web-accessible.
- Whether secrets are shared between environments.
- Whether credentials have excessive privileges.
- Whether secrets are included in source control.
- Whether credentials are rotated.

## 6. Backup and Archive Exposure

Identify common backup formats:

```bash
find /var/backups /opt /var/www -type f \( -name "*.bak" -o -name "*.backup" -o -name "*.old" -o -name "*.tar" -o -name "*.gz" \) -ls 2>/dev/null
```

Investigate:

- Old configuration files.
- Database exports.
- Archived application directories.
- Unprotected deployment backups.
- Files accessible through web servers.
- Copies containing obsolete credentials.

Do not extract or retain unnecessary sensitive information.

## 7. Database Credentials

Applications commonly store database connection information in configuration files or secret stores.

Look for references to:

- Database usernames.
- Connection strings.
- Password fields.
- Hostnames.
- API endpoints.
- Authentication tokens.

If credentials are exposed, record the location, access conditions and affected application without unnecessarily disclosing the secret itself.

## 8. Cloud and Service Credentials

Review the presence and permissions of common configuration directories:

```bash
ls -lah ~/.aws/
ls -lah ~/.config/
ls -lah ~/.docker/
```

Potentially relevant files include:

```text
~/.aws/credentials
~/.aws/config
~/.docker/config.json
~/.config/gcloud/
```

The presence of a configuration file does not establish that it contains valid or privileged credentials.

Assess:

- File permissions.
- Account ownership.
- Credential scope.
- Expiry and rotation.
- Whether credentials are still active.
- Whether access is restricted to necessary services.

Do not test discovered credentials against external services unless explicitly authorised.

## 9. Git and Source Control

Search for repositories and metadata:

```bash
find /home /opt /var/www -type d -name ".git" -print 2>/dev/null
```

Review repository configuration and deployment practices.

Potential exposure includes:

- Committed `.env` files.
- Hardcoded credentials.
- Historical secrets in repository history.
- Deployment tokens.
- Private configuration files.

If a secret is discovered in version history, deleting the current file is not sufficient. Treat the secret as potentially compromised and recommend rotation.

## 10. Secret Handling During Assessments

When a secret is identified:

1. Record its file path or source.
2. Record the permissions and ownership.
3. Identify the affected application or service.
4. Establish whether the secret is exposed to an unauthorised user.
5. Avoid copying the secret value.
6. Use a redacted evidence sample where possible.
7. Recommend rotation and access restriction.

Example redaction:

```text
DATABASE_PASSWORD=[REDACTED]
```

## 11. Defensive Recommendations

- Use a dedicated secrets management platform.
- Avoid hardcoded credentials.
- Restrict configuration file permissions.
- Rotate exposed credentials immediately.
- Use short-lived credentials where supported.
- Remove obsolete backups.
- Prevent secrets entering source control.
- Monitor sensitive file access.
- Restrict service account privileges.
- Use separate credentials for development and production.

## 12. Assessment Checklist

- [ ] Password database permissions reviewed.
- [ ] SSH key exposure assessed.
- [ ] Environment variables reviewed safely.
- [ ] Application configuration identified.
- [ ] Backup files assessed.
- [ ] Database credentials exposure considered.
- [ ] Cloud configuration reviewed.
- [ ] Source control metadata identified.
- [ ] Secrets redacted in evidence.
- [ ] Rotation and remediation recommendations documented.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
