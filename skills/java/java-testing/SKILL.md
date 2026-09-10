---
name: java-testing
description: Use when designing, adding, repairing, or reviewing tests in a Java project. Selects the narrowest meaningful JUnit/Spring test layer and avoids over-mocking or unnecessary full-context tests.
---

# Java Testing

## 1. Detect the existing test architecture

Inspect build plugins, test dependencies, naming conventions, source sets and representative tests.

Determine:

- JUnit 4 vs JUnit 5;
- assertion library;
- Mockito or other mocking framework;
- Spring slices/full-context conventions;
- integration test naming and Surefire/Failsafe/Gradle routing;
- Testcontainers/embedded database/shared fixture conventions.

Do not migrate the project's test stack as part of an unrelated testing task.

## 2. State the behavior under test

Write the guarantee before writing the test:

```text
Given <business/input state>, when <action>, then <observable result>.
```

Prefer public behavior and meaningful state over private method coverage.

## 3. Choose the narrowest honest layer

### Unit test

Use for pure business logic or collaborators that can be isolated without reimplementing framework behavior in mocks.

### Spring slice

Use only when the project already uses a suitable slice and the behavior depends on binding, validation, serialization, repository mapping, etc.

### Integration test

Use when correctness depends on real Spring wiring, transaction behavior, SQL/ORM mapping, schema, serialization or an internal protocol boundary.

### E2E

Use only for critical cross-system flows where lower levels cannot prove the requirement.

Do not default to `@SpringBootTest` for every behavior.

## 4. Build robust fixtures

- give fixture values business meaning;
- make time deterministic through `Clock` or existing project abstraction when possible;
- avoid test ordering;
- avoid real public network calls;
- avoid production credentials/data;
- clean or isolate database state;
- make random input reproducible.

## 5. Mock intentionally

A mock should represent a real controllable boundary. Do not mock simple DTOs/value objects. Do not assert every collaborator call when the observable result already proves the behavior.

For persistence bugs, a mocked repository cannot prove SQL, mapping, locking or transaction behavior; use the project's integration path.

## 6. Validate RED/GREEN for regressions

For a bug fix, verify the new test fails for the expected reason before the fix when practical. Then apply the fix and verify the same test passes.

A RED test that fails because the fixture is broken or the application cannot start does not prove the regression.

## 7. Run broader affected tests

After narrow success, run the affected module/package suite and the repository's expected verify/build quality gates.

In offline environments, do not change repository sources to public registries when tests cannot resolve a dependency. Report the infrastructure gap separately.

## 8. Review test quality

Reject tests that:

- only mirror implementation details;
- have no meaningful assertion;
- catch exceptions just to make the test pass;
- use arbitrary sleeps for concurrency;
- depend on current wall-clock time without tolerance/control;
- silently disable themselves;
- loosen an existing assertion merely because a code change broke it.
