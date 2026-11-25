# Cybersecurity Field Manual

A comprehensive cybersecurity knowledge base covering **Red Team, Blue Team and Purple Team operations**. A centralised collection of tools, practical guides, command cheatsheets, methodologies, detection engineering resources, lab environments and security references.

Built as a practical reference for cybersecurity professionals, penetration testers, security analysts, researchers and enthusiasts.

---

## Table of Contents

- [About](#about)
- [Objectives](#objectives)
- [Repository Structure](#repository-structure)
- [Red Team](#red-team)
- [Blue Team](#blue-team)
- [Purple Team](#purple-team)
- [Command Cheatsheets](#command-cheatsheets)
- [Engagement Operations](#engagement-operations)
- [Labs and Training](#labs-and-training)
- [Tools Directory](#tools-directory)
- [Frameworks and Standards](#frameworks-and-standards)
- [Additional Resources](#additional-resources)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)

---

## About

The Cybersecurity Field Manual is an evolving collection of cybersecurity knowledge and resources designed to make practical security information accessible and easy to reference.

Rather than reinventing existing tools, documentation and research, this project aims to bring together high-quality resources from across the cybersecurity community into one organised and searchable location.

Whether you're conducting an authorised penetration test, investigating a security incident, developing detection capabilities, building a home lab or expanding your technical knowledge, this repository aims to provide a useful starting point.

## Objectives

- **Centralise knowledge:** Bring useful cybersecurity resources together in one place.
- **Practical reference:** Provide commands, examples, guides and technical documentation.
- **Offensive security:** Document tools and methodologies used in authorised security assessments.
- **Defensive security:** Support monitoring, threat detection, incident response and security awareness.
- **Purple teaming:** Bridge offensive and defensive security through adversary emulation and detection validation.
- **Continuous learning:** Provide access to labs, training platforms and research material.
- **Community driven:** Encourage contributions, improvements and knowledge sharing.

---

# Red Team

Offensive security resources, methodologies and tooling for authorised penetration testing and security assessments.

| Category | Description |
|---|---|
| [Web Applications](red-team/web-applications/README.md) | Web application and API security testing |
| [Active Directory](red-team/active-directory/README.md) | Windows domains, Kerberos, LDAP and AD security |
| [Network Penetration Testing](red-team/network-pentesting/README.md) | Network discovery, enumeration and assessment |
| [Linux Security](red-team/linux/README.md) | Linux enumeration and privilege escalation |
| [Windows Security](red-team/windows/README.md) | Windows internals, enumeration and security testing |
| [Cloud Security](red-team/cloud/README.md) | AWS, Azure, GCP and cloud infrastructure |
| [OSINT & Reconnaissance](red-team/osint/README.md) | Open-source intelligence and attack surface discovery |
| [Exploitation](red-team/exploitation/README.md) | Vulnerability research and exploit validation |
| [Wireless Security](red-team/wireless/README.md) | Wi-Fi, Bluetooth and wireless assessments |
| [Social Engineering](red-team/social-engineering/README.md) | Authorised social engineering assessments |
| [Physical Security](red-team/physical-security/README.md) | Physical access and hardware security assessments |

### Core Resources

- [HackTricks](https://book.hacktricks.wiki/)
- [The Hacker Recipes](https://www.thehacker.recipes/)
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
- [SecLists](https://github.com/danielmiessler/SecLists)
- [GTFOBins](https://gtfobins.github.io/)
- [LOLBAS](https://lolbas-project.github.io/)
- [Exploit Database](https://www.exploit-db.com/)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)

---

# Blue Team

Defensive security resources covering security operations, monitoring, detection engineering, incident response and security awareness.

| Category | Description |
|---|---|
| [SIEM & EDR](blue-team/siem-edr/README.md) | Security monitoring and endpoint protection |
| [Detection Engineering](blue-team/detection-engineering/README.md) | Detection rules, telemetry and alert development |
| [Threat Hunting](blue-team/threat-hunting/README.md) | Proactive threat identification |
| [Incident Response](blue-team/incident-response/README.md) | Investigation, containment and recovery |
| [Digital Forensics](blue-team/digital-forensics/README.md) | Host, network and memory forensics |
| [Phishing Campaigns](blue-team/phishing/README.md) | Phishing simulations and email security |
| [Cyber Awareness](blue-team/cyber-awareness/README.md) | Security awareness and educational resources |
| [Threat Intelligence](blue-team/threat-intelligence/README.md) | IOC analysis and intelligence platforms |
| [Malware Analysis](blue-team/malware-analysis/README.md) | Malware investigation and reverse engineering |
| [Hardening & Configuration](blue-team/hardening/README.md) | System hardening and security baselines |
| [Vulnerability Management](blue-team/vulnerability-management/README.md) | Vulnerability identification and remediation |

### Core Resources

- [MITRE ATT&CK](https://attack.mitre.org/)
- [Sigma](https://github.com/SigmaHQ/sigma)
- [Wazuh](https://wazuh.com/)
- [Security Onion](https://securityonionsolutions.com/)
- [Velociraptor](https://github.com/Velocidex/velociraptor)
- [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [CyberChef](https://gchq.github.io/CyberChef/)

---

# Purple Team

Resources for collaborative security testing, adversary emulation and validating defensive capabilities.

| Category | Description |
|---|---|
| [Adversary Emulation](purple-team/adversary-emulation/README.md) | Simulating real-world adversary behaviours |
| [MITRE ATT&CK](purple-team/mitre-attack/README.md) | Mapping techniques and adversary activity |
| [Detection Validation](purple-team/detection-validation/README.md) | Testing and validating security detections |
| [Atomic Testing](purple-team/atomic-testing/README.md) | Individual technique-based security tests |
| [Threat-Informed Defence](purple-team/threat-informed-defense/README.md) | Improving security through threat intelligence |
| [Purple Team Exercises](purple-team/exercises/README.md) | Structured offensive and defensive exercises |
| [Attack Simulation](purple-team/attack-simulation/README.md) | Controlled attack simulation environments |
| [Security Metrics](purple-team/security-metrics/README.md) | Measuring detection and response effectiveness |

### Core Resources

- [MITRE CALDERA](https://github.com/mitre/caldera)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)
- [MITRE ATT&CK Navigator](https://github.com/mitre-attack/attack-navigator)
- [Stratus Red Team](https://github.com/Stratus-Red-Team/Stratus-Red-Team)
- [Adversary Emulation Library](https://github.com/center-for-threat-informed-defense/adversary_emulation_library)
- [ThreatHunter Playbook](https://github.com/OTRF/ThreatHunter-Playbook)

---

# Command Cheatsheets

Quick-reference documentation for commonly used commands, tools, protocols and techniques.

| Category | Description |
|---|---|
| [Linux](cheatsheets/linux/README.md) | Bash, permissions, networking and system administration |
| [Windows](cheatsheets/windows/README.md) | CMD, PowerShell, services and Windows internals |
| [Active Directory](cheatsheets/active-directory/README.md) | LDAP, Kerberos, SMB and AD enumeration |
| [Networking](cheatsheets/networking/README.md) | TCP/IP, DNS, routing and network troubleshooting |
| [Web Applications](cheatsheets/web-applications/README.md) | HTTP, headers, cookies, APIs and common vulnerabilities |
| [Tools](cheatsheets/tools/README.md) | Common syntax and usage for security tools |
| [Scripting](cheatsheets/scripting/README.md) | Bash, Python and PowerShell |
| [Cryptography](cheatsheets/cryptography/README.md) | Hashing, encoding, encryption and certificates |
| [SQL](cheatsheets/sql/README.md) | SQL syntax, queries and database administration |
| [Cloud](cheatsheets/cloud/README.md) | AWS, Azure and GCP CLI references |

---

# Engagement Operations

Practical resources for planning, executing, documenting and completing professional security engagements.

| Category | Description |
|---|---|
| [Engagement Planning](engagement-operations/planning/README.md) | Scoping, objectives and preparation |
| [Rules of Engagement](engagement-operations/rules-of-engagement/README.md) | Authorisation, limitations and testing boundaries |
| [Methodologies](engagement-operations/methodologies/README.md) | Structured security assessment approaches |
| [Evidence Collection](engagement-operations/evidence/README.md) | Evidence management and documentation |
| [Reporting](engagement-operations/reporting/README.md) | Findings, risk ratings and recommendations |
| [Templates](engagement-operations/templates/README.md) | Reusable engagement documentation |
| [Post-Engagement](engagement-operations/post-engagement/README.md) | Cleanup, retesting and lessons learned |

---

# Labs and Training

Platforms and environments for developing practical cybersecurity skills.

| Platform | Description |
|---|---|
| [Hack The Box](https://www.hackthebox.com/) | Practical penetration testing labs |
| [TryHackMe](https://tryhackme.com/) | Guided cybersecurity learning |
| [PortSwigger Academy](https://portswigger.net/web-security) | Web application security training |
| [VulnHub](https://www.vulnhub.com/) | Vulnerable virtual machines |
| [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) | Intentionally vulnerable web application |
| [GOAD](https://github.com/Orange-Cyberdefense/GOAD) | Active Directory lab environment |
| [picoCTF](https://picoctf.org/) | Capture the Flag challenges |
| [OverTheWire](https://overthewire.org/wargames/) | Linux and security fundamentals |
| [DetectionLab](https://github.com/clong/DetectionLab) | Detection engineering lab |
| [CyberDefenders](https://cyberdefenders.org/) | Blue team investigation challenges |

---

# Tools Directory

A categorised index of useful cybersecurity tools.

### Offensive Security
- [Nmap](https://nmap.org/)
- [Burp Suite](https://portswigger.net/burp)
- [Metasploit](https://www.metasploit.com/)
- [Impacket](https://github.com/fortra/impacket)
- [NetExec](https://github.com/Pennyw0rth/NetExec)
- [BloodHound](https://bloodhound.specterops.io/)
- [Certipy](https://github.com/ly4k/Certipy)
- [ffuf](https://github.com/ffuf/ffuf)
- [Nuclei](https://github.com/projectdiscovery/nuclei)

### Defensive Security
- [Wazuh](https://wazuh.com/)
- [Suricata](https://suricata.io/)
- [Zeek](https://zeek.org/)
- [Wireshark](https://www.wireshark.org/)
- [Velociraptor](https://github.com/Velocidex/velociraptor)
- [Autopsy](https://www.autopsy.com/)
- [Volatility](https://github.com/volatilityfoundation/volatility3)

### Utility and Research
- [CyberChef](https://gchq.github.io/CyberChef/)
- [Ghidra](https://ghidra-sre.org/)
- [YARA](https://github.com/VirusTotal/yara)
- [Hashcat](https://hashcat.net/hashcat/)
- [John the Ripper](https://www.openwall.com/john/)
- [CyberChef](https://gchq.github.io/CyberChef/)

For additional tools, see the individual team and category directories.

---

# Frameworks and Standards

A reference collection of recognised cybersecurity frameworks, standards and methodologies.

| Framework | Purpose |
|---|---|
| [MITRE ATT&CK](https://attack.mitre.org/) | Adversary tactics and techniques |
| [PTES](http://www.pentest-standard.org/) | Penetration testing methodology |
| [OWASP Top 10](https://owasp.org/www-project-top-ten/) | Web application security risks |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification |
| [NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final) | Technical security testing |
| [NIST CSF](https://www.nist.gov/cyberframework) | Cybersecurity risk management |
| [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) | Secure configuration guidance |
| [ISO 27001](https://www.iso.org/standard/27001) | Information security management |
| [CVSS](https://www.first.org/cvss/) | Vulnerability severity assessment |
| [CWE](https://cwe.mitre.org/) | Common software weaknesses |

---

# Additional Resources

Additional areas of cybersecurity research and exploration.

- **Hardware Hacking:** RFID, NFC, USB, UART, JTAG and microcontrollers.
- **Wireless Security:** Wi-Fi, Bluetooth and wireless protocols.
- **IoT Security:** Embedded systems, firmware and connected devices.
- **Malware Research:** Reverse engineering, static and dynamic analysis.
- **Cryptography:** Encryption, hashing, certificates and cryptographic weaknesses.
- **OSINT:** Public information gathering and intelligence analysis.
- **AI Security:** LLM security, prompt injection and AI application testing.
- **DevSecOps:** Secure development, CI/CD and infrastructure security.
- **Container Security:** Docker, Kubernetes and orchestration security.
- **Physical Security:** Access control, hardware and physical assessments.

---

# Contributing

Contributions, corrections and additional resources are welcome.

If you have a useful tool, guide, cheatsheet, methodology or research resource that would benefit the community, consider contributing.

### Contribution Guidelines

- Provide reliable and relevant resources.
- Prefer official documentation and actively maintained projects.
- Include a short description of each resource.
- Categorise contributions appropriately.
- Avoid duplicate entries.
- Flag deprecated or archived projects.
- Keep documentation clear, practical and easy to navigate.
- Ensure examples and testing instructions are appropriate for authorised environments.

---

# Disclaimer

This repository is intended for **educational purposes, cybersecurity research and authorised security assessments**.

The tools, techniques and resources documented here can have legitimate security applications but may also be misused.

Users are responsible for ensuring they have appropriate authorisation before conducting security testing, scanning, exploitation or other assessment activities.

The repository maintainers do not endorse or accept responsibility for unauthorised access, malicious activity, damage or misuse of the information provided.

Always comply with applicable laws, regulations, organisational policies and engagement-specific Rules of Engagement.
