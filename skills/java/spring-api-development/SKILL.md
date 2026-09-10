---
name: spring-api-development
description: Use for creating or changing a Spring HTTP API. Detects Spring Boot version and MVC versus WebFlux, preserves project validation/error/security conventions, and verifies the API contract.
---

# Spring API Development

Use only when the repository actually uses Spring HTTP infrastructure.

## 1. Detect the stack

Confirm from dependencies and nearby code:

- Spring Boot/Spring Framework version;
- MVC (`spring-webmvc`) vs WebFlux (`spring-webflux`);
- validation approach;
- exception/error response mapping;
- authentication/authorization mechanism;
- serialization naming/date conventions;
- API documentation/contract mechanism if any.

Never copy MVC blocking patterns into a reactive request path or vice versa.

## 2. Read an analogous endpoint

Find the nearest endpoint with similar behavior and record its conventions:

- route naming and versioning;
- request DTO and validation;
- response DTO/envelope;
- status codes;
- error codes;
- pagination/sorting;
- security annotations/filter behavior;
- service boundary;
- test style.

Reuse these conventions unless the user explicitly requests a new contract.

## 3. Define the external contract first

Specify the observable behavior before implementation:

- method and path;
- request fields/types/requiredness;
- response fields and status;
- validation failures;
- not-found/conflict/permission behavior;
- idempotency expectations for writes;
- backwards compatibility for an existing endpoint.

Do not expose persistence entities directly unless the project intentionally uses that as its API contract.

## 4. Security and resource boundaries

Verify both identity and authorization. For resource-specific operations, trace how the project establishes user/tenant/resource ownership.

Never trust client-supplied userId/tenantId as authorization proof. Check new routes against the actual `SecurityFilterChain`, route matcher, method security or gateway convention.

## 5. Implement through existing architecture

Keep HTTP concerns in the transport boundary and business behavior in the project's established service/domain boundary.

For writes, identify transaction boundary and avoid holding a DB transaction open across slow external calls unless the existing design deliberately requires it.

For WebFlux, do not introduce blocking repository/network calls onto the event loop.

## 6. Test the contract

Use the project's existing testing style. Depending on the behavior this may include:

- controller/slice test for binding, validation and status mapping;
- service unit test for business behavior;
- integration test for security/transaction/serialization;
- contract/OpenAPI regression if the project maintains one.

Test the important invalid/unauthorized path, not only happy path.

## 7. Verify compatibility

Before completion compare old and new API behavior when modifying an existing endpoint:

- removed/renamed fields;
- changed nullability/defaults;
- status/error mapping changes;
- date/number representation;
- ordering/pagination behavior;
- security exposure.

Run fresh relevant tests and build gates after the final edit.
