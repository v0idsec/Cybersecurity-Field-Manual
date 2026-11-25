# Physical Security Assessment Guide

An end-to-end workflow for conducting an authorised physical security assessment, covering facility reconnaissance, access controls, visitor management, environmental protections, security monitoring and physical security processes.

This guide is intended for professional physical security assessments and authorised red team engagements. It focuses on assessing security controls, identifying weaknesses and documenting risk without providing instructions for unauthorised entry or bypassing real-world security systems.

## 1. Engagement Preparation

Physical security assessments require particularly clear authorisation and coordination.

### 1.1 Confirm Scope

Document:

- Approved facilities and buildings.
- Specific floors, rooms and restricted areas.
- External grounds and perimeter boundaries.
- Approved assessment dates and times.
- Areas explicitly excluded from testing.
- Permitted assessment activities.
- Whether staff interaction is included.
- Whether access-control testing is included.
- Whether technical security systems are in scope.
- Whether third-party premises are involved.

### 1.2 Confirm Rules of Engagement

Establish:

- Written authorisation from the appropriate property or business owner.
- Named assessment personnel.
- Identification requirements.
- Permitted access arrangements.
- Areas that must not be entered.
- Restrictions on photography and recording.
- Restrictions on interacting with staff or visitors.
- Emergency procedures.
- Security operations contact details.
- Incident escalation procedures.
- Stop-work conditions.

### 1.3 Define Assessment Boundaries

Explicitly determine whether the engagement includes:

| Assessment Area | Example Scope |
|---|---|
| Perimeter security | Fencing, gates, lighting and external boundaries |
| Building access | Entry points, doors and access control |
| Visitor management | Reception, registration and visitor processes |
| Internal security | Restricted areas and internal access boundaries |
| Physical credentials | Badge issuance, management and revocation |
| Security monitoring | CCTV, alarms and monitoring procedures |
| Environmental security | Server rooms, communications rooms and utilities |
| Personnel security | Security awareness and access procedures |
| Hardware exposure | Unattended devices, exposed ports and equipment |

**Deliverable:** Approved physical assessment scope and rules of engagement.

---

## 2. Pre-Assessment Reconnaissance

The objective is to understand the facility, its security arrangements and the organisation's intended access boundaries.

### 2.1 Review Available Documentation

Where provided, review:

- Site plans.
- Building layouts.
- Access-control policies.
- Visitor management procedures.
- Security guard procedures.
- CCTV coverage documentation.
- Alarm response procedures.
- Restricted-area registers.
- Asset inventories.
- Previous assessment reports.

### 2.2 Understand the Environment

Establish:

- Number of buildings.
- Normal operating hours.
- Public-facing areas.
- Staff-only areas.
- Restricted areas.
- Critical infrastructure locations.
- Reception and visitor areas.
- Delivery and loading areas.
- Emergency exits.
- Security monitoring arrangements.

### 2.3 Identify Relevant Security Boundaries

Consider the separation between:

- Public and private property.
- Visitor and staff areas.
- General office and restricted areas.
- Office and infrastructure environments.
- General staff and privileged personnel.
- Tenant and shared building facilities.

### 2.4 Plan Assessment Activities

Prepare an assessment schedule that accounts for:

- Business operating hours.
- Approved testing windows.
- Staff availability.
- Security team coordination.
- Site access arrangements.
- Safety requirements.
- Emergency contacts.

Do not conduct unannounced activities unless they are explicitly authorised as part of the engagement.

---

## 3. Perimeter Security Assessment

Assess whether the facility's external boundaries provide appropriate protection.

### 3.1 Physical Boundaries

Review:

- Fencing.
- Gates.
- Vehicle barriers.
- Boundary walls.
- Signage.
- External doors.
- Windows.
- Loading areas.
- Emergency exits.

### 3.2 Environmental Conditions

Assess:

- External lighting.
- Visibility.
- Vegetation and obstructions.
- Blind spots.
- Maintenance conditions.
- Signage and wayfinding.
- Public access boundaries.

### 3.3 Vehicle and Delivery Access

Where included in scope, review:

- Vehicle entry procedures.
- Delivery verification.
- Contractor access.
- Loading dock security.
- Visitor vehicle management.
- Restricted parking areas.

