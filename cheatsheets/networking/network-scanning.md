# Network Scanning Cheatsheet

Quick-reference commands for network discovery, port scanning and service identification using Nmap.

## Important

Only scan systems and networks you own or have explicit permission to assess.

Network scanning can generate significant traffic, trigger security alerts or disrupt fragile services.

## Nmap basics

Check version:

```bash
nmap --version
```

Display help:

```bash
nmap -h
```

Scan a host:

```bash
nmap 192.0.2.10
```

Scan multiple hosts:

```bash
nmap 192.0.2.10 192.0.2.11
```

Scan a subnet:

```bash
nmap 192.0.2.0/24
```

Scan a hostname:

```bash
nmap example.com
```

## Host discovery

Discover hosts without a port scan:

```bash
nmap -sn 192.0.2.0/24
```

Disable host discovery and scan the specified target:

```bash
nmap -Pn 192.0.2.10
```

Use `-Pn` when host discovery probes are blocked and the target is known to be in scope.

## Port scanning

Scan common ports:

```bash
nmap 192.0.2.10
```

Scan specific ports:

```bash
nmap -p 22,80,443 192.0.2.10
```

Scan a port range:

```bash
nmap -p 1-1000 192.0.2.10
```

Scan all TCP ports:

```bash
nmap -p- 192.0.2.10
```

Scan UDP ports:

```bash
nmap -sU 192.0.2.10
```

## Service detection

Identify service versions:

```bash
nmap -sV 192.0.2.10
```

Operating system detection:

```bash
sudo nmap -O 192.0.2.10
```

Combined service and OS detection:

```bash
sudo nmap -sV -O 192.0.2.10
```

## Scan types

| Option | Purpose |
|---|---|
| `-sS` | TCP SYN scan |
| `-sT` | TCP connect scan |
| `-sU` | UDP scan |
| `-sV` | Service version detection |
| `-O` | OS detection |
| `-sn` | Host discovery only |
| `-Pn` | Skip host discovery |
| `-p` | Specify ports |
| `-p-` | Scan all TCP ports |
| `-n` | Disable DNS resolution |
| `-R` | Force DNS resolution |

## Nmap scripts

List available scripts:

```bash
ls /usr/share/nmap/scripts/
```

Search scripts:

```bash
grep -i smb /usr/share/nmap/scripts/script.db
```

Run default scripts:

```bash
nmap -sC 192.0.2.10
```

Run selected scripts:

```bash
nmap --script smb-protocols 192.0.2.10
```

Run vulnerability detection scripts against an authorised target:

```bash
nmap --script vuln 192.0.2.10
```

NSE scripts vary in behaviour. Review scripts before execution, particularly those that may be intrusive or disruptive.

## Output formats

Normal output:

```bash
nmap -oN scan.txt 192.0.2.10
```

XML output:

```bash
nmap -oX scan.xml 192.0.2.10
```

Grepable output:

```bash
nmap -oG scan.gnmap 192.0.2.10
```

All formats:

```bash
nmap -oA scan-results 192.0.2.10
```

## Timing options

| Option | Purpose |
|---|---|
| `-T0` | Very slow |
| `-T1` | Slow |
| `-T2` | Reduced speed |
| `-T3` | Default |
| `-T4` | Faster |
| `-T5` | Very aggressive |

Aggressive timing can cause missed results, network load or service disruption. Choose based on the approved test plan.

## Common assessment commands

Basic service scan:

```bash
nmap -sV -sC -oA baseline 192.0.2.10
```

Full TCP port scan:

```bash
nmap -p- -sV -oA full-tcp 192.0.2.10
```

UDP scan of selected common ports:

```bash
sudo nmap -sU -p 53,67,123,161 192.0.2.10
```

Subnet discovery:

```bash
nmap -sn 192.0.2.0/24 -oA subnet-discovery
```

## Port states

| State | Meaning |
|---|---|
| Open | Service is accepting connections |
| Closed | Host is reachable but no service is listening |
| Filtered | Nmap cannot determine the state due to filtering |
| Unfiltered | Port is reachable but state is unknown |
| Open\|Filtered | Cannot determine whether open or filtered |
| Closed\|Filtered | Cannot determine whether closed or filtered |

## Notes

- A port scan is not a vulnerability assessment.
- Service version detection can be inaccurate.
- UDP scans can be slow and inconclusive.
- Firewalls may alter scan results.
- Record scope, timing, source IP and scan options.
- Validate important findings manually.

---

*Cybersecurity Field Manual — Recon. Exploit. Detect. Defend. Improve.*
