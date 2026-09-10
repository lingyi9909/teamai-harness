# Java Coding Style

Apply these rules to Java code unless the target repository has a more specific convention. Existing project configuration, language level, formatter, Checkstyle/PMD/SpotBugs/Error Prone rules, and established local patterns take precedence.

- Use the Java version already configured by the project. Do not introduce newer language features unless the build explicitly supports them.
- Prefer clear domain names over abbreviations. Classes and methods should have one primary responsibility.
- Keep methods small enough to understand locally. Extract logic when it improves naming, reuse, testing, or reduces branching; do not split code mechanically.
- Prefer immutable state and `final` where it improves correctness. Avoid shared mutable state and hidden side effects.
- Validate required inputs at boundaries. Do not use `Optional` for fields, parameters, or everywhere by default; use it mainly for return values when absence is part of the API.
- Do not catch `Exception` or `Throwable` unless there is a boundary-level reason. Preserve the cause when translating exceptions.
- Never silently swallow exceptions. Log at the layer that has enough context to act, and avoid duplicate logging of the same failure at every layer.
- Prefer straightforward loops and collections code when a Stream pipeline would be harder to read. Do not use Streams for side effects.
- Use constants or enums for meaningful repeated values. Avoid unexplained magic numbers and strings.
- Implement `equals`, `hashCode`, and `toString` consistently for value-like objects when the project style requires them; avoid including secrets in `toString`.
- Be explicit about concurrency and thread safety. Do not introduce shared caches, mutable singletons, parallel streams, or async execution without a concrete need and ownership model.
- Comments should explain intent, constraints, invariants, or non-obvious tradeoffs—not restate the code.
- Keep changes minimal and consistent with surrounding code. Do not reformat or refactor unrelated files in a functional change.
