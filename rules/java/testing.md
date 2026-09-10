# Testing

Behavior changes require a test that fails for the intended reason before production code is changed, unless the task is purely generated/configuration content and has its own structural validation.

Use the existing Java test stack and the smallest scope that proves the behavior. Mock external or expensive boundaries, not pure domain objects. Tests must assert meaningful outcomes rather than implementation call counts unless the interaction itself is the contract. Run the narrow test first and then the broader repository-required suite.
