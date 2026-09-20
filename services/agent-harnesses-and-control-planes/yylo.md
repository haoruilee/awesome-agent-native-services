# YYLO

> **"Run the work. Keep the memory."**

| | |
|---|---|
| **Website** | https://yylo.dev |
| **Docs** | https://github.com/yylo-dev/yylo#readme |
| **GitHub** | https://github.com/yylo-dev/yylo |
| **npm** | https://www.npmjs.com/package/@yylo/cli |
| **Classification** | `agent-native` |
| **Category** | [Agent Harnesses & Operator Surfaces](README.md) |
| **Related issue** | https://github.com/haoruilee/awesome-agent-native-services/issues/129 |
| **License / maturity** | MIT · early 0.2.x CLI (`@yylo/cli` `@latest` was `0.2.6` on 2026-09-20) · no MCP server |

---

## Official Website

https://yylo.dev

Live homepage H1 (2026-09-20): **"Run the work. Keep the memory."** The `<title>` line is supporting evidence only: "YYLO — the system of work for agentic engineering."

**Early-maturity note:** YYLO is a young open-source coding-agent harness, not a household-name production platform. The current npm stable channel is `@latest` on the 0.2.x line. Homepage product-direction copy (PR/deployment/production-outcome learning, automatic workflow selection) is **not** a claim about the current release.

---

## Official Repo

https://github.com/yylo-dev/yylo

Companion packages, independently versioned:

- Skills: https://github.com/yylo-dev/yylo-skills
- Ledger (Git-native records): https://github.com/yylo-dev/yylo-ledger
- Benchmark (evaluation/evidence): https://github.com/yylo-dev/yylo-benchmark

