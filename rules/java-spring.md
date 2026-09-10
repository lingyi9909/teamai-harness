# Java / Spring Rules

Apply only when the project uses Spring or Spring Boot. Follow the project's existing Spring version, MVC/WebFlux choice, persistence stack, error model, and package structure.

- Prefer constructor injection. Avoid adding field injection to new code.
- Keep controllers focused on transport concerns: request binding, validation, authentication context, and response mapping. Put business decisions in the appropriate service/domain layer.
- Use request/response DTOs at external API boundaries when exposing persistence/domain objects would couple the API to internal state.
- Use Bean Validation when the project already uses it, and validate data again where a deeper invariant cannot be expressed at the transport boundary.
- Put transaction boundaries at coherent business-operation boundaries, normally in the service layer. Do not widen transactions without need.
- Remember Spring proxy semantics: self-invocation can bypass proxy-backed behavior such as `@Transactional`, caching, security, retry, and async execution.
- Do not mix blocking work into a reactive WebFlux path without an explicit isolation strategy. Do not convert MVC to WebFlux or vice versa as incidental cleanup.
- Reuse the project's exception handling and error response conventions. Do not expose stack traces, internal SQL, filesystem paths, or implementation details to clients.
- Preserve API compatibility unless the requested change explicitly permits a breaking change.
- Do not upgrade Spring, Java, ORM, database drivers, or build plugins merely to simplify an implementation.
