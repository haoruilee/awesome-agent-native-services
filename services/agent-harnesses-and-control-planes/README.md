# Agent Harnesses & Operator Surfaces

> Systems purpose-built around running agents: either **harnesses** that add durable work state, orchestration, verification, and policy, or **operator surfaces** that expose live agent state and bounded session controls.

## Why This Category Exists

The last month produced a distinct infrastructure layer between a raw agent CLI and a general-purpose runtime. These systems do not merely host an agent or help a human build one. They wrap an already-capable agent, either coordinating it across turns, roles, worktrees, computers, or organizations, or translating its live sessions, context, tools, subagents, permissions, and limits into an operable surface.

This boundary is about the project's primary responsibility:

- **Harness/control-plane track:** owns agent-loop state or control, such as objectives, assignments, checkpoints, retries, policy, or verified evidence.
- **Operator-surface track:** is purpose-built for running agents and continuously derives agent-specific operational state from their native logs, configuration, or protocol. It may be human-facing or read-only, but it must expose substantially more than a generic process/dashboard skin.
- **Runtime boundary:** a system whose primary job is provisioning, hosting, or scheduling the execution substrate remains in Agent Runtime & Infrastructure, even when it includes orchestration features.

A qualifying harness provides agent-specific control primitives such as:

- durable objectives, checkpoints, assignments, or verified state across context refreshes
- explicit leader/worker, manager/executor/auditor, or personal/shared scope boundaries
- autonomous continuation, retries, recovery, cancellation, and bounded execution
- structured machine surfaces such as CLI/JSON, hooks, MCP, app-server, or HTTP APIs
- attributable sessions, delegated permissions, audit events, receipts, or independent verification

A qualifying operator surface instead must bind to live agent sessions and expose agent-native state such as context pressure, rollout/session identity, tool or subagent activity, effective permissions, MCP/Skill configuration, or quota windows. Session attach/list/stop controls strengthen the case. Generic terminal themes, static dashboards, and model-agnostic process monitors do not qualify.

Operator surfaces are an explicit narrow exception to the catalog's usual machine-to-machine/control-plane expectation: their primary consumer may be a human operator, and read-only tools need not mint delegated credentials or autonomously act. Their dossiers must state those limitations rather than presenting observation as orchestration.

## Services

