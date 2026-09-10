---
name: codebase-reconnaissance
description: Use when entering an unfamiliar repository or when a requested change spans multiple modules and you need a reliable task-scoped map before editing. Do not use for tiny, obvious, single-file changes. Inspired by GitHub awesome-copilot acquire-codebase-knowledge, but intentionally lighter and non-document-generating.
---

# Codebase Reconnaissance

Build the smallest evidence-backed map needed to make the requested change safely. Do not create repository documentation unless the user explicitly asks for it.

## Workflow

1. **Establish project facts**
   - Inspect repository instructions first: `README*`, `AGENTS.md`, contributing docs, build files, formatter/linter config, and local rules.
   - Identify Java/JDK level, Maven or Gradle, Spring/Spring Boot version if present, modules, test framework, persistence stack, and major integrations.
   - Existing repository configuration and conventions override generic guidance.

2. **Locate the task entry point**
   - Start from the user's requested behavior, error, endpoint, job, consumer, command, or class name.
   - Find the production entry point and trace only the relevant call path.
   - Typical Java path: Controller/Consumer/Job -> Service -> Domain -> Repository/Mapper -> DB/RPC/MQ.

3. **Map the change surface**
   - List the files/modules that actually participate in the behavior.
   - Identify nearby tests and test fixtures.
   - Identify configuration, feature flags, schema, API contracts, messages, or generated code that constrain the change.
   - Note transaction, cache, retry, async, security, and framework proxy boundaries when relevant.

4. **Separate evidence from assumptions**
   - Every non-trivial claim must point to a concrete file, symbol, build output, or repository fact.
   - Mark unknowns explicitly instead of guessing.
   - Do not infer architecture from names alone.

5. **Produce a compact working map**
   - Stack/build facts.
   - Relevant modules and entry point.
   - Call/data flow.
   - Tests and verification commands.
   - Constraints/risks that affect the requested task.
   - Open questions only when they truly block implementation.

6. **Hand off to the implementation workflow**
   - Once the task surface is understood, continue with the relevant Superpowers workflow such as brainstorming, TDD, systematic debugging, or plan execution.
   - Do not keep expanding reconnaissance after you have enough evidence to act.

## Java / Enterprise Notes

- Prefer `mvnw.cmd` or `gradlew.bat` on Windows when present.
- Do not assume WSL or public Internet access.
- For multi-module Maven/Gradle repositories, identify the owning module before running broad searches or builds.
- Distinguish generated code from source code and do not learn coding conventions from generated output.
- Treat README/design docs as intent; confirm current behavior in code and configuration.
- For dependency or startup failures discovered during reconnaissance, switch to `java-build-diagnostics` rather than turning this skill into a debugging workflow.

## Stop Condition

Stop reconnaissance when you can answer, with evidence:

- Where does the requested behavior enter the system?
- Which files/modules own it?
- What is the relevant call/data flow?
- Which tests prove the behavior?
- What project-specific constraints must the implementation preserve?
