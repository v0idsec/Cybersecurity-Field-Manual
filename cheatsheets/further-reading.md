# Further Reading & Resources

A curated collection of external documentation, tools, learning platforms and technical references for cybersecurity professionals.

This page is intended as a starting point for further learning. It links to useful resources rather than duplicating information already covered throughout this handbook.

Resources are grouped by subject and include official documentation wherever possible.

---

# 1. Red Team Tools

Tools commonly used during authorised penetration testing, vulnerability assessments, reconnaissance and security research.

| Tool | Description | Documentation |
|---|---|---|
| Nmap | Network discovery and port scanning | [Official Documentation](https://nmap.org/book/) |
| Burp Suite | Web application security testing | [Documentation](https://portswigger.net/burp/documentation) |
| Metasploit | Penetration testing and exploit development framework | [Documentation](https://docs.metasploit.com/) |
| Hashcat | Password recovery and hash auditing | [Wiki](https://hashcat.net/wiki/) |
| John the Ripper | Password security auditing | [Documentation](https://www.openwall.com/john/doc/) |
| Gobuster | Directory, DNS and virtual host discovery | [GitHub](https://github.com/OJ/gobuster) |
| ffuf | Web application fuzzing | [GitHub](https://github.com/ffuf/ffuf) |
| SQLmap | Automated SQL injection testing | [GitHub](https://github.com/sqlmapproject/sqlmap) |
| BloodHound | Active Directory relationship analysis | [Documentation](https://bloodhound.readthedocs.io/) |
| Impacket | Python tools for network protocols and Windows environments | [GitHub](https://github.com/fortra/impacket) |
| Responder | Network protocol analysis and authorised assessment tooling | [GitHub](https://github.com/lgandx/Responder) |
| Nuclei | Template-based vulnerability scanning | [Documentation](https://docs.projectdiscovery.io/tools/nuclei/overview) |
| Wireshark | Network protocol analysis | [Documentation](https://www.wireshark.org/docs/) |

**Additional resources:**

- [Kali Linux Documentation](https://www.kali.org/docs/)
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
- [SecLists](https://github.com/danielmiessler/SecLists)
- [GTFOBins](https://gtfobins.org/)
- [LOLBAS](https://lolbas-project.github.io/)
- [Exploit Database](https://www.exploit-db.com/)

*Use dual-purpose security tools only within systems and environments you are authorised to assess.*

---

# 2. Blue Team Tools

Tools commonly used for security monitoring, incident response, threat hunting, digital forensics and defensive operations.

| Tool | Description | Documentation |
|---|---|---|
| Microsoft Defender | Endpoint protection and security monitoring | [Microsoft Learn](https://learn.microsoft.com/en-us/defender/) |
| Microsoft Sentinel | Cloud-native SIEM and security analytics | [Documentation](https://learn.microsoft.com/en-us/azure/sentinel/) |
| Splunk | Log management, search and security analytics | [Documentation](https://docs.splunk.com/) |
| Wazuh | Open-source SIEM and XDR platform | [Documentation](https://documentation.wazuh.com/) |
| Wireshark | Network traffic and packet analysis | [Documentation](https://www.wireshark.org/docs/) |
| Zeek | Network security monitoring and traffic analysis | [Documentation](https://docs.zeek.org/) |
| Suricata | Network intrusion detection and prevention | [Documentation](https://docs.suricata.io/) |
| Sysmon | Detailed Windows system activity logging | [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) |
| Velociraptor | Endpoint visibility and digital forensic investigation | [Documentation](https://docs.velociraptor.app/) |
| Volatility 3 | Memory forensics framework | [Documentation](https://volatility3.readthedocs.io/) |
| Autopsy | Digital forensic investigation platform | [Documentation](https://www.autopsy.com/support/) |
| KAPE | Windows forensic artefact collection and processing | [GitHub](https://github.com/EricZimmerman/KapeFiles) |

**Additional resources:**

- [Sigma Rules](https://sigmahq.io/)
- [YARA](https://yara.readthedocs.io/)
- [Sysinternals Suite](https://learn.microsoft.com/en-us/sysinternals/)
- [Security Onion](https://docs.securityonion.net/)
- [The DFIR Report](https://thedfirreport.com/)
- [SANS Digital Forensics Resources](https://www.sans.org/white-papers/)

---

# 3. Networking

Resources for understanding network architecture, protocols, infrastructure and troubleshooting.

| Topic | Resource | Description |
|---|---|---|
| TCP/IP | [RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) | TCP protocol specification |
| DNS | [Cloudflare Learning Centre](https://www.cloudflare.com/learning/dns/what-is-dns/) | DNS fundamentals |
| HTTP | [MDN HTTP Guide](https://developer.mozilla.org/en-US/docs/Web/HTTP) | HTTP concepts and reference |
| TLS | [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) | TLS 1.3 specification |
| Subnetting | [Practical Networking](https://www.practicalnetworking.net/) | Networking and subnetting explanations |
| Wireshark | [Wireshark User Guide](https://www.wireshark.org/docs/wsug_html_chunked/) | Packet capture and analysis |
| Networking | [Cisco Networking Academy](https://www.netacad.com/) | Networking education and training |

---

# 4. SQL and Database Security

Resources covering database fundamentals, query construction, database security and injection vulnerabilities.

| Topic | Resource | Description |
|---|---|---|
| SQL Fundamentals | [W3Schools SQL Tutorial](https://www.w3schools.com/sql/) | SQL basics and query structure |
| SQL Reference | [Microsoft SQL Documentation](https://learn.microsoft.com/en-us/sql/) | SQL Server documentation |
| PostgreSQL | [Official Documentation](https://www.postgresql.org/docs/) | PostgreSQL administration and SQL reference |
| SQL Injection | [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection) | Understanding SQL injection vulnerabilities |
| Injection Prevention | [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) | Secure database query practices |
| Database Security | [OWASP Database Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html) | Database security considerations |

---

# 5. Cryptography

Resources for understanding encryption, hashing, authentication, digital certificates and cryptographic standards.

| Topic | Resource | Description |
|---|---|---|
| Cryptography Fundamentals | [CryptoHack](https://cryptohack.org/) | Interactive cryptography education |
| Cryptography Challenges | [Cryptopals](https://cryptopals.com/) | Practical cryptographic challenges |
| Cryptographic Standards | [NIST Cryptography](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines) | Cryptographic standards and guidance |
| Hashing | [NIST Hash Functions](https://csrc.nist.gov/projects/hash-functions) | Secure hash algorithm information |
| Password Storage | [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) | Secure password hashing and storage |
| TLS | [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/) | Recommended TLS configuration guidance |
| Public Key Infrastructure | [Microsoft PKI Documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-cs/) | Active Directory Certificate Services |

---

# 6. Cloud Security

Resources covering cloud infrastructure, identity management, access control, monitoring and security configuration.

| Platform / Topic | Resource | Description |
|---|---|---|
| AWS | [AWS Security Documentation](https://docs.aws.amazon.com/security/) | AWS security services and best practices |
| AWS Training | [AWS Skill Builder](https://skillbuilder.aws/) | AWS learning and training |
| Azure | [Microsoft Cloud Security](https://learn.microsoft.com/en-us/azure/security/) | Azure security documentation |
| Microsoft Entra | [Microsoft Entra Documentation](https://learn.microsoft.com/en-us/entra/) | Identity and access management |
| Google Cloud | [Google Cloud Security](https://cloud.google.com/security) | Google Cloud security resources |
| Cloud Security | [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) | Secure configuration recommendations |
| AWS Practice | [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) | Vulnerable-by-design AWS training environment |
| AWS Practice | [flAWS](http://flaws.cloud/) | AWS security learning challenges |

---

# 7. Web Application Security

Resources covering secure development, common vulnerabilities, application architecture and web security testing.

| Topic | Resource | Description |
|---|---|---|
| OWASP Top 10 | [OWASP](https://owasp.org/www-project-top-ten/) | Common web application security risks |
| Web Security Testing | [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) | Web application security testing methodology |
| Secure Development | [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification requirements |
| API Security | [OWASP API Security Top 10](https://owasp.org/www-project-api-security/) | Common API security risks |
| Security Cheat Sheets | [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) | Practical application security guidance |
| Web Security Training | [PortSwigger Academy](https://portswigger.net/web-security) | Free web application security training |
| Secure Coding | [Microsoft Security Development Lifecycle](https://www.microsoft.com/en-us/securityengineering/sdl) | Secure software development practices |

---

# 8. Active Directory and Windows Security

Resources covering Windows administration, identity infrastructure, domain security and endpoint hardening.

| Topic | Resource | Description |
|---|---|---|
| Windows Administration | [Microsoft Learn](https://learn.microsoft.com/en-us/windows-server/) | Windows Server documentation |
| Active Directory | [Microsoft AD DS Documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/) | Active Directory Domain Services |
| Group Policy | [Microsoft Group Policy](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview) | Group Policy management |
| Kerberos | [MIT Kerberos Documentation](https://web.mit.edu/kerberos/krb5-latest/doc/) | Kerberos authentication |
| Windows Hardening | [Microsoft Security Compliance Toolkit](https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/security-compliance-toolkit-10) | Windows security baselines |
| Linux Security | [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) | Secure operating system configuration |

---

# 9. Threat Intelligence and Security Frameworks

Resources for understanding attacker behaviour, threat intelligence, defensive controls and industry standards.

| Resource | Description |
|---|---|
| [MITRE ATT&CK](https://attack.mitre.org/) | Knowledge base of adversary tactics and techniques |
| [MITRE D3FEND](https://d3fend.mitre.org/) | Knowledge base of defensive cybersecurity techniques |
| [MITRE CAPEC](https://capec.mitre.org/) | Common attack pattern enumeration |
| [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) | Cybersecurity risk management framework |
| [NIST CSF 2.0](https://www.nist.gov/cyberframework) | Governance, identification, protection, detection, response and recovery |
| [CIS Critical Security Controls](https://www.cisecurity.org/controls) | Prioritised cybersecurity safeguards |
| [OWASP](https://owasp.org/) | Application security projects and resources |
| [CVE Program](https://www.cve.org/) | Publicly disclosed vulnerability identifiers |
| [NVD](https://nvd.nist.gov/) | National Vulnerability Database |
| [CISA](https://www.cisa.gov/) | Cybersecurity guidance, alerts and advisories |
| [Australian Cyber Security Centre](https://www.cyber.gov.au/) | Australian cybersecurity guidance and advisories |
| [Essential Eight](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight) | Australian cybersecurity mitigation strategies |

---

# 10. Learning Platforms and Practical Labs

Hands-on environments for developing cybersecurity skills through guided exercises, practical challenges and simulated investigations.

## General Cybersecurity

| Platform | Description | Link |
|---|---|---|
| TryHackMe | Guided cybersecurity learning paths and practical labs | [Visit](https://tryhackme.com/) |
| Hack The Box | Practical penetration testing machines and challenges | [Visit](https://www.hackthebox.com/) |
| Hack The Box Academy | Structured technical cybersecurity training | [Visit](https://academy.hackthebox.com/) |
| OverTheWire | Wargames covering Linux, networking and security concepts | [Visit](https://overthewire.org/wargames/) |
| PicoCTF | Beginner-friendly capture-the-flag challenges | [Visit](https://picoctf.org/) |

## Red Team and Web Security

| Platform | Description | Link |
|---|---|---|
| PortSwigger Web Security Academy | Free practical web application security training | [Visit](https://portswigger.net/web-security) |
| PentesterLab | Practical web security exercises | [Visit](https://pentesterlab.com/) |
| VulnHub | Downloadable vulnerable virtual machines | [Visit](https://www.vulnhub.com/) |
| Root-Me | Practical challenges across multiple security disciplines | [Visit](https://www.root-me.org/) |
| OWASP Juice Shop | Deliberately vulnerable web application for training | [GitHub](https://github.com/juice-shop/juice-shop) |

## Blue Team and Digital Forensics

| Platform | Description | Link |
|---|---|---|
| CyberDefenders | Practical Blue Team and DFIR challenges | [Visit](https://cyberdefenders.org/) |
| Blue Team Labs Online | Defensive investigation and incident response challenges | [Visit](https://blueteamlabs.online/) |
| LetsDefend | Simulated SOC environment and alert investigations | [Visit](https://letsdefend.io/) |
| Splunk Boss of the SOC | Practical Splunk-based security investigation challenges | [Visit](https://bots.splunk.com/) |

## Cloud Security

| Platform | Description | Link |
|---|---|---|
| CloudGoat | Vulnerable-by-design AWS security training | [GitHub](https://github.com/RhinoSecurityLabs/cloudgoat) |
| flAWS | Practical AWS security challenges | [Visit](http://flaws.cloud/) |
| Pwned Labs | Practical cloud security training | [Visit](https://pwnedlabs.io/) |

---

# 11. Security News and Research

Useful sources for staying informed about vulnerabilities, incidents, emerging threats and security research.

| Resource | Description |
|---|---|
| [The DFIR Report](https://thedfirreport.com/) | Detailed investigations of real-world cyber incidents |
| [Krebs on Security](https://krebsonsecurity.com/) | Cybercrime and security investigative journalism |
| [BleepingComputer](https://www.bleepingcomputer.com/) | Cybersecurity news and incident reporting |
| [The Hacker News](https://thehackernews.com/) | Cybersecurity news and vulnerability reporting |
| [CISA Advisories](https://www.cisa.gov/news-events/cybersecurity-advisories) | Official vulnerability and threat advisories |
| [Australian Cyber Security Centre](https://www.cyber.gov.au/) | Australian threat information and security guidance |
| [Google Threat Intelligence](https://cloud.google.com/security/products/threat-intelligence) | Threat intelligence and research |
| [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/) | Security research and Microsoft threat reporting |
| [SANS Internet Storm Center](https://isc.sans.edu/) | Internet threat activity and security analysis |

---

# 12. General Reference Libraries

Useful collections of documentation, technical references and practical security knowledge.

| Resource | Description |
|---|---|
| [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) | Concise application security guidance |
| [HackTricks](https://book.hacktricks.wiki/) | Technical security research and reference material |
| [CyberChef](https://gchq.github.io/CyberChef/) | Data encoding, decoding, transformation and analysis |
| [GTFOBins](https://gtfobins.org/) | Unix binary security reference |
| [LOLBAS](https://lolbas-project.github.io/) | Windows living-off-the-land binary reference |
| [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | Security testing payload and technique reference |
| [SecLists](https://github.com/danielmiessler/SecLists) | Security assessment wordlists |
| [Microsoft Learn](https://learn.microsoft.com/) | Official Microsoft technical documentation |
| [RFC Editor](https://www.rfc-editor.org/) | Internet protocol specifications |

---

## Disclaimer

External resources are provided for educational and professional development purposes.

Some tools and training environments contain offensive security capabilities. Always obtain appropriate authorisation before testing systems, networks or applications.

Third-party websites, tools and training platforms are independently maintained. Their availability, content, pricing and documentation may change over time.

The inclusion of a resource does not constitute an endorsement by the Cybersecurity Field Manual project.
