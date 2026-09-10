---
name: security-review
description: Use for focused security review of Java/Spring services or repository changes, including authentication, authorization, injection, SSRF, path/file handling, deserialization, secrets, crypto, sensitive data exposure, dependency risk, and business-logic abuse. Adapted from GitHub awesome-copilot security-review for offline enterprise use.
---

# Security Review

Perform an evidence-backed security review. Reason about reachable trust boundaries and data flow rather than producing a generic checklist. This skill is review-first: do not modify code unless the user explicitly asks for fixes after findings are presented.

## 1. Resolve scope and trust boundaries

Identify the code being reviewed and its externally influenced entry points:

- HTTP/RPC requests, headers, cookies, files, redirects, URLs;
- MQ/events/jobs and deserialized messages;
- database content later reused in a dangerous context;
- configuration and identity/authorization context.

Trace relevant data to sensitive sinks such as database queries, command/process execution, file access, outbound HTTP, template/HTML output, deserialization, privilege checks, secret stores, and administrative operations.

## 2. Authentication and authorization

Check the actual resource/action being protected, not only whether a user is logged in.

Look for:

- missing authentication on sensitive operations;
- BOLA/IDOR/resource-ownership failures;
- role or tenant identifiers trusted from client input;
- privilege escalation paths;
- inconsistent enforcement between endpoints, services, jobs, or internal calls;
- Spring Security method/filter configuration that does not cover the real invocation path.

A suspected authorization issue must include a concrete caller, resource, missing check, and reachable action.

## 3. Injection and unsafe sinks

Review for:

- SQL injection and unsafe MyBatis `${}`/raw fragments;
- command/process injection;
- SSRF and unsafe URL fetching;
- path traversal, archive extraction, and unsafe file upload/download paths;
- template/XSS/header/log injection where applicable;
- XML/XXE and unsafe parsers;
- native Java or polymorphic deserialization of untrusted input.

Confirm whether validation, parameter binding, framework encoding, allow-lists, or middleware already neutralize the path before reporting a finding.

## 4. Secrets and sensitive data

- Never echo discovered credentials or tokens in the report; redact values.
- Check hardcoded credentials, private keys, connection strings, authorization headers, and secrets in logs/config/examples.
- Review whether API responses, exceptions, logs, `toString`, audit events, or metrics expose sensitive data.
- Treat internal hostnames alone as context, not automatically as a vulnerability.

## 5. Cryptography and session/token handling

Check concrete uses of:

- insecure password hashing or security-sensitive MD5/SHA-1 usage;
- predictable random values for tokens/nonces;
- hardcoded keys/IVs/salts;
- disabled TLS or certificate verification;
- token expiry, issuer/audience/signature validation, replay or session fixation issues where relevant.

Do not flag non-security checksums solely because they use MD5/SHA-1; verify purpose first.

## 6. Business logic and concurrency abuse

Consider security-relevant logic bugs such as:

- replay/double-submit/double-spend behavior;
- bypassable state transitions;
- race conditions around limits, inventory, balances, coupons, permissions, or one-time actions;
- mass assignment/over-posting;
- missing rate/attempt controls on high-risk operations.

Report only when a realistic abuse path can be described.

## 7. Dependency risk in an offline environment

Inspect dependency files and local scanner/SBOM/advisory output when available.

- Do not claim a dependency has a current CVE solely from model memory.
- In an offline company network, do not attempt public vulnerability lookups unless the environment explicitly provides access.
- If a local SCA tool, mirrored advisory DB, SBOM scanner, or approved internal service is available, use its evidence and record the source/version/date.
- Otherwise report suspicious/outdated dependencies only as items requiring verified advisory data, not confirmed vulnerabilities.

## 8. Self-verification

For every candidate finding:

1. re-read the complete reachable path;
2. check framework/middleware validation and authorization upstream/downstream;
3. identify attacker-controlled input and the sensitive sink/action;
4. state prerequisites and impact;
5. discard speculative findings that cannot be supported.

## Output

Start with a concise findings summary. For each material finding include:

- severity: Critical / High / Medium / Low;
- confidence: High / Medium / Low;
- file/symbol evidence;
- trust boundary and exploit/abuse path;
- concrete impact;
- recommended remediation;
- verification needed to prove the fix.

Zero findings is valid. Do not invent findings, and do not claim a codebase is "secure" beyond the scope actually reviewed.
