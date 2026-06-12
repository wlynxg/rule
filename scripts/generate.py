#!/usr/bin/env python3
"""Generate Clash rule provider file from source domain lists."""

import os

SOURCES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sources")
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "dist")


def load_domains(filepath):
    """Load non-empty, non-comment lines from a domain list file."""
    domains = []
    if not os.path.exists(filepath):
        return domains
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                domains.append(line)
    return sorted(set(domains))


def build_rule(domain):
    """Convert a domain pattern to a DOMAIN-SUFFIX rule."""
    if domain.startswith("*."):
        domain = domain[1:]
    return f"DOMAIN-SUFFIX,{domain}"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    all_rules = []
    for filename in sorted(os.listdir(SOURCES_DIR)):
        if not filename.endswith(".txt"):
            continue
        filepath = os.path.join(SOURCES_DIR, filename)
        domains = load_domains(filepath)
        for domain in domains:
            all_rules.append(build_rule(domain))

    output_file = os.path.join(OUTPUT_DIR, "rule.yaml")
    with open(output_file, "w") as f:
        f.write("# Clash Rule Provider - Auto Generated\n")
        f.write("# Source: https://github.com/wlynxg/rule\n")
        f.write("payload:\n")
        for rule in all_rules:
            f.write(f"  - {rule}\n")

    print(f"Generated {len(all_rules)} rules -> {output_file}")


if __name__ == "__main__":
    main()
