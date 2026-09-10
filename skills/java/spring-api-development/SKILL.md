---
name: spring-api-development
description: Use when creating or changing an HTTP API in a Java repository that actually uses Spring MVC, Spring WebFlux, Spring Boot, Jakarta Validation, or related Spring web infrastructure.
---

# Spring API Development

Use only when repository evidence confirms the relevant Spring stack and version.

**REQUIRED SUB-SKILL:** Use superpowers:test-driven-development for endpoint behavior changes.

Match the project's controller style, DTO conventions, validation annotations, error envelope, exception handling, security configuration, serialization settings, and API documentation mechanism. Keep transport concerns at the boundary: parse/validate request data, delegate business policy to the established service/domain layer, then map the result to the existing response contract.

For Spring Boot 3 / Spring Framework 6 repositories, use Jakarta namespaces when the project does. Do not migrate a legacy `javax.*` project incidentally.

Be explicit about status codes, validation failures, idempotency, pagination, authorization, transaction ownership, and blocking-vs-reactive boundaries where relevant. Never block a reactive request path merely for convenience, and never move a transaction to a controller just to make lazy loading work.

Tests should cover request mapping, validation/security behavior, response/error contracts, and the underlying business behavior at the appropriate scope. Preserve backward compatibility unless the requested change explicitly revises the API contract.
