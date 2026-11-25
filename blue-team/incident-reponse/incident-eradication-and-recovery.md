# Incident Eradication and Recovery

## Overview

Eradication removes the threat and the mechanisms used to maintain access.

Recovery restores affected systems and services to a trusted operational state.

These phases should begin only when responders have sufficient understanding of the incident to avoid restoring a compromised environment.

## Eradication objectives

- Remove malicious code and artefacts.
- Eliminate attacker persistence.
- Remove unauthorised accounts and access.
- Correct exploited vulnerabilities.
- Rotate compromised credentials and secrets.
- Restore security controls.
- Address weaknesses that enabled the incident.

## Eradication activities

### Endpoint remediation

Depending on the incident:

- Rebuild affected systems from trusted images.
- Remove malicious services and scheduled tasks.
- Remove unauthorised software.
- Validate startup and persistence locations.
- Patch exploited vulnerabilities.
- Restore endpoint security controls.
- Review local administrators and permissions.
- Rotate credentials exposed on the device.

For systems with uncertain integrity, rebuilding from a trusted source is generally more defensible than attempting to clean every artefact manually.

### Identity remediation

- Reset compromised credentials.
- Revoke sessions and tokens.
- Rotate API keys and application secrets.
- Remove unauthorised MFA methods.
- Remove malicious application permissions.
- Review privileged roles.
- Review delegated access.
- Investigate service account exposure.
- Validate identity provider configuration.

### Network remediation

- Remove temporary malicious access paths.
- Correct exposed services.
- Patch vulnerable network infrastructure.
- Review firewall and routing changes.
- Restore secure segmentation.
- Rotate exposed network credentials.
- Validate remote access configuration.

### Cloud remediation

- Remove malicious identities and resources.
- Rotate access keys and secrets.
- Correct role assignments and policies.
- Review storage access.
- Remove unauthorised trust relationships.
- Restore security monitoring.
- Validate audit logging.
- Review infrastructure-as-code and deployment pipelines.

## Recovery planning

Before restoring a service, confirm:

- The likely root cause has been addressed.
- Known persistence has been removed.
- Compromised credentials and secrets have been rotated.
- Systems are patched or protected by approved mitigations.
- Backups are known-good and appropriate for restoration.
- Dependencies are understood.
- Security monitoring is operational.
- The system owner has reviewed the recovery plan.

## Backup considerations

A backup should not automatically be considered clean.

Assess:

- Backup creation date.
- Whether the backup predates compromise.
- Whether backup infrastructure was exposed.
- Whether backup credentials were compromised.
- Whether malicious files or configuration changes are present.
- Whether restoration can be tested in an isolated environment.
- Whether immutable or offline copies are available.

Preserve relevant backups and snapshots where they may contain evidence.

## Recovery validation

Validate:

### Security

- Endpoint protection is active.
- Logging and monitoring are functioning.
- Authentication controls are correct.
- Privileged access is restricted.
- Network exposure is appropriate.
- Patches and mitigations are applied.
- No known persistence remains.

### Functionality

- Applications start correctly.
- Data integrity is acceptable.
- Integrations operate correctly.
- Users can perform required business tasks.
- Dependencies are available.
- Performance is acceptable.

### Monitoring

- Increased monitoring is in place.
- Relevant detection rules are enabled.
- High-risk accounts are monitored.
- Network and endpoint activity is reviewed.
- Recovery anomalies are investigated.

## Return to service

Obtain appropriate approval from:

- Incident Commander.
- System owner.
- IT Operations.
- Security team.
- Business owner, where required.

Record any residual risk and obtain formal risk acceptance where appropriate.

## Post-recovery monitoring

For an agreed monitoring period:

- Review authentication activity.
- Monitor endpoint alerts.
- Review network connections.
- Check for renewed persistence.
- Validate backup and security controls.
- Monitor affected applications.
- Investigate unexpected configuration changes.

The monitoring period should be proportionate to the incident and documented.

## Recovery completion criteria

- [ ] Threat activity contained.
- [ ] Known persistence removed.
- [ ] Compromised credentials rotated.
- [ ] Vulnerabilities remediated or mitigated.
- [ ] Systems restored from trusted sources where required.
- [ ] Security controls validated.
- [ ] Business functionality confirmed.
- [ ] Monitoring increased.
- [ ] System owner approval recorded.
- [ ] Residual risks documented.

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
