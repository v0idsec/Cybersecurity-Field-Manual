# SQL Injection (SQLi)

A practical guide to identifying, validating and understanding SQL injection vulnerabilities during authorised web application security assessments.

SQL injection occurs when an application incorporates untrusted input into a database query without safely separating data from executable SQL instructions.

Depending on the database, application permissions and vulnerable query, SQL injection can expose sensitive information, modify records or affect database availability.

> **Scope reminder:** Only test systems where you have explicit authorisation. Use designated test accounts and non-sensitive data. Avoid destructive queries, data extraction beyond the approved scope and testing against production records without permission.

---

## Contents

- [1. SQL Injection Fundamentals](#1-sql-injection-fundamentals)
- [2. How SQL Injection Works](#2-how-sql-injection-works)
- [3. Identifying Injection Points](#3-identifying-injection-points)
- [4. Error-Based SQL Injection](#4-error-based-sql-injection)
- [5. UNION-Based SQL Injection](#5-union-based-sql-injection)
- [6. Boolean-Based Blind SQL Injection](#6-boolean-based-blind-sql-injection)
- [7. Time-Based Blind SQL Injection](#7-time-based-blind-sql-injection)
- [8. Database Fingerprinting](#8-database-fingerprinting)
- [9. SQL Injection Testing with Burp Suite](#9-sql-injection-testing-with-burp-suite)
- [10. SQLmap](#10-sqlmap)
- [11. Second-Order SQL Injection](#11-second-order-sql-injection)
- [12. Common SQL Injection Locations](#12-common-sql-injection-locations)
- [13. Prevention and Remediation](#13-prevention-and-remediation)
- [14. Testing Checklist](#14-testing-checklist)
- [15. Further Reading](#15-further-reading)

---

## 1. SQL Injection Fundamentals

SQL injection is an injection vulnerability affecting applications that interact with relational databases.

Common database platforms include:

- Microsoft SQL Server
- MySQL
- PostgreSQL
- Oracle Database
- SQLite
- MariaDB

SQL injection may occur anywhere user-controlled data influences a database query without appropriate protection.

### Potential impact

Depending on the vulnerability and database permissions:

- Unauthorised access to application data
- Authentication bypass
- Exposure of sensitive records
- Unauthorised modification or deletion of data
- Access to database metadata
- In some configurations, interaction with the underlying operating system

Not every SQL injection vulnerability provides every capability. Impact depends on the application's database account privileges, query context and database configuration.

---

## 2. How SQL Injection Works

Consider an application that constructs a SQL query using string concatenation.

### Vulnerable example

```python
username = request.args.get("username")

query = "SELECT * FROM users WHERE username = '" + username + "'"
```

The application intends to execute:

```sql
SELECT * FROM users WHERE username = 'alice';
```

However, the application has mixed user-controlled input with executable SQL syntax.

### Safer implementation

```python
cursor.execute(
    "SELECT * FROM users WHERE username = ?",
    (username,)
)
```

The parameterised query separates the SQL statement from the supplied value.

The placeholder syntax varies by database driver and programming language.

### Key concept

The fundamental issue is not the presence of unusual characters. It is whether user input can alter the structure or meaning of a database query.

---

## 3. Identifying Injection Points

SQL injection testing begins by identifying inputs that may influence database operations.

### Common injection points

| Location | Example |
|---|---|
| URL parameters | `/products?id=10` |
| Search fields | Product or user search |
| Login forms | Username and password |
| HTTP headers | Certain application-controlled headers |
| Cookies | Session or preference values |
| JSON bodies | API request properties |
| POST parameters | Form submissions |
| Sort and filter options | Column names and ordering |
| GraphQL resolvers | Arguments used in database queries |

### Initial testing

Start with normal application behaviour.

1. Identify an input that retrieves or modifies database-backed information.
2. Record the original request and response.
3. Observe how ordinary values affect the response.
4. Introduce harmless syntax variations in a controlled test environment.
5. Compare response content, status codes and timing.
6. Investigate consistent differences.

### Example input variations

```text
10
' 
"
test'
test"
```

These values alone do not establish SQL injection. They are starting points for observing application behaviour.

### What to look for

- Database error messages
- Unexpected HTTP status codes
- Changes in returned records
- Different response lengths
- Consistent response timing differences
- Unexpected application exceptions

A reliable finding requires validation, not just an error message.

---

## 4. Error-Based SQL Injection

Error-based SQL injection involves database errors that reveal information about query processing.

### Common indicators

- SQL syntax errors
- Database driver exceptions
- Query execution errors
- Invalid column or table errors
- Type conversion errors
- Database-specific error messages

### Example

A vulnerable application may return a database syntax error after receiving malformed input.

```text
Database query failed:
Incorrect syntax near ...
```

This may reveal:

- Database platform
- Query construction behaviour
- Database driver
- Query execution context

### Testing approach

1. Identify a potentially database-backed input.
2. Capture the baseline response.
3. Introduce a harmless malformed value.
4. Compare the response with the baseline.
5. Determine whether the error originates from the database.
6. Verify whether the behaviour is reproducible.

### Important considerations

- An application error is not automatically SQL injection.
- Error messages can originate from application validation.
- Production applications should generally avoid returning detailed database errors to users.

---

## 5. UNION-Based SQL Injection

UNION-based SQL injection attempts to combine the results of an injected query with the results of the original query.

The SQL `UNION` operator combines compatible result sets.

### Example SQL

```sql
SELECT name, description FROM products
UNION
SELECT username, email FROM users;
```

The two queries must return compatible column counts and data types.

### Important concepts

- Column count
- Column data types
- Compatible result sets
- Query context
- Database permissions
- Application response handling

### Identifying UNION-based behaviour

During authorised testing, investigate whether user-controlled input can influence a query that returns data to the application.

A suspected UNION injection requires evidence that the input changes the query's result structure or content.

### Potential impact

- Unauthorised data exposure
- Disclosure of database information
- Exposure of records from other application tables

### Defensive considerations

- Use parameterised queries.
- Avoid dynamic SQL where possible.
- Validate identifiers used in dynamic query construction.
- Restrict database account permissions.

---

## 6. Boolean-Based Blind SQL Injection

Blind SQL injection occurs when an application does not directly display database errors or query results, but differences in application behaviour reveal information.

Boolean-based testing compares the application's response to logically different conditions.

### Concept

A database condition evaluates to either:

```text
TRUE
```

or:

```text
FALSE
```

If the application responds differently depending on the result, that difference may provide evidence of a query injection vulnerability.

### What to compare

- Response status
- Response body
- Response length
- Redirect behaviour
- Visible application content
- Consistent application behaviour

### Testing methodology

1. Capture a normal response.
2. Establish a controlled comparison condition.
3. Observe whether the application response changes.
4. Repeat the comparison to rule out unrelated application behaviour.
5. Validate the finding in an approved environment.

### Important considerations

Blind SQL injection can be difficult to distinguish from ordinary application logic.

A single different response is not sufficient evidence. Look for repeatable behaviour tied to the input.

---

## 7. Time-Based Blind SQL Injection

Time-based blind SQL injection uses a measurable database response delay to investigate whether input influences query execution.

Some database platforms provide functions that can deliberately delay query execution.

Examples include:

| Database | Delay mechanism |
|---|---|
| Microsoft SQL Server | `WAITFOR DELAY` |
| MySQL | `SLEEP()` |
| PostgreSQL | `pg_sleep()` |
| Oracle | `DBMS_SESSION.SLEEP` in supported contexts |

### Testing considerations

Time-based testing can generate additional database load and should only be performed where explicitly permitted.

Consider:

- Baseline response time
- Network latency
- Application load
- Database load
- Request timeouts
- Repeatability of observed delays

### Validation methodology

1. Measure normal response times.
2. Establish whether the application has variable response latency.
3. Perform only approved, low-impact validation.
4. Compare multiple observations.
5. Rule out unrelated network or application delays.

### Important distinction

A slow response does not establish time-based SQL injection. The delay must be reproducibly associated with the tested input and supported by other evidence.

---

## 8. Database Fingerprinting

Different database platforms implement different SQL syntax, functions and behaviours.

Fingerprinting helps identify the database technology involved in a suspected SQL injection.

### Common database platforms

| Database | Common indicators |
|---|---|
| Microsoft SQL Server | T-SQL syntax, SQL Server error messages |
| MySQL | MySQL-specific errors and functions |
| PostgreSQL | PostgreSQL error messages and syntax |
| Oracle | Oracle error codes and SQL syntax |
| SQLite | SQLite error messages and database behaviour |

### Useful information

- Database platform
- Database version, where exposed
- Database driver
- Application framework
- Database error handling
- Query behaviour

### Caution

Technology fingerprints can be misleading. Applications may use database abstraction layers, proxies or generic error handling.

Do not assume the database platform from a single response.

---

## 9. SQL Injection Testing with Burp Suite

Burp Suite is useful for inspecting and modifying HTTP requests during web application assessments.

### Basic workflow

1. Open Burp Suite.
2. Configure the browser to use Burp Proxy.
3. Browse the authorised application.
4. Identify a database-backed input.
5. Capture the relevant request.
6. Send it to Repeater.
7. Establish a baseline response.
8. Change one input at a time.
9. Compare responses.
10. Record reproducible evidence.

### Features worth knowing

| Feature | Purpose |
|---|---|
| Proxy | Intercept HTTP requests |
| Repeater | Manually modify and replay requests |
| Intruder | Perform controlled parameter testing |
| Comparer | Compare responses |
| Logger | Review HTTP traffic |
| Decoder | Encode and decode data |

### Testing notes

- Preserve the original request.
- Change one variable at a time.
- Use controlled test data.
- Avoid excessive request volume.
- Record relevant response differences.

Resource: [Burp Suite Documentation](https://portswigger.net/burp/documentation)

---

## 10. SQLmap

SQLmap is an automated tool for detecting and assessing SQL injection vulnerabilities.

It supports several database platforms and different SQL injection techniques.

Repository: [SQLmap on GitHub](https://github.com/sqlmapproject/sqlmap)

Documentation: [SQLmap Wiki](https://github.com/sqlmapproject/sqlmap/wiki)

### Basic request testing

For an explicitly authorised test application:

```bash
sqlmap -u "https://example.com/item?id=1" --batch
```

### Test a specific parameter

```bash
sqlmap -u "https://example.com/item?id=1" -p id
```

### Test a captured HTTP request

Save an authorised request to a file named `request.txt`.

```bash
sqlmap -r request.txt
```

### Specify a database management system

```bash
sqlmap -u "https://example.com/item?id=1" --dbms="Microsoft SQL Server"
```

### Useful options

| Option | Purpose |
|---|---|
| `-u` | Target URL |
| `-r` | Load a request from a file |
| `-p` | Specify parameters to test |
| `--data` | Supply POST data |
| `--cookie` | Supply cookies |
| `--headers` | Supply additional HTTP headers |
| `--dbms` | Specify a database platform |
| `--batch` | Use default answers to prompts |
| `--level` | Adjust test level |
| `--risk` | Adjust test risk |

### Operational safety

SQLmap can generate substantial traffic and may perform intrusive tests depending on its options.

For controlled assessments:

- Confirm automated testing is permitted.
- Use designated test accounts.
- Start with conservative settings.
- Avoid destructive options.
- Do not dump databases unless explicitly authorised.
- Do not use operating system interaction features without specific written approval.

### Manual verification

Automated detection should be followed by manual validation.

Confirm that:

- The suspected parameter is responsible.
- The behaviour is reproducible.
- The finding is genuinely SQL injection.
- The impact is accurately described.
- The evidence does not expose unrelated sensitive data.

---

## 11. Second-Order SQL Injection

Second-order SQL injection occurs when user-controlled input is stored and later incorporated into a database query in an unsafe way.

Unlike traditional injection, the vulnerable query may execute during a later application workflow.

### Example workflow

1. A user submits a value through a profile form.
2. The application stores that value.
3. A separate administrative function retrieves the stored value.
4. The value is incorporated into another SQL query unsafely.
5. The second query becomes vulnerable.

### Potential locations

- Profile information
- Saved searches
- Support tickets
- User-generated content
- Administrative reporting
- Stored application preferences
- Import and export workflows

### Testing considerations

- Trace how user input is stored.
- Identify where stored values are reused.
- Examine background processing and reporting functions.
- Review administrative workflows where permitted.
- Use harmless test values and controlled data.

Second-order vulnerabilities can be difficult to identify because the initial request may appear completely normal.

---

## 12. Common SQL Injection Locations

| Application feature | Potential concern |
|---|---|
| Login forms | Authentication query construction |
| Search functionality | Dynamic search queries |
| Product filters | Unsafe filtering logic |
| Sorting | Dynamic column or ordering expressions |
| User profiles | Database-backed profile lookups |
| Reports | Dynamic report queries |
| API endpoints | Unsafe JSON-to-query handling |
| Cookies | User-controlled values reused in queries |
| Administrative tools | Dynamic query construction |
| Import functions | Unsafe processing of stored input |

Not every database-backed input is vulnerable. Properly parameterised queries can safely handle user-controlled values.

---

## 13. Prevention and Remediation

### Parameterised queries

The most important defence is using parameterised queries or prepared statements.

Instead of constructing SQL through string concatenation, pass values separately from the query structure.

### Example: Python

**Unsafe:**

```python
query = "SELECT * FROM users WHERE id = " + user_id
```

**Safer:**

```python
cursor.execute(
    "SELECT * FROM users WHERE id = ?",
    (user_id,)
)
```

### Additional controls

- Use prepared statements.
- Avoid unnecessary dynamic SQL.
- Allowlist dynamic column names and sort directions.
- Apply least-privilege database permissions.
- Validate input according to business requirements.
- Avoid exposing detailed database errors.
- Keep database drivers and frameworks updated.
- Log suspicious database errors.
- Review stored procedures for unsafe dynamic SQL.

### Least privilege

The application's database account should only have the permissions it needs.

For example, an application that only reads product information should not need unrestricted database administration privileges.

### References

- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [OWASP Query Parameterisation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html)

---

## 14. Testing Checklist

### Discovery
- [ ] Identify database-backed application functionality
- [ ] Identify URL and form parameters
- [ ] Inspect API request bodies
- [ ] Review relevant cookies and headers
- [ ] Establish baseline application behaviour

### Validation
- [ ] Investigate unexpected database errors
- [ ] Compare controlled input variations
- [ ] Assess response differences
- [ ] Investigate potential blind behaviour
- [ ] Consider second-order injection
- [ ] Confirm findings are reproducible

### Tools
- [ ] Inspect requests using Burp Suite
- [ ] Use SQLmap only where authorised
- [ ] Review automated findings manually
- [ ] Record relevant request and response evidence

### Impact
- [ ] Identify affected functionality
- [ ] Determine the database platform where possible
- [ ] Assess potential data exposure
- [ ] Consider database account privileges
- [ ] Avoid accessing unrelated sensitive records

### Reporting
- [ ] Document the affected endpoint and parameter
- [ ] Include safe reproduction steps
- [ ] Explain the underlying cause
- [ ] Describe realistic impact
- [ ] Recommend parameterised queries and least privilege

---

## 15. Further Reading

### Learning resources

- [PortSwigger Web Security Academy – SQL Injection](https://portswigger.net/web-security/sql-injection)
- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [HackTricks – SQL Injection](https://book.hacktricks.wiki/)
- [PayloadsAllTheThings – SQL Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection)
- [SQLmap Documentation](https://github.com/sqlmapproject/sqlmap/wiki)

### Practice environments

- [PortSwigger SQL Injection Labs](https://portswigger.net/web-security/all-labs#sql-injection)
- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)
- [DVWA](https://github.com/digininja/DVWA)
- [WebGoat](https://owasp.org/www-project-webgoat/)

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
