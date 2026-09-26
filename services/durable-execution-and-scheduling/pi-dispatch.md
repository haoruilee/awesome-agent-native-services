# pi-dispatch

> **"Run the pi coding agent as a service — triggered on demand, on a cron schedule, or by a GitHub or GitLab issue, comment or pull/merge request — in a container you control, with a durable queue, a spend cap, and a live admin panel."**

| | |
|---|---|
| **Website** | https://github.com/edgehero/pi-dispatch |
| **Docs** | https://github.com/edgehero/pi-dispatch#readme |
| **GitHub** | https://github.com/edgehero/pi-dispatch |
| **Classification** | `agent-native` |
| **Category** | [Durable Execution & Scheduling Services](README.md) |
| **License** | MIT |
| **Latest-month signal** | Product release [v1.10.3](https://github.com/edgehero/pi-dispatch/releases/tag/v1.10.3) published 2026-09-07; 178 stars; license MIT; last push 2026-09-25 ([repo metadata](https://api.github.com/repos/edgehero/pi-dispatch)) |
| **Verified at** | 2026-09-26 |

---

## Official Website

https://github.com/edgehero/pi-dispatch

---

## Official Repo

https://github.com/edgehero/pi-dispatch

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `Daemon / Extension + CLI`

```bash
# Guided setup from pi
pi install npm:@edgehero/pi-dispatch-admin
# Then type /dispatch inside pi and follow the setup prompts.

# Headless setup and first job
mkdir my-dispatch && cd my-dispatch
npx @edgehero/pi-dispatch up
npx @edgehero/pi-dispatch worker
npx @edgehero/pi-dispatch run ./my-project --task "add type hints" --flow tidy
```

Docker, Node.js 22.19+, and a supported provider API key are required. Use the scoped `@edgehero/pi-dispatch` package; the unscoped npm package is unrelated.

---

## Agent Skills

**Status:** ✅ Available in the admin pi package

```bash
pi install npm:@edgehero/pi-dispatch-admin
```

| Skill | What It Teaches the Agent |
|---|---|
| [`operate-pi-dispatch`](https://github.com/edgehero/pi-dispatch/blob/main/admin/skills/operate-pi-dispatch/SKILL.md) | Inspect queue state, runs, costs, and triggers; pause/resume processing; use operator-confirmed configuration tools safely |
| Repository `.pi/skills/<flow>/SKILL.md` | Defines the committed, reviewable flow that a trigger executes inside a job container |

---

## MCP

**Status:** ⚠️ No MCP server published. pi-dispatch exposes pi extension tools and a CLI rather than MCP.

---

## What It Does

pi-dispatch turns the pi coding agent into a self-hosted background service. CLI submissions, cron schedules, and GitHub, GitLab, Forgejo/Gitea, or Azure DevOps events enter one BullMQ/Valkey queue. A worker checks spend and turn limits, starts a locked-down ephemeral container, runs one committed skill against the target repository, records the result and usage, and removes the container.

It is scheduling and job-level durability rather than a general step-checkpoint workflow engine. Queue state survives restarts, jobs can be paused without being dropped, and selected follow-up triggers can resume the session that opened a pull request. The operator console provides run history, cost attribution, trigger/flow topology, quiet hours, and a global stop control.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The official description begins, *"Run the pi coding agent as a service"*, and the README describes the missing operational layer for unattended pi jobs — [README](https://github.com/edgehero/pi-dispatch#readme) |
| **Agent-specific primitive** | Committed `.pi/skills` flows, agent turn budgets, AI-trigger opt-in, resumable agent sessions, bot-loop guards, model usage ledgers, and agent-safe tool controls |
| **Autonomy-compatible control plane** | Approved cron and forge triggers enqueue unattended jobs; per-job plus daily/weekly/monthly limits are checked before model spend; quiet hours, pause, rate limits, and container isolation constrain autonomy |
| **M2M integration surface** | CLI, forge webhooks/pollers, BullMQ queue, pi extension tools, JSON trigger files, and structured run records |
| **Identity / delegation** | Forge actor permissions gate triggers; each forge job gets a short-lived repository-scoped token; job and delivery IDs support deduplication and attribution; run records retain flow, target, usage, and parent/child chain data |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Trigger** | A cron, CLI, label, comment, pull-request/review, or work-item event paired with a flow |
| **Flow** | A committed `.pi/skills/<flow>/SKILL.md` containing the job's standing agent instructions |
| **Durable Job** | BullMQ/Valkey queue item retained across bursts, pauses, and worker restarts |
| **Job Container** | Ephemeral non-root Docker boundary with dropped capabilities, read-only instructions, and a controlled workspace mount |
| **Spend Gate** | Per-job turn/token budget plus daily, weekly, and monthly caps checked before execution |
| **Pause Window** | Timezone-aware deferral for a repository or folder; jobs wait rather than disappear |
| **Run Record** | PII-minimized outcome, timing, usage/cost ledger, flow, target, and chain attribution |
| **Resumable Session** | Optional continuation of the agent session that opened a pull request |

---

## Autonomy Model

```text
Operator reviews a flow and trigger, then commits/configures them
    ↓
Cron, CLI, or an authorized forge actor emits an event
    ↓
Receiver verifies signature, actor permission, loop guard, and dedup key
    ↓
Durable queue accepts the job; pause windows may defer it
    ↓
Worker checks image, branch protection, turn budget, and spend caps
    ↓
One isolated container runs pi with the selected committed flow
    ↓
Agent edits, tests, and optionally opens or updates a pull request
    ↓
Run outcome, usage, costs, and chain links are stored for inspection
```

---

## Identity and Delegation Model

- A forge job is attributable to its delivery ID, triggering actor, repository, trigger, flow, and run ID.
- GitHub App mode mints a short-lived, repository-scoped token per job; GitLab, Forgejo, and Azure paths resolve the triggering actor's project/repository permissions.
- Each container receives only an allowlisted environment; credential files are not copied into the staged pi overlay.
- The committed flow is the delegation contract. `ai-trigger: allow` separately opts a flow into model-initiated `dispatch_run` or chaining.
- PII-minimized run records and per-model usage ledgers provide an audit trail; raw logs are opt-in and remain host-side.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `pi-dispatch up`, `worker`, `run`, `pause`, `resume`, `status`, `service`, `sandbox`, and setup commands |
| pi Extension | `/dispatch` TUI and model-callable `dispatch_*` observation/control tools |
| Forge Events | HMAC-verified webhooks or polling for GitHub; webhook receivers for GitLab, Forgejo/Gitea, and Azure DevOps |
| Queue | BullMQ over Valkey with AOF persistence, deduplication, retention, and concurrency control |
| Configuration | `triggers.json`, pause windows, environment variables, committed `.pi/skills`, and pinned staged pi packages |
| Run History | Durable structured records plus a per-model token/cost ledger and generated insights report |

---

## Human-in-the-Loop Support

Humans approve the standing policy rather than every job. GitHub labels and collaborator/reviewer checks can act as the launch approval, while operator-facing confirmation dialogs protect money-affecting configuration changes. Setup is deliberately operator-typed, and pause/resume provides an immediate reversible stop. `dispatch_run` can enqueue autonomously only inside producer-side folder, flow opt-in, dirty-tree, rate, and spend gates. pi-dispatch does not provide a generic mid-flow durable `wait()` primitive.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **cron + shell script** | Schedules a process but lacks agent turn budgets, spend gates, forge actor checks, skill delegation, isolated per-job execution, and agent run attribution |
| **Celery / generic job queue** | Provides queue durability but no coding-agent flow contract, repository token lifecycle, branch protection checks, or model usage policy |
| **Plain pi session** | Interactive and powerful, but has no durable queue, concurrency control, unattended trigger edge, or cross-job spending limits |
| **Generic GitHub Action** | Handles repository events, but does not unify local folders, multiple forges, cron jobs, agent session resume, and one self-hosted queue/control plane |

---

## Use Cases

- **Issue-to-PR automation** — an authorized label or comment launches a contained coding-agent job that opens a reviewable pull request
- **Nightly repository maintenance** — run lint cleanup, backlog triage, or report updates on a bounded schedule
- **Review-follow-up loops** — resume the agent session that opened a PR and address collaborator feedback
- **Multi-repository agent operations** — share one durable queue, concurrency policy, budget, and console across many repositories
- **Cost-bounded experiments** — race replicas or compare models while preserving per-flow and per-model usage evidence
