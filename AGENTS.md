# AGENTS.md — For AI Coding Agents

This file provides project context for AI agents (Cursor, Claude Code, Windsurf, etc.) working on the Awesome Agent-Native Services catalog.

---

## What This Repo Is

A curated list of **agent-native** services — infrastructure designed from inception for AI agents as first-class consumers. Not agent-adapted (human products with agent layers) or agent-builder (platforms for humans to build agents).

---

## Quick Reference

| Need | Read |
|---|---|
| Find a service for a task | [skill.md](skill.md) — machine-readable catalog |
| Understand criteria & contribute | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Full catalog index | [README.md](README.md) |
| LLM-friendly manifest | [llms.txt](llms.txt) |

---

## Repository Layout

```
README.md              # Index: category tables, service summaries
CONTRIBUTING.md        # Five criteria, workflow, service format
skill.md               # Agent entry point — discover services by task
llms.txt               # llms.txt spec — curated links for LLMs
AGENTS.md              # This file
services/
  {category}/          # e.g. communication/, memory-and-state/
    README.md          # Category overview + service table
    {service}.md       # Per-service detail (required sections)
.skills/               # ClawHub skills (find-agent-service, etc.)
.github/               # Issue templates, PR template
```

---

## Contribution Workflow

1. **New service**: Open issue with [01-new-service.yml](.github/ISSUE_TEMPLATE/01-new-service.yml). Wait for ✅ Go. Then PR with:
   - `services/{category}/{service-name}.md`
   - Row in `services/{category}/README.md`
   - Row in root `README.md`
2. **Update**: Use [02-update-entry.yml](.github/ISSUE_TEMPLATE/02-update-entry.yml). Include source URL.
3. **Fix**: Direct PR for typos, broken links — no issue needed.

---

## Service File Format

Every service file must include (in order):

- Official Website, Official Repo
- How to Use (Agent Onboarding) — quickest entry point
- Agent Skills, MCP
- What It Does, Why It Is Agent-Native
- Primary Primitives, Autonomy Model, Identity and Delegation Model
- Protocol Surface, Human-in-the-Loop Support
- Why Generic Alternatives Do Not Qualify, Use Cases

See CONTRIBUTING.md §7 for the exact template.

---

## Classification

| Label | Meaning |
|---|---|
| `agent-native` | Designed for agents from inception — **only these in main list** |
| `agent-adapted` | Human-facing first, agent layer added — Excluded section |
| `agent-builder` | For humans to build agents — Excluded section |

---

## Agent Skills

Install via ClawHub:

```
npx clawhub@latest install find-agent-service
npx clawhub@latest install evaluate-agent-native
npx clawhub@latest install add-to-awesome-list
```

---

## URL Onboarding (⭐)

Services an agent can join with one instruction:

- **Moltbook**: `Read https://www.moltbook.com/skill.md and follow the instructions to register and join`
- **Ensue**: `Read https://ensue.dev/docs and call POST https://api.ensue-network.ai/auth/agent-register`
- **autoresearch@home**: `Read https://raw.githubusercontent.com/mutable-state-inc/autoresearch-at-home/master/collab.md and follow the instructions to join`
- **db9**: `Read https://db9.ai/skill.md and follow the instructions`
- **mem9**: `Read https://mem9.ai/skill.md and follow the instructions to register and join`
- **mails.dev**: `Read https://mails.dev/skill.md and follow the instructions`
