# Log Sources and Telemetry

## Overview

Effective security monitoring requires visibility across endpoints, identities, networks, applications and cloud infrastructure.

This guide identifies common telemetry sources, their security value and important collection considerations.

## Endpoint Telemetry

### Windows

Important sources include:

- Windows Security Event Log
- System Event Log
- Application Event Log
- PowerShell Operational
- Sysmon
- Microsoft Defender
- Windows Firewall
- Task Scheduler
- Windows Filtering Platform

Useful activity includes:

- Process creation
- Authentication
- Account changes
- Privilege assignment
- Service installation
- Scheduled task creation
- PowerShell execution
- Network connections
- Security configuration changes

### Linux

Important sources include:

- `/var/log/auth.log`
- `/var/log/secure`
- `/var/log/syslog`
- `/var/log/messages`
- systemd journal
- auditd
- SSH logs
- sudo logs
- Web server access logs

Useful activity includes:

- Authentication success and failure
- sudo execution
- SSH sessions
- User and group modifications
- Service changes
- Process execution
- Scheduled task changes
- Package installation
- Kernel and system events

## Identity Telemetry

Identity infrastructure is a high-value monitoring source.

### Active Directory

Monitor:

- Successful and failed authentication
- Kerberos activity
- NTLM authentication
- Account creation
- Account deletion
- Password changes
- Group membership changes
- Privileged group modifications
- Group Policy changes
- Domain controller activity

### Microsoft Entra ID

Monitor:

- Interactive sign-ins
- Non-interactive sign-ins
- Conditional Access results
- MFA activity
- Risk detections
- Application consent
- Service principal changes
- Role assignments
- Authentication method changes

## Network Telemetry

### Firewalls

Useful events include:

- Allowed connections
- Blocked connections
- Administrative changes
- VPN activity
- Configuration modifications
- Policy changes

### DNS

DNS telemetry can reveal:

- Connections to suspicious domains
- Domain generation algorithm activity
- Newly registered domains
- Unusual query volumes
- DNS tunnelling indicators
- Unexpected external resolvers

### Proxy and Web Gateway

Monitor:

- Requested URLs
- HTTP methods
- Response codes
- User identity
- Destination categories
- Download activity
- Upload activity
- Blocked requests

### Network Detection

Additional sources may include:

- NetFlow
- IPFIX
- Zeek
- Suricata
- IDS/IPS alerts
- Packet capture metadata

## Cloud Telemetry

### AWS

Relevant sources:

- CloudTrail
- GuardDuty
- VPC Flow Logs
- Route 53 Resolver query logs
- AWS Config
- Security Hub
- IAM activity

### Microsoft Azure

Relevant sources:

- Azure Activity Logs
- Entra ID sign-in logs
- Entra audit logs
- Microsoft Defender for Cloud
- Azure Firewall
- NSG flow logs
- Key Vault audit logs

### Google Cloud

Relevant sources:

- Cloud Audit Logs
- VPC Flow Logs
- Cloud DNS logs
- Security Command Center
- IAM audit activity
- Cloud Logging

## Application Telemetry

Applications can provide visibility into:

- Authentication events
- Authorisation failures
- Administrative actions
- API requests
- Session creation
- File uploads
- Data exports
- Configuration changes
- Errors and exceptions

Application logs should be assessed for sensitive information exposure.

Avoid logging passwords, access tokens, session cookies or unnecessary personal information.

## Telemetry Coverage Matrix

| Security Activity | Useful Sources |
|---|---|
| Credential attacks | Identity, endpoint, VPN |
| Privilege escalation | Endpoint, identity, directory |
| Lateral movement | Endpoint, authentication, network |
| Data exfiltration | Proxy, firewall, endpoint, cloud |
| Persistence | Endpoint, directory, cloud |
| Phishing | Email gateway, endpoint, identity |
| Cloud compromise | Cloud audit, IAM, network |
| Malware execution | EDR, Sysmon, antivirus |

## Collection Priorities

Prioritise telemetry based on:

1. Threat exposure
2. Business criticality
3. Attack surface
4. Detection requirements
5. Collection cost
6. Retention requirements

## Logging Health

Monitor for:

- Missing expected events
- Sudden drops in volume
- Ingestion latency
- Agent failures
- Collector outages
- Parsing errors
- Timestamp inconsistencies
- Unexpected configuration changes

## Operational Considerations

- Protect log integrity.
- Use secure forwarding.
- Restrict access to sensitive telemetry.
- Synchronise system clocks.
- Establish retention requirements.
- Document collection coverage.
- Monitor logging service health.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
