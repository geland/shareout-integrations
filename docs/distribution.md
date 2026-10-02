# Distribution status

Updated 2026-10-02. A valid package is not a directory approval or a complete host acceptance test.

| Route | Current state | Next requirement |
| --- | --- | --- |
| Claude Code repository marketplace | Package prepared; strict manifest validation passes | Publish repository; verify install and host workflow |
| Codex repository marketplace | Package prepared | Publish repository; verify discovery/install |
| skills.sh / Skills CLI | Compact skill prepared | Verify discovery/install from public repository; directory indexing is telemetry-driven |
| OpenCode | Remote and local connection guidance prepared | Check actual connection; interactive OAuth and publish/update/revoke acceptance |
| Cursor | Portable Agent Plugin and MCP configuration prepared | Host acceptance and marketplace submission |
| VS Code / GitHub Copilot | MCP configuration prepared | Host acceptance |
| Official MCP Registry | Remote server.json prepared | Verify shareout.io namespace and publish; record the returned version |
| ChatGPT / Codex public directory | Package prepared; not submitted | Publisher verification, public policy/support URLs, reviewer access without email codes, recorded demo, host test cases, portal login |
| Claude directory | Package prepared; not submitted | Portal login, linked GitHub, publisher/data handling fields, plugin and connector reviews |
| Smithery | Endpoint eligible for remote submission; not submitted | Publisher account and OAuth compatibility test; its gateway documents CIMD while Shareout currently supports DCR |
| Glama | Hosted connector route identified; not submitted | Submit the remote endpoint as a connector, not as an open-source server implementation |
| PulseMCP | New submissions paused by the directory | Wait for submissions to reopen |
| GitHub public MCP directory | Curated surface investigated; no submission made | Establish the current intake route; registry publication alone does not establish a GitHub listing |

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
