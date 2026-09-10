---
name: java-refactoring
description: Use for behavior-preserving refactoring of Java code. Establishes characterization coverage, identifies public and persistence contracts, makes small structural changes, and verifies behavior after each step.
---

# Java Refactoring

Refactoring means changing structure while preserving externally observable behavior unless the user explicitly requests a behavior change.

## 1. Define the preservation boundary

Identify what must not change:

- public Java/API signatures;
- HTTP request/response contract;
- serialized field names and values;
- database schema/query semantics;
- event/message format;
- exception/error mapping;
- transaction semantics;
- ordering/timing guarantees that callers rely on.

If behavior is intentionally changing, separate that change from the structural refactor in tests and explanation.

## 2. Read callers and tests

Before moving or extracting code, inspect direct callers, implementations, tests and DI wiring. For Spring beans also check annotations, qualifiers, proxy-sensitive annotations and configuration.

Do not assume a private-looking implementation is isolated if reflection, framework scanning, serialization or configuration refers to it.

## 3. Add characterization coverage where risk is high

For legacy or poorly tested logic, first capture current observable behavior. Focus on business outcomes, not private structure.

Useful characterization targets include:

- tricky branching/business rules;
- null/empty behavior;
- exception mapping;
- ordering;
- transaction outcomes;
- serialization;
- query result mapping.

## 4. Refactor in small reversible steps

Examples:

- extract a cohesive method/class;
- replace duplicated stable logic with one shared unit;
- introduce a value object around a real invariant;
- move framework mapping away from domain logic;
- split an oversized service by responsibility;
- replace conditional complexity with an existing project strategy pattern.

After each meaningful step, keep the repository buildable and run the narrow relevant tests.

## 5. Spring-specific cautions

When moving methods/classes, preserve or deliberately re-evaluate:

- `@Transactional` proxy boundaries and self-invocation behavior;
- bean names/qualifiers;
- `@Async`, `@Cacheable`, `@Retryable`, security method annotations;
- configuration property binding;
- component scanning/package boundaries;
- AOP pointcuts.

A refactor that changes whether a proxy intercepts a call is a behavior change.

## 6. Persistence cautions

- moving entity fields/getters can affect ORM mapping;
- changing `equals/hashCode` can change entity/set behavior;
- changing collection type can affect ordering/lazy loading;
- repository method rename can alter derived-query semantics;
- MyBatis mapper namespace/signature changes require XML/interface alignment.

## 7. Diff discipline

Do not combine refactoring with:

- dependency upgrades;
- JDK/Spring migrations;
- broad reformatting;
- unrelated warning cleanup;
- API redesign.

If such work is necessary, isolate it as a separate explicitly justified task.

## 8. Final verification

Run characterization tests, changed-module tests and project quality gates on the final diff. Compare the final external behavior against the preservation boundary before declaring the refactor complete.
