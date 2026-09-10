# Spring / Spring Boot

Apply this rule only when the repository uses Spring. Respect the project's Spring and Java versions, configuration style, bean lifecycle, profile strategy, web stack, transaction model, and error contract.

Keep controllers/adapters thin and business policy in the established service/domain layer. Avoid field injection. Do not call transactional/proxied methods through `this` and assume advice will run. Do not add `@Transactional`, retries, caching, async execution, or global exception handlers merely to mask a design or debugging problem. Use Jakarta APIs only when the project's version requires them.
