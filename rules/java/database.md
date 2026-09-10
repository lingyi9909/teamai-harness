# Java Database Rules

数据库改动必须同时考虑数据正确性、事务、性能、上线兼容性和回滚。

## 先识别真实数据访问方式

确认项目使用：

- JPA/Hibernate；
- MyBatis / MyBatis-Plus；
- Spring JDBC / jOOQ；
- R2DBC；
- 项目自研 DAO 层；
- Flyway/Liquibase/SQL 脚本/独立 DBA 流程中的哪一种 migration 机制。

不要把一种框架的假设套到另一种框架。

## 查询正确性

- 参数必须绑定，不拼接不可信输入形成 SQL；
- 明确 null、空集合、分页、排序和大小写语义；
- 修改 join/filter 时检查是否改变结果基数；
- 聚合、distinct、group by 必须与业务口径一致；
- ORM lazy/eager loading 变化需要检查查询数量和 serialization 边界；
- MyBatis dynamic SQL 必须检查空条件是否意外退化成全表操作。

## 性能

对高频或大表路径，检查：

- where/join/order by 与索引是否匹配；
- 是否出现 N+1；
- 是否无界分页/全表扫描；
- offset 深分页是否符合现有方案；
- 批处理是否存在逐条数据库 round-trip；
- 新索引是否影响写入成本、唯一性和存储；
- query plan 只能在有可用测试/预发数据库时实际验证，不要凭 SQL 外观伪造执行计划结论。

## 写入与事务

- update/delete 必须有明确范围条件；
- 批量操作需要说明部分失败语义；
- transaction boundary 与业务原子性一致；
- 外部 HTTP/RPC 调用不要无理由持有数据库锁；
- 乐观锁/悲观锁必须匹配冲突模型；
- 重试逻辑要确认操作幂等性；
- 不用 JVM `synchronized` 假装解决多实例数据库并发问题。

## Schema Migration

生产 schema 变化优先采用 expand -> migrate/backfill -> contract 的向后兼容方式：

- 先增加兼容字段/表/索引；
- 旧代码和新代码过渡期都能运行；
- backfill 可重入、可观察、可限速；
- 再切读写路径；
- 最后删除旧结构。

破坏性 DDL、类型收窄、NOT NULL、唯一约束、大表索引等必须说明现有数据是否满足条件，以及失败/回滚策略。

## 敏感数据

- 不在日志中打印密码、token、完整身份证/银行卡等敏感字段；
- 新增持久化敏感字段时遵循项目加密/脱敏/访问控制规则；
- 测试 fixture 不使用真实生产数据或真实凭据。
