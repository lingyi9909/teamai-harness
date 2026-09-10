---
name: java-debugging
description: Use when a Java service, test, build, JVM process, Spring application, database interaction, or concurrent flow behaves unexpectedly or fails without a proven root cause.
---

# Java Debugging

**REQUIRED SUB-SKILL:** Use superpowers:systematic-debugging before proposing fixes.
**REQUIRED SUB-SKILL:** Use superpowers:verification-before-completion after the fix.

Start from evidence, not framework folklore. Capture the exact failing command, exception chain, relevant logs, configuration/profile, inputs, and the smallest reproducible path.

For Java-specific diagnosis, inspect the full `Caused by` chain; distinguish compile, test, startup, request-time, persistence, and shutdown failures; confirm active Spring profiles and effective configuration; check transaction boundaries and proxy/self-invocation behavior; inspect ORM/SQL evidence before blaming the database; and consider thread state, locks, executors, timeouts, memory pressure, GC, classpath/version conflicts, and resource lifecycle only when the symptom supports them.

Prefer a hypothesis that predicts an observable result. Change one variable, rerun the smallest reproducer, and keep the evidence that falsifies alternatives. If a failure depends on an external internal service, separate local correctness from unavailable-environment evidence.

Never "fix" a symptom by swallowing exceptions, widening timeouts, adding retries, disabling validation, weakening tests, or changing concurrency without proving why that addresses the root cause.
