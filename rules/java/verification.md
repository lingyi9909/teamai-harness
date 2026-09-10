# Verification

Completion claims require fresh evidence from the current worktree/commit. Run the repository's narrow relevant test first, then the owning module's compile/test/static-analysis gates, then any broader gate required by local instructions.

Report the exact commands and results. A previous run, another commit, IDE green state, or reasoning that a change "should compile" is not evidence. If an integration, database, internal service, or environment-dependent gate cannot run, identify that gap explicitly and do not claim it passed.
