# MCP Gateway & Registry

> **"Unified Agent & MCP Server Registry – Gateway for AI Development Tools"**

| | |
|---|---|
| **Website** | https://agentic-community.github.io/mcp-gateway-registry/ |
| **Docs** | https://agentic-community.github.io/mcp-gateway-registry/ |
| **GitHub** | https://github.com/agentic-community/mcp-gateway-registry |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/agentic-community/mcp-gateway-registry?style=social)](https://github.com/agentic-community/mcp-gateway-registry) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Last GitHub push 2026-08-25 ([repo metadata](https://api.github.com/repos/agentic-community/mcp-gateway-registry)) |
| **Verified at** | 2026-10-13 |

---

## Official Website

https://agentic-community.github.io/mcp-gateway-registry/

---

## Official Repo

https://github.com/agentic-community/mcp-gateway-registry

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + MCP gateway

Name this row **MCP Gateway & Registry** so it does not collide with hosted [MCP Gateway](mcpgateway.md).

```bash
git clone https://github.com/agentic-community/mcp-gateway-registry.git
cd mcp-gateway-registry
cp .env.example .env
# Set required secrets (KEYCLOAK_ADMIN_PASSWORD, SECRET_KEY, …) — see docs/configuration.md
./build_and_run.sh --prebuilt
```

The registry UI is served by nginx on port 80 (`http://localhost`). Full walkthrough: [Complete Installation Guide](https://github.com/agentic-community/mcp-gateway-registry/blob/main/docs/installation.md). EKS Helm, ECS Terraform, and a macOS setup skill are documented for other targets.

---

## Agent Skills

**Status:** ✅ Available as in-repo skills (not `npx skills add`).

| Skill | What It Teaches the Agent |
|---|---|
| macOS setup | End-to-end local install on a MacBook (`.claude/skills/macos-setup/SKILL.md`) |
| Terraform setup | ECS/Terraform deploy assistance (`.claude/skills/terraform-setup/SKILL.md`) |

---

## MCP

**Status:** ✅ Available — agents and coding assistants connect through the gateway as MCP clients.

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/agentic-community/mcp-gateway-registry |
| **Transport** | HTTPS through nginx; MCP / OAuth to the gateway |
| **Compatible Clients** | Coding assistants and autonomous agents that speak MCP |
| **Also registers** | A2A agents, `SKILL.md` skills, admin-defined custom entities |

---

## What It Does

The **MCP Gateway & Registry** (agentic-community) is an open-source control plane for organizational AI assets: MCP servers, A2A agents, skills, and custom entity types. Official docs: it began as one secure entry to many MCP servers and grew into a general AI asset registry on the same access-control and audit model.

The **gateway** is the data plane (nginx: TLS, auth validation, routing). The **registry** is the control plane (FastAPI: inventory, access model, audit, embeddings). An auth server talks to Keycloak, Entra ID, Okta, Auth0, Cognito, or PingFederate. By default, A2A discovery and ACL happen in the registry and agents then talk peer-to-peer; reverse-proxy mode can force A2A through the gateway.

**Distinctness:** hosted [MCP Gateway](mcpgateway.md) is a commercial one-URL tools/skills/sandboxes platform (`mcpgateway-sdk`). [ToolHive](toolhive.md) runs MCP servers in secure containers. [ContextForge](contextforge.md) federates MCP+A2A+REST/gRPC with UAID routing. This project is the agentic-community **enterprise registry** (IdP, virtual MCP servers, 3LO egress auth, admission scanning, external-registry federation).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Docs: **"Unified Agent & MCP Server Registry – Gateway for AI Development Tools"** and **"one governed entry point for every AI asset"** — [docs](https://agentic-community.github.io/mcp-gateway-registry/), [README](https://github.com/agentic-community/mcp-gateway-registry) |
| **Agent-specific primitive** | Natural-language tool discovery; virtual MCP servers; A2A agent registry; `SKILL.md` skill registry with scan-on-register; per-user egress OAuth (3LO/OBO/PAT) |
| **Autonomy-compatible control plane** | After registration and token mint, agents call tools through one authenticated gateway. Rate limits and quarantine are admin APIs, not per-call humans |
| **M2M integration surface** | MCP, REST/OpenAPI, Python `registry_client.py`, `registry_management.py` CLI, Helm/Terraform/Compose |
| **Identity / delegation** | OAuth2/OIDC against the org IdP; fine-grained scopes; M2M service accounts; vaulted per-user egress tokens; attributable audit log with credential masking |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Asset registry** | MCP servers, A2A agents, skills, custom entity types |
| **Authenticated gateway** | Single ingress; nginx + auth-server `/validate` |
| **Semantic + lexical search** | Runtime tool/agent discovery by natural language |
| **Virtual MCP server** | Aggregate tools from many backends with per-tool ACL |
| **Egress auth** | 3LO / OBO / PAT so SaaS tokens are not stored in agent dotfiles |
| **Admission gate** | Scan-on-register; fail-closed hold for unsafe assets |
| **Federation** | Pull Anthropic MCP Registry, AWS Agent Registry, peer registries |
| **Quarantine / rate limits** | Identity- and target-aware caps; admin kill switch |

---

## Autonomy Model

```
Operator deploys Compose/Helm/Terraform and connects an IdP
    -> Register servers, agents, and skills (scan + scopes)
    -> Agent or coding assistant obtains an MCP token (TTL configurable)
    -> Calls go through the gateway; A2A may be peer-to-peer or proxied
    -> Audit log records access; quarantine can drop a caller or target
```

---

## Identity and Delegation Model

- **Human users and M2M agents** both exist as first-class callers with groups and scopes.
- **Egress:** gateway runs OAuth for Slack/Atlassian/GitHub-style MCP servers and injects vaulted tokens — the agent never holds the long-lived SaaS secret on disk.
- **Audit:** access and admin events are attributable, with credential masking.
- **Quarantine:** admin-only; cannot quarantine admin-group users (server-side, fail-closed).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP / HTTPS | nginx data plane |
| REST / OpenAPI | Registry API (`api/openapi.json`) |
| CLI | `registry_management.py`; `./build_and_run.sh --prebuilt` |
| Deploy | Docker Compose, Helm (EKS), Terraform (ECS) |
| A2A | Discovery + optional reverse-proxy mode |

---

## Human-in-the-Loop Support

Admin UI for inventory, scopes, rate limits, and quarantine. Data-plane tool calls do not require a human click. First-time 3LO for a SaaS MCP server needs a user to complete OAuth once.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **MCP Gateway (mcpgateway.com)** | Different product (hosted SDK + one URL). Do not merge the rows |
| **ToolHive** | Secure MCP *runtime*. Not an org-wide IdP registry with 3LO egress and A2A assets |
| **ContextForge** | Protocol federation + UAID. Not this Keycloak/Entra registry with virtual MCP + skill scanning |
| **A generic API gateway** | No MCP tool search, skill admission, or agent-to-agent registry |

---

## Use Cases

- **Enterprise MCP on-ramp** — one OAuth gateway instead of credentials in every agent config
- **Runtime tool discovery** — agents search the registry instead of hard-coding server lists
- **Governed A2A** — register agents, then peer-to-peer or proxied invoke
- **Skill catalog with scanning** — versioned `SKILL.md` assets on the same ACL as servers
