# TeamAI CLI Compatibility Notes

## Verification baseline

This harness was designed against the current public `Tencent/teamai-cli` main source observed on 2026-09-10 and the official `teamai-hub/template-backend` reference template.

Relevant TeamAI implementation contracts inspected:

- `src/types.ts` — `TeamaiConfigSchema` and default tool paths;
- `src/resources/skills.ts` — recursive skill discovery and `SKILL.md` frontmatter handling;
- `src/resources/rules.ts` — recursive rule sync and OpenCode instructions activation;
- `src/resources/opencode-config.ts` — exact OpenCode rules glob behavior;
- `src/resources/agents.ts` — canonical YAML agents and legacy Markdown compatibility;
- `src/resources/agent-format.ts` — `AgentSpec` and OpenCode rendering;
- `src/known-agents.ts` — OpenCode registration/detection;
- `src/opencode-hooks.ts` / hooks integration — OpenCode plugin lifecycle behavior.

## Canonical TeamAI resource layout

This repository intentionally stores:

```text
skills/java/<skill>/SKILL.md
rules/java-<rule>.md
agents/<agent>.yaml
teamai.yaml
```

It intentionally does **not** store:

```text
.opencode/skills/
.opencode/rules/
.opencode/agents/
.opencode/plugin/
opencode.json   # as a generated consumer-project file
```

Those are deployment targets in a Java business repository and are owned by TeamAI/OpenCode integration.

## Skills contract

Current TeamAI skill handling recursively discovers directories containing `SKILL.md`, so the namespace layout below is valid:

```text
skills/
└── java/
    ├── java-feature-development/SKILL.md
    ├── java-debugging/SKILL.md
    └── ...
```

Each skill in this harness explicitly provides YAML frontmatter:

```yaml
---
name: <directory-name>
description: <non-empty description>
---
```

This avoids relying on TeamAI's push-time auto-repair of missing frontmatter.

## Rules contract and OpenCode constraint

TeamAI's Rules handler recursively discovers and copies canonical Markdown rules. However, the current OpenCode activation implementation is deliberately **non-recursive**: `opencodeRulesGlob()` returns `<rules-dir>/*.md`.

For project scope that becomes:

```text
.opencode/rules/*.md
```

Therefore a canonical team rule stored at `rules/java/testing.md` would be synchronized to `.opencode/rules/java/testing.md` but would not match TeamAI's current OpenCode `instructions` glob. The file would exist yet remain inactive in OpenCode.

For that reason this OpenCode-first harness keeps all standing Java rules flat at the TeamAI rules root with collision-safe names:

```text
rules/java-repository-first.md
rules/java-coding-style.md
rules/java-spring-boot.md
rules/java-testing.md
rules/java-database.md
rules/java-security.md
rules/java-build-and-offline.md
rules/java-verification.md
```

This is intentionally different from the older backend template's nested `rules/common/` organization. The difference is required by current TeamAI → OpenCode behavior, not by a custom convention invented by this harness.

## Agent format: important difference from the older backend template

The official `teamai-hub/template-backend` reference repository still contains examples such as:

```text
agents/code-reviewer.md
agents/security-reviewer.md
agents/database-reviewer.md
```

Current TeamAI CLI source now defines the canonical format as:

```text
agents/<name>.yaml
```

with at least:

```yaml
name: ...
description: ...
instructions: ...
```

TeamAI renders this canonical spec to each target tool. For OpenCode it emits Markdown frontmatter with `mode: subagent`; the OpenCode agent name is derived from the filename. TeamAI also documents that OpenCode's old common `tools` field is deprecated in favor of OpenCode-specific `permission` settings under `tool_extras.opencode`.

Legacy `agents/*.md` remains a compatibility path but is not the correct source format for an OpenCode-first new harness. This repository therefore uses only YAML agents and explicitly sets:

```yaml
targets:
  - opencode
```

Review agents also use:

```yaml
tool_extras:
  opencode:
    permission:
      edit: deny
```

so review execution is read-only while remaining within TeamAI's documented per-tool extension mechanism.

## OpenCode tool paths

The current TeamAI default project-scope paths are:

```text
skills: .opencode/skills
rules: .opencode/rules
agents: .opencode/agents
mcpProject: opencode.json
```

OpenCode user scope uses a different prefix under `.config/opencode`, which is why this harness does not override `toolPaths` in `teamai.yaml`. Keeping official defaults allows TeamAI CLI to apply the correct scope-specific mapping.

## `teamai.yaml` strategy

The harness keeps `teamai.yaml` deliberately minimal and schema-valid:

- `team`
- `description`
- `repo`
- `provider`
- `reviewers`
- `sharing`

It does not copy TeamAI's default `toolPaths` into the repository. Duplicating the current defaults would freeze path behavior and make future TeamAI fixes harder to inherit.

When this public repository is mirrored to the company intranet, the team administrator should change the `repo` value to the internal canonical repository URL if the locally installed TeamAI CLI relies on that metadata. This is an environment-specific bootstrap edit, not a resource-layout change.

## OpenCode enablement

Current TeamAI source includes OpenCode in the known-agent registry and default `toolPaths`, and init persists requested `--agent` values into `enabledAgents`. The recommended command for a TeamAI CLI build that accepts OpenCode as an explicit agent is:

```text
teamai init <internal-teamai-repo-url> --scope project --agent opencode
```

Because CLI documentation examples may lag the source registry, environments with an older internally mirrored TeamAI build should verify accepted options with that installed version. If explicit selection is unavailable, use ordinary project-scope init with OpenCode installed/detectable and validate via `teamai status`, `teamai list`, and `teamai doctor` rather than inventing custom paths.

## Upgrade policy

When TeamAI CLI is upgraded internally:

1. inspect changes to `TeamaiConfigSchema`, resource handlers, `opencodeRulesGlob()`, and OpenCode agent rendering;
2. run `teamai pull --dry-run` against a disposable Java repository where supported;
3. run normal `teamai pull` in the disposable repository;
4. verify generated `.opencode/skills`, root-level `.opencode/rules/*.md`, `.opencode/agents`, and `opencode.json` instructions;
5. invoke each Java review agent once on a harmless test diff;
6. only then roll the new TeamAI version to production developer machines.

If a future TeamAI release changes OpenCode rules activation to a recursive glob, this harness may reintroduce nested rule namespaces after compatibility testing. Until then, keep rules flat.

Do not fork TeamAI path/layout behavior in this harness to preserve compatibility with an old internal build; prefer upgrading the mirrored CLI or pinning a documented compatible version.
