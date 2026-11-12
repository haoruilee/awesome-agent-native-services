# Limrun

> **"Unlock cloud agents for mobile dev teams"**

| | |
|---|---|
| **Website** | https://limrun.com |
| **Docs** | https://docs.limrun.com/docs |
| **GitHub** | https://github.com/limrun-inc (SDKs and skills; Apache-2.0 TypeScript/Python/Java SDKs) |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **Verified at** | 2026-11-12 |

---

## Official Website

https://limrun.com

Homepage (`https://limrun.com/index.md`): *Limrun: Unlock cloud agents for mobile dev teams.* Meta description: *"Realtime remote Xcode and cloud simulators for AI agents."* `llms.txt`: Limrun runs cloud iOS simulators, Android emulators, remote Xcode builds, and build sandboxes "so AI agents and developers can build, run, test, and preview mobile apps from anywhere, including Linux CI machines and cloud sandboxes without local device tooling."

Backed by Y Combinator (homepage). Not a physical-device farm — simulators and emulators only.

---

## Official Repo

Public repos live under https://github.com/limrun-inc, including [typescript-sdk](https://github.com/limrun-inc/typescript-sdk) (Apache-2.0), [python-sdk](https://github.com/limrun-inc/python-sdk) (Apache-2.0), and the skills install target `limrun-inc/skills` documented in the MCP guide. The hosted product itself is reached through the CLI, API, and MCP, not a single application monorepo.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** remote MCP (OAuth or API key) + `lim` CLI + published skills.

