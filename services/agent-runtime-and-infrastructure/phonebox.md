# Phonebox

> **"The agent-first cloud phone: cloud Android phones that AI agents can see and control, billed per second."**

| | |
|---|---|
| **Website** | https://phonebox.dev |
| **Docs** | https://phonebox.dev/docs |
| **GitHub** | Not published (hosted service; public OpenAPI, skill, and MCP docs) |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **Verified at** | 2026-11-12 |

---

## Official Website

https://phonebox.dev

`llms.txt` lead: *"The agent-first cloud phone: cloud Android phones that AI agents can see and control, billed per second."* Phonebox gives an agent the device itself (screen, apps, touch and keyboard), not a phone number — it cannot send or receive SMS or calls.

---

## Official Repo

No public source repository is published. The hosted service exposes machine-readable docs and a CLI tarball:

- Agent skill: https://phonebox.dev/skills/phonebox/SKILL.md
- Setup for agents: https://phonebox.dev/setup.md
- OpenAPI: https://phonebox.dev/openapi.json
- Full docs: https://phonebox.dev/llms-full.txt
- MCP guide: https://phonebox.dev/docs-markdown/interfaces/mcp

---

## How to Use (Agent Onboarding)

**Interaction pattern:** agent-readable setup document + CLI + hosted MCP + REST.

This is not a one-URL join path. The recommended path is that an agent follows https://phonebox.dev/setup.md, but a person still has to sign in and start the free week (card required, 7 days free). The agent must not ask for a password or card details.

From [setup.md](https://phonebox.dev/setup.md) (Node.js 20 or later):

```bash
npm install -g https://phonebox.dev/downloads/phonebox-0.1.0.tgz
phonebox setup --no-wait
```

`phonebox setup --no-wait` prints one JSON line for the step that is waiting (`sign_in`, `start_trial`, …). The agent gives the person the `url` (and `user_code` when present), waits until they say they are done, and runs the same command again until `"step": "ready"`. The next run saves an agent key on the machine; the agent is told it never sees that key.

After the project is ready, the skill and MCP server can be kept for later (with the user's permission):

```bash
mkdir -p ~/.claude/skills/phonebox && curl -fsSL https://phonebox.dev/skills/phonebox/SKILL.md -o ~/.claude/skills/phonebox/SKILL.md
claude mcp add --scope user --transport http phonebox https://phonebox.dev/mcp --header "Authorization: Bearer $(phonebox token)"
```

Without a shell, `POST https://phonebox.dev/v1/setup` starts the same device-authorization flow. Always park a phone when done — a phone bills from the moment it exists until it parks (`llms.txt` rules for agents).

---

## Agent Skills

**Status:** ✅ Available (hosted `SKILL.md`, not an `npx skills add` registry package)

```bash
curl -fsSL https://phonebox.dev/skills/phonebox/SKILL.md -o ~/.claude/skills/phonebox/SKILL.md
```

| Skill | What It Teaches the Agent |
|---|---|
| `phonebox` | Set up and drive Phonebox from a coding agent (https://phonebox.dev/skills/phonebox/SKILL.md) |

---

## MCP

**Status:** ✅ Available (hosted)

| Detail | Value |
|---|---|
| **MCP Repo** | Not published (hosted endpoint) |
| **Endpoint** | `https://phonebox.dev/mcp` |
| **Transport** | Streamable HTTP |
| **Auth** | `Authorization: Bearer $(phonebox token)` (or a `pbx_…` API key) |
| **Docs** | https://phonebox.dev/docs-markdown/interfaces/mcp |
| **Compatible Clients** | Claude Code, Codex, Cursor, Gemini CLI, Windsurf, Cline, GitHub Copilot, and other Streamable HTTP clients (see the guides in `llms.txt`) |

---

## What It Does

Phonebox provisions cloud Android phones that an agent can see and control. The agent reads the screen as text, taps, types, installs APKs, and parks the phone when it is done. Phones park when idle and keep their apps and sign-ins. Billing is $0.06 per minute, billed per second, with parked phones free, as stated on Phonebox's own guides (check https://phonebox.dev/docs/billing/plans for current plans). A new account starts with a 7-day free week (card required).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | `llms.txt`: *"The agent-first cloud phone: cloud Android phones that AI agents can see and control, billed per second."* Source: https://phonebox.dev/llms.txt |
| **Agent-specific primitive** | A parked/resumable cloud Android phone whose screen is an agent-readable tree, with action batches, idempotent creates, and explicit park-when-done billing rules written for agents. |
| **Autonomy-compatible control plane** | After a person signs in and starts the trial, the agent creates a phone, drives it, and parks it with no per-tap human click. Credit and plan gates (`402`, `403`) return a link for the person, and the agent is told to wait — not to retry in a loop. |
| **M2M integration surface** | Hosted MCP, REST + OpenAPI, CLI, `SKILL.md`, `setup.md`, `llms.txt`. Terminal setup can mint a key after a person confirms a short code. |
| **Identity / delegation** | Agent API keys (`pbx_…`). The setup flow saves a key the agent "never sees." A live-view link is documented as a credential — whoever opens it controls the phone until it expires. `Idempotency-Key` on creates. Pages reviewed do not describe a cross-service KYA token. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Cloud Android phone** | Create, drive (screen/tap/type/install), park. Parked phones keep apps and sign-ins and do not bill. |
| **Agent key** | `pbx_…` Bearer key, minted through CLI setup or `POST /v1/setup`. |
| **Idempotent create** | `Idempotency-Key` on every create; repeat only with the same key and body. |
| **Live view** | A time-limited link a person can use to watch or take over; treat it as a credential. |

---

## Autonomy Model

1. Agent runs `phonebox setup --no-wait` (or `POST /v1/setup`) and hands the person one link at a time.
2. After `"step": "ready"`, the agent creates a phone with an `Idempotency-Key`.
3. Agent reads the screen, acts in batches, and observes before retrying a failed action (per `llms.txt` rules).
4. On `402 insufficient_credits` or `403 plan_required`, the agent gives the person the URL in `details` and waits.
5. Agent always parks the phone when finished, even if the task failed.

---

## Identity and Delegation Model

- Project-scoped agent keys (`pbx_…`); the CLI stores the key locally and `phonebox token` retrieves it for MCP.
- Live-view URLs are credentials.
- Create-idempotency prevents duplicate phones on retry.
- The agent is instructed never to paste the key into a committed file and never to collect passwords or card data.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Setup | https://phonebox.dev/setup.md — CLI or `POST /v1/setup` |
| MCP | `https://phonebox.dev/mcp` |
| REST | OpenAPI at https://phonebox.dev/openapi.json |
| Skill | https://phonebox.dev/skills/phonebox/SKILL.md |
| CLI | `npm install -g https://phonebox.dev/downloads/phonebox-0.1.0.tgz` |

---

## Human-in-the-Loop Support

A person is required to sign in, start the free week (card check), and complete checkout or plan links when credit runs out. A live-view link lets them watch or take over. The drive loop itself is autonomous once the phone exists.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Device farms (BrowserStack, AWS Device Farm)** | Built for Appium/QA suites, not an agent-first MCP + park/billing contract. |
| **Local emulators + ADB** | Operator-run tooling, no hosted agent key, skill, or park-when-done control plane. |

---

## Use Cases

- **Coding-agent QA** — build an APK, install it on a cloud phone, walk the new screens, report the exact screen text.
- **Short burst runs** — per-second billing with free parking, for tasks that do not need an always-on phone.
- **Scheduled smoke tests** — the docs describe nightly recipes that check credit first and always park.
