# Repository First

任何 Java 代码修改之前，先理解当前仓库，而不是把通用模板强加给项目。

## 开始工作前必须确认

至少读取与任务相关的以下事实：

- `pom.xml`、父 POM/BOM 或 `build.gradle` / `build.gradle.kts`；
- `mvnw*` / `gradlew*` 是否存在；
- 当前 Java source/target/toolchain 版本；
- Spring Boot / Spring Framework 版本（如果使用 Spring）；
- 相关 package、module、controller/service/repository/domain 类；
- 同类功能已有实现；
- 对应单元测试、集成测试、测试基类和 fixture；
- `application*.yml/properties` 中与任务相关的配置；
- 项目已有 `AGENTS.md`、README、贡献指南、checkstyle、spotbugs、PMD、ArchUnit 等约束。

## 权威顺序

发生冲突时按以下优先级处理：

1. 用户当前明确要求；
2. 当前项目自身规则与已验收设计；
3. 当前项目构建文件、代码和测试体现出的真实约定；
4. 本 TeamAI Harness 的通用规则；
5. 通用 Java/Spring 最佳实践。

不得仅因为本 Harness 推荐 Java 21 / Spring Boot 3 就升级一个现有 Java 17 / Spring Boot 2 项目。

## 改动范围

- 只改完成当前需求所需的最小范围；
- 不做与任务无关的包结构调整、统一命名、格式化全仓、依赖升级或框架迁移；
- 不因为发现旧代码不理想就顺手重写；
- 如必须触碰公共 API、共享 DTO、数据库 schema、序列化格式或事务边界，先识别调用者和兼容性影响；
- 生成代码、vendor 代码、构建产物默认不手改，除非项目明确把它们作为源文件维护。

## 多模块项目

在 Maven/Gradle 多模块项目中，先确定：

- 真正 owning module；
- 上下游模块依赖；
- 是否存在 shared/common API module；
- 最窄可运行测试模块；
- 根级 verify/build 是否包含额外质量门禁。

不要在根目录凭文件名猜 ownership。

## 完成定义

“代码写完”不等于任务完成。必须能说明：

- 为什么修改这些文件；
- 哪些现有约定被复用；
- 哪些行为由测试覆盖；
- 执行了哪些 fresh 验证；
- 是否有因为内网依赖、环境或外部系统导致无法执行的验证，以及具体缺口。
