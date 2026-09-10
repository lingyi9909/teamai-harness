# 内网 Bootstrap 指南

## 目标

让完全不能访问公网的 Windows Java 开发环境使用 TeamAI + OpenCode + 本 Harness。

正常开发阶段必须做到：公网 DNS/HTTP/HTTPS 不参与依赖获取、skill 同步或代码执行。首次准备安装包和仓库镜像属于 bootstrap 阶段，应在可联网环境完成并经过公司允许的介质/仓库进入内网。

## 需要提前准备的内容

1. 公司批准版本的 Node.js 18+；
2. 公司批准版本的 TeamAI CLI npm 包及其完整依赖，或公司内部 npm 镜像中的对应包；
3. OpenCode 本体及公司内部认可的模型/provider 配置；
4. 本 `teamai-harness` 仓库的完整 Git 历史或至少当前稳定快照；
5. Java 项目所需 JDK、Maven/Gradle wrapper distribution、插件和依赖应已经能从内部镜像/缓存解析。

不要把 token、用户名密码、内部证书私钥、Maven `settings.xml` 密码或 OpenCode provider secret 提交到 Harness 仓库。

## 把 Harness 复制到内网

推荐保留当前仓库结构原样，在内网创建独立 Git 仓并推送：

```text
teamai.yaml
skills/
rules/
agents/
docs/
```

`teamai.yaml` 中的公网 `repo` 字段只是本公开模板的来源描述。复制到内网后，管理员可以按本机 TeamAI CLI 当前 schema 将其改成实际内部仓库 URL；不要修改 `skills/rules/agents` canonical 目录结构，也不要为了 OpenCode 改成 `.opencode/*`。

## 在 Windows Java 项目中初始化

PowerShell 或 CMD 进入项目根目录：

```text
cd C:\path\to\java-project
teamai init <internal-teamai-repo-url> --scope project --agent opencode
teamai pull
```

验证：

```text
teamai --version
teamai status
teamai list --source repo
teamai list --source local --agent opencode --verbose
teamai doctor
```

随后检查项目中由 TeamAI 管理的 OpenCode 资源是否出现：

```text
.opencode\skills\
.opencode\rules\
.opencode\agents\
opencode.json
```

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

外网版本完成审核后，把新的稳定提交同步进入内网团队仓；业务项目再运行：

```text
teamai pull
teamai status
teamai doctor
```

TeamAI 应负责增量同步和 OpenCode 资源渲染。不要用脚本直接覆盖每个项目的 `.opencode` 目录，因为那会绕开 TeamAI 的资源生命周期、删除语义和 OpenCode rules activation 逻辑。
