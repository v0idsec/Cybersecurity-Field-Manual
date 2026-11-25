# Threat Hunting with Splunk

## Overview

Splunk Search Processing Language (SPL) is used to search, correlate and analyse machine-generated data.

Splunk can support threat hunting across endpoint, network, identity, cloud and application telemetry.

This guide provides reusable investigation query patterns.

## SPL Fundamentals

### Basic Search

```spl
index=windows
```

### Time Range

```spl
index=windows earliest=-24h latest=now
```

### Filter by Event ID

```spl
index=windows EventCode=4625
```

### Select Fields

```spl
index=windows
| table _time, host, user, src, EventCode
```

### Sort Results

```spl
index=windows
| sort - _time
```

### Count Events

```spl
index=windows
| stats count
```

## Authentication Hunting

### Failed Logons

```spl
index=windows EventCode=4625
| stats count AS failures by user, src, host
| sort - failures
```

### Successful Logons

```spl
index=windows EventCode=4624
| table _time, host, user, src, Logon_Type
| sort - _time
```

### High-Volume Authentication Failures

```spl
index=windows EventCode=4625
| bin _time span=5m
| stats count AS failures by _time, src, user
| where failures >= 10
| sort - failures
```

## Process Hunting

### Process Creation

```spl
index=windows EventCode=4688
| table _time, host, user, New_Process_Name, Creator_Process_Name
| sort - _time
```

### PowerShell Activity

```spl
index=windows EventCode=4104
| table _time, host, user, ScriptBlockText
| sort - _time
```

Field names depend on the deployed event source and parsing configuration.

## Service Installation

```spl
index=windows (EventCode=4697 OR EventCode=7045)
| table _time, host, user, Service_Name, ServiceName
| sort - _time
```

The two event IDs originate from different Windows logs and may expose different fields.

## Network Hunting

### Outbound Connections

```spl
index=firewall action=allowed
| stats count sum(bytes_out) AS outbound_bytes
    by src_ip, dest_ip, dest_port
| sort - outbound_bytes
```

### DNS Query Volume

```spl
index=dns
| stats count by src_ip, query
| where count > 100
| sort - count
```

### Rare Destinations

```spl
index=firewall
| stats count dc(src_ip) AS unique_sources by dest_ip
| where unique_sources <= 2
| sort count
```

These examples depend on the available network data and field mappings.

## Cloud Hunting

### AWS CloudTrail

```spl
index=aws sourcetype=aws:cloudtrail
| stats count by userIdentity.arn, eventName, sourceIPAddress
| sort - count
```

### Azure Activity

```spl
index=azure
| stats count by caller, operationName, resourceGroup
| sort - count
```

Adjust sourcetypes and fields to the actual ingestion configuration.

## Correlation

Use transaction or join-style searches when necessary, but prefer efficient aggregation where possible.

Example: identify accounts with repeated failures and subsequent success.

```spl
index=windows (EventCode=4624 OR EventCode=4625)
| stats
    count(eval(EventCode=4625)) AS failures
    count(eval(EventCode=4624)) AS successes
    by user, src, host
| where failures >= 5 AND successes >= 1
```

This query identifies accounts with both event types in the search window. It does not prove that the success followed the failures. Review timestamps or build a time-aware correlation for that conclusion.

## Query Optimisation

- Specify indexes.
- Restrict the timeframe.
- Filter early.
- Avoid unnecessary wildcards.
- Use `stats` for aggregation.
- Avoid expensive transactions on large datasets.
- Review field extraction.
- Confirm sourcetype consistency.

## Investigation Notes

Document:

- Search timeframe
- Index and sourcetype
- Query
- Result count
- Relevant entities
- Evidence
- Limitations
- Conclusion

## Further Reading

- Splunk Search Reference: https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/
- Splunk Security Content: https://github.com/splunk/security_content
- Splunk Enterprise Security: https://www.splunk.com/en_us/products/enterprise-security.html

---

*Part of the Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
