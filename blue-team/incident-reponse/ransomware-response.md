# Ransomware Response

## Overview

Ransomware incidents can affect the confidentiality, integrity and availability of organisational information and systems.

Modern ransomware incidents may involve more than file encryption. Attackers may steal information, compromise backups, disable security controls, establish persistence and threaten public disclosure.

Treat suspected ransomware as a potentially widespread incident until the scope is understood.

## Immediate priorities

1. Activate the incident response process.
2. Escalate to the appropriate incident commander and management.
3. Assess immediate operational and safety impacts.
4. Identify affected systems and network segments.
5. Contain active encryption and attacker access.
6. Protect unaffected systems and backups.
7. Preserve relevant evidence.
8. Engage specialist responders where appropriate.

## Initial assessment

Determine:

- Which systems display ransom notes or encryption activity?
- Is encryption currently occurring?
- Are shared drives affected?
- Are servers or virtualisation platforms affected?
- Are backup systems accessible or compromised?
- Are privileged accounts involved?
- Is there evidence of data theft?
- Are cloud services affected?
- Is the attacker still active?
- Are critical business or safety systems impacted?

Do not assume that visible encrypted files represent the full extent of the incident.

## Immediate containment

Potential actions:

- Isolate affected endpoints.
- Restrict affected network segments.
- Disable compromised accounts.
- Revoke active sessions.
- Restrict access to backup infrastructure.
- Disable exposed remote access paths where justified.
- Block confirmed malicious infrastructure.
- Protect unaffected systems.
- Suspend compromised integrations.

Avoid broad network shutdowns without assessing operational and safety consequences.

## Preserve evidence

Where practical, preserve:

- Ransom notes.
- File extensions and sample encrypted files.
- EDR alerts.
- Windows and Linux logs.
- Authentication records.
- Firewall and VPN logs.
- Cloud audit logs.
- Backup activity.
- Suspicious processes and command lines.
- Relevant memory or disk evidence.
- Attacker communications.

Do not delete ransom notes or suspicious files before preserving relevant evidence.

## Investigate the attack path

Investigate:

### Initial access

- Exposed remote access.
- Compromised credentials.
- Phishing.
- Exploited vulnerabilities.
- Third-party access.
- Compromised management tools.

### Privilege escalation and movement

- Privileged account use.
- Credential dumping indicators.
- Remote administration activity.
- Remote service execution.
- Unusual authentication patterns.
- Domain or cloud role changes.

### Preparation for impact

- Backup deletion or modification.
- Security tool tampering.
- Mass file access.
- Shadow copy deletion.
- Unusual administrative scripts.
- Data staging and exfiltration.
- Large-scale file modification.

## Backup assessment

Determine whether backups are:

- Available.
- Isolated from the compromised environment.
- Protected from unauthorised deletion.
- Recent enough for recovery objectives.
- Free from known compromise.
- Tested and restorable.

Do not reconnect backup infrastructure to a compromised network without an approved recovery plan.

## Eradication

Potential activities:

- Remove attacker persistence.
- Rebuild compromised systems.
- Patch exploited vulnerabilities.
- Rotate exposed credentials and secrets.
- Review privileged accounts.
- Remove malicious remote access.
- Correct security configuration weaknesses.
- Validate backup infrastructure.
- Review third-party access.

Assume credentials may have been exposed if attackers had access to systems where those credentials were stored or used.

## Recovery

- Restore from known-good backups.
- Rebuild systems from trusted images.
- Validate data integrity.
- Restore services in a controlled order.
- Confirm security controls are active.
- Increase monitoring.
- Obtain business owner approval.
- Document residual risk.

Prioritise restoration based on business impact and system dependencies.

## Ransom payment considerations

Do not make payment decisions independently.

Engage executive management, legal counsel, insurers, law enforcement and specialist incident responders as appropriate.

Consider:

- Whether recovery is possible without payment.
- Whether data was stolen.
- Legal and sanctions implications.
- Whether payment is prohibited or restricted.
- Whether payment would actually result in recovery.
- Whether the attacker may retain access or copies.
- Whether the organisation can meet its obligations to affected parties.

Payment does not guarantee decryption, deletion of stolen information or removal of attacker access.

## Communications

Communications should be coordinated through approved channels.

Avoid:

- Speculating about attribution.
- Claiming data was not accessed without evidence.
- Publishing unverified recovery estimates.
- Sharing sensitive technical details unnecessarily.
- Making independent statements to media or affected parties.

## Closure criteria

- [ ] Active encryption stopped.
- [ ] Attacker access contained.
- [ ] Affected systems identified.
- [ ] Backup integrity assessed.
- [ ] Recovery completed or formally planned.
- [ ] Security controls validated.
- [ ] Potential data exposure assessed.
- [ ] Required stakeholders engaged.
- [ ] Evidence preserved.
- [ ] Post-incident review scheduled.

## Further reading

- [CISA StopRansomware](https://www.cisa.gov/stopransomware)
- [Australian Cyber Security Centre](https://www.cyber.gov.au/)
- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
