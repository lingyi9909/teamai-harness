# TeamAI Java Harness

A deliberately small TeamAI repository for Java development with OpenCode.

It contains only:

1. the upstream **Superpowers v6.3.0** skill set from `obra/superpowers`;
2. five lightweight Java standing rules for coding style, Spring, testing, security, and offline Windows builds.

It intentionally does **not** contain custom Java workflow skills, custom review agents, generated `.opencode/` files, or a public `teamai.yaml`.

## Superpowers

Source: `https://github.com/obra/superpowers`

Pinned release: **v6.3.0**
Pinned commit: `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`

The complete upstream `skills/` directory is vendored unchanged, including:

- `brainstorming`
- `dispatching-parallel-agents`
- `executing-plans`
- `finishing-a-development-branch`
- `receiving-code-review`
- `requesting-code-review`
- `subagent-driven-development`
- `systematic-debugging`
- `test-driven-development`
- `using-git-worktrees`
- `using-superpowers`
- `verification-before-completion`
- `writing-plans`
- `writing-skills`

Upstream license and version provenance are retained under `third_party/superpowers/`.

Note: the upstream Superpowers `brainstorming` skill includes an optional Visual Companion. That feature uses its bundled shell/Node scripts. On Windows it expects a compatible shell such as Git Bash plus Node.js. The ordinary skills do not require the Visual Companion to be used for every task.

## Java rules

TeamAI distributes these flat files as standing rules:

- `rules/java-coding-style.md`
- `rules/java-spring.md`
- `rules/java-testing.md`
- `rules/java-security.md`
- `rules/java-build-offline.md`

Repository-local conventions always win over generic rules. The rules do not force a Java/Spring upgrade and do not assume public Internet access.

## Internal-network setup

Copy the contents of this repository into an empty internal Git repository. Keep the public template's lack of `teamai.yaml`; the internal repository should own its actual TeamAI configuration.

From a Java project that should consume the team harness:

```text
teamai init <internal-teamai-repo-url> --scope project --agent opencode
teamai pull
teamai status
teamai list --source local --agent opencode --verbose
teamai doctor
```

With current TeamAI/OpenCode mappings, skills are installed under `.opencode/skills/` and rules under `.opencode/rules/`. The Java rule files are intentionally flat because TeamAI's current OpenCode rule instruction glob is non-recursive.

TeamAI CLI, OpenCode, JDKs, Maven/Gradle artifacts, and any other runtime dependencies must be installed or mirrored inside the company network separately.

## Updating Superpowers

Upgrades should be deliberate. When moving to a newer Superpowers release:

1. review the upstream release notes and license;
2. replace the vendored `skills/` directory from the chosen tag;
3. update `third_party/superpowers/VERSION`;
4. verify the copied `skills/` directory matches that upstream tag;
5. run a real `teamai pull` + OpenCode smoke test in the internal environment.
