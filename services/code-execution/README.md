# Code Execution Services

> Services that give AI agents a **secure, isolated runtime for executing generated code** — without human-side sandbox setup, without risking the host environment, and with output formatted for direct LLM consumption.

## Why This Category Exists

AI agents that generate and execute code face a fundamental security and logistics problem: where does the code actually run?

Running AI-generated code on the host machine is dangerous — malicious or buggy code can damage the system, exfiltrate data, or consume resources without bound. Building a custom sandbox for each agent is time-consuming and error-prone. Sharing a single sandbox across agents creates isolation failures.

Agent-native code execution services solve this with:

1. **Ephemeral, per-session sandboxes** — each agent run gets a clean isolated environment
2. **Fast startup** — sandboxes ready in ~150ms, not minutes
3. **Stateful execution** — the agent can run multiple code blocks in the same context, with state persisting between calls
4. **Output streaming** — stdout, stderr, charts, and files streamed back to the agent in real time
5. **No infrastructure management** — the agent calls an API; the service handles provisioning and teardown

## Services

| Service | Tagline | Protocol Surface | MCP? |
|---|---|---|---|
| [Axern](axern.md) [![⭐](https://img.shields.io/github/stars/cofy-x/axern?style=social)](https://github.com/cofy-x/axern) | Open-source sandbox platform for AI agents | CLI, gRPC/HTTP, Go/Python/TypeScript SDKs, Axrun evidence | ⚠️ |
| [OpenSandbox](opensandbox.md) [![⭐](https://img.shields.io/github/stars/opensandbox-group/OpenSandbox?style=social)](https://github.com/opensandbox-group/OpenSandbox) | Secure, fast, extensible sandbox runtime for AI agents | Sandbox runtime, Kubernetes, MCP server | ✅ |
| [CodeRunner](coderunner.md) [![⭐](https://img.shields.io/github/stars/instavm/coderunner?style=social)](https://github.com/instavm/coderunner) | A local sandbox for your AI agents | Apple Containers, local sandbox CLI, MCP | ✅ |
| [E2B](e2b.md) | Cloud for AI agents — secure sandboxes for AI-generated code | Python SDK, TypeScript SDK, REST API | ❌ |
| [Daytona](daytona.md) | Secure elastic infrastructure for running AI-generated code | Python/TS/Ruby/Go SDK, REST, Daytona CLI + MCP | ✅ |
| [Runloop](runloop.md) | Your AI agent accelerator — Devboxes and agent benchmarks | Python/TS SDK, REST, Runloop CLI (`rli`) + MCP | ✅ |
| [Vercel Sandbox](vercel-sandbox.md) [![⭐](https://img.shields.io/github/stars/vercel/sandbox?style=social)](https://github.com/vercel/sandbox) | Firecracker microVMs for AI-generated and untrusted code | `@vercel/sandbox` SDK, REST API, Sandbox CLI | ❌ |
| [AIO Sandbox](agent-infra-sandbox.md) [![⭐](https://img.shields.io/github/stars/agent-infra/sandbox?style=social)](https://github.com/agent-infra/sandbox) | All-in-one Docker sandbox — browser, shell, VS Code, Jupyter, MCP | Docker image, OpenAPI, Python/JS/Go SDKs, MCP HTTP | ✅ |
| [Agent Sandbox](agent-sandbox.md) | The trusted runtime for untrusted code | REST API, Python SDK, URL onboarding (`skill.md`) | ⚠️ |
| [Riza](riza.md) | AI writes code. Riza runs it. | REST API, Python/TypeScript/Go SDKs, MCP server, self-hosting | ✅ |
| [Agent Sandbox (Kubernetes SIG)](kubernetes-agent-sandbox.md) [![⭐](https://img.shields.io/github/stars/kubernetes-sigs/agent-sandbox?style=social)](https://github.com/kubernetes-sigs/agent-sandbox) | Secure isolated execution layer for autonomous agents on Kubernetes | Sandbox CRD, WarmPool/Claim, Python/Go SDKs, RuntimeClass | ⚠️ |
| [Clawk](clawk.md) [![⭐](https://img.shields.io/github/stars/clawkwork/clawk?style=social)](https://github.com/clawkwork/clawk) | Give a coding agent its own disposable Linux machine, not yours | Local hypervisor VM, DNS-aware egress allow-list, JSON CLI | ⚠️ |
| [Dormice](dormice.md) [![⭐](https://img.shields.io/github/stars/BitMiracle-AI/Dormice?style=social)](https://github.com/BitMiracle-AI/Dormice) | The SQLite of agent sandboxes — self-hosted, idle costs nothing | acquireSandbox, HTTP RPC, E2B SDK compat, dor CLI | ⚠️ |
| [CubeSandbox](cubesandbox.md) [![⭐](https://img.shields.io/github/stars/TencentCloud/CubeSandbox?style=social)](https://github.com/TencentCloud/CubeSandbox) | Instant, Concurrent, Secure & Lightweight Sandbox Service for AI Agents | E2B-compat REST, cubemastercli, CubeCoW, credential vault | ⚠️ |
| [forkd](forkd.md) [![⭐](https://img.shields.io/github/stars/deeplethe/forkd?style=social)](https://github.com/deeplethe/forkd) | A microVM sandbox runtime for AI agent fan-out. | Firecracker CoW fork, live BRANCH, REST/SDK, forkd-mcp | ✅ |
| [SmolVM](smolvm.md) [![⭐](https://img.shields.io/github/stars/CelestoAI/SmolVM?style=social)](https://github.com/CelestoAI/SmolVM) | SmolVM: secure microVM sandboxes for AI agents | Python SDK, smolvm CLI, browser sandbox, snapshots | ⚠️ |


---

## Criteria Reminder

To qualify for this category, a service must:

1. Provide **isolated execution environments** — not shared compute.
2. Support **agent-controlled sandbox lifecycle** — create, execute, destroy via API.
3. Return **structured, LLM-ready output** — not raw process output for a human terminal.
4. Support **stateful execution** — multiple code blocks in the same context.
5. Start **fast enough for interactive agent use** — under 1 second cold start.
