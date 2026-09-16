# AffixIO

> **"Agentic Pay Kit for host-side action attestation before pay."**

| | |
|---|---|
| **Website** | https://www.affix-io.com/ |
| **Docs** | https://www.affix-io.com/agent-trust/ |
| **npm** | https://www.npmjs.com/package/affixio |
| **GitHub** | https://github.com/AffixIO/SDK |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |

## Official Website
https://www.affix-io.com/

## Official Repo
https://github.com/AffixIO/SDK

---

## How to Use (Agent Onboarding)

**Quickest verified path:**

`npm install affixio` then follow https://www.affix-io.com/agent-trust/ and https://hub.affix-io.com/onboarding/

---

## Agent Skills
**Status:** ⚠️ None found.

## MCP
**Status:** ⚠️ Not an MCP server. Exposes `mcpToolGate` as an SDK helper for gating tool calls.

## What It Does
npm Agentic Pay Kit (`affixio`) with x402BeforePay host-side action attestation before pay (signed yes/no on host, not person KYC), plus agenticPay, mcpToolGate, and KYA createAgentTrust.

## Why It Is Agent-Native
Built for agent payment and trust gates: host-side before-pay attestation, KYA agent trust creation, and tool gating rather than human checkout or person KYC.

## Primary Primitives
- x402BeforePay host-side action attestation (signed yes/no on host)
- agenticPay
- mcpToolGate
- KYA createAgentTrust

## Autonomy Model
Agents can attest and pay under host policy without person KYC or per-click human checkout.

## Identity and Delegation Model
KYA / action attestation for the agent action on the host. Not person KYC.

## Protocol Surface
npm package `affixio`; TypeScript SDK on GitHub; docs on affix-io.com.

## Human-in-the-Loop Support
Host policy can require attestation results before pay; not person identity verification.

## Why Generic Alternatives Do Not Qualify
Ordinary payment SDKs expect human checkout or person KYC. AffixIO targets agentic pay with host-side action attestation and KYA.

## Use Cases
Gate x402 or agentic pay flows with before-pay attestation, create agent trust (KYA), and gate MCP tool calls from application code.
