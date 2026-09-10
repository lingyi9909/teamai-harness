# Java Build and Offline Environment

This harness is intended for Windows-native enterprise environments that may have no public Internet access.

- Do not assume WSL. Commands and instructions must work with Windows 10/11 and the tools already present in the repository/environment.
- For Maven, prefer `mvnw.cmd` when present; otherwise use the internally configured `mvn`. For Gradle, prefer `gradlew.bat` when present.
- Do not add Maven Central, Gradle Plugin Portal, public GitHub package sources, or other public repositories to solve a missing dependency.
- Do not use `curl | sh`, public `git clone`, implicit-download `npx`, or similar network bootstrap steps during normal project work.
- Respect existing internal mirrors, `settings.xml`, Gradle init scripts, repository managers, and corporate certificate configuration.
- If an artifact, plugin, JDK, or tool is unavailable internally, report the exact missing coordinate/version/tool and the failing command. Do not silently change versions or repository configuration to bypass the problem.
- Do not commit machine-specific absolute paths, internal credentials, or developer-local repository settings.
