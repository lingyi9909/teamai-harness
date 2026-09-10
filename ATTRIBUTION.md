# Third-party attribution

## Superpowers

This repository vendors the core skills from `obra/superpowers` so the TeamAI harness can be copied into an offline or intranet environment without fetching public resources at runtime.

- Upstream: `https://github.com/obra/superpowers`
- Pinned commit: `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`
- Upstream release represented by that commit: v6.3.0
- License: MIT; preserved at `third_party/superpowers/LICENSE`
- Vendored path: `skills/superpowers/`

The vendored upstream files are kept byte-identical to the pinned Git blobs. OpenCode adaptation is implemented separately as TeamAI-native rules; the upstream Skill bodies are not rewritten for this repository.
