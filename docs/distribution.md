# Distribution status

Updated 2026-10-05. A valid package is not a directory approval or a complete host acceptance test.

| Route | Current state | Next requirement |
| --- | --- | --- |
| Claude Code repository marketplace | Published; Claude Code 2.1.284 installed from GitHub; strict validation passes | Interactive OAuth and publish/update/revoke acceptance |
| Codex repository marketplace | Published; install check and full hosted API-key workflow passed in Codex 0.155.1 | Interactive OAuth and recorded browser/host demonstration |
| skills.sh / Skills CLI | Published; Skills CLI discovered and installed the skill for OpenCode in a temporary project | Directory indexing is telemetry-driven; test telemetry was disabled |
| OpenCode | Configuration published; OpenCode 1.17.11 connected to production with a disposable API key | Interactive OAuth and publish/update/revoke acceptance |
| Cursor | Portable Agent Plugin and MCP configuration prepared | Host acceptance and publisher-application sign-in |
| VS Code / GitHub Copilot | MCP configuration prepared | Host acceptance |
| Official MCP Registry | Published and independently verified: `io.shareout/shareout` version `0.6.0` | Keep metadata aligned with releases |
| ChatGPT / Codex public directory | 0.1.4 draft uploaded; identity/domain verified; metadata and skill checks passed | Reviewer access saved; native ChatGPT publication passed; finish remaining cases, recording and draft refresh |
| Claude directory | Deferred by the owner on 2026-10-02; existing repository package remains available | Revisit if a paid publisher account and product fit justify it |
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
- Production policy/support pages, connection guide and agent discovery file verified live. Worker `908eb9e8-3bf0-4688-bb33-4d637dbcca27` serves source `1b26a08` at 100%. HTML matches source after excluding Cloudflare’s injected analytics beacon; the privacy policy explicitly discloses it. Typecheck, 82 Worker tests and exact-source CI passed; post-deploy MCP initialization and all eight tool definitions returned successfully.
- OpenAI and Claude publisher sign-ins completed. OpenAI confirmed the individual developer identity and accepted package 0.1.3 as a draft on 2026-10-03. The replacement 0.1.4 draft passes metadata and skill checks, its domain is verified, and all five positive/three negative cases imported. The live OAuth flow now reaches Shareout account consent; the discovered relay-state length incompatibility was fixed and deployed with 85 passing Worker tests. The owner approved consent. Manual clicks exposed native-form origin and callback CSP defects. A three-origin fixture reproduced the remaining client relay failure in both regular Chrome and the built-in browser. The production correction passes 87 Worker tests and both browser fixtures; one consent click now reaches OpenAI's callback. The owner completed OpenAI's human-verification check; the portal now shows Authorized, Domain verified, and all eight tools. Three tools have generic further-review findings. Reviewer access, running and recording the scenarios, and final submission remain incomplete. Claude directory submission is deferred at the owner’s request; the signed-in account is Free and the portal requires a paid plan. Cursor, Smithery and Glama still need their publisher account flows. The OpenAI draft is not a submitted or approved listing.

## Host acceptance procedure

Use a disposable Shareout workspace and fictional HTML, never a customer's document. In each host: connect using its normal UI, list tools, publish via file upload, open the recipient link, update with the starting base version, verify the same link shows the revision, revoke the test link, and remove the test data. Record the host version and outcome. Validate error handling when the host has no file-transfer capability. Existing service-level OAuth/tool tests do not replace these host checks.

## Listing copy

**Name:** Shareout

**Publisher:** Greg Eland

**Support email:** hello@gregeland.com

**Support:** https://shareout.io/support

**Privacy:** https://shareout.io/privacy

**Terms:** https://shareout.io/terms

**Short description:** Share what your agent makes

**Description:** Publish HTML reports, proposals, walkthroughs, and interactive pages. Share a link, collect feedback, and publish revisions at the same address. Named links can expire or be revoked. A Shareout account is required. Hosted publishing accepts native ChatGPT HTML attachments or direct HTTP transfer; local MCP and the standalone CLI read files directly from disk.

**Endpoint:** https://shareout.io/mcp

**Website:** https://shareout.io

**Docs:** https://shareout.io/agents

**Live example:** https://shareout.io/d/cujufgdheurd

The publisher and support contact were confirmed on 2026-10-02. Cloudflare confirms the support address has an enabled forwarding rule and a verified destination. Public policies are live. Publisher verification is confirmed; MCP authorization/discovery and private reviewer credentials are now complete. The actual host walkthrough/recording and generic tool review findings remain before submission. Do not place private review credentials in this repository or ZIP. The live example is not a substitute for a recorded host demo.

The 0.1.3 package adds the public policy URLs and five positive/three negative scenarios. Fictional first/revised HTML files live in `examples/review/`; see [submission kit](submission-kit.md) for data-handling answers and remaining gates. Public policy URLs were verified after deployment. Cases are prepared, not a claim that every host has passed them.

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


### Review readiness update — 2026-10-03

Service MCP 0.6.1 and isolated reviewer demo access are live. OpenAI's private reviewer fields were saved successfully, and the new tool definitions were rescanned. Three generic further-review notices remain. ChatGPT host sign-in and the actual recorded review workflow are still needed; no final submission or approval is claimed. The integration package remains 0.1.4 and the official MCP Registry listing remains 0.6.0 until a separate registry update.

Package 0.1.5 prepares native ChatGPT file-input guidance for deployed MCP 0.6.2. Native attachment publication and anonymous exact-byte recipient access passed; see [host acceptance](host-acceptance.md). The portal remains on draft 0.1.4 until a replacement package is uploaded; no directory approval is implied.
