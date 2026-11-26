#!/usr/bin/env python3

"""
TCP Port Check Template

Checks a predefined list of TCP ports on an authorised target.

Usage:
    python tcp-port-check.py 192.168.1.10

This script performs basic connection checks only.
It does not attempt authentication or exploitation.
"""

import socket
import sys


# Update this list for your assessment.
PORTS = [
    21,
    22,
    25,
    53,
    80,
    110,
    135,
    139,
    143,
    443,
    445,
    3306,
    3389,
    5432,
    8080,
]


def check_port(host, port, timeout=1):
    try:
        with socket.create_connection(
            (host, port),
            timeout=timeout
        ):
            return True

    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


def main():
    if len(sys.argv) != 2:
        print("Usage: python tcp-port-check.py <target>")
        sys.exit(1)

    target = sys.argv[1]

    print(f"[*] Checking TCP ports on {target}")
    print("[*] Only use against authorised targets.\n")

    for port in PORTS:
        if check_port(target, port):
            print(f"[+] TCP/{port}: Open")
        else:
            print(f"[-] TCP/{port}: Closed or filtered")


if __name__ == "__main__":
    main()
