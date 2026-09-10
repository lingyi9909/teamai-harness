# TeamAI Harness for Java + OpenCode

这是一个可直接复制到公司内网 Git 仓库的 **TeamAI 团队资源模板**，面向 Java 后端研发，并以 OpenCode 为唯一必需的 Coding Agent 目标。

它不是一个 Spring Boot 示例工程，也不是另一套 Agent Runtime。它只提供 TeamAI CLI 能识别和分发的标准资源：`skills/`、`rules/`、`agents/`、`docs/`。

## 里面有什么

- `skills/superpowers/`：固定到 `obra/superpowers` commit `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` 的核心 Superpowers Skills，离线可用；许可和来源见 `ATTRIBUTION.md`。
- `skills/java/`：6 个高频 Java Skills：功能开发、调试、测试、重构、Spring API、数据库变更。
- `rules/java/`：Java/Spring/数据库/安全/测试/离线构建/验收规则。
- `rules/opencode/superpowers-runtime.md`：把 Superpowers 的通用动作映射到 OpenCode 原生工具，并解决 `superpowers:<name>` 的 Skill 引用映射。
- `agents/`：3 个 TeamAI canonical YAML reviewer：Java Code、Security、Database，全部 `targets: [opencode]`。

## 为什么仓库里没有 `teamai.yaml`

这是有意设计，不是遗漏。这个仓库要先从公网复制到你的内网 Git，再作为内网 TeamAI Team Repo 使用。如果这里写死公网 `repo:`，复制后就不再是“原样可迁移”。

TeamAI CLI 当前的标准 `init` 流程会在目标 Team Repo 没有 `teamai.yaml` 时，根据你传入的实际仓库 URL 自动创建合法配置。因此内网仓库 URL 应由 `teamai init` 决定。

同理，本模板**不提交 `.opencode/`**。TeamAI 会把技能同步到业务仓库 `.opencode/skills`，规则同步到 `.opencode/rules`，Agent 渲染到 `.opencode/agents`；对于 OpenCode 不会自动扫描 rules 的问题，TeamAI 会管理业务仓库 `opencode.json` 的 `instructions` glob。

## 内网落地

先把本仓库完整复制/镜像到你的公司内网仓库。之后不要在这个模板仓库里执行 `teamai init .`；正常用法是在一个 Java **业务代码仓库**根目录执行：

```bash
teamai init <INTRANET_TEAMAI_HARNESS_GIT_URL> --agent opencode
teamai pull
```

推荐首次同步后检查：

```bash
teamai status
teamai list --source repo
teamai list --source local
teamai doctor
```

业务仓库里应能看到 TeamAI 生成/维护的 OpenCode 资源，例如：

```text
.opencode/
├── skills/
│   ├── using-superpowers/
│   ├── test-driven-development/
│   ├── java-feature-development/
│   └── ...
├── rules/
│   ├── java/
│   └── opencode/
└── agents/
    ├── java-code-reviewer.md
    ├── java-security-reviewer.md
    └── java-database-reviewer.md
opencode.json
```

注意：TeamAI 的 Skill namespace 是 Team Repo 的组织/角色结构；同步到 OpenCode 时 Skill 会按 Skill 名进入 OpenCode skills 根目录。因此运行时引用的是 `using-superpowers`、`java-testing` 等原生 Skill 名。

## Java 约束

基线支持 Java 17+，Java 21 推荐，但**实际版本永远以业务仓库 build 文件为准**。Spring Boot 3 / Spring 6、JUnit 5、Maven/Gradle、JPA/MyBatis 等也都必须先从仓库证据确认，模板不会强行迁移技术栈。

公司内网场景下，运行阶段禁止通过公网补依赖/装工具。优先使用业务仓库自带 Maven/Gradle wrapper，以及已配置的公司内部 Maven/Gradle 镜像。如果内部镜像缺少制品，应明确报出缺失项，而不是绕过网络策略。

## 本模板自身验证

不依赖 PyPI/npm：

```bash
python -m unittest discover -s tests -v
python scripts/validate_harness.py
```

GitHub 侧也配置了同一套 contract CI，用于防止误提交 `.opencode/*`、破坏 Skill frontmatter、加入非 OpenCode Agent 或丢失关键规则。

## 更新 TeamAI / Superpowers

升级 TeamAI CLI 前先重新核对 `src/types.ts` 的 tool paths、`src/resources/skills.ts`、`src/resources/rules.ts` 和 `src/resources/agent-format.ts`，不要根据旧文档猜 schema。

升级 Superpowers 时，把 `skills/superpowers/` 整体更新到一个明确的上游 commit，并同步更新 `ATTRIBUTION.md`；不要只替换某个 `SKILL.md` 而遗漏其配套文件。
