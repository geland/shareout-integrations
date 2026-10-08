# Community distribution audit

Reviewed 2026-10-08 after Greg clarified that Shareout should target community contribution routes. This audits submission mechanisms, not authenticated host behavior or all current review outcomes.

## Default scope

Use community directories, ecosystem galleries, open metadata registries and Shareout's own repository marketplaces. Before submitting, confirm that third-party entries are explicitly invited and distinguish free listings from paid placement. A vendor-owned catalog may accept community entries, but that does not make Shareout an official or verified vendor integration.

Do not open PRs against a host's core implementation or pursue curated first-party marketplaces under a generic distribution request. Explain the destination and proposed contribution before asking Greg to authorize such a route separately. Existing approved submissions are not silently withdrawn.

## Route decisions

| Route | Mechanism and fit | Decision |
| --- | --- | --- |
| Cursor Directory | Community website; detects MCP and skill from Shareout's own public repository | Submitted at https://cursor.directory/plugins/shareout; security scan pending, currently unpublished/hidden |
| Cursor Marketplace | Curated first-party application; declined in owner-shared email | Replaced by Cursor Directory; no appeal or repeat application planned |
| Cline Marketplace | Vendor-maintained catalog explicitly invites new entry PRs; our PR changes only skill metadata and icon | Keep PR #179. It is OPEN, not draft; no changes to Cline's core implementation |
| skills.sh / Skills CLI | Community skill discovery from public repositories and real installations | Keep the existing skill listing; no PR to Vercel core is required |
| Gemini CLI extension gallery | Community extensions indexed from public repositories with the `gemini-cli-extension` topic and root manifest | Keep this route; topic reverified. Indexing and authenticated publishing remain separate checks |
| Official MCP Registry | Open metadata publication under a verified publisher namespace, including remote-only servers | Keep; registry publication is metadata, not first-party endorsement |
| Smithery | Independent MCP directory with its own remote-server publishing flow | Keep existing submission/listing |
| Glama | Independent MCP directory; remote connectors accepted through website and ownership verification | Keep existing connector and isolated health profile |
| Awesome MCP Servers / mcpservers.org | Independent directory explicitly accepts free submissions | Keep the existing submission; no duplicate or paid upgrade |
| PulseMCP | Independent directory; previous intake check found submissions paused | Community fit; do not claim a submission while intake is paused |
| mcp.so | Independent aggregator; previous intake required payment | Community fit in principle; no paid listing authorized or purchased |
| Claude Code repository marketplace | Shareout-maintained public repository that users add themselves | Keep; distinct from Anthropic's curated directory |
| Codex repository marketplace | Shareout-maintained public repository that users add themselves | Keep; distinct from OpenAI's public directory |
| OpenCode, VS Code / Copilot | Host-specific MCP configuration distributed in Shareout's public repository | Keep setup instructions and directory discovery; configuration alone is not a marketplace listing |
| Docker MCP Catalog | Official curated catalog that invites metadata PRs, not the Docker Engine core repository; our submission was withdrawn at Greg's request | PR #5462 reverified CLOSED and unmerged. Do not reopen or seek provider onboarding. No replacement Docker-specific submission identified |
| OpenAI public plugin directory | Explicit third-party plugin intake with identity verification and review; first-party public distribution surface | Greg confirmed retaining the existing application on 2026-10-08. Do not withdraw. Focus new effort on repository marketplaces, skill and MCP directories |
| Vercel Connect | Explicit third-party service intake with review; separate from Vercel Native Marketplace or core source | Greg confirmed retaining the existing API-key application on 2026-10-08. Do not withdraw. Focus new effort on skills.sh and MCP directories |
| Vercel Native Marketplace | Separate provider/integration program; no native listing was submitted | Outside current scope; do not pursue |
| Claude curated directory | First-party review route previously deferred by Greg | Remains deferred; community repository distribution stays available |
| GitHub curated MCP directory | Separate curated surface, not automatic approval from the open MCP Registry | No submission made; do not pursue under community scope |

The OpenAI and Vercel application decisions above concern previously authorized submissions. After clarifying that both intakes welcome third-party submissions, Greg accepted the recommendation to leave the existing applications running and focus new effort on community discovery. This decision does not establish their live review status; no withdrawal has occurred. No new OAuth grant, customer data or test credential was shared in this audit.

## Current verification

The Cursor community form detected the existing hosted MCP and skill, accepted the brand icon and revised listing copy, and navigated to the Shareout listing with a security-scan notice. Cline PR #179 contains only `registry/skills/shareout/entry.json` and `icon.svg`. Docker PR #5462 is closed with `mergedAt: null`. The public repository still has the Gemini gallery topic. Source packaging, installation, directory review and real authenticated workflows remain separate evidence boundaries.

## Primary sources checked

- [Cursor Directory contribution guide](https://github.com/cursor/community-plugins#contributing)
- [Cline catalog contribution guide](https://github.com/cline/marketplace/blob/main/CONTRIBUTING.md)
- [Skills discovery FAQ](https://skills.sh/docs/faq)
- [Gemini extension release and gallery guide](https://geminicli.com/docs/extensions/releasing/)
- [MCP Registry publication guide](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/quickstart.mdx)
- [Smithery publishing](https://smithery.ai/docs/build/publish)
- [Glama server and connector submissions](https://glama.ai/mcp/faq)
- [Awesome MCP Servers free intake](https://mcpservers.org/submit)
- [Docker catalog contribution guide](https://github.com/docker/mcp-registry#contributing-to-the-docker-mcp-registry)
- [OpenAI package and repository marketplaces](https://developers.openai.com/plugins/build/plugins) and [public submission](https://developers.openai.com/plugins/deploy/submission)
- [Vercel Connect service submissions](https://vercel.com/changelog/vercel-connect-service-submissions)
