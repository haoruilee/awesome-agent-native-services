# Galileo

> **"Galileo is the AI observability and eval engineering platform where offline evals become production guardrails."**

| | |
|---|---|
| **Website** | https://galileo.ai |
| **Docs** | https://docs.galileo.ai |
| **GitHub** | https://github.com/rungalileo |
| **Classification** | `agent-native` |
| **Category** | [Observability & Tracing Services](README.md) |
| **License** | Mixed (hosted product + open-source SDKs/examples) |

---

## Official Website

https://galileo.ai

---

## Official Repo

https://github.com/rungalileo

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `MCP` (Cursor / VS Code) + Galileo API key

1. Open your MCP settings in Cursor or VS Code.
2. Add Galileo MCP server:

```json
{
  "mcpServers": {
    "galileo_mcp_server": {
      "url": "https://api.galileo.ai/mcp/http/mcp",
      "headers": {
        "Galileo-API-Key": "YOUR-API-KEY",
        "Accept": "text/event-stream"
      }
    }
  }
}
```

3. Restart IDE and ask the assistant: `Can you show me how to add Galileo logging to my agent bot?`

Reference: https://docs.galileo.ai/getting-started/mcp/setup-galileo-mcp

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add ...` package found.

Search community skills:

```bash
npx clawhub@latest search galileo
```

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Docs** | https://docs.galileo.ai/getting-started/mcp/setup-galileo-mcp |
| **Transport** | Streamable HTTP (`Accept: text/event-stream`) |
| **Endpoint** | `https://api.galileo.ai/mcp/http/mcp` |
| **Compatible Clients** | Cursor, VS Code (with AI assistant / Copilot) |

---

## What It Does

Galileo is an observability and evaluation platform for LLM systems, with explicit support for agent workflows. It captures traces, runs evals, surfaces failure patterns (Signals), and provides IDE-integrated remediation workflows via MCP.

The MCP server extends this into coding-time operations: your IDE agent can create datasets, run experiments, inspect Log stream signals, and get integration guidance without leaving the editor.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage emphasizes agent reliability: "Observe, evaluate, guardrail, and improve agent behavior in minutes" — https://galileo.ai/ |
| **Agent-specific primitive** | Agent eval primitives include Log stream Signals and agent metrics, plus MCP-assisted root-cause/fix loop from IDE — https://docs.galileo.ai/release-notes |
| **Autonomy-compatible control plane** | MCP lets coding agents pull latest signals and propose fixes directly in IDE workflows — https://docs.galileo.ai/release-notes |
| **M2M integration surface** | MCP endpoint, SDK/API docs, tracing/logging instrumentation and experiment APIs — https://docs.galileo.ai |
| **Identity / delegation** | API-key based access (`Galileo-API-Key` header), project/log stream scoped operations, and trace/session artifacts for attribution — https://docs.galileo.ai/getting-started/mcp/setup-galileo-mcp |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent Evals MCP** | IDE-accessible eval/observability operations via MCP |
| **Signals (Log streams)** | Root-cause insights on where agents deviate from expected behavior |
| **Synthetic Dataset Generation** | Generate eval datasets for edge-case simulation |
| **Experiments & Prompt Templates** | Run controlled evaluations and tune prompts against metrics |
| **Tracing / Analytics** | Trace all steps taken by an agent and evaluate end-to-end behavior |

---

## Autonomy Model

Agent runtime emits traces/logs to Galileo
    ↓
Galileo computes metrics/signals and stores trajectory artifacts
    ↓
Coding agent (in Cursor/VS Code) calls Galileo MCP tools
    ↓
Agent retrieves issues, proposes fixes, and updates instrumentation/prompts
    ↓
New runs are traced/evaluated again for closed-loop improvement

---

## Identity and Delegation Model

- Access is delegated through `Galileo-API-Key` in MCP configuration.
- Operations are bounded to the caller's Galileo account/workspace context.
- Trace/log stream artifacts create attributable records of agent behavior and changes.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP (HTTP) | `https://api.galileo.ai/mcp/http/mcp` |
| SDK / API | Python/TypeScript SDKs and API reference under docs |
| Web Console | Hosted UI for traces, metrics, datasets, and experiments |

---

## Human-in-the-Loop Support

Optional. Human reviewers can inspect traces/signals and approve remediation changes, but core logging/eval loops and MCP queries are machine-driven.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Infrastructure monitoring only (CPU, memory, uptime dashboards)** | Useful for system health, but does not natively model agent traces, eval datasets, or agent-quality metrics |
| **Log storage/search tools** | Centralize logs, but typically require custom pipelines to derive agent-eval outcomes and trajectory-level analysis |
| **Manual QA workflows** | Rely on human review cycles and do not provide a machine-callable MCP surface for coding-time agent remediation loops |

---

## Use Cases

- **Agent regression triage in IDE** — pull recent signals and patch likely root causes from coding assistant.
- **Continuous agent evals** — generate synthetic datasets for edge cases and run experiments before release.
- **Prompt and workflow tuning** — iterate templates and observe impact on agent behavior metrics.
- **Production incident debugging** — inspect log streams to locate failing branches/tool paths in agent trajectories.
