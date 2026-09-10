---
name: java-build-diagnostics
description: Use for Java build, dependency, classpath, JDK, Maven/Gradle, annotation processing, test-runtime, or Spring Boot startup failures. Complements Superpowers systematic-debugging with Java-specific diagnostic steps, especially for Windows-native and offline enterprise environments.
---

# Java Build Diagnostics

Diagnose Java build and startup failures from evidence. Use Superpowers `systematic-debugging` for the general debugging discipline; this skill supplies Java/JVM/build-tool specifics.

## 1. Classify the failure before changing code

Place the failure in one primary category:

- JDK/toolchain mismatch
- dependency resolution or repository failure
- Maven/Gradle plugin failure
- compile/type error
- annotation processor/code generation failure
- classpath/version conflict
- test compile/runtime failure
- packaging/startup failure
- Spring bean/configuration/auto-configuration failure

Record the exact failing command and the first meaningful error, not only the final summary line.

## 2. Confirm the actual toolchain

Inspect repository configuration before proposing fixes:

- Maven: `pom.xml`, parent/BOM, `.mvn/`, `mvnw.cmd`, profiles, compiler/surefire/failsafe plugins.
- Gradle: `build.gradle*`, `settings.gradle*`, `gradle.properties`, wrapper, version catalogs, Java toolchains.
- JDK: configured source/target/release/toolchain and the JDK actually executing the build.
- Spring Boot: parent/BOM/plugin version and framework generation already used by the project.

Never solve a mismatch by casually upgrading Java, Spring, plugins, or dependencies.

## 3. Diagnose by failure type

### Dependency/repository

- Capture the exact group/artifact/version or plugin coordinate that cannot resolve.
- Check whether dependency management, exclusions, profiles, mirrors, or repository configuration changes the effective version.
- Maven evidence may include `dependency:tree` and `help:effective-pom` when available.
- Gradle evidence may include `dependencies`, `dependencyInsight`, and configured repositories.
- Distinguish "artifact does not exist internally" from "network/certificate/auth/mirror configuration failed".

### JDK / compiler

Check for:

- `Unsupported class file major version`
- invalid `source`, `target`, or `release`
- toolchain mismatch between IDE, shell, CI, and wrapper
- module-system issues
- encoding or generated-source configuration

### Annotation processors / generated code

Inspect Lombok, MapStruct, QueryDSL, protobuf/OpenAPI generation, kapt-like processors, and compiler processor paths. Confirm generated sources are actually registered in the build.

### Classpath conflicts

For `ClassNotFoundException`, `NoClassDefFoundError`, `NoSuchMethodError`, `AbstractMethodError`, or linkage failures:

- identify the missing/changed class or method;
- determine which JAR version is loaded versus expected;
- inspect transitive dependency convergence and exclusions;
- do not add a random direct dependency until the conflicting path is known.

### Spring Boot startup

For bean creation, binding, configuration, or auto-configuration failures:

- start from the deepest root cause in the exception chain;
- inspect active profiles and relevant configuration sources;
- check constructor dependencies, conditional beans, component scanning, proxy constraints, configuration properties, migrations, and external service initialization;
- use framework diagnostic output such as condition evaluation only when it materially narrows the problem;
- never print secrets while inspecting configuration.

## 4. Offline / Windows constraints

- Prefer `mvnw.cmd` and `gradlew.bat` when present.
- Do not assume WSL, bash-only tooling, Maven Central, Gradle Plugin Portal, or public GitHub access.
- Never add a public repository to bypass a missing internal artifact.
- Never use `curl | sh`, public `git clone`, or implicit-download tooling as a normal fix.
- Respect internal mirrors, `settings.xml`, corporate certificates, proxies, and artifact repository policy.
- If an internal artifact/plugin is genuinely missing, report the exact coordinate/version and failing command instead of hiding the problem by changing versions.

## 5. Fix and verify

- Prefer the smallest root-cause fix consistent with the repository's existing stack.
- Re-run the narrow failing command first.
- Then run the repository's normal broader verification before claiming completion.
- State what evidence proved the diagnosis and what evidence proved the fix.
