# Riza

> **"AI writes code. Riza runs it."**

| | |
|---|---|
| **Website** | https://riza.io/ |
| **Docs** | https://docs.riza.io/ |
| **GitHub** | https://github.com/riza-io |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |
| **Funding / Compliance** | API-first cloud with self-hosting option |

---

## Official Website

https://riza.io/

---

## Official Repo

https://github.com/riza-io

---

## How to Use (Agent Onboarding)

**The quickest path for an agent to start using this service.**

```bash
uv add rizaio
```

Then execute generated code directly via the API/SDK:

```python
import rizaio
riza = rizaio.Riza()
response = riza.command.exec(code="print('Hello, World!')", language="python")
```

---

## Agent Skills

**Status:** ⚠️ Not yet published

No official AgentSkills `SKILL.md` package is published by Riza as of April 2026.

Search community skills: `npx clawhub@latest search riza`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/riza-io/riza-mcp |
| **Transport** | stdio (package) |
| **Compatible Clients** | Claude Desktop, Cursor, other MCP-compatible clients |

---

## What It Does

Riza is a code-execution runtime built for AI systems that need to run untrusted, LLM-generated code safely and quickly. It provides an API-first execution layer with low startup latency, configurable network/env controls, and structured outputs (`stdout`, `stderr`, exit codes).

Riza also supports tool-style execution patterns where agents can create reusable tools and execute them on demand, making it a strong fit for autonomous agents that need repeatable programmable actions.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: "AI writes code. Riza runs it." and "giving LLMs the ability to run code" (https://riza.io/) |
| **Agent-specific primitive** | LLM code execution, reusable tool execution, and MCP integration for agent tool-use workflows |
| **Autonomy-compatible control plane** | Agents can execute code via API without per-action human clicks; policy controls include execution isolation and runtime config |
| **M2M integration surface** | REST API, Python/TypeScript/Go SDKs, MCP server |
| **Identity / delegation** | API-key based project identity, execution-level configuration, and attributable tool/code runs per account |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Command Exec API** | Executes untrusted code in isolated runtime and returns structured result artifacts |
| **Tools API** | Save and invoke reusable agent-callable tools with schema-validated inputs |
| **Secrets API** | Store secrets and attach them at execution time instead of injecting raw credentials into prompts |
| **MCP Server** | Exposes Riza execution as MCP tools for standardized agent integrations |
| **Self-Hosting** | Deploy Riza on your own infrastructure with similar API surface |

---

## Autonomy Model

1. Agent receives a task requiring code execution or transformation.
2. Agent generates code or picks a stored tool.
3. Agent calls Riza via SDK/API/MCP with runtime constraints.
4. Riza executes in isolated environment and returns structured outputs.
5. Agent uses outputs to continue planning, retry, or produce final result.

---

## Identity and Delegation Model

- Agent uses service credentials (API key / project-scoped auth) to execute actions.
- Runtime policy is delegated at request-time (allowed hosts, env vars, resource constraints).
- Executions are attributable to the calling account/project for auditability.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | Primary execution and tooling interface |
| Python SDK | `rizaio` package for command/tool execution |
| TypeScript SDK | Official JS/TS API client |
| Go SDK | Official Go API client |
| MCP | Official `riza-mcp` integration |

---

## Human-in-the-Loop Support

Optional. Riza is designed for autonomous calls, but teams can insert review gates in their own orchestration layer before submitting execution requests.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Generic serverless functions** | Not purpose-built for LLM-generated untrusted code; usually require app-specific deployment and lack agent-oriented tool primitives |
| **Raw Docker on your own infra** | Requires manual sandbox lifecycle, scaling, and security engineering that Riza provides as an API-first agent runtime |
| **Traditional CI runners** | Built for human/dev pipelines, not low-latency agent tool-calling loops |

---

## Use Cases

- **LLM-generated code execution** in production agent loops.
- **Data extraction/transformation agents** on heterogeneous inputs.
- **Tool-writing agents** that generate and later reuse functions.
- **Code-generation eval harnesses** for model/prompt iteration.