| Service | Tagline | Control Primitives | Machine Surface |
|---|---|---|---|
| [oh-my-codex (OMX)](oh-my-codex.md) [![⭐](https://img.shields.io/github/stars/Yeachan-Heo/oh-my-codex?style=social)](https://github.com/Yeachan-Heo/oh-my-codex) | Workflow and multi-agent runtime layer for OpenAI Codex CLI | Durable goals · role workflows · teams/worktrees · authority leases · replay | CLI/JSON · hooks · Skills · optional MCP |
| [Ruflo](ruflo.md) [![⭐](https://img.shields.io/github/stars/ruvnet/ruflo?style=social)](https://github.com/ruvnet/ruflo) | Agent meta-harness for Claude Code and Codex | Swarms · memory · background workers · federation · budgets | CLI · MCP · plugins · Skills |
| [QM](qm.md) [![⭐](https://img.shields.io/github/stars/yc-software/qm?style=social)](https://github.com/yc-software/qm) | Multiplayer agent harness for work | Personal/shared scopes · durable sandboxes · policy · crons/watches | HTTP API · CLI · deployment Skill |
| [LongHorizon-Harness](longhorizon-harness.md) [![⭐](https://img.shields.io/github/stars/AMAP-ML/LongHorizon-Harness?style=social)](https://github.com/AMAP-ML/LongHorizon-Harness) | Verified long-horizon loop for desktop and CLI agents | Manager/Executor/Auditor · checkpoints · recovery · evidence | CLI · dashboard · agent adapters · MCP config |
| [Agent QA](agent-qa.md) [![⭐](https://img.shields.io/github/stars/vostride/agent-qa?style=social)](https://github.com/vostride/agent-qa) | The self-improving QA agent for software teams | Live run IDs · observe/plan/execute/verify · file-backed memory · queue cancel | CLI · dashboard · MCP · Skills |
| [Codex HUD (fwyc0573)](codex-hud-fwyc0573.md) [![⭐](https://img.shields.io/github/stars/fwyc0573/codex-hud?style=social)](https://github.com/fwyc0573/codex-hud) | Real-time statusline HUD for OpenAI Codex CLI | Live context/tools/subagents · multi-session view · attach/list/kill | tmux wrapper CLI · Codex rollout/config readers |
| [Codex HUD (anhannin)](codex-hud-anhannin.md) [![⭐](https://img.shields.io/github/stars/anhannin/codex-hud?style=social)](https://github.com/anhannin/codex-hud) | Patched Codex status line for usage and session state | Model/project/git · 5-hour and 7-day usage windows | `status_line_command` · rollout JSONL reader |
| [Claude HUD](claude-hud.md) [![⭐](https://img.shields.io/github/stars/jarrodwatts/claude-hud?style=social)](https://github.com/jarrodwatts/claude-hud) | A Claude Code plugin that shows what's happening | Context/usage · tools · subagents · todos | Claude Code plugin · statusline stdin/stdout |
| [LoopX](loopx.md) [![⭐](https://img.shields.io/github/stars/huangruiteng/loopx?style=social)](https://github.com/huangruiteng/loopx) | The open, provider-neutral, stateful control plane for long-horizon agents | Objectives · gates · evidence · quota · claims/leases | CLI · workflow skills · host adapters |
| [DeepSeek Harness (dsh)](deepseek-harness.md) [![⭐](https://img.shields.io/github/stars/deepseek-ai/deepseek-harness?style=social)](https://github.com/deepseek-ai/deepseek-harness) | Everything is a Plugin. | Cordis plugins · session log · Trajectory · PTC/Code Mode | CLI · Web UI · ACP · JSON-RPC SDK |
| [YYLO](yylo.md) [![⭐](https://img.shields.io/github/stars/yylo-dev/yylo?style=social)](https://github.com/yylo-dev/yylo) | Run the work. Keep the memory. | Typed tasks · frozen-target worktrees · watch receipts · merge land | CLI/JSON · Agent Skills · no MCP |
| [Pizza Bot](pizza-bot.md) [![⭐](https://img.shields.io/github/stars/pizza-bot-app/pizza-bot?style=social)](https://github.com/pizza-bot-app/pizza-bot) | Pizza Bot is an inbox for long-running AI work. | Unread/Action queues · checkpointed runs · skill subagents · folder grants | HTTP/SSE api-server · CLI · MCP host · Skills |
| [txcript](txcript.md) [![⭐](https://img.shields.io/github/stars/skillsynchq/txcript?style=social)](https://github.com/skillsynchq/txcript) | Continue your conversation in another coding agent. | Harness codecs · canonical transcript · continue/export · session search | CLI · stdio MCP · Rust crate · npm WASM |
| [peerd](peerd.md) [![⭐](https://img.shields.io/github/stars/NotASithLord/peerd?style=social)](https://github.com/NotASithLord/peerd) | peerd: the AI agent harness native to the browser | In-browser loop · keyless actors · WASM compute · vaulted BYOK | Browser extension · preview WebRTC A2A |

## Criteria Reminder

To qualify for this category, a project must satisfy one of the two tracks:

1. **Harness/control plane:** be positioned for agents; add durable loop primitives; support bounded autonomous progress; expose a machine surface; and preserve meaningful identity, delegation, and evidence.
2. **Operator surface:** be purpose-built for operating running agents; continuously consume agent-native state; attribute that state to a concrete session or rollout; expose an operable CLI/status-line/daemon surface; and document honestly when control, autonomy, Skills, MCP, or delegated authority are absent.

Both tracks exclude generic IDE skins, terminal customizations, observability dashboards, and process monitors that merely relabel human-application telemetry as agent activity.
