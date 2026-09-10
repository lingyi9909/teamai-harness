---
name: java-debugging
description: Use when a Java or Spring application has a bug, failing test, exception, incorrect result, startup failure, or regression. Requires evidence and root-cause proof before changing production code.
---

# Java Debugging

Do not start by guessing a fix. Establish what fails, where it first becomes wrong, and why.

## 1. Capture the symptom precisely

Collect the smallest useful evidence available:

- exact failing test and assertion;
- exception type, message and relevant stack frames;
- HTTP request/response contract;
- input that reproduces incorrect output;
- startup error and first causal exception;
- database error code/query context;
- commit/diff context if the problem is a regression.

Do not paste or expose secrets while collecting evidence.

## 2. Reproduce with the narrowest deterministic path

Prefer, in order:

1. an existing failing automated test;
2. a new regression test around the public behavior;
3. a local service/integration reproduction using existing fixtures;
4. a controlled manual reproduction when automation is not possible.

If the failure is environment-only, prove the environmental dependency before editing code.

## 3. Trace from symptom to first bad state

Read the actual caller/callee path and identify the first point where observed state diverges from expected state.

For Spring applications inspect relevant boundaries such as:

- request binding / validation;
- filter/interceptor/security context;
- controller -> service mapping;
- transaction proxy boundary;
- repository/ORM/MyBatis mapping;
- JSON serialization/deserialization;
- cache key/value lifetime;
- async executor/thread-local context;
- configuration property binding.

Do not infer a root cause from the deepest stack frame alone.

## 4. Form one falsifiable hypothesis at a time

State the hypothesis as:

```text
Because <specific condition>, <specific component> produces <bad state>, which causes <observed failure>.
```

Then find evidence that would prove or disprove it. Avoid changing multiple independent variables before rerunning the reproduction.

## 5. Common Java/Spring checks

Only inspect these when the symptom supports them:

- null/default value mismatch;
- `equals`/`hashCode` identity errors;
- `BigDecimal` scale/rounding comparison;
- timezone/offset conversion;
- generic type erasure/deserialization;
- Spring proxy/self-invocation and missing transaction interception;
- checked-exception rollback semantics;
- lazy-loading outside persistence context;
- MyBatis parameter/result mapping;
- concurrent modification/data race/thread-local leakage;
- stale cache or inconsistent cache key;
- classpath/version conflict;
- profile/config precedence.

A checklist match is not proof. Confirm against the current code path.

## 6. Add regression proof

Before the production fix when feasible, add a test that fails for the observed reason. The test should exercise the behavior boundary, not encode the intended implementation.

If adding a regression test first is impossible, document why and create the earliest practical automated proof after isolating the issue.

## 7. Apply the smallest root-cause fix

Fix the earliest appropriate layer. Do not add downstream null checks, retries, broad catches, sleeps, or data cleanup merely to mask an upstream correctness bug.

Do not combine unrelated refactoring with the fix.

## 8. Verify

Run:

- the reproduction/regression test;
- neighboring affected tests;
- build/static gates relevant to the changed module.

If the failure disappeared because an external service or dataset changed, that is not sufficient proof of a code fix.

## 9. Report evidence

Explain:

- root cause;
- evidence proving it;
- exact fix boundary;
- regression test;
- fresh validation results;
- unresolved environment dependency, if any.
