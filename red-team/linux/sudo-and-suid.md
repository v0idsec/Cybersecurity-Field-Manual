# Sudo and SUID Security

Sudo and SUID provide mechanisms for executing operations with elevated privileges. Incorrect configuration can weaken privilege boundaries and expose administrative functionality.

This guide covers enumeration, assessment and defensive validation.

## 1. Sudo Configuration

Sudo allows authorised users to execute commands as another user, commonly root.

Review current permissions:

```bash
sudo -l
```

Inspect sudo configuration:

```bash
sudo cat /etc/sudoers
sudo ls -lah /etc/sudoers.d/
```

The sudoers file should normally be edited with `visudo`, which performs syntax validation.

## 2. Sudoers Syntax

Example:

```text
username ALL=(ALL:ALL) ALL
```

Common fields:

| Field | Meaning |
|---|---|
| `username` | User or group receiving the rule |
| `ALL` | Applicable hosts |
| `(ALL:ALL)` | Permitted run-as user and group |
| `ALL` | Permitted commands |

Example restricted rule:

```text
username ALL=(root) /usr/bin/systemctl status example.service
```

Assess whether the permitted command can indirectly perform actions beyond its intended purpose.

## 3. Important Sudo Directives

| Directive | Security consideration |
|---|---|
| `NOPASSWD` | Removes password prompting for specified commands |
| `SETENV` | May permit environment variable manipulation |
| `NOEXEC` | Attempts to restrict execution of child processes, but is not a universal security boundary |
| `secure_path` | Defines the executable search path used by sudo |
| `env_reset` | Controls environment variable preservation |
| `Defaults` | Defines global or scoped behaviour |

Review environment handling carefully, particularly where privileged commands depend on environment variables, external programs or user-controlled paths.

## 4. Sudo Environment Assessment

Inspect relevant environment variables:

```bash
env
sudo -V
```

Review sudoers entries for:

- `SETENV`.
- Explicit environment preservation.
- Unsafe executable paths.
- Wildcard command arguments.
- User-controlled configuration files.
- Commands that invoke interpreters or external utilities.

Do not assume that environment variables are preserved or removed without checking the actual sudo configuration.

## 5. SUID Fundamentals

SUID is a permission bit that causes an executable to run with the effective UID of its owner.

Inspect a binary:

```bash
ls -l /usr/bin/passwd
stat /usr/bin/passwd
```

An SUID executable commonly appears with an `s` in the owner's execute position.

Find SUID files:

```bash
find / -type f -perm -4000 -ls 2>/dev/null
```

Find SGID files:

```bash
find / -type f -perm -2000 -ls 2>/dev/null
```

## 6. SUID Assessment

For each unusual executable, establish:

- Owner and group.
- File permissions.
- Package provenance.
- Expected functionality.
- Whether it accepts user-controlled input.
- Whether it accesses files or executes other programs.
- Whether its behaviour creates an unintended privilege boundary.

Check package ownership where supported:

Debian-based systems:

```bash
dpkg -S /path/to/binary
```

RPM-based systems:

```bash
rpm -qf /path/to/binary
```

## 7. GTFOBins

[GTFOBins](https://gtfobins.github.io/) documents security-relevant behaviour in common Unix binaries.

Its categories include:

- Shell.
- Command execution.
- File read.
- File write.
- Upload.
- Download.
- Library load.
- SUID.
- Sudo.
- Capabilities.

Use it to identify whether an exposed binary has behaviour that could undermine the intended privilege restrictions.

A GTFOBins entry is not proof of vulnerability. The installed binary, version, permissions and execution context must match the documented conditions.

## 8. Common Assessment Patterns

Investigate:

- Unrestricted sudo access.
- Broad wildcard command permissions.
- Privileged scripts writable by ordinary users.
- SUID binaries with unnecessary functionality.
- SUID executables that invoke external programs unsafely.
- Incorrect ownership of privileged executables.
- Unexpected SUID files in application directories.
- Dangerous capabilities assigned to executables.

Avoid executing proof-of-concept commands that modify system files or establish persistent access.

## 9. Defensive Recommendations

- Restrict sudo permissions to required commands.
- Avoid broad `ALL` rules.
- Remove unnecessary `NOPASSWD` entries.
- Avoid granting `SETENV` unless justified.
- Keep sudo and privileged packages patched.
- Remove unnecessary SUID and SGID bits.
- Audit executable ownership.
- Ensure privileged scripts are not writable by untrusted users.
- Monitor changes to sudoers and privileged executables.

## 10. Monitoring and Auditing

Identify changes to sudo configuration:

```bash
stat /etc/sudoers
find /etc/sudoers.d -type f -exec stat {} \;
```

Review authentication logs:

Debian-based systems:

```bash
grep sudo /var/log/auth.log
```

RHEL-based systems:

```bash
grep sudo /var/log/secure
```

Where available, use auditd to monitor changes to sensitive files and privileged execution events.

## 11. Assessment Checklist

- [ ] Current sudo permissions reviewed.
- [ ] Sudoers configuration inspected.
- [ ] Included configuration files reviewed.
- [ ] Environment handling assessed.
- [ ] Wildcard rules investigated.
- [ ] SUID and SGID files enumerated.
- [ ] Unusual executables investigated.
- [ ] Package ownership verified.
- [ ] GTFOBins references checked where relevant.
- [ ] Privileged scripts and dependencies assessed.
- [ ] Remediation documented.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
