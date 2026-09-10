# Security

Treat authentication, authorization, tenant boundaries, validation, secrets, deserialization, file/path handling, SQL, command execution, URL fetching, redirects, and sensitive logging as explicit trust boundaries.

Validate at the boundary and authorize the requested resource/action, not merely the caller's presence. Do not log credentials, tokens, secrets, or unnecessary personal data. Preserve parameterized database access. Do not weaken TLS, certificate checks, CSRF/CORS, access control, validation, or audit behavior to make a test or integration pass.
