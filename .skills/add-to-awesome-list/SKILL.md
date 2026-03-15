---
name: add-to-awesome-list
description: >
  Guide a contributor through the full process of adding a new service to the
  awesome-agent-native-services catalog: verifying criteria, opening an issue,
  writing the service file in the correct format, and submitting a PR.
  Use this when the user says "I want to add X to the list" or "how do I contribute?"
license: CC0-1.0
compatibility: Works with any agent that can read, write, and use git.
metadata:
  repo: https://github.com/haoruilee/awesome-agent-native-services
  catalog-version: "2026-03"
allowed-tools: WebSearch Read Write Shell
---

# Skill: add-to-awesome-list

Use this skill to walk a contributor through the complete process of adding a new service to the awesome-agent-native-services catalog, from initial eligibility check through a merged PR.

## When to activate

Activate when the user says:
- "I want to add [service] to the list."
- "How do I contribute a new service?"
- "I found a service that should be in the catalog."
- "Walk me through the contribution process."

## Phase 1 — Pre-flight eligibility check

Before writing anything, verify the service qualifies.

### 1.1 Check for duplicates

```
1. Read README.md — search for the service name in all 12 category sections.
2. Search open issues: https://github.com/haoruilee/awesome-agent-native-services/issues?q=<service-name>
3. If found: report the existing entry or issue URL and stop.
```

### 1.2 Apply the five criteria

Use the `evaluate-agent-native` skill (or apply the criteria inline):

For each criterion, find **evidence from the official homepage or docs** — a direct quote or specific API documentation. Do not infer. Do not use marketing blog posts alone.

If any criterion fails: tell the user clearly which criterion failed, why, and what the correct classification is (`agent-adapted` or `agent-builder`). Do not proceed to Phase 2.

### 1.3 Determine the category

Use this map:

| What the service does | Category folder |
|---|---|
| Gives agents a communication identity (email, messaging) | `communication/` |
| Provides remote browser or web extraction for agents | `browser-and-web-execution/` |
| Runtime tool discovery, delegated OAuth, managed tool execution | `tool-access-and-integration/` |
| Agent-initiated human approval gates | `oversight-and-approval/` |
| Agent wallets, KYA identity, autonomous payment execution | `commerce-and-payments/` |
| Execution environments, session isolation, secrets, gateway | `agent-runtime-and-infrastructure/` |
| Persistent, self-managing agent memory | `memory-and-state/` |
| LLM-optimized web search and content retrieval | `search-and-web-intelligence/` |
| Secure sandboxes for AI-generated code | `code-execution/` |
| Agent trajectory tracing, evaluation, cost attribution | `observability-and-tracing/` |
| Fault-tolerant long-running agent workflows | `durable-execution-and-scheduling/` |
| Agent presence in voice/video meetings | `meeting-and-conversation/` |

If none fit, consider whether a new category is needed (requires 2+ qualifying services — see the new category issue template).

---

## Phase 2 — Open a GitHub issue

**Do not write the PR before the issue is approved.**

Direct the user to open an issue using the structured template:

```
Issue URL: https://github.com/haoruilee/awesome-agent-native-services/issues/new?template=01-new-service.yml
```

Help the user fill in the required fields:
- **Service name** and **official website**
- **Official tagline** — exact quote from the homepage
- **Proposed category** — from Phase 1
- **Criterion evidence** — one field per criterion, quote + source URL
- **MCP status** — is there a published MCP server? Link it.
- **Agent Skills status** — is there a published `SKILL.md`? Provide the install command.
- **Classification** — `agent-native`
- **Generic alternative comparison** — name the obvious human-facing alternative and why it fails

After submission, wait for a maintainer ✅ Go before proceeding.

---

## Phase 3 — Write the service file

Once the issue has a ✅ Go, create the service file.

### File location

```
services/{category-folder}/{service-name}.md
```

**Naming rules:**
- All lowercase
- Hyphens only (no underscores, no spaces)
- Match the service's common name
- Examples: `agentmail.md`, `trigger-dev.md`, `amazon-bedrock-agentcore.md`

### Required sections (in this order)

Every service file must contain all 13 sections. Use the template below.

