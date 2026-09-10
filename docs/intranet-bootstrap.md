# 内网 Bootstrap 指南

## 目标

让完全不能访问公网的 Windows Java 开发环境使用 TeamAI + OpenCode + 本 Harness。

正常开发阶段必须做到：公网 DNS/HTTP/HTTPS 不参与依赖获取、skill 同步或代码执行。首次准备安装包和仓库镜像属于 bootstrap 阶段，应在可联网环境完成并经过公司允许的介质/仓库进入内网。

## 需要提前准备的内容

1. 公司批准版本的 Node.js 18+；
2. 公司批准版本的 TeamAI CLI npm 包及其完整依赖，或公司内部 npm 镜像中的对应包；
3. OpenCode 本体及公司内部认可的模型/provider 配置；
4. 本 `teamai-harness` 仓库 `develop` 分支的完整内容或最终稳定快照；
5. Java 项目所需 JDK、Maven/Gradle wrapper distribution、插件和依赖应已经能从内部镜像/缓存解析。

不要把 token、用户名密码、内部证书私钥、Maven `settings.xml` 密码或 OpenCode provider secret 提交到 Harness 仓库。

## 把 Harness 原样复制到内网

在公司内网创建独立 Git 团队仓，将模板内容原样推送进去：

```text
skills/
rules/
agents/
docs/
README.md
```

**不要从公网模板携带 `teamai.yaml`。** 本模板故意不提交它。当前 TeamAI CLI 在 `teamai init <repo>` 时如果发现远端团队仓没有 `teamai.yaml`，会创建默认配置，并将 `repo` / `provider` 基于实际初始化的团队仓生成。这样内部仓不会残留 `github.com/lingyi9909/teamai-harness` 之类公网地址。

同样不要为了 OpenCode 手工创建 `.opencode/*`；它们属于业务项目中的 TeamAI 生成物。

## 首次初始化内网团队仓

在一台已经安装 TeamAI CLI、能访问内网 Git 和 OpenCode 的开发机上，进入一个 Java 业务项目根目录：

```text
cd C:\path\to\java-project
teamai init <internal-teamai-repo-url> --scope project --agent opencode
teamai pull
```

第一次初始化后检查内网团队仓是否已经出现 TeamAI 创建的 `teamai.yaml`。该文件此后属于**内网团队仓自己的配置**，应按你们正常 review/merge 流程维护；不要再用公网模板覆盖它。

如果内网镜像的是较旧 TeamAI CLI，不接受或不正确处理 `--agent opencode`，先使用：

```text
teamai init <internal-teamai-repo-url> --scope project
teamai pull
```

然后通过 `teamai doctor` 确认 OpenCode 检测/同步状态。优先升级内部 TeamAI CLI，不要自造 `.opencode` 路径绕过 TeamAI。

## 验证 TeamAI / OpenCode 注入

```text
teamai --version
teamai status
teamai list --source repo
teamai list --source local --agent opencode --verbose
teamai doctor
```

随后检查项目中由 TeamAI 管理的 OpenCode 资源：

```text
.opencode\skills\
.opencode\rules\
.opencode\agents\
opencode.json
```

当前 TeamAI 对 OpenCode 的 rules activation 是 `.opencode/rules/*.md` 非递归 glob，所以应该看到本 Harness 的 `java-*.md` 规则直接位于 `.opencode\rules\` 根目录，而不是嵌套在 `.opencode\rules\java\`。

不要以“目录存在”作为唯一成功标准。`teamai doctor` 必须没有与 TeamAI/OpenCode 注入相关的阻断问题，且 `opencode.json` 中 TeamAI 管理的 rules instructions 应有效。

## Java 构建的离线规则

OpenCode 执行构建时按以下顺序选择命令：

### Maven

Windows：

```text
mvnw.cmd test
mvnw.cmd verify
```

如果仓库没有 wrapper，才使用公司已安装并已配置内部镜像的：

```text
mvn test
mvn verify
```

### Gradle

Windows：

```text
gradlew.bat test
gradlew.bat build
```

如果仓库没有 wrapper，才使用公司已安装并已配置内部镜像的 Gradle。

## 依赖缺失时的行为

如果 Maven/Gradle 报告 artifact/plugin/wrapper distribution 无法从内网解析：

1. 保留完整坐标、版本和失败仓库信息；
2. 判断是项目声明问题还是内部镜像缺包；
3. 如果属于镜像缺包，停止自动换源；
4. 报告需要由内部制品管理员补齐的 artifact/plugin/version；
5. 补齐后重新执行同一条构建命令。

禁止为了让测试“变绿”而临时增加 Maven Central、Gradle Plugin Portal、GitHub raw URL 或其他公网源。

## 更新 Harness

后续外网模板更新时，只同步 canonical 资源和文档：

```text
skills/
rules/
agents/
docs/
README.md
```

**不要用外网模板覆盖内网团队仓已经生成的 `teamai.yaml`。** 该文件携带内网团队仓自身 repo/provider 等配置。

同步完成后，业务项目运行：

```text
teamai pull
teamai status
teamai doctor
```

TeamAI 应负责增量同步和 OpenCode 资源渲染。不要用脚本直接覆盖每个项目的 `.opencode` 目录，因为那会绕开 TeamAI 的资源生命周期、删除语义和 OpenCode rules activation 逻辑。
