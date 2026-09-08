#!/usr/bin/env python3

"""
MailTrace URL and domain defanging utility.

Purpose:
    Convert URLs and domain names into safer forms for security reports,
    notes, and public documentation.

Examples:
    https://example.com/login
    -> hxxps://example[.]com/login

    http://example.com
    -> hxxp://example[.]com

The tool performs text transformation only. It does not resolve,
connect to, or otherwise access the supplied indicators.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


URL_PATTERN = re.compile(
    r"(?i)\bhttps?://[^\s<>'\"`]+"
)

DOMAIN_PATTERN = re.compile(
    r"(?i)(?<![@\w.-])"
    r"(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+"
    r"[a-z]{2,63}"
    r"(?![\w.-])"
)


def defang_url(url: str) -> str:
    """Defang a URL without contacting the destination."""
    value = url.rstrip(".,;:!?)]}")
    value = re.sub(r"(?i)^https://", "hxxps://", value)
    value = re.sub(r"(?i)^http://", "hxxp://", value)

    scheme_split = value.find("://")
    if scheme_split != -1:
        scheme = value[:scheme_split + 3]
        remainder = value[scheme_split + 3:]
        remainder = remainder.replace(".", "[.]")
        return scheme + remainder

    return value.replace(".", "[.]")


def defang_domain(domain: str) -> str:
    """Defang a domain name without contacting the destination."""
    return domain.replace(".", "[.]")


def defang_text(text: str) -> str:
    """Defang URLs first, then remaining domain names."""
    protected: list[str] = []

    def protect_url(match: re.Match[str]) -> str:
        token = f"__MAILTRACE_URL_{len(protected)}__"
        protected.append(defang_url(match.group(0)))
        return token

    transformed = URL_PATTERN.sub(protect_url, text)

    transformed = DOMAIN_PATTERN.sub(
        lambda match: defang_domain(match.group(0)),
        transformed,
    )

    for index, value in enumerate(protected):
        transformed = transformed.replace(
            f"__MAILTRACE_URL_{index}__",
            value,
        )

    return transformed


def read_input(path: str | None) -> str:
    """Read text from a file or standard input."""
    if path:
        return Path(path).read_text(encoding="utf-8")

    return sys.stdin.read()


def build_parser() -> argparse.ArgumentParser:
    """Build the command line argument parser."""
    parser = argparse.ArgumentParser(
        description="Safely defang URLs and domains for MailTrace documentation."
    )

    parser.add_argument(
        "text",
        nargs="?",
        help="Text containing URLs or domains to defang.",
    )

    parser.add_argument(
        "-f",
        "--file",
        dest="file",
        help="Read input text from a file.",
    )

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.text is not None and args.file is not None:
        parser.error("Use either positional text or --file, not both.")

    if args.text is not None:
        source = args.text
    else:
        try:
            source = read_input(args.file)
        except FileNotFoundError:
            print(f"Error: file not found: {args.file}", file=sys.stderr)
            return 1
        except OSError as exc:
            print(f"Error reading input: {exc}", file=sys.stderr)
            return 1

    if not source:
        print("Error: no input supplied.", file=sys.stderr)
        return 1

    print(defang_text(source))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())