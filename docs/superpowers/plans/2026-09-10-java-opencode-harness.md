# TeamAI Java + OpenCode Harness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver a standalone TeamAI team repository that can be copied into an intranet and initialized into Java business repositories using OpenCode.

**Architecture:** Keep TeamAI source resources canonical in this repository and let TeamAI CLI render/sync them into OpenCode. Vendor the current upstream Superpowers skills under their own namespace, add a small Java-specific skill/rule layer, and define OpenCode-targeted TeamAI agent YAML rather than committing generated `.opencode/*` artifacts.

**Tech Stack:** TeamAI CLI 0.22.x source contract, OpenCode, Markdown/YAML, Java 17+/21, Spring Boot 3.x, Maven/Gradle, JUnit 5.

**Spec:** `docs/superpowers/specs/2026-09-10-teamai-java-opencode-harness-design.md`

## Global Constraints

- Canonical TeamAI resources only; never commit generated `.opencode/*` copies.
- OpenCode is the only required agent target for custom reviewer agents.
- OpenCode project resources must rely on TeamAI's current default paths: `.opencode/skills`, `.opencode/rules`, `.opencode/agents`, plus root `opencode.json` instructions activation managed by TeamAI.
- No Claude/Codex-only model or tool semantics in Java resources.
- Normal intranet development must not require public network access.
- Repository-local Maven/Gradle wrappers and configured internal mirrors take precedence over public package registries.
- Project evidence (`pom.xml`, `build.gradle*`, wrappers, source/tests and local instructions) overrides framework/version assumptions.
- Keep the resource set focused on high-frequency Java development rather than a broad low-frequency workflow catalog.

---

### Task 1: TeamAI repository contract and machine validation

**Files:**
- Create: `teamai.yaml`
- Create: `scripts/validate_harness.py`
- Create: `tests/test_harness.py`

**Interfaces:**
- Consumes: TeamAI `TeamaiConfigSchema`, canonical Skill and Agent formats.
- Produces: a repository-level validation command `python scripts/validate_harness.py` and tests that fail when required resources or OpenCode constraints are broken.

- [ ] **Step 1:** Add failing tests for required TeamAI config fields, Skill frontmatter, canonical agent YAML, OpenCode-only agent targets, generated-artifact prohibition, and public-network-command prohibition.
- [ ] **Step 2:** Run `python -m unittest discover -s tests -v` and confirm failures because implementation resources are missing.
- [ ] **Step 3:** Add the smallest validator and TeamAI config that satisfy the contract.
- [ ] **Step 4:** Re-run tests and keep them green as later tasks add resources.

### Task 2: Vendor current Superpowers core skills

**Files:**
- Create: `skills/superpowers/<skill>/...`
- Create: `third_party/superpowers/LICENSE`
- Create: `ATTRIBUTION.md`

**Interfaces:**
- Consumes: `obra/superpowers` exact source commit pinned in `ATTRIBUTION.md`.
- Produces: an offline-copyable TeamAI skill namespace with upstream filenames preserved, including supporting files referenced by each selected core skill.

- [ ] **Step 1:** Pin the upstream commit and record MIT attribution.
- [ ] **Step 2:** Vendor the core Superpowers skill set required for design, planning, TDD, debugging, review, execution, worktrees, and verification.
- [ ] **Step 3:** Preserve upstream `SKILL.md` frontmatter and support-file references verbatim; do not fork their behavior into OpenCode-specific copies.
- [ ] **Step 4:** Run harness validation.

### Task 3: Add high-frequency Java development skills

**Files:**
- Create: `skills/java/java-feature-development/SKILL.md`
- Create: `skills/java/java-debugging/SKILL.md`
- Create: `skills/java/java-testing/SKILL.md`
- Create: `skills/java/java-refactoring/SKILL.md`
- Create: `skills/java/spring-api-development/SKILL.md`
- Create: `skills/java/database-change/SKILL.md`

**Interfaces:**
- Consumes: repository evidence and the vendored Superpowers process skills.
- Produces: Java-specific techniques that add language/framework judgment without duplicating generic Superpowers workflows.

- [ ] **Step 1:** Add each Skill with TeamAI/Agent Skills compatible `name` + trigger-only `description` frontmatter.
- [ ] **Step 2:** Make each Skill repository-first, offline-safe, Java/Spring-aware, and explicit about its required Superpowers sub-skills where applicable.
- [ ] **Step 3:** Run harness validation.

### Task 4: Add Java engineering rules

**Files:**
- Create: `rules/java/repository-first.md`
- Create: `rules/java/coding-style.md`
- Create: `rules/java/spring-boot.md`
- Create: `rules/java/testing.md`
- Create: `rules/java/database.md`
- Create: `rules/java/security.md`
- Create: `rules/java/build-and-offline.md`
- Create: `rules/java/verification.md`

**Interfaces:**
- Consumes: TeamAI recursive rules handler and OpenCode instruction-glob activation.
- Produces: concise standing constraints TeamAI can copy to `.opencode/rules/java/*` and activate via `opencode.json`.

- [ ] **Step 1:** Add rules with project-local evidence precedence and no company-specific paths/secrets.
- [ ] **Step 2:** Enforce offline build behavior, test discipline, security fundamentals, database safety, and fresh verification evidence.
- [ ] **Step 3:** Run harness validation.

### Task 5: Add canonical OpenCode reviewer agents

**Files:**
- Create: `agents/java-code-reviewer.yaml`
- Create: `agents/java-security-reviewer.yaml`
- Create: `agents/java-database-reviewer.yaml`

**Interfaces:**
- Consumes: TeamAI canonical `AgentSpec` YAML schema.
- Produces: TeamAI-renderable OpenCode subagents with `targets: [opencode]` and tool-neutral instructions.

- [ ] **Step 1:** Add required `name`, `description`, and `instructions` fields to each canonical YAML.
- [ ] **Step 2:** Set `targets: [opencode]`; do not use deprecated common `tools` or vendor-specific model names.
- [ ] **Step 3:** Run harness validation.

### Task 6: Intranet/OpenCode usage documentation and final certification

**Files:**
- Create: `README.md`
- Create: `README.zh-CN.md`
- Create: `docs/verification/2026-09-10-certification.md`

**Interfaces:**
- Consumes: all repository resources and current TeamAI/OpenCode mappings.
- Produces: copy-and-run intranet instructions plus exact verification evidence.

- [ ] **Step 1:** Document standalone team-repo usage: `teamai init <repo>`, `teamai pull`, `teamai status`, `teamai list`, and `teamai doctor`.
- [ ] **Step 2:** Explain that TeamAI generates `.opencode/*` in the business repository and manages the `opencode.json` rule instruction glob; users do not copy generated files into this harness.
- [ ] **Step 3:** Run `python -m unittest discover -s tests -v` and `python scripts/validate_harness.py` against the exact final branch state.
- [ ] **Step 4:** Record final source pins, validation output, scope, and known environment-dependent verification limits in the certification document.
