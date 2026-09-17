# AffixIO

> **"Know which agent acted. Prove it stayed inside the lines."**

| | |
|---|---|
| **Website** | https://www.affix-io.com/ |
| **Docs** | https://www.affix-io.com/agent-trust/ |
| **npm** | https://www.npmjs.com/package/affixio |
| **GitHub** | https://github.com/AffixIO/SDK |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **Related issue** | https://github.com/haoruilee/awesome-agent-native-services/issues/147 |

---

## Official Website

https://www.affix-io.com/

Agent-trust surface (strongest agent-first official line): https://www.affix-io.com/agent-trust/

Honest wider-product note: the marketing homepage also frames AffixIO as verification / Agentic Pay Kit infrastructure for eligibility decisions before spend, tool use, or access (including related ZK eligibility tooling). For this catalog entry, the sit point is host-side agent action attestation and Know Your Agent (KYA), not person KYC.

---

## Official Repo

https://github.com/AffixIO/SDK

Apache-2.0. Install surface for this listing: npm package `affixio`.

---

## How to Use (Agent Onboarding)

**Quickest verified path (SDK / REST):**

```bash
npm install affixio
```

Then follow https://www.affix-io.com/agent-trust/ and hub onboarding at https://hub.affix-io.com/onboarding/

Typical host flow: enrol / create agent trust, attach host policy (capability sheet / spend or tool grants), call `x402BeforePay` or `mcpToolGate` before a privileged action, keep the signed yes/no + proof id for audit.

Not claiming URL Onboarding gold-standard (`Read <url> and join`) for this entry.

---

## Agent Skills

**Status:** ⚠️ Not yet published

No official `SKILL.md` pack claimed for AffixIO as of 2026-09-17.

Search community skills: `npx clawhub@latest search affixio`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` - [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ Not an MCP server product; MCP-adjacent helpers exist

AffixIO is **not** listed here as an installable MCP server. Clarification (both can be true):

1. Primary surface is the npm SDK / HTTP API for host-side gates.
2. Public materials also mention Streamable HTTP proof/tool endpoints (for example zk_prove-style tools) and an `mcpToolGate` helper so a host can allow/deny MCP tool calls under policy before they run.

| Detail | Value |
|---|---|
| **Primary install** | `npm install affixio` - https://www.npmjs.com/package/affixio |
| **Docs** | https://www.affix-io.com/agent-trust/ |
| **MCP product claim** | No - not "install this MCP server" |
| **MCP-adjacent** | `mcpToolGate` SDK helper; Streamable HTTP proof/tool endpoints documented in public materials |

---

## What It Does

AffixIO ships an Agentic Pay Kit (npm `affixio`) so a **host application** can get a signed yes/no before an agent pays, runs a privileged tool, or is granted access. The core idea is host-side **action attestation**: Know Your Agent (KYA) enrolment and capability grants for a named agent id, then runtime checks such as `x402BeforePay` and `mcpToolGate` that return an attestible allow/deny with a proof id.

This path is **not person KYC**. It decides whether *this agent* may act under a host-written policy, not whether a human passed identity verification at checkout.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Agent-trust H1: *"Know which agent acted. Prove it stayed inside the lines."* Source: https://www.affix-io.com/agent-trust/ . Also: *"Know Your Agent (KYA) is identity and access control for AI agents that you run yourself."* Wider homepage still markets verification / Agentic Pay Kit; agent permission is a first-class path, disclosed honestly above. |
| **Agent-specific primitive** | Host-side signed yes/no action attestation before pay (`x402BeforePay`) or tool use (`mcpToolGate`); KYA `createAgentTrust` / enrolment for a named agent id + capability digest. A human card-checkout API is not the same primitive. |
| **Autonomy-compatible control plane** | Agents/host code can enrol, check grants, and receive allow/deny attestations without a human click per tool call. Constraints are host-written capability sheets / spend or action policy; deny when no matching grant. |
| **M2M integration surface** | npm SDK `affixio`, HTTP API (`api.affix-io.com`), local ops via `npx affixio dashboard`. Docs: https://www.affix-io.com/agent-trust/ |
| **Identity / delegation** | Agent id + owner + capability digest enrolment; runtime grant check; proof id / Merkle-style behaviour trail for later audit. Host attests action permission. Explicit non-goal for this path: person KYC. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **KYA / createAgentTrust** | Enrol a named agent under host policy; create agent trust / capability objects |
| **x402BeforePay** | Host-side signed yes/no before an agentic pay / x402 spend under policy |
| **mcpToolGate** | Host-side allow/deny helper before an MCP (or similar) tool call runs |
| **agenticPay** | Agentic payment helpers in the Agentic Pay Kit |
| **Proof id / audit trail** | Attestible outcome identifiers for later review (not person identity proof) |

---

## Autonomy Model

```
Operator / host writes capability sheet or spend/tool policy
    ↓
Host enrols agent (KYA / createAgentTrust) with agent id + capability digest
    ↓
Agent requests pay or tool use through host application code
    ↓
Host calls x402BeforePay or mcpToolGate
    ↓
Signed yes/no + proof id returned
    ↓
On allow: privileged action proceeds; on deny: action blocked with attestible reason
    ↓
Proof retained for audit / behaviour trail
```

No person KYC step and no per-click human checkout are required for the gate itself. Host policy is the constraint mechanism.

---

## Identity and Delegation Model

- **Agent identity** - named agent id enrolled with owner and capability digest (KYA)
- **Delegated permissions** - host-written grants for spend / tool / access scope
- **Runtime check** - allow/deny attestation before the privileged action
- **Audit** - proof id / Merkle-style trail attributable to the agent action on the host
- **Boundary** - this listing path is host-side **action** attestation, **not person KYC**
- **Dual-use honesty** - company also ships broader verification / ZK eligibility surfaces; keep that note when summarizing AffixIO outside the agent-trust sit point

---

## Protocol Surface

| Interface | Detail |
|---|---|
| npm SDK | `affixio` - https://www.npmjs.com/package/affixio |
| TypeScript / GitHub | https://github.com/AffixIO/SDK (Apache-2.0) |
| HTTP API | `api.affix-io.com` (see agent-trust docs) |
| Local dashboard | `npx affixio dashboard` |
| Docs | https://www.affix-io.com/agent-trust/ |
| MCP | Not an MCP server product; `mcpToolGate` + Streamable HTTP proof/tool endpoints as documented publicly |

---

## Human-in-the-Loop Support

Host operators write and revise capability / spend / tool policy. Individual gated actions can proceed autonomously within those grants. Attestation outcomes and proof ids support post-hoc human review. This is policy HITL on the host, not person-identity verification at pay time.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Ordinary payment SDK (Stripe checkout, etc.)** | Human browser checkout / cardholder flow; no agent id + host action attestation primitive |
| **Person KYC / age-assurance vendor API** | Proves a human identity attribute; does not answer whether *this agent* may pay or call a tool under host policy |
| **Generic API gateway rate limit** | Traffic control without KYA enrolment, signed action attestation, or agent-attributable proof ids |
| **"Add AI agents" footnote on a human SaaS** | Agents are not the primary consumer; missing agent-specific before-action attestation primitives |

---

## Use Cases

- **x402 / agentic pay gate** - call `x402BeforePay` so the host gets a signed yes/no before an agent spends
- **Tool / MCP gate** - use `mcpToolGate` (or equivalent host check) before privileged tool execution
- **KYA enrolment** - create agent trust objects and capability grants for agents the operator runs
- **Audit / dispute** - retain proof ids and behaviour trail for which agent was allowed or denied
