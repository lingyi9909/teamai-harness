from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

JAVA_SKILLS = {
    "java-feature-development",
    "java-debugging",
    "java-testing",
    "java-refactoring",
    "spring-api-development",
    "database-change",
}
SUPERPOWERS_SKILLS = {
    "using-superpowers",
    "brainstorming",
    "writing-plans",
    "executing-plans",
    "test-driven-development",
    "systematic-debugging",
    "verification-before-completion",
    "requesting-code-review",
    "receiving-code-review",
}
JAVA_RULES = {
    "repository-first.md",
    "coding-style.md",
    "spring-boot.md",
    "testing.md",
    "database.md",
    "security.md",
    "build-and-offline.md",
    "verification.md",
}
OPEN_CODE_AGENTS = {
    "java-code-reviewer.yaml",
    "java-security-reviewer.yaml",
    "java-database-reviewer.yaml",
}


def frontmatter(text: str) -> str:
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    return match.group(1) if match else ""


class HarnessContractTest(unittest.TestCase):
    def test_required_java_skills_exist_with_teamai_skill_frontmatter(self) -> None:
        base = ROOT / "skills" / "java"
        self.assertTrue(base.is_dir())
        self.assertEqual(JAVA_SKILLS, {p.name for p in base.iterdir() if p.is_dir()})
        for name in JAVA_SKILLS:
            skill = base / name / "SKILL.md"
            self.assertTrue(skill.is_file(), skill)
            fm = frontmatter(skill.read_text(encoding="utf-8"))
            self.assertRegex(fm, rf"(?m)^name:\s*{re.escape(name)}\s*$")
            self.assertRegex(fm, r"(?m)^description:\s*Use when\b")

    def test_required_superpowers_skills_are_vendored(self) -> None:
        base = ROOT / "skills" / "superpowers"
        actual = {p.name for p in base.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()}
        self.assertTrue(SUPERPOWERS_SKILLS.issubset(actual))
        attribution = (ROOT / "ATTRIBUTION.md").read_text(encoding="utf-8")
        self.assertIn("b36e0829c6d0140e93cfef2ca599b1b07d4a7797", attribution)
        self.assertTrue((ROOT / "third_party" / "superpowers" / "LICENSE").is_file())

    def test_java_rules_and_opencode_superpowers_runtime_rule_exist(self) -> None:
        java_rules = ROOT / "rules" / "java"
        self.assertEqual(JAVA_RULES, {p.name for p in java_rules.glob("*.md")})
        runtime_rule = ROOT / "rules" / "opencode" / "superpowers-runtime.md"
        text = runtime_rule.read_text(encoding="utf-8")
        self.assertIn("superpowers:<name>", text)
        self.assertIn("using-superpowers", text)
        self.assertIn("todowrite", text)
        self.assertIn("task", text)
        self.assertIn("skill", text)

    def test_agents_use_canonical_teamai_yaml_and_target_only_opencode(self) -> None:
        agents = ROOT / "agents"
        self.assertEqual(OPEN_CODE_AGENTS, {p.name for p in agents.glob("*.yaml")})
        for path in agents.glob("*.yaml"):
            text = path.read_text(encoding="utf-8")
            for field in ("name:", "description:", "instructions:", "targets:"):
                self.assertIn(field, text, f"{path}: missing {field}")
            self.assertRegex(text, r"(?m)^\s*-\s+opencode\s*$")
            self.assertNotRegex(text, r"(?m)^\s*tools\s*:")
            self.assertNotRegex(text, r"(?m)^\s*model\s*:")
            self.assertNotIn("claude", text.lower())
            self.assertNotIn("codex", text.lower())

    def test_template_contains_no_generated_opencode_tree(self) -> None:
        offenders = [p for p in ROOT.rglob("*") if ".opencode" in p.parts]
        self.assertEqual([], offenders)

    def test_template_does_not_pin_public_repo_in_teamai_yaml(self) -> None:
        config = ROOT / "teamai.yaml"
        if not config.exists():
            return
        text = config.read_text(encoding="utf-8")
        self.assertNotIn("github.com/lingyi9909/teamai-harness", text)

    def test_offline_rule_blocks_public_runtime_dependency_fetches(self) -> None:
        text = (ROOT / "rules" / "java" / "build-and-offline.md").read_text(encoding="utf-8").lower()
        for phrase in ("internal mirror", "public network", "maven wrapper", "gradle wrapper"):
            self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
