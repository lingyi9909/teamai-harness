# Build and offline execution

Normal development must work without public network access. Use the repository's Maven wrapper (`mvnw` / `mvnw.cmd`) or Gradle wrapper (`gradlew` / `gradlew.bat`) when present; otherwise use the build tool already provisioned by the environment.

Dependencies and plugins must resolve from the project's configured internal mirror or already available caches. Do not run `curl | sh`, public `git clone`, implicit `npx`/package downloads, or add Maven/Gradle Central/public repositories as a workaround. Do not change repository/proxy settings to bypass the intranet policy.

If a required artifact is absent from the internal mirror, report the exact unresolved coordinate/tool and stop that verification path rather than silently substituting another version.
