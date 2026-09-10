# Superpowers runtime mapping for OpenCode

This TeamAI-managed repository vendors Superpowers as ordinary skills. OpenCode must use its native skill mechanism rather than the upstream Superpowers plugin.

At the start of a task, load `using-superpowers` when it is available, then follow every applicable skill before acting. When a vendored skill names `superpowers:<name>`, resolve that reference to the TeamAI-synced native skill `<name>`.

Map generic Superpowers actions to OpenCode capabilities as follows: todo creation/update → `todowrite`; general subagent dispatch → `task`; skill invocation → `skill`; file read → `read`; file edits → `apply_patch`; shell execution → `bash`; repository search → `grep` / `glob`; URL retrieval → `webfetch` only when that URL is allowed by the current intranet environment.

Do not install or generate the upstream `.opencode/plugins/superpowers.js` from this team repository. TeamAI owns resource distribution and OpenCode rule activation here.
