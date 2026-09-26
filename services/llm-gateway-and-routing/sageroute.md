# SageRoute

> **"A trajectory-aware model router."**

| | |
|---|---|
| **Website** | https://github.com/codejunkie99/sageroute |
| **Docs** | https://github.com/codejunkie99/sageroute/tree/main/docs |
| **GitHub** | https://github.com/codejunkie99/sageroute |
| **Classification** | `agent-native` |
| **Category** | [LLM Gateway & Routing Services](README.md) |
| **License** | MIT |
| **Latest-month signal** | Still no GitHub release; last push remains 2026-07-29; 105 stars; license MIT ([repo metadata](https://api.github.com/repos/codejunkie99/sageroute)) |
| **Verified at** | 2026-09-26 |

---

## Official Website

https://github.com/codejunkie99/sageroute

---

## Official Repo

https://github.com/codejunkie99/sageroute

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `OpenAI/Anthropic-compatible proxy`

```bash
git clone https://github.com/codejunkie99/sageroute.git
cd sageroute
bun install
echo "SAGE_API_KEY=lv_..." > .env
bun run serve                     # http://127.0.0.1:8787

export OPENAI_BASE_URL=http://127.0.0.1:8787/v1
export OPENAI_MODEL=sageroute
```

SageRoute requires Bun 1.1+ and, for live trajectory decisions, a key for the external [Levanto Sage API](https://docs.levanto.ai/). Configure cheap and strong upstream model credentials or supported subscription OAuth before production use.

---

## Agent Skills

**Status:** ⚠️ No official skill published.

Search community skills: `npx clawhub@latest search sageroute`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ No MCP server published. SageRoute is an OpenAI Responses / Chat Completions and Anthropic Messages proxy.

---

## What It Does

SageRoute is a proxy that changes models based on an agent's observed execution trajectory instead of classifying only its opening prompt. Every session starts on a cheap model. The router reconstructs tool calls and results from each request, detects loops, repeated error classes, rewrite/retest thrashing, and lack of successful execution, then asks the Levanto Sage decision API whether to continue, switch models, restart with cleaned context, or escalate to a human.

The project is explicitly early. It has no published release/tag, stores session state in one process, and is not battle-tested at scale. The README documents a real cheap-to-strong run but not a multi-task benchmark, aggregate savings study, or live proof for every ladder action. Live decision quality also depends on the external Levanto Sage API; an offline deterministic stub exists for development, and live Sage failures default to continuing rather than taking the agent down.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The README opens with the failure mode of coding-agent model selection and says the proxy watches *"what the agent actually does"* — [README](https://github.com/codejunkie99/sageroute#readme) |
| **Agent-specific primitive** | Tool-trajectory recovery, agent-loop/thrash detectors, execution-progress semantics, per-session capability ladder, clean-context restart, and human-escalation action |
| **Autonomy-compatible control plane** | The router switches tiers and rebuilds context without changing the harness; local spend limits run before network calls; switch/restart caps and one-way hysteresis bound intervention |
| **M2M integration surface** | OpenAI Responses, Anthropic Messages, Chat Completions passthrough, model discovery, health, and structured session-history endpoints |
| **Identity / delegation** | Stable harness session keys isolate tier and budget state; optional bearer auth scopes access to the proxy; each session exposes an attributable decision and cost history while provider credentials remain server-side |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Trajectory** | Ordered tool calls, outputs, failures, and successful executions reconstructed from agent requests |
| **Deterministic Detectors** | Local repeat, error-class, ping-pong, rewrite/retest, and no-progress signals |
| **Sage Gate** | Two-stage external decision: first whether to intervene, then which action to take |
| **Model Ladder** | One-way cheap → strong → restart → human progression with bounded switches and restarts |
| **`restart_clean`** | Keeps task facts, tool calls, and outputs while removing stale narration and provider-specific reasoning payloads |
| **Budget Stop** | Per-session cost ledger and threshold checked locally before paying for another routing decision |
| **Decision Headers** | Response headers report model, tier, action, probability, and decision source |
| **Session History** | Tier, cost, switch count, and decision history exposed by a structured endpoint |

---

## Autonomy Model

```text
Agent harness sends a normal Responses or Messages request using model=sageroute
    ↓
Proxy derives a stable session and reconstructs tool execution evidence
    ↓
Local budget and deterministic failure detectors run first
    ↓
When needed, Levanto Sage gates intervention and selects an action
    ↓
Policy applies continue, cheap→strong switch, clean restart, or human escalation
    ↓
Request is translated and sent to the selected upstream provider/model
    ↓
Response includes routing headers; usage updates the session cost ledger
```

---

## Identity and Delegation Model

- Codex's `prompt_cache_key` and the equivalent derived keys on other wires identify one agent conversation; unrelated Codex and Claude Code sessions keep separate ladders and budgets.
- An optional proxy `authToken` requires clients to send a bearer credential, while upstream provider and Sage keys stay behind the proxy.
- Stored OAuth credentials use restricted filesystem permissions and are not written back into Codex or Claude Code credential stores.
- Every routed response carries decision headers, and `/v1/sageroute/sessions` exposes the session's running ledger and routing history.
- This is session-level routing identity, not a full organization-level agent/user delegation system; deployments needing per-team roles must add that boundary in front of the proxy.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| `POST /v1/responses` | Native routed path for Codex and OpenAI-compatible clients |
| `POST /v1/messages` | Anthropic Messages adapter for Claude Code, translated into the same evidence model |
| `POST /v1/chat/completions` | Passthrough path for non-routed aliases |
| `GET /v1/models` | Router alias plus configured provider/model names |
| `GET /v1/sageroute/sessions` | Per-session tier, cost ledger, switches, and decision history |
| `GET /health` | Liveness endpoint |
| CLI | `serve`, `init`, `check`, provider selection, and OAuth login/import/status commands |

---

## Human-in-the-Loop Support

`escalate_human` is a first-class terminal action in the routing ladder and can be triggered by repeated intervention evidence or a local budget threshold. SageRoute itself does not provide an approval inbox or operator UI; the calling harness must interpret the action and perform the handoff. That path, along with live `restart_clean`, is documented as less field-proven than the cheap-to-strong switch.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Static model alias** | Chooses one model before execution and cannot react when an easy-looking task begins to thrash |
| **Prompt classifier router** | Sees the initial text but not tool failures, repeated rewrites, passing tests, or progress over later turns |
| **Generic reverse proxy** | Forwards requests but has no agent trajectory, session ladder, clean restart, or execution-aware budget policy |
| **Retry middleware** | Repeats the same request/model and may preserve polluted reasoning rather than escalating capability or trimming context |

---

## Use Cases

- **Cost-aware coding agents** — start routine work cheaply and escalate only after tests and tool output show real difficulty
- **Cross-vendor agent routing** — accept Claude Code's Messages wire while serving an OpenAI model, or move between configured vendors mid-session
- **Thrash detection** — identify rewrite/retest loops that simple identical-call detectors miss
- **Budget-bounded autonomy** — stop and request human involvement before a session exceeds its configured spend threshold
- **Routing research** — inspect decision headers and per-session histories while benchmarking trajectory policies