### 3.4 Assessment Questions

- Are physical boundaries clearly defined?
- Are access points appropriately controlled?
- Are damaged barriers identified and repaired?
- Is lighting sufficient?
- Are restricted areas clearly marked?
- Are delivery and contractor processes documented?
- Are emergency exits appropriately secured and monitored?

Record weaknesses and their potential impact without interfering with normal facility operations.

---

## 4. Building Access Controls

Assess how entry to the building is controlled and monitored.

### 4.1 Entry Point Inventory

Document relevant entry points:

- Main entrances.
- Staff entrances.
- Reception areas.
- Loading docks.
- Car parks.
- Emergency exits.
- Service entrances.
- Shared building access points.

### 4.2 Access Control Mechanisms

Identify the systems used:

- Electronic access cards.
- Mobile credentials.
- PIN-based systems.
- Biometric authentication.
- Reception-controlled entry.
- Mechanical locks.
- Security personnel.

### 4.3 Access Control Review

Assess:

- Whether access is role-based.
- Whether credentials are individually assigned.
- Whether lost credentials are revoked promptly.
- Whether access permissions are periodically reviewed.
- Whether terminated staff lose access.
- Whether access events are logged.
- Whether restricted areas have appropriate controls.
- Whether shared credentials are used.

### 4.4 Access Lifecycle

Review the full credential lifecycle:

1. Request.
2. Approval.
3. Issuance.
4. Permission assignment.
5. Periodic review.
6. Modification.
7. Revocation.
8. Return or disposal.

**Deliverable:** Access-control observations and identified control weaknesses.

---

## 5. Visitor and Contractor Management

Visitor and contractor processes are an important part of physical security.

### 5.1 Visitor Registration

Review:

- Visitor identification requirements.
- Registration procedures.
- Host approval.
- Visitor badges.
- Visitor logs.
- Access restrictions.
- Sign-in and sign-out processes.
- Visitor record retention.

### 5.2 Contractor Management

Assess:

- Contractor identity verification.
- Work authorisation.
- Site induction.
- Access permissions.
- Escort requirements.
- After-hours access.
- Credential expiry.
- Supervision.

### 5.3 Visitor Oversight

Determine whether:

- Visitors are clearly identifiable.
- Visitor access is limited to approved areas.
- Visitors are appropriately escorted.
- Temporary credentials are returned or disabled.
- Hosts are accountable for their visitors.
- Visitor records are protected.

### 5.4 Process Validation

Where permitted, review documented procedures and observe normal visitor processing.

Do not impersonate staff, misrepresent identity or attempt to obtain access through deception unless a specifically authorised social engineering component is included.

---

## 6. Internal Physical Security

Assess how access is controlled within the facility.

### 6.1 Restricted Areas

Identify relevant restricted locations:

- Server rooms.
- Network communications rooms.
- Data centres.
- Records storage.
- Finance departments.
- Executive offices.
- Security control rooms.
- Equipment storage.
- Critical operational areas.

### 6.2 Internal Access Boundaries

Assess:

- Whether restricted areas are clearly identified.
- Whether access is limited to appropriate personnel.
- Whether access permissions are reviewed.
- Whether sensitive areas are monitored.
- Whether visitors are escorted.
- Whether access events are logged.

### 6.3 Tailgating and Access Discipline

Assess organisational controls designed to prevent unauthorised persons from entering secured areas.

Review:

- Staff awareness.
- Access-control policies.
- Visitor escort practices.
- Door security procedures.
- Security guard responsibilities.
- Incident reporting processes.

Testing of access-control bypasses must only occur under explicit authorisation and a pre-agreed safety procedure.

---

## 7. Server Rooms and Critical Infrastructure

Physical access to IT infrastructure can undermine otherwise effective technical security controls.

### 7.1 Server Room Security

Review:

- Physical access restrictions.
- Access logging.
- Environmental monitoring.
- CCTV coverage.
- Fire detection and suppression.
- Cooling and ventilation.
- Water ingress protection.
- Equipment racks.
- Cable management.
- Visitor procedures.

### 7.2 Network Infrastructure