```markdown
# {Service Name}

> **"{Official tagline from homepage — exact quote}"**

| | |
|---|---|
| **Website** | https://... |
| **Docs** | https://... |
| **GitHub** | https://... (if public) |
| **Classification** | `agent-native` |
| **Category** | [{Category Name}](README.md) |
| **Funding** | (optional: e.g., $6M seed · Y Combinator) |
| **Compliance** | (optional: e.g., SOC 2 Type I) |

---

## Official Website

https://...

---

## Official Repo

https://github.com/...

(If multiple repos, list each with a brief label.)

---

## Agent Skills

**Status:** ✅ Available / ⚠️ Not yet published

<!-- If available: -->
```bash
npx skills add {org/repo}
```

| Skill | What It Teaches the Agent |
|---|---|
| `skill-name` | One-line description |

**Compatibility:** Claude Code, Cursor, Codex, and all AgentSkills-compatible tools.

<!-- If not available: -->
No official skill published yet. Search community skills:
```bash
npx clawhub@latest search {service-name}
```
See https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available / ⚠️ Not yet published

<!-- If available: -->
| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/... |
| **Transport** | stdio / Streamable HTTP |
| **Auth** | API key env var name |
| **Compatible Clients** | Claude Desktop, Cursor, Windsurf, ... |

<!-- If not available: -->
No MCP server published yet. Integration is via REST API / SDK.

---

## What It Does

One to three paragraphs explaining what the service does and why it is agent-native.
The core abstraction should be stated clearly: **{the agent-specific thing}**.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "{exact quote}" — {source URL} |
| **Agent-specific primitive** | {description of the primitive with no human equivalent} |
| **Autonomy-compatible control plane** | {how agents operate without per-action human confirmation} |
| **M2M integration surface** | {SDK name + install command, REST API URL, MCP server, webhooks} |
| **Identity / delegation** | {how agent identity, delegated permissions, and audit trail work} |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **{Name}** | {one sentence} |

(List 4–10 primitives. Each should be a distinct, named agent-specific abstraction.)

---

## Autonomy Model

Step-by-step numbered list showing how an agent uses the service end-to-end without human intervention. Use code blocks for API calls where relevant.

```
Step 1: Agent calls {endpoint} → receives {result}
Step 2: ...
Step N: {final outcome, no human clicked anything}
```

---

## Identity and Delegation Model

Bullet list explaining:
- How the agent gets its own identity (not shared with a human)
- How permissions are delegated from operator/user to agent
- How the audit trail attributes actions to the specific agent

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | {base URL or description} |
| Python SDK | `pip install {package}` |
| TypeScript SDK | `npm install {package}` |
| MCP Server | {repo URL or "not yet available"} |
| Webhooks | {event types} |

---

## Human-in-the-Loop Support

One paragraph. Is HITL required? Optional? How is it integrated?

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **{Name}** | {specific reason referencing criteria} |

(List 3–5 obvious human-facing alternatives and why each fails.)

---

## Use Cases

- **{Use case title}** — {one sentence description of how an agent uses this service}

(List 4–6 concrete, specific use cases.)
```

### Research checklist for each section

Before writing each section, verify the information from primary sources:

- [ ] **Official Website / Repo**: from the service's GitHub or homepage
- [ ] **Agent Skills**: check skills.sh, agentskills.io, and the service's GitHub for `SKILL.md` files
- [ ] **MCP**: check the service's GitHub for `mcp-server` repos; check mcp.so, glama.ai/mcp, smithery.ai
- [ ] **Why It Is Agent-Native**: direct quotes from docs.{service}.com or {service}.com/docs
- [ ] **Protocol Surface**: check the SDK README for install commands
- [ ] **Use Cases**: sourced from the service's own documentation, not invented

---

## Phase 4 — Update the index files

After creating the service file, update two more files:

### 4.1 Update `services/{category}/README.md`

Add a row to the service table:

```markdown
| [{Service Name}]({service-name}.md) | {tagline} | {key primitives} | ✅/⚠️ |
```

### 4.2 Update root `README.md`

Find the correct category section and add a row to the summary table:

```markdown
| [{Service Name}](services/{category}/{service-name}.md) | {tagline} | {key primitives} | ✅/⚠️ |
```

---

## Phase 5 — Open the PR

### PR title format

```
[New Service] {Service Name}
```

### PR body checklist

The PR template (`.github/PULL_REQUEST_TEMPLATE.md`) will auto-populate. Fill in:
- [ ] Linked issue: `Closes #{issue number}`
- [ ] Five-criterion evidence table
- [ ] All 13 required sections confirmed
- [ ] Classification confirmed as `agent-native`
- [ ] Conflict-of-interest declaration

### Git commands

```bash
git checkout -b add-{service-name}
git add services/{category}/{service-name}.md
git add services/{category}/README.md
git add README.md
git commit -m "[New Service] {Service Name}

Closes #{issue number}

- Category: {category}
- MCP: {✅ available / ⚠️ not yet}
- Agent Skills: {✅ available / ⚠️ not yet}"
git push origin add-{service-name}
```

Then open a PR on GitHub targeting the `main` branch.

---

## Quality checklist before submitting

- [ ] All links are live (clicked each one)
- [ ] Official tagline is an exact quote from the homepage (in quotation marks)
- [ ] All criterion evidence cites a specific URL
- [ ] Service file name is lowercase with hyphens only
- [ ] All 13 required sections are present
- [ ] Agent Skills section shows real install commands (not invented)
- [ ] MCP section shows real repo/transport (not invented)
- [ ] No undisclosed financial interest in the service
