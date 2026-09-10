# Java Testing Rules

测试目标是证明行为，而不是追求无意义的覆盖率数字。

## 先识别项目测试栈

修改测试前确认：

- JUnit 4 还是 JUnit 5；
- Mockito / AssertJ / Hamcrest / Spring Test 是否已经使用；
- 是否使用 Testcontainers、H2、真实测试数据库或自研 fixture；
- Maven Surefire/Failsafe 或 Gradle test task 的实际配置；
- 单元测试、integration test、E2E 的命名和目录约定。

不要为了本 Harness 的默认值把一个稳定的现有测试栈整体迁移。

## 测试层级

优先选择能够证明当前改动的最窄层级：

1. 纯业务逻辑：普通 JUnit 单测；
2. 一个 Spring slice：仅在项目已有且确实需要 framework wiring 时使用 `@WebMvcTest`、`@DataJpaTest` 等；
3. 多 Bean/数据库/事务/序列化真实集成：integration test；
4. 完整系统行为：仅在关键链路需要时做 E2E。

不要默认给所有测试加 `@SpringBootTest`。

## 测试内容

每个 bug fix 至少包含能在修复前失败、修复后通过的 regression test，除非无法自动化并明确说明原因。

功能测试应覆盖：

- happy path；
- 与需求相关的边界值；
- 明确错误路径；
- 权限/租户边界（适用时）；
- transaction/rollback 行为（适用时）；
- 序列化、时区、金额精度等契约风险（适用时）。

## Mock 原则

- Mock 真正的外部边界或昂贵/不可控依赖；
- 不要 mock 被测类内部每一个协作者到导致测试只验证调用次数；
- 不要 mock value object、简单 DTO 或纯函数；
- 对 repository/database 行为，如果 bug 与 SQL、mapping、transaction 相关，优先用真实 integration fixture 而不是 mock 掩盖问题；
- 避免 `lenient()` 作为默认逃生口。

## 稳定性

- 测试不得依赖执行顺序；
- 不依赖真实公网服务；
- 时间相关逻辑优先注入 `Clock` 或项目已有时间抽象；
- 随机数据要可复现；
- 并发测试必须有确定的同步条件，避免纯 sleep 猜时序；
- 测试创建的数据必须隔离或清理。

## 验证顺序

实现过程中：

1. 先跑最窄测试；
2. 再跑受影响 module/package 的测试；
3. 最后跑项目要求的 verify/build/quality gate。

任何最终 PASS 声明都必须来自当前代码 HEAD 的 fresh 执行结果，不能引用修改前或之前会话的测试结果。
