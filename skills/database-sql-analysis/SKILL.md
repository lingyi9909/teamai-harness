---
name: database-sql-analysis
description: Use when reviewing or changing SQL, MyBatis/MyBatis-Plus, JPA/Hibernate, JDBC, transactions, indexes, pagination, batch operations, locking, or database performance/correctness. Adapted from GitHub awesome-copilot sql-code-review and sql-optimization for Java backend work.
---

# Database and SQL Analysis

Review database-related changes for correctness first, then security, concurrency, and performance. Never invent schema facts, execution plans, row counts, indexes, or database behavior that are not supported by evidence.

## 1. Establish the database context

Before recommending changes, identify from the repository or supplied evidence:

- database engine and version when available;
- persistence layer: MyBatis, MyBatis-Plus, JPA/Hibernate, JDBC, jOOQ, or raw SQL;
- relevant mapper/repository/entity/query code;
- table definitions, constraints, indexes, migrations, and transaction boundaries when available;
- expected data volume or query plan only if evidence exists.

If the database engine is unknown, avoid engine-specific advice.

## 2. Check correctness and data integrity

Inspect for:

- wrong joins or missing join predicates;
- incorrect null semantics;
- duplicate or missing rows caused by join/cardinality mistakes;
- unsafe update/delete scope;
- incorrect pagination ordering;
- lost precision, timezone, charset, or type-conversion issues;
- missing uniqueness or integrity guarantees;
- ORM mapping mismatches and lazy/eager loading surprises;
- MyBatis dynamic SQL branches that can produce invalid or over-broad SQL.

Correctness outranks micro-optimization.

## 3. Check injection and data exposure

- User-controlled values must use safe parameter binding.
- Treat `${...}`-style textual substitution, string-built SQL, dynamic identifiers, and raw fragments as high-risk until proven safe.
- Do not expose sensitive columns unnecessarily.
- Preserve the application's authorization/resource-ownership checks around data access.

Use `security-review` for a broader trust-boundary audit.

## 4. Check transactions and concurrency

Reason about the full business operation, not only one query:

- transaction boundary and propagation;
- isolation assumptions;
- read-modify-write races;
- optimistic/pessimistic locking;
- deadlock risk and lock ordering;
- idempotency and retries;
- uniqueness races;
- consistency across DB plus MQ/RPC/cache side effects.

Do not claim a race or deadlock without a concrete interleaving or lock path.

## 5. Check performance

Look for evidence-backed risks such as:

- N+1 queries;
- unbounded reads or writes;
- `SELECT *` on wide/hot tables where unnecessary;
- functions/casts on indexed predicates;
- non-sargable predicates;
- deep OFFSET pagination;
- repeated row-by-row operations instead of batching;
- large `IN` lists;
- unnecessary DISTINCT/sorts/aggregations;
- missing or poorly ordered composite indexes;
- over-indexing on write-heavy tables;
- fetching large graphs through ORM relationships.

### Index guidance

Recommend an index only after considering the actual predicate, join, ordering/grouping, selectivity evidence, existing indexes, and write cost. Do not state that an index "will" improve performance without an execution plan or measurement.

### Execution plans

If an `EXPLAIN`/execution plan is available, analyze the real plan. If it is not available, clearly label performance observations as hypotheses to validate rather than pretending a plan was examined.

## 6. Java persistence specifics

### MyBatis / MyBatis-Plus

- inspect XML and annotation SQL together with parameter types;
- verify dynamic `<if>`, `<foreach>`, `<choose>`, and wrapper conditions;
- check result mappings, generated keys, pagination plugins, and batch semantics;
- watch for `${}` versus `#{}` security differences.

### JPA / Hibernate

- inspect fetch strategy, cascade behavior, transaction scope, dirty checking, entity equality, locking, and query count;
- distinguish JPQL/HQL/native SQL behavior;
- avoid "fixing" N+1 by globally switching everything to eager loading.

### JDBC

- use prepared parameters for values;
- verify resource lifecycle and transaction ownership;
- validate batch and generated-key behavior where relevant.

## Output

For each material finding provide:

1. severity/priority;
2. file/query evidence;
3. concrete correctness, security, concurrency, or performance risk;
4. recommended change;
5. verification method (test, query result, execution plan, benchmark, or concurrency proof).

Zero findings is a valid result. Do not manufacture issues to fill a checklist.
