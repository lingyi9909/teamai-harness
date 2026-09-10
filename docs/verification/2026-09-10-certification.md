# TeamAI Java + OpenCode Harness Certification

**Date:** 2026-09-10

## Source authority

This implementation was checked against Tencent TeamAI CLI current `main` at:

- Commit: `9e7adc79faa03ef4c3a49cb7a148bba83b7dc1f3`
- Package version at that commit: `0.22.0`

Relevant source contracts inspected include TeamAI's known-agent/tool paths, skill synchronization, recursive rule synchronization and OpenCode rule activation, canonical agent YAML rendering, and `teamai init` behavior for a Team Repo that does not yet contain `teamai.yaml`.

The public template intentionally does not commit a public-URL `teamai.yaml`: after this repository is copied/mirrored into an intranet Git service, `teamai init <INTRANET_TEAMAI_HARNESS_GIT_URL> --agent opencode` is the authority that binds TeamAI to the actual internal remote.

## Superpowers authority

Vendored upstream:

- Repository: `obra/superpowers`
- Pinned commit: `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`
- Upstream release represented by the pin: `v6.3.0`
- License: MIT (`third_party/superpowers/LICENSE`)

Core Skill files and their referenced support files are stored under `skills/superpowers/`. The upstream Skill bodies are not rewritten for OpenCode. OpenCode compatibility is isolated in the TeamAI rule `rules/opencode/superpowers-runtime.md`.

## Delivered scope

- Core high-frequency Superpowers workflow Skills for brainstorming/design, planning/execution, TDD, debugging, code review, worktrees, and completion verification.
- Six focused Java Skills: feature development, debugging, testing, refactoring, Spring API development, and database change.
- Eight Java standing rules: repository-first, coding style, Spring Boot, testing, database, security, offline build, and verification.
- TeamAI-native OpenCode Superpowers runtime/tool mapping.
- Three canonical TeamAI reviewer agents targeting only OpenCode: code, security, and database review.
- Standard-library-only validation tests and validator plus repository CI.
- Chinese and English usage documentation for intranet deployment.

## TDD evidence

### RED

Contract tests were committed before the Java/OpenCode resources existed:

- Commit: `e6e7e583984989405fb47ec22c6e5485f5cd7605`
- GitHub Actions run: `34475203646`
- Conclusion: `failure`

The failure was expected because required Java Skills, rules, and agents had not yet been implemented.

### GREEN

Implementation commit:

- Commit: `01b84dedcb8de4b83264bbe44e85940d0ab08959`
- GitHub Actions run: `34475601549`
- Job: `contract`
- Conclusion: `success`
- `Run harness contract tests`: `success`
- `Run standalone validator`: `success`

The contract covers required Java Skills and Skill frontmatter, required Superpowers pin/license, Java rules, OpenCode runtime mapping, canonical OpenCode-only agent YAML, prohibition of committed generated `.opencode` artifacts, public-template URL pinning, and offline-build requirements.

## Boundaries and remaining environment evidence

This certification proves the repository structure and policies against the inspected TeamAI/OpenCode source contracts and proves the repository's automated contract on GitHub Actions.

It does **not** claim execution inside the user's actual corporate intranet, because that environment is not accessible from this session. The final internal acceptance step is therefore environment-specific: copy/mirror this repository to the internal Git service, run `teamai init <INTRANET_TEAMAI_HARNESS_GIT_URL> --agent opencode` from a representative Java business repository, run `teamai pull`, and verify TeamAI renders/synchronizes the resources into the installed OpenCode environment without public network access.

No generated `.opencode/*` tree belongs in this Team Repo; those files are owned by TeamAI synchronization in each business repository.
