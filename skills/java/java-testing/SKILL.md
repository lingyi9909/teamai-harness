---
name: java-testing
description: Use when adding, repairing, reviewing, or selecting tests for Java code, including JUnit tests, Spring integration tests, persistence tests, contract tests, and regression coverage.
---

# Java Testing

**REQUIRED SUB-SKILL:** Use superpowers:test-driven-development for production behavior changes.

Follow the repository's existing test stack. Prefer JUnit 5 when the project already uses it; use Mockito only at meaningful boundaries; use Spring test slices, full-context tests, Testcontainers, embedded infrastructure, or fixtures only when already supported or justified by the behavior under test.

A good Java test proves externally relevant behavior with the smallest stable scope. Assert outputs, state transitions, persisted effects, emitted events, authorization decisions, error contracts, or integration boundaries rather than private implementation steps. Avoid mocking value objects and pure collaborators merely to increase isolation.

For regressions, first reproduce the bug with a failing test. For database code, cover transaction/constraint semantics that an in-memory fake cannot represent. For HTTP APIs, cover validation and error shape as well as the happy path. For concurrency, retries, caching, scheduling, or time-sensitive logic, control time and synchronization explicitly instead of sleeping blindly.

Do not replace a repository's working assertion/test libraries just to standardize style. Run the narrow test class first, then the owning module suite, then the broader verification required by project instructions.
