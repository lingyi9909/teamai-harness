# Database and persistence

Use the persistence and migration mechanism already established by the repository. Parameterize SQL; never concatenate untrusted input. Preserve transaction and locking semantics deliberately.

Schema changes must consider deploy order, rollback/forward recovery, old/new application coexistence, defaults/nullability, large-table locks, backfill restartability, and index cost. Query changes that can affect scale require evidence appropriate to the real database engine; do not infer production performance from an in-memory substitute.
