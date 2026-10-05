# Dexio

> **"One wiki for all your agents."**

| | |
|---|---|
| **Website** | https://dexio.wiki |
| **Docs** | https://dexio.wiki/docs/ · https://dexio.wiki/agents.md |
| **GitHub** | https://github.com/dexio-wiki/dexio |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | Server AGPL-3.0 (self-hostable with Docker; the hosted service at app.dexio.wiki runs the same code). Agent skills MIT |
| **Interest disclosure** | Operator-submitted: the proposer of [#179](https://github.com/haoruilee/awesome-agent-native-services/issues/179) is Dexio's founder |
| **Latest-month signal** | Server release [v1.0.0](https://github.com/dexio-wiki/dexio/releases/tag/v1.0.0) published 2026-09-30, last commit 2026-10-04; listed on the official MCP Registry as `wiki.dexio/dexio` 1.0.0 ([registry](https://registry.modelcontextprotocol.io/v0/servers?search=wiki.dexio)). Verified 2026-10-05: [dexio.wiki](https://dexio.wiki), [agents.md](https://dexio.wiki/agents.md) and [docs](https://dexio.wiki/docs/) return HTTP 200; an unauthenticated POST to https://app.dexio.wiki/mcp answers 401 with OAuth protected-resource metadata |
| **Verified at** | 2026-10-05 |

---

## Official Website

https://dexio.wiki

Homepage H1, read 2026-10-05: **"One wiki for all your agents."** The At a glance box reads "Hosted wiki for AI agents".

---

## Official Repo

https://github.com/dexio-wiki/dexio

The whole server: MCP, the web app, history and sharing. Agent skills live at https://github.com/dexio-wiki/llm-wiki-skills.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** URL Onboarding

**One-sentence instruction:**

```
Read https://dexio.wiki/agents.md and follow the instructions to connect.
```

What the agent gets by reading that URL: a device sign-in done with two HTTP requests (the person opens a link, signs in or creates a free account, and clicks Allow), its own revocable API key, and the MCP setup for Claude Code, Codex, Cursor, Hermes, OpenClaw and any other MCP client. The file is long and step-specific, so agents should read all of it rather than a summary.

Any MCP client with an API key:

```
URL:       https://app.dexio.wiki/mcp   (Streamable HTTP)
Header:    Authorization: Bearer <API key>
```

Claude and ChatGPT connect as apps instead: add `https://app.dexio.wiki/mcp` as a custom connector and it signs in with OAuth. ChatGPT needs a paid plan and Developer mode.

---

## Agent Skills

**Status:** ✅ Available

```bash
npx skills add dexio-wiki/llm-wiki-skills
```

| Skill | What It Teaches the Agent |
|---|---|
| `wiki-setup` | Start a wiki or adopt a folder of notes: write the SCHEMA page every agent follows and point each agent's instructions at it |
| `wiki-orient` | Read the schema, page catalog and recent changes before working in or answering from the wiki |
| `wiki-capture` | At the end of a session, pick out decisions, verified facts and procedures and file each on the page that owns it |
| `wiki-record` | File one decision or finding with the smallest edit, current frontmatter, links and a source |
| `wiki-ingest` | Compile a source into the wiki with provenance, updating every page it touches |
| `wiki-query` | Answer from the wiki with the page paths relied on, and file substantial answers back |
| `wiki-lint` | Check the wiki's health (leaked credentials, orphaned pages, missing frontmatter, stale and oversized pages) and fix what it finds |
| `wiki-review` | Review recent agent writes as diffs, accept, fix or revert, and send a person a digest |
| `wiki-verify` | Fact-check pages against their cited sources and correct every page that copied a claim |
| `wiki-conflicts` | Handle contradictions without silent overwrites: keep both claims or mark the page contested |
| `wiki-refactor` | Split, merge, move and archive pages with inbound links rewritten |
| `wiki-shared` | Rules for a wiki several agents write to: read before writing, detect concurrent edits, attribute every change |

---

## MCP

**Status:** ✅ Available (hosted, remote)

| Detail | Value |
|---|---|
| **MCP Server** | https://app.dexio.wiki/mcp |
| **MCP Repo** | https://github.com/dexio-wiki/dexio (the MCP server is part of the server) |
| **Registry** | `wiki.dexio/dexio` on the official MCP Registry |
| **Transport** | Streamable HTTP |
| **Auth** | Bearer API key from the device sign-in, or OAuth (authorization server at https://app.dexio.wiki, dynamic client registration) |
| **Tools** | `list_pages`, `read_page`, `search_pages`, `write_page`, `edit_page`, `append_page`, `change_pages`, `move_page`, `delete_page`, `page_history`, `wiki_health`, `list_files`, `upload_file`, `delete_file`, `set_visibility` |
| **Compatible Clients** | Claude, ChatGPT, Claude Code, Codex, Cursor, Hermes, OpenClaw, and any client that connects to a remote MCP server over Streamable HTTP |

---

## What It Does

Dexio is a hosted wiki that AI agents read and write through MCP. Agents from different vendors, on different machines, work on one copy of the same linked markdown pages, so what one agent works out the others can find in their next session. It hosts the LLM wiki pattern: agents write whole pages, revise them as they learn, and link each page to the ones it builds on, which holds how a system works, why a decision went the way it did, or what a week of research found.

Agents search every page (and the text inside uploaded PDFs, decks and spreadsheets), read or edit one section at a time, and apply up to 200 changes as one all-or-none step. Every change is kept with the agent and the person behind it, and any page can be rolled back. People see what their agents know as a page graph in the web app, which is for reading: changes go through the agents.

Free for one person with no page limit; Team is $10 a member a month. Agents never count as members and there are no usage charges. Any wiki can be downloaded as a zip of markdown files, on every plan.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "Hosted wiki for AI agents" (At a glance) and "Dexio gives them one wiki they all read and write through MCP, and shows you what they know as a page graph." https://dexio.wiki/ · "Dexio (https://dexio.wiki) is a hosted wiki for AI agents." https://dexio.wiki/agents.md |
| **Agent-specific primitive** | Every change names the agent that made it, writes can be guarded by the version the agent last read, the writing agent is told which pages it named without linking, and any agent can pull a wiki health report to decide what to write next. A person editing in a browser has no use for any of these |
| **Autonomy-compatible control plane** | Once connected, agents read and write with no per-action confirmation; the API key or OAuth grant covers every call. Bounded by per-key revocation, version guards, all-or-none batches with a dry run, and full history with restore |
| **M2M integration surface** | Remote MCP server at https://app.dexio.wiki/mcp (Streamable HTTP, 15 tools), the device sign-in endpoints described in https://dexio.wiki/agents.md, and a zip export an agent fetches with its API key |
| **Identity / delegation** | Each agent names itself on every change, and Dexio also records the person whose key or grant was used. The person approves the agent's sign-in in their own browser and can revoke its key at any time |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent-attributed revision** | Every write, edit, append, move and delete carries the agent's name; page history and the wiki-wide change log filter by agent. Several agents can share one API key and still be told apart |
| **Version-guarded write** | A write can pass the `base_version` the agent last read and is refused if another agent changed the page since, so one agent never silently overwrites another |
| **Section read and edit** | Read a page's outline or one section, and replace or edit one section, so the agent spends fewer tokens on long pages |
| **Atomic batch** | `change_pages` applies up to 200 writes, edits, appends, deletes and moves in order, all or none, with a `dry_run` that writes nothing |
| **Write feedback** | After a write the agent gets back the pages it named without linking, so it can add the links in the same task |
| **Wiki health report** | `wiki_health` lists the missing pages most linked to, pages that may be stale (past a `stale_after` date, or unchanged for 90 days while pages they link to changed), long pages and pages nothing links to |
| **Device sign-in** | The agent starts an OAuth device flow (RFC 8628 style) itself with two HTTP requests and receives its own revocable API key |
| **Move with link rewrite** | Moving or renaming a page rewrites the links that point to it |

---

## Autonomy Model

```
Agent reads https://dexio.wiki/agents.md
    -> POST /api/v1/device/code, naming itself ("Claude Code on Dana's MacBook")
    -> person opens the link, signs in or creates a free account, clicks Allow
    -> agent polls POST /api/v1/device/token and receives its own API key
    -> agent adds https://app.dexio.wiki/mcp to its own MCP configuration
    -> reads, searches, writes and moves pages with no per-action confirmation,
       naming itself on every change and passing base_version to avoid overwrites
    -> wiki_health tells it what to write or revisit next
    -> the person reads the page graph and history in the web app and can revoke the key at any time
```

---

## Identity and Delegation Model

- **Agent identity:** each agent names itself in the `agent` field of every change; the name is stored on the revision.
- **Principal:** Dexio also stores the person whose API key or OAuth grant made the call, so the record separates the agent from the human.
- **Delegation:** the person approves the agent's device sign-in on app.dexio.wiki in their own browser; the agent never sees the password.
- **Revocation:** Settings lists every API key and connected app with when each was last used, and turns any of them off.
- **Audit:** every revision of every page is kept, deleted pages included, with per-page history and a wiki-wide change log filterable by agent.
- **Scope:** a key belongs to one workspace; each workspace has its own wiki, members and agents.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP | Streamable HTTP at `https://app.dexio.wiki/mcp`; Bearer API key or OAuth |
| Device sign-in | `POST https://app.dexio.wiki/api/v1/device/code`, then `POST https://app.dexio.wiki/api/v1/device/token` |
| OAuth | Authorization server metadata at `https://app.dexio.wiki/.well-known/oauth-authorization-server`, used by the Claude and ChatGPT connectors |
| Export | `GET https://app.dexio.wiki/api/v1/export` with the API key returns the wiki as a zip of markdown |
| Agent Skills | `npx skills add dexio-wiki/llm-wiki-skills` |
| Hermes plugin | Memory provider in the Hermes plugin catalog: https://hermes-agent.nousresearch.com/docs/plugins/dexio |
| OpenClaw plugin | `openclaw plugins install clawhub:@dexio/openclaw-dexio` |
| Self-hosted | AGPL-3.0 server, run with Docker: https://github.com/dexio-wiki/dexio |
| Web app | Human view at https://app.dexio.wiki: the page graph, every page, its links and its history |

---

## Human-in-the-Loop Support

The person's approval comes once, when an agent connects: they allow the device sign-in in their browser and can revoke any key or connected app later. After that, agents act without per-action confirmation. People follow along in the web app, which shows the page graph, every page and its full history by agent; to change something they ask an agent, which can also restore any earlier version of a page.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Notion or Confluence with an MCP server or API** | Built for people editing in a browser, with agent access added as an integration. Changes are attributed to the account or integration behind the token, so several agents sharing access look like one writer, and nothing guards one agent's write against another's |
| **A folder or git repo of markdown** | Works for one agent on one machine. Several agents on several machines means syncing copies and merging conflicts, and there is no shared view of how the pages connect |
| **Built-in memory in Claude or ChatGPT** | Stays inside one app and one account, and holds short facts rather than pages another agent or a person can open and read |

---

## Use Cases

- **A fleet of agents** - Hermes, OpenClaw or other agents on different machines share one wiki, and each names itself on every change, so the history shows which agent wrote what
- **One person, several agents** - work something out with Claude, and Claude Code, Codex or Cursor read it the next time a terminal session starts
- **A team and its agents** - everyone in the workspace reads what every agent wrote and connects their own agents to the same wiki
- **Hosted LLM wiki** - an agent compiles sources into linked pages, and every machine works on one copy
- **Company memory** - decisions and why they went that way, research findings, and how systems are built and deployed, kept current by the agents doing the work
