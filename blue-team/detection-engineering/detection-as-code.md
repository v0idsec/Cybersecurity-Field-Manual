# Detection as Code

## Overview

Detection as Code applies software engineering practices to the development, testing, review and deployment of security detections.

Rather than maintaining detection logic exclusively through a SIEM interface, detections are stored in version control and managed through repeatable workflows.

## Benefits

- Version history
- Peer review
- Change tracking
- Repeatable deployment
- Testing and validation
- Easier rollback
- Consistent documentation
- Reduced manual configuration

## Repository Structure

Example:

```text
detections/
├── README.md
├── sigma/
│   ├── windows/
│   ├── linux/
│   ├── cloud/
│   └── network/
├── sentinel/
│   ├── analytics-rules/
│   └── hunting-queries/
├── splunk/
│   ├── detections/
│   └── saved-searches/
├── tests/
│   ├── test-data/
│   └── validation/
└── documentation/
```

The structure should reflect the platforms and workflows used by the organisation.

## Detection Files

Each detection should include:

- Unique identifier
- Name
- Description
- Detection objective
- Query or rule logic
- Required data sources
- Severity
- ATT&CK mapping
- False-positive considerations
- Testing information
- Investigation guidance

## Version Control

Use Git to track changes.

Example workflow:

1. Create a feature branch.
2. Add or modify detection logic.
3. Update documentation.
4. Run validation.
5. Submit a pull request.
6. Obtain peer review.
7. Merge approved changes.
8. Deploy through the approved pipeline.

## Example Git Workflow

```bash
git checkout -b detection/suspicious-powershell

git add detections/

git commit -m "Add suspicious PowerShell detection"

git push -u origin detection/suspicious-powershell
```

## Code Review

Reviewers should assess:

- Detection objective
- Query correctness
- Data source availability
- False-positive handling
- Performance
- Severity
- ATT&CK mapping
- Testing evidence
- Investigation instructions

A detection should not be approved solely because the query executes successfully.

## Automated Validation

Possible validation stages include:

- YAML syntax checks
- Sigma rule validation
- Query syntax validation
- Required metadata checks
- Duplicate identifier checks
- Unit tests against sample events
- Detection regression tests

Example Sigma validation:

```bash
sigma check detections/sigma/
```

The exact command and supported options depend on the installed Sigma CLI version.

## Deployment

Deployment methods may include:

- SIEM APIs
- Infrastructure as Code
- CI/CD pipelines
- Platform-specific deployment tools
- Controlled manual deployment

Separate development, testing and production environments where practical.

## Rollback

Maintain the ability to:

- Restore previous detection versions.
- Disable a faulty rule.
- Revert incorrect exclusions.
- Restore previous configuration.
- Identify who made the change.

Rollback procedures should not silently remove required security coverage.

## Secrets and Sensitive Data

Never commit:

- API keys
- SIEM credentials
- Access tokens
- Private certificates
- Production secrets
- Sensitive customer data
- Unredacted incident evidence

Use approved secret management systems.

## Example Pull Request Checklist

- [ ] Detection objective documented.
- [ ] Required telemetry confirmed.
- [ ] Rule syntax validated.
- [ ] Positive test completed.
- [ ] Negative test completed.
- [ ] False positives documented.
- [ ] Severity justified.
- [ ] ATT&CK mapping reviewed.
- [ ] Investigation guidance included.
- [ ] Peer review completed.

## Further Reading

- Sigma: https://sigmahq.io/
- GitHub Actions: https://docs.github.com/actions
- GitLab CI/CD: https://docs.gitlab.com/ci/
- Detection Rules: https://github.com/elastic/detection-rules

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
