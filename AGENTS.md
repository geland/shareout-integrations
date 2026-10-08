# Shareout integration packages

This is the public distribution repository, not the service implementation.

- Keep skills short and load https://shareout.io/skill.md or guidelines.md only when needed. Do not duplicate the full tool catalog or templates.
- Hosted MCP must hand file bytes to an HTTP upload, never through tool arguments. Local MCP reads disk via the standalone CLI.
- Keep credentials and customer content out of this repository, packages, test fixtures and logs.
- Preserve host-specific config shapes. Validate the portable manifests with the official schemas, plus Claude manifests with `claude plugin validate --strict`.
- Increment the plugin version across its manifests when publishing changes. MCP server versions in server.json follow the released service, not this package.
- Package only the explicit allowlist in scripts/package.py. No install hooks, shell scripts or automatic config edits belong in the plugin.
- Record actual host checks and submission status in docs/distribution.md. Installable, submitted, approved and indexed are different states.

- Distribution defaults to community directories, ecosystem galleries, open metadata registries and this repository's own marketplaces. Verify third-party intake before submitting. Do not infer authorization for curated first-party applications or host core-repository changes. See docs/distribution-community-audit.md; Docker remains withdrawn.
