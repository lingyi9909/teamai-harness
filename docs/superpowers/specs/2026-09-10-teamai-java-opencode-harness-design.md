# TeamAI Java + OpenCode Harness Design

## Goal

Build a portable TeamAI team-repository template for enterprise Java backend development that can be copied unchanged into an intranet Git repository, initialized by TeamAI against that real internal repository, and consumed by OpenCode without hand-maintaining generated `.opencode/*` files.

## Authority

This repository follows the current `Tencent/teamai-cli` source contract, with current source taking precedence over older template examples. The design was checked against TeamAI CLI main source observed on 2026-09-10 (including `src/types.ts`, `src/init.ts`, `src/resources/skills.ts`, `src/resources/rules.ts`, `src/resources/opencode-config.ts`, `src/resources/agents.ts`, `src/resources/agent-format.ts`, `src/known-agents.ts`) and the official `teamai-hub/template-backend` repository.

## Core decision

This repository is a **portable TeamAI team harness template**, not a sample Spring Boot application, not an already-initialized team repository, and not an OpenCode-generated repository.

Portable canonical resources live in TeamAI source form:

- `skills/<namespace>/<skill>/SKILL.md`
- OpenCode-active standing rules as root-level `rules/<name>.md`
- `agents/<name>.yaml`
- `docs/...`
- `README.md`

The public template intentionally omits `teamai.yaml`. Current TeamAI `init` creates it when the actual team repository lacks one and fills its repository/provider identity from the repository being initialized. This keeps a copy moved into an intranet Git service from retaining the public GitHub repository identity.

After the internal repository has been initialized once, its generated `teamai.yaml` becomes internal-team-owned configuration and must not be overwritten by future template refreshes.

TeamAI owns deployment into an application repository. For OpenCode project scope, current TeamAI CLI maps resources to:

- `.opencode/skills`
- `.opencode/rules`
- `.opencode/agents`
- project `opencode.json` for MCP and rule `instructions` activation

The harness MUST NOT commit pre-rendered `.opencode/*` copies to this template repository.

## OpenCode compatibility rules

1. OpenCode is a first-class TeamAI target in current `toolPaths`.
2. OpenCode does not auto-scan a rules directory. TeamAI's Rules handler activates/deactivates the TeamAI rule glob in root `opencode.json`; users must not manually duplicate this behavior.
3. Current TeamAI `opencodeRulesGlob()` emits `.opencode/rules/*.md` in project scope, not a recursive `**/*.md` glob. Therefore OpenCode-active rules in this harness MUST be flat at the TeamAI `rules/` root. Nested `rules/java/*.md` would be copied but not activated.
4. Canonical TeamAI agents use `agents/<name>.yaml`. Current TeamAI CLI renders them to OpenCode Markdown agents and defaults `mode: subagent`.
5. OpenCode's deprecated common `tools` field is not relied on. OpenCode-specific permission settings, when needed, belong under `tool_extras.opencode` in canonical agent YAML.
6. Java review agents are targeted to `opencode` so they cannot accidentally depend on Claude-only model/tool semantics.
7. The template itself MUST NOT hard-code an external `teamai.yaml` `repo` or `provider`; the actual internal team repository is responsible for those values after initialization.

## Java baseline

The harness is framework-aware but does not force a single application skeleton.

Primary baseline:

- Java 17+; Java 21 recommended for new services
- Spring Boot 3.x / Spring Framework 6.x when Spring is present
- Maven Wrapper preferred when available; Gradle Wrapper supported when detected
- JUnit 5
- Mockito only where a real boundary needs isolation
- Spring Boot Test/Testcontainers only when integration behavior requires them
- Jakarta namespace for Spring Boot 3+
- MyBatis, MyBatis-Plus, JPA/Hibernate, JDBC all supported by repository-detection rules rather than hard-coded assumptions

Project-local evidence always overrides these defaults: `pom.xml`, `build.gradle*`, wrapper files, parent POM/BOM, existing package structure, tests, repository conventions, and local instructions are authoritative.

## Resource set

### Skills

`skills/java/` contains task workflows, not passive style guidance:

