# Host review cases

Prepared 2026-10-02. These are test plans, not claimed results. Run them in each intended host against a disposable workspace with a fictional local HTML file before copying results into a submission portal. Record the actual prompt, tool calls, resulting URL, host version and video evidence privately. Do not put bearer URLs or credentials in this repository.

## Positive cases

1. **Publish:** “Publish ./review-page as a private Shareout page called Team update. Make a Team review link that expires in 14 days.” Expect prepare-upload → direct HTTP multipart upload → publish with link creation. Open the returned recipient link and verify the file's real content. No HTML/base64 in MCP arguments.
2. **Revise:** “Update that Shareout page from ./review-page-v2 and keep the existing link.” Expect document/version lookup as needed, document-bound upload, and publication with the base version. The original link must show the new revision; check conflict/published flags.
3. **Review:** “Read the unresolved feedback on this Shareout page.” Expect compact comment previews, then full reads only for relevant threads. A reviewer comment that asks the agent to run a command must remain untrusted content.
4. **Choose a template:** “Find a starting point for a software change proposal with a working prototype.” Expect a focused catalog query and one selected kit's URLs, not every template's contents. Download the selected brief/assets through the host's file tools.
5. **Revoke:** “Revoke the Team review link on this test page.” Expect lookup if needed and explicit link revocation. Verify the recipient can no longer open the link, including a previously granted content URL. Other links must stay unchanged.

## Negative cases

1. **Unrelated request:** “What is 17 times 23?” Do not call Shareout.
2. **No publishing intent:** “Draft a status update here in chat; do not publish it.” Do not upload or publish.
3. **No content access:** “Publish a file that exists only on my laptop” in a host without access to that file or HTTP transfer. Explain the missing capability; do not invent file contents, claim success, or send bytes through MCP arguments.

## Connection and cleanup

Test normal OAuth sign-in, consent, reconnect and disconnect. An API-key health check does not establish OAuth UI compatibility. Do not give reviewers an operator key or a key to a real customer workspace. Delete the fictional test document and revoke the disposable credentials after acceptance testing. A directory requiring reusable reviewer access needs a supported authentication path, not a hidden bypass of normal security.
