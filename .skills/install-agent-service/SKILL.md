---
name: install-agent-service
description: >
  Use the Awesome Agent-Native Services catalog as an installation entry point.
  Given a task or service name, return the exact install/onboarding command for
  catalog services that expose Agent Skills, Claude Code plugins, URL onboarding,
  MCP servers, CLIs, or SDKs.
license: CC0-1.0
compatibility: Works with Claude Code plugin skills and agents that can read SKILL.md.
metadata:
  repo: https://github.com/haoruilee/awesome-agent-native-services
  catalog-version: "2026-09-03"
allowed-tools: WebSearch Read Bash
---

# Skill: install-agent-service

Use this skill when a user asks to **install**, **connect**, **enable**, **add a skill/plugin**, or **turn the catalog into an entry point** for an agent-native service.

This skill does **not** blindly run third-party code. It returns a ranked install path and asks the host agent/operator to execute the command appropriate for its environment.

---

## Installability tiers

Prefer the highest available tier:

1. **Repository plugin/skill** — install this repo as a plugin/skill hub, then invoke a catalog skill.
2. **URL Onboarding** — agent reads a machine-readable URL and self-registers.
3. **Agent Skill / Claude Code plugin** — explicit skill installation command exists.
4. **MCP server** — add a stdio or remote MCP endpoint.
5. **CLI / SDK** — install package and call documented API.

When multiple tiers exist, show the highest tier first and include lower-tier fallbacks.

---

## Install this repository as the entry point

### Claude Code plugin marketplace

```text
/plugin marketplace add haoruilee/awesome-agent-native-services
/plugin install awesome-agent-native-services@awesome-agent-native-services
/reload-plugins
```

After install, invoke:

```text
/awesome-agent-native-services:find-agent-service <task>
/awesome-agent-native-services:install-agent-service <service or task>
/awesome-agent-native-services:evaluate-agent-native <service URL>
/awesome-agent-native-services:add-to-awesome-list <candidate>
```

### Manual SKILL.md install

```bash
mkdir -p ~/.claude/skills
cp -R .skills/install-agent-service ~/.claude/skills/
```

---

## Catalog services with first-class install/onboarding commands

### URL Onboarding — agent can start from one instruction

| Service | Install / onboarding instruction |
|---|---|
| Moltbook | `Read https://www.moltbook.com/skill.md and follow the instructions to register and join` |
| Ensue | `Read https://ensue.dev/docs and call POST https://api.ensue-network.ai/auth/agent-register` |
| autoresearch@home | `Read https://raw.githubusercontent.com/mutable-state-inc/autoresearch-at-home/master/collab.md and follow the instructions to join` |
| db9 | `Read https://db9.ai/skill.md and follow the instructions` |
| mem9 | `Read https://mem9.ai/skill.md and follow the instructions to register and join` |
| mails.dev | `Read https://mails.dev/skill.md and follow the instructions` |
| MailboxKit | `Read https://mailboxkit.com/skill.md and follow the instructions` |
| Agents Mail | `Read https://agentsmail.org/skill.md and follow the instructions` |

### Agent Skills / plugin-native entries

| Service | Install command |
|---|---|
| Browserbase | `npx skills add browserbase/skills` |
| Firecrawl | `npx skills add firecrawl/cli` |
| Novu | `npx skills add novuhq/skills` |
| Composio | `npx skills add composiohq/skills` |
| Trigger.dev | `npx skills add triggerdotdev/skills` |
| Inngest | `npx skills add inngest/inngest-skills` |
| Tavily | `npx skills add tavily-ai/skills` |
| Langfuse | `npx skills add https://github.com/langfuse/skills --skill langfuse-observability` |
| Openwork | `npx playbooks add skill openclaw/skills --skill openwork` |

### MCP-first entries with one-command local or remote setup

| Service | MCP install / endpoint |
|---|---|
| Browser MCP | `npx -y @browsermcp/mcp` |
| Playwright MCP | `npx @playwright/mcp@latest` |
| Chrome DevTools MCP | `npx -y chrome-devtools-mcp@latest` |
| Bright Data Agent Browser | `npx -y @brightdata/mcp` |
| Hyperbrowser | `npx hyperbrowser-mcp <API_KEY>` |
| Olostep | `npx -y olostep-mcp` or remote `https://mcp.olostep.com/mcp` |
| Framelink MCP for Figma | `npx -y figma-developer-mcp --figma-api-key=... --stdio` |
| GitHub MCP Server | Remote endpoint: `https://api.githubcopilot.com/mcp/` |
| MCP Toolbox for Databases | `npx -y @toolbox-sdk/server --prebuilt=postgres` |
| Infisical Agent Sentinel | `npx -y @infisical/mcp` |
| Memoria | `memoria mcp` |
| Recall | `uvx ai-recallworks stdio` |
| Kitaru | `uv add "kitaru[cli,worker,mcp]"` then `npx skills add zenml-io/kitaru-skills`; MCP: `kitaru-mcp` per https://docs.zenml.io/kitaru |
| MCP-Cloud (mcp-agent) | `uvx mcp-agent login` then `uvx mcp-agent deploy ...` |
| Meeting BaaS | Use `meeting-mcp` from upstream docs |
| Vexa | Self-host Vexa, then enable its MCP server |
| Retell AI | Configure Retell MCP/tools from docs |
| Agentgateway | Run `agentgateway -f config.yaml` with MCP routing enabled |

### CLI / SDK-first entries that are still actionable from the catalog

| Service | Quick install |
|---|---|
| Vercel Agent Browser | `npm install -g agent-browser` |
| bb-browser | `npm install -g bb-browser` plus the Chrome extension |
| OpenCLI | `npm install -g @jackwener/opencli` |
| Steel | `pip install steel-sdk` |
| Notte | `pip install notte-sdk` |
| E2B | `pip install e2b-code-interpreter` |
| Daytona | Install the Daytona CLI/SDK from upstream docs |
| Riza | Install the Riza SDK or MCP server from upstream docs |
| HumanLayer | `pip install humanlayer` |
| Payman AI | `npm install @paymanai/payman-node` |
| Nevermined | `pip install payments-py` |
| Mem0 | `pip install mem0ai` |
| Zep | `pip install zep-python` |
| Cognee | `pip install cognee` |
| Agent Trace | Install `agent-strace` from PyPI/GitHub, then wrap agent runs |
| agent-inspect | Add to a TypeScript agent project |
| Vapi | `pip install vapi-server-sdk` |
| Pipecat | `pip install pipecat-ai` |
| LiteLLM | Self-host proxy from upstream docs |
| Portkey | `pip install portkey-ai` |

---

## Response format

When invoked, answer with:

~~~markdown
## Install path for <service/task>

**Best entry point:** <repository skill / URL onboarding / Agent Skill / MCP / CLI / SDK>

**Command:**
```bash
<exact command or instruction>
```

**Fallbacks:**
- <fallback 1>
- <fallback 2>

**Catalog source:** `services/<category>/<service>.md`
~~~

If a service is not listed above, read the service file and extract its `How to Use`, `Agent Skills`, and `MCP` sections before answering.
