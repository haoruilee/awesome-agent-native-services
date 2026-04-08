# Modal

> **"AI infrastructure that developers love."**

| | |
|---|---|
| **Website** | https://modal.com |
| **Docs** | https://modal.com/docs |
| **GitHub** | https://github.com/modal-labs/modal-client |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/modal-labs/modal-client?style=social)](https://github.com/modal-labs/modal-client) |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |

---

## Official Website

https://modal.com

---

## Official Repo

https://github.com/modal-labs/modal-client — Python client for Modal platform

---

## How to Use (Agent Onboarding)

**Python SDK — decorate functions for serverless GPUs, inference, sandboxes, and batch jobs.**

```bash
pip install modal
modal setup
# Define Modal app in Python per https://modal.com/docs/guide
```

**Sandboxes** — programmatically create **ephemeral secure environments** for untrusted code — see [Sandboxes product](https://modal.com/products/sandboxes).

---

## Agent Skills

**Status:** ⚠️ No official AgentSkills bundle located.

```bash
npx clawhub@latest search modal
```

---

## MCP

**Status:** ⚠️ Not an MCP product; teams deploy **MCP servers** on Modal (see customer quotes on modal.com).

---

## What It Does

Modal is **serverless infrastructure for AI workloads**: **inference**, **fine-tuning**, **batch** jobs, **notebooks**, and **dynamic sandboxes** with **sub-second cold starts**, **elastic GPU/CPU** scaling, and **unified observability**. It is explicitly marketed for **LLM inference**, **evals**, **RL environments**, and **MCP servers** at scale — workloads that autonomous agents and their orchestrators spawn unpredictably.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage and examples center **AI inference, sandboxes, and agent-scale batch**; testimonial cites **MCP servers** and **evals** as core workloads |
| **Agent-specific primitive** | **Programmatic sandboxes** for **untrusted agent-generated code**; **elastic parallel containers** for fan-out tool/batch agent patterns |
| **Autonomy-compatible control plane** | Jobs start/stop via **API/SDK** without human console steps; scales to zero when idle |
| **M2M integration surface** | Python SDK, CLI, HTTP web endpoints for Modal functions |
| **Identity / delegation** | **Workspace / token** auth; team controls for secrets and data residency |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`@app.function`** | Serverless function with GPU/CPU, image, and concurrency config |
| **Sandboxes** | Isolated, ephemeral environments for untrusted execution |
| **Volumes & buckets** | Data attachments for models and datasets |
| **Web endpoints** | Expose agent backends over HTTPS |
| **Scheduling & parallelism** | Map huge batch/agent workloads across many containers |

---

## Autonomy Model

```
Agent orchestrator calls Modal SDK or HTTP endpoint
    ↓
Modal schedules container with correct image + GPU
    ↓
Function runs (inference, sandbox exec, batch step)
    ↓
Results stream back; containers scale down automatically
```

---

## Identity and Delegation Model

- **Modal tokens** authenticate API access.
- **Secrets** injected as environment or Modal secret objects — not embedded in agent prompts.
- **Team policies** govern who can deploy and spend.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install modal` |
| CLI | `modal` — deploy, run, logs |
| HTTP | Function endpoints — see docs |

---

## Human-in-the-Loop Support

Notebooks and dashboards support human debugging; production agent paths are unattended.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw Kubernetes** | You manage autoscaling, images, and GPU quotas; Modal abstracts cold start and scheduling |
| **Lambda without GPUs** | Poor fit for LLM inference and large parallel agent batches |
| **Single VM** | No elastic fan-out for thousands of concurrent agent tool calls |

---

## Use Cases

- **Tool sandboxes** — run agent-written code safely at scale
- **Batch evals / RL** — parallel rollouts referenced in Modal marketing
- **Hosted MCP servers** — low-ops deployment surface for tool endpoints
