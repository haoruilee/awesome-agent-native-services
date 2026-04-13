# AIO Sandbox (agent-infra)

> **"AIO Sandbox is an all-in-one agent sandbox environment that combines Browser, Shell, File, MCP operations, and VSCode Server in a single Docker container."**

| | |
|---|---|
| **Website** | https://github.com/agent-infra/sandbox |
| **Docs** | http://localhost:8080/v1/docs (when container running) · https://github.com/agent-infra/sandbox |
| **GitHub** | https://github.com/agent-infra/sandbox |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/agent-infra/sandbox?style=social)](https://github.com/agent-infra/sandbox) |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |

---

## Official Website

https://github.com/agent-infra/sandbox (project hub; product site may redirect or challenge automated fetches)

---

## Official Repo

https://github.com/agent-infra/sandbox

---

## How to Use (Agent Onboarding)

**Docker (quick start)** — from [README](https://github.com/agent-infra/sandbox):

```bash
docker run --security-opt seccomp=unconfined --rm -it -p 8080:8080 ghcr.io/agent-infra/sandbox:latest
```

Then open:

- **API docs:** http://localhost:8080/v1/docs
- **VNC browser:** http://localhost:8080/vnc/index.html?autoconnect=true
- **VS Code Server:** http://localhost:8080/code-server/
- **MCP endpoint:** http://localhost:8080/mcp

**SDKs:**

```bash
pip install agent-sandbox
```

```bash
npm install @agent-infra/sandbox
```

See repo README for Go and full API usage.

---

## Agent Skills

**Status:** ⚠️ Not yet published as a dedicated `npx skills add …` pack

Search community skills: `npx clawhub@latest search agent-infra sandbox`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Built-in MCP HTTP endpoint in the container

| Detail | Value |
|---|---|
| **MCP URL** | `http://localhost:8080/mcp` (default port from README) |
| **Transport** | HTTP (when container running) |
| **Compatible Clients** | MCP hosts that can reach the sandbox network |

---

## What It Does

AIO Sandbox provides a **single isolated environment** where agents can use a **real browser (VNC)**, **shell**, **files**, **Jupyter**, **VS Code Server**, and **MCP** together with a **unified filesystem** — addressing coordination friction when separate single-purpose sandboxes cannot share artifacts. README markets it as **agent-ready** with **MCP-compatible APIs**.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: *"unified, secure execution environment for **AI agents** and developers"* and *"**Agent-Ready** — MCP-compatible APIs for seamless **AI agent** integration"* — [GitHub README](https://github.com/agent-infra/sandbox) |
| **Agent-specific primitive** | **All-in-one agent workspace** — browser + code + shell + MCP in one **cloud-native sandbox** with shared state; not merely "a VM" |
| **Autonomy-compatible control plane** | Agents drive sandbox via **API/SDK/MCP** once the container is up; no per-command human UI inside the guest for normal tool loops |
| **M2M integration surface** | Docker image, REST/OpenAPI docs on `:8080/v1/docs`, Python/JS/Go SDKs, MCP URL |
| **Identity / delegation** | Runs as **container-isolated** workload; caller auth is whatever the operator configures at the API/network edge; filesystem and process boundaries isolate agent effects from the host |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Unified sandbox** | Browser, terminal, files, VS Code Server, Jupyter in one VM |
| **Shared filesystem** | Artifacts from browser downloads immediately visible to shell/code tools |
| **MCP endpoint** | `http://<host>:8080/mcp` |
| **SDKs** | Python `agent-sandbox`, npm `@agent-infra/sandbox`, Go |
| **Secure execution** | Documented sandboxed Python/Node execution |

---

## Autonomy Model

```
Operator starts ghcr.io/agent-infra/sandbox container
  ↓
Agent uses SDK or MCP to run commands, browse, edit files
  ↓
State persists within the container lifecycle (see upstream for snapshot semantics)
  ↓
Outputs stream back to the agent host
```

---

## Identity and Delegation Model

- **Host boundary** — container isolates agent actions from the operator's host OS.
- **Network exposure** — default `localhost` binding; remote use requires explicit secure exposure.
- **No built-in "agent passport"** — identity is deployment-specific (API keys, network ACLs) per operator integration.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **REST/OpenAPI** | `/v1/docs` on port 8080 |
| **MCP** | `/mcp` on port 8080 |
| **VNC / VS Code / Jupyter** | Browser-accessible URLs in README |
| **SDKs** | PyPI, npm, Go module per repo |

---

## Human-in-the-Loop Support

Humans provision Docker (or orchestrator) and networking. Optional interactive debugging via VNC or VS Code in browser. Agent API loops can run unattended inside the guest subject to policy.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Separate browser + code sandbox** | No **single shared filesystem and session** across modalities |
| **Raw Docker + manual glue** | No **pre-wired MCP + VS Code + VNC + API** agent surface |
| **Cloud laptops only** | May not ship the same **open, self-hostable** all-in-one MCP contract |

---

## Use Cases

- **End-to-end agent evals** — browser task + code fix + tests in one environment
- **Research agents** — download papers/data in browser, analyze in Jupyter, commit via VS Code
- **CUA + coding** — combine computer-use style browsing with repository editing without re-uploading files between services
