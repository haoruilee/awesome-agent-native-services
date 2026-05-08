# OpenLibx402

> **"An open-source library for AI-native x402 integrations."**

| | |
|---|---|
| **Website** | https://openlibx402.xyz |
| **Docs** | https://github.com/openlibx402/openlibx402 |
| **GitHub** | https://github.com/openlibx402/openlibx402 |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |

## Official Website
https://openlibx402.xyz

## Official Repo
https://github.com/openlibx402/openlibx402

## Agent Skills
**Status:** ⚠️ None found.

## MCP
**Status:** ⚠️ Not an MCP server; SDK/protocol library.

## What It Does
Implements x402 payment flows so autonomous agents can pay APIs machine-to-machine with HTTP 402 semantics.

## Why It Is Agent-Native
Agent-first payment protocol primitives, micropayment flow, and no human checkout step.

## Primary Primitives
- 402 challenge/response
- Wallet-based agent payment authorization
- FastAPI/Express middleware for paid endpoints

## Autonomy Model
Agents receive a 402 response and can complete payment + retry automatically.

## Identity and Delegation Model
Agent wallet identity signs transactions; delegated spending rules can be applied upstream.

## Protocol Surface
Python and Node SDKs; server middleware.

## Human-in-the-Loop Support
Optional policy checks; not required by default.

## Why Generic Alternatives Do Not Qualify
Traditional Stripe checkout requires human flows; x402 flows are designed for autonomous software clients.

## Use Cases
Pay-per-call MCP tools, paid API access for agent swarms, low-friction micropayments.
