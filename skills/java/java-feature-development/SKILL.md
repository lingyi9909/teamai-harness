---
name: java-feature-development
description: Use for implementing a Java backend feature in an existing repository. Detects the real build/framework conventions first, then implements the smallest compatible change with tests and fresh verification.
---

# Java Feature Development

Use this skill for new Java backend behavior, API capability, service logic, repository logic, or a contained cross-layer feature.

## 1. Establish repository truth

Before proposing code changes, inspect only the relevant project evidence:

- root/module `pom.xml` or `build.gradle*`;
- wrapper and JDK/toolchain settings;
- owning module/package;
- nearest analogous implementation;
- related tests and test conventions;
- Spring MVC/WebFlux/data access/security conventions if present;
- project instructions and quality plugins.

Write down the implementation boundary in one sentence: **what existing behavior will change, where, and what must remain unchanged**.

If the requested feature actually requires a public API/schema/event compatibility decision that the user has not specified, choose the least-breaking behavior supported by existing repository conventions and make that assumption explicit in the completion report.

## 2. Trace the real call path

Follow the request/entry point through the minimum relevant chain. Examples:

```text
Controller -> Application/Service -> Domain -> Repository
Consumer -> Handler -> Service -> Repository
Scheduled job -> Use case -> Gateway
```

Do not create layers merely because this diagram exists. Reuse the project's actual architecture.

Identify:

- input contract;
- validation location;
- authorization/tenant boundary;
- transaction boundary;
- persistence/external calls;
- output/error mapping.

## 3. Define executable guarantees

Convert the request into a small set of observable guarantees. For each guarantee identify the narrowest useful test level.

Examples:

- pure calculation -> unit test;
- controller validation/status mapping -> MVC/WebFlux test when the project uses it;
- transaction/query mapping -> integration test;
- backwards-compatible JSON contract -> serialization/contract test.

For a changed behavior, prefer adding the failing test before implementation when the project test architecture supports it. For legacy code that cannot be isolated safely, first add a characterization test around current behavior.

## 4. Implement the smallest compatible change

- follow existing naming/package conventions;
- reuse existing DTO/error/mapper patterns;
- do not introduce a new library for functionality already available in the JDK or project dependencies;
- do not upgrade Java, Spring Boot, Maven/Gradle plugins or unrelated dependencies;
- keep public API/schema changes explicit;
- preserve causes and existing error semantics;
- keep database and remote calls outside loops when batching is already supported.

## 5. Run narrow feedback first

Choose commands from repository evidence.

Maven Wrapper examples on Windows:

```text
mvnw.cmd -pl <module> -am -Dtest=<TestClass> test
mvnw.cmd -pl <module> -am test
```

Gradle Wrapper examples on Windows:

```text
gradlew.bat :<module>:test --tests <TestClass>
gradlew.bat :<module>:test
```

These are patterns, not mandatory literal commands. Match the project's modules and plugins.

If dependency resolution attempts to leave the intranet, stop and report the missing internal artifact/configuration instead of adding a public repository.

## 6. Review the diff

Before broader verification, inspect the complete diff and ask:

- Did anything outside the feature boundary change?
- Did generated/format-only changes appear?
- Did an API/DTO/schema compatibility change slip in?
- Is there a security, transaction, concurrency or nullability edge introduced by the diff?
- Are tests proving behavior rather than implementation details?

Remove unrelated changes.

## 7. Fresh verification

Run the narrow tests again after the final edit, then the affected module's broader test/build/quality gates. Never claim a gate passed without current output.

## 8. Completion evidence

Report:

- behavior implemented;
- files/modules touched;
- compatibility decisions;
- tests/gates actually executed and results;
- any environment-only gap.

Do not report speculative follow-up work as if it were required unless evidence from the current repository supports it.
