# TeamAI Java + OpenCode Harness — Portable Template Amendment

**Date:** 2026-09-10

This amendment is authoritative where it conflicts with `2026-09-10-teamai-java-opencode-harness-design.md`.

## Reason

Current TeamAI CLI `init` clones/links the Team Repo and, when that repo has no `teamai.yaml`, creates a valid default `teamai.yaml` using the actual repository URL and detected provider. The public harness is intended to be copied into an intranet repository, so committing a public `repo:` value would make the template non-portable.

## Changes

1. The distributable template MUST NOT commit a public-URL `teamai.yaml`. The internal operator copies the repository to intranet Git and runs `teamai init <INTRANET_TEAMAI_HARNESS_GIT_URL> --agent opencode` from each Java business repository. TeamAI then creates/owns the Team Repo config for that internal remote.
2. The team template still MUST NOT commit generated `.opencode/*` resources.
3. Because upstream Superpowers' native OpenCode plugin normally injects OpenCode-specific tool mappings, while this harness distributes Superpowers through TeamAI skills instead of that plugin, the harness adds `rules/opencode/superpowers-runtime.md` as the TeamAI-native compatibility layer.
4. The compatibility rule maps `superpowers:<name>` references to the flattened native TeamAI/OpenCode skill name `<name>` and maps generic tool actions to OpenCode tools.
5. Custom reviewer agents remain canonical `agents/*.yaml` with `targets: [opencode]`; no pre-rendered OpenCode agent Markdown is stored in the Team Repo.
