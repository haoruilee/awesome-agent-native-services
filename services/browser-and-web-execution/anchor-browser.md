# Anchor Browser

> **"The Secure Infrastructure for Computer Use Agents."**

| | |
|---|---|
| **Website** | https://www.anchorbrowser.io |
| **Docs** | https://docs.anchorbrowser.io |
| **GitHub** | https://github.com/anchorbrowser/AnchorBrowser-SDK-Python (SDK) · https://github.com/anchorbrowser/AnchorBrowser-SDK-Typescript |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |

---

## Official Website

https://www.anchorbrowser.io

---

## Official Repo

SDKs: [AnchorBrowser-SDK-Python](https://github.com/anchorbrowser/AnchorBrowser-SDK-Python), [AnchorBrowser-SDK-Typescript](https://github.com/anchorbrowser/AnchorBrowser-SDK-Typescript) — integrate **Anchor Cloud** from agent code

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK / REST` + **MCP** (per marketing: integrate anywhere via SDK, MCP, or automation platforms)

1. Sign in at [signin.anchorbrowser.io](https://signin.anchorbrowser.io/) and obtain API credentials.
2. Follow [docs](https://docs.anchorbrowser.io/introduction): define a task in natural language → Anchor configures proxy/browser/AI usage → call via **SDK** or **MCP**.
3. Product surfaces include **OmniConnect** (auth lifecycle for cloud computer-use agents), **Web Action Cache** (deterministic replay of workflows), **Anchor Chromium** (stealth fork), and **enterprise VPN** options — see [homepage](https://www.anchorbrowser.io).

---

## Agent Skills

**Status:** ⚠️ No official ClawHub-style skill pack found.

```bash
npx clawhub@latest search anchor browser
```

---

## MCP

**Status:** ✅ Listed on homepage as an integration path (*"Integrate anywhere — Use the browser workload through our SDK, MCP, or any automation platform"*) — configure per [docs](https://docs.anchorbrowser.io).

| Detail | Value |
|---|---|
| **Compatible Clients** | Claude, Cursor, and other MCP hosts |

---

## What It Does

Anchor provides a **cloud fleet of browsers** tuned for **computer-use agents**: humanized Chromium, **authenticated sessions**, **CAPTCHA** and **anti-bot** positioning, **scalable parallel sessions**, and **auth infrastructure** (SSO/MFA/VPN patterns per marketing). It emphasizes **deterministic cached actions** with **AI only when needed** to reduce token cost and flakiness versus pure prompt-only browser agents.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Title: *"Anchor - Build reliable browser agents"*; hero: *"The Secure Infrastructure for Computer Use Agents"*; FAQ: *"cloud-hosted browser that allows AI agents to interact with the web"* — [anchorbrowser.io](https://www.anchorbrowser.io) |
| **Agent-specific primitive** | **Web Action Cache** (workflows as deterministic code), **OmniConnect** auth lifecycle for **cloud computer-use agents**, **computer-use** task definition flow |
| **Autonomy-compatible control plane** | API/SDK-driven sessions and tasks at scale without a human operating each browser |
| **M2M integration surface** | Official Python/TypeScript SDK repos, REST/API docs, MCP path |
| **Identity / delegation** | **Authenticated browsers**, enterprise security posture (SOC2/ISO/HIPAA tiers on pricing), **Cloudflare verified browser agents** on higher tiers |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Cloud browser session** | Stealth, humanized Chromium at scale |
| **NL task → workload** | Agent describes task; platform optimizes config |
| **Web Action Cache** | Replay deterministic browser actions |
| **OmniConnect** | End-to-end auth for computer-use agents |
| **MCP / SDK** | Machine integration for coding agents and backends |

---

## Autonomy Model

```
Agent obtains Anchor credentials → define task (NL) via SDK/API
    ↓
Anchor provisions browser + proxy/VPN/auth as configured
    ↓
Deterministic cached path where possible; AI fallback at runtime when needed
    ↓
Results returned to calling agent or downstream system
```

---

## Identity and Delegation Model

- **API credentials** scope tenant access to the browser fleet.
- **Authenticated browser tiers** model delegated login state for agents.
- **Enterprise controls** (SSO, RBAC, retention) for org delegation.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST / API | https://docs.anchorbrowser.io |
| Python SDK | https://github.com/anchorbrowser/AnchorBrowser-SDK-Python |
| TypeScript SDK | https://github.com/anchorbrowser/AnchorBrowser-SDK-Typescript |
| MCP | Per docs / integration guides |

---

## Human-in-the-Loop Support

Enterprise support and dashboard-style operations; core integration is API-first for autonomous runs.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Vanilla CDP farm** | No **computer-use agent** positioning, **OmniConnect**-style auth product, or **web action cache** primitive |
| **Human RPA** | Not an **M2M API for AI agents** as primary consumer |

---

## Use Cases

- **Enterprise computer-use** — Secure, compliant browser agents at scale
- **SaaS integrations** — Sites without APIs, with auth and anti-bot constraints
- **Partner ecosystem** — LangChain and cloud partner integrations listed on site
