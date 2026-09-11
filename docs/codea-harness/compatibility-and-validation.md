# 兼容依据与验证记录

核对日期：2026-09-11。本资源包不携带 Runtime，不声明任何 1.7 功能已实现或任何版本组合已经获得生产验收。

## 依据

- 核心仓库核对提交：`b864bd19b9313bd882da89612e701d8bb3221e7d`。这是当时 main 的安装与路由参考，**不是** 1.6.4.final 已验收基线的证明。
- 依据：[正式安装说明](https://github.com/lingyi9909/codea-harness/blob/b864bd19b9313bd882da89612e701d8bb3221e7d/README.md)、[安装器源文件](https://github.com/lingyi9909/codea-harness/blob/b864bd19b9313bd882da89612e701d8bb3221e7d/.github/scripts/task164-install.ps1)、[bootstrap 与 Reviewer Host 约束](https://github.com/lingyi9909/codea-harness/blob/b864bd19b9313bd882da89612e701d8bb3221e7d/.code-harness/bootstrap.md)。这些文档表明独立 Reviewer 还需三个包根 `.opencode` 资源；不可只复制核心目录。
- 该核心提交的 Host 说明使用 `opencode-ai@1.18.25` 作为其认证版本。这里只记录来源，不要求自动升级用户机器，不以“能启动 OpenCode”代替核心指定版本的验收。
- TeamAI 结构依据：[官方说明](https://github.com/Tencent/teamai-cli/blob/main/README.md)、[使用指南](https://github.com/Tencent/teamai-cli/blob/main/docs/usage-guide.zh-CN.md)、[配置定义](https://github.com/Tencent/teamai-cli/blob/main/src/types.ts)、[Skills 处理](https://github.com/Tencent/teamai-cli/blob/main/src/resources/skills.ts)、[Rules 处理](https://github.com/Tencent/teamai-cli/blob/main/src/resources/rules.ts)、[Docs 处理](https://github.com/Tencent/teamai-cli/blob/main/src/resources/docs.ts)。已核对 flat Skill、rules、docs 布局和示例配置字段；内网已安装版本可能不同，仍须实际核对。

## 本次验证范围

验证资源文件的格式、相对文档链接、路径归属及合并边界；使用独立 Agent 模拟错误工作目录、旧版 1.6.4、Reviewer 失败和必需规则缺失场景。该验证只覆盖文档与入口决策，不执行正式审核，不等同于产品端到端验收。

基线模拟能识别“同步不等于安装”和“缺规则不算通过”，但未给出正式入口和三个 Reviewer 文件，且将 Reviewer 失败泛化为“恢复后继续”。新增入口明确从项目实际合同定位资源、交给正式 Reviewer，并按已安装版本合同处理失败，避免自行恢复失败阶段。

本包无业务源码、无构建脚本、无运行时依赖；未安装第三方包。配置示例通过 YAML 解析与官方字段静态核对，不声称已调用 TeamAI 原生配置解析器。

本次资源验证结果：

| 检查 | 结果与限制 |
|---|---|
| Skill 元信息、YAML、相对文档链接、空白检查 | 通过；仅检查交付资源 |
| 向已有总仓合并、重复合并、同名不同内容 | 模拟通过；保留原配置、知识和核心文件；不是已实现的自动合并器 |
| A：总仓与业务项目根混淆 | 模拟正确定位业务根及正式组件 |
| B：1.6.4 遇到拟定 1.7 配置和草稿规则 | 模拟未启用未实现能力，保留原范围与正式流程 |
| C：独立 Reviewer 失败 | 模拟按版本合同失败处理并停止，不接管或自行推进 |
| D：技术零缺陷但必查规则缺失 | 模拟保留业务未完成项，不给整体通过 |

复核中发现的 `pwsh` 前提不明确、详细设计仅有外网链接两项均已修订：安装说明明确需要可用的 `pwsh`，固定版本的代码 Review 设计与原执行计划已作为随包离线参考提供。

## 必须在内网补做的验证

- 已批准 TeamAI 版本能发现 Skill，并激活 OpenCode 规则；有资源筛选时入口确实在同步范围内。
- 实际 Windows 完整安装/升级，Reviewer Host 与 Runtime 同包一致，存在同名文件时不破坏原配置。
- 正式独立 Reviewer 在已批准 OpenCode/模型环境完成一次真实 Review；验证缺组件与 Reviewer 失败处理。
- 1.7 核心交付后再验证知识绑定、必读规则/引用校验、冲突与运行中变化，以及报告未完成项。
- 外网完全不可达时，无新依赖下载，已有内网 Git/模型可用；公司知识不外发。公共模板或本地模拟不能代替这项验证。

本次没有实际内网、Windows/PowerShell、TeamAI CLI 和公司模型运行条件，上述验证均未执行。正式联调以最终通过验收的核心基线、公司已批准组件及实测结果为准。
