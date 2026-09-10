---
name: java-feature-development
description: Use when implementing or changing business behavior in a Java codebase, especially when the repository has multiple modules, Spring components, persistence boundaries, or established local conventions.
---

# Java Feature Development

Use this skill for Java implementation work. Repository evidence is authoritative: read local instructions, build files, module boundaries, nearby production code, and nearby tests before choosing a pattern.

**REQUIRED SUB-SKILL:** Use superpowers:test-driven-development for behavior changes.
**REQUIRED SUB-SKILL:** Use superpowers:verification-before-completion before claiming completion.
**REQUIRED SUB-SKILL:** Use superpowers:brainstorming when requirements or design choices are materially ambiguous.

## Working contract

1. Identify the owning module and the smallest existing extension point.
2. Confirm Java/framework versions from `pom.xml`, `build.gradle*`, wrappers, parent BOMs, and source imports. Do not assume Spring, Lombok, MapStruct, JPA, MyBatis, or AssertJ merely because they are common.
3. Add or change a test first and observe the expected failure.
4. Implement the minimum production change that satisfies the test while preserving existing public contracts unless the task explicitly changes them.
5. Keep controllers/adapters thin, business policy in the established domain/service layer, and persistence details behind the repository's existing boundary.
6. Preserve nullability, exception, logging, transaction, serialization, validation, and concurrency conventions already used by the module.
7. Do not add a dependency, plugin, annotation processor, or build repository unless project evidence and the task require it and the dependency is available through the configured intranet source.
8. Run the narrow test first, then the module/project verification commands supported by the repository.

When the requested change crosses modules, treat each module contract explicitly rather than bypassing it with a convenience dependency.
