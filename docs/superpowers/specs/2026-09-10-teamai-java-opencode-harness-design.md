# TeamAI Java + OpenCode Harness Design

> Status update (2026-09-11): Historical proposal. The current delivery scope is
> Code Review plus intranet/TeamAI collaboration; see
> [the current delivery plan](../../codea-harness/1.7-delivery-plan.md).
> The Java development/debug/testing skills and separate Java reviewer agents below
> are not part of this delivery. Formal review stays with the installed Codea Harness
> Reviewer and Runtime. No new Java/Spring version requirement is imposed on existing
> projects. The current repository is a mergeable resource pack for an existing team
> repo; `teamai.yaml` is supplied only as an inactive example to avoid replacing
> the intranet repository configuration.

## Goal

Build a standalone TeamAI team repository for enterprise Java backend development that can be initialized into existing business repositories and consumed by OpenCode without hand-maintaining generated `.opencode/*` files.

## Authority

This repository follows the current `Tencent/teamai-cli` source contract, with current source taking precedence over older template examples. The design was checked against TeamAI CLI main source observed on 2026-09-10 (including `src/types.ts`, `src/resources/skills.ts`, `src/resources/rules.ts`, `src/resources/agents.ts`, `src/resources/agent-format.ts`, `src/known-agents.ts`) and the official `teamai-hub/template-backend` repository.

## Core decision

This repository is a **TeamAI team harness repository**, not a sample Spring Boot application and not an OpenCode-specific generated repository.

Canonical resources live only in TeamAI source form:

- `skills/<namespace>/<skill>/SKILL.md`
- `rules/<namespace>/<rule>.md`
- `agents/<name>.yaml`
- `docs/...`
- `teamai.yaml`

TeamAI owns deployment into an application repository. For OpenCode project scope, current TeamAI CLI maps resources to:

- `.opencode/skills`
- `.opencode/rules`
- `.opencode/agents`
- project `opencode.json` for MCP and rule `instructions` activation

The harness MUST NOT commit pre-rendered `.opencode/*` copies to this team repository.

## OpenCode compatibility rules

1. OpenCode is a first-class TeamAI target in current `toolPaths`.
2. OpenCode does not auto-scan a rules directory. TeamAI's Rules handler activates/deactivates the TeamAI rule glob in root `opencode.json`; users must not manually duplicate this behavior.
3. Canonical TeamAI agents use `agents/<name>.yaml`. Current TeamAI CLI renders them to OpenCode Markdown agents and defaults `mode: subagent`.
4. OpenCode's deprecated common `tools` field is not relied on. OpenCode-specific permission settings, when needed, belong under `tool_extras.opencode` in canonical agent YAML.
5. Java review agents are targeted to `opencode` so they cannot accidentally depend on Claude-only model/tool semantics.

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

`rules/java/` contains always-applicable or broadly applicable constraints:

- `repository-first.md`
- `coding-style.md`
- `spring-boot.md`
- `testing.md`
- `database.md`
- `security.md`
- `build-and-offline.md`
- `verification.md`

Rules are intentionally independent of one company's package names or internal infrastructure.

### Agents

Canonical TeamAI YAML agents:

- `java-code-reviewer.yaml`
- `java-security-reviewer.yaml`
- `java-database-reviewer.yaml`

All three target OpenCode and use tool-neutral instructions. No Anthropic-specific model name is set.

## Offline/intranet model

The business repository must be usable after the TeamAI CLI package and this team repository are available inside the intranet.

The harness itself MUST NOT instruct OpenCode to fetch remote dependencies, run `curl | sh`, use `npx` as an implicit downloader, or clone public repositories during normal coding workflows.

Build/test commands must prefer repository-local wrappers (`mvnw.cmd`, `gradlew.bat`) on Windows and existing internal Maven/Gradle mirrors. If a dependency is unavailable internally, the agent must report the dependency gap instead of silently switching to a public registry.

TeamAI installation itself is an environment/bootstrap concern and is documented separately from normal agent workflows.

## Usage model

For an existing Java business repository:

1. Install an intranet-approved TeamAI CLI package/version.
2. `cd` to the Java project root.
3. Run project-scope `teamai init <team-repo-url>`.
4. Ensure OpenCode is installed/detectable for the project, then run `teamai pull`.
5. Verify with `teamai status`, `teamai list --source repo`, `teamai list --source local`, and `teamai doctor`.
6. OpenCode consumes generated `.opencode/skills`, `.opencode/rules`, `.opencode/agents`, with rules activated by TeamAI-managed `opencode.json` instructions.

Because TeamAI CLI's published documentation has evolved and some self-repo `--agent` examples lag the broader known-agent registry, this harness documents both the safe auto-detection path and an optional explicit OpenCode enablement path only when the installed CLI reports `opencode` as a valid `--agent` target.

## Non-goals

- No Spring Boot demo application
- No custom TeamAI CLI fork
- No custom OpenCode plugin implementation
- No public-network bootstrap inside normal project workflows
- No company-specific secrets, registry URLs, database credentials, or internal hostnames
- No duplicate `.opencode/*` generated resources committed to this team repository

## Acceptance criteria

1. Repository layout is parseable by current TeamAI resource handlers.
2. Every `SKILL.md` has non-empty `name` and `description` frontmatter.
3. Every canonical agent YAML has non-empty `name`, `description`, and `instructions`, and `targets: [opencode]`.
4. No legacy `agents/*.md` is used.
5. `teamai.yaml` conforms to the current TeamAI config schema and keeps official OpenCode default paths rather than overriding them unnecessarily.
6. README contains exact standalone-team-repo usage for a Java project and explains generated OpenCode paths.
7. Offline guidance never assumes public internet access during normal Java development.
