#!/usr/bin/env python3

"""
File Integrity Template

Calculates SHA-256 hashes for files in a specified directory.

Can be used to establish a baseline for later integrity checks.

Usage:
    python file-integrity.py /path/to/directory

This template does not modify files.
"""

import hashlib
import sys
from pathlib import Path


def calculate_hash(file_path):

    sha256 = hashlib.sha256()

    try:
        with file_path.open("rb") as file:

            for chunk in iter(
                lambda: file.read(65536),
                b""
            ):
                sha256.update(chunk)

        return sha256.hexdigest()

    except OSError as error:
        print(f"[-] Unable to read {file_path}: {error}")
        return None


def scan_directory(directory):

    root = Path(directory)

    if not root.is_dir():
        print("[-] Supplied path is not a directory.")
        return

    print(f"[*] Calculating SHA-256 hashes in: {root}\n")

    for file_path in sorted(root.rglob("*")):

        if not file_path.is_file():
            continue

        file_hash = calculate_hash(file_path)

        if file_hash:
            print(f"{file_hash}  {file_path}")


def main():

    if len(sys.argv) != 2:
        print("Usage: python file-integrity.py <directory>")
        sys.exit(1)

    scan_directory(sys.argv[1])


if __name__ == "__main__":
    main()
