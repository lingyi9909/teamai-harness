# Java Security Rules

安全判断必须基于真实 trust boundary、输入来源和可利用路径，不做形式化“安全剧场”。

## Secrets

- 不把 password、API key、token、cookie、private key、数据库连接密钥写入源码、测试、日志或文档；
- 不打印环境变量全集、Maven settings 凭据、OpenCode provider secret；
- 示例值必须明显是无效占位符；
- 发现疑似真实 secret 时停止传播其值，只报告位置和处理建议。

## Input Validation

所有外部边界输入按项目现有方式验证：HTTP、消息队列、文件、数据库外部数据、RPC、CLI 参数。

- 业务合法性不能只靠前端；
- Bean Validation 只负责其能够表达的约束，跨字段/业务权限仍需服务端校验；
- 文件路径、文件名和归档内容要防 traversal；
- URL/回调地址/代理能力要考虑 SSRF；
- HTML/富文本输出根据输出上下文防 XSS；
- SQL 使用参数化查询或 ORM 参数绑定。

## Authentication and Authorization

- authentication 与 authorization 分开验证；
- 新接口必须确认是否进入现有 security chain；
- 服务端检查 resource ownership、tenant boundary、role/permission；
- 不信任客户端提交的 userId/tenantId 作为最终权限依据；
- 管理员/内部接口仍需遵循项目明确的访问控制边界。

## Deserialization and Binding

- 不把任意外部 JSON 直接绑定到带有敏感可写字段的 persistence entity；
- 对 polymorphic deserialization、Java serialization、表达式执行、脚本执行保持高警惕；
- 新增反序列化能力时限制允许类型和输入大小；
- 不使用不安全的 native Java serialization 接收不可信数据。

## File and Process Execution

- 不把用户输入直接拼进 shell 命令；
- 能使用 Java API 完成的文件/进程操作，不通过 `sh -c` / `cmd /c` 增加 shell 注入面；
- 如必须启动进程，参数用结构化参数列表并进行 allowlist 校验；
- 上传文件不信任原始文件名和 MIME 声明。

## HTTP Clients

- 明确 connect/read/request timeout；
- 重试只用于可安全重试的请求；
- 不自动把认证 header 转发给任意重定向目标；
- TLS 验证不得为了调试永久关闭；
- 内网服务地址来自受控配置，不在代码中散落硬编码。

## Review Severity

只有能说明具体输入、可达路径、缺失保护和实际影响时才把问题定为 HIGH/CRITICAL。无法证明可利用性的猜测应降级或不报告。
