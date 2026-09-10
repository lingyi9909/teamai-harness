# TeamAI Java Harness

A deliberately small TeamAI repository for Java development with OpenCode.

It contains:

1. the upstream **Superpowers v6.3.0** skill set from `obra/superpowers`;
2. four focused engineering skills for codebase reconnaissance, Java build diagnostics, database/SQL analysis, and security review;
3. five lightweight Java standing rules for coding style, Spring, testing, security, and offline Windows builds.

It intentionally does **not** contain custom review agents, generated `.opencode/` files, or a public `teamai.yaml`.

## Skills

### Superpowers v6.3.0

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

Note: the upstream Superpowers `brainstorming` skill includes an optional Visual Companion. That feature uses its bundled shell/Node scripts. On Windows it expects a compatible shell such as Git Bash plus Node.js. Ordinary skill use does not require the Visual Companion.

### Focused engineering skills

Four additional skills complement Superpowers instead of duplicating its general workflow capabilities:

- `codebase-reconnaissance` — task-scoped understanding of an unfamiliar repository, relevant modules, call/data flow, tests, and constraints before editing.
- `java-build-diagnostics` — Java/JDK/Maven/Gradle/classpath/annotation-processing/Spring Boot startup diagnostics with Windows and offline-enterprise constraints.
- `database-sql-analysis` — SQL plus MyBatis/MyBatis-Plus/JPA/Hibernate/JDBC correctness, injection, transactions, locking, indexes, pagination, batching, and performance analysis.
- `security-review` — evidence-backed Java/Spring security review focused on trust boundaries, authorization, injection, SSRF/files/deserialization, secrets, crypto, business logic, and locally verified dependency risk.

`codebase-reconnaissance`, `database-sql-analysis`, and `security-review` are lightweight adaptations inspired by the MIT-licensed `github/awesome-copilot` skills pinned at commit `7568a482ce2df38f8965ab5336a3220db796a4ba`. Their provenance and license are retained under `third_party/github-awesome-copilot/`.

`java-build-diagnostics` is maintained by this harness because the public skill ecosystem does not provide an equivalent fit for the Java + Windows-native + offline enterprise environment targeted here.

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

## Upgrade policy

Keep the harness small and upgrades deliberate:

- update Superpowers only after reviewing the upstream release and re-verifying the vendored `skills/` tree;
- review upstream changes before refreshing any `awesome-copilot`-derived skill;
- do not add generic skills that substantially overlap Superpowers or the existing four focused skills;
- run a real `teamai pull` + OpenCode smoke test in the internal environment after material skill changes.
