# ParallelSandbox

> **"A row of in-progress test builds of your app."**

| | |
|---|---|
| **Website** | https://parallelsandbox.com/en/ |
| **Docs** | https://parallelsandbox.com/en/docs/quickstart/ |
| **GitHub** | https://github.com/parallel-sandbox/parallelsandbox-mcp |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |

---

## Official Website

https://parallelsandbox.com/en/

---

## Official Repo

The hosted service is closed source. The MCP stdio adapter and the Agent Skill are public: https://github.com/parallel-sandbox/parallelsandbox-mcp (MIT).

---

## How to Use (Agent Onboarding)

> **URL Onboarding with human steps: the agent reads one document and connects itself, but a person completes the OAuth sign-in in the browser once.**

**One-sentence instruction:**

```
Read https://parallelsandbox.com/skill/SKILL.md and follow the instructions to install the ParallelSandbox skill and complete the connection.
```

**Interaction pattern:** `URL Onboarding` ⚠️ — partial.

People still have to do one thing:
- Complete the OAuth sign-in in the browser when the MCP client connects (OAuth 2.1 with PKCE and dynamic client registration). No API key is needed.

The stdio adapter, which also moves local files into and out of a box, needs Node 20+ and `npx`:

```
claude mcp add parallelsandbox -- npx -y parallelsandbox-mcp
```

Remote MCP (Streamable HTTP, OAuth), without local file transfers:

```
claude mcp add --transport http parallelsandbox https://mcp.parallelsandbox.com/mcp
```

---

## Agent Skills

**Status:** ✅ Available

```bash
npx skills add parallel-sandbox/parallelsandbox-mcp
```

| Skill | What It Teaches the Agent |
|---|---|
| `parallelsandbox` | Start a box with a goal, sync the project in, build and run it, test it with screenshots and recordings, read browser logs, hand a working version to a person with `sandbox_review`, ask for a takeover for logins or payments, and stop the box |

The same guide is served as plain markdown at https://parallelsandbox.com/skill/SKILL.md.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/parallel-sandbox/parallelsandbox-mcp (stdio adapter); hosted endpoint `https://mcp.parallelsandbox.com/mcp` |
| **Registry** | Official MCP Registry: `com.parallelsandbox/parallelsandbox` |
| **Transport** | Streamable HTTP; stdio through `npx -y parallelsandbox-mcp` |
| **Auth** | OAuth 2.1 (PKCE, dynamic client registration); API keys optional for clients without OAuth |
| **Compatible Clients** | Claude Code, Codex, Cursor, Gemini CLI, any MCP client |

---

## What It Does

ParallelSandbox gives a coding agent a remote Linux machine (a "box") for each piece of work: a small virtual machine with its own disk and network, Docker, git, Node, Go, Python, Chromium and a virtual display. The agent starts a box with a goal, copies the project in, runs commands, docker compose stacks and browser tests there, and takes screenshots and screen recordings of what it built. Several boxes run at once, isolated from each other and from the person's own computer.

