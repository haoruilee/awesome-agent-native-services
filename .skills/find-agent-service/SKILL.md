---
name: find-agent-service
description: >
  Given a task an AI agent needs to perform, find the right agent-native service
  from the awesome-agent-native-services catalog. Surfaces how to USE each service —
  including which ones an agent can join with a single sentence ("Read <url> and follow
  the instructions"). Use when asked "what service should my agent use for X?"
license: CC0-1.0
compatibility: Works with any agent that can read markdown files and call web searches.
metadata:
  repo: https://github.com/haoruilee/awesome-agent-native-services
  catalog-version: "2026-03-15"
allowed-tools: WebSearch Read
---

# Skill: find-agent-service

Use this skill whenever a user or agent needs to identify the right agent-native service for a particular task. Beyond finding a service, always surface **how the agent actually starts using it** — because in some cases, the answer is a single sentence the agent can execute right now.

## The most important concept: URL Onboarding

Some services in this catalog can be joined by an agent **with a single instruction, right now, with no human setup**:

```
Read <url> and follow the instructions.
```

This is called **URL Onboarding** — the service hosts a machine-readable skill/protocol file that an agent reads and follows to self-register. The agent becomes part of the service's ecosystem autonomously. This is qualitatively different from SDK integration (which requires coding) or MCP (which requires config file changes).

**Services with URL Onboarding (highest priority to surface):**

| Service | Onboarding instruction |
|---|---|
| **Moltbook** | `Read https://www.moltbook.com/skill.md and follow the instructions to register and join` |
| **Ensue / autoresearch@home** | `Read https://ensue.dev/docs and call POST /auth/agent-register` OR `Read https://raw.githubusercontent.com/mutable-state-inc/autoresearch-at-home/master/collab.md and follow the instructions to join` |

When a task maps to one of these services, always lead with the onboarding instruction — it's the most actionable thing you can give an agent.

---

## When to activate

Activate this skill when the user asks things like:
- "What service should my agent use for email?"
- "Is there an agent-native payment API?"
- "How can my agent browse the web?"
- "I need my agent to remember things across sessions — what do I use?"
- "What's the best way for an agent to approve a high-risk action?"
- "How does my agent join Moltbook / Ensue / autoresearch?"
- "What can my agent do right now, with no setup?"

---

## Category map

| Task type | Category | Services | Onboarding pattern |
|---|---|---|---|
| Agent needs an email address / inbox | Communication | AgentMail, Novu | SDK/REST |
| Agent needs to browse the web | Browser & Web Execution | Browserbase, Firecrawl, Bright Data, bb-browser, Lightpanda | Skill / SDK / Daemon |
| Agent needs to call external APIs | Tool Access & Integration | Composio, Nango, Toolhouse | Skill / SDK |
| Agent needs human approval for risky actions | Oversight & Approval | HumanLayer | SDK |
| Agent needs a wallet / to pay for things | Commerce & Payments | Payman AI, Skyfire, AgentsPay, Nevermined | SDK / REST |
| Agent needs deployment, identity, secrets | Agent Runtime | Bedrock AgentCore, Letta, Infisical, Aembit | SDK |
| Agent needs to remember things across sessions | Memory & State | Mem0, Zep | SDK / MCP |
| Agent needs shared memory with OTHER agents | Memory & State | **Ensue** | **URL Onboarding** ⭐ |
| Agent needs unified context: memory + resources + skills | Memory & State | **OpenViking** | MCP / SDK |
| Agent needs a memory OS (parametric + activation + plaintext) | Memory & State | **MemOS** | MCP / SDK |
| Agent runs 24/7 and needs proactive monitoring memory | Memory & State | **memU** | SDK |
| Agent wants to earn money by doing tasks for other agents | **Agent Social / Commerce** | **Openwork** | Skill |
| Agent wants to find pen pals / form agent-to-agent relationships | **Agent Social** | **Shellmates** | REST |
| Agent needs to search the web | Search & Web Intelligence | Tavily, Exa | Skill / MCP |
| Agent needs to run generated code safely | Code Execution | E2B | SDK / MCP |
| Agent needs tracing / debugging | Observability | Langfuse | Skill |
| Agent needs long-running fault-tolerant tasks | Durable Execution | Trigger.dev, Inngest, Kitaru, Restate | Skill / SDK |
| Agent needs to join a meeting | Meeting & Conversation | Recall.ai | REST |
| Agent needs to make or receive phone calls | Voice & Phone | Vapi | SDK |
| Agent needs to control LLM costs and routing | LLM Gateway | Portkey | SDK |
| Agent wants to post, comment, build reputation | **Agent Social** | **Moltbook** | **URL Onboarding** ⭐ |

---

## How to find the right service

### Step 1 — Map the task to a category

Use the table above. Note the onboarding pattern — if it's **URL Onboarding**, you can give the agent a one-sentence instruction immediately.

### Step 2 — Read the category file

The catalog is at `services/{category}/README.md`. Read it to see all services and their onboarding commands.

**Category folder names (15 categories):**
- `services/communication/`
- `services/browser-and-web-execution/`
- `services/tool-access-and-integration/`
- `services/oversight-and-approval/`
- `services/commerce-and-payments/`
- `services/agent-runtime-and-infrastructure/`
- `services/memory-and-state/`
- `services/search-and-web-intelligence/`
- `services/code-execution/`
- `services/observability-and-tracing/`
- `services/durable-execution-and-scheduling/`
- `services/meeting-and-conversation/`
- `services/voice-and-phone/`
- `services/llm-gateway-and-routing/`
- `services/agent-social-network/`

### Step 3 — Read the service file

Each service has a detailed file at `services/{category}/{service-name}.md` containing:
- **How to Use (Agent Onboarding)** — the quickest entry point (always check this first)
- Primary primitives (the agent-specific abstractions)
- Protocol surface (SDK, REST API, MCP, webhooks)
- Agent Skills install command
- MCP server details
- Use cases with concrete examples

### Step 4 — Recommend with the right entry point

Match the recommendation to the onboarding pattern:

```
## Recommended service: {Service Name}

**Why:** {specific primitive that matches the task}

**How to start** ({URL Onboarding / Coding-time Skill / MCP / SDK / Daemon}):
{one-line instruction appropriate to the pattern}

URL Onboarding example:
  Read https://www.moltbook.com/skill.md and follow the instructions to register and join.

Coding-time Skill example:
  npx skills add tavily-ai/skills

MCP example:
  Add to mcp_servers: { "command": "npx", "args": ["-y", "bb-browser", "--mcp"] }

SDK example:
  pip install mem0ai  # then: m.add(messages, user_id="agent-1")

**Relevant use case from the catalog:**
> {quote the use case that matches the task}
```

---

## When nothing fits

If no service in the current catalog fits the task:
1. Say so clearly — do not recommend an `agent-adapted` service as if it were `agent-native`.
2. Note the closest existing service and explain what is missing.
3. Suggest opening a [new service issue](https://github.com/haoruilee/awesome-agent-native-services/issues/new?template=01-new-service.yml) if the user knows of a qualifying service.

---

## Classification reminder

This catalog only lists `agent-native` services. Do not recommend:
- `agent-adapted` services (e.g., Resend, Stripe, Twilio) — built for humans, agent layers added later.
- `agent-builder` platforms (e.g., Dify, n8n, LangGraph) — for humans building agents.

If asked about those, explain the distinction and point to the `Excluded / Boundary Cases` section in `README.md`.
