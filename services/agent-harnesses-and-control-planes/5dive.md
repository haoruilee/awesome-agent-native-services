# 5dive

> **"Run a company of AI agents on a server you own."**

| | |
|---|---|
| **Website** | https://5dive.ai |
| **Docs** | https://5dive.ai/docs/5dive-cli |
| **GitHub** | https://github.com/5dive-ai/5dive |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/5dive-ai/5dive?style=social)](https://github.com/5dive-ai/5dive) |
| **Classification** | `agent-native` |
| **Category** | [Agent Harnesses & Operator Surfaces](README.md) |
| **License** | MIT |
| **Disclosure** | Submitted by [5dive-bot](https://github.com/5dive-bot), the 5dive team's own account, for the 5dive team. We build 5dive. Proposed in [#360](https://github.com/haoruilee/awesome-agent-native-services/issues/360) |
| **Latest-month signal** | [v0.142.0](https://github.com/5dive-ai/5dive/releases/tag/v0.142.0) released 2026-11-24; MIT; [5dive.ai](https://5dive.ai) returned HTTP 200. Operator-surface evidence is pinned to commit [f373b23](https://github.com/5dive-ai/5dive/commit/f373b237a4f7356b92903dfeb45793af7fbf936a) (2026-11-23), the commit re-checked before the Go on [#360](https://github.com/haoruilee/awesome-agent-native-services/issues/360#issuecomment-7118568294); the README is unchanged at `main` commit [c615db8](https://github.com/5dive-ai/5dive/commit/c615db886abbc3681470b02a2c4f467579367652) |
| **Verified at** | 2026-11-24 |

---

## Official Website

https://5dive.ai

---

## Official Repo

https://github.com/5dive-ai/5dive

MIT-licensed. Bash, systemd and SQLite ([README.md#L34](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L34)).

---

## How to Use (Agent Onboarding)

> **URL Onboarding with human steps (⚠️): an agent with sudo on the operator's server can follow one pasted instruction to install 5dive and its skill, but the install runs as root (`curl … | sudo bash`, then `sudo 5dive init`), and every agent runs on the operator's own model credentials (an AI subscription or API key).**

**One-sentence instruction:** the paste block from the [README](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L84-L88):

```
Install 5dive on this server: curl -fsSL https://install.5dive.ai | sudo bash
Then add the 5dive-cli skill: npx -y skills add https://github.com/5dive-ai/skills --skill 5dive-cli
Then ask me which agent to create first.
```

**Interaction pattern:** `URL Onboarding` ⚠️ — partial.

People still have to do these steps:
- Provide a Linux server (Ubuntu 22.04 or newer) and run the installer as root, or let an agent with sudo run it. The README asks you to review `install.sh` before running it as root ([L38](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L38), [L227](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L227)).
- Run `sudo 5dive init`, which walks through creating the first agent ([L92](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L92)). That first agent is `admin` by default ([L227](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L227)).
- Sign in to their own model plan or save their own API key once (`sudo 5dive account add` and `account login`). Agents run on the operator's credentials, and several agents can share one plan or key ([L96](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L96), [L74](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L74)).

The plain install from the [README](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L25-L28):

```bash
curl -fsSL https://install.5dive.ai | sudo bash
sudo 5dive init
```

The README also lists an apt package, Docker Compose and a Vultr Marketplace app ([L42-L67](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L42-L67)).

There is no hosted 5dive account to register ([L38](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L38)). Reading a document does not join an agent to anything; this is not a one-URL join path.

---

## Agent Skills

**Status:** ✅ Available

```bash
npx -y skills add https://github.com/5dive-ai/skills --skill 5dive-cli
```

| Skill | What It Teaches the Agent |
|---|---|
| `5dive-cli` | Lets Claude Code, Codex or another agent run the 5dive team by chatting ([README.md#L80-L88](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L80-L88)). Listed on [skills.sh](https://skills.sh/5dive-ai/skills/5dive-cli) |

---

## MCP

**Status:** ⚠️ Not documented in the 5dive README

This entry makes no MCP claim. Agents and the operator reach 5dive through the `5dive` CLI on the same server ([README.md#L182-L211](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L182-L211)).

---

## What It Does

5dive is a self-hosted runtime and operator surface for a team of CLI agents on the operator's own Linux server. It runs agents such as Claude Code and Codex (the README also lists OpenClaw, Hermes, Antigravity, Grok, OpenCode and Pi) as persistent Linux services. Each agent is its own Linux user with its own permissions and its own systemd service. Agents share one task queue stored in SQLite, hand work to each other, and a second agent can check the work before a task closes. Cron and webhooks trigger work, journald keeps the logs, and coordination goes through the `5dive` CLI, with no external orchestrator.

The operator watches and steers the team from the same CLI. `5dive watch` and `5dive wall` show the team working, live. `activity <agent>` shows what each agent actually did, and `sudo 5dive usage` shows who used the plan's limits. `5dive trace <task>` gives a task's history from the request to the verdict, and `5dive reflex log` keeps a receipt for each routine decision, such as who got a task and why. Permissions are `sandboxed`, `standard` or `admin`, and human approvals are configurable; `5dive human add` sends a person's agents' approvals to that person.

The primary consumer is the human operator of that agent team, and the primary interface is the `5dive` CLI on the server. This entry is admitted on the **operator-surface track**.

---

## Why It Is Agent-Native

Operator-surface track (not the standard five infrastructure criteria). Quotes and source URLs below are pinned to 5dive commit [`f373b23`](https://github.com/5dive-ai/5dive/commit/f373b237a4f7356b92903dfeb45793af7fbf936a), the commit re-checked before the ✅ Go on [#360](https://github.com/haoruilee/awesome-agent-native-services/issues/360#issuecomment-7118568294). The README is unchanged at `main` ([`c615db8`](https://github.com/5dive-ai/5dive/commit/c615db886abbc3681470b02a2c4f467579367652)) as of 2026-11-24.

| Requirement | Evidence |
|---|---|
| **Agent-operations-first** | Built to run and supervise CLI agents, not general applications: CLI agents run as persistent Linux services, each as its own Linux user; `systemd` supervises them and SQLite stores their tasks — [README.md#L32](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L32), [README.md#L219](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L219) |
| **Agent-specific live state** | `5dive watch` · `5dive wall` (the team working, live); `activity <agent>` (what each agent did); `sudo 5dive usage` (who used the plan's limits); `5dive trace <task>`; `5dive reflex log`; per-agent permission tiers — [README.md#L204](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L204), [README.md#L206](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L206), [README.md#L197-L198](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L197-L198), [README.md#L227](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L227) |
| **Session attribution** | State is attributed to a named agent, which is its own Linux user and systemd service: `activity <agent>` and `5dive agent logs` take the agent's name, and `5dive trace <task>` takes the task — [README.md#L216](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L216), [README.md#L206](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L206), [README.md#L187](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L187), [README.md#L197](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L197) |
| **Dedicated operational surface** | The `5dive` CLI ("Every command has `--help`"); one systemd service per agent with journald logs; a daily team digest to Telegram — [README.md#L182-L211](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L182-L211), [README.md#L219](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L219), [README.md#L205](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L205) |
| **Honest boundary** | Present: always-on agents that wake when work waits, schedules, configurable human approvals, per-person approval routing, delegated git push, and an Agent Skill (quotes below). Absent or limited: the primary consumer is the human operator; `watch`, `wall`, `activity` and `usage` are views, and this entry claims observation only for them, not authorization or enforcement; no MCP server is documented in the README; agents run on the operator's own model credentials, not a credential of their own; the install runs as root; the first agent is `admin` by default |

### Evidence quotes (pinned to `f373b23`)

**1. Explicitly built to operate or supervise AI agents, not general applications**

> 5dive runs CLI agents like Claude Code, Codex, OpenClaw, Hermes, Antigravity, Grok, OpenCode and Pi as persistent Linux services. Agents share tasks, delegate work and check each other's results. Each agent runs as its own Linux user, with permissions you choose.

https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L32

> Linux users isolate agents; `systemd` supervises them; SQLite stores tasks; `cron` and webhooks trigger work; journald stores logs. Coordination uses the `5dive` CLI. No external orchestrator.

https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L219

**2. Continuously interprets agent-specific state**

> `5dive watch` · `5dive wall` | Watch the team work, live

https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L204

> `sudo 5dive usage` · `activity <agent>` | Who used your plan's limits, and what each agent actually did

https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L206

> `5dive trace <task>` | A task's full history, from the request to the verdict
>
> `5dive reflex log` | A receipt for every routine decision, like who got a task and why

https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L197-L198

> Every task lands on one shared list. A second agent can check the work before it closes, and an agent wakes only when work is waiting for it. Tasks can also come from GitHub issues and webhooks.

https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L135

**3. Attributes that state to a concrete agent session or rollout**

Each agent is a separate Linux user and systemd service, so state is attributed to a named agent. The architecture diagram's caption:

> Each agent runs as a Linux user and systemd service. Agents coordinate through a shared SQLite queue and the 5dive CLI.

https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L216

> `5dive agent create` · `list` · `logs` · `rm` | Run and manage agents

https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L187

`activity <agent>` (quote 2, L206) names the agent, and `5dive trace <task>` (quote 2, L197) names the task.

**4. Exposes a dedicated operational surface such as a CLI, wrapper, daemon, hook, or status-line protocol**

> Every command has `--help`.

https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L211

> `5dive task add` · `ls` · `inbox` | The shared task list, and what's waiting on you

https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L196

> `5dive digest on` | The team's daily summary, sent to your Telegram

https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L205

**5. Documents honestly when autonomy, machine APIs, delegated credentials, approval enforcement, Skills, or MCP are absent**

Several of those are present, not absent.

Permissions and approvals:

> Agents use `sandboxed`, `standard` or `admin` permissions. The first agent created by `init` is `admin` by default. Human approvals are configurable.

https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L227

> `5dive human add` | Add a person to the team; their agents' approvals go to them

https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L194

Delegated git push and secrets:

> With `5dive push`, agents push code through your own GitHub App and never hold its token.

https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L231

> When an agent needs a key, it sends you a one-time link and you paste it on your phone: the key goes straight to your server, never through 5dive.

https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L229

Autonomy:

> **Always on.** Agents keep working after you close the terminal.

https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L73

What is absent or limited, as documented:

The primary surface is the `5dive` CLI for the human operator. The README presents `watch`, `wall`, `activity` and `usage` as views, and this entry claims observation only for them. The README documents no MCP server. Agents have no model credential of their own; they run on the operator's:

> You need a Linux server (Ubuntu 22.04 or newer) and your own AI subscription or API key, no 5dive account.

https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L38

> **One plan, many agents.** Agents can share one plan or API key, from Claude and ChatGPT to Google and Grok.

https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L74

The install runs as root:

> Review `install.sh` before running it as root.

https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L227

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent as a Linux user** | Each agent is its own Linux user and systemd service, with `sandboxed`, `standard` or `admin` permissions |
| **Shared task queue** | One SQLite-backed list for every task. `--review=<agent>` has a second agent check the work before it closes, `--recurring` repeats a task on a cron schedule, and an agent wakes only when work is waiting for it |
| **Ask / send / task** | `5dive agent ask` waits for an answer, `agent send` tells without a reply, `task add` hands over work |
| **Live team view** | `5dive watch` · `5dive wall` show the team working, live |
| **Per-agent activity and plan usage** | `activity <agent>` shows what each agent actually did; `sudo 5dive usage` shows who used the plan's limits |
| **Task trace and decision receipts** | `5dive trace <task>` from the request to the verdict; `5dive reflex log` records who got a task and why |
| **Human approvals** | Configurable. `5dive human add` sends a person's agents' approvals to that person; `task inbox` lists what is waiting on them |
| **Delegated git push** | With `5dive push`, agents push through the operator's own GitHub App and never hold its token |
| **One-time secret links** | An agent that needs a key sends a one-time link; the key goes straight to the server |
| **Triggers and loops** | `5dive trigger add` turns GitHub or webhook events into tasks; `5dive loop install` gives an agent a job on a schedule |

---

## Autonomy Model

```
Operator installs 5dive on their own Linux server as root (curl … | sudo bash), runs `sudo 5dive init`, and signs in to their own model plan or API key
    -> Each agent runs as its own Linux user and systemd service, and keeps working after the terminal closes
    -> Work lands on one shared task list: from a person, another agent, a cron schedule, a GitHub issue or a webhook
    -> An agent wakes only when work is waiting for it
    -> Agents ask, tell and hand tasks to each other through the `5dive` CLI; a second agent can check the work before a task closes
    -> Human approvals are configurable; after `5dive human add`, a person's agents' approvals go to that person
    -> The operator watches with `5dive watch` / `5dive wall`, reads `activity <agent>` and `sudo 5dive usage`, and audits with `5dive trace <task>` and `5dive reflex log`
```

---

## Identity and Delegation Model

- **Agent identity:** each agent is its own Linux user and systemd service, with the permissions the operator picks (`sandboxed`, `standard` or `admin`). The first agent created by `init` is `admin` by default.
- **No agent-owned model credential:** agents run on the operator's own AI subscription or API key, and several agents can share one plan or key. There is no 5dive account.
- **Delegated git push:** with `5dive push`, agents push code through the operator's own GitHub App and never hold its token.
- **Secrets:** an agent that needs a key sends the person a one-time link; the key goes straight to the server, never through 5dive.
- **Per-person routing:** `5dive human add` adds a person to the team, and their agents' approvals go to them.
- **Audit trail:** `activity <agent>`, `5dive trace <task>`, `5dive reflex log`, and per-agent `5dive agent logs`; journald stores the logs.
- **Optional signed identity:** the OpenAgent plugin, marked new in the README, gives each agent its own signed identity ([README.md#L174](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L174)).
- **Disclosure:** submitted by [5dive-bot](https://github.com/5dive-bot) for the 5dive team. We build 5dive.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `5dive` on the server: agents, tasks, the approvals inbox, live views and traces; every command has `--help` |
| systemd / journald | One systemd service per agent; journald stores the logs |
| Task queue | SQLite, shared by every agent on the server |
| Agent Skill | `5dive-cli`, installed with `npx -y skills add` |
| Triggers | GitHub issues and webhook events become tasks (`5dive trigger add`); cron schedules run recurring tasks and loops |
| Human surfaces (optional) | The 5dive app (link the server at 5dive.ai/self-host), a daily digest in Telegram, and a read-only web dashboard plugin |
| Install | The `install.5dive.ai` script run as root, an apt package, Docker Compose, or the Vultr Marketplace |
| MCP | Not documented in the README |

---

## Human-in-the-Loop Support

Human approvals are configurable ([L227](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L227)). After `5dive human add`, a person is on the team and their agents' approvals go to them ([L194](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L194)); `5dive task inbox` lists what is waiting on the person ([L196](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L196)). A task can name a reviewing agent (`--review=`), so a second agent checks the work before it closes ([L131](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L131), [L135](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L135)). With the browser plugin, the agent asks the person before a step that pays, and asks only when it can't get past an email code or robot check itself ([L156](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L156)). Keys come in through a one-time link the person opens ([L229](https://github.com/5dive-ai/5dive/blob/f373b237a4f7356b92903dfeb45793af7fbf936a/README.md#L229)). The README does not list which actions need approval by default, so this entry claims no default.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Several CLI agents in tmux or screen** | Sessions run side by side under one user. There is no shared task queue, no per-agent Linux user and permissions, no reviewer step, and no per-agent activity or usage view |
| **Generic process monitor or `systemctl status`** | Shows units, CPU and memory. It does not show which agent holds which task, what each agent did, or whose plan limits were used |
| **Generic issue tracker** | A human inbox. It does not wake an agent when work is waiting for it, send approvals to a named person, or record why a task went to a given agent |
| **Agent builders (excluded category)** | A person configures or visually assembles an agent. 5dive runs existing CLI agents such as Claude Code and Codex as Linux services and adds the queue, permissions and operator views around them |

---

## Use Cases

- **Self-hosted agent team** — run Claude Code, Codex and other CLI agents as always-on services on one Linux server, each as its own Linux user
- **Watch the team live** — `5dive watch` / `5dive wall`, then `activity <agent>` for what one agent actually did
- **Plan-limit accounting** — `sudo 5dive usage` to see which agents used a shared plan's limits
- **Reviewed hand-offs** — `5dive task add … --assignee=<agent> --review=<agent>` so a second agent checks the work before it closes
- **Audit a task** — `5dive trace <task>` and `5dive reflex log` for the request-to-verdict history and why a task went where it did
- **Bounded permissions** — `sandboxed` / `standard` / `admin` per agent, approvals sent to a named person, and git push through the operator's own GitHub App
