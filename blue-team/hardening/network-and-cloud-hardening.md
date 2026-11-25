# Network and Cloud Hardening

## Overview

Network and cloud hardening reduces opportunities for unauthorised access, lateral movement, data exposure and infrastructure compromise.

The goal is to make access explicit, restrict unnecessary connectivity and ensure that infrastructure is securely configured and monitored.

## 1. Network segmentation

Network segmentation separates systems according to their function, sensitivity and trust level.

Common segmentation boundaries include:

- User workstations.
- Servers.
- Management infrastructure.
- Production environments.
- Development and testing environments.
- Guest wireless networks.
- Internet-facing services.
- Backup infrastructure.
- Operational technology (OT).

Recommended practices:

- Avoid flat networks where practical.
- Restrict traffic between security zones.
- Permit only required protocols and destinations.
- Isolate management interfaces.
- Restrict access to backup infrastructure.
- Review inter-segment firewall rules.
- Monitor unexpected cross-zone connections.

Segmentation should reflect actual business dependencies rather than arbitrary network boundaries.

## 2. Firewall and network access controls

Review:

- Inbound rules.
- Outbound rules.
- Inter-VLAN routing.
- Internet egress.
- Management access.
- Remote access.
- Administrative protocols.
- Temporary firewall exceptions.

For each rule, document:

- Source.
- Destination.
- Protocol and port.
- Business purpose.
- Owner.
- Approval.
- Review or expiry date.

Remove obsolete rules through an approved change process.

## 3. Network device management

Secure routers, switches, wireless controllers and firewalls.

Recommended controls:

- Change default credentials.
- Use centralised authentication where appropriate.
- Restrict management interfaces.
- Use secure management protocols.
- Disable unused services.
- Apply vendor security updates.
- Back up configurations securely.
- Restrict configuration changes.
- Monitor administrative activity.
- Use dedicated management networks where practical.

Prefer secure management protocols such as SSH and HTTPS over Telnet and unencrypted HTTP.

SNMPv3 should be preferred over older SNMP versions where supported and compatible.

## 4. Wireless security

Consider:

- WPA3 or appropriately configured WPA2-Enterprise.
- 802.1X authentication for managed enterprise networks.
- Separate guest wireless access.
- Client isolation where appropriate.
- Restricted wireless management interfaces.
- Secure wireless controller administration.
- Detection of unauthorised access points.
- Regular review of wireless credentials and certificates.

Avoid using a shared guest password as the only control protecting internal resources.

## 5. Remote access

Remote access should be authenticated, restricted and monitored.

Recommended practices:

- Require MFA.
- Use approved VPN, ZTNA or remote access gateways.
- Avoid exposing administrative services directly to the internet.
- Restrict access based on device health and identity.
- Monitor unusual access patterns.
- Remove inactive remote access accounts.
- Review third-party access regularly.
- Apply session timeouts appropriate to the risk.

## 6. DNS and web security

Review:

- DNS resolver configuration.
- DNS administrative access.
- Zone transfer restrictions.
- Domain registration security.
- DNS logging.
- Protective DNS capabilities.
- Web filtering.
- Certificate management.
- Secure TLS configuration.

Where supported, use DNS security controls to detect or block access to known malicious infrastructure.

## 7. Cloud shared responsibility

Cloud providers secure parts of the underlying platform, but customers remain responsible for many configuration and identity controls.

The responsibility split depends on the service model.

| Area | Common customer responsibilities |
|---|---|
| Identity | Users, roles, MFA and permissions |
| Data | Classification, access and protection |
| Network | Security groups, routing and exposure |
| Workloads | Operating system and application security where customer-managed |
| Storage | Access policies, encryption and retention |
| Logging | Enabling, retaining and monitoring customer-visible logs |
| Secrets | Secure storage, access and rotation |
| Configuration | Secure deployment and ongoing assessment |

Do not assume that using a managed cloud service removes the need for security configuration.

## 8. Cloud identity and permissions

Apply least privilege to cloud users, roles and workloads.

Review:

- Human administrator roles.
- Workload identities.
- Cross-account or cross-subscription access.
- Federated identity relationships.
- Temporary credentials.
- Service principals and application registrations.
- API keys and access tokens.
- Privileged role assignments.

Prefer short-lived credentials and managed identities where supported.

Avoid long-lived access keys embedded in scripts, repositories or application configuration.

## 9. Cloud network security

Recommended controls:

- Restrict public IP exposure.
- Limit inbound security group rules.
- Avoid unrestricted management access.
- Segment workloads.
- Restrict outbound access where justified.
- Protect private endpoints.
- Review peering and transit connectivity.
- Monitor network flow logs.
- Restrict access to control-plane interfaces.

Publicly exposed services should have an identified owner, documented purpose and appropriate protective controls.

## 10. Cloud storage and data protection

Review:

- Public access settings.
- Bucket and container permissions.
- Anonymous access.
- Encryption at rest.
- Encryption in transit.
- Key management.
- Backup configuration.
- Data retention.
- Cross-region replication.
- Access logging.

Do not rely on encryption alone. Access controls and key management remain critical.

## 11. Cloud logging and monitoring

Enable relevant audit and activity logs.

Examples include:

- AWS CloudTrail.
- AWS VPC Flow Logs.
- Microsoft Azure Activity Log.
- Microsoft Entra sign-in and audit logs.
- Azure resource diagnostic logs.
- Google Cloud Audit Logs.
- Cloud firewall and network telemetry.

Forward important logs to a protected central platform.

Monitor for:

- Public exposure changes.
- New privileged roles.
- Security group modifications.
- Logging being disabled.
- Unusual API activity.
- New access keys.
- Suspicious data access.
- Unexpected workload creation.
- Changes to encryption or backup settings.

## 12. Validation checklist

- [ ] Network zones and trust boundaries documented.
- [ ] Inter-segment access restricted.
- [ ] Firewall rules have owners and purposes.
- [ ] Management interfaces restricted.
- [ ] Network devices use secure management protocols.
- [ ] Wireless networks appropriately segmented.
- [ ] Remote access requires strong authentication.
- [ ] Public cloud exposure reviewed.
- [ ] Cloud IAM follows least privilege.
- [ ] Workload credentials protected.
- [ ] Storage public access reviewed.
- [ ] Encryption and key management assessed.
- [ ] Cloud audit logs enabled.
- [ ] Network telemetry collected.
- [ ] Backup infrastructure protected.

## References

- [CIS Controls](https://www.cisecurity.org/controls)
- [AWS Security Best Practices](https://docs.aws.amazon.com/security/)
- [Microsoft Azure Security Documentation](https://learn.microsoft.com/en-us/azure/security/)
- [Google Cloud Security Best Practices](https://cloud.google.com/security/best-practices)
- [NIST SP 800-207 — Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [Australian Information Security Manual](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
