# Distribution status

Updated 2026-10-02. A valid package is not a directory approval or a complete host acceptance test.

| Route | Current state | Next requirement |
| --- | --- | --- |
| Claude Code repository marketplace | Published; Claude Code 2.1.284 installed from GitHub; strict validation passes | Interactive OAuth and publish/update/revoke acceptance |
| Codex repository marketplace | Published; Codex 0.155.1 discovered and installed the package | Interactive OAuth and publish/update/revoke acceptance |
| skills.sh / Skills CLI | Published; Skills CLI discovered and installed the skill for OpenCode in a temporary project | Directory indexing is telemetry-driven; test telemetry was disabled |
| OpenCode | Configuration published; OpenCode 1.17.11 connected to production with a disposable API key | Interactive OAuth and publish/update/revoke acceptance |
| Cursor | Portable Agent Plugin and MCP configuration prepared | Host acceptance and publisher-application sign-in |
| VS Code / GitHub Copilot | MCP configuration prepared | Host acceptance |
| Official MCP Registry | Published and independently verified: `io.shareout/shareout` version `0.6.0` | Keep metadata aligned with releases |
| ChatGPT / Codex public directory | Package prepared; not submitted | Publisher verification, public policy/support URLs, reviewer access without email codes, recorded demo, host test cases, portal login |
| Claude directory | Package prepared; not submitted | Portal login, linked GitHub, publisher/data handling fields, plugin and connector reviews |
| Smithery | Endpoint eligible for remote submission; not submitted | Publisher sign-in and OAuth compatibility test; its gateway documents CIMD while Shareout currently supports DCR |
| Glama | Hosted connector route identified; not submitted | Sign-in/account required; submit the remote endpoint as a connector, not as an open-source server implementation |
| PulseMCP | New submissions paused by the directory | Wait for submissions to reopen |
| GitHub public MCP directory | Curated surface investigated; no submission made | Establish the current intake route; registry publication alone does not establish a GitHub listing |

## Verified evidence

- Public source: [geland/shareout-integrations](https://github.com/geland/shareout-integrations). Initial package CI [37078527842](https://github.com/geland/shareout-integrations/actions/runs/37078527842) passed.
- [Official Registry version 0.6.0](https://registry.modelcontextprotocol.io/v0.1/servers/io.shareout%2Fshareout/versions/0.6.0): published through shareout.io domain verification, then independently read back. This is not endorsement by the registry or an automatic curated listing elsewhere.
- Claude Code and Codex installation checks used isolated/local test scopes. The temporary Codex installation was removed afterward. Claude Code's separate MCP health check stopped at its project trust approval; it did not establish a connected session.
- Skills CLI discovery and project-scoped OpenCode installation passed with test telemetry disabled. No claim of skills.sh indexing or ranking.
- OpenCode's actual MCP connection returned `connected`. Its disposable empty workspace was deleted and key revoked. This check used API-key authentication, not the OAuth sign-in UI.
- Production connection guide and agent discovery file link to the package. Worker `99c2e5db-a395-4402-a337-50cbff158c51` serves source `13d2ff4` at 100%; exact assets and registry proof verified. Service validation: typecheck, 82 Worker tests and source CI passed.
- OpenAI, Claude, Cursor and Smithery portals require sign-in in the current browser. Glama's Add Server opens account registration/sign-in. None has received a curated submission.

## Host acceptance procedure

Use a disposable Shareout workspace and fictional HTML, never a customer's document. In each host: connect using its normal UI, list tools, publish via file upload, open the recipient link, update with the starting base version, verify the same link shows the revision, revoke the test link, and remove the test data. Record the host version and outcome. Validate error handling when the host has no file-transfer capability. Existing service-level OAuth/tool tests do not replace these host checks.

## Listing copy

**Name:** Shareout

**Short description:** Share agent-made work with people.

**Description:** Publish HTML reports, proposals, walkthroughs, and interactive pages. Share a link, collect feedback, and publish revisions at the same address. Named links can expire or be revoked. A Shareout account is required. Hosted publishing needs a host that can transfer local files over HTTP; local MCP and the standalone CLI read files directly from disk.

**Endpoint:** https://shareout.io/mcp

**Website:** https://shareout.io

**Docs:** https://shareout.io/agents

**Live example:** https://shareout.io/d/cujufgdheurd

Publisher verification, support contact, public policies, and reviewer credentials must be accurate before submission. Do not place private review credentials in this repository or ZIP. The live example is not a substitute for a recorded host demo.

## Sources

- [OpenAI packaging](https://developers.openai.com/plugins/build/plugins) and [submission](https://developers.openai.com/plugins/deploy/submission)
- [Claude plugin submission](https://claude.com/docs/plugins/submit) and [manifest reference](https://code.claude.com/docs/en/plugins-reference)
- [Skills CLI](https://skills.sh/docs/cli) and [directory discovery](https://skills.sh/docs/faq)
- [OpenCode MCP](https://opencode.ai/docs/mcp-servers/)
- [Cursor plugins](https://prod.cursor.com/docs/plugins)
- [Official MCP Registry](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/quickstart.mdx)
- [Smithery publishing](https://smithery.ai/docs/build/publish)
- [Glama connector submissions](https://glama.ai/mcp/faq)
- [PulseMCP submission notice](https://www.pulsemcp.com/)
