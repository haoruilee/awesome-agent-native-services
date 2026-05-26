# agentOS by Fiserv

> **"A governed operating layer that enables financial institutions to deploy AI agents safely and securely."**

| | |
|---|---|
| **Website** | https://www.fiserv.com/en/lp/agentos-by-fiserv.html |
| **Docs** | Product page and Fiserv release materials |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |

---

## Official Website

https://www.fiserv.com/en/lp/agentos-by-fiserv.html

---

## Official Repo

No public source repository listed.

---

## How to Use (Agent Onboarding)

Start with the official agentOS page and enterprise onboarding through Fiserv.

---

## Agent Skills

**Status:** ⚠️ Not publicly documented.

---

## MCP

**Status:** ⚠️ Not publicly documented as an MCP endpoint.

---

## What It Does

agentOS is a banking-focused runtime/control plane for deploying, governing, monitoring, and auditing AI agents across financial workflows.

---

## Why It Is Agent-Native

- Built around deploying and governing AI agents across core systems.
- Emphasizes deterministic guardrails, auditability, and kill-switch controls for autonomous behavior.
- Marketplace model centered on agent deployment and lifecycle in financial institutions.

---

## Primary Primitives

- Governance and policy enforcement
- Audit logging for agent actions
- Human-in-the-loop escalation and control
- Agent marketplace and deployment model

---

## Autonomy Model

Agents run within institutional policy controls; high-risk actions are constrained by governance and can be escalated or halted.

---

## Identity and Delegation Model

Identity-bound access and role-based controls are used so agent actions remain attributable and policy-scoped.

---

## Protocol Surface

Enterprise platform integration on Fiserv systems; public low-level API surface is not fully documented on the public landing page.

---

## Human-in-the-Loop Support

Explicitly supported: humans can review, approve, and suspend agent behavior.

---

## Why Generic Alternatives Do Not Qualify

Generic cloud runtimes do not provide banking-specific governance, controls, and operating constraints as first-class agent runtime primitives.

---

## Use Cases

- AI-driven fraud and risk operations with strict controls.
- Agent-assisted service workflows in financial institutions.
- Cross-system agent orchestration with auditable governance.
