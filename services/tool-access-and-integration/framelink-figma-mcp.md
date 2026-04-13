# Framelink MCP for Figma

> **"Give your coding agent access to your Figma data. Implement designs in any framework in one-shot."**

| | |
|---|---|
| **Website** | https://www.framelink.ai/ |
| **Docs** | https://www.framelink.ai/docs/quickstart |
| **GitHub** | https://github.com/GLips/Figma-Context-MCP |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/GLips/Figma-Context-MCP?style=social)](https://github.com/GLips/Figma-Context-MCP) |
| **npm** | `figma-developer-mcp` |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **License** | MIT |

---

## Official Website

https://www.framelink.ai/

---

## Official Repo

https://github.com/GLips/Figma-Context-MCP

---

## How to Use (Agent Onboarding)

**MCP via npx** — create a [Figma personal access token](https://help.figma.com/hc/en-us/articles/8085703771159-Manage-personal-access-tokens), then add to MCP config ([README](https://github.com/GLips/Figma-Context-MCP)):

```json
{
  "mcpServers": {
    "Framelink MCP for Figma": {
      "command": "npx",
      "args": ["-y", "figma-developer-mcp", "--figma-api-key=YOUR-KEY", "--stdio"]
    }
  }
}
```

**Windows** — use `cmd` wrapper per [Getting Started](https://github.com/GLips/Figma-Context-MCP#getting-started).

**Quickstart:** https://www.framelink.ai/docs/quickstart

---

## Agent Skills

**Status:** ⚠️ Not yet published as a dedicated `npx skills add …` pack

Search community skills: `npx clawhub@latest search figma-developer-mcp`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ MCP server (`figma-developer-mcp`)

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/GLips/Figma-Context-MCP |
| **Transport** | stdio |
| **Compatible Clients** | Cursor (primary), other MCP-enabled coding tools |

---

## What It Does

Framelink MCP fetches **Figma file metadata via the Figma API** and **simplifies/translates** the payload so coding agents receive **layout- and styling-focused context** instead of noisy raw JSON. README positions it for **one-shot UI implementation** in agent mode when the user pastes a Figma link.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | H3: *"Give your **coding agent** access to your Figma data"*; describes Cursor agent mode workflow — [GitHub README](https://github.com/GLips/Figma-Context-MCP) |
| **Agent-specific primitive** | **LLM-compacted Figma design context** — curated fields for layout/style so the model implements UI with less hallucination than screenshots alone |
| **Autonomy-compatible control plane** | After token setup, agent pulls design context on demand via MCP tools without designer hand-exporting assets each time |
| **M2M integration surface** | MCP server + Figma REST API |
| **Identity / delegation** | **Figma personal access token** scopes what files/components the agent may read; actions attributable to that token's owner |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Figma link ingestion** | User pastes file/frame/group URL; agent triggers MCP fetch |
| **Context reduction** | Server filters to design-relevant layout/style signals |
| **MCP tool calls** | Standard MCP integration for coding hosts |
| **npm distribution** | `figma-developer-mcp` |

---

## Autonomy Model

```
Developer adds MCP server with Figma PAT
  ↓
User pastes Figma URL in agent chat
  ↓
Agent calls MCP tools to retrieve simplified design context
  ↓
Agent generates framework-specific UI code in one session
```

---

## Identity and Delegation Model

- **Figma PAT** — read access bounded by Figma permissions of the token creator.
- **No write path to Figma** by default — agent consumes design intelligence; code changes land in the repo under normal git auth.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **MCP** | stdio via `npx -y figma-developer-mcp …` |
| **Figma API** | https://www.figma.com/developers/api |

---

## Human-in-the-Loop Support

Designer retains control via **Figma sharing** and **token issuance**. Agents cannot access unpublished files without permission.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Screenshots only** | Lose structured layout/style; higher hallucination rate (per project claims) |
| **Raw Figma JSON in prompt** | Oversized, noisy context — Framelink explicitly **prunes** for LLMs |
| **Manual design handoff** | Breaks autonomous agent loops inside the IDE |

---

## Use Cases

- **Cursor/Copilot UI builds** — implement frames from a link in one agent session
- **Design-system adherence** — agent reads spacing, typography, and component structure from Figma
- **Cross-framework output** — same MCP context for React, Vue, or other targets
