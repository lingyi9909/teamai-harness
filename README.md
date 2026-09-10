# TeamAI Harness for Java + OpenCode

A portable TeamAI team-resource template for enterprise Java development with OpenCode as the required coding-agent target.

This repository intentionally contains TeamAI canonical resources (`skills/`, `rules/`, `agents/`, `docs/`) rather than generated `.opencode/*` artifacts or a sample Spring application.

## Included

- Vendored Superpowers core skills pinned to `obra/superpowers` commit `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` (MIT; see `ATTRIBUTION.md`).
- Six focused Java skills for feature work, debugging, testing, refactoring, Spring APIs, and database changes.
- Standing Java engineering rules for repository-first work, style, Spring, testing, database safety, security, offline builds, and verification.
- A TeamAI-native OpenCode runtime rule that maps generic Superpowers actions to OpenCode tools and resolves `superpowers:<name>` to native TeamAI-synced skill `<name>`.
- Three canonical TeamAI YAML reviewers targeting only OpenCode.

## Portable intranet setup

`teamai.yaml` is intentionally absent from this public template. After you copy/mirror the repository into your intranet Git service, TeamAI should create the config from the actual intranet remote during initialization instead of retaining a public URL.

From the root of a Java business repository:

```bash
teamai init <INTRANET_TEAMAI_HARNESS_GIT_URL> --agent opencode
teamai pull
teamai status
teamai list --source repo
teamai list --source local
teamai doctor
```

TeamAI then owns synchronization into `.opencode/skills`, `.opencode/rules`, `.opencode/agents`, and OpenCode rule activation through the business repository's `opencode.json`. Do not copy generated `.opencode/*` files back into this team template.

## Offline policy

Normal development must not depend on the public network. Use repository-local Maven/Gradle wrappers and configured internal mirrors/caches. Missing intranet artifacts are reported as verification gaps; public repositories are not added as a workaround.

## Validate this template

```bash
python -m unittest discover -s tests -v
python scripts/validate_harness.py
```

See `README.zh-CN.md` for the detailed Chinese usage guide.
