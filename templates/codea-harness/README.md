# 模板使用方式

这些文件由人按需复制，不由 TeamAI 自动激活，不是 Harness 已支持的配置协议。

| 模板 | 复制到哪里 | 谁确认 |
|---|---|---|
| [business-rule.md](business-rule.md) | 业务仓库已有规则目录，或 `docs/harness/business-rules/` | 业务/项目负责人 |
| [project-knowledge.md](project-knowledge.md) | 内网 `docs/codea-knowledge/projects/` 或已有项目资料目录 | 项目负责人 |
| [common-knowledge.md](common-knowledge.md) | 内网 `docs/codea-knowledge/common/` 或已有公共资料目录 | 组件/团队负责人 |
| [teamai.example.yaml](teamai.example.yaml) | 仅新建总仓时参考生成其根 `teamai.yaml` | TeamAI 管理员 |

从前三个模板创建的实例使用自己的文件名，归内网维护；今后导入公共模板更新时不覆盖实例。正式业务规则只留一个可编辑权威来源，项目介绍使用引用。

模板未填写时状态为 DRAFT；填写字段本身不证明审批有效。引用已经评审的来源和版本，并由现有团队流程确认。不得向本公共仓库提交填写后的内网实例。
