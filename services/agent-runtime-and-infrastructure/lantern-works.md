# Lantern Works

> **"GPU price comparison for agents, checked daily."**

| | |
|---|---|
| **Website** | https://thelanternworks.com |
| **Docs** | https://thelanternworks.com/for-agents/ · https://thelanternworks.com/install/ |
| **MCP** | https://lantern-works-mcp.lantern-works.workers.dev/mcp |
| **GitHub** | https://github.com/connormatthewdouglas/agent-work-stack-deals |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **Disclosure** | Submitted by the operator of Lantern Works. Some listed GPU vendors may have affiliate programs; ranking does not use affiliate status. |

---

## Official Website

https://thelanternworks.com

---

## Official Repo

https://github.com/connormatthewdouglas/agent-work-stack-deals

---

## How to Use (Agent Onboarding)

**Interaction pattern:** MCP (local stdio package or hosted Streamable HTTP). No API key for the core tools.

```
# MCP (stdio, PyPI package lantern-works-deals-mcp):
Add to mcp_servers: "command": "uvx", "args": ["lantern-works-deals-mcp"]

# MCP (hosted Streamable HTTP):
claude mcp add --transport http lantern-works https://lantern-works-mcp.lantern-works.workers.dev/mcp

# Agent guide:
Read https://thelanternworks.com/for-agents/ and follow the install steps.
```

---

## Agent Skills

**Status:** ⚠️ Not yet published

Search community skills: `npx clawhub@latest search lantern-works`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/connormatthewdouglas/agent-work-stack-deals (PyPI: `lantern-works-deals-mcp`) |
| **Transport** | stdio (`uvx lantern-works-deals-mcp`) / Streamable HTTP (`https://lantern-works-mcp.lantern-works.workers.dev/mcp`) |
| **Auth** | None for the core comparison and estimate tools |
| **Compatible Clients** | Claude Desktop, Claude Code, Cursor, and other MCP clients |

---

## What It Does

Lantern Works tracks GPU rental prices across cloud GPU vendors and checks them daily. Agents call MCP tools to compare current rates for a GPU, estimate what a job will cost before it runs, and see which prices changed recently.

Every rate comes with the vendor's `source_url`, an evidence snippet, and a `checked_at` time, so an agent can cite where a price came from and how fresh it is. Job estimates come back as itemized receipts. Lantern Works does not rent GPUs or spend money on the agent's behalf; it only compares and estimates.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | *"GPU price comparison for agents, checked daily"* / *"Give your agent live GPU prices"* — https://thelanternworks.com · https://thelanternworks.com/for-agents/ |
| **Agent-specific primitive** | MCP tools (`compare_gpu_prices`, `estimate_job_cost`, `optimize_agent_stack`, `get_price_changes`, …) that return cited, dated rates and itemized job-cost receipts an agent can act on before spending |
| **Autonomy-compatible control plane** | Free, keyless MCP for the core tools; read-only toward vendors, so agents can compare and estimate without a human in the loop |
| **M2M integration surface** | stdio MCP (`uvx lantern-works-deals-mcp`), hosted Streamable HTTP MCP, JSON feeds and docs at /install/ and /for-agents/ |
| **Identity / delegation** | No agent spends or rents through Lantern Works; each rate carries `source_url`, evidence snippet, and `checked_at` so the agent's decision is attributable to a dated source |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`compare_gpu_prices`** | Current rental rates for a GPU across vendors, each with source URL and check time |
| **`estimate_job_cost`** | Itemized cost receipt for a job (GPU, count, hours) before the agent commits |
| **`optimize_agent_stack`** | Suggests a lower-cost mix of providers for an agent's workload |
| **`get_price_changes`** | Recent price moves, so an agent can re-check a plan |
| **Price watches** | `create_watch_key` / `watch_price` / `list_watches` / `delete_watch` for tracking a rate over time |

---

## Autonomy Model

1. Agent adds the MCP server (stdio via `uvx` or the hosted URL); no key needed for core tools.
2. Before launching a GPU job, the agent calls `compare_gpu_prices` or `estimate_job_cost`.
3. Agent picks a vendor using the cited, dated rates and keeps the receipt with its plan.
4. Optionally, the agent calls `get_price_changes` or a price watch to re-check before the next run.

---

## Identity and Delegation Model

- No account or API key is needed for the core tools, so no user credentials are delegated.
- Lantern Works never rents, buys, or spends on the agent's behalf; it is compare and estimate only.
- Every rate carries `source_url`, an evidence snippet, and `checked_at`, giving an audit trail for the agent's choice.
- Wrong prices can be reported through a public issue form.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP (stdio) | `uvx lantern-works-deals-mcp` (PyPI `lantern-works-deals-mcp`) |
| MCP (Streamable HTTP) | `https://lantern-works-mcp.lantern-works.workers.dev/mcp` |
| JSON feeds + docs | https://thelanternworks.com/install/ · https://thelanternworks.com/for-agents/ |

---

## Human-in-the-Loop Support

None is required to compare or estimate. Because Lantern Works never spends money, any actual GPU rental stays with the agent's own vendor account and whatever approval flow its operator sets there.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Vendor consoles (Vast, RunPod, etc.)** | Built for humans to click through one vendor's offers; no cited, multi-vendor MCP tool surface |
| **Generic GPU price comparison pages** | Human-readable tables with no agent tools, per-rate source URLs, or itemized job-cost receipts |
| **Web search for prices** | Unstructured, often stale results with no `checked_at` time an agent can rely on |

---

## Use Cases

- **Cost check before a training run** — the agent estimates the job's cost across vendors before renting anything
- **Cheapest GPU for an inference job** — compare current rates for a GPU and cite the source in the plan
- **Re-plan when prices move** — watch a rate or pull recent changes and adjust the vendor choice
