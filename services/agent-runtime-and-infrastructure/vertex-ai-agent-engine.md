# Gemini Enterprise Agent Platform (formerly Vertex AI Agent Engine)

> **"Scale your agents"** — [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale)

| | |
|---|---|
| **Website** | https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale |
| **Docs** | https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale |
| **GitHub** | https://github.com/googleapis/python-aiplatform |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **Provider** | Google Cloud |
| **Verified at** | 2026-10-19 |

---

## Official Website

https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale

Former Vertex AI Agent Engine / Agent Builder URLs (including `cloud.google.com/agent-builder/agent-engine/overview` and sibling set-up/deploy pages) redirect here. Live H1: *"Scale your agents"*. Product name: **Gemini Enterprise Agent Platform**.

---

## Official Repo

Gemini Enterprise Agent Platform (formerly Vertex AI Agent Engine) is a managed Google Cloud service. Client integration is through the **Vertex AI SDK for Python** (open source):

https://github.com/googleapis/python-aiplatform

Other Google Cloud client libraries (REST, gRPC) apply for non-Python stacks per [Google Cloud documentation](https://cloud.google.com/docs).

---

## How to Use (Agent Onboarding)

**SDK / REST:**

```bash
pip install "google-cloud-aiplatform[agent_engines,adk]"
```

Then follow [Scale your agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale) — former set-up / develop / deploy URLs redirect to this hub. Deployment still uses `client.agent_engines.create(...)` with optional source packages, container image, or [Developer Connect](https://cloud.google.com/developer-connect/docs/connect-repo) Git linkage.

---

## Agent Skills

**Status:** ⚠️ Not yet published

Search community skills: `npx clawhub@latest search vertex agent engine`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ No standalone MCP server

Agents deployed on Agent Engine can call external MCP servers from agent code; Google does not ship a first-party `vertex-agent-engine` MCP binary.

| Detail | Value |
|---|---|
| **Integration pattern** | Deploy agent that wraps or proxies MCP tool calls |
| **Compatible Clients** | Any agent host that can use Vertex AI credentials |

---

## What It Does

Gemini Enterprise Agent Platform (formerly Vertex AI Agent Engine) is Google Cloud’s managed layer for **running agent workloads in production**. Live docs: *"a fully managed environment for developers to handle testing, release management, and reliability at a global scale"* — **Agent Runtime**, **Sessions**, **Memory Bank**, **Code Execution**, **Computer Use**, plus evaluation and example-store quality loops. Framework guides on the scale page still cover ADK, LangChain, LangGraph, LlamaIndex, AG2, and Agent2Agent (A2A).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Live H1 *"Scale your agents"*; *"Bringing AI agents into production requires a high-performance runtime"* — [scale](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale) |
| **Agent-specific primitive** | Managed **Agent Runtime**, **Sessions**, **Memory Bank**, **Code Execution** sandbox, **Example Store**, **Evaluation Service**, **agent identity** — not generic VM or batch job abstractions |
| **Autonomy-compatible control plane** | Fully managed runtime so teams *"focus entirely on application creation"*; agents run without per-turn human clicks once deployed |
| **M2M integration surface** | Vertex AI SDK (`agent_engines` API), REST, CI/CD-style deployment from source — [scale](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale) |
| **Identity / delegation** | **IAM agent identity** ties credentials to the deployed agent resource; optional **custom service account** per deployment — [agent identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent Engine Runtime** | Managed deploy/scale surface for agent HTTP servers and framework integrations |
| **Sessions** | Store interaction history for definitive conversation context |
| **Memory Bank** | Retrieve and personalize from cross-session memory |
| **Code Execution** | Secure isolated execution environment for agent-written code |
| **Observability** | OpenTelemetry-compatible tracing plus Cloud Monitoring and Logging |
| **Agent identity (preview)** | IAM-oriented identity for the deployed agent resource |

---

## Autonomy Model

1. Developer packages an agent (ADK, LangGraph, custom, etc.) and calls `client.agent_engines.create` with requirements, entrypoint, and optional identity or service account.
2. Google Cloud builds/hosts the runtime; the agent serves requests over the managed endpoint.
3. Sessions and Memory Bank update through API calls without a human in the loop for each step.
4. Code Execution and tool calls (including external MCP) run under configured policies and quotas.

---

## Identity and Delegation Model

- **Agent identity:** Identity bound to the Agent Platform resource — [agent identity overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview)
- **Custom service account:** Deployed agent runs as a dedicated GCP service account for fine-grained IAM to BigQuery, Cloud SQL, Secret Manager, etc.
- **Audit:** Cloud Logging and Cloud Trace provide request- and trace-level attribution for operations issued through the managed endpoint

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Vertex AI SDK (Python) | `google-cloud-aiplatform` with `agent_engines` — primary path in docs |
| REST / gRPC | Vertex AI platform APIs for ReasoningEngine / agent resources |
| OpenTelemetry | Tracing integration per [runtime tracing docs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/tracing) |
| A2A | Agent2Agent protocol guides remain linked from the [scale hub](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale) |

---

## Human-in-the-Loop Support

Optional at application level (your agent code or upstream product). Agent Platform provides governance (IAM, VPC-SC) and observability, not a built-in approval inbox primitive.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Cloud Run / GKE alone** | General container hosting; no first-class Sessions, Memory Bank, agent identity, or Agent Platform evaluation integrations |
| **Vertex AI (models only)** | Model inference APIs; Agent Platform is the separate production agent runtime and memory/session layer |
| **Dialogflow / Contact Center AI** | Human-business workflow and bot-builder surfaces; different primary consumer than autonomous tool-using agents |

---

## Use Cases

- **Enterprise agents on GCP** — RAG and tool-using agents with VPC-SC, CMEK, and data residency
- **Multi-agent systems** — A2A-linked agents across frameworks
- **Long-running assistants** — Sessions + Memory Bank for continuity across conversations
- **Code-using agents** — Managed Code Execution instead of self-built sandboxes
