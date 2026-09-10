#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JAVA_SKILLS = {
    "java-feature-development", "java-debugging", "java-testing",
    "java-refactoring", "spring-api-development", "database-change",
}
SUPERPOWERS_SKILLS = {
    "using-superpowers", "brainstorming", "writing-plans", "executing-plans",
    "test-driven-development", "systematic-debugging", "verification-before-completion",
    "requesting-code-review", "receiving-code-review",
}
JAVA_RULES = {
    "repository-first.md", "coding-style.md", "spring-boot.md", "testing.md",
    "database.md", "security.md", "build-and-offline.md", "verification.md",
}
AGENTS = {"java-code-reviewer.yaml", "java-security-reviewer.yaml", "java-database-reviewer.yaml"}
PIN = "b36e0829c6d0140e93cfef2ca599b1b07d4a7797"


def fm(text: str) -> str:
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    return match.group(1) if match else ""


def validate() -> list[str]:
    errors: list[str] = []

    java_root = ROOT / "skills" / "java"
    actual_java = {p.name for p in java_root.iterdir() if p.is_dir()} if java_root.is_dir() else set()
    if actual_java != JAVA_SKILLS:
        errors.append(f"Java skill set mismatch: expected {sorted(JAVA_SKILLS)}, got {sorted(actual_java)}")
    for name in JAVA_SKILLS:
        path = java_root / name / "SKILL.md"
        if not path.is_file():
            errors.append(f"Missing {path.relative_to(ROOT)}")
            continue
        meta = fm(path.read_text(encoding="utf-8"))
        if not re.search(rf"(?m)^name:\s*{re.escape(name)}\s*$", meta):
            errors.append(f"{path.relative_to(ROOT)}: missing/mismatched name")
        if not re.search(r"(?m)^description:\s*Use when\b", meta):
            errors.append(f"{path.relative_to(ROOT)}: description must be trigger-oriented")

    sp_root = ROOT / "skills" / "superpowers"
    actual_sp = {p.name for p in sp_root.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()} if sp_root.is_dir() else set()
    missing_sp = SUPERPOWERS_SKILLS - actual_sp
    if missing_sp:
        errors.append(f"Missing Superpowers skills: {sorted(missing_sp)}")
    attr = ROOT / "ATTRIBUTION.md"
    if not attr.is_file() or PIN not in attr.read_text(encoding="utf-8"):
        errors.append("Superpowers attribution/pin is missing")
    if not (ROOT / "third_party" / "superpowers" / "LICENSE").is_file():
        errors.append("Superpowers MIT license is missing")

    rules_root = ROOT / "rules" / "java"
    actual_rules = {p.name for p in rules_root.glob("*.md")} if rules_root.is_dir() else set()
    if actual_rules != JAVA_RULES:
        errors.append(f"Java rule set mismatch: expected {sorted(JAVA_RULES)}, got {sorted(actual_rules)}")
    runtime = ROOT / "rules" / "opencode" / "superpowers-runtime.md"
    if not runtime.is_file():
        errors.append("Missing OpenCode Superpowers runtime mapping rule")

    agents_root = ROOT / "agents"
    actual_agents = {p.name for p in agents_root.glob("*.yaml")} if agents_root.is_dir() else set()
    if actual_agents != AGENTS:
        errors.append(f"Agent set mismatch: expected {sorted(AGENTS)}, got {sorted(actual_agents)}")
    for path in agents_root.glob("*.yaml") if agents_root.is_dir() else []:
        text = path.read_text(encoding="utf-8")
        for field in ("name:", "description:", "instructions:", "targets:"):
            if field not in text:
                errors.append(f"{path.relative_to(ROOT)}: missing {field}")
        if not re.search(r"(?m)^\s*-\s+opencode\s*$", text):
            errors.append(f"{path.relative_to(ROOT)}: must target OpenCode")
        if re.search(r"(?m)^\s*(tools|model)\s*:", text):
            errors.append(f"{path.relative_to(ROOT)}: common tools/model are intentionally forbidden")

    generated = [p for p in ROOT.rglob("*") if ".opencode" in p.parts]
    if generated:
        errors.append(f"Generated .opencode artifacts must not be committed: {generated}")

    cfg = ROOT / "teamai.yaml"
    if cfg.is_file() and "github.com/lingyi9909/teamai-harness" in cfg.read_text(encoding="utf-8"):
        errors.append("teamai.yaml pins the public template URL; let teamai init create config from the intranet remote")

    offline = ROOT / "rules" / "java" / "build-and-offline.md"
    if offline.is_file():
        lower = offline.read_text(encoding="utf-8").lower()
        for phrase in ("internal mirror", "public network", "maven wrapper", "gradle wrapper"):
            if phrase not in lower:
                errors.append(f"build-and-offline.md missing requirement: {phrase}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("TEAMAI_HARNESS_VALIDATION FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("TEAMAI_HARNESS_VALIDATION PASS")
    print(f"java_skills={len(JAVA_SKILLS)} superpowers_required={len(SUPERPOWERS_SKILLS)} java_rules={len(JAVA_RULES)} agents={len(AGENTS)}")
    print(f"superpowers_pin={PIN}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
