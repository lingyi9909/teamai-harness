# TeamAI Java + OpenCode Harness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a TeamAI-compliant Java backend harness repository whose canonical skills, rules, and agents are deployed by TeamAI into OpenCode project scope and remain usable in an offline corporate network.

**Architecture:** Keep only TeamAI canonical resources in this repository. Java workflows live under `skills/java`, standing constraints under `rules/java`, and OpenCode-targeted subagents under `agents/*.yaml`; TeamAI CLI performs all rendering/synchronization into `.opencode/*` and root `opencode.json` in consumer repositories.

**Tech Stack:** TeamAI CLI current source contract, OpenCode, Markdown/YAML, Java 17+/21, Spring Boot 3.x, Maven/Gradle wrappers, JUnit 5.

**Spec:** `docs/superpowers/specs/2026-09-10-teamai-java-opencode-harness-design.md`

## Global Constraints

- TeamAI CLI current source contract has authority over stale template examples.
- Canonical agents MUST use `agents/<name>.yaml`, not legacy `agents/*.md`.
- OpenCode generated resources MUST NOT be committed into this team repository.
- Java project evidence overrides default framework/tool assumptions.
- Normal development workflows MUST NOT require public internet access.
- No secrets, internal hostnames, credentials, or company-specific registry URLs may be committed.

---

### Task 1: Team repository contract and usage docs

**Files:**
- Create: `teamai.yaml`
- Create: `README.md`
- Create: `docs/opencode-usage.md`
- Create: `docs/intranet-bootstrap.md`

**Interfaces:**
- Consumes: current TeamAI `TeamaiConfigSchema` and OpenCode default tool paths.
- Produces: a valid standalone TeamAI team repository and exact operator instructions.

- [ ] Create a minimal `teamai.yaml` containing only schema-valid fields required for this team repo; do not override official `toolPaths` defaults.
- [ ] Document project-scope initialization, pull/status/doctor verification, and OpenCode generated destinations.
- [ ] Document offline bootstrap boundary: TeamAI CLI package/repo must already be mirrored or copied into the intranet before use.
- [ ] Verify no documentation tells normal coding agents to access public registries or fetch-and-execute scripts.

### Task 2: Java standing rules

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
- Consumes: arbitrary existing Java repository structure.
- Produces: tool-neutral Markdown rules that TeamAI syncs to `.opencode/rules` and activates through `opencode.json`.

- [ ] Require repository/build/framework detection before edits.
- [ ] Define Java/Spring style without forcing a package architecture where the project already has one.
- [ ] Define unit/integration testing expectations and regression scope.
- [ ] Define transaction/query/schema safety rules.
- [ ] Define secret/input/auth/logging security rules.
- [ ] Define Maven/Gradle wrapper and intranet dependency behavior.
- [ ] Define fresh verification and evidence-before-completion requirements.

### Task 3: Java implementation skills

**Files:**
- Create: `skills/java/java-feature-development/SKILL.md`
- Create: `skills/java/java-debugging/SKILL.md`
- Create: `skills/java/java-testing/SKILL.md`
- Create: `skills/java/java-refactoring/SKILL.md`
- Create: `skills/java/spring-api-development/SKILL.md`
- Create: `skills/java/database-change/SKILL.md`

**Interfaces:**
- Consumes: user request plus repository evidence.
- Produces: repeatable OpenCode workflows with explicit triggers, steps, validation, and stop conditions.

- [ ] Give every skill valid YAML frontmatter with non-empty `name` and `description` matching the directory name.
- [ ] Make feature work repository-first and test-first where feasible.
- [ ] Make debugging evidence-first: reproduce, isolate, hypothesize, prove, fix, regress.
- [ ] Make testing select the narrowest meaningful layer before broader verification.
- [ ] Make refactoring behavior-preserving with characterization tests for risky legacy code.
- [ ] Make Spring API work detect MVC vs WebFlux and existing error/validation conventions before changes.
- [ ] Make database changes reason about transaction boundaries, indexes, locks, migration compatibility, and rollback.

### Task 4: OpenCode-targeted Java review agents

**Files:**
- Create: `agents/java-code-reviewer.yaml`
- Create: `agents/java-security-reviewer.yaml`
- Create: `agents/java-database-reviewer.yaml`

**Interfaces:**
- Consumes: TeamAI canonical `AgentSpec` schema.
- Produces: OpenCode subagents rendered by TeamAI into `.opencode/agents/*.md`.

- [ ] Each YAML must contain `name`, `description`, `instructions`, and `targets: [opencode]`.
- [ ] Do not set Claude-specific model names or common deprecated OpenCode `tools` fields.
- [ ] Code reviewer reports only actionable, evidence-backed findings and permits zero findings.
- [ ] Security reviewer focuses on Java/Spring trust boundaries and concrete exploitability.
- [ ] Database reviewer focuses on correctness, transactionality, query plans, locking, migrations, and rollback safety.

### Task 5: Compatibility documentation and final verification

**Files:**
- Create: `docs/teamai-compatibility.md`

**Interfaces:**
- Consumes: all files from Tasks 1-4 and current TeamAI source rules.
- Produces: auditable compatibility statement and copy-to-intranet checklist.

- [ ] Document the canonical-vs-generated resource mapping.
- [ ] Record why current YAML agent format supersedes the old official backend template's legacy Markdown agents.
- [ ] Verify the repository tree contains no `.opencode` generated copies.
- [ ] Re-read all `SKILL.md`, `agents/*.yaml`, `teamai.yaml`, README, and offline guidance for schema/contract consistency.
- [ ] Fetch the resulting files from `develop` and compare the final tree against this plan before declaring completion.
