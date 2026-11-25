# Digital Forensics

Digital forensics is the process of identifying, acquiring, preserving, examining and interpreting digital evidence to support security investigations.

This section provides practical guidance for conducting defensible forensic investigations across endpoints, operating systems, networks, email, browsers and cloud environments.

## Contents

| File | Description |
|---|---|
| [Digital Forensics Fundamentals](digital-forensics-fundamentals.md) | Core principles, terminology and forensic concepts |
| [Forensic Investigation Methodology](forensic-investigation-methodology.md) | Structured investigation workflow |
| [Evidence Acquisition and Preservation](evidence-acquisition-and-preservation.md) | Collection, imaging, hashing and preservation |
| [Chain of Custody](chain-of-custody.md) | Evidence handling and accountability |
| [Disk Forensics](disk-forensics.md) | Storage media, partitions, file systems and artefacts |
| [Memory Forensics](memory-forensics.md) | Volatile memory acquisition and analysis |
| [Windows Forensics](windows-forensics.md) | Windows event logs, registry, execution artefacts and persistence |
| [Linux Forensics](linux-forensics.md) | Linux logs, authentication, processes and file-system artefacts |
| [Browser and Email Forensics](browser-and-email-forensics.md) | Browser activity, email artefacts and message analysis |
| [Network Forensics](network-forensics.md) | Packet capture, flow analysis and network evidence |
| [Cloud Forensics](cloud-forensics.md) | Cloud audit logs, identity events and workload evidence |
| [Digital Forensics Tools Reference](digital-forensics-tools-reference.md) | Common forensic tools and example workflows |

## Investigation Principles

- Obtain appropriate authority before collecting or examining data.
- Preserve original evidence wherever possible.
- Document every collection and examination action.
- Record timestamps, time zones and clock discrepancies.
- Calculate cryptographic hashes to verify evidence integrity.
- Use validated tools and document their versions.
- Maintain a complete chain of custody.
- Separate observed facts from assumptions and interpretations.
- Protect sensitive information encountered during investigations.
- Preserve evidence before performing destructive remediation where practical.

## Typical Investigation Workflow

1. Establish authority, scope and objectives.
2. Identify relevant evidence sources.
3. Assess volatility and collection priorities.
4. Acquire evidence using appropriate methods.
5. Verify integrity and document provenance.
6. Examine forensic copies or collected datasets.
7. Correlate artefacts into an event timeline.
8. Develop and test investigative hypotheses.
9. Document findings, limitations and conclusions.
10. Securely retain or dispose of evidence according to policy.

## Important Considerations

Digital evidence may contain personal, confidential or legally protected information. Investigators must follow applicable legislation, organisational policies, privacy requirements and engagement authorisations.

Live acquisition can change system state. Record the collection method, tools used, commands executed and any known impact.

A hash proves that data has not changed relative to the hashed reference. It does not independently prove that the evidence was authentic before collection or that the collection process was complete.

## Related Sections

- [Incident Response](../incident-response/README.md)
- [Threat Hunting](../threat-hunting/README.md)
- [SIEM and EDR](../siem-edr/README.md)
- [Vulnerability Management](../vulnerability-management/README.md)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
