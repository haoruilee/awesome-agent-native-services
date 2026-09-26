# Qwen Audio Agent

> **"A realtime voice runtime that keeps Agents talking, working, and present."**

| | |
|---|---|
| **Website** | https://github.com/QwenAudio/qwen-audio-agent |
| **Docs** | https://github.com/QwenAudio/qwen-audio-agent/tree/main/docs |
| **GitHub** | https://github.com/QwenAudio/qwen-audio-agent |
| **Classification** | `agent-native` |
| **Category** | [Voice & Phone Services](README.md) |
| **License** | Apache 2.0 |
| **Latest-month signal** | [v2.0.0](https://github.com/QwenAudio/qwen-audio-agent/releases/tag/v2.0.0) released 2026-09-23; 2,764 stars; license Apache-2.0; last push 2026-09-23; docs site [qwenaudio.github.io/qwen-audio-agent](https://qwenaudio.github.io/qwen-audio-agent/) returned HTTP 200 ([repo metadata](https://api.github.com/repos/QwenAudio/qwen-audio-agent)) |
| **Verified at** | 2026-09-26 |

---

## Official Website

https://github.com/QwenAudio/qwen-audio-agent

---

## Official Repo

https://github.com/QwenAudio/qwen-audio-agent

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `Daemon / CLI`

```bash
npm install -g qwen-audio-agent
qwenaudio config                 # add realtime voice credentials and optional backend
qwenaudio                        # start the local Gateway
qwenaudio tui                    # in another terminal; or: qwenaudio webui
```

Choose an installed backend with `AGENT_PROTOCOL`, or inspect/install one with `qwenaudio setup` and `qwenaudio install <backend>`. Frontend-only mode works without a backend agent; a local speech-to-speech frontend is also supported.

---

## Agent Skills

**Status:** ⚠️ No official Qwen Audio Agent `SKILL.md` is published.

The runtime reuses the selected backend agent's existing Skills and MCP configuration; that is capability passthrough, not an official skill for operating Qwen Audio Agent itself.

Search community skills: `npx clawhub@latest search qwen-audio-agent`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ No MCP server exposed by Qwen Audio Agent. It connects to backend agents through ACP and can reuse the backend's configured MCP servers and tools.

---

## What It Does

Qwen Audio Agent is a local realtime voice front end for persistent tool-using agents. The voice layer keeps listening and speaking while long-running work continues asynchronously, so the conversation does not freeze during searches, code changes, or other tool calls. Users can ask for status, cancel work, interrupt speech naturally, and receive the completed result back in the originating conversation.

Its architecture separates a low-latency realtime assistant from one persistent backend-agent session. Requests that need tools are converted into Work records and sent through ACP to OpenCode, OpenClaw, Qoder, Qwen Code, Kimi Code, Hermes, CodeBuddy, Codex, Claude Code, or another ACP-compatible agent. The desktop, WebUI, and TUI share the same gateway primitives, local memory boundaries, permission relay, and result-delivery semantics.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The project calls itself *"a realtime voice runtime that keeps Agents talking, working, and present"* — [README](https://github.com/QwenAudio/qwen-audio-agent#readme) |
| **Agent-specific primitive** | Nonblocking `spawn_thinking`, persistent backend-agent sessions, asynchronous Work receipts, progress projection from tool calls, correlated delegation, cancellation, owner-scoped permission relay, and completion reinsertion into live conversation |
| **Autonomy-compatible control plane** | Multiple Work items queue while voice continues; backend agents choose their own tool strategy; `native` and `full` permission modes, cancellation, serialization, and local policy boundaries constrain execution |
| **M2M integration surface** | ACP over stdio, generic ACP command adapter, local Gateway, CLI, WebUI/TUI clients, and backend session lifecycle calls |
| **Identity / delegation** | Stable per-owner/backend session identity, isolated per-user local state, Work and delegation IDs, explicit owner-scoped permission requests, credential-redacted logs, and task recovery records |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Realtime Frontend** | Full-duplex voice layer for immediate answers, interruption, and conversational continuity |
| **`spawn_thinking`** | Accepts a goal and returns immediately while backend work continues asynchronously |
| **Work Record** | Queued/running/delegated/finalizing/completed lifecycle receipt with timestamps, result, and bounded activity |
| **Fixed Backend Session** | Persistent ACP session keyed by owner and backend, resumed across voice conversations |
| **Delegated Session** | Correlated target session for longer backend work, completed only by the matching delegation ID |
| **Permission Relay** | Forwards only an explicit current-turn user answer to a pending owner-scoped backend request |
| **Progress Projection** | Converts backend tool updates into safe generic activity without exposing raw reasoning or secrets |
| **Local Memory Layers** | Separate assistant profile, user preferences, factual memory, audit log, and task state |

---

## Autonomy Model

```text
User speaks while the realtime frontend remains responsive
    ↓
Simple requests are answered immediately; tool work calls spawn_thinking
    ↓
Gateway creates an owner-scoped Work record and queues it
    ↓
One persistent ACP backend session receives the objective and recent context
    ↓
Backend selects tools, Skills, MCP servers, and execution strategy
    ↓
Gateway projects safe progress; user may ask status or cancel
    ↓
Matching completion is validated and returned to the realtime conversation
    ↓
Result is marked delivered only after playback completes
```

---

## Identity and Delegation Model

- The Gateway generates a local identity key and isolates browser-mode profiles, memory, tasks, and logs per user.
- The coordination session has a stable identity of `qwen-audio-agent:<owner>:backend`; native ACP session IDs are stored behind that key and resumed later.
- Every task has a Work ID. Native backend delegation adds an opaque delegation ID and target session ID so unrelated or stale updates cannot complete the task.
- Permission prompts are owner-scoped and can be answered only from an explicit current-turn user decision; the realtime model cannot invent consent or alter backend policy.
- `tasks.json`, credential-redacted JSONL logs, and `memory-audit.jsonl` preserve task delivery and memory-change evidence locally.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| ACP | Native or adapted stdio connections to supported backend coding agents; session new/resume/update/cancel semantics |
| CLI | `qwenaudio`, `config`, `setup`, `install`, `tui`, `webui`, and `gateway` service controls |
| Local Gateway | Coordinates realtime sessions, Work queues, task state, permission requests, and frontend clients |
| Voice Frontends | DashScope Qwen realtime models or a local Hugging Face speech-to-speech pipeline |
| User Interfaces | Terminal TUI, browser WebUI, and desktop floating orb for macOS, Windows, and Linux |
| Local State | Markdown identity/preferences/memory files, JSON task recovery, and redacted JSONL logs |

---

## Human-in-the-Loop Support

The default `native` mode preserves the backend agent's own permission prompts. The Gateway may relay only a user's explicit answer to the currently pending, owner-scoped request; it cannot manufacture approval. Users can inspect progress, cancel a queued/running/delegated task, interrupt speech, and correct or delete memory. A `full` mode removes per-action prompts for supported backends and should be used only in trusted workspaces.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **STT + TTS pipeline** | Converts audio but lacks persistent agent sessions, nonblocking work receipts, permission relay, cancellation correlation, and result recovery |
| **Consumer voice assistant** | Human-facing closed product without a generic ACP backend, reusable Skills/MCP tools, inspectable local state, or agent task lifecycle |
| **Standalone coding-agent CLI** | Can execute tools but does not remain present in a continuous full-duplex conversation or return asynchronous results into it |
| **Generic WebSocket chat UI** | Transports messages but does not model voice interruption, backend delegation, owner identity, permissions, or Work delivery semantics |

---

## Use Cases

- **Always-present coding assistant** — talk with Codex, Claude Code, Qwen Code, or another backend while it works on files asynchronously
- **Voice-driven desktop operations** — delegate tool-using tasks, hear progress and completion, and interrupt or cancel naturally
- **Accessible long-running research** — keep conversing while one or more research tasks queue behind a persistent backend session
- **Local personalized assistant** — maintain per-user preferences and factual memory with explicit boundaries and audit records
- **ACP voice front end** — add realtime speech and task delivery to a custom ACP-compatible agent without rewriting its tools or memory
