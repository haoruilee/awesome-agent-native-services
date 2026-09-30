# Agent QA

> **"The self-improving QA agent for software teams."**

| | |
|---|---|
| **Website** | https://vostride.com/ |
| **Docs** | https://vostride.com/docs/agent-qa |
| **GitHub** | https://github.com/vostride/agent-qa |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/vostride/agent-qa?style=social)](https://github.com/vostride/agent-qa) |
| **Classification** | `agent-native` |
| **Category** | [Agent Harnesses & Operator Surfaces](README.md) |
| **License** | FSL-1.1-ALv2; converts to Apache-2.0 two years after each version is published |
| **Latest-month signal** | v0.1.21 (2026-06-03) is still the latest release and npm `agent-qa` is 0.1.21; last GitHub push 2026-08-03; 892 stars; `LICENSE.md` still FSL-1.1-ALv2; three `skills/agent-qa-*` SKILL.md files present; [vostride.com](https://vostride.com/) and [docs](https://vostride.com/docs/agent-qa) HTTP 200 (verified 2026-09-30) |
| **Verified at** | 2026-09-30 |

---

## Official Website

https://vostride.com/

Product documentation: https://vostride.com/docs/agent-qa

---

## Official Repo

https://github.com/vostride/agent-qa

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI workspace + MCP + published Agent Skills`

```bash
npx agent-qa init
npx agent-qa dashboard --port 3470 --open
codex mcp add agent-qa -- agent-qa mcp
npx skills add vostride/agent-qa --skill agent-qa-authoring --skill agent-qa-debug-fix --skill agent-qa-result-triage
```

`npx agent-qa init` scaffolds file-backed config, sample tests, and suites. Start the local operator UI with `npx agent-qa dashboard --port 3470 --open`. Runs need a configured LLM (hosted, local, or Codex/Claude Code subscription auth via the optional `@vostride/agent-qa-subscription-auth` package). There is no URL-onboarding document.

---

## Agent Skills

**Status:** ✅ Available

```
npx skills add vostride/agent-qa --skill agent-qa-authoring --skill agent-qa-debug-fix --skill agent-qa-result-triage
```

| Skill | What It Teaches the Agent |
|---|---|
| `agent-qa-authoring` | Discover config, generate IDs, validate definitions, and create or update tests, suites, and hooks through MCP before editing YAML |
| `agent-qa-result-triage` | Gather run detail, steps, artifacts, and logs, then classify a failure without immediately patching |
| `agent-qa-debug-fix` | Start from run evidence and `agent_qa_classify_failure`, apply the smallest change that explains the evidence, and rerun the narrowest affected case |

The package currently ships those three skills. `agent-qa skills --json` lists the skills bundled with the installed CLI version.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/vostride/agent-qa |
| **Transport** | stdio (`agent-qa mcp`) or dashboard-backed Streamable HTTP at `http://127.0.0.1:3471/mcp` |
| **Compatible Clients** | Codex, Claude Code, OpenCode, and other MCP clients that accept stdio or a Streamable HTTP URL |

```
agent-qa mcp
codex mcp add agent-qa -- agent-qa mcp
```

Dashboard-backed authoring, run, artifact, and triage tools need a live dashboard. Start `agent-qa dashboard --port 3470` or pass `dashboardUrl` to stdio tool calls. Source-backed tools include discovery and schema helpers plus `agent_qa_enqueue_test_run`, `agent_qa_enqueue_suite_run`, `agent_qa_get_run`, `agent_qa_get_run_steps`, `agent_qa_get_run_logs`, `agent_qa_get_run_artifact`, `agent_qa_cancel_run`, and `agent_qa_classify_failure`. Treat local MCP access as workspace access: an enabled client can read config, inspect artifacts, enqueue runs, and mutate tests.

---

## What It Does

Agent QA is a source-available QA-agent harness with a local live operator surface. Teams write web and mobile journeys in plain-English YAML. The bundled QA agent observes the live UI, plans the next action, executes it, and verifies the result, including re-observation and self-healing when a click, fill, or select fails. Each run can produce file-backed product, suite, and test memory, plus screenshots, logs, artifacts, and model-usage records. Operators and coding agents share the same CLI, dashboard, MCP, and Skill surfaces.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Official docs and homepage call it **"The self-improving QA agent for software teams"** and tell operators to **"follow a live run while an agent is acting"** — [docs](https://vostride.com/docs/agent-qa), [dashboard](https://vostride.com/docs/agent-qa/dashboard#runs) |
| **Agent-specific primitive** | The live run surface keeps a concrete run ID, current natural-language step, observe/plan/execute/verify feedback, captured browser state, self-healing attempts, model/token usage, and memory produced for later runs — not generic pass/fail telemetry |
| **Autonomy-compatible control plane** | Once started, the QA agent chooses and verifies UI actions without per-action human confirmation. Operators or MCP clients can enqueue a test or suite, follow it live, inspect evidence, and cancel a pending or running run |
| **M2M integration surface** | `agent-qa` CLI, local dashboard APIs, stdio and loopback HTTP MCP, and three published Agent Skills. Authoring and run tools are source-backed and addressable by run ID |
| **Identity / delegation** | Every execution has a run ID and `/runs/:id` detail/live route. Steps, attempts, logs, artifacts, screenshots, model usage, and memory observations are attributed to that run. Agent QA models a QA-agent run, not a distinct long-lived identity, and it does not mint delegated authority or enforce a general approval policy |

This entry is admitted on the category's operator-surface track: the dashboard and CLI are purpose-built around the bundled QA agent's live runs. The same product also publishes MCP and Skills and can enqueue or cancel work; those extras strengthen the case and are not required for the track.

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Natural-language YAML journeys** | Reviewable, source-controlled web and mobile tests written as plain-English steps |
| **Live run identity** | Concrete run IDs with `/runs/:id` and `/runs/:id/live` routes, step timelines, and suite-child context |
| **Observe / plan / execute / verify** | Per-step reasoning, action feedback, verifier results, and self-healing retries on failed UI actions |
| **File-backed memory** | Product, suite, and test observations written after a run and injected as evidence on later steps |
| **Queue controls** | Enqueue tests or suites; list and cancel pending or running jobs from CLI, dashboard, or MCP |
| **Evidence pack** | Screenshots, artifacts, console/network logs, execution logs, and model/token usage attributed to the run |

---

## Autonomy Model

```
Operator or coding agent authors a natural-language YAML test or suite
    -> enqueue via dashboard, agent-qa run, or MCP enqueue tools
    -> QA agent observes the live UI, plans the next action, executes it, and verifies the result
    -> failed actions re-observe the screen and try another path in the same run
    -> live /runs/:id/live view updates the step timeline, browser evidence, and verifier/action feedback
    -> operator or MCP client may inspect artifacts or cancel a pending/running run
    -> memory curator writes file-backed product, suite, and test observations for later runs
```

The agent loop is autonomous inside a started test or suite. Enqueue, cancel, and workspace mutation remain explicit CLI, dashboard, or MCP actions.

---

## Identity and Delegation Model

- **Run identity:** Each execution has a concrete run ID. Dashboard routes and MCP tools return steps, attempts, logs, artifacts, and suite-child context by that ID.
- **Attribution:** Screenshots, artifacts, model usage, and memory observations are stored against the run that produced them.
- **Workspace credentials:** Model-provider keys and target-app authentication stay in workspace configuration (`~/.agent-qa/auth.json` for model secrets; named auth-state for signed-in web targets). They are not minted as a per-agent identity credential.
- **No delegated authority:** Agent QA does not issue a distinct long-lived agent identity, lease, or delegated-permission token.
- **No general approval policy:** Client-level MCP auto-approval is controlled by the MCP host. Agent QA does not enforce a product-wide approval gate.
- **License boundary:** The repository is source-available under FSL-1.1-ALv2 and grants Apache-2.0 on the second anniversary of each published version. Upstream README sometimes says open source; the license file is FSL, not a current OSI-approved grant.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `agent-qa init`, `run`, `dashboard`, `queue list`, `queue cancel`, `validate`, `doctor`, `mcp`, `skills` |
| Dashboard | Local operator UI and dashboard APIs for runs, tests, hooks, suites, memory, insights, and config |
| MCP stdio | `agent-qa mcp` for discovery, authoring, enqueue, inspect, cancel, and failure classification |
| MCP HTTP | Dashboard-backed loopback endpoint, default `http://127.0.0.1:3471/mcp` |
| Agent Skills | Packaged `agent-qa-authoring`, `agent-qa-debug-fix`, and `agent-qa-result-triage` |
| File-backed state | Tests, suites, hooks, config, memory observations, cache, and run artifacts in the workspace |

---

## Human-in-the-Loop Support

The dashboard is the human operator surface: follow a live run, inspect the step timeline beside captured browser state, review memory, and cancel in-progress work. `agent-qa queue cancel` and `agent_qa_cancel_run` expose the same cancel path to CLI and coding agents. Capturing a named web auth-state requires a human to sign in once. MCP mutation tools can change tests and enqueue runs, so client auto-approval should be reviewed before enabling them. After a run starts, the QA agent does not wait for per-action human confirmation.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Playwright HTML report** | Shows generic test/process outcomes after the fact. It is not bound to a live autonomous QA-agent run and does not interpret observe/plan/execute/verify state, healing attempts, agent memory, or run-addressable MCP APIs |
| **Ordinary test-runner dashboard** | Can list pass/fail and duration, but does not keep a QA-agent step timeline, live reasoning/action/verifier feedback, or file-backed memory produced for later agent runs |
| **Generic process monitor** | Displays host telemetry rather than a concrete QA-agent run identity with screenshots, artifacts, and cancelable queue state |

---

## Use Cases

- **Natural-language web and mobile QA** — write reviewable YAML journeys and let the QA agent execute them against local or staged apps
- **Live operator follow-along** — watch an acting QA agent, inspect browser evidence, and cancel a stuck run
- **Coding-agent authoring** — use MCP and `agent-qa-authoring` to create, validate, and enqueue tests from Codex, Claude Code, or OpenCode
- **Failure triage** — classify a failed run from artifacts and logs with `agent-qa-result-triage` before deciding what to change
- **Self-improving regression loops** — keep file-backed memory so later runs adapt to product behavior and UI drift
