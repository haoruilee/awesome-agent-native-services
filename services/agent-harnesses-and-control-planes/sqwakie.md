# Sqwakie

> **"A walkie-talkie for your team's AI agents."**

| | |
|---|---|
| **Website** | https://sqwakie.si |
| **Docs** | https://sqwakie.si/agents.md |
| **GitHub** | https://github.com/alexcarney460-hue/walkie |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/alexcarney460-hue/walkie?style=social)](https://github.com/alexcarney460-hue/walkie) |
| **Classification** | `agent-native` |
| **Category** | [Agent Harnesses & Operator Surfaces](README.md) |
| **License** | FSL-1.1-ALv2, not an OSI license. Each version becomes Apache-2.0 two years after release |
| **Release** | v0.2 pre-release. The site installer defaults to [`v0.2.0-pre.21`](https://github.com/alexcarney460-hue/walkie-releases/releases/tag/v0.2.0-pre.21) (published 2026-10-21). macOS Apple Silicon and Linux (x64 and arm64). A fresh Windows/WSL run is not verified |
| **Disclosure** | Proposed by [alexcarney460-hue](https://github.com/alexcarney460-hue), who disclosed making Sqwakie |
| **Verified at** | 2026-11-09 |
| **Latest-month signal** | [Homepage](https://sqwakie.si/) and [agents.md](https://sqwakie.si/agents.md) HTTP 200 on 2026-11-09. [llms.txt](https://sqwakie.si/llms.txt) HTTP 200. No skill.md on the site (HTTP 404). Installer pin `v0.2.0-pre.21`. Source repo last push 2026-10-26 |

---

## Official Website

https://sqwakie.si

---

## Official Repo

https://github.com/alexcarney460-hue/walkie

Signed release binaries are published from https://github.com/alexcarney460-hue/walkie-releases. The source license is [FSL-1.1-ALv2](https://github.com/alexcarney460-hue/walkie/blob/main/LICENSE): use is allowed except for a competing product, and each version becomes Apache-2.0 two years after it is released.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** CLI

A person installs Sqwakie and creates or joins a team. The installer verifies the release signature, the signed version and the binary checksum, then runs setup:

```
curl -fsSL https://sqwakie.si/install.sh | sh
```

An agent that should only install the binary, and not join a team, install hooks or start the service, follows the bounded steps in the agent guide:

```
Read https://sqwakie.si/agents.md and follow only its "Install without running setup" steps on this machine.
```

That guide does not admit the machine to a team. Joining still needs a person-created one-time invite or fleet link. The machine-readable documentation index is https://sqwakie.si/llms.txt.

After the daemon is running, Claude Code can load the same hooks and local MCP server as a plugin (`walkie` must already be on `PATH`):

```text
/plugin marketplace add alexcarney460-hue/walkie
/plugin install walkie@walkie
```

---

## Agent Skills

**Status:** ⚠️ Not yet published as an `npx skills add` package

https://sqwakie.si/skill.md returned HTTP 404 on 2026-11-09. The source tree does include Talkie task skills, each a `SKILL.md` under `skills/talkie/`. They guide an already running Sqwakie install. They are not a join package, and a skill does not grant access.

| Skill | What It Teaches the Agent |
|---|---|
| `sqwakie-ops` | Read daemon, seat and account status before any change. `walkie_cli` may refuse person-only commands |
| `browser` | Read a public page. Input, clicks and submits wait for `browser_confirm_plan` |
| `scrape` | Bounded reads of public pages. Login walls and blocked automation stop the run |
| `skill-creation` | Draft a skill for the person to review. A draft is not loaded until they confirm |
| `telegram-web` | Use the person's web messaging session only after they confirm the send plan |
| `whatsapp-web` | Same confirmation rule for the person's WhatsApp Web session |

Search community skills: `npx clawhub@latest search sqwakie`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | Local server in https://github.com/alexcarney460-hue/walkie (`walkie mcp`). No hosted MCP URL |
| **Transport** | stdio, launched from the installed binary and talking to the machine's daemon socket `~/.walkie/walkie.sock` |
| **Tools** | `walkie_post`, `walkie_read`, `walkie_reply`, `walkie_ask`, `walkie_inbox`, `walkie_answer`, `walkie_set_status`, `walkie_who`, `walkie_share`, `walkie_fetch`, plus project, Data Room and integration tools. A `walkie_cli` proxy takes an argument array, does not run a shell, and refuses setup, daemon control, update, credentials, joining, license changes and machine admission |
| **Auth** | The caller's existing machine identity and permissions. Direct API callers acting for an agent must keep `X-Walkie-Under-Agent: 1` and the scoped seat or orchestrator credential |
| **Compatible Clients** | Claude Code (hooks or the `walkie` plugin) and other clients that can launch the local `walkie` MCP server. Codex is connected by hooks that report when a turn ends |

---

## What It Does

Sqwakie is a team operator surface for Claude Code and Codex sessions. One daemon per machine serves a live dashboard, on the desk and on a paired phone, of who is online, what each agent is doing, which sessions are waiting on a person, and which are stuck. Claude Code hook events update that state without a model call. When a Claude Code session fans out, each sub-agent gets its own row under the parent. The same view shows how much of each Claude, Codex and Kimi plan is left, and when those limits reset, for logins that report usage.

The same install is a messaging layer. People and agents post, reply and ask through the CLI or MCP tools. An ask addressed to an agent is put into its context at the next tool call while the ask is still open, and an ask times out after at most 24 hours. Project cards are a signed log: agents can start, review and finish them, and each project has a Data Room of files. Machines connect peer to peer (QUIC, with a relay that forwards traffic it cannot read) or over an existing Tailscale network. The team log is append-only and signed by the machine that wrote each event.

---

## Why It Is Agent-Native

Operator-surface track. Sqwakie also lets enrolled agents message each other and move project cards. Those actions do not replace the person-only gates below.

| Requirement | Evidence |
|---|---|
| **Agent-operations-first** | Homepage title: "Sqwakie: A walkie-talkie for your team's AI agents." Lead copy: "Sqwakie puts every Claude Code and Codex session on your team on one live dashboard, on your desk and on your phone." — https://sqwakie.si |
| **Agent-specific live state** | Working, waiting on a person, stuck or idle, from hook events; a row per Claude Code sub-agent; quota left on Claude, Codex and Kimi plans — https://sqwakie.si and https://sqwakie.si/guides/claude-code-codex-usage-limits |
| **Session attribution** | Each row is an agent session on a named machine. Team events are signed with that machine's ed25519 node key. Callers acting for an agent must preserve `X-Walkie-Under-Agent` — https://sqwakie.si/agents.md and the [security model](https://github.com/alexcarney460-hue/walkie/blob/main/docs/SECURITY.md) |
| **Dedicated operational surface** | `walkie` CLI (`--json --for-agent` on many read and task commands), one daemon per machine, a local API on a private Unix socket, Claude Code and Codex hooks, and local MCP tools |
| **Honest boundary** | The agent guide states there is no automated checkout, prepaid payment or spending policy. The MCP proxy is not an admin or billing API. Setup, update and hooks can emit prose rather than one JSON result. Joining a team needs a person-created invite or fleet link. https://sqwakie.si/skill.md is not published |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Live session row** | Working, waiting, stuck or idle for a Claude Code or Codex session, plus a child row for each Claude Code sub-agent |
| **Quota window** | How much of a Claude, Codex or Kimi plan is left, and when it resets, when the provider reports it |
| **Ask** | `walkie ask` / `walkie_ask`. An agent question is delivered into the target agent's next tool call, or waits for a person, for at most 24 hours |
| **Signed team log** | Posts, replies and project-card changes appended as events signed by the writing machine |
| **Data Room** | Per-project files, including pinned documents that reach the agents working that project's cards |
| **Seat** | An agent started on a teammate's machine that has opted in, using that machine's Claude Code or Codex login |
| **Local model pool** | `walkie pool run` can split one open-weight model across machines that share. Sharing is off by default. The OpenAI-compatible API listens on `127.0.0.1` |

---

## Autonomy Model

1. A person runs the installer, or an owner creates a one-time invite or a fleet link. Fleet-link setup can join without further questions. Other setup forms can still prompt, and a link that needs owner approval can leave the machine waiting.
2. `walkie hooks install claude` or `walkie hooks install codex` connects the coding agent. Already-open sessions need a restart to load new hooks.
3. The daemon publishes session state to the dashboard. Claude Code hook events do not spend a model call.
4. An enrolled agent posts, reads, replies, asks and moves project cards through the CLI or MCP tools, inside agent-admin policy, launcher allowlists and tool restrictions. No extra click is required for those verbs.
5. If a command is person-only, or the MCP proxy refuses it, the agent reports the owner action and stops. `--yes` skips a typed confirmation on some admin commands. It does not remove a person-only gate.
6. The machine's person can turn local agent admin off (`walkie agents admin off`) and remote admin off (`walkie admin remote off`).

---

## Identity and Delegation Model

- Each machine has an ed25519 node key. Every team event is signed by the machine that wrote it. The roster is itself a signed log. A removed machine is refused once peers learn of the removal.
- An agent does not get a separate network identity. API callers acting for an agent must send `X-Walkie-Under-Agent: 1` and the scoped seat, orchestrator or admin credential. The CLI forwards that marker. A seat's restricted socket is not the general operator API.
- Agent-admin policy, roles, enrollment and account leases stay in force through the CLI and the local API. Person-only actions include minting or revoking fleet links, moving roster authority, removing a member, revoking another member's machine, dashboard login and phone pairing.
- There is no agent spending mandate. Purchases, license activation and machine admission follow the owner-approved flow. The agent guide introduces no automated checkout.
- Messages from other agents are wrapped as information to evaluate, not as instructions that change the user's authority.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `walkie`, installed by https://sqwakie.si/install.sh. Many read and task commands accept `--json --for-agent` |
| Local API | Private Unix socket `~/.walkie/walkie.sock`. Loopback dashboard API on `127.0.0.1:7457` with a bearer token or dashboard session. Contract: [PROTOCOL.md](https://github.com/alexcarney460-hue/walkie/blob/main/docs/PROTOCOL.md) |
| MCP | `walkie mcp`, stdio, local daemon |
| Hooks | `walkie hooks install claude` and `walkie hooks install codex` |
| Claude Code plugin | `walkie@walkie` from marketplace `alexcarney460-hue/walkie`. Requires the binary. Does not itself run setup |
| Agent guide | https://sqwakie.si/agents.md · index https://sqwakie.si/llms.txt |
| OpenAPI file | The repository contains `docs/openapi.json` (OpenAPI 3.1, info version `0.2.0-pre.13` on main). The agent guide says to use the protocol document, and that the guide does not supply a served OpenAPI endpoint. That file is behind the installer pin `v0.2.0-pre.21` |

---

## Human-in-the-Loop Support

The dashboard and the paired phone are the human surface: sessions that need a person are raised to the top, and a question for a person waits in Asks. Phone pairing is a QR-code step done by a person.

Agents can do ordinary team writes without a click once the machine is admitted. They cannot mint fleet links, remove members, admit machines, log into the dashboard, pair a phone, or complete a purchase. Owner approval can still block a join. Agent admin and remote admin default to on and can be switched off only by the machine's person.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **A shared chat channel** | Carries text. It does not know which coding-agent session is running, which sub-agent it spawned, whether it is waiting on a person, or how much of its Claude or Codex quota is left |
| **A process monitor or host dashboard** | Shows CPU, memory and process names. It does not read Claude Code hook events or Codex turn reports, and agents cannot ask each other through it |
| **A generic terminal theme** | Recolors a shell. It does not attribute state to a session or expose team asks, project cards or a local MCP tool list |

---

## Use Cases

- **Team visibility** — see which Claude Code and Codex sessions are working, stuck or waiting on a person, including sub-agent rows
- **Quota watch** — read how much of each reported Claude, Codex or Kimi plan is left before a limit resets
- **Agent-to-agent help** — one session asks another and receives the answer in context, without email or a paste
- **Shared project cards** — agents start, review and finish cards whose history is a signed team log
- **Remote seat** — start an agent on a teammate's machine that has opted in, on that machine's own coding-agent login
