---
name: add-to-awesome-list
description: >
  Guide a contributor through the full process of adding a new service to the
  awesome-agent-native-services catalog: verifying criteria, checking for URL Onboarding
  (the gold standard of agent-nativeness), opening an issue, writing the service file,
  and submitting a PR. Use when "I want to add X to the list" or "how do I contribute?"
license: CC0-1.0
compatibility: Works with any agent that can read, write, and use git.
metadata:
  repo: https://github.com/haoruilee/awesome-agent-native-services
  catalog-version: "2026-03-15"
allowed-tools: WebSearch Read Write Shell
---

# Skill: add-to-awesome-list

Use this skill to walk a contributor through the complete process of adding a new service to the catalog, from eligibility check through a merged PR.

## The most important thing to check first: URL Onboarding

Before running through the five criteria, ask this one question:

> **Can an agent join and start using this service by reading a single URL?**

```
Read <url> and follow the instructions.
```

If YES — this is **URL Onboarding**, the highest form of agent-nativeness. Mark it prominently throughout the service file, the issue, and the PR. It means the service designed its onboarding for machines, not humans.

**Known URL Onboarding services in the catalog:**
- Moltbook: `Read https://www.moltbook.com/skill.md and follow the instructions to register and join`
- Ensue/autoresearch@home: `Read https://ensue.dev/docs` + `Read .../collab.md and follow the instructions to join`

When the new service has URL Onboarding, lead with this in every section.

---

## Phase 1 — Pre-flight eligibility check

### 1.0 Check for URL Onboarding first

Look for a machine-readable protocol file:
- `skill.md` or `SKILL.md` at the service's domain
- `collab.md`, `protocol.md`, or similar at the repo root
- Any URL the service documents as the agent onboarding entry point

Test it: can you give an agent the instruction `Read <url> and follow the instructions` and have it complete registration autonomously?

Record the result for Phase 3's "How to Use" section.

### 1.1 Check for duplicates

```
1. Read README.md — search for the service name in all 15 category sections.
2. Search open issues: https://github.com/haoruilee/awesome-agent-native-services/issues?q=<service-name>
3. If found: report the existing entry or issue URL and stop.
```

### 1.2 Apply the five criteria

Use the `evaluate-agent-native` skill (or apply inline):

For each criterion, find **evidence from the official homepage or docs** — direct quotes, not marketing copy.

If any criterion fails: tell the user which failed and what the correct classification is. Do not proceed.

### 1.3 Determine the category and interaction pattern

| What the service does | Category folder | Typical pattern |
|---|---|---|
| Communication identity (email, notifications) | `communication/` | SDK / Skill |
| Remote browser or web extraction | `browser-and-web-execution/` | Skill / SDK / Daemon |
| Runtime tool discovery, OAuth, execution | `tool-access-and-integration/` | Skill / SDK |
| Human approval gates | `oversight-and-approval/` | SDK |
| Agent wallets, payments, identity | `commerce-and-payments/` | SDK / REST |
| Execution, secrets, identity, gateway | `agent-runtime-and-infrastructure/` | SDK |
| Per-agent memory | `memory-and-state/` | SDK / MCP |
| Multi-agent shared memory / coordination | `memory-and-state/` | URL Onboarding ⭐ |
| LLM-optimized search | `search-and-web-intelligence/` | Skill / MCP |
| Code sandbox | `code-execution/` | SDK / MCP |
| Agent trajectory tracing | `observability-and-tracing/` | Skill |
| Fault-tolerant agent workflows | `durable-execution-and-scheduling/` | Skill / SDK |
| Agent presence in meetings | `meeting-and-conversation/` | REST |
| Voice calls / phone | `voice-and-phone/` | SDK |
| LLM routing, cost, fallback | `llm-gateway-and-routing/` | SDK |
| Agent social network / community | `agent-social-network/` | URL Onboarding ⭐ |

---

## Phase 2 — Open a GitHub issue

**Do not write the PR before the issue is approved.**

Issue URL: https://github.com/haoruilee/awesome-agent-native-services/issues/new?template=01-new-service.yml

Required fields:
- Service name and official website
- Official tagline — exact quote from homepage
- Proposed category
- Criterion evidence — one field per criterion
- **URL Onboarding instruction** — if available, provide the exact sentence
- MCP status — is there a published MCP server?
- Agent Skills status — is there a published SKILL.md?
- Classification: `agent-native`
- Generic alternative comparison

After submission, wait for a maintainer ✅ Go before proceeding.

---

## Phase 3 — Write the service file

### File location

```
services/{category-folder}/{service-name}.md
```

Naming: lowercase, hyphens only, e.g. `agentmail.md`, `trigger-dev.md`.

### Required sections (14 total, in this order)

