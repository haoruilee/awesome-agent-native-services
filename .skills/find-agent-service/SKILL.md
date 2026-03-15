---
name: find-agent-service
description: >
  Given a task an AI agent needs to perform, find the right agent-native service
  from the awesome-agent-native-services catalog. Use this when the user asks
  "what service should my agent use for X?" or "is there an agent-native way to do Y?"
license: CC0-1.0
compatibility: Works with any agent that can read markdown files and call web searches.
metadata:
  repo: https://github.com/haoruilee/awesome-agent-native-services
  catalog-version: "2026-03"
allowed-tools: WebSearch Read
---

# Skill: find-agent-service

Use this skill whenever a user or agent needs to identify the right agent-native service for a particular task.

## When to activate

Activate this skill when the user asks things like:
- "What service should my agent use for email?"
- "Is there an agent-native payment API?"
- "How can my agent browse the web?"
- "I need my agent to remember things across sessions — what do I use?"
- "What's the best way for an agent to approve a high-risk action?"

## Category map

Use this map to quickly narrow down the relevant category before looking up the specific service:

| Task type | Category | Services to check |
|---|---|---|
| Agent needs an email address / inbox | Communication | AgentMail |
| Agent needs to browse the web, click, fill forms | Browser & Web Execution | Browserbase, Firecrawl |
| Agent needs to call external APIs (GitHub, Slack, Salesforce…) | Tool Access & Integration | Composio, Nango, Toolhouse |
| Agent needs a human to approve a risky action | Oversight & Approval | HumanLayer |
| Agent needs to pay for something / has a wallet | Commerce & Payments | Payman AI, Skyfire, AgentsPay, Nevermined |
| Agent needs to be deployed, have its own identity, secrets | Agent Runtime & Infrastructure | Amazon Bedrock AgentCore, Infisical Agent Sentinel |
| Agent needs to remember things across sessions | Memory & State | Mem0 |
| Agent needs to search the web | Search & Web Intelligence | Tavily, Exa |
| Agent needs to run generated code safely | Code Execution | E2B |
| Agent needs its actions traced / debugged / evaluated | Observability & Tracing | Langfuse |
| Agent needs to run long tasks without timeouts | Durable Execution & Scheduling | Trigger.dev, Inngest |
| Agent needs to join a meeting / get transcripts | Meeting & Conversation | Recall.ai |

## How to find the right service

### Step 1 — Map the task to a category

Read the task description. Use the category map above to identify the relevant category (or categories).

### Step 2 — Read the category file

The catalog is organized at `services/{category}/README.md`. Read the category README to understand which services are available and what criteria they meet.

**Category folder names:**
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

### Step 3 — Read the service file

Each service has a detailed file at `services/{category}/{service-name}.md` containing:
- What it does
- Primary primitives (the agent-specific abstractions)
- Protocol surface (SDK, REST API, MCP, webhooks)
- Agent Skills install command (`npx skills add ...`)
- MCP server details
- Use cases with concrete examples

### Step 4 — Recommend with evidence

When recommending a service, always include:
1. **Why this service specifically** — which primitive matches the user's task
2. **The install or integration path** — SDK, MCP, or Agent Skills command
3. **A concrete next step** — link to the service's docs or the skill install command

## Output format

```
## Recommended service: {Service Name}

**Why:** {specific primitive or feature that matches the task}

**Get started:**
- Website: {url}
- Docs: {url}
- Agent Skills: `npx skills add {org/repo}` (if available)
- MCP: {server url or "not yet available"}

**Relevant use case from the catalog:**
> {quote the use case from the service file that matches the task}
```

## When nothing fits

If no service in the current catalog fits the task:
1. Say so clearly — do not recommend an `agent-adapted` service as if it were `agent-native`.
2. Note the closest existing service and explain what is missing.
3. Suggest opening a [new service issue](https://github.com/haoruilee/awesome-agent-native-services/issues/new?template=01-new-service.yml) if the user knows of a qualifying service.

## Classification reminder

This catalog only lists `agent-native` services. Do not recommend:
- `agent-adapted` services (e.g., Resend, Stripe, Twilio) — they were built for humans and have agent layers added.
- `agent-builder` platforms (e.g., Dify, n8n, LangGraph) — they are for humans building agents, not services agents consume.

If the user asks about those, explain the distinction and point them to the `Excluded / Boundary Cases` section in `README.md`.