`yy ledger` and `yy benchmark` delegate to those separately installed CLIs; they are not bundled alternate implementations.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI`

```bash
npm install --global '@yylo/cli@latest'
yy --version
yy init --task "Ship one verified change" --subagent pi
yy info --json
yy doctor workspace
```

The README canary (`yy watch exec pwd` after `yy init`) emits a watch receipt with `"state":"COMPLETED"`, `"exit_code":0`, and nonzero `log_bytes` without contacting a model provider. Provider credentials stay with the chosen coding subagent (Pi, Codex, and the other aliases listed by `yy --help`).

Install the seven user-intent-first skills from the public skills repo (not bundled in the CLI):

```bash
yy skills install
# or
npx skills add yylo-dev/yylo-skills
```

Account/provider setup for the coding subagent is external. Reading a document does not register the agent.

---

## Agent Skills

**Status:** ✅ Available (independently versioned; not bundled in `@yylo/cli`)

```bash
yy skills install
npx skills add yylo-dev/yylo-skills
```

| Skill | What It Teaches the Agent |
|---|---|
| `ledger-tasks-yylo` | Operate YYLO Ledger task management and source-of-truth boundaries |
| `wiki-yylo` | Find and maintain durable Markdown knowledge as revisioned Ledger Records |
| `workflow-yylo` | Store and validate workflow Records while keeping execution separately authorized |
| `artifact-yylo` | Capture and inspect durable, provenance-bound Ledger evidence |
| `understand-project-yylo` | Inspect the user project before planning or implementation |
| `plan-ledger-tasks-yylo` | Create a PDR and implementation-sized Ledger tasks |
| `ralph-loop-yylo` | Execute exactly one explicitly assigned Ledger task through validated delivery |

Source: [yylo-dev/yylo-skills](https://github.com/yylo-dev/yylo-skills). Acquisition is staged through `npx skills add` first and can fall back to a shallow exact-tag Git clone. The Go on [#129](https://github.com/haoruilee/awesome-agent-native-services/issues/129) asked to keep a no-Skills disclosure **if still accurate**; live homepage and the skills repo now publish these seven skills, so this listing records that change.

---

## MCP

**Status:** ⚠️ Not yet published

There is no official MCP server. The machine surface is the structured CLI (`yylo` / `yy` / `ypl`), JSON/NDJSON output (`yy info --json`, `--format json|ndjson --raw`), watch receipts, and terminal manifests. Homepage and README contain no MCP claim (verified 2026-09-20).

Search community skills: `npx clawhub@latest search yylo`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## What It Does

YYLO is a command-line orchestrator for coding agents. It coordinates a typed task loop — intent, isolated worktree, validation, review, merge, and release-readiness — and keeps the receipts that explain what happened. It does not replace Git. It routes bounded work to coding subagents, freezes a protected target SHA, and records task, session, review, and evaluation evidence.

The control plane (`yy` / `yylo`) coordinates action; [YYLO Ledger](https://github.com/yylo-dev/yylo-ledger) preserves task truth in Git; [YYLO Benchmark](https://github.com/yylo-dev/yylo-benchmark) turns attempts into evaluation evidence.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Live H1: *"Run the work. Keep the memory."* Homepage: "YYLO (why-lo) coordinates coding agents from engineering intent through validated code, while preserving the task, session, review, and evaluation evidence that explains what happened." — [yylo.dev](https://yylo.dev). README: "YYLO is a command-line orchestrator for coding agents, repeatable workflows, and receipt-backed repository changes." — [yylo-dev/yylo](https://github.com/yylo-dev/yylo) |
| **Agent-specific primitive** | Typed task lifecycle (`task start\|run\|status\|checkpoint\|preflight\|finish`): `task start` freezes the protected target SHA and creates a dedicated branch/worktree; runs emit machine-readable watch receipts; merge is risk-bounded and receipt-backed. A human editing files directly does not need frozen-target worktrees or agent-run receipts. |
| **Autonomy-compatible control plane** | An agent can start → implement in the task worktree → validate → checkpoint → preflight → finish without a dashboard click per step. Hard bounds: after one repair candidate and one delta-review group, unresolved findings stop as `REVIEW_FINDINGS_EXHAUSTED`. A successful epoch emits read-only release readiness and does **not** authorize an RC, tag, push, npm/PyPI publication, deployment, production mutation, or worktree cleanup. |
| **M2M integration surface** | Structured CLI (`yylo`, `yy`, `ypl`), JSON/NDJSON (`yy info --json`, `--format json\|ndjson --raw`), `yy doctor workspace`, `--tmux` observer sessions, published Agent Skills. **No MCP.** |
| **Identity / delegation** | A workflow run retains rendered command identity, stdout/stderr, responses, session IDs, declared receipt hashes, attempts, and terminal manifests. Hash-linked receipts attribute work to the task run and subagent. YYLO does **not** mint per-agent credentials; subagents run with their own configured provider auth. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Typed task** | One bounded outcome with constraints, dependencies, and a frozen protected-target SHA |
| **Task worktree** | Isolated checkout for scoped implementation; controller metadata and integration-owner product bytes stay separate |
| **Watch receipt** | Machine-readable execution evidence (`state`, `exit_code`, `log_bytes`) for a local command |
| **Merge land** | One-task native Git composition with expected-old ref protection; Ledger projection is separate |
| **Release-readiness epoch** | Read-only readiness signal; publication and production mutation remain separate explicit actions |
| **Ledger / Benchmark delegates** | Independently installed record store and evaluation package |

---

## Autonomy Model

1. A human (or prior setup) installs `@yylo/cli`, Git, and a coding subagent with its own provider credentials.
2. `yy init --task "…" --subagent pi` records intent and workspace topology.
3. `yy task start` / `yy task run` freezes the target SHA and delegates implementation to the subagent in the task worktree.
4. Validation and evidence commands (`yy evidence run`, `yy task checkpoint`, optional `yy task preflight`) retain exact-input receipts.
5. `yy task finish` queues a clean committed tip; `yy merge land` composes that one task. Unrelated dirty bytes and conflicts stay private to their task.
6. Release, publish, push, and production mutation stay outside the autonomous loop.

No per-action dashboard confirmation is required inside those typed bounds.

---

## Identity and Delegation Model

- Attribution is per **task run and subagent session**, not a minted YYLO agent credential.
- Receipts, manifests, and session IDs form the audit trail.
- Workspace roles are fail-closed: metadata controller, task worktree, and integration owner are separate authorities (`yy where`, `yy doctor workspace`).
- Provider keys remain with Pi/Codex/other configured subagents. YYLO does not issue those credentials.
- Release publication needs separate maintainer authority (`scripts/release-cli.sh`); the CLI has no release command.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `yylo` and `yy` (equivalent); `ypl` is `yy pi --live` — [@yylo/cli](https://www.npmjs.com/package/@yylo/cli) |
| Machine output | `--format json\|ndjson --raw`; `yy info --json`; `yy capabilities` |
| Receipts | Watch receipts, terminal manifests, content-addressed evidence |
| Agent Skills | [yylo-dev/yylo-skills](https://github.com/yylo-dev/yylo-skills) |
| Ledger / Benchmark | Separate CLIs via `yy ledger` / `yy benchmark` |
| MCP | Not published |

---

## Human-in-the-Loop Support

Humans choose Simple vs Advanced workspace mode, install provider credentials, and authorize release/publish. Risk-based merge review can require semantic reviewers on a frozen candidate. Observation (`yy task status`, `yy merge status`, `--tmux`) does not acquire merge or release authority. There is no hosted approval-queue product; the bounds are typed CLI policy.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Kanban + git worktree + manual review** | Organizes human tickets. It does not drive a typed agent task loop, emit watch receipts attributable to a subagent run, or enforce risk-based merge of agent-made candidates. |
| **Raw coding-agent CLI alone** | Runs an agent. It does not freeze a protected target, isolate controller vs task worktree, or retain receipt-backed validation/merge/release-readiness boundaries. |

---

## Use Cases

- **Bounded agent change** — start one task, implement in the frozen-base worktree, finish with receipts, land that task only.
- **Observable local validation** — `yy watch exec` / `yy evidence run` so acceptance is inspectable later.
- **Repeatable agent workflow** — `yy loop` or a reviewed YAML workflow with retained command identity and manifests.
- **Engineering memory** — keep intent, attempts, and validated code as Ledger Records for later work.
