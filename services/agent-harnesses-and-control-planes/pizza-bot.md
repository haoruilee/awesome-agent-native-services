# Pizza Bot

> **"Pizza Bot is an inbox for long-running AI work."**

| | |
|---|---|
| **Website** | https://github.com/pizza-bot-app/pizza-bot |
| **Docs** | https://github.com/pizza-bot-app/pizza-bot/blob/main/docs/RUNNING.md |
| **GitHub** | https://github.com/pizza-bot-app/pizza-bot |
| **Classification** | `agent-native` |
| **Category** | [Agent Harnesses & Operator Surfaces](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Show HN 2026-09-15 ([item 49713894](https://news.ycombinator.com/item?id=49713894)); Amazon-developed OSS inbox for background agent runs |
| **Verified at** | 2026-09-20 |

---

## Official Website

https://github.com/pizza-bot-app/pizza-bot

The GitHub README and releases page are the live product surface. Packaged installers for macOS, Windows, and Linux are attached to every [release](https://github.com/pizza-bot-app/pizza-bot/releases). There is no separate marketing domain.

---

## Official Repo

https://github.com/pizza-bot-app/pizza-bot

Apache-2.0. Developed at Amazon and released as Pizza Bot OSS.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + HTTP/SSE api-server (desktop, browser, or terminal)

From a checkout (Node.js 24+):

```bash
git clone https://github.com/pizza-bot-app/pizza-bot.git
cd pizza-bot
npm install
npm run build
npm run dev
```

`npm run dev` starts the Vite frontend and Electron desktop shell. The shell forks and supervises its own api-server. Configure a model under **Settings > Providers** before starting a live run.

Terminal client against a running backend:

```bash
PORT=8080 npx tsx apps/api-server/src/index.ts
npm run shell
# or: npm run shell -- "one-shot prompt"
```

The packaged `pizza` executable is the same HTTP client. See [Running from source](https://github.com/pizza-bot-app/pizza-bot/blob/main/docs/RUNNING.md) for isolated data roots, browser development, desktop packages, and [standalone backends](https://github.com/pizza-bot-app/pizza-bot/blob/main/docs/STANDALONE_BACKEND.md).

This is **not** URL Onboarding. A human (or an operator agent with local install rights) must provision the api-server, a model provider, and any folder grants. Reading a document does not register an agent.

---

## Agent Skills

**Status:** ⚠️ Not published as a standalone `npx skills add` pack for this catalog entry.

Pizza Bot *consumes* Agent Skills as tool-scoped subagents. User skills live under `<PIZZA_DATA_ROOT>/skills/<id>/SKILL.md` (default data root `~/.pizza-bot-oss`). A Built-in **Pizza Bot Guide** can explain features, suggest workflows, and point at project docs. Skills become callable only after their declared MCP servers and tools are enabled and connected. See [Extending Pizza Bot](https://github.com/pizza-bot-app/pizza-bot/blob/main/docs/EXTENDING.md).

Search community skills: `npx clawhub@latest search pizza-bot`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ Not published as an installable MCP *server* product.

Pizza Bot is the harness. It *hosts* MCP servers as tools for the conversation agent and for skill-scoped subagents. Add servers from the UI or a Claude Code-compatible `<PIZZA_DATA_ROOT>/.mcp.json`. Startup connects to at most three servers concurrently.

| Detail | Value |
|---|---|
| **Primary interface** | Local api-server over HTTP/SSE (LangGraph / Agent Protocol) |
| **MCP role** | Consumer / host of operator-configured MCP servers |
| **Config** | UI or `~/.pizza-bot-oss/.mcp.json` |
| **Compatible clients** | Electron desktop, browser UI, `pizza` / `npm run shell` CLI |

---

## What It Does

Pizza Bot is a local-first inbox for long-running AI agents. Start or schedule a task, leave, and let completed work collect in **Unread** while runs waiting for a decision collect in **Action**. Agents keep working when the UI navigates away or disconnects; the api-server process must remain running.

The runtime is a stateful DeepAgents / LangGraph graph. Desktop, web, and terminal clients all talk to the same api-server over HTTP/SSE. Checkpointed runs survive client disconnects. Cron or webhook triggers can start work without an open conversation. Skills become tool-scoped specialist subagents whose progress appears in the Activity panel.

**Human UI honesty:** the desktop/web inbox is an approval and review surface, not the primary worker. The agent loop runs in the api-server. Humans grant folders, configure providers, and decide Action-queue approvals.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | *"Pizza Bot is an inbox for long-running AI work."* Source: [official README](https://github.com/pizza-bot-app/pizza-bot). GitHub description: *"A local-first inbox for long-running AI agents, built with DeepAgents and LangGraph."* |
| **Agent-specific primitive** | Unread / Action queues, checkpointed background runs, durable approval cards (`interruptOn` with approve / edit / reject), and skill-scoped subagents. A human mail inbox or generic task board is not the same primitive. |
| **Autonomy-compatible control plane** | Once a run is started (or triggered by cron / webhook), the api-server continues without an attached UI. Constraints are provider config, explicit folder grants, and HITL gates on consequential tools. |
| **M2M integration surface** | HTTP/SSE Agent Protocol api-server, terminal CLI, standalone backend (Docker / Compose / Kubernetes), MCP host, and SKILL.md subagent catalog. The human UI is optional for an already-running backend. |
| **Identity / delegation** | Conversation agent vs tool-scoped skill subagents; explicit read-only or writable folder grants (no default home-directory access); approval decisions attributed to the waiting run. Local-first: the process runs as the OS user; there is no hosted Pizza Bot account or URL-join identity. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Unread queue** | Completed background work waiting for the operator to read |
| **Action queue** | Durable approval / decision requests that block a run |
| **Checkpointed run** | LangGraph / DeepAgents state that survives client disconnects |
| **Skill subagent** | Enabled `SKILL.md` becomes a tool-scoped specialist invoked through `task` |
| **Folder grant** | Explicit read-only or writable path under Settings > Files |
| **Trigger** | Cron or webhook start without an open conversation |

---

## Autonomy Model

```
Operator installs Pizza Bot (or a standalone api-server) and configures a model provider
    ↓
Operator grants only the folders the agent may read or write
    ↓
Operator (or cron / webhook) starts a thread / task
    ↓
api-server runs the DeepAgents / LangGraph loop while the UI may disconnect
    ↓
Completed work lands in Unread; interruptOn tools land in Action
    ↓
On approve / edit / reject, the run resumes with that decision in context
    ↓
Skill-scoped subagents report progress in Activity
```

The api-server must stay up. Disconnecting the desktop or browser does not stop a live run.

---

## Identity and Delegation Model

- **Conversation agent** — Pizza Bot itself is the primary worker for a thread.
- **Skill subagents** — each ready skill is a separate tool-scoped delegate; its `SKILL.md` body is the instruction set and its declared tools are the complete tool surface.
- **Folder grants** — local filesystem access is deny-by-default; each path is read-only unless writes are allowed. Remote grants name paths on the backend host.
- **Approvals** — `interruptOn` frontmatter requires a human decision (approve / edit / reject) before listed tools run.
- **Boundary** — no hosted agent identity, no URL onboarding, and no pizza-bot cloud account. Attribution is local thread / run / skill ids under `<PIZZA_DATA_ROOT>`.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| HTTP/SSE api-server | Hono Agent Protocol routes; clients use `@langchain/langgraph-sdk` |
| Electron desktop | Local inbox; forks and supervises the api-server |
| Browser UI | Vite / static deployment against a running backend |
| CLI | `npm run shell` or packaged `pizza` HTTP client |
| Standalone backend | Docker, Compose, Kubernetes — [backend guide](https://github.com/pizza-bot-app/pizza-bot/blob/main/docs/STANDALONE_BACKEND.md) |
| MCP host | Operator-configured servers via UI or `.mcp.json` |
| Agent Skills | `<PIZZA_DATA_ROOT>/skills`, Built-in, and Plugin packs |

---

## Human-in-the-Loop Support

HITL is a first-class queue, not a dashboard afterthought. Consequential tools can require `interruptOn` approvals; those cards collect in **Action** and accept approve, edit, or reject. Completed work waits in **Unread**. Desktop notifications are built in. Folder grants and provider secrets remain operator-controlled. Ordinary in-policy tool use proceeds without a click.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **ChatGPT / Claude.ai chat tab** | Human chat workspace; no Unread/Action queues, no disconnect-survivable api-server, no skill-scoped subagent catalog |
| **Generic mail inbox** | Human messages, not checkpointed agent runs with durable approval cards |
| **LangGraph Studio / agent builder** | Human orchestration of graphs; Pizza Bot is a shipped inbox + runtime for already-running work |
| **tmux + a coding CLI** | Process host without Unread/Action primitives or protocol-level approval state |

---

## Use Cases

- **Background research or launch briefs** — start a run, leave, read the result in Unread
- **Release or publish gates** — `interruptOn` a publish tool so Action holds the decision
- **Specialist delegation** — enable a skill so Pizza Bot can `task` a scoped subagent
- **Headless / remote backend** — run the api-server in Docker or Kubernetes and attach CLI or browser clients
