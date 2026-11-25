# Threat Hunting Data Sources

## Overview

Threat hunting depends on the availability and quality of security telemetry.

The choice of data source should be driven by the hypothesis being investigated.

No single source provides complete visibility into an environment.

## Endpoint Telemetry

### Windows

Useful sources:

- Security Event Log
- Sysmon
- PowerShell Operational
- Windows Defender
- Task Scheduler
- Windows Firewall
- EDR telemetry

Useful activity:

- Process execution
- Authentication
- Service installation
- Scheduled task creation
- Registry modification
- File activity
- Network connections

### Linux

Useful sources:

- systemd journal
- auth.log or secure
- auditd
- SSH logs
- sudo logs
- system service logs
- EDR telemetry

Useful activity:

- Authentication
- Privilege escalation
- Process execution
- Account modification
- Service changes
- Persistence
- Network activity

## Identity Telemetry

### Active Directory

Monitor:

- Successful and failed logons
- Kerberos authentication
- NTLM activity
- Privileged group changes
- Account creation
- Password changes
- Domain controller activity
- Group Policy modifications

### Microsoft Entra ID

Monitor:

- Sign-in logs
- Audit logs
- Conditional Access results
- MFA activity
- Risk detections
- Application consent
- Service principal changes
- Role assignments
- Authentication method changes

## Network Telemetry

### DNS

Useful for:

- Suspicious domain lookups
- Unusual query frequency
- Newly registered domains
- Unexpected DNS resolvers
- Possible tunnelling behaviour

### Firewall

Useful for:

- Unexpected connections
- Blocked traffic
- Unusual outbound access
- Lateral movement
- Administrative changes

### Proxy

Useful for:

- Web requests
- File downloads
- Data uploads
- User activity
- Suspicious destinations

### Network Monitoring

Potential sources:

- Zeek
- Suricata
- NetFlow
- IPFIX
- Packet capture metadata

## Cloud Telemetry

### AWS

- CloudTrail
- GuardDuty
- VPC Flow Logs
- Route 53 Resolver query logs
- AWS Config
- IAM activity

### Azure

- Azure Activity Logs
- Entra ID logs
- Microsoft Defender for Cloud
- Azure Firewall
- NSG flow logs
- Key Vault audit logs

### Google Cloud

- Cloud Audit Logs
- VPC Flow Logs
- Cloud DNS logs
- Security Command Center
- IAM activity

## Application Telemetry

Useful events:

- Authentication
- Authorisation
- Administrative actions
- API access
- Session creation
- File uploads
- Data exports
- Configuration changes

## Data Source Selection

| Hunt Objective | Recommended Sources |
|---|---|
| Credential compromise | Identity, endpoint, VPN |
| Lateral movement | Endpoint, authentication, network |
| Persistence | Endpoint, system logs |
| Data exfiltration | Proxy, firewall, cloud, endpoint |
| Cloud compromise | Cloud audit, IAM, network |
| Malware execution | EDR, Sysmon, antivirus |
| Phishing impact | Email, identity, endpoint |
| Privilege escalation | Endpoint, identity, directory |

## Data Quality

Before relying on a source, assess:

- Collection coverage
- Retention period
- Timestamp accuracy
- Parsing and normalisation
- Event completeness
- Agent health
- Ingestion latency
- Access permissions

## Logging Gaps

Document missing visibility.

Examples:

- Endpoints without EDR
- Servers not forwarding logs
- Cloud audit logging disabled
- Missing DNS telemetry
- Incomplete process command lines
- Insufficient retention

A missing event is not proof that activity did not occur.

## Privacy and Access

- Collect only relevant information.
- Restrict access to sensitive logs.
- Follow organisational monitoring policies.
- Protect personal and customer information.
- Document evidence handling.
- Apply retention requirements.

## Further Reading

- Microsoft Sentinel: https://learn.microsoft.com/azure/sentinel/
- Sysmon: https://learn.microsoft.com/sysinternals/downloads/sysmon
- Zeek: https://docs.zeek.org/
- Suricata: https://docs.suricata.io/
- Wazuh: https://documentation.wazuh.com/

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
