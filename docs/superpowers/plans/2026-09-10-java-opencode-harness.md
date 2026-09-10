# TeamAI Java + OpenCode Harness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for completed work.

**Goal:** Deliver a standalone TeamAI team repository that can be copied into an intranet and initialized into Java business repositories using OpenCode.

**Architecture:** Keep TeamAI source resources canonical in this repository and let TeamAI CLI render/sync them into OpenCode. Vendor the current upstream Superpowers skills under their own namespace, add a small Java-specific skill/rule layer, and define OpenCode-targeted TeamAI agent YAML rather than committing generated `.opencode/*` artifacts.

**Tech Stack:** TeamAI CLI 0.22.x source contract, OpenCode, Markdown/YAML, Java 17+/21, Spring Boot 3.x, Maven/Gradle, JUnit 5.

**Spec:** `docs/superpowers/specs/2026-09-10-teamai-java-opencode-harness-design.md`

**Authority amendment:** `docs/superpowers/specs/2026-09-10-teamai-portable-template-amendment.md` overrides the original plan/design where portability requires the distributable template to omit `teamai.yaml`. TeamAI creates that config from the actual intranet remote during `teamai init`.

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
- Intentionally omit from distributable template: `teamai.yaml` (see portability amendment)
- Create: `scripts/validate_harness.py`
- Create: `tests/test_harness.py`

**Interfaces:**
- Consumes: TeamAI canonical Skill and Agent formats plus portable `teamai init` behavior.
- Produces: a repository-level validation command `python scripts/validate_harness.py` and tests that fail when required resources or OpenCode constraints are broken.

- [x] **Step 1:** Add failing tests for Skill frontmatter, canonical agent YAML, OpenCode-only agent targets, generated-artifact prohibition, portable config behavior, and public-network-command prohibition.
- [x] **Step 2:** Run the contract before implementation and confirm RED because implementation resources are missing (`e6e7e583...`, Actions `34475203646`).
- [x] **Step 3:** Add the standalone validator and portable-template contract; omit public `teamai.yaml` per the authority amendment.
- [x] **Step 4:** Re-run tests and keep them green as later tasks add resources.

### Task 2: Vendor current Superpowers core skills

**Files:**
- Create: `skills/superpowers/<skill>/...`
- Create: `third_party/superpowers/LICENSE`
- Create: `ATTRIBUTION.md`

**Interfaces:**
- Consumes: `obra/superpowers` exact source commit pinned in `ATTRIBUTION.md`.
- Produces: an offline-copyable TeamAI skill namespace with upstream filenames preserved, including supporting files referenced by each selected core skill.

- [x] **Step 1:** Pin upstream commit `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` and record MIT attribution.
- [x] **Step 2:** Vendor the core Superpowers skill set required for design, planning, TDD, debugging, review, execution, worktrees, and verification.
- [x] **Step 3:** Preserve upstream `SKILL.md` and supporting Git blobs rather than forking them into OpenCode-specific copies.
- [x] **Step 4:** Run harness validation.

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

- [x] **Step 1:** Add each Skill with TeamAI/Agent Skills compatible `name` + trigger-only `description` frontmatter.
- [x] **Step 2:** Make each Skill repository-first, offline-safe, Java/Spring-aware, and explicit about its required Superpowers sub-skills where applicable.
- [x] **Step 3:** Run harness validation.

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
- Create: `rules/opencode/superpowers-runtime.md`

**Interfaces:**
- Consumes: TeamAI recursive rules handler and OpenCode instruction-glob activation.
- Produces: concise standing constraints TeamAI can copy to `.opencode/rules/**` and activate via `opencode.json`.

- [x] **Step 1:** Add rules with project-local evidence precedence and no company-specific paths/secrets.
- [x] **Step 2:** Enforce offline build behavior, test discipline, security fundamentals, database safety, fresh verification evidence, and TeamAI-native Superpowers→OpenCode tool mapping.
- [x] **Step 3:** Run harness validation.

### Task 5: Add canonical OpenCode reviewer agents

**Files:**
- Create: `agents/java-code-reviewer.yaml`
- Create: `agents/java-security-reviewer.yaml`
- Create: `agents/java-database-reviewer.yaml`

**Interfaces:**
- Consumes: TeamAI canonical `AgentSpec` YAML schema.
- Produces: TeamAI-renderable OpenCode subagents with `targets: [opencode]` and tool-neutral instructions.

- [x] **Step 1:** Add required `name`, `description`, and `instructions` fields to each canonical YAML.
- [x] **Step 2:** Set `targets: [opencode]`; do not use deprecated common `tools` or vendor-specific model names.
- [x] **Step 3:** Run harness validation.

### Task 6: Intranet/OpenCode usage documentation and final certification

**Files:**
- Create: `README.md`
- Create: `README.zh-CN.md`
- Create: `docs/verification/2026-09-10-certification.md`

**Interfaces:**
- Consumes: all repository resources and current TeamAI/OpenCode mappings.
- Produces: copy-and-run intranet instructions plus exact verification evidence.

- [x] **Step 1:** Document standalone team-repo usage with current CLI syntax: `teamai init <repo> --agent opencode`, `teamai pull`, `teamai status`, `teamai list --source ...`, and `teamai doctor`.
- [x] **Step 2:** Explain that TeamAI generates `.opencode/*` in the business repository and manages the `opencode.json` rule instruction glob; users do not copy generated files into this harness.
- [x] **Step 3:** Run `python -m unittest discover -s tests -v` and `python scripts/validate_harness.py` through repository CI against the exact final branch state.
- [x] **Step 4:** Record source pins, RED/GREEN validation evidence, scope, and the remaining corporate-intranet environment verification boundary in the certification document.
