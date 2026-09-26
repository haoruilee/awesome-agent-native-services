# OpenAI Symphony

> **"Symphony turns project work into isolated, autonomous implementation runs, allowing teams to manage work instead of supervising coding agents."**

| | |
|---|---|
| **Website** | https://openai.com/index/open-source-codex-orchestration-symphony/ |
| **Docs** | https://github.com/openai/symphony/blob/main/SPEC.md |
| **GitHub** | https://github.com/openai/symphony |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/openai/symphony?style=social)](https://github.com/openai/symphony) |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | [v0.0.3](https://github.com/openai/symphony/releases/tag/v0.0.3) released 2026-09-15; 27,409 stars; license Apache-2.0; last push 2026-09-15. The marketing page returned HTTP 403 to this client on 2026-09-26 ([repo metadata](https://api.github.com/repos/openai/symphony)) |
| **Verified at** | 2026-09-26 |

---

## Official Website

https://openai.com/index/open-source-codex-orchestration-symphony/

That URL returned HTTP 403 to the catalog client on 2026-09-26. The same URL is still the repository homepage. This re-check used the GitHub repository, not the marketing page body.

---

## Official Repo

https://github.com/openai/symphony

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `Agent-readable specification` or `Elixir reference service`

The primary onboarding path is itself agent-readable:

```text
Implement Symphony according to the following spec:
https://github.com/openai/symphony/blob/main/SPEC.md
```

To evaluate the official reference implementation instead:

```text
Set up Symphony for my repository based on
https://github.com/openai/symphony/blob/main/elixir/README.md
```

The reference requires a configured issue tracker, a working Codex CLI, and an in-repository `WORKFLOW.md`. It is explicitly **prototype software for trusted evaluation**, not a hardened production distribution.

---

## Agent Skills

**Status:** ✅ Repository skills available

The Elixir reference includes optional `commit`, `push`, `pull`, `land`, and tracker skills. Copy only the skills needed by the target repository after reviewing them; the canonical operating policy remains the repository-owned `WORKFLOW.md`.

---

## MCP

**Status:** ⚠️ No standalone MCP server

Symphony launches Codex through the Codex app-server protocol. Tracker adapters can advertise provider-native tools such as `linear_graphql`, `github_api`, `jira_rest`, `asana_api`, and `gitlab_api` to the coding-agent session.

---

## What It Does

Symphony continuously reads eligible work from an issue tracker, claims an issue, creates a deterministic isolated workspace, and launches a Codex app-server session inside it. It keeps the agent working through bounded turns, reconciles tracker state, schedules retries, and exposes structured runtime status. The work policy lives in version-controlled `WORKFLOW.md`, so the prompt, completion rules, proof requirements, and handoff state travel with the codebase.

The language-neutral [SPEC.md](https://github.com/openai/symphony/blob/main/SPEC.md) is the product contract. The included Elixir/OTP implementation is a reference implementation and supports Linear, GitHub Issues, Jira Cloud, Asana, and GitLab.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The official description says Symphony turns work into **autonomous implementation runs** so teams manage work instead of supervising coding agents — [README](https://github.com/openai/symphony) |
| **Agent-specific primitive** | Issue-to-agent dispatch, per-issue workspaces, multi-turn agent workers, tracker reconciliation, retry queues, blocked-agent state, and Codex thread/turn metadata are primitives for operating coding agents rather than generic jobs |
| **Autonomy-compatible control plane** | Fixed-cadence polling, bounded global/per-state concurrency, retry backoff, terminal-state cancellation, and configurable Codex approval/sandbox settings let runs progress unattended within repository policy |
| **M2M integration surface** | Language-neutral service specification, tracker adapters, Codex app-server protocol, JSON API, structured logs, and repository-owned machine-readable workflow configuration |
| **Identity / delegation** | Stable tracker issue IDs become dispatch identities; each issue owns a collision-resistant workspace and live Codex thread/turn metadata. Host-side tracker credentials are used by provider-native tools and removed from the Codex child environment, separating delegated action from raw-secret access |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Tracker adapter** | Normalizes work items and exposes provider-native agent tools |
| **Dispatch/reconciliation loop** | Claims eligible issues, bounds concurrency, stops obsolete runs, and schedules retries |
| **Per-issue workspace** | Deterministic, preserved execution directory with lifecycle hooks |
| **Agent runner** | Starts Codex app server, streams events, and continues bounded turns |
| **`WORKFLOW.md` policy** | Versioned prompt, completion contract, tool policy, and handoff rules |
| **Blocked state** | Surfaces operator input, approval, or MCP elicitation requirements |
| **Structured observability** | Session status, token/runtime totals, rate limits, logs, and optional dashboard |

---

## Autonomy Model

```text
Tracker issue becomes eligible
    -> Symphony claims its stable issue ID
    -> isolated workspace is created or resumed
    -> WORKFLOW.md is rendered for a Codex app-server session
    -> Codex works and uses host-mediated tracker tools
    -> Symphony reconciles state, continues, retries, blocks, or releases
    -> terminal tracker state stops the worker and triggers cleanup
```

The spec deliberately leaves the final approval and sandbox posture to the deployment. A successful run may hand off to a state such as `Human Review` instead of merging automatically.

---

## Identity and Delegation Model

- **Work identity:** The tracker issue ID is the opaque dispatch identity; the human-readable key names logs and workspaces.
- **Run identity:** Codex `thread_id` and `turn_id` form a live session identity, while the workspace binds effects to one issue.
- **Delegated credentials:** Tracker credentials stay host-side where adapters execute provider-native operations; declared secret variables are stripped before spawning Codex.
- **Audit boundary:** Structured logs, tracker history, workspace/git evidence, and session metrics support attribution. Symphony does not claim to be a tamper-proof audit ledger.
- **Current reference limitation:** The Elixir blocked map is memory-only, so a restart may make an active tracker issue dispatchable again. Hardened deployments must address this and the preview security posture.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Specification | `SPEC.md` — language-neutral normative service contract |
| Agent runtime | Codex app-server protocol |
| Tracker integrations | Linear, GitHub Issues, Jira Cloud, Asana, GitLab in the reference |
| Configuration | YAML front matter plus prompt body in repository-owned `WORKFLOW.md` |
| Operations | Structured logs, optional JSON API/dashboard, workspace lifecycle hooks |

---

## Human-in-the-Loop Support

Symphony detects when Codex requests operator input, approval, or MCP elicitation and exposes the run as blocked. Workflow policy can make `Human Review` the successful handoff state. Operators can also stop work by moving an issue to a terminal state.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Generic cron + shell script** | No tracker reconciliation, per-issue claim identity, Codex turn lifecycle, blocked-agent state, or repository-owned workflow contract |
| **CI job runner** | Treats work as a fixed pipeline rather than a resumable multi-turn agent session with retries and tracker handoff |
| **Raw issue webhook** | Starts work once but does not continuously reconcile issue eligibility, concurrency, retries, or terminal cancellation |

---

## Use Cases

- **Issue-to-PR implementation** — dispatch eligible tracker issues into isolated Codex workspaces
- **Background maintenance** — run bounded refactors or dependency work without supervising every turn
- **Proof-driven delivery** — require CI, review, complexity, or walkthrough evidence in `WORKFLOW.md`
- **Human-review queues** — let agents finish implementation and move work to an explicit review state
- **Multi-project agent operations** — implement the portable spec against the tracker and runtime used by an organization
