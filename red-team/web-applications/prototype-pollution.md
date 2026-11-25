
# JavaScript Prototype Pollution

> Professional reference guide for identifying, validating and assessing JavaScript prototype pollution vulnerabilities.

## Contents

- [Overview](#overview)
- [JavaScript Prototype Fundamentals](#javascript-prototype-fundamentals)
- [Prototype Pollution](#prototype-pollution)
- [Common Sources](#common-sources)
- [Dangerous Operations](#dangerous-operations)
- [Client-Side Assessment](#client-side-assessment)
- [Server-Side Assessment](#server-side-assessment)
- [Exploitation Primitives](#exploitation-primitives)
- [Assessment Methodology](#assessment-methodology)
- [Impact Analysis](#impact-analysis)
- [Validation and Evidence](#validation-and-evidence)
- [Mitigation](#mitigation)
- [Tools and References](#tools-and-references)
- [Assessment Checklist](#assessment-checklist)

---

## Overview

Prototype pollution is a JavaScript vulnerability in which an attacker can modify properties on an object's prototype.

Because JavaScript objects can inherit properties from their prototypes, modifying a shared prototype may influence the behaviour of other objects throughout an application.

Prototype pollution can occur in:

- Client-side JavaScript applications.
- Node.js applications.
- API endpoints processing JSON.
- Third-party JavaScript libraries.
- Configuration and object-merging functionality.

Potential consequences include:

- Application logic manipulation.
- Security control bypass.
- Denial of service.
- Cross-site scripting.
- Server-side code execution in vulnerable environments.
- Authentication or authorisation weaknesses.

Prototype pollution is often an enabling vulnerability rather than a complete exploit by itself.

## JavaScript Prototype Fundamentals

JavaScript objects can inherit properties from another object through their prototype chain.

For example:

```javascript
const user = {
    name: "Alice"
};

console.log(user.name);
console.log(user.toString);
```

The `name` property belongs directly to the object.

The `toString` method is inherited through the prototype chain.

The special property `__proto__` can expose or modify an object's prototype in environments where it is supported.

```javascript
const example = {};

console.log(Object.getPrototypeOf(example));
```

Other relevant mechanisms include:

- `Object.prototype`
- `Object.getPrototypeOf()`
- `Object.setPrototypeOf()`
- Constructor properties.
- Prototype inheritance.
- Property descriptors.

## Prototype Pollution

Prototype pollution occurs when untrusted input can influence prototype-related properties or operations.

A common example involves unsafe object merging.

```javascript
function merge(target, source) {
    for (const key in source) {
        target[key] = source[key];
    }

    return target;
}
```

If an application passes attacker-controlled objects into an unsafe merge function, inherited or prototype-related properties may be processed unexpectedly.

The precise outcome depends on the merge implementation and JavaScript runtime.

### Common Pollution Properties

Commonly investigated property names include:

| Property | Relevance |
|---|---|
| `__proto__` | Prototype accessor in many JavaScript environments |
| `constructor` | Constructor reference on objects |
| `prototype` | Prototype property on constructor functions |

These properties are not automatically exploitable. Their behaviour depends on the specific operation and implementation.

## Common Sources

Look for untrusted input flowing into object manipulation functionality.

### JSON Input

```json
{
  "preferences": {
    "theme": "dark"
  }
}
```

Investigate whether nested JSON properties are merged into application configuration or shared objects.

### Query Parameters

Applications may convert query parameters into nested objects.

Example structure:

```text
?preferences[theme]=dark
```

Investigate:

- Nested parameter parsing.
- Array construction.
- Object assignment.
- Parameter-to-object conversion.
- Recursive merge functions.

### Configuration Merging

Configuration systems frequently combine:

- Default values.
- Environment configuration.
- User preferences.
- Request-specific options.
- Third-party library configuration.

Unsafe merging can expose prototype manipulation opportunities.

### Third-Party Libraries

Review dependencies that perform:

- Deep merging.
- Object cloning.
- Path assignment.
- Nested property access.
- Configuration processing.
- Query-string parsing.

Library vulnerabilities may affect applications even where the application code itself appears safe.

## Dangerous Operations

Pay particular attention to the following patterns.

### Object Assignment

```javascript
Object.assign(target, source);
```

The security implications depend on the source object's properties and how they are created.

### Deep Merge Functions

```javascript
merge(target, source);
```

Review whether the function:

- Recursively processes nested properties.
- Handles special property names safely.
- Uses own-property checks.
- Prevents prototype traversal.
- Accepts arbitrary attacker-controlled objects.

### Dynamic Property Assignment

```javascript
object[userSuppliedKey] = value;
```

Investigate whether user-controlled keys can reference prototype-related properties.

### Path-Based Property Setters

```javascript
setValue(object, "settings.theme", "dark");
```

Path-based setters can become dangerous if they permit traversal into prototype-related properties.

## Client-Side Assessment

Client-side prototype pollution occurs in browser-executed JavaScript.

### Identify Input Sources

Inspect:

- URL query parameters.
- URL fragments.
- POST messages.
- Local storage.
- Session storage.
- JSON responses.
- DOM-derived values.
- Third-party scripts.

### Identify Potential Sinks

Look for code that:

- Merges user-controlled objects.
- Assigns dynamic property names.
- Processes nested object paths.
- Modifies application configuration.
- Reads inherited properties for security decisions.

### Confirm Pollution

In an authorised test environment, use a harmless, unique property to determine whether attacker-controlled input affects a shared prototype.

For example, a controlled test may use a property named:

```text
pp_test_marker
```

The validation objective is to establish whether the property becomes visible on unrelated objects through inheritance.

Do not assume that a property appearing on one object proves global prototype pollution.

### Identify Security-Relevant Gadgets

A gadget is an application behaviour that uses a polluted property in a security-relevant way.

Examples include code that reads inherited properties when deciding:

- Which HTML element to create.
- Which URL to navigate to.
- Which script or resource to load.
- Which application option to enable.
- Which template or rendering operation to perform.

Investigate the complete data flow before assigning impact.

## Server-Side Assessment

Node.js applications may be affected when attacker-controlled data reaches unsafe object operations.

Review:

- API request processing.
- JSON deserialisation.
- Configuration endpoints.
- User profile updates.
- Template engines.
- Logging and serialisation.
- Background job processing.
- Third-party dependencies.

### Server-Side Indicators

Look for:

- Unexpected properties on newly created objects.
- Configuration values changing unexpectedly.
- Application behaviour changing between requests.
- Security checks relying on inherited properties.
- Exceptions during object processing.
- Unexpected child-process or template behaviour.

Avoid testing code execution or process manipulation on production systems unless explicitly authorised and safely isolated.

## Exploitation Primitives

Prototype pollution may become exploitable when a polluted property reaches a useful application gadget.

Potential exploitation categories include:

| Category | Potential outcome |
|---|---|
| DOM manipulation | Unexpected elements or attributes |
| URL manipulation | Navigation or resource loading changes |
| Template manipulation | Altered rendering behaviour |
| Configuration manipulation | Security control changes |
| Authentication logic | Incorrect inherited-property checks |
| Server-side gadgets | Potential process or code execution impact |

### From Pollution to Impact

A useful assessment distinguishes:

1. A controllable input source.
2. An unsafe property assignment or merge operation.
3. A confirmed prototype modification.
4. A security-relevant gadget.
5. A demonstrable impact.

Do not report prototype pollution as remote code execution without demonstrating the complete exploit chain.

## Assessment Methodology

### 1. Map JavaScript Functionality

Identify:

- Application framework.
- Client-side dependencies.
- Server-side runtime.
- API endpoints.
- Object-processing functionality.
- Configuration and preference systems.

### 2. Review Dependencies

Prioritise libraries involved in:

- Deep merging.
- Object assignment.
- Query parsing.
- Path manipulation.
- Serialisation.
- Template rendering.

Check dependency versions against known advisories.

### 3. Trace Untrusted Input

Follow data from the source to the operation that creates or modifies objects.

Document:

- Input location.
- Parsing behaviour.
- Transformations.
- Assignment or merge operation.
- Resulting object.
- Security-relevant property usage.

### 4. Test for Pollution

Use unique, harmless test properties.

Determine whether:

- The property is accepted.
- It is assigned to the intended object.
- It reaches a prototype.
- It affects unrelated objects.
- It persists between requests or sessions.

### 5. Identify Gadgets

Search for application code that reads inherited properties.

Determine whether the polluted property can influence a meaningful security decision.

### 6. Validate Impact

Prefer controlled, reversible demonstrations.

Avoid destructive actions, sensitive data access and unauthorised execution.

## Impact Analysis

Consider:

- Whether pollution is client-side or server-side.
- Whether the pollution affects one object or a shared prototype.
- Whether it persists across requests.
- Whether it affects other users.
- Whether a security-relevant gadget exists.
- Whether exploitation requires authentication.
- Whether a dependency or application component is responsible.

Prototype pollution without an exploitable gadget may still represent a security weakness, but severity should reflect demonstrated impact.

## Validation and Evidence

Collect:

- Affected endpoint or functionality.
- Relevant input.
- Raw request and response.
- JavaScript source or dependency information.
- Pollution confirmation.
- Gadget or affected application behaviour.
- Reproduction steps.
- Browser or runtime version.
- User authentication requirements.
- Demonstrated impact.

Use unique marker properties to avoid interfering with normal application state.

## Mitigation

Recommended controls:

- Avoid merging untrusted objects into sensitive objects.
- Reject dangerous property names.
- Use `Object.hasOwn()` or equivalent own-property checks.
- Use `Object.create(null)` for suitable dictionary structures.
- Prefer `Map` for user-controlled key/value collections.
- Avoid unsafe recursive merge implementations.
- Validate object schemas.
- Use allowlists for accepted properties.
- Keep dependencies patched.
- Review libraries that process nested objects.
- Avoid relying on inherited properties for security decisions.

Freezing prototypes may provide additional protection in some environments, but it should not replace safe input handling and object manipulation.

## Tools and References

### Tools

- Browser developer tools.
- Burp Suite.
- DOM Invader.
- JavaScript source inspection.
- Node.js debugging tools.
- Dependency auditing tools.
- Prototype pollution detection tools.

### References

- [PortSwigger — Prototype Pollution](https://portswigger.net/web-security/prototype-pollution)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [MDN — Inheritance and the Prototype Chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)
- [MDN — Object.prototype](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/prototype)
- [CWE-1321 — Improperly Controlled Modification of Object Prototype Attributes](https://cwe.mitre.org/data/definitions/1321.html)

## Assessment Checklist

- [ ] Client-side and server-side JavaScript components identified.
- [ ] Relevant dependencies reviewed.
- [ ] Untrusted object sources identified.
- [ ] Merge and assignment operations reviewed.
- [ ] Prototype-related property handling assessed.
- [ ] Pollution confirmed using harmless markers.
- [ ] Shared prototype impact established.
- [ ] Security-relevant gadgets investigated.
- [ ] Impact demonstrated safely.
- [ ] Dependency and application remediation documented.

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
