# OpenChatCut

> **"Open-source, local-first conversational AI video editor with a professional multi-track timeline, Agent Skills, MCP integration, and Remotion rendering."**

| | |
|---|---|
| **Website** | https://openchatcut.com |
| **Docs** | https://github.com/0xsline/OpenChatCut#using-openchatcut-with-codex--claude-code |
| **GitHub** | https://github.com/0xsline/OpenChatCut |
| **Stars** | [2,000 stars (snapshot: 2026-09-26)](https://github.com/0xsline/OpenChatCut) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **Latest-month signal** | [v0.2.14](https://github.com/0xsline/OpenChatCut/releases/tag/v0.2.14) released 2026-09-04; 2,000 stars; root `LICENSE` is AGPL-3.0; [openchatcut.com](https://openchatcut.com) returned HTTP 200 on 2026-09-26 ([repo metadata](https://api.github.com/repos/0xsline/OpenChatCut)) |
| **Verified at** | 2026-09-26 |
| **Status** | Early, actively evolving local-first project; AGPL-3.0-or-later |

---

## Official Website

https://openchatcut.com

---

## Official Repo

https://github.com/0xsline/OpenChatCut

---

## How to Use (Agent Onboarding)

Start OpenChatCut, install its single routing skill, and ask the agent to configure the local MCP connection:

```bash
npx skills add 0xsline/OpenChatCut
```

```text
Set up OpenChatCut
```

The verified default MCP endpoint is:

```text
http://localhost:5199/api/external-mcp/mcp
```

Before timeline work, the agent calls `openchatcut_status`, selects a project, opens an edit session, loads the relevant specialized skill, and submits the resulting draft for review or automatic application.

---

## Agent Skills

**Status:** ✅ Available.

```bash
npx skills add 0xsline/OpenChatCut
```

| Skill | What It Teaches the Agent |
|---|---|
| [`openchatcut`](https://github.com/0xsline/OpenChatCut/blob/main/skills/openchatcut/SKILL.md) | MCP setup, project selection, edit-session discipline, progressive skill loading, error recovery, and completion verification |
| **26 in-editor specialized skills** | Timeline, transcript, captions, media, generation, motion graphics, audio, color, export, and other workflows loaded on demand through `load_skill` |

Custom `SKILL.md` files can also be installed under `~/.openchatcut/skills/<slug>/SKILL.md` and exposed to the agent by the running editor.

---

## MCP

**Status:** ✅ Available — first-party Streamable HTTP MCP.

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/0xsline/OpenChatCut |
| **Endpoint** | `http://localhost:5199/api/external-mcp/mcp` |
| **Transport** | Streamable HTTP |
| **Authentication** | Local bind by default; optional Bearer token through `OPENCHATCUT_MCP_TOKEN` when exposed |
| **Compatible Clients** | Codex app/CLI, Claude Code, and other Streamable HTTP MCP clients |

---

## What It Does

OpenChatCut turns a real, editable video project into an agent tool surface. Its built-in agent and external MCP clients operate the same `EditorCore` commands over multitrack timelines, media, transcripts, captions, audio, transitions, effects, motion graphics, and color rather than generating a one-off flattened result.

External agents work inside isolated draft edit sessions. They can inspect a project, propose precise operations, and submit an atomic set of changes that is either manually reviewed or applied in explicit `auto` mode as one undo step. Immediate, non-reversible side effects such as generation, export, and project deletion are intentionally unavailable through these draft sessions.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The official repository describes OpenChatCut as an [agent-native video editor](https://github.com/0xsline/OpenChatCut#what-is-openchatcut) where built-in and external MCP agents share tools. |
| **Agent-specific primitive** | `begin_edit_session`, isolated drafts, `load_skill`, proposal review, stale-session refusal, and atomic/undoable application let an agent modify a real creative project safely. |
| **Autonomy-compatible control plane** | `approvalMode: auto` applies a complete valid draft without human review; manual mode is available when oversight is desired. Unsupported immediate side effects remain outside the external session. |
| **M2M integration surface** | First-party Agent Skill plus Streamable HTTP MCP with project discovery, structured read/edit tools, session polling, and progressive skill/tool exposure. |
| **Identity / delegation** | Bearer authentication can protect a remotely exposed endpoint, and every edit is scoped to an `editSessionId`. The bridge is explicitly single-user/single-machine rather than multi-tenant; it does not claim independent per-agent accounts. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Edit session** | Isolated draft identified by `editSessionId`; all project reads and edits stay within it |
| **Project-aware tool set** | Structured access to real timelines, clips, tracks, transcripts, captions, media, and effects |
| **Progressive skill loading** | `load_skill` exposes workflow guidance and its referenced tools only when needed |
| **Proposal review** | `review_edit_session` submits the complete draft for manual review or auto application |
| **Atomic apply / undo** | Applies an approved draft as one undoable project change |
| **Stale-session guard** | Rejects stale automatic drafts instead of silently switching to manual approval |
| **Shared EditorCore** | UI, built-in agent, and MCP agents use the same validated command path and project format |

---

## Autonomy Model

1. OpenChatCut runs locally with a target project available; the MCP client connects to the verified endpoint.
2. The agent calls `openchatcut_status` and `list_projects`, then starts `begin_edit_session` with `manual` (default) or explicitly requested `auto` approval.
3. It calls `load_skill` for the editing domain, refreshes the MCP tool list when signaled, and reads/modifies only the session draft.
4. `review_edit_session` validates and submits the whole proposal.
5. Manual sessions wait for user approval in the editor; auto sessions apply immediately. The agent reports success only after `get_edit_session` returns `applied`.

---

## Identity and Delegation Model

- The MCP endpoint binds locally by default; an operator can require `Authorization: Bearer <token>` when exposing it.
- An `editSessionId` is the capability boundary for one draft and must accompany all draft-safe read/edit calls.
- Manual versus auto approval is explicit at session creation; auto mode must not be inferred from a stale or failed manual session.
- Local project profiles isolate development checkouts, including projects, media, credentials, settings, and authorization state.
- The current bridge targets one user on one machine, not multiple users or independent agent principals. Auditability comes from traceable `EditorCore` commands, proposal state, project versions, and undo—not a multi-tenant identity ledger.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **Agent Skill** | Installable router with MCP setup and safe editing workflow |
| **MCP** | Streamable HTTP endpoint for project discovery, skill loading, draft reads/edits, review, and status |
| **EditorCore commands** | Validated immutable timeline operations shared by UI and agents |
| **Local application** | Electron desktop builds and local web development server |
| **Project artifacts** | Editable project state, local media, version history, MP4/audio/captions/FCPXML export through the application |

---

## Human-in-the-Loop Support

Manual edit sessions are the default. An agent prepares an isolated draft, while the user previews, selects, approves, or rejects it inside the open project. `auto` mode is available only when unattended application is intentionally selected. In both modes, applied operations form one undo step; irreversible generation, export, and deletion tools are withheld from external draft sessions.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Traditional timeline editor** | Exposes a human GUI and scripting surface, not a sessioned agent workflow with skills, structured project reads, proposals, and MCP control. |
| **One-shot AI video generator** | Produces a flattened output rather than inspectable, reversible edits in a persistent multitrack project. |
| **Ad hoc editor scripting** | Creates a separate automation path that can drift from the UI's project semantics and lacks draft-level approval/atomic application. |

---

## Use Cases

- **Agent-assisted rough cut** — assemble clips, transitions, pacing, and soundtrack into a real editable timeline
- **Transcript-driven editing** — find and remove mistakes or pauses, then generate captions
- **Coding-agent video operations** — let Codex or Claude Code inspect and modify a local project through MCP
- **Review-gated creative automation** — prepare a complete draft while keeping final application with the editor user
- **Repeatable production workflows** — package specialized editing guidance as installable or local Agent Skills
