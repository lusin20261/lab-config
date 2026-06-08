#!/usr/bin/env python3

from pathlib import Path

MODE_FILE = "mode.txt"
BLOCKED_FILE = "blocked.txt"

OUTPUT_FILE = "/etc/dnsmasq.d/lab-filter.conf"


def read_mode():
    try:
        return Path(MODE_FILE).read_text().strip().lower()
    except FileNotFoundError:
        return "open"


def read_domains():
    try:
        return [
            line.strip()
            for line in Path(BLOCKED_FILE).read_text().splitlines()
            if line.strip() and not line.startswith("#")
        ]
    except FileNotFoundError:
        return []


mode = read_mode()
domains = read_domains()

rules = []

if mode == "class":
    rules.append("# Generated automatically\n")

    for domain in domains:
        rules.append(f"address=/{domain}/0.0.0.0")
        rules.append(f"address=/www.{domain}/0.0.0.0")

else:
    rules.append("# Open mode\n")


with open(OUTPUT_FILE, "w") as f:
    f.write("\n".join(rules))

print(f"Generated {OUTPUT_FILE}")
print(f"Mode: {mode}")
print(f"Domains: {len(domains)}")
