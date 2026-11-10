# CorpusIQ

> **"Accelerate your business. All your tools in one place."**

| | |
|---|---|
| **Website** | https://www.corpusiq.io |
| **Docs** | https://www.corpusiq.io/developers |
| **GitHub** | https://github.com/CorpusIQ/corpusiq-docs |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/CorpusIQ/corpusiq-docs?style=social)](https://github.com/CorpusIQ/corpusiq-docs) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **License** | Platform API declared proprietary (`LicenseRef-CorpusIQ-Proprietary`) in [openapi.json](https://www.corpusiq.io/openapi.json). MCP server source is private. `corpusiq-docs` has no license file |
| **Operator** | CorpusIQ LLC, as named on https://www.corpusiq.io/developers |
| **Disclosure** | Proposed by [Ben-Home](https://github.com/Ben-Home) in [#146](https://github.com/haoruilee/awesome-agent-native-services/issues/146). That issue does not state a financial interest |
| **Verified at** | 2026-11-10 |
| **Latest-month signal** | [Homepage](https://www.corpusiq.io/) (apex [https://corpusiq.io](https://corpusiq.io) returns 308), [llms.txt](https://www.corpusiq.io/llms.txt), [developers](https://www.corpusiq.io/developers), [pricing.md](https://www.corpusiq.io/pricing.md) and [openapi.json](https://www.corpusiq.io/openapi.json) HTTP 200 on 2026-11-10. `POST https://mcp2.corpusiq.io/mcp` `initialize` returned `serverInfo.name` `multi-source-mcp` version `1.0.0`. Unauthenticated `tools/list` returned 121 tools. Unauthenticated `tools/call` returned HTTP 401. Registry `io.corpusiq/multi-source-mcp` `1.0.3` is latest. `corpusiq-docs` last push 2026-11-10, 28 stars, no license file |

---

## Official Website

https://www.corpusiq.io

`https://corpusiq.io` responds with HTTP 308 to `https://www.corpusiq.io/`. The markdown homepage (HTTP 200 with `Accept: text/markdown`, last updated 2026-10-26) opens with the tagline above and describes CorpusIQ as an AI intelligence layer that gives AI assistants and AI agents governed access to live business data through one connection. The HTML title is "Business Answers From Your Data With Sources | CorpusIQ" and the HTML H1 is "AI answers on your data. See where every number comes from."

The same markdown page says the service works inside ChatGPT, Claude, and Perplexity, and with any MCP-capable agent or self-hosted model. "Self-hosted" there refers to the caller's model.

---

## Official Repo

https://github.com/CorpusIQ/corpusiq-docs

Public docs and the agent install note (`llms-install.md`). The GitHub org is https://github.com/CorpusIQ. On 2026-11-10 the docs repo had 28 stars. Its README badge says MIT and links to `LICENSE`. That file returns HTTP 404, and a recursive tree listing contains no `LICENSE`, `LICENCE`, or `COPYING` file.

The MCP server source is not in that repo. https://github.com/CorpusIQ/mcp-manifest states that it holds metadata only and that the server source is not public. `server.json` there is version `1.0.3`, name `io.corpusiq/multi-source-mcp`, remote `https://mcp2.corpusiq.io/mcp`. The official registry marks `1.0.3` as latest: https://registry.modelcontextprotocol.io/v0.1/servers?search=corpusiq

Issue #146 (2026-09-15) called CorpusIQ an open-source, self-hostable server with 36 connectors. Current public docs describe a hosted remote server, no local package, and 40+ connectors. No public self-host guide for the server was found. Enterprise pricing mentions custom deployment and says to contact sales.

Two other public repos are MIT and are not the server: the Claude skills bundle https://github.com/CorpusIQ/corpusiq-claude-skills and the n8n node source https://github.com/CorpusIQ/n8n-nodes-corpusiq. `n8n-nodes-corpusiq` was not on the npm registry (HTTP 404 on 2026-11-10), and that repo's checklist still leaves `npm publish` unchecked. https://github.com/CorpusIQ/runbook-spec is a separate MIT spec, not the server.

Rendered docs also live at https://docs.corpusiq.io (HTTP 200).

---

## How to Use (Agent Onboarding)

**Interaction pattern:** MCP

**One-sentence instruction:** Add the hosted MCP server, then complete the user's OAuth sign-in.

```
claude mcp add --transport http corpusiq https://mcp2.corpusiq.io/mcp
```

The install note for agents is https://github.com/CorpusIQ/corpusiq-docs/blob/main/llms-install.md (raw: https://raw.githubusercontent.com/CorpusIQ/corpusiq-docs/main/llms-install.md). It registers the remote server in Claude Code, Cursor, VS Code, Gemini CLI, and other Streamable HTTP clients. The user signs in through the browser or the device-code flow. There is no API key in that guide.

`https://www.corpusiq.io/skill.md` and `https://www.corpusiq.io/SKILL.md` returned HTTP 404 on 2026-11-10. Reading https://www.corpusiq.io/llms.txt indexes the site. It does not create an account.

---

## Agent Skills

**Status:** ✅ Available

The product also uses "skills" for server-side workflows (`list_skills`, `invoke_skill`, and `featured_*` tools). Those are MCP tools, not `SKILL.md` files. The installable Agent Skills are the MIT bundle in `CorpusIQ/corpusiq-claude-skills`. That README does not document `npx skills add`.

```text
/plugin marketplace add CorpusIQ/corpusiq-claude-skills
/plugin install corpusiq-truth-layer@corpusiq
```

Other agents copy a folder from `plugins/*/skills/` into their skills directory. The bundle requires a CorpusIQ account and the remote MCP connector.

| Skill | What It Teaches the Agent |
|---|---|
| `corpusiq-truth-layer` | Business numbers must come from a connected source and carry a citation, or be labelled unknown |
| `corpusiq-investor-pack` | Pitch and investor text whose traction figures come from the connected systems |
| `corpusiq-competitor-scout` | Compare a competitor's public claims with measured numbers from connected sources |
| `corpusiq-monthly-review` | One monthly close across billing, accounting, store, and analytics, with one definition per metric |

Search community skills: `npx clawhub@latest search corpusiq`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | Server source is private. Manifest: https://github.com/CorpusIQ/mcp-manifest (`io.corpusiq/multi-source-mcp`, version `1.0.3`). Install examples live in https://github.com/CorpusIQ/corpusiq-docs |
| **Endpoint** | `https://mcp2.corpusiq.io/mcp` |
| **Transport** | Streamable HTTP. `initialize` on 2026-11-10 selected protocol `2025-03-26` and returned `serverInfo` `multi-source-mcp` `1.0.0`. A bare GET returned HTTP 406, body `Accept header must include text/event-stream` |
| **Auth** | Live metadata: authorization code, refresh token, and device code; PKCE `S256`; dynamic client registration; scopes `openid`, `email`, `profile`. Protected resource: https://mcp2.corpusiq.io/.well-known/oauth-protected-resource. Authorization server: https://mcp2.corpusiq.io/.well-known/oauth-authorization-server. JWKS: https://api.corpusiq.app/.well-known/jwks.json (HTTP 200). The developers page calls this OAuth 2.0. `llms-install.md` calls it OAuth 2.1. Unauthenticated `tools/list` returned HTTP 200 and 121 tools. Unauthenticated `tools/call` of `get_connector_status` returned HTTP 401 `Authentication required` with `WWW-Authenticate: Bearer` |
| **Tools** | Instructions returned by `initialize` name `ask_corpusiq`, `resolve_connector`, `select_runbook`, `list_skills`, `invoke_skill`, `get_connector_status`, and `featured_*` tools. Of the 121 names from `tools/list`, 105 set `readOnlyHint` true. Sixteen do not, including canonical-fact and metric writes, connector enable/disable, `reset_connector_token`, and `logout_all` |
| **Compatible Clients** | Claude, Claude Code, ChatGPT, Cursor, VS Code, Gemini CLI, Cline, and other remote MCP clients named in `llms-install.md` and on the developers page |

---

## What It Does

CorpusIQ is a hosted MCP server that answers questions from business systems the user has connected. The current site says 40+ connectors, including Stripe, Google Analytics 4, and Shopify, and lists others such as QuickBooks, HubSpot, ads platforms, mail, files, and databases. Issue #146's figure of 36 is older than that copy. The connectors page also says "50+ more coming." This entry does not treat any of those phrases as a hand-counted inventory.

The user authorizes each source. External retrieval tools are documented as read-only against those vendor systems: they do not create, update, or delete a vendor record, send a message, or move money. Separate control-plane tools write CorpusIQ's own configuration, such as enabling a connector, resetting a token, or storing a canonical fact. Several of those writes return a `pending_write_id` and ask for `canonical_pending_commit` after the user confirms.

`ask_corpusiq` is the server's route for an executive financial snapshot. It selects a read-only runbook and returns an answer, evidence, warnings, and an execution receipt. Broad questions go through `resolve_connector`. A matching `featured_*` tool returns a `skill_body` runbook for the agent to execute. The site also advertises 150+ pre-built expert workflows. Plans on https://www.corpusiq.io/pricing.md (last updated 2026-11-10) are Solo $29.95, Team $109.95, and Business $189.95 per month, with a 30-day trial and no card required to start.

https://www.corpusiq.io/docs/api/ still documents `POST https://api.corpusiq.io/v1/query` and `POST /v1/deep_search`. An unauthenticated POST to `https://api.corpusiq.io/v1/query` on 2026-11-10 returned HTTP 404 with Vercel's `DEPLOYMENT_NOT_FOUND`. The live machine contract that responded is the MCP host. Its public description is OpenAPI 3.1 at https://www.corpusiq.io/openapi.json, titled "CorpusIQ Platform API", server `https://mcp2.corpusiq.io`, covering OAuth discovery, the device flow, `POST /mcp`, and `GET /api/v1/usage/public-counter`.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Markdown homepage: "Gives AI assistants and AI agents governed access to live business data through one connection" and "any MCP-capable agent or self-hosted model." — https://www.corpusiq.io. `llms-install.md`: "This file is written for AI agents and coding assistants … that install MCP servers by reading a repository." The docs README lists "AI agents - 24/7 autonomous agents querying live business data via MCP protocol" among its users. ChatGPT, Claude, and Perplexity are also first-class clients |
| **Agent-specific primitive** | `initialize` tells the client to call `ask_corpusiq` for an executive financial snapshot. That tool runs a fixed read-only allowlist and returns the answer, evidence, warnings, and an execution receipt. `featured_*` tools and `resolve_connector` return a `skill_body` runbook the agent executes. A tool result may include `correction.tool` and `correction.arguments` for an immediate retry. When output includes an attribution footer, the instructions say to append that Markdown link unchanged |
| **Autonomy-compatible control plane** | The developers page says a long-running agent refreshes its access token instead of prompting a person every hour, and that external retrieval cannot modify vendor records. Connecting a source and the first OAuth approval are person steps. After that, retrieval uses the bearer token. Canonical fact, decision, metric, and source-of-truth writes are annotated to stop at a `pending_write_id` until `canonical_pending_commit`. `disable_connector`, `reset_connector_token`, and `logout_all` are separate control-plane tools |
| **M2M integration surface** | Remote MCP, OAuth metadata, OpenAPI 3.1 at https://www.corpusiq.io/openapi.json, https://www.corpusiq.io/llms.txt, and `llms-install.md`. The developers page says there is no CorpusIQ SDK to install |
| **Identity / delegation** | Developers page: "Every tool call carries the identity of the authorized account. There is no shared service account and no impersonation path." Live scopes are `openid`, `email`, and `profile`. Each connector is authorized by that user. This is the user's CorpusIQ account, not a separate agent principal. Operational query text, per-user tool-call metadata, and bounded outcome summaries may be kept for up to 30 days |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`ask_corpusiq`** | Deterministic read-only runbook for supported questions, including an executive financial snapshot. Returns the answer, evidence, warnings, and an execution receipt |
| **`resolve_connector`** | Routes a broad cross-source question to a CorpusIQ skill runbook. The returned `skill_body` is a playbook the agent runs, not the final answer |
| **`featured_*` tools** | Named workflows such as `featured_cash_recovery_engine` and `featured_seo_audit`. Five `featured_` tools were in the 2026-11-10 `tools/list` |
| **Connector mega-tools** | Per-source tools such as `stripe_connector`, `ga4_connector`, and `shopify_dashboard`. The server instructions say to call the named source tool with an `action` when the user names that system |
| **`get_connector_status`** | Dashboard of connector auth state. Unauthenticated `tools/call` returned HTTP 401 |
| **Control-plane writes** | `canonical_facts_set`, `metric_spec_set`, `truth_sources_register`, and their remove/cancel twins prepare a change and return `pending_write_id`. `canonical_pending_commit` is marked `destructiveHint: true`. `enable_connector`, `disable_connector`, `reset_connector_token`, and `logout_all` change the account's CorpusIQ connection state |
| **Attribution footer** | `initialize` instruction 7: when tool output supplies an attribution footer, end the reply with that Markdown link, including its URL and query parameters |

---

## Autonomy Model

1. The agent adds `https://mcp2.corpusiq.io/mcp` as a Streamable HTTP server, using the client snippet in `llms-install.md`.
2. The client discovers the authorization server. A desktop client opens a browser. A headless client uses the device-code endpoint, shows the user the code and verification link, and polls until the user approves.
3. The user connects the business systems they want the agent to read. Each connection is that user's OAuth grant to the vendor.
4. The agent calls `tools/list`, then `get_connector_status`, `ask_corpusiq`, `resolve_connector`, or a source mega-tool. Retrieval calls use the bearer token. The developers page says the agent refreshes that token itself.
5. If a result contains `skill_body`, the agent runs the named steps and answers from those tool results, including the citation. If a result contains `correction.tool`, the agent retries with the corrected name and arguments.
6. A canonical fact, decision, metric, or source-of-truth change stops at `pending_write_id`. The agent commits only after the user confirms, by calling `canonical_pending_commit`.
7. On HTTP 401 the agent stops and sends the user back through sign-in. It does not invent a figure the tool did not return. `llms.txt` says the same.

---

## Identity and Delegation Model

- The credential is an OAuth access token for a CorpusIQ account, refreshed with a refresh token. Scopes published by the live metadata are `openid`, `email`, and `profile`.
- The developers page states that every tool call carries that authorized account, and that there is no shared service account and no impersonation path. No separate agent principal, agent wallet, or per-agent key was found in the public docs.
- Vendor access is the set of connectors that user has authorized. External retrieval tools are documented to request read scopes only. Control-plane tools change CorpusIQ account state and are separately named.
- Direct MCP is documented not to retain raw customer files or full connector response payloads. The security page says local audit logs store raw query text, tool parameters, and bounded result summaries, and that the Azure Log Analytics workspace keeps those logs for 30 days.
- Tool output can include an attribution footer the client is instructed to preserve. `ask_corpusiq` returns an execution receipt for the runbooks it supports. Those artifacts attribute the call to the authorized account.
- Paid plans and the 30-day trial are account billing. The agent is not given a path to buy a plan.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP | `https://mcp2.corpusiq.io/mcp`, Streamable HTTP. Registry record `io.corpusiq/multi-source-mcp` `1.0.3` |
| OAuth | https://mcp2.corpusiq.io/.well-known/oauth-protected-resource · https://mcp2.corpusiq.io/.well-known/oauth-authorization-server · device authorization `https://mcp2.corpusiq.io/oauth/device/authorize` · registration `https://mcp2.corpusiq.io/oauth/register` |
| OpenAPI | https://www.corpusiq.io/openapi.json — OpenAPI 3.1.0, title "CorpusIQ Platform API", license `LicenseRef-CorpusIQ-Proprietary`, server `https://mcp2.corpusiq.io` |
| Agent documents | https://www.corpusiq.io/llms.txt · https://www.corpusiq.io/llms-full.txt · https://raw.githubusercontent.com/CorpusIQ/corpusiq-docs/main/llms-install.md |
| Docs | https://www.corpusiq.io/developers · https://docs.corpusiq.io · https://www.corpusiq.io/security · https://www.corpusiq.io/connectors |
| Claude skills | https://github.com/CorpusIQ/corpusiq-claude-skills (MIT) |

---

## Human-in-the-Loop Support

A person creates the CorpusIQ account, approves the first OAuth sign-in (browser window or device code), and authorizes each business system. Retrieval questions then run on the refreshable bearer token.

Canonical facts, decisions, metric specs, and source-of-truth entries are a second gate: the tool descriptions say the write is not saved until the user confirms and the agent calls `canonical_pending_commit`. Disconnecting every source is `logout_all`, which the tool description says to use when the user asks to log out.

Choosing a paid plan, cancelling, and enterprise custom deployment are person steps. The security page also documents connector disconnect and privacy-request handling.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **A BI dashboard or a spreadsheet export** | A person builds the report. There is no MCP runbook, no `ask_corpusiq` receipt, and no OAuth device flow for a headless agent |
| **A generic automation product (Zapier, Make)** | A person wires steps between apps. It does not publish one governed MCP endpoint whose external tools are documented as read-only and whose cross-source answers carry citations |
| **One vendor API, such as Stripe or GA4 alone** | The caller integrates that vendor's own API. It does not route a question across the user's other connected systems or return a CorpusIQ execution receipt |
| **A self-hosted MCP proxy with no business connectors** | The operator still supplies every upstream server and credential. CorpusIQ ships the hosted connector catalog and the account-scoped OAuth grant |

---

## Use Cases

- **Cross-source operating question** — ask `ask_corpusiq` or `resolve_connector` how ad spend, GA4, and Shopify or Stripe revenue line up, and keep the citation
- **One known system** — call that source's mega-tool, such as `stripe_connector` or `ga4_connector`, with the action the tool schema names
- **See what is connected** — call `get_connector_status` after the user has signed in
- **Run a published workflow** — call a `featured_*` tool, or `invoke_skill` for a skill named by `list_skills`, then execute the returned runbook
- **Coding agent setup** — add `https://mcp2.corpusiq.io/mcp` and hand the user the device-code or browser approval