This is not a one-URL join path. An operator (or OAuth browser flow) must have a Limrun account. Keys are created in the console under Settings → API Keys (https://console.limrun.com).

**Remote MCP**, from https://docs.limrun.com/docs/agents/remote-mcp.md:

```bash
claude mcp add --transport http limrun https://mcp.limrun.com/mcp
```

Then `/mcp` → **limrun** → **Authenticate**. Headless clients send `Authorization: Bearer <LIM_API_KEY>` to the same URL. The server is listed in the official MCP registry as `com.limrun/mcp`.

**CLI:**

```bash
npm install -g lim
# or: brew install limrun-inc/tap/lim
```

**Skills** (builds and local files, which the MCP server does not accept as raw bytes):

```bash
lim skills install
# or, before the CLI is installed:
npx skills add limrun-inc/skills
```

The MCP tool `get-agent-skill` also serves `limrun-xcode`, `limrun-gradle`, `limrun-xcode-bazel`, and `limrun-expo-development`. Discovery indexes: https://limrun.com/.well-known/mcp/server-card.json and https://limrun.com/.well-known/agent-skills/index.json. Auth guide: https://limrun.com/auth.md. OpenAPI: https://limrun.com/openapi.json.

Every instance also has a [per-instance MCP server](https://docs.limrun.com/docs/agents/mcp) at `status.mcpUrl`, authenticated with that instance's `status.token` — for handing one device to an agent that holds no organization credential.

---

## Agent Skills

**Status:** ✅ Available

```bash
npx skills add limrun-inc/skills
# or: lim skills install
```

| Skill | What It Teaches the Agent |
|---|---|
| `limrun-xcode` | Remote Xcode builds via the `lim` CLI |
| `limrun-gradle` | Cloud Gradle sandbox builds |
| `limrun-xcode-bazel` | Bazel iOS path |
| `limrun-expo-development` | Expo development flow |

---

## MCP

**Status:** ✅ Available (hosted remote + per-instance)

| Detail | Value |
|---|---|
| **Endpoint** | `https://mcp.limrun.com/mcp` (organization-level; unauthenticated requests return 401, verified 2026-11-12) |
| **Transport** | Streamable HTTP |
| **Auth** | OAuth (default) or `Authorization: Bearer <LIM_API_KEY>` |
| **Server card** | https://limrun.com/.well-known/mcp/server-card.json |
| **Tools** | 16 tools: create/list/delete iOS simulators and Android emulators, screenshot + element tree, batched `ios-use` / `android-use`, live `stream-device`, `get-agent-skill`, and related lifecycle/asset tools |
| **Compatible Clients** | Claude Code and any Streamable HTTP MCP client |
| **Docs** | https://docs.limrun.com/docs/agents/remote-mcp |

Instances created through this server carry a `created-by: mcp` label. The remote MCP cannot reach billing or upload local build bytes — those stay on the CLI and SDKs. OAuth tokens appear in the console as MCP OAuth tokens and can be revoked.

---

## What It Does

Limrun gives a cloud or CI agent a remote Xcode Mac, an iOS simulator, and an Android emulator it can drive from Linux, Windows, or a sandbox that has no local device tooling. The agent creates an instance over MCP, reads the accessibility tree and screenshots, taps and types, records video, and deletes the instance when done. Remote Xcode and Gradle builds, PR preview links, and demo videos sit beside that control plane.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"Unlock cloud agents for mobile dev teams"* and *"so your cloud agent can build, validate and share its work."* Dedicated "For AI agents" section and MCP/skills indexes. Sources: https://limrun.com/index.md, https://limrun.com/llms.txt |
| **Agent-specific primitive** | Organization MCP that provisions a simulator/emulator, returns an `instanceId`, and exposes screenshot + accessibility-tree tools; plus a per-instance MCP whose token dies with that instance. Instances created over MCP are labeled `created-by: mcp`. |
| **Autonomy-compatible control plane** | After one OAuth or API-key sign-in, the client creates, drives, and deletes devices by itself. Tools that touch a device take an explicit `instanceId` (stateless). Optional `idempotencyKey` on create. `inactivityTimeout` is documented. |
| **M2M integration surface** | Remote and per-instance MCP; OpenAPI; RFC 9727 API catalog; CLI; TypeScript/Python/Go SDKs; Agent Skills; `llms.txt`; MCP server card. |
| **Identity / delegation** | Organization OAuth or API key for the remote server (scoped to instances, not billing). Per-instance `status.token` limits blast radius to one device. Docs also describe [Workload Identity](https://docs.limrun.com/docs/platform/workload-identity.md) so workloads can get permissions without copying an API key. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Cloud iOS simulator / Android emulator** | Create, drive (a11y tree, screenshot, batched actions), stream, delete. |
| **Remote Xcode / Gradle** | Build on a cloud Mac or Android sandbox from a machine that has no local toolchain. |
| **Per-instance MCP** | Hand one already-created instance to an agent with only that instance's token. |
| **Preview and recording** | Live preview links and demo videos the agent can request for a PR. |

---

## Autonomy Model

1. Operator signs in once (OAuth in the client, or an API key in a header).
2. Agent calls `create-ios-simulator` or `create-android-emulator` (optional `apps`, `idempotencyKey`, `tunnel`).
3. Agent drives the instance with screenshot + element-tree tools and batched `ios-use` / `android-use`.
4. For builds, the agent fetches a skill and uses the `lim` CLI (MCP has no filesystem access for local APKs/projects).
5. Agent calls `delete-instance` (the only destructive tool) when done.

---

## Identity and Delegation Model

- Remote MCP: organization OAuth or API key; cannot reach billing.
- Per-instance MCP: `status.token`, invalid once the instance is gone — for agents that must not hold an org credential ([sandboxed agents guide](https://docs.limrun.com/docs/agents/sandboxed-agents.md)).
- `created-by: mcp` label on MCP-created instances.
- Workload Identity is documented for keyless permissions inside Limrun workloads.
- OAuth access tokens are listed and revocable in the console; refresh continues until the client is removed.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Remote MCP | `https://mcp.limrun.com/mcp` |
| Per-instance MCP | `status.mcpUrl` + `status.token` |
| CLI | `npm install -g lim` / `brew install limrun-inc/tap/lim` |
| REST / SDKs | https://api.limrun.com — OpenAPI at https://limrun.com/openapi.json; TS/Python/Go SDKs |
| Skills | `npx skills add limrun-inc/skills` or `lim skills install` |

---

## Human-in-the-Loop Support

OAuth opens a browser for the operator once. `stream-device` can show the live interactive screen inline. PR preview links are for human reviewers. The create-drive-delete loop does not need a per-action click.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Local Xcode / Android Studio** | Human IDE toolchains, not a cloud agent MCP. |
| **Physical device farms** | Limrun itself says it is not a fit for physical-device-only testing; those farms are QA suites, not this agent provision/drive/delete surface. |

---

## Use Cases

- **Claude Code on the web / cloud sandboxes** — build and run an iOS app with no local Mac.
- **Agent-driven QA on simulators** — create a device, walk a flow, record video, delete.
- **Sandboxed agents** — lifecycle stays outside; the inner agent only gets a per-instance MCP token.
