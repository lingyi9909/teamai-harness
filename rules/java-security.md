# Java Security Rules

Treat all external input and identity/authorization context as untrusted unless the application proves otherwise.

- Never hardcode, print, echo, or commit credentials, tokens, private keys, session identifiers, internal secrets, or sensitive personal data.
- Enforce authorization against the actual requested resource/action, not only authentication or a client-supplied role/owner identifier.
- Use parameterized SQL or the ORM/query framework's safe parameter binding. Never build SQL from untrusted string concatenation.
- Validate and constrain file paths, URLs, redirects, archive entries, and process arguments before use. Guard against traversal, SSRF, open redirects, command injection, and zip-slip style issues where relevant.
- Avoid native Java deserialization of untrusted data and unsafe polymorphic deserialization unless the project has an explicit allow-list design.
- Encode output for its destination context and follow the framework's established XSS/CSRF protections for web applications.
- Use cryptographic APIs already approved by the project. Do not invent encryption schemes or downgrade TLS/certificate validation.
- Avoid logging passwords, tokens, authorization headers, full payment data, or sensitive request/response bodies.
- Security fixes must preserve evidence: identify the trust boundary, the reachable bad behavior, and the verification used to prove the fix.
