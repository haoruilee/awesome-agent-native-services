# Vertex AI Agent Engine

> **"Vertex AI Agent Engine, a part of the Vertex AI Platform, is a set of services that enables developers to deploy, manage, and scale AI agents in production."**

| | |
|---|---|
| **Website** | https://cloud.google.com/agent-builder/agent-engine/overview |
| **Docs** | https://cloud.google.com/agent-builder/agent-engine/overview |
| **GitHub** | https://github.com/googleapis/python-aiplatform |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **Provider** | Google Cloud |

---

## Official Website

https://cloud.google.com/agent-builder/agent-engine/overview

---

## Official Repo

Vertex AI Agent Engine is a managed Google Cloud service. Client integration is through the **Vertex AI SDK for Python** (open source):

https://github.com/googleapis/python-aiplatform

Other Google Cloud client libraries (REST, gRPC) apply for non-Python stacks per [Google Cloud documentation](https://cloud.google.com/docs).

---

## How to Use (Agent Onboarding)

**SDK / REST:**

```bash
pip install "google-cloud-aiplatform[agent_engines,adk]"
```

Then follow [Set up the environment](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/set-up), [Develop an agent](https://cloud.google.com/agent-builder/agent-engine/develop/overview), and [Deploy the agent](https://cloud.google.com/agent-builder/agent-engine/deploy) — deployment uses `client.agent_engines.create(...)` with optional source packages, container image, or [Developer Connect](https://cloud.google.com/developer-connect/docs/connect-repo) Git linkage.

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

Vertex AI Agent Engine is Google Cloud’s managed layer for **running agent workloads in production**: deploy and scale agents, attach **Sessions** and **Memory Bank** for conversational context, run **Code Execution** in an isolated sandbox, and observe behavior through **Cloud Trace**, **Cloud Monitoring**, and **Cloud Logging**. It supports multiple Python agent frameworks (including ADK, LangChain, LangGraph, AG2, LlamaIndex) and the **Agent2Agent (A2A)** open protocol for interoperable multi-agent systems.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Google documents Agent Engine as *"a set of services that enables developers to deploy, manage, and scale AI agents in production"* and *"handles the infrastructure to scale agents in production"* — [overview](https://cloud.google.com/agent-builder/agent-engine/overview) |
| **Agent-specific primitive** | Managed **Agent Engine Runtime**, **Sessions**, **Memory Bank**, **Code Execution** sandbox, **Example Store** (preview), **agent identity** (preview) — not generic VM or batch job abstractions |
| **Autonomy-compatible control plane** | Autoscaling (`min_instances` / `max_instances`), concurrency, resource limits, VPC-SC, PSC-I, CMEK — agents run without per-turn human clicks once deployed |
| **M2M integration surface** | Vertex AI SDK (`agent_engines` API), REST, CI/CD and Terraform-style deployment from source — [deploy](https://cloud.google.com/agent-builder/agent-engine/deploy) |
| **Identity / delegation** | **Agent identity** (preview) ties credentials to the deployed agent resource; optional **custom service account** per deployment — [agent identity](https://cloud.google.com/agent-builder/agent-engine/agent-identity), [IAM setup](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/set-up#identity-and-permissions) |

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

- **Agent identity (preview):** Identity bound to the Agent Engine resource ID, independent of framework — [create agent identity](https://cloud.google.com/agent-builder/agent-engine/agent-identity#create-agent-identity)
- **Custom service account:** Deployed agent runs as a dedicated GCP service account for fine-grained IAM to BigQuery, Cloud SQL, Secret Manager, etc.
- **Audit:** Cloud Logging and Cloud Trace provide request- and trace-level attribution for operations issued through the managed endpoint

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Vertex AI SDK (Python) | `google-cloud-aiplatform` with `agent_engines` — primary path in docs |
| REST / gRPC | Vertex AI platform APIs for ReasoningEngine / agent resources |
| OpenTelemetry | Tracing integration per [Agent Engine tracing docs](https://cloud.google.com/agent-builder/agent-engine/manage/tracing) |
| A2A | [Agent2Agent protocol](https://cloud.google.com/agent-builder/agent-engine/develop/a2a) for cross-framework agent collaboration |

---

## Human-in-the-Loop Support

Optional at application level (your agent code or upstream product). Agent Engine provides governance (IAM, VPC-SC, threat detection preview) and observability, not a built-in approval inbox primitive.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Cloud Run / GKE alone** | General container hosting; no first-class Sessions, Memory Bank, agent identity, or Agent Engine evaluation integrations |
| **Vertex AI (models only)** | Model inference APIs; Agent Engine is the separate production agent runtime and memory/session layer |
| **Dialogflow / Contact Center AI** | Human-business workflow and bot-builder surfaces; different primary consumer than autonomous tool-using agents |

---

## Use Cases

- **Enterprise agents on GCP** — RAG and tool-using agents with VPC-SC, CMEK, and data residency
- **Multi-agent systems** — A2A-linked agents across frameworks
- **Long-running assistants** — Sessions + Memory Bank for continuity across conversations
- **Code-using agents** — Managed Code Execution instead of self-built sandboxes
