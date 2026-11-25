# Web Application Reconnaissance

A practical guide to discovering, mapping and understanding web application attack surfaces during authorised security assessments.

The objective of reconnaissance is to understand what exists, how it is exposed, what technologies are in use and where further testing may be valuable.

> **Important:** Passive reconnaissance and active scanning are different activities. Confirm the engagement scope and permitted testing methods before interacting with target infrastructure.

---

## Contents

- [1. Reconnaissance Workflow](#1-reconnaissance-workflow)
- [2. Scope and Target Identification](#2-scope-and-target-identification)
- [3. DNS and Subdomain Discovery](#3-dns-and-subdomain-discovery)
- [4. Technology Fingerprinting](#4-technology-fingerprinting)
- [5. HTTP and HTTPS Analysis](#5-http-and-https-analysis)
- [6. Directory and Endpoint Discovery](#6-directory-and-endpoint-discovery)
- [7. JavaScript Analysis](#7-javascript-analysis)
- [8. Parameter Discovery](#8-parameter-discovery)
- [9. API Discovery](#9-api-discovery)
- [10. Useful Tools](#10-useful-tools)
- [11. Reconnaissance Checklist](#11-reconnaissance-checklist)
- [12. Further Reading](#12-further-reading)

---

## 1. Reconnaissance Workflow

A repeatable workflow helps avoid overlooking important parts of an application.

| Stage | Objective |
|---|---|
| Scope | Identify authorised domains, IPs and applications |
| Passive discovery | Gather publicly available information |
| DNS enumeration | Identify domains and subdomains |
| Live host identification | Determine which discovered hosts respond |
| Fingerprinting | Identify web servers, frameworks and technologies |
| Content discovery | Identify directories, files and endpoints |
| Application mapping | Understand functionality and user workflows |
| Documentation | Record findings and potential testing opportunities |

### Recommended approach

1. Establish the authorised target list.
2. Collect known domains and subdomains.
3. Identify live web services.
4. Fingerprint technologies and infrastructure.
5. Browse the application and map functionality.
6. Discover additional endpoints and parameters.
7. Identify authentication boundaries and user roles.
8. Record potential attack surfaces for further testing.

---

## 2. Scope and Target Identification

Before conducting reconnaissance, establish exactly what is authorised.

Record:

- Primary domain
- In-scope subdomains
- Excluded domains and infrastructure
- Permitted IP ranges
- Test accounts and user roles
- Permitted scanning intensity
- Restricted endpoints or functionality
- Third-party services and integrations
- Testing window and emergency contacts

### Target inventory template

| Target | Type | Scope status | Notes |
|---|---|---|---|
| example.com | Primary domain | Confirmed | Main application |
| api.example.com | API | Confirmed | API endpoint |
| dev.example.com | Subdomain | Verify | Check scope before testing |

Never assume that a discovered subdomain, third-party service or associated IP address is automatically in scope.

---

## 3. DNS and Subdomain Discovery

Subdomain discovery can reveal additional applications, development environments, administrative portals and forgotten infrastructure.

### Passive discovery

Useful sources:

- Certificate Transparency logs
- DNS records
- Public search engines
- Historical DNS datasets
- Public code repositories
- Internet-wide asset search engines

### Useful resources

- [crt.sh](https://crt.sh/)
- [Google Certificate Transparency](https://transparencyreport.google.com/https/certificates)
- [SecurityTrails](https://securitytrails.com/)
- [VirusTotal](https://www.virustotal.com/)
- [Shodan](https://www.shodan.io/)
- [Censys](https://search.censys.io/)

### Useful tools

**Subfinder**

Passive subdomain discovery.

```bash
subfinder -d example.com -o subdomains.txt
```

**Amass**

Attack surface mapping and subdomain enumeration.

```bash
amass enum -passive -d example.com
```

**Findomain**

```bash
findomain -t example.com
```

**Important:** These commands use a placeholder domain. Replace it only with an authorised target.

### DNS record inspection

```bash
dig example.com
dig example.com A
dig example.com AAAA
dig example.com MX
dig example.com NS
dig example.com TXT
```

Alternative:

```bash
nslookup example.com
```

---

## 4. Technology Fingerprinting

Identifying the technologies behind an application can help guide later testing.

Look for:

- Web server
- Programming language
- Application framework
- Content management system
- JavaScript frameworks
- CDN and reverse proxy
- Web application firewall
- Authentication provider
- Database indicators
- Third-party integrations

### Tools

| Tool | Purpose |
|---|---|
| Wappalyzer | Technology identification |
| WhatWeb | Web technology fingerprinting |
| httpx | HTTP probing and metadata |
| Nmap | Service and version discovery |
| BuiltWith | Website technology lookup |
| Netcraft | Website and hosting information |

### WhatWeb

```bash
whatweb https://example.com
```

### httpx

```bash
httpx -l subdomains.txt -title -tech-detect -status-code -o live-hosts.txt
```

### Nmap

For authorised targets:

```bash
nmap -sV -p 80,443 example.com
```

Technology fingerprinting is indicative, not definitive. Headers and other fingerprints can be misleading or deliberately modified.

---

## 5. HTTP and HTTPS Analysis

HTTP responses can reveal useful information about application behaviour, server configuration and security controls.

### Inspect response headers

```bash
curl -I https://example.com
```

View the complete request and response:

```bash
curl -v https://example.com
```

Follow redirects:

```bash
curl -IL https://example.com
```

### Important response headers

| Header | Purpose |
|---|---|
| Strict-Transport-Security | Enforces HTTPS |
| Content-Security-Policy | Restricts permitted content sources |
| X-Content-Type-Options | Helps prevent MIME-type confusion |
| X-Frame-Options | Controls framing behaviour |
| Referrer-Policy | Controls referrer information |
| Permissions-Policy | Controls browser feature access |
| Set-Cookie | Reveals cookie attributes |

### Cookie attributes to review

- Secure
- HttpOnly
- SameSite
- Domain
- Path
- Expiry and Max-Age

Missing security headers are not automatically vulnerabilities. Assess them in the context of the application's functionality and threat model.

---

## 6. Directory and Endpoint Discovery

Content discovery can identify functionality that is not immediately accessible through the application's navigation.

Examples:

- Administrative interfaces
- API routes
- Backup files
- Documentation
- Development endpoints
- Configuration files
- Old application versions
- Forgotten directories

### ffuf

Basic directory discovery:

```bash
ffuf -u https://example.com/FUZZ \
-w /path/to/wordlist.txt
```

Filter by response status:

```bash
ffuf -u https://example.com/FUZZ \
-w /path/to/wordlist.txt \
-mc 200,204,301,302,307,401,403
```

### Gobuster

```bash
gobuster dir \
-u https://example.com \
-w /path/to/wordlist.txt
```

### Useful wordlists

- [SecLists](https://github.com/danielmiessler/SecLists)
- [Assetnote Wordlists](https://wordlists.assetnote.io/)
- [FuzzDB](https://github.com/fuzzdb-project/fuzzdb)

**Operational note:** Directory brute-forcing can generate significant traffic. Use only where permitted, with appropriate rate limits and request volume.

---

## 7. JavaScript Analysis

JavaScript files can expose application routes, API references, client-side logic and information about how the frontend communicates with backend services.

Look for:

- API endpoint references
- Hidden application routes
- Authentication logic
- Feature flags
- Client-side validation
- Source maps
- Hardcoded configuration
- References to development environments
- Potentially exposed credentials or tokens

### Identify JavaScript files

```bash
curl -s https://example.com | grep -Eo 'src="[^"]+\.js[^"]*"'
```

### Download a JavaScript file

```bash
curl -O https://example.com/static/app.js
```

### Search for interesting strings

```bash
grep -Eio 'api|admin|internal|debug|token|secret|graphql' app.js
```

Treat any discovered credentials or tokens as sensitive. Do not use them to access systems or accounts without explicit authorisation.

### Useful tools

- [LinkFinder](https://github.com/GerbenJavado/LinkFinder)
- [SecretFinder](https://github.com/m4ll0k/SecretFinder)
- [JSluice](https://github.com/BishopFox/jsluice)
- [Retire.js](https://retirejs.github.io/retire.js/)

---

## 8. Parameter Discovery

Identifying parameters helps build an understanding of how the application processes user input.

Look for:

- Query string parameters
- Form fields
- JSON properties
- URL path parameters
- HTTP headers
- Cookies
- Hidden form fields
- API request bodies

### Example

```text
https://example.com/profile?id=123
```

Potential parameter:

```text
id=123
```

Questions to investigate during authorised testing:

- Does the parameter influence displayed data?
- Is it used in a database query?
- Does changing it affect object access?
- Is input validated server-side?
- Does the application behave differently for unexpected values?

### Useful tools

- [Arjun](https://github.com/s0md3v/Arjun)
- [ParamSpider](https://github.com/devanshbatham/ParamSpider)
- [Burp Suite](https://portswigger.net/burp)

---

## 9. API Discovery

Modern applications often rely heavily on APIs. Map the endpoints and understand their authentication and authorisation requirements.

Look for:

- REST endpoints
- GraphQL endpoints
- API documentation
- OpenAPI / Swagger specifications
- Versioned API routes
- Authentication tokens
- User and administrative endpoints
- Object identifiers
- Rate limiting

Common documentation paths to check manually:

```text
/swagger
/swagger-ui
/swagger.json
/openapi.json
/api-docs
/graphql
```

These are discovery examples, not guaranteed locations.

### Useful tools

- Burp Suite
- Postman
- Insomnia
- Kiterunner
- Arjun
- GraphQL Voyager

**Further reading:** [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)

---

## 10. Useful Tools

| Tool | Category | Repository |
|---|---|---|
| Subfinder | Subdomain discovery | [GitHub](https://github.com/projectdiscovery/subfinder) |
| Amass | Attack surface mapping | [GitHub](https://github.com/owasp-amass/amass) |
| httpx | HTTP probing | [GitHub](https://github.com/projectdiscovery/httpx) |
| Nmap | Network discovery | [Website](https://nmap.org/) |
| WhatWeb | Fingerprinting | [GitHub](https://github.com/urbanadventurer/WhatWeb) |
| ffuf | Content discovery | [GitHub](https://github.com/ffuf/ffuf) |
| Gobuster | Content discovery | [GitHub](https://github.com/OJ/gobuster) |
| Katana | Web crawling | [GitHub](https://github.com/projectdiscovery/katana) |
| Arjun | Parameter discovery | [GitHub](https://github.com/s0md3v/Arjun) |
| LinkFinder | JavaScript analysis | [GitHub](https://github.com/GerbenJavado/LinkFinder) |
| Burp Suite | Web testing | [Website](https://portswigger.net/burp) |

---

## 11. Reconnaissance Checklist

### Scope
- [ ] Confirm authorised domains and IP ranges
- [ ] Review exclusions and restrictions
- [ ] Confirm permitted scanning intensity

### Discovery
- [ ] Identify known domains and subdomains
- [ ] Review DNS records
- [ ] Identify live web services
- [ ] Identify third-party dependencies

### Fingerprinting
- [ ] Identify server technologies
- [ ] Identify application frameworks
- [ ] Review HTTP response headers
- [ ] Inspect TLS configuration

### Application mapping
- [ ] Map application functionality
- [ ] Identify login and registration workflows
- [ ] Identify user roles
- [ ] Discover API endpoints
- [ ] Inspect JavaScript files
- [ ] Identify input parameters

### Documentation
- [ ] Record discovered assets
- [ ] Record technologies and versions
- [ ] Document interesting endpoints
- [ ] Identify areas requiring further testing
- [ ] Preserve relevant evidence

---

## 12. Further Reading

- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [HackTricks – Web Pentesting](https://book.hacktricks.wiki/)
- [ProjectDiscovery Documentation](https://docs.projectdiscovery.io/)
- [The Hacker Recipes](https://www.thehacker.recipes/)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
