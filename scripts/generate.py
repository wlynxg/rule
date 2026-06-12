#!/usr/bin/env python3
"""
将 sources/ 下的域名列表生成 Clash rule-provider 格式的 YAML 文件。
输出到 dist/ 目录。

Clash rule-provider YAML 格式:
  payload:
    - DOMAIN-SUFFIX,example.com
    - DOMAIN,exact.example.com
"""

import os
import sys
from pathlib import Path

RULE_TYPES = ["proxy", "direct", "reject"]
CLASH_ACTIONS = {
    "proxy": None,   # rule-provider 不带 action, 由配置决定
    "direct": None,
    "reject": None,
}
SOURCES_DIR = Path("sources")
DIST_DIR = Path("dist")


def load_domains(filepath: Path) -> list[str]:
    """读取域名列表，忽略空行和注释"""
    domains = []
    if not filepath.exists():
        return domains
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            domains.append(line)
    return domains


def generate_rule_provider(domains: list[str]) -> str:
    """生成 Clash rule-provider YAML 格式"""
    lines = ["payload:"]
    for domain in domains:
        # 前缀匹配 *.domain 的用 DOMAIN-SUFFIX
        if domain.startswith("*."):
            suffix = domain[2:]
            lines.append(f"  - DOMAIN-SUFFIX,{suffix}")
        elif domain.startswith("+."):
            suffix = domain[2:]
            lines.append(f"  - DOMAIN-SUFFIX,{suffix}")
        else:
            lines.append(f"  - DOMAIN-SUFFIX,{domain}")
    if not domains:
        lines.append("  # (empty)")
    return "\n".join(lines) + "\n"


def main():
    DIST_DIR.mkdir(parents=True, exist_ok=True)

    for rule_type in RULE_TYPES:
        src = SOURCES_DIR / f"{rule_type}.txt"
        dst = DIST_DIR / f"{rule_type}.yaml"

        domains = load_domains(src)
        yaml_content = generate_rule_provider(domains)

        with open(dst, "w", encoding="utf-8") as f:
            f.write(yaml_content)

        print(f"[OK] {rule_type}: {len(domains)} rules -> {dst}")


if __name__ == "__main__":
    main()
