#!/usr/bin/env python3

"""
HTTP Header Review Template

Retrieves HTTP response headers and checks for common
security-related headers.

Usage:
    python http-header-review.py https://example.com

Uses Python's standard library.
"""

import sys
import urllib.request
import urllib.error


SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
    "Cross-Origin-Opener-Policy",
]


def review_headers(url):

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Security-Header-Review/1.0"
        },
        method="GET"
    )

    try:
        with urllib.request.urlopen(
            request,
            timeout=10
        ) as response:

            print(f"[*] URL: {url}")
            print(f"[*] Status: {response.status}\n")

            headers = response.headers

            print("[+] Response headers:")

            for name, value in headers.items():
                print(f"{name}: {value}")

            print("\n[*] Security header review:")

            for header in SECURITY_HEADERS:

                if headers.get(header):
                    print(f"[+] Present: {header}")
                else:
                    print(f"[-] Missing: {header}")

    except urllib.error.HTTPError as error:
        print(f"[-] HTTP error: {error.code}")

    except urllib.error.URLError as error:
        print(f"[-] Connection error: {error.reason}")

    except TimeoutError:
        print("[-] Request timed out.")


def main():

    if len(sys.argv) != 2:
        print("Usage: python http-header-review.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    if not url.startswith(("http://", "https://")):
        print("[-] Supply a complete HTTP or HTTPS URL.")
        sys.exit(1)

    review_headers(url)


if __name__ == "__main__":
    main()
