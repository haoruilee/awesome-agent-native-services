# box by Simular

> **"Give your agents a computer."**

| | |
|---|---|
| **Website** | https://box.simular.ai |
| **Docs** | https://box.simular.ai/docs/mcp |
| **GitHub** | No public product repository (hosted service is closed-source; connectors repo is MIT) |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | Hosted service closed-source. https://github.com/simular-ai/box-plugin is MIT and contains connectors only |
| **Latest-month signal** | Checked 2026-11-25: [homepage](https://box.simular.ai) HTTP 200, title "Give your agents a computer"; [llms.txt](https://box.simular.ai/llms.txt), [auth.md](https://box.simular.ai/auth.md), [install.md](https://box.simular.ai/install.md), and [docs/mcp](https://box.simular.ai/docs/mcp) HTTP 200; MCP GET [https://mcp.box.simular.ai/mcp](https://mcp.box.simular.ai/mcp) 401; server card https://box.simular.ai/.well-known/mcp/server-card.json HTTP 200; [box-plugin](https://github.com/simular-ai/box-plugin) MIT, 3 stars, pushed 2026-11-25T07:23:22Z |
| **Verified at** | 2026-11-25 |

---

## Official Website

https://box.simular.ai

Homepage title: *"box by Simular | Give your agents a computer."* `llms.txt`: *"box is a cloud Linux desktop for your AI."* Server card title: *"box by Simular."* One hosted Ubuntu desktop per account. The slug in this catalog is `simular-box`, not `box`.

---

## Official Repo

The hosted desktop is not open-source.

https://github.com/simular-ai/box-plugin is MIT and holds connectors that add the hosted MCP server to Claude Code, DeepSeek Harness, and other agents. The README says most agents need no plugin: add `https://mcp.box.simular.ai/mcp` and sign in once. The plugin repository is not the desktop service.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** remote MCP after a person's Simular login, or a human-created `cb_` key. Not a one-URL join.

[auth.md](https://box.simular.ai/auth.md) states there is no agent self-registration: no anonymous, email, or identity-assertion signup. Every credential comes from a person with a Simular account.

```text
https://mcp.box.simular.ai/mcp
```

OAuth: the client opens a browser, the person signs in, and they click Allow (scope `boxes`). Clients that cannot sign in use `Authorization: Bearer cb_...` with a key from https://box.simular.ai/access. GET https://mcp.box.simular.ai/mcp returned 401 on 2026-11-25. Server card: https://box.simular.ai/.well-known/mcp/server-card.json.

---

## Agent Skills

**Status:** ⚠️ Not yet published

No official `SKILL.md` or `npx skills add` package was found on the pages reviewed on 2026-11-25. `install.md` is an MCP setup page, not an Agent Skill.

Search community skills: `npx clawhub@latest search simular-box`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available — hosted Streamable HTTP

| Detail | Value |
|---|---|
| **MCP Repo** | Server is hosted. Connectors only: https://github.com/simular-ai/box-plugin |
| **Endpoint** | `https://mcp.box.simular.ai/mcp` |
| **Transport** | Streamable HTTP |
| **Auth** | OAuth (Simular account, scope `boxes`) or `Bearer cb_...` |
| **Server card** | https://box.simular.ai/.well-known/mcp/server-card.json |
| **Docs** | https://box.simular.ai/docs/mcp |
| **Compatible Clients** | Claude, ChatGPT, Claude Code, Codex, Cursor, OpenCode, Hermes, OpenClaw, VS Code, DeepSeek Harness (`llms.txt`) |

---

## What It Does

box is one cloud Linux desktop for the account. The agent opens a browser, clicks, types, reads the screen, and runs shell commands. The desktop sleeps when idle (the M plan is the exception that does not sleep, per `llms.txt`) and wakes when the agent connects. A person can watch and take over at https://box.simular.ai/box. Takeover is optional.

`llms.txt` says a box asleep 14 days in a row is deleted with its files (30 days if the account has ever paid; not while an S or M plan is active). Any wake resets that count. The agent's own model bill stays on the agent's plan. box credits pay for awake time.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage title: *"Give your agents a computer."* `llms.txt`: *"box is a cloud Linux desktop for your AI."* Server card: *"A cloud Linux desktop for your AI: browse, click, type, read the screen and run commands."* Sources: https://box.simular.ai and https://box.simular.ai/llms.txt |
| **Agent-specific primitive** | One persistent cloud desktop per account, driven as MCP tools (browser, click, type, screenshot, shell), sleeping when the agent is away. |
| **Autonomy-compatible control plane** | After OAuth Allow or a `cb_` key, actions do not each require a click. Live takeover is optional. There is no per-action approval queue in auth.md. |
| **M2M integration surface** | One hosted MCP server, auth.md, install.md, llms.txt, and the server card. The MIT repo is connectors only. |
| **Identity / delegation** | A Simular user delegates with OAuth scope `boxes`, or pastes a personal `cb_` key they created. The agent does not register itself. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Desktop** | One hosted Ubuntu machine per account. Browser, click, type, screenshot, shell. |
| **Sleep / wake** | Sleeps when idle; wakes when the agent connects. Long sleep can delete the disk (`llms.txt`). |
| **OAuth or cb_ key** | Browser sign-in, or a bearer key from https://box.simular.ai/access. |
| **Takeover** | Optional live control by a person at `/box`. |

---

## Autonomy Model

1. A person creates a Simular account.
2. The agent adds `https://mcp.box.simular.ai/mcp`. The person signs in and clicks Allow, or creates a `cb_` key.
3. The agent wakes the desktop and uses the browser, pointer, keyboard, and shell.
4. The desktop sleeps again when idle. The agent does not have a second desktop on the same account.

---

## Identity and Delegation Model

- auth.md: no agent self-registration. The identity is the person's Simular account.
- OAuth uses PKCE, scope `boxes`, and `resource=https://mcp.box.simular.ai/mcp`. Refresh and revoke are on that authorization server.
- A `cb_` key is a personal key for clients that cannot run OAuth. Treat it as access to that one desktop.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Hosted MCP | `https://mcp.box.simular.ai/mcp` |
| Auth | https://box.simular.ai/auth.md |
| Install | https://box.simular.ai/install.md |
| Docs | https://box.simular.ai/docs/mcp |
| Index | https://box.simular.ai/llms.txt |
| Server card | https://box.simular.ai/.well-known/mcp/server-card.json |
| Connectors | https://github.com/simular-ai/box-plugin (MIT, not the desktop) |

---

## Human-in-the-Loop Support

A person must hold the Simular account and approve OAuth or create the `cb_` key. There is no agent signup. After that, the agent drives the desktop alone. Live takeover at `/box` is available and not required for each action.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **box-plugin as the product** | Installers for other agents. The computer is the hosted MCP service. |
| **E2B Desktop / Orgo** | Other vendors' computers, with their own accounts and APIs. box is one Simular desktop per account. |
| **A VPS** | No MCP desktop tools, no sleep lifecycle, and no Simular OAuth scope for an agent. |

---

## Use Cases

- **One Linux desktop for an agent** — browse, click, and run commands without a local GUI.
- **A machine that sleeps** — the desktop stays, disks and all, and wakes on the next MCP connection until the idle-delete window.
- **A client that cannot do OAuth** — a person creates a `cb_` key and the agent sends it as a bearer token.
