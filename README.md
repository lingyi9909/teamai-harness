# TeamAI × Codea Harness

这是供内网总仓库合并使用的 **TeamAI 侧资源包**：共享 Review 入口、协作约定、知识模板和 1.7 研发交付说明。Harness 的 Runtime、核心 Skill 和 Reviewer 随正式 Codea Harness 包提供。

**当前交付状态：资源与设计已准备；1.7 核心功能尚未在本仓库实现，内网 Windows 联调尚未验收。** 本次范围为 Code Review、内网协同与 TeamAI 协同；日志平台、登录验证码、排障和修复增强留待后续版本。

## 合并到你的总仓库

将本仓库的 `skills/`、`rules/`、`docs/`、`templates/` **合并**到内网总仓库同名目录。首次合并新增本文列出的文件；遇到同名不同内容先比较，不整目录替换。总仓库已有 `teamai.yaml`、`README.md`、`AGENTS.md` 和工具配置继续由原维护人管理，不复制本仓库的 `.git/`。

组合后的布局：

```text
内网总仓库/
├── teamai.yaml                         # 已有 TeamAI 配置
├── skills/codea-harness-review/         # 本仓库提供的轻量入口
├── rules/codea-harness-collaboration.md # 本仓库提供的协作约定
├── docs/codea-harness/                 # 接入、归属、研发计划
├── docs/codea-knowledge/               # 真实知识仅在内网补充
├── templates/codea-harness/            # 手工使用的模板，不自动激活
├── .code-harness/                      # 另行导入正式安装包
├── .opencode/                          # 正式安装包自带的 Reviewer 资源
└── install.ps1                        # 同一正式安装包自带的安装入口
```

**需要调整你说的“只复制 `.code-harness`”这一步：** 已核对的 1.6.4 安装契约要求同时保留正式包中的 `install.ps1` 和三个 `.opencode` Reviewer 文件。缺这些文件，Review 无法完整运行。不要从核心源码仓库复制 `.code-harness` 代替正式包；源码不包含运行程序。

总仓库是资源来源。每个业务项目仍须通过正式安装器接入 Harness；`teamai pull` 负责 TeamAI 资源同步，不能替代 Runtime 安装。完整操作见 [复制与使用](docs/codea-harness/copy-and-use.md)。已有 Harness 项目走其正式升级流程。

## 文件导航

| 内容 | 入口 |
|---|---|
| 复制、安装、OpenCode 使用 | [copy-and-use.md](docs/codea-harness/copy-and-use.md) |
| 外网/内网、TeamAI/Harness、知识归属 | [ownership-and-knowledge.md](docs/codea-harness/ownership-and-knowledge.md) |
| 本次 1.7 研发范围和实施顺序 | [1.7-delivery-plan.md](docs/codea-harness/1.7-delivery-plan.md) |
| 版本依据及已执行/未执行的验证 | [compatibility-and-validation.md](docs/codea-harness/compatibility-and-validation.md) |
| 内网知识放置约定 | [codea-knowledge](docs/codea-knowledge/README.md) |
| 可复制的知识和配置模板 | [templates](templates/codea-harness/README.md) |

本仓库不携带实际公司规则、项目资料、账号、内网地址和日志，不要求安装任何新依赖。内网只连接已批准的内网 Git 和模型服务；不将外网 GitHub 仓库设置为内网运行时订阅来源。
