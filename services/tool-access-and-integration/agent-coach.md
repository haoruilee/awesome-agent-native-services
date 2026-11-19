# Agent Coach

> **"Agent Coach: tested skills and a daily coach for AI agents"**

| | |
|---|---|
| **Website** | https://upskill.coach |
| **Docs** | https://upskill.coach/llms.txt |
| **GitHub** | None (hosted service, closed source) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **Funding / Compliance** | Free. Operator: Avatar 8 LLC (ops@avatar33.com). Hosted service is closed source; there is no public application repository |
| **Latest-month signal** | Live on 2026-11-19: [homepage](https://upskill.coach), [start](https://upskill.coach/start), [llms.txt](https://upskill.coach/llms.txt), [OpenAPI](https://upskill.coach/openapi.json), [rules](https://upskill.coach/api/v1/rules) (all HTTP 200). MCP `initialize` at `https://upskill.coach/mcp` returns `agent-coach` 0.1.0 with 13 tools. [Catalog](https://upskill.coach/api/v1/catalog) version 0.5.1: 126 items, 121 with vetting status pass |
| **Verified at** | 2026-11-19 |

---

## Official Website

https://upskill.coach

---

## Official Repo

None. Agent Coach is a hosted, closed-source service operated by Avatar 8 LLC. Proposal issue #351 disclosed that the submitter works on Agent Coach.

---

## ⭐ How to Use (Agent Onboarding)

> **URL Onboarding — an agent reads one document, registers itself, and starts its daily check-ins.**

**One-sentence instruction:**

```
Read https://upskill.coach/start and follow it.
```

**Interaction pattern:** `URL Onboarding` ⭐

`/start` walks the agent through the whole setup on its own: `POST /api/v1/agents` returns an `agent_id` and an `api_key` (shown once), then the agent sets one north-star metric, gets scanned recommendations, and checks in daily. There is no captcha and no dashboard step. `owner_email` is optional but is the only key recovery path; the owner confirms the address once by email. If the owner is not around, the agent sets `"constraints": {"owner_present": false}` and adopts only items with `owner_approval_needed: false`.

---

## Agent Skills

**Status:** ⚠️ Not yet published

Search community skills: `npx clawhub@latest search agent-coach`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **Endpoint** | `https://upskill.coach/mcp` (Streamable HTTP) |
| **Auth** | No OAuth. `register_agent`, `get_rules`, `search_library` and `get_library_item` need no key; later tools take the `api_key` from registration (argument or `Authorization: Bearer`) |
| **Tools** | `register_agent`, `set_goals`, `get_recommendations`, `update_items`, `check_in`, `get_report`, `share_report`, `get_digest`, `get_rules`, `rotate_key`, `delete_agent`, `search_library`, `get_library_item` |
| **Docs** | https://upskill.coach/docs/mcp |

---

## What It Does

Agent Coach is a training coach for AI agents. The agent registers itself, declares one north-star metric with a fixed definition and baseline, its job type, stage and capability gaps, and gets matched with skills, MCP servers, repos and prompts from a library that is security-scanned at a pinned commit (prompt injection, malicious code, leaked secrets, vulnerable dependencies).

The agent then checks in once a day. The coach applies published verdict rules to each adopted item (permanent, temporary for this task, or pending removal), tracks health signals such as north-star freshness and unsupported claims, and tags every reported value as self-reported or verified. A progress report can be read by the agent or shared with its owner.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage title: **"Agent Coach: tested skills and a daily coach for AI agents"**. [llms.txt](https://upskill.coach/llms.txt): **"A training coach for AI agents"** |
| **Agent-specific primitive** | Agent self-registration that mints a per-agent credential; one north-star goal with a fixed definition for that agent; `owner_approval_needed` on every library item so the agent knows what it may adopt alone; a daily `check_in` that returns keep/drop verdicts on the agent's own toolbelt |
| **Autonomy-compatible control plane** | After registration the agent sets goals, searches the scanned library, adopts or declines items, checks in, rotates its key and deletes itself without a human click. Recommendations are suggestions; the setup doc tells the agent to ask its owner before installing anything that runs code, needs keys or costs money |
| **M2M integration surface** | URL onboarding (`/start`), REST + [OpenAPI](https://upskill.coach/openapi.json), remote MCP, [llms.txt](https://upskill.coach/llms.txt) / [llms-full.txt](https://upskill.coach/llms-full.txt), markdown copy of every page (`.md` or `Accept: text/markdown`) |
| **Identity / delegation** | Each agent gets its own `agent_id` + `api_key`; check-ins are attributed to it. The owner (`owner_email`) is a separate party who confirms the address, recovers a lost key and can receive an optional digest |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Register** | `POST /api/v1/agents` or MCP `register_agent` returns `agent_id` and `api_key` |
| **Goals** | `set_goals`: one north-star metric with definition and baseline, deliverable, capability gaps, constraints |
| **Scanned library** | `search_library`, `get_library_item`: items scanned at a pinned commit, with vetting status and `owner_approval_needed` |
| **Recommendations** | `get_recommendations` matched to the agent's job type, stage and gaps; `update_items` to adopt or decline |
| **Check-in** | `check_in` once a day; verdicts follow the public rules at https://upskill.coach/api/v1/rules |
| **Report** | `get_report`, `share_report`, `get_digest` |
| **Key lifecycle** | `rotate_key`, `delete_agent` |

---

## Autonomy Model

1. The agent reads https://upskill.coach/start.
2. It calls `POST /api/v1/agents` (or MCP `register_agent`) and saves `api_key` and `agent_id` in its private memory or secrets store.
3. It sets one north-star with `set_goals`, then calls `get_recommendations`.
4. It adopts items with `owner_approval_needed: false` on its own and queues the rest for its owner.
5. It calls `check_in` daily and applies the returned verdicts (keep, temporary, pending removal).
6. A person is involved only to confirm the owner email, approve installs that run code, need keys or cost money, and agree before a report is shared publicly.

---

## Identity and Delegation Model

- The agent is the principal: `agent_id` + `api_key`, sent as `Authorization: Bearer` on later calls.
- `owner_email` is a separate party for confirmation, key recovery and the optional digest; confirmation emails are rate-limited.
- The agent can rotate its key and, when the owner asks, delete itself.
- Boundary, stated plainly: the hosted service is closed source; the identity is a bearer key, not a cryptographic agent identity; there is no published Agent Skill package yet.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| URL Onboarding | https://upskill.coach/start |
| REST API | `https://upskill.coach/api/v1`, Bearer `api_key` ([reference](https://upskill.coach/docs/rest-api)) |
| OpenAPI | https://upskill.coach/openapi.json |
| MCP | `https://upskill.coach/mcp` |
| Docs for LLMs | https://upskill.coach/llms.txt, https://upskill.coach/llms-full.txt |

---

## Human-in-the-Loop Support

Built in, as guidance plus item flags. Each library item carries `owner_approval_needed`; the setup doc tells the agent to ask its owner before installing anything that runs code, needs keys or accounts, or costs money, and not to share its public report until the owner agrees. Registration and check-ins need no human click. The owner can confirm their address, recover a lost key and receive an optional digest.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Awesome lists / skill directories** | Pages a person browses and pastes into a config. They do not register the agent, give it a credential, or run a keep/drop loop on its toolbelt |
| **Smithery / ClawHub** | Registries for discovering and installing tools. They do not tie items to one declared goal or measure whether an adopted item helped that agent |

---

## Use Cases

- **Find a vetted tool** — search a library scanned for prompt injection, malicious code and leaked secrets before adopting a skill or MCP server
- **Goal-matched toolbelt** — get recommendations for the agent's job type, stage and capability gaps
- **Daily keep/drop** — check in daily and drop items that go unused, keep failing, or coincide with a north-star regression
- **Owner report** — share a progress report with the agent's owner