Assess the physical security of:

- Network switches.
- Routers.
- Firewalls.
- Wireless controllers.
- Patch panels.
- Communications cabinets.
- Fibre termination points.
- Network distribution areas.

### 7.3 Workstation and Device Security

Review:

- Unattended workstations.
- Screen locking.
- Device storage.
- Laptop security.
- Removable media controls.
- Exposed connection ports.
- Equipment disposal procedures.

### 7.4 Environmental Controls

Consider:

- Power redundancy.
- UPS protection.
- Generator arrangements.
- Cooling.
- Fire suppression.
- Water detection.
- Environmental alerting.

Do not disconnect, modify or interfere with critical infrastructure during an assessment.

---

## 8. Security Monitoring and Surveillance

Assess whether physical security events are detected, recorded and acted upon.

### 8.1 CCTV

Review:

- Coverage of critical access points.
- Coverage of restricted areas.
- Camera positioning.
- Image quality.
- Recording retention.
- Access to recordings.
- Monitoring arrangements.
- Maintenance procedures.

### 8.2 Alarm Systems

Assess:

- Intrusion detection coverage.
- Alarm monitoring.
- Alert escalation.
- Response procedures.
- Maintenance and testing.
- False alarm handling.

### 8.3 Security Personnel

Where relevant, review:

- Security guard responsibilities.
- Shift handover procedures.
- Incident response training.
- Visitor management.
- Patrol documentation.
- Escalation procedures.

### 8.4 Monitoring and Response

Determine:

- Who receives physical security alerts?
- How are alerts prioritised?
- What response times are expected?
- How are incidents recorded?
- How are security events investigated?
- Are monitoring systems periodically tested?

Avoid accessing, disabling or interfering with surveillance or alarm systems unless a specific controlled test has been authorised.

---

## 9. Social Engineering and Human Factors

Social engineering should be treated as a separate, explicitly approved assessment activity.

Potential assessment areas include:

- Visitor verification.
- Identity verification procedures.
- Security awareness.
- Information disclosure.
- Staff reporting behaviour.
- Contractor verification.
- Physical security policy awareness.

### 9.1 Assessment Controls

Before conducting any social engineering activity, establish:

- Approved scenarios.
- Approved personnel.
- Target groups.
- Excluded personnel.
- Permitted communication methods.
- Prohibited scenarios.
- Safety boundaries.
- Data collection limits.
- Immediate stop conditions.

### 9.2 Avoid Harmful Testing

Do not:

- Threaten or intimidate staff.
- Create unnecessary distress.
- Request personal passwords.
- Collect sensitive personal information unnecessarily.
- Interfere with emergency procedures.
- Impersonate emergency services.
- Create false emergencies.
- Place staff or members of the public at risk.

### 9.3 Reporting Human-Factor Findings

Focus on process weaknesses rather than blaming individuals.

Examples:

- Inconsistent visitor verification.
- Unclear contractor procedures.
- Lack of access-control awareness.
- Inadequate reporting channels.
- Insufficient security training.

---

## 10. Physical Security Findings and Risk Assessment

Assess each identified weakness based on its realistic security implications.

### 10.1 Potential Impact Areas

Consider:

- Unauthorised facility access.
- Access to restricted areas.
- Theft or loss of equipment.
- Exposure of sensitive information.
- Compromise of network infrastructure.
- Disruption of business operations.
- Safety implications.
- Regulatory or contractual exposure.

### 10.2 Risk Factors

Consider:

- Ease of exploitation.
- Required access or privileges.
- Exposure duration.
- Existing controls.
- Monitoring and detection.
- Business criticality.
- Potential consequences.

### 10.3 Avoid Overstating Findings

For example, an unlocked internal door may be an observation, but its severity depends on:

- Where the door leads.
- Who can reach it.
- What assets are behind it.
- Whether additional controls exist.
- Whether access is monitored.

Document the actual conditions rather than assuming the worst-case scenario.

---

## 11. Evidence Collection

Physical security evidence requires careful handling and consideration of privacy.

### 11.1 Evidence Types

Potential evidence includes:

