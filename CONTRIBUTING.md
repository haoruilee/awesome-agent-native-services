# Contributing to Awesome Agent-Native Services

This repository maintains a curated list of services **designed from the ground up for AI agents**. Quality over quantity: every entry must meet strict criteria, follow a consistent format, and remain accurate over time.

---

## Table of Contents

1. [The Five Hard Criteria](#1-the-five-hard-criteria)
2. [Bonus Signals](#2-bonus-signals)
3. [Explicit Exclusions](#3-explicit-exclusions)
4. [Contribution Workflow](#4-contribution-workflow)
5. [Issue Types and Templates](#5-issue-types-and-templates)
6. [PR Rules](#6-pr-rules)
7. [Service File Format](#7-service-file-format)
8. [Repository Structure](#8-repository-structure)
9. [Category Guidelines](#9-category-guidelines)
10. [Maintenance Responsibilities](#10-maintenance-responsibilities)
11. [Code of Conduct](#11-code-of-conduct)

---

## 1. The Five Hard Criteria

A service must satisfy **all five** to be listed.

### 1.1 Agent-First Positioning

The official website or documentation must explicitly identify AI agents as the **primary consumer** — not a secondary use case, not an integration footnote, not a marketing addition.

**Pass examples:**
- "Email for AI agents" (AgentMail)
- "A web browser for AI agents & applications" (Browserbase)
- "Human in the Loop for AI Agents" (HumanLayer)
- "Identity and payments for autonomous AI agents" (Skyfire)

**Fail examples:**
- "Powerful automation platform — now with AI agent support"
- "Build apps, workflows, and AI agents" (agents are one of many outputs)
- "The developer platform for everything" (agents mentioned in a blog post)

### 1.2 Agent-Specific Primitives

The API must expose **primitives that only make sense for agents** — abstractions with no meaningful human-facing equivalent. If a human developer would use the exact same API without modification to build a human-facing product, the service does not qualify.

**Pass examples:**
- Agent inbox (not a user inbox) with webhook-on-inbound-message
- Approval gate with denial-feedback injection into the agent's context window
- Know Your Agent (KYA) identity token
- Remote browser session lifecycle controlled by an agent
- Durable step checkpoint between LLM calls

**Fail examples:**
- A standard REST CRUD API that happens to be callable by an agent
- A webhook that any server can receive
- An email API that requires a human Gmail account

### 1.3 Autonomy-Compatible Control Plane

The service must allow agents to operate **without per-action human confirmation**, while providing agent-appropriate constraint mechanisms (spending limits, policy gates, session isolation, approval gates, etc.).

The key question: *Can an agent complete a full task loop — including the actions this service provides — without a human clicking anything?*

### 1.4 Machine-to-Machine Integration Surface

The **primary interface** must be an SDK, REST API, MCP server, or webhook. A human-facing management dashboard is acceptable as a secondary surface but must not be required for the agent's operational flow.

### 1.5 Agent Identity / Delegation Semantics

Where the service involves external actions (payments, sending emails, executing tools, making API calls on behalf of users), it must:

- Distinguish the **agent's own identity** from the user's identity
- Model **delegated permissions** — what the agent is authorized to do on the user's behalf
- Maintain an **audit trail** attributable to the specific agent

---

## 2. Bonus Signals

These are not required, but strengthen an entry. Entries with more bonus signals are more clearly agent-native.

| Signal | Why it matters |
|---|---|
| Dedicated agent identity model | Agent gets its own credential/wallet/token — not sharing a human's |
| MCP (Model Context Protocol) support | Native integration with the emerging agent tool standard |
| Published Agent Skills (`SKILL.md`) | Installable via `npx skills add` — extends coding agents directly |
| Per-agent state / memory / session | Service isolates state by agent, not just by user |
| Audit / trajectory / replay / approval artifacts | Service generates machine-readable evidence of agent actions |

---

## 3. Explicit Exclusions

The following categories are **not eligible** regardless of marketing language:

| Category | Why excluded | Example |
|---|---|---|
| **Agent builders** | Humans configure, orchestrate, or visually assemble agents | Dify, n8n, Flowise, AutoGen Studio, LangGraph |
| **RAG studios** | Help humans build retrieval pipelines | LlamaIndex Cloud, Cohere Compass |
| **Chat workspaces** | Designed for humans to interact with AI | ChatGPT Teams, Claude.ai, Notion AI |
| **No-code AI platforms** | Target non-technical users building AI apps | Voiceflow, Botpress |
| **Agent-adapted services** | Originally human-facing, agent interface added later | Resend (added MCP), Stripe (added Agent Toolkit), Twilio |

> **Agent-adapted services** belong in the `Excluded / Boundary Cases` section of `README.md`, not the main list. They are not wrong — they are in the wrong list.

---

## 4. Contribution Workflow

### Step 1 — Check before you start

1. Search [open and closed issues](../../issues?q=) to see if your service has been discussed.
2. Check the [current list](../../blob/main/README.md) — the service may already be listed.
3. Read the [five criteria](#1-the-five-hard-criteria) honestly. If you are unsure, open an issue before writing any files.

### Step 2 — Open an issue

**All new service proposals require a pre-approved issue before a PR is opened.** This prevents wasted work on entries that do not qualify.

Use the appropriate issue template:

| Scenario | Template |
|---|---|
| Proposing a new service | [🆕 New service](../../issues/new?template=01-new-service.yml) |
| Reporting outdated info / broken link / new MCP / new Skills | [✏️ Update entry](../../issues/new?template=02-update-entry.yml) |
| Service shut down / pivoted / should be removed | [🚩 Flag service](../../issues/new?template=03-flag-service.yml) |
| Proposing a new category | [📂 New category](../../issues/new?template=04-new-category.yml) |

> **Exception:** PRs that fix broken links, typos, or obvious factual errors may be opened directly without a prior issue.

### Step 3 — Wait for maintainer review

A maintainer will respond to new service issues within **7 days** with one of:
- ✅ **Go** — proceed with the PR
- ❌ **No-go** — explanation of which criterion is not met
- ❓ **Needs clarification** — follow-up questions before a decision

Do not open a PR until you receive a ✅ Go on your issue.

### Step 4 — Write the PR

Follow the [service file format](#7-service-file-format) exactly. Use the [PR template](PULL_REQUEST_TEMPLATE.md) checklist to verify your submission is complete.

**PR title format:**

| Type | Format |
|---|---|
| New service | `[New Service] ServiceName` |
| Update existing | `[Update] ServiceName — what changed` |
| Fix (no issue needed) | `[Fix] brief description` |
| New category | `[New Category] CategoryName` |
| Maintenance | `[Maintenance] brief description` |

### Step 5 — Review and merge

- Maintainers review PRs within **14 days**.
- Minor formatting issues may be requested via review comments.
- Once approved, a maintainer merges the PR and closes the linked issue.

---

## 5. Issue Types and Templates

### 🆕 New Service Proposal

**Template:** `.github/ISSUE_TEMPLATE/01-new-service.yml`

Required information:
- Service name, website, official repo
- Official tagline (exact quote from homepage)
- Proposed category
- Evidence for each of the five criteria (quote + source URL)
- MCP status and Agent Skills install command (if available)
- Classification (`agent-native` / `agent-adapted` / `agent-builder`)
- Why the obvious generic alternative does not qualify

### ✏️ Update Existing Entry

**Template:** `.github/ISSUE_TEMPLATE/02-update-entry.yml`

Required information:
- Service name and file path
- Current (incorrect) content — exact quote
- Proposed replacement content
- Source URL confirming the change

Use this for: broken links, new MCP server, new Agent Skills, pricing/tier changes, new primitives, rebranding.

### 🚩 Flag or Remove a Service

**Template:** `.github/ISSUE_TEMPLATE/03-flag-service.yml`

Required information:
- Service name and file path
- Reason (shut down / pivoted / never qualified / acquired)
- Evidence with source URLs
- Proposed action (remove / reclassify / deprecation notice)

### 📂 New Category Proposal

**Template:** `.github/ISSUE_TEMPLATE/04-new-category.yml`

Required information:
- Proposed category name
- What agent-specific problem it solves (distinct from existing categories)
- Why existing categories are insufficient
- At least **two** qualifying services with criterion evidence

---

## 6. PR Rules

### Must-haves for all PRs

- [ ] PR title follows the format above.
- [ ] All links in modified files are live (you have clicked them).
- [ ] No undisclosed financial interest in any mentioned service.

### Must-haves for new service PRs

- [ ] Linked issue has a ✅ Go from a maintainer.
- [ ] Created `services/{category}/{service-name}.md` with all required sections.
- [ ] Added a row to `services/{category}/README.md`.
- [ ] Added a row to the correct section of the root `README.md`.
- [ ] Classification is `agent-native` (not `agent-adapted` or `agent-builder`).

### Must-haves for update PRs

- [ ] Source URL confirming the change is included.
- [ ] Classification was not changed without a prior issue.

### What gets a PR rejected

- Missing required sections in the service file
- No linked issue for a new service
- Classification as `agent-native` without meeting all five criteria
- Broken links in the submitted file
- Undisclosed conflict of interest

---

## 7. Service File Format

Every service file at `services/{category}/{service-name}.md` must contain all of the following sections in this order:

```markdown
# Service Name

> **"Official tagline from the homepage."**

| | |
|---|---|
| **Website** | https://... |
| **Docs** | https://... |
| **GitHub** | https://... |
| **Classification** | `agent-native` |
| **Category** | [Category Name](README.md) |
| **Funding / Compliance** | (if notable) |

---

## Official Website

https://...

---

## Official Repo

https://github.com/...

---

## How to Use (Agent Onboarding)

**The quickest path for an agent to start using this service.**

Identify which [interaction pattern](../README.md#how-agents-interact-with-these-services) applies and provide the corresponding entry point:

```
# URL Onboarding:
Read <url> and follow the instructions to register and join.

# MCP:
Add to mcp_servers: "command": "npx", "args": ["-y", "<package>", "--mcp"]

# Coding-time Skill:
npx skills add <org>/<repo>

# SDK / REST:
pip install <package>  # then: <one-line first API call>

# Daemon / Extension:
npm install -g <package>  # then: run daemon + install extension
```

---

## Agent Skills

**Status:** ✅ Available / ⚠️ Not yet published

<!-- If available: -->
```bash
npx skills add org/repo
```

| Skill | What It Teaches the Agent |
|---|---|
| `skill-name` | Description |

<!-- If not available: -->
Search community skills: `npx clawhub@latest search service-name`
See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available / ⚠️ Not yet published

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/... |
| **Transport** | stdio / Streamable HTTP |
| **Compatible Clients** | Claude Desktop, Cursor, ... |

---

## What It Does

One to three paragraphs.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Exact quote + source URL |
| **Agent-specific primitive** | Description |
| **Autonomy-compatible control plane** | Description |
| **M2M integration surface** | List of interfaces |
| **Identity / delegation** | Description |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Name** | Description |

---

## Autonomy Model

Step-by-step flow showing how an agent uses the service without human intervention.

---

## Identity and Delegation Model

Bullet list explaining agent identity, delegated permissions, audit trail.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | ... |
| Python SDK | ... |

---

## Human-in-the-Loop Support

Description of whether and how HITL is supported.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Name** | Explanation |

---

## Use Cases

- **Use case name** — description
```

### Naming conventions

- File name: lowercase, hyphens only, matches the service's common name. Examples: `agentmail.md`, `amazon-bedrock-agentcore.md`, `trigger-dev.md`
- Category folder: lowercase, hyphens only. Examples: `commerce-and-payments/`, `browser-and-web-execution/`

---

## 8. Repository Structure

```
README.md                                    ← Index: category tables + service summary tables
CONTRIBUTING.md                              ← This file
.github/
  ISSUE_TEMPLATE/
    01-new-service.yml                       ← New service proposal template
    02-update-entry.yml                      ← Update existing entry template
    03-flag-service.yml                      ← Flag / remove service template
    04-new-category.yml                      ← New category proposal template
    config.yml                               ← Disables blank issues
  PULL_REQUEST_TEMPLATE.md                   ← PR checklist
services/
  {category}/
    README.md                                ← Category overview, rationale, criteria, service table
    {service-name}.md                        ← Full per-service detail file
```

**When adding a new service, you must update three places:**

1. Create `services/{category}/{service-name}.md`
2. Add a row to `services/{category}/README.md` (service table)
3. Add a row to the correct section of the root `README.md` (summary table)

**When adding a new category, you must update four places:**

1. Create `services/{new-category}/README.md`
2. Create at least one `services/{new-category}/{service-name}.md`
3. Add the category to the root `README.md` (categories table + new section)
4. Add the category to the Category Guidelines table in this file

---

## 9. Category Guidelines

Use existing categories wherever possible. Propose a new one only when at least two qualifying services do not fit any existing category.

| Category folder | What belongs here |
|---|---|
| `communication/` | Services giving agents a first-class communication identity (email, messaging, notifications) |
| `browser-and-web-execution/` | Remote browser sessions and intent-driven web extraction for agents |
| `tool-access-and-integration/` | Runtime tool discovery, delegated OAuth, and managed tool execution |
| `oversight-and-approval/` | Agent-initiated human approval gates, denial feedback, and escalation |
| `commerce-and-payments/` | Agent wallets, KYA identity, autonomous payment execution |
| `agent-runtime-and-infrastructure/` | Execution environments, session isolation, secrets, tool gateway, identity tokens |
| `memory-and-state/` | Persistent, queryable, self-managing agent memory across sessions |
| `search-and-web-intelligence/` | LLM-optimized web search and structured content retrieval |
| `code-execution/` | Secure, isolated sandboxes for AI-generated code |
| `observability-and-tracing/` | Agent trajectory tracing, evaluation datasets, cost attribution |
| `durable-execution-and-scheduling/` | Fault-tolerant long-running workflows with checkpointing and HITL |
| `meeting-and-conversation/` | Agent presence (bots) in voice and video meetings |
| `voice-and-phone/` | Agent-controlled voice calls and phone infrastructure |
| `llm-gateway-and-routing/` | Per-agent LLM routing, budget, fallback, and observability |
| `agent-social-network/` | Social networks and communities where agents are first-class participants |

---

## 10. Maintenance Responsibilities

### Keeping entries current

Anyone can open an [✏️ Update issue](../../issues/new?template=02-update-entry.yml) to report a stale entry. Common triggers:

- A service's MCP server is published → update the MCP section status from ⚠️ to ✅
- A service publishes Agent Skills → update the Agent Skills section with the install command
- A pricing tier changes → update the Pricing section if present
- The homepage changes its tagline or positioning → update the quote and verify the criteria
- A link returns 404 → fix immediately via a direct PR (no issue needed)

### Flagging dead or pivoted services

If a service shuts down or pivots away from agent-native positioning, open a [🚩 Flag issue](../../issues/new?template=03-flag-service.yml). The service will be either removed or moved to the `Excluded / Boundary Cases` section in `README.md` depending on the situation.

### Agent Skills update cadence

The Agent Skills ecosystem is evolving quickly. When a service that currently shows `⚠️ Not yet published` releases an official skill:

1. Open an [✏️ Update issue](../../issues/new?template=02-update-entry.yml).
2. In the PR, update the `## Agent Skills` section: change `⚠️` to `✅`, add the install command, and add the skill table.

---

## 11. Code of Conduct

- Be respectful and constructive in all issue and PR discussions.
- **Disclose financial interests.** If you work for, invest in, or otherwise benefit financially from a service you are proposing, state this clearly in your issue and PR. Failure to disclose is grounds for immediate rejection.
- Do not submit services that are vaporware, in closed beta without public documentation, or have not shipped a production-ready product.
- Do not open duplicate issues. Search first.
- Maintainers reserve the right to close issues and reject PRs that do not follow these guidelines without extended discussion.

---

## License

By contributing, you agree that your contributions will be licensed under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).
