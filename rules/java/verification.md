# Verification Before Completion

任何“完成、修复、通过、没有问题”的结论都必须有当前 HEAD 的 fresh evidence。

## 最小验证链

根据项目实际构建系统选择：

1. 与改动直接相关的最窄测试；
2. 受影响 module/package 的测试；
3. compile/build；
4. 项目已经配置的静态检查、格式、架构或质量 gate；
5. 对数据库/API/安全改动，执行对应 integration/contract/security regression（如果项目具备环境）。

不要为了套固定模板执行项目不存在的工具。

## Fresh Evidence

- 修改代码后重新执行验证；
- review 后如果又改代码，关键验证必须重跑；
- 不能拿上一个 commit、别人留言、历史 CI 或修改前的 PASS 作为当前 HEAD 证据；
- 命令执行结果必须看 exit code 和实际测试统计，不能只看最后一行看起来像成功。

## Failure Handling

验证失败时：

- 保留首个有信息量的失败；
- 区分代码 regression 与环境/内网依赖问题；
- 不通过删测试、放宽断言、关闭质量插件、`skipTests` 来制造绿色结果；
- 如果当前任务之外的既有失败阻塞全量验证，先证明它与当前改动无关，并单独报告。

## 完成报告

最终说明至少包含：

- 修改了什么；
- 为什么这样改；
- fresh 执行了哪些命令；
- 哪些命令 PASS；
- 哪些验证无法执行及具体原因；
- 是否存在需要人工/环境后续处理的风险。

没有执行的验证不能写成 PASS。