- Photographs of relevant security conditions.
- Approved site diagrams.
- Access-control policy excerpts.
- Sanitised access logs.
- CCTV coverage observations.
- Visitor process observations.
- Equipment inventory details.
- Interview notes.
- Assessment timestamps.

### 11.2 Evidence Handling

- Obtain approval before taking photographs.
- Avoid capturing identifiable people unnecessarily.
- Do not photograph sensitive documents without permission.
- Protect access-control information.
- Redact personal information.
- Record where and when observations were made.
- Store evidence securely.
- Follow retention and disposal requirements.

### 11.3 Evidence Register

Maintain a record containing:

| Field | Description |
|---|---|
| Evidence ID | Unique reference |
| Finding ID | Associated finding |
| Location | Relevant facility or area |
| Date/time | Observation timestamp |
| Evidence type | Photograph, document, observation, etc. |
| Description | What the evidence demonstrates |
| Collector | Assessment team member |
| Handling | Storage and sensitivity requirements |

---

## 12. Reporting

A physical security assessment report should be understandable to both security personnel and business stakeholders.

### 12.1 Executive Summary

Include:

- Assessment objectives.
- Facilities assessed.
- Overall security posture.
- Significant risks.
- Business implications.
- Recommended priorities.

### 12.2 Assessment Overview

Document:

- Assessment dates.
- Locations.
- Scope.
- Exclusions.
- Assessment methodology.
- Activities performed.
- Limitations.

### 12.3 Findings

Each finding should include:

- Finding title.
- Severity.
- Location.
- Description.
- Security control involved.
- Observed condition.
- Potential impact.
- Evidence.
- Remediation.
- References, where applicable.

### 12.4 Recommendations

Recommendations may include:

- Improving access-control policies.
- Reviewing credential permissions.
- Improving visitor management.
- Enhancing restricted-area security.
- Improving CCTV coverage.
- Strengthening monitoring procedures.
- Improving staff awareness.
- Securing exposed infrastructure.
- Reviewing contractor access.
- Improving incident response processes.

### 12.5 Prioritisation

Prioritise findings based on:

1. Immediate safety or critical infrastructure risks.
2. Unauthorised access to sensitive areas.
3. Weaknesses affecting critical IT infrastructure.
4. Credential and access lifecycle weaknesses.
5. Monitoring and detection gaps.
6. General security improvements.

---

## 13. Close-Out

Before concluding the engagement:

- Confirm all assessment activities have stopped.
- Return temporary credentials and badges.
- Confirm temporary access has been revoked.
- Remove approved test artefacts.
- Confirm no security controls were left modified.
- Notify the appropriate facility contact.
- Securely transfer evidence and reports.
- Confirm any outstanding risks.
- Conduct a findings walkthrough where required.

Ensure the facility's normal security arrangements are operating as expected before leaving.

---

## 14. Final Checklist

### Preparation

- [ ] Written authorisation obtained.
- [ ] Facility scope confirmed.
- [ ] Exclusions documented.
- [ ] Rules of engagement approved.
- [ ] Emergency contacts confirmed.
- [ ] Assessment schedule agreed.

### Assessment

- [ ] Perimeter security reviewed.
- [ ] Building access controls assessed.
- [ ] Visitor management reviewed.
- [ ] Contractor management reviewed.
- [ ] Internal restricted areas assessed.
- [ ] Critical infrastructure security reviewed.
- [ ] Surveillance and monitoring reviewed.
- [ ] Environmental controls reviewed.
- [ ] Human-factor activities conducted only where authorised.

### Evidence and Reporting

- [ ] Evidence collected with approval.
- [ ] Personal information protected.
- [ ] Findings validated.
- [ ] Risk ratings assigned.
- [ ] Remediation recommendations documented.
- [ ] Report reviewed.

### Close-Out

- [ ] Temporary credentials returned.
- [ ] Temporary access revoked.
- [ ] Assessment activities stopped.
- [ ] Facility security arrangements confirmed.
- [ ] Evidence securely transferred.
- [ ] Client handover completed.

---

## Related Resources

- `../../red-team/social-engineering/`
- `../../red-team/wireless/`
- `../rules-of-engagement/`
- `../planning/`
- `../evidence/`
- `../reporting/`
- `../templates/`

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
