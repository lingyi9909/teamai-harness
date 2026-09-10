---
name: database-change
description: Use when Java work changes a relational schema, SQL, migration, ORM mapping, transaction boundary, index, query plan, data backfill, or persistence compatibility contract.
---

# Database Change

First identify the repository's actual persistence technology and migration authority: Flyway, Liquibase, project SQL, JPA/Hibernate, MyBatis/MyBatis-Plus, JDBC, or another established mechanism. Do not introduce a second migration system.

**REQUIRED SUB-SKILL:** Use superpowers:test-driven-development for behavior changes.
**REQUIRED SUB-SKILL:** Use superpowers:verification-before-completion before completion claims.

For schema changes, reason about deploy order and mixed-version compatibility. Prefer additive expand/migrate/contract sequences when old and new application versions may overlap. Specify null/default semantics deliberately, protect large-table migrations from unsafe full rewrites or long locks, and make backfills restartable when scale requires it.

For query changes, preserve parameterization, verify cardinality assumptions, indexes, ordering and pagination semantics, and inspect the plan or representative evidence when performance is material. For ORM changes, watch fetch strategy, N+1 behavior, cascades, orphan removal, dirty checking, optimistic locking, and transaction boundaries.

Never concatenate untrusted input into SQL. Never claim a migration is safe from unit tests alone when its safety depends on the real database engine or production-scale data; record the missing environment evidence explicitly.
