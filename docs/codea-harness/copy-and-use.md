# 复制到内网总仓库并接入业务项目

本文的“总仓库”指已有的独立 TeamAI 团队仓库，可供多个业务仓使用。若现有仓库采用 `teamai init .` 的单仓模式，TeamAI 资料根为 `.teamai/`：只把本文的 `skills/rules/docs` 合并到已有资料根下，先保留其原配置；不能在根目录再建一套并行团队资料。

## 1. 合并 TeamAI 侧文件

首次将以下内容合并到内网团队资料根，同名文件内容不同则先比对：

```text
skills/codea-harness-review/
rules/codea-harness-collaboration.md
docs/codea-harness/
docs/codea-knowledge/README.md
templates/codea-harness/
```

`docs/superpowers/` 是历史设计，可作为研发参考保留，不作为 Agent 的生效规范。根 `README.md` 只供阅读，不覆盖总仓已有 README。`.git/`、本机工具配置、凭据和运行记录不复制。

已有 `teamai.yaml` 继续使用原文件。本包不提供自动生效的根配置，避免把内网仓库地址改为 GitHub，或重置原有角色/项目配置。新建总仓时才参考 [配置示例](../../templates/codea-harness/teamai.example.yaml)，填写实际内网仓地址，并核对已安装 TeamAI 的支持字段。

若原仓已有 roles/projects 资源筛选，把此入口和规则加入对应的现有配置范围；不新增另一套角色系统。只新增一份 `codea-harness-review`，不把 `.code-harness/skills/*` 再复制进 TeamAI `skills/`，也不新增 TeamAI 版 `reviewer` Agent。

## 2. 并列放入 Harness 正式包

从已获准导入内网的**正式安装 ZIP**获取组件，保留包完整目录。当前核对的 1.6.4 安装包根包含：

```text
install.ps1
.code-harness/                          # 含正式 Runtime、清单与核心规则
.opencode/agents/reviewer.md
.opencode/commands/harness-review-reviewer.md
.opencode/tools/codea-reviewer-submit.ts
```

可以将这些正式包内容与 TeamAI 文件并列放在总仓库根，保留正式包其他附带文件和清单。若总仓已有任一同名运行组件或 OpenCode 配置，不整目录覆盖，保留完整安装包在单独的内网制品目录，从该目录安装。总仓库是否提交二进制沿用公司现有制品管理方式；本包不新增下载/发布工具。

**只复制 `.code-harness` 不足以接入目前的 1.6.4 Review。** 三个 Reviewer Host 文件与 Runtime 必须来自同一正式包。它们由 Harness 管理，TeamAI 不从总仓根 `.opencode/` 分发这些文件。

不要从某个已使用的业务项目反向复制 `.code-harness`：其中可能已经包含 `harness.yaml`、`project.md`、`runs/`、`chains/` 等项目状态。公共分发源必须是正式包，不带任何业务项目实例。

## 3. 在业务项目安装

以下 Windows 路径仅为操作示例。前提：公司已批准的 PowerShell（须能运行 `pwsh`）、TeamAI、OpenCode、Git 和正式包均可用；不在此步骤安装新依赖。Windows 自带的 `powershell.exe` 不等同于 `pwsh`。缺少 `pwsh` 时先按公司流程申请并准备核心安装说明要求的版本，不直接换成 Windows PowerShell 5.1 执行未经验证的安装。

假设完整正式安装包根是 `D:\team\total-repo`，业务项目是 `D:\work\order-service`。**首次安装**，在 PowerShell 执行：

```powershell
pwsh -NoProfile -File 'D:\team\total-repo\install.ps1' -ProjectRoot 'D:\work\order-service'
```

安装器按正式契约检查冲突并安装完整组件。项目已有 `.code-harness` 时使用该目标版本的正式 upgrade 包及其入口，不能用首次安装命令覆盖。不得为了通过安装删除项目状态或现有 Reviewer 配置。

在业务项目目录打开 OpenCode TUI，输入：

```text
读取 .code-harness/bootstrap.md，执行 harness init
```

已经完成初始化的项目直接使用现有配置。`harness init` 和 `harness review` 是发给 Agent 的意图，不能把它们当作一个已安装的 shell 命令。

## 4. 让 TeamAI 同步入口和资料

已连接正确内网总仓的项目只需按现有流程同步。首次接入先在**业务项目根目录**查看本机版本和帮助：

```powershell
Set-Location 'D:\work\order-service'
teamai --version
teamai init --help
```

确认该版本支持 `opencode` 目标后，把下列 URL 替换成实际内网 Git 地址执行；示例域名仅为占位符：

```powershell
teamai init 'https://git.example.invalid/team/total-repo.git' --scope project --agent opencode
teamai pull
teamai status
teamai doctor
```

若版本不支持该参数，使用其交互式初始化选择 OpenCode；不猜其他参数，不因此自动升级或安装包。选择公司已配置的 Git provider，缺认证或 provider 工具时通过现有内网流程补齐。

检查 OpenCode 实际能发现 `codea-harness-review`，并确认 TeamAI 已将规则关联到有效的 `opencode.json` instructions。只出现 `.opencode/rules/` 文件不等于规则已启用；不自行整文件替换工具配置。

TeamAI 的 `docs` 有独立同步位置配置，不保证变成业务项目 `docs/`。从本机有效配置确认实际位置；1.7 知识绑定必须显式指向已准备好的资料根，不猜 TeamAI 私有缓存路径。`templates/` 是供人使用的 Git 文件，不假设 TeamAI 自动分发它。

最后在业务项目 OpenCode TUI 输入：

```text
使用 codea-harness-review，执行 harness review。
```

TeamAI 同步成功、Harness 安装成功、Review 实际完成是三个独立结果。即使 TeamAI 暂时不可用，已安装 Harness 仍按自身入口工作；已要求的业务知识缺失必须显示为检查缺口。

## 5. 今后更新

- 外网更新：先导入新的公共资源包，仅比较和合并本包拥有的文件。内网自建知识和总仓配置保留。
- 内网更新：公司资料按原团队评审流程维护，不反推公共仓库。通用缺陷若需外网修复，另行整理无公司信息的复现例。
- Harness 更新：导入正式升级包，沿用核心升级程序保留项目状态、业务资料和规则；TeamAI 不负责替换 EXE。
- 不在 Review 中主动 `pull` 或升级。已有 TeamAI 会话开始同步行为沿用内网配置；运行中观察到文件变化时，受影响依据须重新验证。
