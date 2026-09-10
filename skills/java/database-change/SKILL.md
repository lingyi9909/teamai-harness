---
name: database-change
description: Use for Java database schema, query, mapping, index, transaction, or migration changes. Requires compatibility, locking/performance, migration, rollback, and integration-test reasoning.
---

# Database Change

Use this skill whenever correctness depends on persistent data behavior, not only when editing SQL files.

## 1. Identify the persistence contract

Read the actual stack and nearby implementation:

- JPA/Hibernate, MyBatis/MyBatis-Plus, JDBC/jOOQ/R2DBC or custom DAO;
- datasource/database type if repository evidence shows it;
- migration mechanism;
- entity/mapper/query definitions;
- transaction boundary;
- relevant schema/index definitions;
- existing integration tests.

Do not infer production database features from a test database alone.

## 2. Classify the change

Mark the task as one or more of:

- query-only;
- mapping-only;
- transaction/concurrency;
- additive schema;
- destructive/contracting schema;
- data backfill/migration;
- index/performance.

The verification and rollout risks differ by class.

## 3. Define data invariants

Write the invariants that must remain true. Examples:

- uniqueness;
- non-negative balance;
- exactly-one active record;
- parent/child consistency;
- tenant isolation;
- ordering/version monotonicity;
- idempotent processing.

Use database constraints for invariants that must survive concurrent writers when appropriate; application checks alone can race.

## 4. Design safe schema evolution

Prefer backwards-compatible expansion before contraction:

```text
expand schema
-> deploy compatible code
-> migrate/backfill
-> switch reads/writes
-> verify
-> contract old schema later
```

For large tables consider lock duration, online DDL capability, index build cost, backfill batching and observability. Do not claim an operation is online/lock-free without database/version evidence.

## 5. Review query behavior

Check:

- bound parameters;
- result cardinality;
- null and empty-list semantics;
- join multiplication;
- N+1 behavior;
- pagination/sort determinism;
- expected index access path;
- batching and round trips.

Only report an execution plan if one was actually obtained from an appropriate environment.

## 6. Review transaction/concurrency behavior

Identify:

- start/end of transaction;
- rows/resources that can be locked;
- isolation assumptions;
- optimistic/pessimistic lock behavior;
- retry policy and idempotency;
- external calls inside the transaction;
- multi-instance race conditions.

Do not use JVM-local locks as a substitute for cross-instance data concurrency control.

## 7. Test at the right level

If the change depends on SQL, ORM mapping, constraints, migration, isolation or transaction semantics, use the project's real integration testing mechanism when available. A Mockito test of the repository interface is not sufficient proof.

Add regression coverage for the concrete invariant or failure being changed.

## 8. Rollback and completion

State whether rollback means:

- code rollback only;
- code + compatible schema rollback;
- forward-fix because data migration is irreversible.

Run fresh affected integration tests/build gates. If no representative database environment exists, clearly separate code-level PASS from unverified production-database behavior.
