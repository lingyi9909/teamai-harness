# OpenCode 使用说明

## 1. TeamAI 与 OpenCode 的职责边界

本仓库只维护 TeamAI canonical 资源。不要把 `.opencode/skills`、`.opencode/rules`、`.opencode/agents` 当作源数据提交到本仓。

TeamAI CLI 当前默认 project-scope OpenCode 路径为：

```text
skills  -> .opencode/skills
rules   -> .opencode/rules
agents  -> .opencode/agents
MCP     -> opencode.json
```

OpenCode 不会自动扫描 rules 目录，所以 TeamAI 会在 `teamai pull` 时维护项目根目录 `opencode.json` 的 `instructions`。当前 TeamAI 生成的是 `.opencode/rules/*.md` 非递归 glob，因此本 Harness 的 Java rules 全部直接存放在 TeamAI `rules/` 根目录并使用 `java-` 前缀；不要把 OpenCode 需要生效的规则放进 `rules/java/` 等子目录。

## 2. 在 Java 项目中接入

进入业务 Java 项目根目录：

```bash
teamai init <internal-teamai-repo-url> --scope project --agent opencode
teamai pull
```

然后验证：

```bash
teamai status
teamai list --source repo
teamai list --source local --agent opencode --verbose
teamai doctor
```

如果你所在内网安装的 TeamAI CLI 版本没有接受 `--agent opencode`，不要改本仓的目录结构来绕过。使用普通 project-scope 初始化，让 TeamAI 根据已安装工具进行识别：

```bash
teamai init <internal-teamai-repo-url> --scope project
teamai pull
```

再用 `teamai doctor` 查看实际识别结果。升级 TeamAI CLI 应优先于手工复制生成目录。

## 3. OpenCode 中如何使用 Skills

TeamAI pull 后，Java skills 会出现在 `.opencode/skills/<skill-name>/SKILL.md`。

推荐按照任务触发，而不是每次把全部技能强行塞入上下文：

- 新功能：`java-feature-development`
- Java/Spring 故障：`java-debugging`
- 测试补齐或测试设计：`java-testing`
- 重构：`java-refactoring`
- Spring HTTP API：`spring-api-development`
- 数据库变更：`database-change`

Skill 的第一步普遍要求读取当前仓库事实，避免把通用模板误当成项目现实。

## 4. OpenCode 中如何使用 Agents

TeamAI 团队仓使用 `agents/*.yaml` 保存 canonical agent。TeamAI 会渲染成 OpenCode native Markdown，并放到：

```text
.opencode/agents/java-code-reviewer.md
.opencode/agents/java-security-reviewer.md
.opencode/agents/java-database-reviewer.md
```

这些 agent 的 canonical YAML 都显式：

```yaml
targets:
  - opencode
```

因此不会依赖 Claude Code 的 frontmatter 语义，也不写 `model: sonnet` 一类厂商绑定配置。

## 5. 推荐开发闭环

一次正常 Java 任务建议形成如下闭环：

```text
需求
  -> repository-first 检查
  -> 选择对应 Java skill
  -> 最小范围实现
  -> narrow tests
  -> broader affected tests
  -> build/quality gate
  -> java-code-reviewer
  -> 必要时 security/database reviewer
  -> fresh verification evidence
```

Review agent 不是为了制造问题。没有可证明的问题时应该明确 APPROVE，而不是输出样式噪音。

## 6. 不应该做的事情

- 不手工维护 TeamAI 已经生成的 `.opencode` 副本；
- 不把需要 OpenCode 自动加载的 TeamAI rule 放进 `rules/` 子目录；
- 不因为模板默认 Java 21 就擅自升级已有项目 JDK；
- 不因为推荐 Spring Boot 3 就擅自迁移 Spring Boot 2 项目；
- 不把 Maven 和 Gradle 同时引入同一个已有项目；
- 不从公网补依赖来掩盖内网镜像缺失；
- 不跳过项目已有的 `AGENTS.md`、README、父 POM、checkstyle/spotbugs/PMD 等约束；
- 不在没有证据的情况下把 review 猜测标成 HIGH/CRITICAL。
