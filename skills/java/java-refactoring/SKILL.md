---
name: java-refactoring
description: Use when restructuring Java code while the intended observable behavior should remain unchanged, including extraction, renaming, dependency cleanup, package movement, and simplification.
---

# Java Refactoring

Refactoring must preserve behavior. Establish that behavior with existing tests or add characterization tests before structural changes when coverage is insufficient.

**REQUIRED SUB-SKILL:** Use superpowers:test-driven-development when new characterization coverage is required.
**REQUIRED SUB-SKILL:** Use superpowers:verification-before-completion before declaring the refactor safe.

Work in small semantic steps. Respect module/API boundaries, dependency direction, Spring bean wiring, serialization names, persistence mappings, reflection/service-loader usage, configuration keys, public exception behavior, and binary/source compatibility where those are part of the repository contract.

Prefer removing duplication and clarifying ownership over introducing abstraction for hypothetical reuse. Do not mix unrelated behavior changes into a refactor. If a behavior change is necessary, split it into a separately tested change and make it explicit.

After each meaningful step, run the nearest relevant tests. Finish with repository-required compile, static analysis, and test gates so mechanical correctness and wiring failures are caught as well as behavioral regressions.
