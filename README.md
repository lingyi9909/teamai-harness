# TeamAI Java + OpenCode Harness

面向企业 Java 后端项目的 TeamAI 团队 Harness，重点适配 **OpenCode**。

这个仓库不是 Java 示例工程，也不是 `.opencode/` 生成目录。它保存 TeamAI 的 canonical 团队资源：

```text
teamai-harness/
├── teamai.yaml
├── skills/
│   └── java/
├── rules/
│   ├── java-repository-first.md
│   ├── java-coding-style.md
│   └── java-*.md
├── agents/
├── docs/
└── docs/superpowers/
```

当业务项目执行 `teamai init` / `teamai pull` 后，TeamAI CLI 再把这些资源转换并同步到业务仓库的 OpenCode 目录。

> **OpenCode 兼容性要求：** 当前 TeamAI CLI 为 OpenCode 写入的 rules `instructions` glob 是 `.opencode/rules/*.md`，不是递归 glob。因此本仓的 Java Rules 必须直接位于 `rules/` 根目录，不能像旧模板那样放在 `rules/common/` 或 `rules/java/` 子目录。Skills 不受这个限制，TeamAI 会递归发现 `skills/java/<skill>/SKILL.md`。

## 适用场景

- 公司内网无法访问公网；
- Java/Spring Boot 后端研发；
- AI 编程工具以 OpenCode 为主；
- 希望多个业务仓统一复用编码规范、开发流程、测试方法和 review agent；
- TeamAI CLI 和本仓库可以提前镜像/复制进内网。

## 技术基线

默认参考：

- Java 17+；新项目推荐 Java 21；
- Spring Boot 3.x / Spring Framework 6.x；
- Maven Wrapper 优先，Gradle Wrapper 兼容；
- JUnit 5；
- Mockito 按边界使用；
- MyBatis / MyBatis-Plus / JPA / Hibernate / JDBC 均可。

**已有项目自身配置永远优先。** OpenCode 必须先读取 `pom.xml`、`build.gradle*`、wrapper、父 POM/BOM、源码布局、现有测试和项目规则，再决定具体实现方式，不得为了套模板擅自重构项目。

## 推荐接入方式：独立 TeamAI 团队仓

你在内网可以把本仓库完整复制到一个内部 Git 仓库，例如：

```text
<internal-teamai-repo-url>
```

然后在任意已有 Java 项目根目录执行：

```bash
teamai init <internal-teamai-repo-url> --scope project --agent opencode
teamai pull
```

如果当前安装的 TeamAI CLI 对 `--agent` 参数行为有版本差异，可先执行：

```bash
teamai init <internal-teamai-repo-url> --scope project
teamai pull
```

并通过 `teamai status`、`teamai list --source local` 和 `teamai doctor` 确认 OpenCode 被识别。当前 TeamAI CLI 源码已经包含 `opencode` 的 toolPaths、skills、rules、agents 和 hook/plugin 支持。

## OpenCode 最终会看到什么

TeamAI 当前 project-scope 默认映射：

```text
<your-java-project>/
├── .teamai/                  # TeamAI 本机项目配置/团队仓副本
├── .opencode/
│   ├── skills/               # TeamAI 下发的 Java skills
│   ├── rules/                # TeamAI 下发的 Java rules
│   ├── agents/               # TeamAI 渲染后的 Java review subagents
│   └── plugin/               # TeamAI OpenCode lifecycle plugin（由 CLI 管理）
├── opencode.json             # TeamAI 合并/维护 rules instructions、MCP 等
├── pom.xml / build.gradle...
└── src/
```

OpenCode **不会自动扫描 `.opencode/rules/`**。TeamAI CLI 会负责把 TeamAI rule glob 加入项目根目录 `opencode.json` 的 `instructions`。当前 TeamAI 使用的是直接子文件 `*.md` glob，所以本仓的 rules 已全部扁平放在 `rules/` 根目录。不要手工复制 rules 后期待自动生效，也不要在本团队仓提交生成后的 `.opencode/*`。

## 仓库包含的 Java 能力

### Skills

- `java-feature-development`：从需求到验证的 Java 功能开发流程；
- `java-debugging`：复现、证据收集、根因定位、最小修复；
- `java-testing`：JUnit 5 单测/集成测试分层策略；
- `java-refactoring`：行为保持式重构；
- `spring-api-development`：Spring MVC/WebFlux API 开发与修改；
- `database-change`：数据库 schema/query/transaction 变更流程。

### Rules

覆盖 repository-first、Java 编码风格、Spring Boot、测试、数据库、安全、内网构建、最终验证。文件均采用 `rules/java-*.md` 根级布局，以匹配当前 TeamAI → OpenCode 的非递归 rules glob。

### OpenCode Agents

- `java-code-reviewer`
- `java-security-reviewer`
- `java-database-reviewer`

团队仓中的 agent 使用 TeamAI 当前 canonical `agents/*.yaml` 格式；`teamai pull` 会为 OpenCode 渲染成 `.opencode/agents/*.md`。

## 日常使用

同步团队更新：

```bash
teamai pull
```

检查状态：

```bash
teamai status
teamai list --source repo
teamai list --source local
teamai doctor
```

查看某个 skill：

```bash
teamai skill show java-feature-development
```

## 内网要求

正常 Java 开发阶段不得假设能访问公网：

- 优先使用 `mvnw.cmd` / `gradlew.bat`（Windows）和仓库已有 wrapper；
- 依赖只能来自公司已配置的 Maven/Gradle 内部镜像或本地缓存；
- 不使用 `curl | sh`、在线安装脚本、隐式下载式 `npx`、公网 `git clone` 作为正常开发步骤；
- 如果依赖在内网不存在，明确报告缺口，不得偷偷切换到公网源。

首次把 TeamAI CLI 和本仓库带入内网属于 bootstrap 阶段，详见 [`docs/intranet-bootstrap.md`](docs/intranet-bootstrap.md)。

## 兼容性说明

本仓以 **TeamAI CLI 当前源码契约** 为准。官方 `teamai-hub/template-backend` 是本项目的结构参考，但其中 `agents/*.md` 属于旧兼容格式，且其嵌套 `rules/common/` 布局不能直接满足当前 TeamAI → OpenCode 的非递归 rules activation。当前 TeamAI CLI 的 canonical agent 新格式是 `agents/<name>.yaml`，本仓按当前源码做了 OpenCode 专化。

详见 [`docs/teamai-compatibility.md`](docs/teamai-compatibility.md)。