- `java-feature-development`: repository-first feature implementation workflow
- `java-debugging`: evidence-first bug diagnosis for Java/Spring services
- `java-testing`: JUnit 5 testing strategy and test-level selection
- `java-refactoring`: behavior-preserving refactoring workflow
- `spring-api-development`: Spring MVC/WebFlux API change workflow with explicit stack detection
- `database-change`: schema/query/transaction change workflow

Each skill has valid TeamAI/OpenCode-compatible `SKILL.md` frontmatter with explicit `name` and `description`.

### Rules

OpenCode-active standing rules are deliberately flat at `rules/` because current TeamAI OpenCode activation uses a non-recursive glob:

- `rules/java-repository-first.md`
- `rules/java-coding-style.md`
- `rules/java-spring-boot.md`
- `rules/java-testing.md`
- `rules/java-database.md`
- `rules/java-security.md`
- `rules/java-build-and-offline.md`
- `rules/java-verification.md`

The `java-` prefix provides namespace-like collision avoidance while keeping every rule matched by `.opencode/rules/*.md` after TeamAI sync.

Rules are intentionally independent of one company's package names or internal infrastructure.

### Agents

Canonical TeamAI YAML agents:

- `java-code-reviewer.yaml`
- `java-security-reviewer.yaml`
- `java-database-reviewer.yaml`

All three target OpenCode and use tool-neutral instructions. No Anthropic-specific model name is set. Review agents use `tool_extras.opencode.permission.edit: deny` so review stays read-only.

## Offline/intranet model

The business repository must be usable after the TeamAI CLI package and this template repository are available inside the intranet.

The harness itself MUST NOT instruct OpenCode to fetch remote dependencies, run `curl | sh`, use `npx` as an implicit downloader, or clone public repositories during normal coding workflows.

Build/test commands must prefer repository-local wrappers (`mvnw.cmd`, `gradlew.bat`) on Windows and existing internal Maven/Gradle mirrors. If a dependency is unavailable internally, the agent must report the dependency gap instead of silently switching to a public registry.

TeamAI installation itself is an environment/bootstrap concern and is documented separately from normal agent workflows.

## Usage model

For first-time intranet setup:

1. Copy this template unchanged into an empty internal Git team repository.
2. Do not add a public-template `teamai.yaml`.
3. From a Java project on a machine that can reach the internal Git service, run `teamai init <internal-team-repo-url> --scope project --agent opencode` when the installed TeamAI build accepts explicit OpenCode selection; otherwise use normal project-scope init and verify detection.
4. Current TeamAI creates the missing team repository `teamai.yaml` using the actual repository/provider identity.
5. Run `teamai pull` and verify with `teamai status`, `teamai list --source repo`, `teamai list --source local`, and `teamai doctor`.
6. OpenCode consumes generated `.opencode/skills`, root-level `.opencode/rules/*.md`, `.opencode/agents`, with rules activated by TeamAI-managed `opencode.json` instructions.
7. Future template updates must not overwrite the internal repository's initialized `teamai.yaml`.

Because TeamAI CLI's published documentation has evolved and some self-repo agent-choice examples lag the broader known-agent registry, this harness documents both the safe auto-detection path and explicit OpenCode enablement for builds that accept `--agent opencode`.

## Non-goals

- No Spring Boot demo application
- No custom TeamAI CLI fork
- No custom OpenCode plugin implementation
- No public-network bootstrap inside normal project workflows
- No company-specific secrets, registry URLs, database credentials, or internal hostnames
- No public-repository-specific `teamai.yaml`
- No duplicate `.opencode/*` generated resources committed to this template repository

## Acceptance criteria

1. Portable repository layout is accepted by current TeamAI resource handlers after TeamAI initialization.
2. The public template contains no `teamai.yaml`; current TeamAI can create the actual internal team's configuration from the internal repo URL/provider.
3. Every `SKILL.md` has non-empty `name` and `description` frontmatter.
4. Every canonical agent YAML has non-empty `name`, `description`, and `instructions`, and `targets: [opencode]`.
5. No legacy `agents/*.md` is used.
6. All OpenCode-active Java rules are direct files under `rules/`, so current TeamAI `.opencode/rules/*.md` activation matches them.
7. README contains exact template-copy, initialization, OpenCode generation, and internal-config preservation instructions.
8. Offline guidance never assumes public internet access during normal Java development.
