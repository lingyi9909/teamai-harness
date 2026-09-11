# TeamAI × Codea Harness

本仓库提供加入现有内网 TeamAI 总仓的 Harness 接入资源。**TeamAI 原有目录、配置和知识位置保持不变，仅增加入口、必要协作约定和接入说明。**

| 对象 | 管理方式 |
|---|---|
| 总仓文件，包括附带的 Harness 完整正式包 | Git 管理版本及变更 |
| Skills、Rules、知识等 TeamAI 资源 | 原有 `teamai init/pull` 等流程同步 |
| 业务项目中实际安装的 Harness | 原正式安装器与 upgrade 流程 |

Git拉取或TeamAI同步成功，都不表示业务项目的Harness已经安装或升级。

## 接入时需要的内容

- 在原 `skills/` 中加入 `codea-harness-review/` 轻量入口。
- 在原 `rules/` 中加入必要的 `codea-harness-collaboration.md`。
- 将 [接入说明](docs/codea-harness/copy-and-use.md) 放在原文档位置；已有项目/业务知识继续原地维护。
- Harness 完整正式包可存放在总仓中一个独立目录，或公司已有内网制品位置。其内部目录保持原样，不拆散到总仓根。

本仓库的 `templates/`、`docs/codea-knowledge/` 都是可选说明，不是必须新增的TeamAI目录。已有对应资料时直接沿用。合并同名资源先比较，保留原 `teamai.yaml`、README、AGENTS及工具配置，不复制`.git/`。

当前核对的1.6.4完整包除了`.code-harness/`，还包含`install.ps1`和三个`.opencode` Reviewer资源；从正式包安装，不能只复制核心目录或源码。详见[复制与使用](docs/codea-harness/copy-and-use.md)。

## 1.7 研发交接

最新完整文档由核心仓库统一维护：

- [1.7 完整项目设计](https://github.com/lingyi9909/codea-harness/blob/main/docs/superpowers/specs/2026-09-11-codea-harness-1.7-integrated-design.md)
- [1.7 完整执行计划](https://github.com/lingyi9909/codea-harness/blob/main/docs/superpowers/plans/2026-09-11-codea-harness-1.7-integrated-plan.md)

研发从同一提交读取两份文档，内网按原审批方式导入离线副本，保留两文件的相对目录。这里的历史设计/参考副本不再作为开发主计划，不独立维护第二份最新方案，也不要求TeamAI加载完整研发文档。

当前交付是接入资源和设计，1.7核心功能与真实内网Windows联调仍待完成。范围仅限Code Review、内网协同和TeamAI协同；日志平台、登录验证码、排障及修复增强留待后续。

其他材料：[文件归属](docs/codea-harness/ownership-and-knowledge.md)、[兼容记录](docs/codea-harness/compatibility-and-validation.md)、[可选模板](templates/codea-harness/README.md)。本公共仓库只保存通用资源，不接收真实公司知识、代码、账号或运行资料，不新增依赖。