```markdown
# {Service Name}

> **"{Official tagline}"**

| | |
|---|---|
| **Website** | https://... |
| **Classification** | `agent-native` |
| **Category** | [{Category}](README.md) |

---

## Official Website
https://...

---

## Official Repo
https://github.com/...

---

## ⭐ How to Use (Agent Onboarding)

<!-- CRITICAL: This section tells an agent how to START USING the service. -->
<!-- For URL Onboarding services, this is THE most important section. -->

**Interaction pattern:** URL Onboarding / MCP Tool / Coding-time Skill / SDK+REST / Daemon+Extension

<!-- URL Onboarding (highest tier): -->
**One-sentence agent instruction:**
```
Read https://... and follow the instructions to [register / join / participate].
```
What the agent gets by reading that URL: {full onboarding sequence, registration, protocol}

<!-- For other patterns: -->
**MCP:** Add to `mcp_servers`: `{ "command": "npx", "args": ["-y", "<pkg>", "--mcp"] }`
**Skill:** `npx skills add <org>/<repo>`
**SDK:** `pip install <pkg>` then `<one-line first API call>`
**Daemon:** `npm install -g <pkg>` + install extension

---

## Agent Skills
**Status:** ✅ / ⚠️
[install command + skill table OR community search note]

---

## MCP
**Status:** ✅ / ⚠️
[server details OR "not yet published"]

---

## What It Does
[1-3 paragraphs]

---

## Why It Is Agent-Native
| Criterion | Evidence |
|---|---|
| Agent-first positioning | "{quote}" — {url} |
| Agent-specific primitive | {description} |
| Autonomy-compatible control plane | {description} |
| M2M integration surface | {interfaces} |
| Identity / delegation | {model} |

---

## Primary Primitives
| Primitive | Description |
|---|---|
| **{Name}** | {one sentence} |

---

## Autonomy Model
[Step-by-step: what the agent does, no human in the loop]

---

## Identity and Delegation Model
[Bullet list: agent identity, delegated permissions, audit trail]

---

## Protocol Surface
| Interface | Detail |
|---|---|
| REST API | ... |
| SDK | ... |

---

## Human-in-the-Loop Support
[One paragraph]

---

## Why Generic Alternatives Do Not Qualify
| Alternative | Why It Fails |
|---|---|
| **{Name}** | {reason} |

---

## Use Cases
- **{title}** — {description}
```

### Research checklist

- [ ] **URL Onboarding**: try `Read <url> and follow the instructions` — does it work?
- [ ] **Official Website / Repo**: from GitHub or homepage
- [ ] **Agent Skills**: check skills.sh, agentskills.io, service GitHub
- [ ] **MCP**: check service GitHub, mcp.so, glama.ai/mcp, smithery.ai
- [ ] **Why It Is Agent-Native**: direct quotes from official docs
- [ ] **Protocol Surface**: check SDK README for install commands
- [ ] **Use Cases**: from service's own documentation

---

## Phase 4 — Update the index files

### 4.1 Update `services/{category}/README.md`

Add a row to the service table (5 columns now: Service, Tagline, Primitives, MCP, How to Use):

```markdown
| [{Service Name}]({service-name}.md) | {tagline} | {primitives} | ✅/⚠️ | {onboarding instruction} |
```

For URL Onboarding services, the "How to Use" cell should be the full one-sentence instruction.

### 4.2 Update root `README.md`

Find the correct category section and add a row:

```markdown
| [{Service Name}](services/{category}/{service-name}.md) | {tagline} | {primitives} | ✅/⚠️ | {onboarding instruction} |
```

---

## Phase 5 — Open the PR

### PR title format

```
[New Service] {Service Name}
[New Service] {Service Name} — URL Onboarding  ← if has URL Onboarding
```

### Git commands

```bash
git checkout -b add-{service-name}
git add services/{category}/{service-name}.md services/{category}/README.md README.md
git commit -m "[New Service] {Service Name}

Closes #{issue number}

- Category: {category}
- Interaction pattern: {URL Onboarding ⭐ / MCP / Skill / SDK / Daemon}
- How to use: {one-sentence instruction}
- MCP: {✅ / ⚠️}
- Agent Skills: {✅ / ⚠️}"
git push origin add-{service-name}
```

---

## Quality checklist before submitting

- [ ] All links are live
- [ ] Official tagline is an exact quote
- [ ] All criterion evidence cites a specific URL
- [ ] "How to Use" section accurately describes the interaction pattern
- [ ] URL Onboarding instruction tested and confirmed working (if applicable)
- [ ] All 14 required sections present
- [ ] Agent Skills section shows real install commands
- [ ] MCP section shows real repo/transport
- [ ] No undisclosed financial interest in the service
