# Threat Hunting with KQL

## Overview

Kusto Query Language (KQL) is used to query telemetry in Microsoft Sentinel, Microsoft Defender and other Microsoft security services.

KQL supports filtering, aggregation, joins, parsing, time-based analysis and correlation.

This guide provides practical query patterns for threat hunting.

## Query Fundamentals

### Select a Table

```kql
SecurityEvent
```

### Filter by Time

```kql
SecurityEvent
| where TimeGenerated > ago(24h)
```

### Filter by Event ID

```kql
SecurityEvent
| where EventID == 4625
```

### Select Columns

```kql
SecurityEvent
| project TimeGenerated, Computer, TargetUserName, IpAddress
```

### Sort Results

```kql
SecurityEvent
| order by TimeGenerated desc
```

### Count Events

```kql
SecurityEvent
| summarize EventCount = count()
```

## Authentication Hunting

### Failed Logons

```kql
SecurityEvent
| where TimeGenerated > ago(24h)
| where EventID == 4625
| summarize Attempts = count()
    by TargetUserName, IpAddress, Computer
| order by Attempts desc
```

### Successful Logons

```kql
SecurityEvent
| where TimeGenerated > ago(24h)
| where EventID == 4624
| project TimeGenerated, Computer, TargetUserName, IpAddress, LogonType
| order by TimeGenerated desc
```

### Privileged Logons

```kql
SecurityEvent
| where TimeGenerated > ago(24h)
| where EventID == 4672
| project TimeGenerated, Computer, SubjectUserName, SubjectLogonId
| order by TimeGenerated desc
```

## Process Hunting

### Process Creation

```kql
SecurityEvent
| where TimeGenerated > ago(24h)
| where EventID == 4688
| project
    TimeGenerated,
    Computer,
    SubjectUserName,
    NewProcessName,
    CommandLine
| order by TimeGenerated desc
```

This query requires process creation auditing and suitable command-line collection.

### Sysmon Process Creation

```kql
WindowsEvent
| where TimeGenerated > ago(24h)
| where Provider == "Microsoft-Windows-Sysmon"
| where EventID == 1
| project TimeGenerated, Computer, EventData
| order by TimeGenerated desc
```

Actual fields depend on the connector and table schema.

## PowerShell Hunting

```kql
WindowsEvent
| where TimeGenerated > ago(24h)
| where EventID == 4104
| project TimeGenerated, Computer, EventData
| order by TimeGenerated desc
```

Review script block content for suspicious behaviour.

## Service Installation Hunting

```kql
SecurityEvent
| where TimeGenerated > ago(7d)
| where EventID == 4697
| project TimeGenerated, Computer, SubjectUserName, ServiceName
| order by TimeGenerated desc
```

## Entra ID Hunting

### Failed Sign-ins

```kql
SigninLogs
| where TimeGenerated > ago(24h)
| where ResultType != "0"
| summarize Attempts = count()
    by UserPrincipalName, IPAddress
| order by Attempts desc
```

### Successful Sign-ins

```kql
SigninLogs
| where TimeGenerated > ago(24h)
| where ResultType == "0"
| project
    TimeGenerated,
    UserPrincipalName,
    IPAddress,
    AppDisplayName,
    Location
| order by TimeGenerated desc
```

### Privileged Role Changes

```kql
AuditLogs
| where TimeGenerated > ago(7d)
| where Category =~ "RoleManagement"
| project TimeGenerated, ActivityDisplayName, InitiatedBy, TargetResources
| order by TimeGenerated desc
```

## Network Hunting

### Unusual Connection Volume

```kql
DeviceNetworkEvents
| where Timestamp > ago(24h)
| summarize ConnectionCount = count()
    by DeviceName, RemoteIP
| order by ConnectionCount desc
```

This table is typically associated with Microsoft Defender XDR advanced hunting.

## Correlation

Use joins to connect related telemetry.

Example:

```kql
let FailedLogons =
    SecurityEvent
    | where TimeGenerated > ago(24h)
    | where EventID == 4625
    | summarize Failures = count()
        by TargetUserName, IpAddress;
let SuccessfulLogons =
    SecurityEvent
    | where TimeGenerated > ago(24h)
    | where EventID == 4624
    | project TargetUserName, IpAddress, SuccessTime = TimeGenerated;
FailedLogons
| join kind=inner SuccessfulLogons
    on TargetUserName, IpAddress
| where Failures >= 5
```

This is a starting point. Refine the time relationship and correlation keys to suit the investigation.

## Query Optimisation

- Filter by time early.
- Filter by event source early.
- Project only required columns.
- Avoid unnecessarily broad joins.
- Use summarisation for large datasets.
- Validate field types.
- Confirm table availability.

## Schema Awareness

Microsoft Sentinel and Defender tables are not interchangeable.

Before using a query:

1. Confirm the table exists.
2. Review available columns.
3. Confirm timestamp fields.
4. Confirm event normalisation.
5. Validate field semantics.

## Further Reading

- KQL Documentation: https://learn.microsoft.com/azure/data-explorer/kusto/query/
- Microsoft Sentinel Hunting: https://learn.microsoft.com/azure/sentinel/hunting
- Defender Advanced Hunting: https://learn.microsoft.com/defender-xdr/advanced-hunting-overview

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
