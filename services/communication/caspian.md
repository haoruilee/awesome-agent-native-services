# Caspian

> **"Agent communication SDK. The open-source agent communication layer for AI agents — email, WhatsApp, Slack, Discord, Telegram, SMS."**

| | |
|---|---|
| **Website** | https://trycaspianai.com |
| **Docs** | https://api.trycaspianai.com/SKILL.md |
| **GitHub** | https://github.com/TryCaspian/caspian-sdk |
| **Stars** | [973 stars (snapshot: 2026-09-26)](https://github.com/TryCaspian/caspian-sdk) |
| **Classification** | `agent-native` |
| **Category** | [Communication Services](README.md) |
| **Latest-month signal** | Latest release is still [v0.1.2](https://github.com/TryCaspian/caspian-sdk/releases/tag/v0.1.2); 973 stars; last push 2026-08-25; root `LICENSE` is still AGPL-3.0 while the README license section still says Apache-2.0; [SKILL.md](https://api.trycaspianai.com/SKILL.md) returned HTTP 200 on 2026-09-26 ([repo metadata](https://api.github.com/repos/TryCaspian/caspian-sdk)) |
| **Verified at** | 2026-09-26 |
| **License** | **The root repository is AGPL-3.0 according to its actual [`LICENSE`](https://github.com/TryCaspian/caspian-sdk/blob/main/LICENSE) and GitHub metadata, despite the root README's Apache-2.0 badge/text.** The [Python](https://github.com/TryCaspian/caspian-sdk/blob/main/sdks/python/LICENSE) and [TypeScript](https://github.com/TryCaspian/caspian-sdk/blob/main/sdks/typescript/LICENSE) SDK subdirectories separately carry MIT license files; verify the scope of the artifact you use. |

---

## Official Website

https://trycaspianai.com

On 2026-09-26 the page title was **"The Constructor"**. The meta description still reads **"Caspian: the AI infrastructure stack for self-sovereign agents and their relationships with humans."** The hosted skill at `https://api.trycaspianai.com/SKILL.md` still describes the channel SDK.

---

## Official Repo

https://github.com/TryCaspian/caspian-sdk

---

## How to Use (Agent Onboarding)

Give a coding agent the official live guide:

```text
Integrate Caspian so my agent can message people on email, Slack, Discord, Telegram, and more.
Read https://api.trycaspianai.com/SKILL.md and follow it end to end.
```

The guide installs an SDK, creates a Caspian key, connects a channel, and helps the agent write its handler. The upstream README also documents a manual Python path:

```bash
pip install caspian-sdk
pipx install caspian-cli
caspian init
caspian connect email
```

---

## Agent Skills

**Status:** ✅ Available — both a live URL-onboarding skill and an official ClawHub package are documented upstream.

```bash
clawhub install @trycaspian/caspian
```

| Skill | What It Teaches the Agent |
|---|---|
| [`api.trycaspianai.com/SKILL.md`](https://api.trycaspianai.com/SKILL.md) | End-to-end SDK setup, API-key creation, channel connection, event handling, and validation |
| [`@trycaspian/caspian`](https://github.com/TryCaspian/caspian-sdk/tree/main/packages/clawhub-skill) | How an OpenClaw agent wires itself to Caspian channels |

---

## MCP

**Status:** ⚠️ Not yet published. The [official roadmap](https://github.com/TryCaspian/caspian-sdk#roadmap) lists an MCP server as future work; the current verified surfaces are URL onboarding, SDKs, CLI, REST/event APIs, and webhooks.

---

## What It Does

Caspian gives one AI agent a normalized communication layer across email, Slack, Discord, Telegram, GitHub, Instagram, Facebook Messenger, X, Bluesky, and additional hosted channels. The agent uses one message handler and one reply abstraction while adapters handle platform payloads, thread routing, signature verification, reconnection, and capability differences.

Its defining model is that channels are transports rather than separate identities. Caspian can scope connections to explicit customer and agent records, deliver ordered events with conversation and connection identifiers, and return channel-specific etiquette through `behavior_prompt()` for the model's context.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The official repository calls Caspian an ["agent communication SDK"](https://github.com/TryCaspian/caspian-sdk#readme) and describes the agent as the actor deciding what to say. |
| **Agent-specific primitive** | One agent identity binds multiple human channels; normalized conversations, `message.reply()`, behavior prompts, idempotent channel connections, and agent/customer-scoped events are designed for agent loops. |
| **Autonomy-compatible control plane** | Free hosted channels can be provisioned from the CLI/SDK and operated through `listen()` or serverless `handle_webhook()` without confirmation on each message. Paid channels may require one developer login and prepaid credit. |
| **M2M integration surface** | Python and TypeScript SDKs, CLI, REST/event endpoints, verified webhooks, and a machine-readable live `SKILL.md`. |
| **Identity / delegation** | Explicit customer, agent, connection, conversation, message, and event identifiers scope channel use. Adapter capability negotiation prevents granting operations a transport cannot support. Caspian exposes ordered operational records, but does not claim a tamper-evident audit journal. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Cross-channel agent identity** | Binds several communication transports to one logical agent |
| **Normalized message** | Common sender, text, conversation, attachment, interaction, and reaction shapes across providers |
| **Contextual reply** | `message.reply()` returns to the correct channel and thread without provider-specific routing code |
| **Channel connection** | Idempotent `connect_*()` / `install_*()` lifecycle scoped to a customer and agent when needed |
| **Behavior prompt** | Supplies channel etiquette that the reasoning model can incorporate at runtime |
| **Ordered event stream** | Polling or webhook delivery with stable event, connection, conversation, customer, and agent references |
| **Capability negotiation** | Constrains rich-message and interaction behavior to what a transport supports |

---

## Autonomy Model

1. The agent reads the live `SKILL.md`, installs the SDK/CLI, and runs `caspian init` to create its project credential.
2. It provisions one or more free channels immediately, or the operator performs the documented one-time login/funding step for a paid hosted channel.
3. A single handler consumes normalized inbound events through `listen()` or a serverless webhook.
4. The agent chooses a channel, follows the generated behavior guidance, and sends or replies programmatically.
5. Ordered events and stable conversation identifiers let the agent resume after restarts and avoid rebuilding per-platform lifecycle code.

---

## Identity and Delegation Model

- One logical **agent** can own multiple channel connections; channels do not become independent agent identities.
- Multi-tenant deployments create explicit `customer_id` and `agent_id` scopes and attach connections/events to both.
- Provider credentials remain behind the selected hosted or self-hosted adapter boundary; webhook signatures are verified before inbound dispatch.
- Adapter-declared capabilities bound what the agent may request from each transport.
- Event/message/connection identifiers provide attributable operational history. The project does not document cryptographic audit receipts or a human approval policy engine.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **URL onboarding** | Live machine-readable guide at https://api.trycaspianai.com/SKILL.md |
| **Python SDK** | `caspian-sdk` on PyPI; `CommClient`, channel connects, messages, events, and webhooks |
| **TypeScript SDK** | `caspian-sdk` on npm with the same contract and camelCase API |
| **CLI** | `caspian-cli` for project initialization, channel connection, and event tailing |
| **REST / events** | Hosted or self-hosted gateway, including ordered `/v1/events` access |
| **Webhooks** | Signed inbound webhook ingestion and serverless `handle_webhook()` dispatch |
| **MCP** | Not yet shipped; listed on the official roadmap |

---

## Human-in-the-Loop Support

Routine send/receive operations do not require a human. Free hosted channels connect without a sign-in; paid X, WhatsApp, and iMessage paths can require a one-time developer login and prepaid balance. Caspian supports communication handoff at the application layer, but the repository does not document a native per-message approval gate.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Separate Slack, Discord, Telegram, and email SDKs** | Leave identity, threading, retries, signature verification, and event normalization to each agent application. |
| **A2A / ACP** | Connect agents to other agents; they do not give one agent a coherent identity on the human channels where its users already communicate. |
| **Human mailbox or chat account automation** | Delegates a person's account and UI instead of provisioning and scoping a programmatic agent communication identity. |

---

## Use Cases

- **Omnichannel support agent** — preserve one conversation identity while replying on the channel a customer used
- **Executive assistant** — coordinate email, Telegram, and Slack from one reasoning loop
- **Community agent** — operate the same identity across Discord and Slack communities
- **Multi-tenant agent fleet** — isolate customer/agent channel connections while sharing one gateway
- **Serverless communication agent** — receive verified events in Lambda, Vercel, or Workers and scale to zero
