# E2B

> **"Cloud for AI agents — secure sandboxes for AI-generated code."**

| | |
|---|---|
| **Website** | https://e2b.dev |
| **Docs** | https://e2b.dev/docs |
| **GitHub** | https://github.com/e2b-dev/e2b |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |
| **GitHub Org Description** | "Cloud for AI Agents" |

---

## Official Website

https://e2b.dev

---

## Official Repo

https://github.com/e2b-dev/e2b — Core sandbox SDK

https://github.com/e2b-dev/mcp-server — Official MCP server

https://github.com/e2b-dev/code-interpreter — Code interpreter SDK

---

## Skills

| Skill | Description |
|---|---|
| **Create Sandbox** | Spin up an isolated Linux VM in ~150ms via API |
| **Run Code** | Execute Python, JavaScript, shell commands, or any language in the sandbox |
| **Stateful Execution** | Persist variables and state across multiple code blocks in the same session |
| **Stream Output** | Receive stdout, stderr, charts (matplotlib, plotly), and file output in real time |
| **Upload / Download Files** | Transfer files to and from the sandbox programmatically |
| **Run MCP Server in Sandbox** | Host any MCP server inside a sandbox for safe, isolated tool execution |
| **200+ Pre-built MCP Tools** | Access the Docker MCP Catalog from within E2B sandboxes |
| **Destroy Sandbox** | Terminate and clean up a sandbox session via API |

---

## MCP

**Status:** ✅ Available — and uniquely, E2B *runs MCP servers inside sandboxes*

E2B has a dual MCP relationship:
1. **E2B as MCP tool** — An official MCP server (`e2b-dev/mcp-server`) that exposes code interpreter capabilities to LLMs via MCP.
2. **E2B as MCP host** — E2B sandboxes can run any MCP server (200+ from the Docker MCP Catalog) inside isolated VMs, providing a safe execution environment for MCP tools.

| Detail | Value |
|---|---|
| **MCP Docs** | https://e2b.dev/docs/mcp |
| **MCP Server Repo** | https://github.com/e2b-dev/mcp-server |
| **MCP in Sandbox Docs** | https://e2b.dev/docs/mcp/quickstart |
| **Transport** | stdio (as MCP server) / HTTP (MCP gateway inside sandbox) |
| **Compatible Clients** | Claude Desktop, OpenAI Agents SDK, any MCP-compatible client |

---

## What It Does

E2B provides secure, isolated Linux cloud sandboxes that AI agents can spin up in ~150ms to execute generated code. Each agent session gets its own sandbox with a full Linux filesystem, internet connectivity, and stateful execution contexts. Agents can run Python, JavaScript, shell commands, and more — with stdout, stderr, charts, and files streamed back in real time.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | E2B's GitHub organization is literally named *"Cloud for AI Agents"*; the product is designed around the use case of running AI-generated code |
| **Agent-specific primitive** | Per-session ephemeral sandbox; stateful execution context; streaming output for agent consumption; file upload/download for agent workflows |
| **Autonomy-compatible control plane** | Agents spin up, use, and destroy sandboxes via API; no human provisions or manages compute |
| **M2M integration surface** | Python SDK, TypeScript SDK, REST API; compatible with LangChain, AutoGen, CrewAI, and any agent framework |
| **Identity / delegation** | Per-session sandbox isolation; API key scoped per integration |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Ephemeral Sandbox** | Isolated Linux VM created and destroyed per agent session |
| **~150ms Cold Start** | Sandboxes ready almost instantly — fast enough for interactive agent loops |
| **Stateful Execution Context** | Variables, imports, and filesystem persist across multiple code blocks in the same session |
| **Streaming Output** | stdout, stderr, charts (matplotlib, plotly), and file output streamed back in real time |
| **File Operations** | Agents can upload input files and download output files |
| **Multi-Language** | Python, JavaScript/TypeScript, shell commands, and more |

---

## Autonomy Model

```
Agent generates code (from LLM output)
    ↓
Agent calls sandbox.run_code(code)  // or creates sandbox first
    ↓
E2B executes in isolated Linux VM
    ↓
Streams back: stdout, stderr, charts, error traces
    ↓
Agent reads output, decides next step
    ↓
Agent destroys sandbox when task is complete
```

The agent is the only entity that touches the sandbox. No human sets up or monitors the execution environment.

---

## Identity and Delegation Model

- Per-session sandbox isolation — each agent session gets a clean environment
- API key authentication scoped per integration
- Sandbox IDs enable per-session attribution in logs
- No shared state between agent sessions

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `from e2b_code_interpreter import Sandbox` |
| TypeScript SDK | `import { Sandbox } from "@e2b/code-interpreter"` |
| REST API | Sandbox lifecycle management and code execution |
| LangChain | Native tool integration |
| AutoGen | Compatible with AutoGen's code execution model |
| CrewAI | Compatible with CrewAI tool definitions |

---

## Human-in-the-Loop Support

None required. Agents manage the full sandbox lifecycle. Output can be reviewed by humans post-hoc, but no human intervention is needed during execution.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **AWS Lambda** | Stateless functions; no interactive REPL, no persistent execution context across calls |
| **Docker (self-hosted)** | Developer manages container lifecycle; no 150ms cold start; requires infrastructure management |
| **subprocess (local)** | Runs on the host machine — dangerous for AI-generated code; no isolation |
| **Replit** | IDE designed for human developers; not an agent-controlled execution API |
| **Google Colab** | Human-facing Jupyter notebook environment; not designed for programmatic agent control |

---

## Notable Users

- Maissa
- Athena Intelligence
- Flint
- Cognosys

---

## Use Cases

- **Data analysis agents** — agent generates and executes Python data analysis code, reads charts and results
- **Coding agents** — agent generates code, tests it in a sandbox, iterates based on test output
- **Research agents** — agent runs statistical analyses or simulations to verify hypotheses
- **Math agents** — agent executes symbolic computation and numerical verification
- **File processing agents** — agent processes CSV, JSON, images in a sandboxed environment
- **Agent playgrounds** — multi-agent systems where each agent gets its own isolated execution context
