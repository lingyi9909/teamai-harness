# Build and Offline Rules

本团队默认运行在公司内网。正常开发流程不得依赖公网可达性。

## Build Tool Detection

先依据仓库文件选择构建工具：

- `mvnw.cmd` / `mvnw` -> Maven Wrapper；
- `gradlew.bat` / `gradlew` -> Gradle Wrapper；
- 没有 wrapper 才使用机器已安装的 Maven/Gradle；
- 同时存在 Maven 与 Gradle 时读取 README/CI/最近使用方式，不猜主构建系统。

Windows 内网环境优先使用 `.cmd` / `.bat` wrapper；不要假设 WSL、bash、Homebrew 或 Unix-only 工具存在。

## Dependency Resolution

- 使用项目现有 Maven `settings.xml`、mirror、repository manager 和 Gradle repository 配置；
- 不新增 Maven Central、Gradle Plugin Portal、GitHub Packages 或任意公网 repository 来修复内网缺包；
- 不通过 `curl`、`wget`、PowerShell `Invoke-WebRequest`、`npx` 或 `git clone` 下载开发依赖；
- wrapper distribution 如果未缓存且内部镜像不存在，应报告 bootstrap 缺口，而不是切公网。

## Maven

优先从最小命令开始：

```text
mvnw.cmd -pl <module> -am test
mvnw.cmd test
mvnw.cmd verify
```

具体命令必须结合当前 POM 的 profile、Surefire/Failsafe、quality plugin 和 module 结构调整。

不得为了绕过失败随意使用：

```text
-DskipTests
-Dmaven.test.skip=true
```

除非用户明确要求构建不跑测试，且最终说明跳过了什么。

## Gradle

优先：

```text
gradlew.bat <module>:test
gradlew.bat test
gradlew.bat build
```

结合实际 task graph、custom verification task 和 wrapper 配置执行。

## 失败分类

构建失败先分类，不要立即改代码：

1. compile/test 真实代码失败；
2. 依赖或 plugin 无法从内部镜像解析；
3. JDK/toolchain 不匹配；
4. wrapper distribution 缺失；
5. 环境配置/数据库/外部服务缺失；
6. 静态检查或质量门禁失败。

只有类别 1 或与当前改动直接相关的类别 6 才应直接推动业务代码修复。环境问题必须如实报告。

## No Network Surprise

任何可能触发网络访问的命令都要先根据仓库和内网配置判断来源。不要把“命令本身是常见构建命令”等同于“不会访问公网”。
