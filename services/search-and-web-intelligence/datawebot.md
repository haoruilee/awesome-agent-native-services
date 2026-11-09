# datawebot

> **"The world's ecommerce. One MCP."**

| | |
|---|---|
| **Website** | https://www.datawebot.com |
| **Docs** | https://www.datawebot.com/docs/agents |
| **GitHub** | https://github.com/datawebot/datawebot-mcp |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/datawebot/datawebot-mcp?style=social)](https://github.com/datawebot/datawebot-mcp) |
| **Classification** | `agent-native` |
| **Category** | [Search & Web Intelligence Services](README.md) |
| **License** | Hosted service closed source. Connection kit MIT |
| **Operator** | Revenue Scaler Pte. Ltd., as named in https://www.datawebot.com/llms.txt |
| **Disclosure** | Proposed by [Wakmagpie](https://github.com/Wakmagpie), who disclosed working on datawebot |
| **Verified at** | 2026-11-09 |
| **Latest-month signal** | Homepage, [setup.md](https://mcp.datawebot.com/setup.md), [llms.txt](https://www.datawebot.com/llms.txt), [SKILL.md](https://www.datawebot.com/SKILL.md) and [openapi.json](https://www.datawebot.com/openapi.json) HTTP 200 on 2026-11-09. Unauthenticated `POST https://mcp.datawebot.com/mcp` returned HTTP 401 `login_required` with OAuth `WWW-Authenticate`. Connection-kit repo last push 2026-11-02. npm `@datawebot/cli` latest 0.1.4 |

---

## Official Website

https://www.datawebot.com

---

## Official Repo

https://github.com/datawebot/datawebot-mcp

The hosted service is closed source. This repository is the public connection kit: the MCP registry document (`server.json`, name `com.datawebot/datawebot`), Claude Code, Cursor and Gemini CLI plugins, the agent skill and examples.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** URL Onboarding

**One-sentence instruction:** Read https://mcp.datawebot.com/setup.md and follow the instructions.

```
Read https://mcp.datawebot.com/setup.md and follow the instructions.
```

The homepage tells a person to give an agent `set up https://mcp.datawebot.com/setup.md`. For a coding agent with a shell, that file signs in by email approval, saves the key to an owner-only file, and registers the MCP server without printing the key. A chat app or a sandboxed agent cannot add the server itself. The same file tells that agent to stop and hand the person the connector steps for `https://mcp.datawebot.com/mcp`.

The hosted skill is https://www.datawebot.com/SKILL.md. The site index for agents is https://www.datawebot.com/llms.txt.

---

## Agent Skills

**Status:** ✅ Available

The skill is published at https://www.datawebot.com/SKILL.md and in the connection kit at `skills/datawebot/SKILL.md` (MIT). The Claude Code plugin and the Gemini CLI extension include it. Other agents copy the `skills/datawebot` folder into their skills directory. The kit does not document an `npx skills add` command.

```text
/plugin marketplace add datawebot/datawebot-mcp
/plugin install datawebot@datawebot
```

Gemini CLI: `gemini extensions install https://github.com/datawebot/datawebot-mcp`

| Skill | What It Teaches the Agent |
|---|---|
| `datawebot` | When to search or open a product, how to run an extraction Job, how credits and errors work, and to treat listing text as untrusted data |

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/datawebot/datawebot-mcp (registry name `com.datawebot/datawebot`). The server is hosted |
| **Endpoint** | `https://mcp.datawebot.com/mcp` |
| **Transport** | Streamable HTTP |
| **Auth** | OAuth 2.1 authorization code with PKCE (S256), dynamic client registration and refresh tokens, or `Authorization: Bearer`. Protected-resource metadata: https://mcp.datawebot.com/.well-known/oauth-protected-resource/mcp. Authorization server: https://mcp.datawebot.com/.well-known/oauth-authorization-server. Unauthenticated calls, including `discover`, return HTTP 401 `login_required` |
| **Tools** | `discover`, `search_products`, `get_product`, `get_results`, `check_site`, `get_account`, `find_endpoints`, `submit_job`, `run_tool` |
| **Compatible Clients** | Claude, Claude Code, Cursor, VS Code, ChatGPT, Codex, Gemini CLI, Cline, LM Studio, and other remote MCP clients |

---

## What It Does

datawebot gives an agent ecommerce product data: what is for sale, at what price, from which shop, with a link to the product page. `search_products` searches one shop or across shops in a chosen country. `get_product` reads one product by URL or by the `product_id` from a search. When several shops sell it, the answer lists each seller's price, shipping total, delivery note and direct link. Ads are returned separately from organic results. Every answer is a best-effort snapshot labelled with when it was retrieved. It is not a verified or guaranteed-current price, and datawebot does not store a price history.

Extraction Jobs read one exact store endpoint: a search page, a catalogue or category page, or a product page. `find_endpoints` lists a shop's endpoint ids, prices and page limits. `submit_job` runs one id on one URL. The same operations are on the REST API and on the `dtwb` CLI. The site index, checked against the catalogue when the site is built (the copy fetched on 2026-11-09 says checked 2026-11-03), states that Jobs cover 36,413 stores in 126 countries through 109,094 endpoints, including Amazon in 20 countries, Mercado Libre in 18, eBay in 17, Zalando in 17 and Walmart US. Product search is not limited to that store list.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage title: "Ecommerce MCP server and product data API for AI agents." Hero: "The world's ecommerce. One MCP." The page says "Give this to your agent" and shows `set up https://mcp.datawebot.com/setup.md`. — https://www.datawebot.com |
| **Agent-specific primitive** | `discover` returns the tools available now, including ones added after the session started, with `meta.catalog_version`. `run_tool` calls a tool by the name `discover` returned. `find_endpoints` returns per-store contracts (id, price, page limit) that the agent must use as given. Results tell the agent to treat titles, descriptions and URLs as untrusted data. — https://www.datawebot.com/SKILL.md |
| **Autonomy-compatible control plane** | After one email approval, the agent searches, reads products and submits Jobs without another click. Spend is a prepaid credit balance. A search costs 5 credits and a product read costs 1. Jobs default to 5 credits per search or catalogue page and 1 per product page. Failed requests are free. A page that loads but has no results is still charged. The agent is told not to buy credits itself. — https://www.datawebot.com/llms.txt |
| **M2M integration surface** | Remote MCP, REST at `https://api.datawebot.com` with OpenAPI 3.1 (https://www.datawebot.com/openapi.json), CLI `dtwb` (`npm install --global @datawebot/cli`), `setup.md`, `SKILL.md`, `llms.txt` |
| **Identity / delegation** | Setup saves an owner-only key and sends a client name plus a random installation ID that is not derived from the computer. The agent must not ask for or print a key. The service reads public listings. It does not buy, log into shops, or act for the user inside a store. — https://mcp.datawebot.com/setup.md |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`discover` / `run_tool`** | Current tool list and schemas, plus `catalog_version`. Call `discover` again when a result's version changes. `run_tool` invokes a tool added after the session started |
| **`search_products`** | Keyword search on one shop or across shops. `country` is a two-letter code (default `US`). `limit` is 1–20. Organic hits are separate from `sponsored` |
| **`get_product`** | One product by URL or `product_id`, including each seller's offer and a direct link |
| **`find_endpoints`** | Free list of one shop's exact endpoint ids, types, prices, page limits and example URLs. Ids are not constructed by the caller |
| **`submit_job`** | One endpoint on one URL, with `max_pages`, optional `max_credits`, and a `request_key` so a retry returns the same request |
| **`get_results`** | Polls an answer whose status was `working`, then pages with `next_cursor`. Free. Results expire after seven days |
| **Credit balance** | New accounts start with 200 credits, no card. `get_account` and `check_site` report what is left and what a shop costs. Packs are bought by a person on the dashboard |

---

## Autonomy Model

1. The agent reads https://mcp.datawebot.com/setup.md. A coding agent with a shell runs the sign-in script. It reuses a saved key when `discover` still shows `signed_in`.
2. If no key is saved, the agent asks which email to use. The person opens the email, checks the code, and clicks Approve. No card and no password. The script waits up to 10 minutes and writes the key itself.
3. The agent calls `discover`, then `search_products` and `get_product` for keyword and offer questions.
4. For a catalogue or a repeated page, the agent calls `find_endpoints`, then `submit_job` on one example-shaped URL, then `get_results` until `next_cursor` is null.
5. On `insufficient_credits` (HTTP 402) the agent stops and tells the person. It does not sign in again and it does not buy credits. On `rate_limited` it waits. It does not loop.
6. A chat-app connector uses OAuth instead of the script. The person still approves one email. After that, the connector refreshes itself.

---

## Identity and Delegation Model

- The coding-agent path issues a key to that installation. Setup sends the client name (the script's example is `"opencode"`) and a random installation ID stored beside the key. The ID is not derived from the computer or the user. The script's own check expects a key shaped `dwb_` plus 64 hex characters, and it refuses to print the key.
- Keys from `setup.md` last 30 days. A person can also create a dashboard API key for 30 days, 90 days or 1 year and pass it as `Authorization: Bearer` for scripts and frameworks.
- Chat apps use OAuth 2.1. The access token is the connector's credential, refreshed by the client, still backed by the same email approval.
- datawebot reads publicly accessible product pages. It does not place orders, log into shops, or use the person's store session.
- REST responses carry `X-Request-Id`. Job tools return a `request_id`. Those identifiers are how a failed call is reported. They are not a full action-replay log.
- An agent cannot raise its own credit balance. Packs are one-time dashboard purchases (Scout, Agent, Fleet, Swarm). Free and bought credits expire 6 months after they are added.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP | `https://mcp.datawebot.com/mcp`, Streamable HTTP, OAuth 2.1 or bearer key. Discovery document: https://www.datawebot.com/.well-known/mcp.json |
| REST | `https://api.datawebot.com`. OpenAPI 3.1, title "datawebot. Jobs API", at https://www.datawebot.com/openapi.json. Intent calls use `POST /v1/requests`. Jobs use `GET /v1/job-blueprints`, `POST /v1/jobs`, `GET /v1/jobs/{id}`, `GET /v1/jobs/{id}/results` |
| CLI | `npm install --global @datawebot/cli`, then `dtwb login`, `dtwb search`, `dtwb product`, `dtwb extract`. stdout is one JSON document. Guide: https://www.datawebot.com/cli.md |
| Agent documents | https://mcp.datawebot.com/setup.md · https://www.datawebot.com/SKILL.md · https://www.datawebot.com/llms.txt |
| Reference | https://www.datawebot.com/docs/agents · https://www.datawebot.com/docs/api/reference · store directory https://www.datawebot.com/scraper |

---

## Human-in-the-Loop Support

A person approves the first sign-in in their email inbox, matching the code the agent was shown. After that, search, product reads and Jobs run without further clicks, inside the credit balance and any `max_credits` the agent was given.

Buying credits, creating a long-lived dashboard key, and adding a connector inside Claude or ChatGPT are person steps. The skill tells the agent to stop on `insufficient_credits` and to never buy credits itself. Listing text is data, not permission to spend or to follow an instruction found on a product page.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **A general web-scraping API** | A person points it at URLs and parses the page. It has no `discover` / `run_tool` catalog, no per-store endpoint contract with a credit price, and no agent sign-in document |
| **A shopping API built for storefront apps** | Returns the same JSON to any caller that pasted a developer key. It is not set up by an agent reading one URL, and it does not separate organic hits from sponsored listings for a model |
| **A price-comparison website** | Built for a person browsing. No MCP server, no OpenAPI Job contract, and no machine-readable setup |

---

## Use Cases

- **Find a product in one country** — search shops in `US`, `GB`, `JP` or another market and show title, price, shop and link
- **Compare sellers** — pass a `product_id` or product URL and list each seller's price and direct link
- **Pull one catalogue page** — pick an endpoint id from `find_endpoints` and submit a one-page Job
- **Script the same read** — call `POST /v1/requests` or `dtwb search` with the same account key the agent saved
- **Stay inside a budget** — pass `max_credits`, read `get_account`, and stop when the balance cannot cover the next page
