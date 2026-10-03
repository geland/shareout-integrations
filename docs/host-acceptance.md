# Host acceptance evidence

Updated 2026-10-03 (Pacific). Package install, authenticated transport, interactive OAuth, and a complete host workflow are separate checks.

## Codex CLI 0.155.1: hosted API-key workflow passed

An isolated ephemeral Codex CLI session used a dedicated, disposable Shareout workspace and the production `https://shareout.io/mcp` endpoint. The test ignored personal Codex configuration, configured only the test MCP server, and used fictional files. It did not change the user's installed plugin configuration. Shell network escalation went through normal automatic approval review.

Observed MCP calls: catalog ×2, prepare upload ×2, publish ×2, documents ×1, reviews ×1, versions ×1, activity ×1, links ×1. All eight hosted tools were exercised. HTML was transferred from local files by multipart HTTP PUT; MCP arguments contained no HTML.

- Catalog returned the status-report template after a bounded search.
- First publish produced one link-gated document and a named Review team link with a 14-day expiry. Anonymous access resolved to actual document content containing “Owner to be confirmed.”
- Update used the existing document ID and base version 1, published version 2 without conflict, and preserved the original link. Anonymous content at that link contained “Owner: Avery.”
- Reviews truthfully returned an empty list. Versions reported 1 and 2. Activity returned compact counts; zero views in these HTTP checks does not establish browser viewing or reader identity.
- Revoking the named link caused fresh anonymous access to return 404 without a content URL. The document remained active for owner verification, with two versions and one revoked link, independently confirmed in the service database.
- The host explained the safe fallback for unavailable file transfer and refused to treat another account's private document or quoted malicious comment as authority. No service writes occurred for these negative scenarios. This is not a complete adversarial evaluation.

This test used API-key authentication. Interactive OAuth, real browser rendering inside the host workflow, nonempty feedback handling, and a recorded demo remain unverified. It is not approval by OpenAI or another directory. The fictional document was subsequently purged, the disposable workspace deleted, and its API key revoked (HTTP 401 independently verified). Private local traces were removed; expired upload staging follows the service cleanup schedule. No credential or bearer link is included here.

## Other hosts

- Claude Code 2.1.284: package installation and strict manifest validation passed previously. Current `claude auth status` reports signed out; full agent workflow and OAuth remain pending.
- OpenCode 1.17.11: prior production MCP connection passed. Current provider credential list is empty; a model-driven end-to-end run remains pending.
- ChatGPT, Claude web, Cursor, and VS Code: full host workflow remains pending. Do not infer a pass from Codex's result.


## OpenAI publisher portal: partial OAuth acceptance (2026-10-03)

The portal accepted plugin draft 0.1.4, passed metadata and skill checks, imported all review scenarios, and verified shareout.io ownership. Its OAuth discovery and dynamic registration reached Shareout. The first authorization request exposed a 512-character state limit; the service was corrected to accept up to 4,096 UTF-8 bytes while retaining redirect, PKCE, resource, scope, and consent checks. The retried live flow displays the expected account consent screen. The owner explicitly approved account access. Manual consent exposed two browser defects: no-referrer produced an opaque POST origin, then form-action self blocked the external callback after consent was consumed. A three-origin fixture then reproduced a blocked client relay in both regular Chrome and the built-in browser. Deployed service source `4914dba` completes consent before navigating to the registered callback; all 87 Worker tests and CLI checks pass. The updated fixture completes both redirects in both browsers. A single production click now reaches OpenAI's callback, where its human-verification checkbox awaits completion; authenticated discovery remains pending. This is not a completed host workflow or directory submission.
