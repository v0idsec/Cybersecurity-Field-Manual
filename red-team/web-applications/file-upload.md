# File Upload Security

## Overview

File upload functionality is a common attack surface in web applications.

Applications that accept user-supplied files must validate, process, store and serve those files safely. Weak controls can allow attackers to upload unexpected content, expose sensitive files, exhaust storage, or exploit vulnerable file-processing components.

This guide covers file upload assessment, common weaknesses, safe testing techniques and remediation.

> **Authorisation:** Only test applications and upload functionality explicitly included in your engagement scope. Use harmless test files and avoid uploading executable content to production systems unless explicitly authorised.

---

## Table of Contents

1. [How File Upload Vulnerabilities Work](#1-how-file-upload-vulnerabilities-work)
2. [Common Attack Surfaces](#2-common-attack-surfaces)
3. [File Validation Controls](#3-file-validation-controls)
4. [Reconnaissance and Discovery](#4-reconnaissance-and-discovery)
5. [Testing Methodology](#5-testing-methodology)
6. [Common Vulnerability Classes](#6-common-vulnerability-classes)
7. [File Processing Risks](#7-file-processing-risks)
8. [Tools](#8-tools)
9. [Remediation](#9-remediation)
10. [Reporting](#10-reporting)
11. [Testing Checklist](#11-testing-checklist)
12. [References](#12-references)

---

## 1. How File Upload Vulnerabilities Work

A typical upload process involves:

1. A user selects a file.
2. The browser sends the file to an application endpoint.
3. The server validates the file.
4. The application stores or processes the file.
5. The application makes the file available for later use.

Security weaknesses can occur at any stage.

For example, an application may rely on the filename extension supplied by the browser rather than independently validating the actual file content.

### Potential impact

- Unauthorised file access.
- Stored cross-site scripting.
- Exposure of sensitive information.
- Denial of service through resource exhaustion.
- Exploitation of vulnerable file-processing libraries.
- Unintended execution of uploaded content where unsafe server configuration permits it.

The impact depends on the application's storage architecture, processing pipeline and serving configuration.

---

## 2. Common Attack Surfaces

Look for upload functionality in:

| Feature | Potential risk |
|---|---|
| Profile pictures | Image validation and processing |
| Document uploads | Unsafe document processing |
| Attachments | Access control and file exposure |
| Support tickets | File storage and retrieval |
| Import functionality | Parsing and conversion vulnerabilities |
| Resume uploads | Document processing |
| Media galleries | Content validation and serving |
| Avatar or banner uploads | Image processing and metadata |
| Bulk imports | Archive handling and resource exhaustion |
| Cloud storage integrations | Access permissions and object exposure |

### Common upload parameters

Look for fields such as:

```text
file
upload
attachment
document
image
avatar
filename
content
media
```

Also inspect multipart form requests and JSON-based upload APIs.

---

## 3. File Validation Controls

Understanding how an application validates files is essential.

### 3.1 File extension

The extension is the suffix of a filename.

Examples:

```text
photo.jpg
report.pdf
document.docx
archive.zip
```

Applications should not trust the extension alone.

### 3.2 MIME type

The browser may include a content type in the upload request.

Example:

```text
Content-Type: image/jpeg
```

This value is supplied by the client and can be manipulated. It should not be treated as proof of the file's actual format.

### 3.3 File signatures

Many formats contain recognisable signatures, sometimes called magic bytes.

These can help identify a file's actual format.

However, signature checks alone are not sufficient. Some formats allow additional content, and complex files may contain structures that require deeper validation.

### 3.4 File size

Applications should enforce:

- Maximum upload size.
- Maximum decompressed size.
- Maximum image dimensions.
- Maximum archive entry count.
- Processing time limits.

### 3.5 Filename handling

User-controlled filenames can create problems if they are used directly in filesystem paths or object storage keys.

Applications should generate their own storage names and safely handle filenames when displaying them to users.

---

## 4. Reconnaissance and Discovery

### 4.1 Identify upload endpoints

Use the application normally and inspect requests with Burp Suite Proxy or browser developer tools.

Look for:

- `multipart/form-data` requests.
- File input fields.
- Upload API endpoints.
- File import functionality.
- Attachment creation endpoints.
- File download and preview endpoints.

### 4.2 Review the upload workflow

Document:

- Whether authentication is required.
- Whether users can upload multiple files.
- Which formats are accepted.
- Whether files are processed immediately.
- Whether uploaded files receive public URLs.
- Whether files can be accessed by other users.
- Whether deletion is supported.

### 4.3 Review the response

Record:

- HTTP status.
- Returned filename.
- Storage identifier.
- File URL.
- Error messages.
- Processing status.

A successful upload response does not necessarily mean the file is publicly accessible or executable.

### 4.4 Build an endpoint inventory

| Endpoint | Method | Accepted format | Authentication | Notes |
|---|---|---|---|---|
| `/api/profile/avatar` | POST | Images | Required | Profile picture |
| `/api/tickets/attachment` | POST | Documents | Required | Support attachment |
| `/api/import` | POST | CSV | Required | Bulk import |

Replace these examples with actual engagement findings.

---

## 5. Testing Methodology

### 5.1 Establish a baseline

Start with a normal file that the application explicitly supports.

Record:

- Filename.
- File format.
- File size.
- Browser-supplied MIME type.
- HTTP request and response.
- Resulting file URL or identifier.

This provides a baseline for later comparisons.

### 5.2 Test allowed and disallowed formats

Use harmless files to determine whether the application enforces its documented format restrictions.

Check:

- Expected file types.
- Unsupported extensions.
- Incorrect MIME types.
- Mismatched file signatures.
- Empty files.
- Unusual filenames.

Do not use executable payloads or destructive files in production.

### 5.3 Review filename handling

Check whether the application:

- Preserves the original filename.
- Generates a unique storage name.
- Handles long filenames.
- Handles spaces and Unicode.
- Prevents path traversal.
- Prevents collisions between uploads.

Use harmless filenames containing unusual characters to assess normalisation.

### 5.4 Test size restrictions

Gradually assess documented upload limits using benign files.

Observe whether:

- Oversized files are rejected.
- The server enforces limits independently of the browser.
- Error messages are appropriate.
- Partial uploads are cleaned up.
- Resource consumption remains controlled.

Avoid deliberately exhausting application resources.

### 5.5 Test access control

Determine whether uploaded files are accessible only to the intended users.

With authorised test accounts:

1. Upload a harmless file using account A.
2. Record its identifier or URL.
3. Attempt to access it using account B.
4. Check whether access is correctly restricted.
5. Verify that deleted files are no longer accessible.

This is particularly important for support attachments, medical documents and other sensitive uploads.

### 5.6 Test retrieval and content handling

Review how uploaded files are served back to users.

Check:

- Response `Content-Type`.
- `Content-Disposition`.
- Cache headers.
- Authentication requirements.
- Whether content is served from a separate origin.
- Whether the browser renders the file inline.

Unexpectedly rendering uploaded content in the application's trusted origin may create security risks.

---

## 6. Common Vulnerability Classes

### 6.1 Extension validation bypass

A weak implementation may trust only the filename extension.

**Assessment focus:**

- Whether extensions are allowlisted.
- Whether validation occurs server-side.
- Whether filenames are normalised before checking.
- Whether the actual file format is independently validated.

### 6.2 MIME type validation bypass

Applications may trust the client-supplied `Content-Type` header.

**Assessment focus:**

- Whether MIME types are checked server-side.
- Whether the content matches the expected format.
- Whether unsupported content is rejected.
- Whether multiple validation layers are used.

### 6.3 Stored cross-site scripting

An uploaded file may contain content that executes when rendered by a browser.

This can occur when applications serve user-controlled content using an unsafe content type or within the application's trusted origin.

**Assessment focus:**

- How HTML-like content is served.
- Whether uploaded files are rendered inline.
- Whether the file is isolated from the application origin.
- Whether browser content sniffing is controlled.

Use harmless proof-of-concept content in an authorised test environment.

### 6.4 Path traversal

Applications may mishandle user-controlled filenames or file paths.

This can result in files being stored or retrieved outside their intended directory.

**Assessment focus:**

- Whether storage paths are generated server-side.
- Whether path components are normalised.
- Whether user input can influence filesystem locations.
- Whether download endpoints enforce object-level access control.

### 6.5 Insecure direct object references

An application may expose uploaded files through predictable identifiers.

**Assessment focus:**

- Whether file identifiers are guessable.
- Whether authorisation is checked on every retrieval.
- Whether access is restricted by tenant and ownership.
- Whether deleted or expired files remain accessible.

### 6.6 Unrestricted file upload

An application may accept file types beyond those required for its intended purpose.

This can increase the risk of unsafe rendering, processing or storage.

**Assessment focus:**

- Whether accepted formats are narrowly defined.
- Whether validation is enforced on the backend.
- Whether files are stored outside executable locations.
- Whether uploaded content is isolated from the application.

---

## 7. File Processing Risks

File uploads are not limited to the upload endpoint itself. Processing libraries and background services introduce additional risks.

### 7.1 Image processing

Image libraries can contain vulnerabilities or be exposed to malformed input.

Review:

- Image processing library versions.
- Supported formats.
- Maximum dimensions.
- Processing timeouts.
- Memory limits.
- Whether original files are retained.

### 7.2 Document processing

PDF, office document and other conversion tools can introduce risks when processing untrusted files.

Review:

- Parser and converter versions.
- Macro handling.
- External resource loading.
- Sandboxing.
- Processing permissions.
- Temporary file cleanup.

### 7.3 Archive extraction

Archive processing can introduce path traversal and resource exhaustion risks.

Review:

- Extraction destination restrictions.
- Maximum decompressed size.
- Maximum number of entries.
- Nested archive handling.
- Symbolic link handling.
- File overwrite behaviour.

Use benign test archives and controlled lab environments when assessing extraction behaviour.

### 7.4 Metadata

Images and documents may contain metadata such as:

- GPS coordinates.
- Author names.
- Device information.
- Software versions.
- Creation timestamps.

Check whether sensitive metadata is unintentionally exposed when files are shared or published.

---

## 8. Tools

| Tool | Purpose |
|---|---|
| Burp Suite | Inspect and modify upload requests |
| OWASP ZAP | Web application testing |
| curl | Submit and inspect HTTP requests |
| ExifTool | Inspect file metadata |
| file | Identify file formats |
| TrID | Identify file types |
| CyberChef | Inspect and transform file data |
| ImageMagick | Inspect image properties in a lab |
| Wireshark | Analyse network traffic |
| Python | Create benign test files and automate checks |

### Useful Linux commands

Identify a file:

```bash
file sample.jpg
```

Inspect file metadata:

```bash
exiftool sample.jpg
```

Display file size:

```bash
stat sample.jpg
```

Calculate a SHA-256 hash:

```bash
sha256sum sample.jpg
```

Inspect MIME information:

```bash
file --mime-type sample.jpg
```

These commands help document test artefacts and compare the uploaded file with the original.

---

## 9. Remediation

### 9.1 Use strict allowlists

Define exactly which formats the application needs to accept.

Reject everything else by default.

### 9.2 Validate files server-side

Do not rely on browser validation or client-supplied MIME types.

Use multiple validation layers:

- Extension allowlist.
- MIME type inspection.
- File signature checks.
- Format-specific parsing.
- Size and dimension limits.

### 9.3 Generate server-side filenames

Do not use user-supplied filenames directly as storage paths.

Generate unique storage identifiers and safely retain the original filename only when necessary.

### 9.4 Store files outside the web root

Uploaded files should not be stored in locations where the web server can execute them.

Where practical, use dedicated object storage or a separate file-serving service.

### 9.5 Enforce access control

Every file retrieval operation should verify:

- User identity.
- File ownership.
- Tenant boundaries.
- Required permissions.
- File availability and expiry.

Do not rely on unguessable file identifiers as an authorisation mechanism.

### 9.6 Isolate uploaded content

Consider:

- Separate storage domains.
- Separate origins for user-controlled content.
- Appropriate `Content-Type` headers.
- `Content-Disposition: attachment` where appropriate.
- `X-Content-Type-Options: nosniff`.
- Strict content security policies.

### 9.7 Secure file processing

- Keep parsing libraries updated.
- Run processing in isolated environments.
- Apply CPU, memory and time limits.
- Disable unnecessary external resource loading.
- Scan files where appropriate.
- Clean up temporary files.
- Limit archive extraction resources.

### 9.8 Monitor uploads

Log relevant events, including:

- User identity.
- File identifier.
- File size.
- Detected format.
- Validation failures.
- Processing failures.
- Access attempts.

Avoid logging sensitive file contents or unnecessary personal information.

---

## 10. Reporting

### Suggested report structure

**Title:** Insecure File Upload in [Feature / Endpoint]

**Summary:**

Describe the affected upload functionality and the validation, storage, processing or access-control weakness.

**Affected endpoint:**

```text
POST /api/example/upload
```

**Steps to reproduce:**

1. Authenticate using an authorised test account.
2. Navigate to the affected upload functionality.
3. Upload a harmless test file.
4. Observe the application's validation and response.
5. Verify the demonstrated security impact using an approved test account or controlled environment.

**Evidence:**

- Sanitised HTTP request.
- Sanitised HTTP response.
- Test file details.
- File retrieval behaviour.
- Relevant screenshots.
- Access-control results, if applicable.

**Impact:**

Explain what an attacker could realistically achieve. Distinguish confirmed behaviour from theoretical consequences.

**Remediation:**

Recommend strict server-side validation, safe storage, access control, content isolation and secure processing.

---

## 11. Testing Checklist

### Discovery

- [ ] Identify upload functionality.
- [ ] Identify upload API endpoints.
- [ ] Record accepted file formats.
- [ ] Review upload authentication requirements.
- [ ] Identify file retrieval endpoints.
- [ ] Identify background processing components.

### Validation

- [ ] Test expected file formats.
- [ ] Test unsupported formats using harmless files.
- [ ] Review MIME type handling.
- [ ] Review file signature validation.
- [ ] Check filename normalisation.
- [ ] Check file size restrictions.
- [ ] Review image and document processing.
- [ ] Review archive handling.

### Access control

- [ ] Check file ownership.
- [ ] Check cross-account access.
- [ ] Check tenant isolation.
- [ ] Check deleted file access.
- [ ] Review public file URLs.
- [ ] Check access to sensitive attachments.

### Reporting

- [ ] Capture sanitised requests and responses.
- [ ] Record file details and hashes.
- [ ] Demonstrate impact safely.
- [ ] Avoid unnecessary sensitive data access.
- [ ] Provide practical remediation guidance.

---

## 12. References

- [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [PortSwigger — File Upload Vulnerabilities](https://portswigger.net/web-security/file-upload)
- [MITRE CWE-434 — Unrestricted Upload of File with Dangerous Type](https://cwe.mitre.org/data/definitions/434.html)
- [ExifTool](https://exiftool.org/)
- [CyberChef](https://gchq.github.io/CyberChef/)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
