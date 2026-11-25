# Screenbox

> **"Real desktops for AI agents."**

| | |
|---|---|
| **Website** | https://screenbox.dev |
| **Docs** | https://github.com/dklymentiev/screenbox |
| **GitHub** | https://github.com/dklymentiev/screenbox |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | AGPL-3.0 (LICENSE file; GitHub SPDX was NOASSERTION on 2026-11-25) |
| **Latest-month signal** | Checked 2026-11-25: [homepage](https://screenbox.dev) HTTP 200; [repo](https://github.com/dklymentiev/screenbox) HTTP 200, 26 stars, pushed 2026-11-12T03:42:27Z; LICENSE file is GNU Affero General Public License. No public hosted MCP |
| **Verified at** | 2026-11-25 |

---

## Official Website

https://screenbox.dev

Homepage title: *"Screenbox - Virtual Desktops for AI Agents."* Meta description: *"Real virtual desktops for AI agents. MCP-native, Docker-isolated, self-hosted."* The README lead, which matches the line used here, is *"Real desktops for AI agents."*

---

## Official Repo

https://github.com/dklymentiev/screenbox

The LICENSE file is the GNU Affero General Public License, Copyright 2026 Dmytro Klymentiev: https://github.com/dklymentiev/screenbox/blob/main/LICENSE. GitHub's API reported `license.spdx_id` `NOASSERTION` on 2026-11-25. Trust the file: AGPL-3.0. About 26 stars, pushed 2026-11-12T03:42:27Z. Description: *"Real virtual desktops for AI agents. MCP-native, self-hosted, fully isolated."*

---

## How to Use (Agent Onboarding)

**Interaction pattern:** self-hosted Docker Compose and a local MCP URL. Not a one-URL join.

There is no public hosted MCP. The agent talks to a server on the operator's machine.

```bash
git clone https://github.com/dklymentiev/screenbox
cd screenbox
./setup.sh
docker compose up -d
# Dashboard: http://localhost:16000
# MCP: http://localhost:8080/mcp
```

`./setup.sh` generates `.env` and builds the desktop image and services (repo README). Add `http://localhost:8080/mcp` to the MCP client on that machine.

---

## Agent Skills

**Status:** ⚠️ Not yet published

No official `SKILL.md` or `npx skills add` package was found in the repo README reviewed on 2026-11-25.

Search community skills: `npx clawhub@latest search screenbox`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available — local Streamable HTTP after you start the stack

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/dklymentiev/screenbox |
| **Endpoint** | `http://localhost:8080/mcp` (no public vendor URL) |
| **Transport** | Streamable HTTP on the self-hosted API |
| **Auth** | The local deployment. Nothing is published at a Screenbox-hosted MCP host |
| **Docs** | https://github.com/dklymentiev/screenbox |
| **Compatible Clients** | Claude, Cursor, Copilot, and other MCP clients that can reach the local URL (README) |

---

## What It Does

Screenbox is a self-hosted desktop runtime for MCP agents. Each desktop is an isolated Docker container with Chromium. The agent sees, clicks, types, and navigates. Snapshots save and restore state. Files move through the API, not through a bind mount of the host (README: *"No bind mounts — files move only through explicit API calls."*). A person can watch or take over with RDP or VNC. Takeover is optional.

The homepage `llms.txt` is only a title and a contact line. The README is the setup document.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: *"Real desktops for AI agents."* Homepage: *"Real virtual desktops for AI agents. MCP-native, Docker-isolated, self-hosted."* Sources: https://github.com/dklymentiev/screenbox and https://screenbox.dev |
| **Agent-specific primitive** | An MCP-native desktop container: Chromium, snapshots, and explicit file transfer, with the agent's screen separate from the host. |
| **Autonomy-compatible control plane** | After `docker compose up`, the agent uses the MCP endpoint with no per-action click. RDP/VNC takeover is optional. |
| **M2M integration surface** | Local MCP at `http://localhost:8080/mcp`, the Docker Compose stack, and the dashboard at `http://localhost:16000`. |
| **Identity / delegation** | The operator who runs the compose stack. Each desktop is a container. There is no hosted account or delegated OAuth in the README's quick start. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Desktop container** | Isolated Docker desktop with Chromium. No host bind mounts. |
| **MCP endpoint** | `http://localhost:8080/mcp` once the stack is up. |
| **Snapshot** | Save and restore desktop state. |
| **RDP / VNC** | Optional live view and takeover. |

---

## Autonomy Model

1. The operator clones the repo, runs `./setup.sh`, and `docker compose up -d`.
2. The agent connects to `http://localhost:8080/mcp`.
3. The agent screenshots, clicks, and types in its container.
4. The agent snapshots when it needs to keep the desktop. A person opens RDP or VNC only if they want to watch or help.

---

## Identity and Delegation Model

- Self-hosted. The people who can reach port 8080 can drive desktops.
- Containers do not mount the host filesystem. Moving a file is an API call.
- There is no Screenbox-issued agent identity token in the quick start. Isolation is the container boundary.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP | `http://localhost:8080/mcp` |
| Dashboard | `http://localhost:16000` |
| Runtime | Docker Compose — https://github.com/dklymentiev/screenbox |
| Website | https://screenbox.dev |

---

## Human-in-the-Loop Support

Installing Docker and starting Compose is a human step. After that, the agent does not need a click per action. RDP and VNC are how a person watches or takes the desktop. The README presents them as optional.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **A browser container** | Chromium in Docker is not an MCP desktop lifecycle, snapshot API, or file-transfer boundary. |
| **Holm / E2B Desktop** | Other desktop control planes. Screenbox is this AGPL stack, with its own compose file and local MCP port. |
| **A hosted computer-use vendor** | Screenbox does not publish a public MCP host. The endpoint is on the machine that runs Compose. |

---

## Use Cases

- **A desktop on hardware the operator controls** — Docker on their server, MCP on localhost.
- **A browser the agent can see** — Chromium inside the container, not the host's Chrome profile.
- **A snapshot before a risky click** — save the desktop, act, restore if the run should be discarded.
