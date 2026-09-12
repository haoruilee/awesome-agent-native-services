# OrcaReplay

> **"Your agent broke something at 2am. Replay it at 9am — exactly, offline, as many times as you like."**

| | |
|---|---|
| **Website** | https://github.com/Continuum-AI-Corp/OrcaReplay |
| **Docs** | https://github.com/Continuum-AI-Corp/OrcaReplay/tree/main/docs |
| **GitHub** | https://github.com/Continuum-AI-Corp/OrcaReplay |
| **Classification** | `agent-native` |
| **Category** | [Observability & Tracing Services](README.md) |
| **License** | Apache-2.0 (code); trace spec CC BY 4.0 |
| **Admission track** | Operator-surface track |
| **Interest disclosure** | Builder-submitted — originally submitted by [@xizhuomengcontin](https://github.com/xizhuomengcontin) in [#126](https://github.com/haoruilee/awesome-agent-native-services/pull/126). The proposer is affiliated with Continuum AI Corp, which builds OrcaReplay (and the related [OrcaRouter](https://www.orcarouter.ai) gateway). Maintainer completed remaining dossier sections and catalog regen in [#134](https://github.com/haoruilee/awesome-agent-native-services/pull/134) after ✅ Go on [#128](https://github.com/haoruilee/awesome-agent-native-services/issues/128). |
| **Latest-month signal** | [Created 2026-08-29](https://api.github.com/repos/Continuum-AI-Corp/OrcaReplay); [`orcareplay@0.2.4` on npm 2026-09-11](https://registry.npmjs.org/orcareplay); [active on `main` 2026-09-11](https://github.com/Continuum-AI-Corp/OrcaReplay/commits/main); **229 stars** on 2026-09-12 UTC ([GitHub metadata](https://api.github.com/repos/Continuum-AI-Corp/OrcaReplay)); official MCP registry entry [`io.github.Continuum-AI-Corp/orcareplay`](https://registry.modelcontextprotocol.io/v0/servers?search=orcareplay) is `active`. Early maturity: no tagged 1.0 and no stability guarantee on the v0 trace schema. |
| **Verified at** | 2026-09-12 |

---

## Official Website

The GitHub repository is the canonical project and documentation surface. There is no separate marketing homepage for OrcaReplay.

https://github.com/Continuum-AI-Corp/OrcaReplay

The exact official tagline is the README lead immediately under the `# OrcaReplay` H1, copied character for character:

> Your agent broke something at 2am. Replay it at 9am — exactly, offline, as many times as you like.

[orcarouter.ai](https://www.orcarouter.ai) is a related Continuum gateway that `orca setup` / `orca compare` can use as a default model origin. It is optional. OrcaReplay records against `api.anthropic.com`, `api.openai.com`, or any origin you point it at.

---

## Official Repo

https://github.com/Continuum-AI-Corp/OrcaReplay — Apache-2.0 CLI, capture layers, on-disk trace format, stdio MCP server, Agent Skill, and TypeScript API.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** CLI wrapper (process + socket interception; operator-surface track)

**Quickest verified path** (from the [README install](https://github.com/Continuum-AI-Corp/OrcaReplay#install) and [three-command loop](https://github.com/Continuum-AI-Corp/OrcaReplay#try-it-in-three-commands)):

```bash
npm i -g orcareplay
orca doctor
orca record claude
orca replay last
orca fork last
```

`orca doctor` checks Node, git, and which coding agents it can find. `orca record claude` launches the unmodified harness behind a local proxy (two environment variables for that process only). `orca replay last` re-runs the recording with egress blocked — no model called, no tokens spent. `orca fork` / `orca replay last --from N --model <other>` restores a derived checkpoint and goes live from there.

For a harness that reads no base-URL variable:

```bash
orca record exec --tls-intercept -- <command>
```

There is no URL-onboarding document. The repository README is the join path.

---

## Agent Skills

**Status:** ✅ Published — [`skills/orca-replay/SKILL.md`](https://github.com/Continuum-AI-Corp/OrcaReplay/tree/main/skills/orca-replay), also discoverable on ClawHub.

```bash
npx clawhub@latest search orca-replay
```

For faster access in China, use `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com`.

| Skill | What It Teaches the Agent |
|---|---|
| `orca-replay` | Answer questions about a past run from the recording rather than from memory; distinguish `recorded` vs `inferred` edges; replay offline; treat `orca_compare` as a spend-and-disclosure action that needs approval |

---

## MCP

**Status:** ✅ Available (`orca mcp`, protocol `2025-06-18`)

Listed in the official MCP registry as [`io.github.Continuum-AI-Corp/orcareplay`](https://registry.modelcontextprotocol.io/v0/servers?search=orcareplay) (`active`).

```json
{ "mcpServers": { "orca": { "command": "orca", "args": ["mcp"] } } }
```

Equivalent: `npx -y orcareplay mcp`.

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/Continuum-AI-Corp/OrcaReplay |
| **Transport** | stdio |
| **Tools (6)** | `orca_list_runs`, `orca_show_run`, `orca_checkpoints`, `orca_graph`, `orca_replay`, `orca_compare` |
| **Auth** | Local process; traces stay in the project's `.orca/runs/` |
| **Compatible Clients** | Claude Code, Cursor, Codex, any MCP client that can spawn stdio |
| **Also observes MCP** | A JSON-RPC tee can record the MCP calls the *recorded* agent made, on the same timeline as model traffic |

`orca_replay` is free and offline. `orca_compare` says in its own tool description that it spends real tokens.

---

## What It Does

OrcaReplay records a coding agent **below the harness** and gives the run back. Capture happens at the process and socket boundary rather than through an SDK, so the agent binary stays unmodified. Five layers cooperate on one timeline: a loopback proxy for model traffic, a PATH shim for shell commands and exit codes, an MCP JSON-RPC tee, a shadow git index for per-turn file state, and a `fetch` hook (or opt-in `--tls-intercept`) for hardcoded origins. That shared timeline is what lets you ask which tool call sent the run down the wrong branch.

`orca replay` serves recorded HTTP bodies back with the network off (`egress=blocked`), so the harness runs again against a fixed transcript. `orca fork` / `orca replay --from N --model <other>` sits a cursor on a derived checkpoint: earlier turns stay on disk, later turns go live on a different model against the same conversation prefix and restored git tree. `orca compare` repeats that fork across named models and grades each with a `--verify` command.

Bounds, stated rather than implied. The byte-for-byte guarantee holds when the prompt was recorded through argv (`orca record claude -- -p "…"`). A hand-driven terminal session replays the conversation but not the run byte for byte — the harness makes calls for itself, and interactive-only tools such as `AskUserQuestion` are absent without a person. Replay proves the recorded decisions still reproduce; it cannot prove a fresh run would fail the same way, because the model is not asked again. Replay re-executes recorded tool calls for real and is not a sandbox. `orca compare` uploads recorded context to third-party providers and spends real money.

Supported capture paths include Claude Code, Codex CLI (API key or ChatGPT-subscription login via `--tls-intercept`), opencode, goose, OpenClaw, grok-cli, Cursor-in-the-IDE, plus framework traffic that reads a base-URL variable (OpenAI Agents SDK, Vercel AI SDK, LangGraph, CrewAI, Aider, and others listed in the README).

**Maturity, stated plainly.** The repository was created on **2026-08-29**. As of 2026-09-12 it is on npm as `orcareplay@0.2.4`, listed in the official MCP registry, and ships a published Agent Skill — and it is still early. There is no tagged 1.0, no stability guarantee on the v0 trace schema, and no adoption figure worth claiming. The catalog lists it because the operator-surface is real and documented, not because it is mature.

---

## Why It Is Agent-Native

Admitted on the **operator-surface track**: a CLI wrapper plus stdio MCP and Skill, purpose-built around live coding-agent runs. It is not a generic process monitor, and it is not an SDK you wrap around an agent you wrote.

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README lead under `# OrcaReplay`: *"Your agent broke something at 2am. Replay it at 9am — exactly, offline, as many times as you like."* Next line: *"Record any coding agent."* The product names coding agents (Claude Code, Codex CLI, opencode, goose, OpenClaw, Cursor, grok-cli) as the thing being recorded — [README](https://github.com/Continuum-AI-Corp/OrcaReplay#readme) |
| **Agent-specific primitive** | A `run_<id>` trace of model.request/response, tool.call, fs.snapshot, file diffs, and derived checkpoints; offline **replay** that serves recorded bytes with egress blocked; **fork** from a checkpoint onto another model with byte-identical prefix and restored git tree. These are agent-run primitives, not host CPU graphs — [How it works](https://github.com/Continuum-AI-Corp/OrcaReplay#how-it-works) |
| **Autonomy-compatible control plane** | After install, `orca record` / `orca replay` / `orca show` / `orca graph` run without a human click per event. MCP exposes the same loop to another agent. Spend and disclosure (`orca compare`, live `--from` forks) are explicit, not silent. Observation does not gate the recorded agent |
| **M2M integration surface** | `orca` CLI with `--json`, stdio MCP (`orca mcp`), published Agent Skill, TypeScript `Orca` API, on-disk `.orca/runs/` format with a conformance suite — [For an agent, a script, or CI](https://github.com/Continuum-AI-Corp/OrcaReplay#for-an-agent-a-script-or-ci) |
| **Identity / delegation** | Each run directory's `manifest.json` names the adapter, version, argv, cwd, and harness version. Events carry `seq`, `turn`, and `actor`. A fork records its parent run and the checkpoint it branched at. **Observation is not authorization.** OrcaReplay mints no agent credential and holds no key of its own — it passes the operator's key through, or substitutes a placeholder when the environment carries none |

Honest boundary (operator-surface requirement 5): Qwen Code's DashScope and Gemini origins are deliberately not redirected (wire-dialect mismatch). goose's shell bypasses the PATH shim, so those tool calls miss real exit codes unless `--no-shell` is used to claim nothing. Replay is not a sandbox. The product states these gaps in the README rather than in a footnote.

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Run / trace** | A `run_<id>` directory under `.orca/runs/`: `manifest.json`, append-only `events.jsonl`, blobs, shadow git, redaction log |
| **Loopback proxy** | Process-scoped base-URL rewrite; records verbatim request/response bytes so replay can serve them back |
| **PATH shim** | Captures shell argv, exit code, duration, and stdout/stderr split |
| **MCP tee** | Rewrites the harness MCP config and records JSON-RPC on the same timeline |
| **Shadow git snapshot** | Per-turn workspace tree hash and file diffs; the state a fork restores |
| **Fetch hook / TLS intercept** | Capture when the origin is hardcoded or the harness reads no base-URL variable (`--tls-intercept` mints a per-run CA the child alone trusts) |
| **Replay** | Re-execute the harness against the recording with `egress=blocked` |
| **Checkpoint** | Derived (not recorded) point where the conversation prefix is complete and the workspace was snapshotted |
| **Fork** | Replay through checkpoint N, then go live on a named model from identical files and prefix |
| **Compare** | Several forks from the same checkpoint; `--verify` makes a command's exit code the verdict |
| **Causal graph** | `orca graph` edges labelled `recorded` or `inferred`, never written back as facts |

---

## Autonomy Model

```
Operator or agent installs orcareplay and runs orca doctor
    ↓
orca record <harness> launches the unmodified agent behind local capture
    ↓
Events land as a run_<id> trace in the project's .orca/runs/
    ↓
orca show / orca graph / MCP tools read the timeline without a dashboard
    ↓
orca replay last serves recorded model bytes with egress=blocked
    ↓
Optional: orca fork / replay --from N --model X goes live from a checkpoint
    ↓
Optional: orca compare spends tokens and needs explicit approval
```

The recorded agent keeps its own permission model. OrcaReplay does not approve, deny, or enforce tool calls.

---

## Identity and Delegation Model

- **Run identity** — `run_<id>` is the unit of record. The manifest attributes adapter, adapter version, argv, cwd, and harness version.
- **Event identity** — events carry `seq`, `turn`, and `actor`. Forks name the parent run and the checkpoint they branched at.
- **Session store** — traces are per-project (`.orca/runs/`), mode `0600`, never a global cloud store. Auth headers are stripped on the write path.
- **No minted authority** — OrcaReplay does not issue agent credentials, wallets, or delegated tokens. It forwards the operator's existing key or uses a placeholder when none is present.
- **Observation ≠ authorization** — seeing a tool call or file write is not permission to have done it, and the recorder does not block the agent.
- **Compare / live fork** — those paths send recorded context to a model provider the operator named. That is disclosure and spend, not a new identity.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `orca doctor`, `record`, `replay`, `fork`, `compare`, `show`, `checkpoints`, `graph`, `export`, `scrub`, `gc`, `attach`, `setup`, `models`, `quickstart`; `--json` on the read/replay commands |
| MCP | stdio `orca mcp` / `npx -y orcareplay mcp`; six tools; official registry `io.github.Continuum-AI-Corp/orcareplay` |
| Agent Skill | [`skills/orca-replay/SKILL.md`](https://github.com/Continuum-AI-Corp/OrcaReplay/tree/main/skills/orca-replay); ClawHub search `orca-replay` |
| TypeScript API | `import { Orca } from 'orcareplay'` — same source of truth the CLI renders |
| On-disk format | v0 trace + JSON Schema; spec at [`spec/orca-trace-v0.md`](https://github.com/Continuum-AI-Corp/OrcaReplay/blob/main/spec/orca-trace-v0.md) (CC BY 4.0) |
| Viewer | Optional single-file HTML (`orca replay --ui` / `orca export -o run.html`); not required for the operational loop |

---

## Human-in-the-Loop Support

Optional, not a gate on record or exact replay. A human may drive the recorded session in a terminal; that path replays approximately, which the README names. `orca compare` and live `--from` forks need operator approval because they upload recorded context and spend real tokens; the Skill and MCP tool descriptions say so. Replay re-executes shell commands for real, so a run that touched Docker, a database, or another host needs a person (or a container) before the first replay. The HTML viewer and shareable cards are operator conveniences. None of this is an approval-gate product: OrcaReplay does not pause the agent for consent on each tool call.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **[Kitaru](kitaru.md)** | Kitaru is SDK/wrap replay-based evals for agents **you instrument**. Recording adapters are a one-line wrap for PydanticAI, OpenAI Agents SDK, LangGraph, Mastra, or the Vercel AI SDK, and replay re-executes *your* code. OrcaReplay captures **below the harness** (loopback proxy, PATH shim, MCP tee, shadow git, fetch hook / TLS intercept) so unmodified binaries — Claude Code, Codex CLI, opencode — can be recorded, replayed offline, and forked. A team on PydanticAI cannot use OrcaReplay's harness adapters as a substitute for Kitaru; a team debugging Claude Code cannot one-line-wrap it in Kitaru |
| **OpenTelemetry GenAI / Langfuse / Braintrust dashboards** | Message content is not captured by default; even when it is, the result is span attributes — a normalised view, not the bytes on the wire. You cannot serve a span back to an SDK as an HTTP response, and closed-source CLIs are not instrumented |
| **mitmproxy / a generic HTTPS dump** | Records bytes but knows nothing of turns, checkpoints, tool calls, or git trees, and cannot fork a run onto another model. The interpretation is the product |
| **[AgentSight](agentsight.md)** | Below-harness *observation* (eBPF + session DBs). It does not re-execute a run with egress blocked or fork a checkpoint onto another model |
| **Generic `strace` / APM** | Host process and request telemetry. No agent turn, no recorded tool result, no replayable conversation prefix |

---

## Use Cases

- **Replay a 2am failure at 9am** — `orca replay last` with the network off until the intermittent failure is a fixture
- **Ask which tool call deleted the file** — `orca show` / `orca graph` on the same timeline as model turns, shell exit codes, and shadow-git diffs
- **Fork onto another model from step N** — same files and conversation prefix; the model is the only variable
- **Compare models with a real verdict** — `orca compare last --from N --models a,b --verify "npm test"`
- **Let a coding agent debug itself** — register `orca mcp` and the `orca-replay` Skill so the next session reads the trace instead of reconstructing from memory
- **Record a binary you cannot edit** — `orca record claude` or `orca record exec --tls-intercept -- <command>` when there is no SDK to wrap
