# Spring Boot Rules

仅当仓库实际使用 Spring/Spring Boot 时应用本规则。先确认版本和技术栈，再修改。

## 版本与技术栈检测

- 从 parent POM、BOM、plugin 或 Gradle dependency management 确认 Spring Boot 版本；
- Spring Boot 3+ 使用 Jakarta namespace；不要把 Boot 2 项目局部改成 `jakarta.*`；
- 明确项目使用 Spring MVC 还是 WebFlux；不得在同一请求链中误混 blocking 与 reactive 模型；
- 明确项目的数据访问方式：JPA、MyBatis、JDBC、R2DBC 或其他；
- 明确 validation、exception handler、security、serialization 的现有约定。

## Bean 与依赖注入

- 优先 constructor injection；
- 不新增 field injection；
- Bean 的生命周期和 scope 必须明确；
- 避免用静态全局状态绕过 Spring lifecycle；
- 不为方便测试随意把内部实现暴露成 public Bean API。

## Controller/API

- Controller 负责协议边界：参数绑定、基础验证、认证上下文接入、响应映射；业务决策放在合适的 service/domain 边界；
- 使用项目已有 DTO，不直接把 persistence entity 暴露成外部 API，除非这就是项目明确契约；
- 新增或修改 endpoint 时检查 status code、content type、validation、异常映射、幂等语义和向后兼容性；
- 分页、排序、过滤参数必须有边界限制，避免无上限查询；
- 对上传、批量输入、大 body 显式考虑大小限制和资源消耗。

## 配置

- 配置项使用项目已有 `@ConfigurationProperties`/配置管理方式；
- 不硬编码环境地址、secret、数据库密码、token；
- 新配置必须说明默认值和缺失时行为；
- 启动期必需配置应 fail fast，而不是运行到请求路径才 NPE；
- profile 差异不能改变核心业务语义而没有测试。

## 事务

- `@Transactional` 放在真实事务边界，不为了“保险”到处添加；
- 理解 proxy/self-invocation 限制；
- 不把长时间远程调用默认包进数据库事务；
- 明确 rollback 语义，尤其是 checked exception、自定义异常和批量操作；
- 异步线程不会自动继承调用线程事务上下文；
- reactive transaction 必须使用对应 reactive 机制，不套 blocking 事务假设。

## Spring Security

- 不通过关闭 CSRF、permitAll 全路径、跳过方法鉴权等方式“先让接口跑通”；
- 新 endpoint 必须确认现有 SecurityFilterChain / method security 是否覆盖；
- 身份、租户、资源 owner 等授权条件必须在服务端验证；
- 认证成功不等于拥有业务资源操作权限。

## 可观测性

遵循项目已有 Actuator、metrics、trace、logging 方案。不要为单个功能引入第二套 observability stack。
