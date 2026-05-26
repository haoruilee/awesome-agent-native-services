# Circle Agent Stack

> **"Financial infrastructure for the agentic economy."**

| | |
|---|---|
| **Website** | https://www.circle.com/ |
| **Docs** | https://developers.circle.com/agent-stack |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |

---

## Official Website

https://www.circle.com/

---

## Official Repo

Not published as a single product repo (service + docs are official sources).

---

## How to Use (Agent Onboarding)

Read https://developers.circle.com/agent-stack and follow the Agent Stack quickstart to configure Agent Wallets, CLI, and payment flows.

---

## Agent Skills

**Status:** ✅ Available

Circle documents Circle Skills as part of Agent Stack for agent tooling and command-driven operation via Circle CLI.

---

## MCP

**Status:** ⚠️ Not documented as a standalone official MCP server on the Agent Stack entry page.

---

## What It Does

Circle Agent Stack provides agent-first financial primitives so AI agents can hold wallets, discover paid services, and execute programmable payments with guardrails.

---

## Why It Is Agent-Native

- Product positioning is explicitly for autonomous AI agents as economic actors.
- Core primitives are machine-to-machine wallet and payment flows rather than human checkout.
- Documentation includes controls, permissions, and compliance guardrails intended for autonomous execution.

---

## Primary Primitives

- Agent Wallets
- Agent Marketplace
- Circle CLI
- Nanopayments via Circle Gateway (x402)
- Circle Skills

---

## Autonomy Model

Operator configures policy and wallet controls; agent performs payment and service-consumption actions programmatically within those controls.

---

## Identity and Delegation Model

Identity is wallet-based with operator-defined permissions and spending controls; delegation is enforced through policy boundaries.

---

## Protocol Surface

- Circle developer APIs
- Circle CLI
- Agent Stack components documented for machine-driven integration

---

## Human-in-the-Loop Support

Optional through policy design; primary path is autonomous execution within configured guardrails.

---

## Why Generic Alternatives Do Not Qualify

Generic payment APIs usually assume a human payer session and checkout interaction; Circle Agent Stack is designed around autonomous agent wallets and machine-speed service payments.

---

## Use Cases

- AI agents paying for APIs and data services directly.
- Autonomous spend for workflow execution with programmable limits.
- Multi-agent systems using stablecoin-based settlement rails.
