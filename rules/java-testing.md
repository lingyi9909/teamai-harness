# Java Testing Rules

Follow the test framework and patterns already used by the repository. Prefer JUnit 5 for new projects, but do not migrate an existing suite as part of unrelated work.

- Add or update tests for changed behavior and bug fixes when the behavior can be exercised automatically.
- Prefer fast unit tests for isolated logic and focused integration tests for framework, database, serialization, transaction, HTTP, or wiring behavior that mocks cannot prove.
- Mock real boundaries, not every collaborator. Avoid tests that only verify implementation call sequences without checking observable behavior.
- Keep tests deterministic: control time, randomness, ordering, locale, timezone, external services, and shared state when they affect the result.
- Name tests so the behavior and condition are clear. Keep Arrange / Act / Assert readable even if the project uses another equivalent style.
- For bug fixes, reproduce the failure in a regression test when practical, then verify the fix.
- Do not weaken, delete, or broadly rewrite existing tests merely to make a change pass unless the old expectation is demonstrably obsolete.
- Run the narrowest relevant tests first, then the repository's normal broader verification before claiming completion.
