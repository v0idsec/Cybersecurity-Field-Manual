# Hardening Tools Reference

## Overview

This document lists tools useful for reviewing, implementing and validating security configurations.

Tools should be selected according to the platform, assessment requirements and available permissions.

Run assessments only against systems you own or are explicitly authorised to assess.

## 1. Cross-platform assessment

| Tool | Purpose |
|---|---|
| CIS-CAT Pro | CIS Benchmark assessment |
| OpenSCAP | Configuration compliance and vulnerability assessment |
| Lynis | Linux and Unix security auditing |
| Nessus | Vulnerability and configuration assessment |
| Qualys | Vulnerability and configuration management |
| Tenable Security Center | Enterprise vulnerability management |
| Nmap | Network service discovery and exposure review |

### Lynis

Lynis performs security audits on Linux and Unix-like systems.

```bash
# Run a local security audit
sudo lynis audit system

# Review Lynis version
lynis show version

# Review available commands
lynis show commands
```

Review findings in context. Lynis recommendations are not automatically appropriate for every workload.

Project: https://cisofy.com/lynis/

### OpenSCAP

OpenSCAP provides tools for security compliance assessment.

```bash
# Check OpenSCAP version
oscap --version

# List available information about a data stream
oscap info security-baseline.xml

# Example XCCDF evaluation
oscap xccdf eval \
  --profile PROFILE_ID \
  --results results.xml \
  security-baseline.xml
```

The data stream and profile must be appropriate for the target operating system.

Project: https://www.open-scap.org/

## 2. Windows tools

| Tool | Purpose |
|---|---|
| Microsoft Security Compliance Toolkit | Windows security baseline assessment and management |
| Policy Analyzer | Compare Group Policy objects and local policy |
| LGPO.exe | Manage local Group Policy |
| Microsoft Defender | Endpoint protection and security monitoring |
| Microsoft Intune | Device and policy management |
| Microsoft Defender for Endpoint | Endpoint detection and response |
| Sysinternals | Windows troubleshooting and investigation utilities |
| Windows Security Baselines | Microsoft-recommended configuration baselines |

### Group Policy Resultant Set

```powershell
# Generate a Group Policy report
gpresult /h gpresult.html

# Display applied computer policy
gpresult /scope computer /v

# Display applied user policy
gpresult /scope user /v
```

### Windows Defender

```powershell
# Review Defender health
Get-MpComputerStatus

# Review Defender preferences
Get-MpPreference

# Review detected threats
Get-MpThreatDetection
```

### Windows Firewall

```powershell
# Review firewall profiles
Get-NetFirewallProfile

# Review enabled rules
Get-NetFirewallRule -Enabled True

# Review listening TCP ports
Get-NetTCPConnection -State Listen
```

References:

- https://learn.microsoft.com/en-us/windows/security/
- https://learn.microsoft.com/en-us/sysinternals/
- https://learn.microsoft.com/en-us/mem/intune/
- https://learn.microsoft.com/en-us/defender-endpoint/

## 3. Linux tools

| Tool | Purpose |
|---|---|
| Lynis | Linux security auditing |
| OpenSCAP | Security compliance assessment |
| auditd | Linux audit framework |
| AIDE | File integrity monitoring |
| Fail2ban | Automated response to repeated authentication failures |
| nftables | Linux packet filtering |
| UFW | Simplified firewall management |
| firewalld | Firewall management |
| AppArmor | Mandatory access control |
| SELinux | Mandatory access control |

### Auditd

```bash
# Check audit service
systemctl status auditd

# Review audit rules
sudo auditctl -l

# Review audit log
sudo ausearch -m USER_LOGIN

# Search audit events by time
sudo ausearch -ts today
```

### AIDE

AIDE can detect changes to files and directories by comparing filesystem state against a stored database.

```bash
# Initialise a database
sudo aide --init

# Check for changes
sudo aide --check
```

Database initialisation and replacement should be controlled. If an attacker can modify both the system and its integrity database, the results may be unreliable.

### Firewall tools

```bash
# UFW status
sudo ufw status verbose

# firewalld status
sudo firewall-cmd --state

# nftables ruleset
sudo nft list ruleset
```

## 4. Cloud security tools

| Platform | Tool | Purpose |
|---|---|---|
| AWS | Security Hub | Centralised security findings |
| AWS | Config | Configuration tracking and compliance |
| AWS | GuardDuty | Threat detection |
| AWS | IAM Access Analyzer | Access policy analysis |
| Azure | Defender for Cloud | Cloud security posture and workload protection |
| Azure | Microsoft Entra ID | Identity and access management |
| Azure | Azure Policy | Configuration governance |
| Google Cloud | Security Command Center | Security posture and threat findings |
| Google Cloud | Cloud Asset Inventory | Asset and configuration visibility |

Use native cloud tools alongside independent reviews where appropriate.

## 5. Configuration baseline resources

| Resource | Description |
|---|---|
| CIS Benchmarks | Security configuration recommendations |
| Microsoft Security Baselines | Microsoft platform security configurations |
| Australian ISM | Australian government information security guidance |
| Essential Eight | Prioritised Australian cyber mitigation strategies |
| NIST SP 800-53 | Security and privacy control catalogue |
| NIST SP 800-70 | Security configuration checklist guidance |
| DISA STIGs | Security Technical Implementation Guides |

References:

- https://www.cisecurity.org/cis-benchmarks
- https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines
- https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism
- https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight
- https://csrc.nist.gov/
- https://public.cyber.mil/stigs/

## 6. Tool selection considerations

Before selecting a tool, consider:

- Supported operating systems.
- Licensing and cost.
- Required privileges.
- Whether assessment is agent-based or agentless.
- Data collection and privacy implications.
- Reporting capabilities.
- Integration with existing SIEM or vulnerability platforms.
- Ability to assess against the required benchmark.
- Operational impact.

## 7. Important operational considerations

- Run assessments within an approved scope.
- Use read-only assessment modes where possible.
- Understand the impact of remediation options.
- Avoid blindly applying automated recommendations.
- Retain assessment evidence securely.
- Protect configuration exports and reports.
- Review false positives and unsupported checks.
- Test changes before production deployment.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
