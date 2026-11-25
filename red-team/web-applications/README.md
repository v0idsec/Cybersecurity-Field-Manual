# Web Application Security

A practical field guide to web application security assessments, penetration testing and vulnerability research.

This section contains testing methodologies, reconnaissance techniques, vulnerability references, tools, payload resources and practical checklists for assessing web applications and APIs.

> **Scope reminder:** Only test applications and infrastructure where you have explicit authorisation. Follow the engagement's rules of engagement, testing restrictions and reporting requirements.

---

## Contents

- [Assessment Methodology](#assessment-methodology)
- [Reconnaissance and Attack Surface Mapping](#reconnaissance-and-attack-surface-mapping)
- [Core Testing Areas](#core-testing-areas)
- [API Security](#api-security)
- [Tools](#tools)
- [Payloads and Reference Material](#payloads-and-reference-material)
- [Testing Checklist](#testing-checklist)
- [Further Reading](#further-reading)

---

## Assessment Methodology

A structured testing process helps ensure consistent coverage and reliable findings.

| Phase | Focus |
|---|---|
| 1. Scoping | Confirm authorised domains, applications, accounts and restrictions |
| 2. Reconnaissance | Identify technologies, endpoints, subdomains and entry points |
| 3. Mapping | Understand application functionality, roles and data flows |
| 4. Testing | Assess vulnerabilities across the application's attack surface |
| 5. Validation | Safely reproduce and verify potential findings |
| 6. Documentation | Record evidence, impact, affected assets and remediation |
| 7. Reporting | Communicate findings and practical recommendations |

### Methodology references

- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- [Penetration Testing Execution Standard](http://www.pentest-standard.org/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

---

## Reconnaissance and Attack Surface Mapping

Identify the application's exposed functionality and understand how its components interact.

Topics:
- Domain and subdomain discovery
- DNS enumeration
- Technology fingerprinting
- HTTP response analysis
- Endpoint and directory discovery
- JavaScript analysis
- API endpoint discovery
- Parameter discovery
- Robots.txt and sitemap analysis
- Third-party integrations
- Exposed files and configuration
- Authentication and registration entry points

**Related resources:**
- [OWASP WSTG – Information Gathering](https://owasp.org/www-project-web-security-testing-guide/)
- [ProjectDiscovery](https://projectdiscovery.io/)
- [SecLists](https://github.com/danielmiessler/SecLists)

---

## Core Testing Areas

| Area | What to assess |
|---|---|
| [Authentication](authentication.md) | Login mechanisms, password resets, MFA and authentication logic |
| [Access Control](access-control.md) | IDOR, privilege escalation and authorisation weaknesses |
| [SQL Injection](sql-injection.md) | Unsafe database queries and injection vulnerabilities |
| [Cross-Site Scripting](xss.md) | Reflected, stored and DOM-based XSS |
| [Server-Side Request Forgery](ssrf.md) | Server-side requests and access to unintended resources |
| [File Uploads](file-upload.md) | Upload validation, file handling and unsafe processing |
| [JWT Security](jwt-security.md) | Token validation, signing and implementation weaknesses |

Additional testing areas:
- Cross-Site Request Forgery (CSRF)
- XML External Entity (XXE)
- Server-Side Template Injection (SSTI)
- Local and Remote File Inclusion
- Path Traversal
- Open Redirects
- Command Injection
- Insecure Deserialisation
- Business Logic Vulnerabilities
- Race Conditions
- Security Misconfiguration
- Information Disclosure
- Cache Poisoning and Cache Deception
- CORS Misconfiguration
- Clickjacking

---

## API Security

APIs frequently expose functionality and data that may not be visible through the application's normal interface.

Testing areas:
- REST API security
- GraphQL security
- Broken Object Level Authorisation (BOLA)
- Broken Function Level Authorisation (BFLA)
- Mass Assignment
- Excessive Data Exposure
- Rate Limiting
- Authentication and Token Handling
- API Versioning
- Input Validation
- GraphQL Introspection
- Improper Error Handling

**Dedicated guide:** [API Security](api-security.md)

**Reference:**
- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)

---

## Tools

### Intercepting proxies
- [Burp Suite](https://portswigger.net/burp)
- [OWASP ZAP](https://www.zaproxy.org/)

### Reconnaissance and discovery
- [Nmap](https://nmap.org/)
- [httpx](https://github.com/projectdiscovery/httpx)
- [Subfinder](https://github.com/projectdiscovery/subfinder)
- [Amass](https://github.com/owasp-amass/amass)
- [Katana](https://github.com/projectdiscovery/katana)
- [ffuf](https://github.com/ffuf/ffuf)
- [Gobuster](https://github.com/OJ/gobuster)

### Vulnerability discovery
- [Nuclei](https://github.com/projectdiscovery/nuclei)
- [Dalfox](https://github.com/hahwul/dalfox)
- [SQLmap](https://sqlmap.org/)
- [Nikto](https://github.com/sullo/nikto)

### Supporting tools
- [CyberChef](https://gchq.github.io/CyberChef/)
- [JWT.io](https://jwt.io/)
- [Retire.js](https://retirejs.github.io/retire.js/)

---

## Payloads and Reference Material

Useful repositories and references for understanding and validating common web vulnerabilities.

- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
- [SecLists](https://github.com/danielmiessler/SecLists)
- [HackTricks](https://book.hacktricks.wiki/)
- [The Hacker Recipes](https://www.thehacker.recipes/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [HackTricks Cloud](https://cloud.hacktricks.wiki/)

---

## Testing Checklist

Use this as a high-level coverage checklist during an authorised assessment.

- [ ] Confirm scope and testing restrictions
- [ ] Identify application technologies
- [ ] Map application functionality
- [ ] Identify authentication mechanisms
- [ ] Identify user roles and privilege levels
- [ ] Review session management
- [ ] Test access control boundaries
- [ ] Assess input handling and injection risks
- [ ] Review file upload functionality
- [ ] Assess API endpoints
- [ ] Review security headers and configuration
- [ ] Check for sensitive information exposure
- [ ] Validate potential vulnerabilities safely
- [ ] Capture supporting evidence
- [ ] Document remediation recommendations

---

## Further Reading

- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [OWASP Foundation](https://owasp.org/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [CWE – Common Weakness Enumeration](https://cwe.mitre.org/)
- [NVD – National Vulnerability Database](https://nvd.nist.gov/)
