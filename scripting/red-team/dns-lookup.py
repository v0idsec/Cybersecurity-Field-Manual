#!/usr/bin/env python3

"""
DNS Lookup Template

Performs basic DNS resolution for a supplied hostname.

Usage:
    python dns-lookup.py example.com

Uses Python's standard library.
"""

import socket
import sys


def resolve_hostname(hostname):
    print(f"[*] Resolving: {hostname}")

    try:
        results = socket.getaddrinfo(
            hostname,
            None,
            proto=socket.IPPROTO_TCP
        )

        addresses = sorted({
            result[4][0]
            for result in results
        })

        if not addresses:
            print("[-] No addresses returned.")
            return

        print("\n[+] Resolved addresses:")

        for address in addresses:
            print(f"    {address}")

    except socket.gaierror as error:
        print(f"[-] DNS resolution failed: {error}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python dns-lookup.py <hostname>")
        sys.exit(1)

    hostname = sys.argv[1]

    resolve_hostname(hostname)


if __name__ == "__main__":
    main()
