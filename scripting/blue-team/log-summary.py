#!/usr/bin/env python3

"""
Log Summary Template

Summarises a text log file by counting lines containing
common severity labels and configurable keywords.

Usage:
    python log-summary.py application.log

This is a simple text-based helper. It does not replace
a dedicated log parser or SIEM.
"""

import sys
from collections import Counter
from pathlib import Path


SEVERITY_LABELS = [
    "critical",
    "error",
    "warning",
    "warn",
    "info",
    "debug",
]

KEYWORDS = [
    "failed",
    "denied",
    "unauthorised",
    "unauthorized",
    "timeout",
    "exception",
]


def analyse_log(file_path):

    path = Path(file_path)

    if not path.is_file():
        print(f"[-] File not found: {path}")
        return

    severity_counts = Counter()
    keyword_counts = Counter()

    total_lines = 0

    with path.open(
        "r",
        encoding="utf-8",
        errors="replace"
    ) as log_file:

        for line in log_file:

            total_lines += 1
            content = line.lower()

            for severity in SEVERITY_LABELS:
                if severity in content:
                    severity_counts[severity] += 1

            for keyword in KEYWORDS:
                if keyword in content:
                    keyword_counts[keyword] += 1

    print(f"\n[*] Log file: {path}")
    print(f"[*] Total lines: {total_lines}")

    print("\n[+] Severity matches:")

    for severity, count in severity_counts.most_common():
        print(f"    {severity}: {count}")

    print("\n[+] Keyword matches:")

    for keyword, count in keyword_counts.most_common():
        print(f"    {keyword}: {count}")


def main():

    if len(sys.argv) != 2:
        print("Usage: python log-summary.py <logfile>")
        sys.exit(1)

    analyse_log(sys.argv[1])


if __name__ == "__main__":
    main()
