# Cyberdesk

> **"Open source virtual desktops for AI agents."**

| | |
|---|---|
| **Website** | https://www.cyberdesk.io |
| **Docs** | https://docs.cyberdesk.io |
| **GitHub** | https://github.com/cyberdesk-hq/cyberdesk |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |

---

## Official Website

https://www.cyberdesk.io

---

## Official Repo

https://github.com/cyberdesk-hq/cyberdesk

---

## ⭐ How to Use (Agent Onboarding)

```bash
pip install cyberdesk
# then create a desktop and execute computer actions via SDK/API
```

Quickstart: https://docs.cyberdesk.io

---

## Agent Skills

**Status:** ⚠️ No official `SKILL.md` package published yet.

---

## MCP

**Status:** ⚠️ Not MCP-first.

Cyberdesk is API/SDK-first for programmatic desktop lifecycle and computer actions.

---

## What It Does

Cyberdesk provides cloud-hosted virtual desktops that AI agents can control programmatically (mouse, keyboard, screenshot, app/browser interaction) with isolated sessions and auditable execution.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Product tagline explicitly targets AI agents |
| **Agent-specific primitive** | Programmatic computer actions + desktop lifecycle APIs |
| **Autonomy-compatible control plane** | Headless API execution; no per-action human clicks required |
| **M2M integration surface** | SDK + API as primary interface |
| **Identity / delegation** | API-key controlled workspace and per-session attribution |

---

## Primary Primitives

- Virtual desktop create/start/stop/delete
- Computer-use actions (click, type, keypress, screenshot)
- Isolated sessions for concurrent agents
- Execution logs and auditability

---

## Why Generic Alternatives Do Not Qualify

- Generic VDI/remote desktop products are human-operator-first and do not expose agent-native computer-use primitives as the default product surface.

---

## Use Cases

- Computer-use agents for back-office workflows
- Browser-and-desktop automation with isolation
- Human fallback review on recorded sessions