When a version works, the agent hands it to a person with `sandbox_review`. The person opens it as a user (a web page, or a phone or desktop app on the box's screen), says what is wrong and circles it on the screen; the recording, circled screenshots and transcript come back to the same agent conversation, and the agent makes the next version. For steps only a person can do, such as a login, a second factor or a payment, the agent asks for a takeover of the box's live screen and gets control back afterwards.

Before building, the agent can propose screens (`sandbox_draft`), services (`sandbox_architecture`) and data schemas (`sandbox_schema`) for the person to mark up. Idle boxes freeze and stop billing, and are stopped after a set time.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "A row of in-progress test builds of your app. Use each one, say what's wrong and circle it on screen, and your AI makes the next version." and "Your AI works on several versions at once." — https://parallelsandbox.com/en/ ; the agent drives each build through MCP tool calls |
| **Agent-specific primitive** | `sandbox_start` takes a required `goal` returned to any later agent session that picks the box up; `sandbox_review` hands a tested version to a person and returns their report to the same agent conversation; `sandbox_takeover` hands the live screen to a person and back — https://parallelsandbox.com/en/docs/tools/ |
| **Autonomy-compatible control plane** | The agent starts, runs commands in, screenshots, hands over and stops boxes with no per-action confirmation. Limits: one virtual machine per box with its own disk and network (https://parallelsandbox.com/en/docs/faq/), usage metered against the account's credits (https://parallelsandbox.com/en/docs/tools/credits/), idle boxes freeze and are stopped after a set time (https://parallelsandbox.com/en/docs/tools/box-states/) |
| **M2M integration surface** | Remote MCP over Streamable HTTP, MIT stdio adapter, REST API (https://parallelsandbox.com/en/docs/tools/rest/), browser log SDK (https://parallelsandbox.com/en/docs/log-sdk/); the person's app is a secondary surface for reviewing results |
| **Identity / delegation** | Each agent client is authorized with its own OAuth grant, revocable separately from the person's sign-in; each box records the agent conversation using it and the last steps taken in it — https://parallelsandbox.com/en/docs/tools/sandbox-status/ |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Box** (`sandbox_start`) | A remote Linux virtual machine started with a required `goal`, an optional size, toolchains, secrets and an environment |
| **Command** (`sandbox_exec`, `sandbox_procs`) | Runs a command in the box, in the foreground or in the background, and lists running processes |
| **File transfer** (`sandbox_sync`, `sandbox_get`, `sandbox_pull`) | Copies the local project into the box and files back out |
| **Screenshot / recording** (`sandbox_shot`, `sandbox_scene`, `sandbox_media`) | Screenshots and mp4 recordings of the box's screen, kept per step |
| **Review** (`sandbox_review`) | Hands a working version to a person and returns their recording, circled screenshots and transcript to the agent |
| **Takeover** (`sandbox_takeover`) | Asks a person to take over the live screen for a login, a second factor or a payment |
| **Designs** (`sandbox_draft`, `sandbox_architecture`, `sandbox_schema`) | Screens, services and data schemas the person marks up before the agent builds |
| **Status** (`sandbox_status`) | The box's goal, last 30 steps and whether the conversation using it is still at it |
| **Browser logs** (`logs_errors`, `logs_search`, `logs_tail`) | Console output and errors from pages the box runs, with source maps resolved |

---

## Autonomy Model

1. A person connects the agent once and completes the OAuth sign-in in the browser.
2. The agent calls `sandbox_start` with a goal; the box restores from a snapshot.
3. The agent copies the project in with `sandbox_sync`, then builds, runs and tests it with `sandbox_exec`.
4. The agent checks the result with screenshots, recordings and browser logs, and fixes what fails.
5. When the version works, the agent calls `sandbox_review`; the person's report returns to the same conversation and the agent makes the next version.
6. When nothing is left for the person to see, the agent calls `sandbox_stop`; an idle box freezes and is stopped by the idle rules.

---

## Identity and Delegation Model

- The person authorizes each agent client with OAuth 2.1 (PKCE, dynamic client registration); each grant is tied to the client that requested it and can be revoked separately from the person's own sign-in.
- API keys, for clients without OAuth, are created and revoked by the account owner; an API key or OAuth token cannot create other keys.
- Each box records the MCP client and agent conversation that started or last used it, and its `goal`.
- `sandbox_status` returns the last steps taken in the box (commands, directories and notes), with screenshots and recordings per step; steps a person did are marked `human`.
- Secrets enter a box as environment variables only when the agent names them.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP | `https://mcp.parallelsandbox.com/mcp`, Streamable HTTP, OAuth |
| MCP stdio adapter | `npx -y parallelsandbox-mcp` (MIT, Node 20+), adds local file transfer |
| REST API | https://parallelsandbox.com/en/docs/tools/rest/ |
| Browser log SDK | `@parallelsandbox/log` — https://parallelsandbox.com/en/docs/log-sdk/ |
| Agent Skill | `npx skills add parallel-sandbox/parallelsandbox-mcp` |
| Docs for agents | https://parallelsandbox.com/llms.txt, https://parallelsandbox.com/skill/SKILL.md |

---

## Human-in-the-Loop Support

Human review is a first-class step: `sandbox_review` puts a working version in the person's app, and their recording, circled screenshots and transcript return to the agent conversation that handed it over. `sandbox_takeover` gives the person the box's live screen for a login, a second factor, a CAPTCHA or a payment, then returns control to the agent. The person can also watch any box's screen live and leave messages the agent receives on its next call. None of these are needed for the agent's own build-and-test loop.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **A cloud VM (EC2)** | A person provisions and configures it; no goal-scoped lifecycle for the agent, no primitive that hands a running version to a person and returns their feedback, no takeover handoff |
| **A cloud development environment (GitHub Codespaces)** | Built for a human developer working through an IDE or SSH; the agent has no review or takeover primitive and no per-session record of what it did |

---

## Use Cases

- **Iterate on a user experience** — the agent builds several versions in parallel boxes and hands each to a person, who circles what is wrong and talks
- **End-to-end tests off the laptop** — docker compose stacks and headed browser tests run in a box instead of on the person's computer
- **Logins and payments in a flow** — the agent hands the live screen to a person for a second factor or a payment, then continues
- **Design before building** — the agent proposes screens, services and schemas, the person marks them up, then the agent builds
- **Picking up another session's work** — a later agent conversation reads the box's goal and last steps and continues
