# Amazon Bedrock AgentCore

> **"Purpose-built for deploying and scaling dynamic AI agents and tools."**

| | |
|---|---|
| **AWS Page** | https://aws.amazon.com/bedrock/agentcore/ |
| **Docs** | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/ |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **Provider** | Amazon Web Services |

---

## Official Website

https://aws.amazon.com/bedrock/agentcore/

---

## Official Repo

AWS managed service — no open-source repository. SDK access via the standard AWS SDK:

https://github.com/aws/aws-sdk-python (Python: `boto3`)

https://github.com/aws/aws-sdk-js-v3 (JavaScript/TypeScript)

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ⚠️ No official skill published by AWS for AgentCore yet.

AgentCore is an AWS managed service primarily integrated via the AWS SDK and CloudWatch. No `SKILL.md`-based skill has been published to the AgentSkills ecosystem as of Q1 2026.

```bash
# No official install command yet — watch:
# https://aws.amazon.com/bedrock/agentcore/
```

---

## MCP

**Status:** ⚠️ No standalone MCP server

AgentCore uses OpenTelemetry as its telemetry standard and integrates with AWS-native tooling (CloudWatch, ADOT SDK). It does not publish a standalone MCP server. Agents running on AgentCore can consume MCP servers hosted externally via the AgentCore Gateway.

| Detail | Value |
|---|---|
| **Observability Docs** | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html |
| **Memory Docs** | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html |
| **Telemetry Standard** | OpenTelemetry (OTEL) + AWS Distro for OpenTelemetry (ADOT) |

---

## What It Does

Amazon Bedrock AgentCore is a modular, purpose-built agent runtime suite from AWS. Unlike Bedrock's model inference APIs (which are general-purpose), AgentCore addresses the specific operational problems of running agents at scale: **Runtime** (managed execution), **Memory** (session and cross-session persistence), **Identity** (verified agent tokens), **Gateway** (tool access routing and security), and **Observability** (OpenTelemetry-based tracing and dashboards).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | AWS explicitly positions AgentCore as a separate product suite: *"purpose-built for deploying and scaling dynamic AI agents and tools"* |
| **Agent-specific primitive** | Agent runtime (not just Lambda), memory with automatic insight extraction, identity tokens for agents, tool gateway, OTEL agent traces |
| **Autonomy-compatible control plane** | Fully managed execution with per-agent session isolation; agents run without per-action human supervision |
| **M2M integration surface** | AWS SDK, REST API, OpenTelemetry, CloudWatch integration |
| **Identity / delegation** | Built-in AgentCore Identity with verified agent tokens; full CloudWatch audit trail per agent action |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **AgentCore Runtime** | Managed execution environment for hosting and running AI agents with isolated, scalable runtime sessions |
| **AgentCore Memory** | Short-term and long-term memory services that capture session interactions and extract durable insights across sessions |
| **AgentCore Identity** | Verified identity tokens for agent instances, enabling attribution and policy enforcement |
| **AgentCore Gateway** | Secure proxy for routing and governing tool and API access on behalf of agents |
| **AgentCore Observability** | OpenTelemetry-compatible traces, metrics, and dashboards for agent execution |

### Module Breakdown

### AgentCore Runtime

Managed execution environment for hosting and running AI agents. Handles the compute layer so agent code runs in an isolated, scalable environment without managing servers.

### AgentCore Memory

| Memory Type | Description |
|---|---|
| **Short-term** | Captures turn-by-turn interactions within a single session |
| **Long-term** | Automatically extracts and stores key insights (preferences, facts) across sessions |

Memory is updated and retrieved autonomously; no human manages what is remembered.

### AgentCore Identity

Verified identity tokens for agents — enabling cryptographic attribution of actions to specific agent instances. Integrates with AgentCore Gateway and Observability for end-to-end audit.

### AgentCore Gateway

Secure proxy controlling which external tools, APIs, and services an agent can access. Centralizes tool routing and access control.

### AgentCore Observability

| Feature | Detail |
|---|---|
| **Real-time dashboards** | CloudWatch dashboards: session count, latency, duration, token usage, error rates |
| **OpenTelemetry** | OTEL-compatible for integration with existing monitoring stacks |
| **Trace visualization** | Per-agent execution traces in CloudWatch console |
| **Custom instrumentation** | AWS Distro for OpenTelemetry (ADOT) SDK for custom spans |
| **Built-in metrics** | Runtime, memory, gateway, built-in tools, and identity resources all emit metrics |

---

## Autonomy Model

Agents are deployed to AgentCore Runtime and execute autonomously. Session isolation ensures each run has its own context. Memory is updated across sessions automatically. Identity tokens enable audit without human observation of individual actions.

---

## Identity and Delegation Model

- AgentCore Identity issues verified tokens per agent instance
- Tokens are used by Gateway to enforce per-agent tool access policies
- All actions flow through Observability, creating a tamper-evident audit trail
- CloudWatch Transaction Search enables forensic replay of agent execution

---

## Protocol Surface

| Interface | Detail |
|---|---|
| AWS SDK | Primary integration surface for all AgentCore modules |
| REST API | AgentCore management and query APIs |
| OpenTelemetry | OTEL-compatible telemetry export |
| CloudWatch | Metrics, traces, and logs dashboard |
| ADOT SDK | AWS Distro for OpenTelemetry for custom instrumentation |

---

## Human-in-the-Loop Support

Optional. Observability layer captures all agent actions for post-hoc human review. AgentCore does not include a built-in approval primitive (that would be composed via HumanLayer or similar).

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **AWS Lambda** | Stateless compute; no agent session isolation, no memory, no identity tokens, no agent-specific observability |
| **AWS ECS/EKS** | Container orchestration for general workloads; no agent primitives |
| **AWS Step Functions** | Workflow orchestration for human-defined processes; no agent reasoning model, no memory |
| **Amazon Bedrock (base)** | Model inference API; AgentCore is the separate agent runtime layer built on top |

---

## Use Cases

- **Enterprise agent deployment** — organizations deploying customer-facing or internal agents at scale with full observability and compliance
- **Multi-agent architectures** — coordinating multiple specialized agents with isolated memory and identity
- **Regulated industries** — financial services, healthcare agents requiring audit trails and identity verification
- **Long-running research agents** — agents with persistent long-term memory that improves over multiple sessions
