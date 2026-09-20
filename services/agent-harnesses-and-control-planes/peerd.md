# peerd

> **"peerd: the AI agent harness native to the browser"**

| | |
|---|---|
| **Website** | https://peerd.ai |
| **Docs** | https://github.com/NotASithLord/peerd/blob/main/README.md |
| **GitHub** | https://github.com/NotASithLord/peerd |
| **Classification** | `agent-native` |
| **Category** | [Agent Harnesses & Operator Surfaces](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Softer HN heat this week; architecture fit + Apache-2.0 OSS (earlier Show HN 2026-06-23, [item 48646165](https://news.ycombinator.com/item?id=48646165)) |
| **Verified at** | 2026-09-20 |

---

## Official Website

https://peerd.ai

Live page title: *peerd: the AI agent harness native to the browser*. Homepage H1: *The first browser-native AI agent harness*.

---

## Official Repo

https://github.com/NotASithLord/peerd

Apache-2.0. v0.x developer preview: install from source. Chrome Web Store and Firefox AMO packages are documented as coming soon. CheerpX (Linux WebVM engine) is a commercial dependency today and is **not** covered by peerd's Apache license; the project documents a later move toward v86.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** Browser extension (load unpacked) — local harness, no peerd account

```bash
git clone https://github.com/NotASithLord/peerd.git
```

Then open `chrome://extensions`, enable Developer mode, **Load unpacked**, and select the repo's `extension/` folder. Bring an Anthropic or OpenRouter API key, or a supported local provider (Ollama). First run: unlock the local vault, finish the short profile, add a provider, start a chat.

Firefox needs a packaged XPI (`bun run package -- --channel=preview --browser=firefox --no-sign`), then Load Temporary Add-on. Do not load the checked-in Chrome development manifest into Firefox.

This is **not** URL Onboarding. There is no peerd backend to join, no `skill.md` registration, and no hosted agent account. "No peerd account, hosted browser, or tool-server connection is required" — [README](https://github.com/NotASithLord/peerd).

---

## Agent Skills

**Status:** ⚠️ Not published as an official `npx skills add` pack.

Skills, memory, goals, review, and checkpoints live **inside the extension**. That in-harness skill store is not a ClawHub / agentskills.io install command.

Search community skills: `npx clawhub@latest search peerd`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ Not published — and not the architecture.

peerd's FAQ states it does not ship MCP: tabs, `fetch`, WebVM, and WebRTC replace the usual MCP bridge. MCP is optional interop in the marketing contrast, not the product surface. Do not list peerd as `npx … --mcp`.

| Detail | Value |
|---|---|
| **MCP product claim** | No |
| **Primary interface** | In-browser agent loop (extension side panel + service worker) |
| **Other machine surfaces** | Preview-channel WebRTC A2A / `peerd-distributed` mesh (`did:key`, `peerd://` bundles) |
| **Compatible clients** | Chromium (Chrome, Edge, Brave, Arc, Vivaldi) and Firefox (with packaged XPI) |

---

## What It Does

peerd is a browser extension that runs a full agent harness *inside* the browser you already use. The agent can drive your tabs and signed-in sessions, run sealed JS notebooks, compiled WASI tools, client-side apps, and WASM Linux VMs, and — on preview builds — talk to other peerd browsers over WebRTC.

The homepage thesis: native and cloud apps drive the browser from outside; peerd lives inside it. No background host process, no sidecar, no peerd cloud, no external tool broker. Model calls go to the provider you configured (or local Ollama / planned WebGPU). Current builds send no product telemetry to peerd.

**Category honesty:** this is a **harness**, not a remote browser-as-a-service. Browser & Web Execution in this catalog is for managed / remote browser sessions. peerd inverts that: the user's browser *is* the runtime, hypervisor, and control plane.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Page title: *"peerd: the AI agent harness native to the browser"* — [peerd.ai](https://peerd.ai). README H1: *"The first web-native AI agent harness"*. *"While agent platforms are trying to pull the browser into the harness. peerd pulls the harness into the browser."* |
| **Agent-specific primitive** | In-browser agent loop with mediated tab tools, keyless per-environment **actors**, WASM compute (Notebook / WASI / WebVM), vaulted model keys, structural prompt-injection split (orchestrator never reads raw page; disposable runner has no keys / no egress), optional P2P A2A. Not a Playwright session API. |
| **Autonomy-compatible control plane** | After vault + provider setup, the agent can act on allowed tabs and sandboxes without a peerd server. Constraints: sensitive-site denylist, optional per-step confirm, egress allowlist/denylist, sandbox trust levels. |
| **M2M integration surface** | Extension agent loop, tool/actor APIs, preview WebRTC A2A. No REST SaaS and no MCP server. Machine surface is the browser runtime itself. |
| **Identity / delegation** | Local vault (passphrase / WebAuthn); model key stays in the service worker and is never given to Notebook / App / VM / runner. Preview: Ed25519 `did:key` for peers. Page work is delegated to keyless actors. No peerd cloud identity. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Browser-native harness** | Agent control plane, permissions, audit, storage, and execution live in the extension |
| **Actor** | Keyless delegate scoped to one tab or compute environment |
| **Sandbox spectrum** | Language-sealed Notebook, WASI tool, opaque-origin App iframe, WASM Linux VM |
| **Egress gates** | `safeFetch` provider allowlist and `webFetch` open-web denylist, shared by agent and spawned runtimes |
| **Vaulted BYOK** | Provider key decrypted only in the service worker |
| **P2P A2A (preview)** | WebRTC mesh, `did:key`, `peerd://` bundles — store builds omit dweb |

---

## Autonomy Model

```
Operator loads the unpacked extension and unlocks the local vault
    ↓
Operator adds a model provider (BYOK or local)
    ↓
Agent loop runs in the extension; page reads go to a disposable keyless runner
    ↓
Allowed tab / notebook / WASI / WebVM work proceeds under egress and permission policy
    ↓
Optional Confirm-before-actions still gates individual steps
    ↓
Preview builds may discover other peerd browsers over WebRTC
```

There is no peerd control plane in the cloud. Stopping the browser stops the harness.

---

## Identity and Delegation Model

- **Local operator vault** — passphrase always; passkey when WebAuthn PRF is available.
- **Model credential isolation** — plaintext key never leaves the service worker; sandboxes relay through the same egress gate.
- **Keyless actors** — each page or compute environment gets tools for that environment only; the main agent does not hold page-read + keys + egress in one context (lethal-trifecta split).
- **Peer identity (preview)** — Ed25519 `did:key`; content-addressed `peerd://` bundles.
- **Boundary** — no hosted peerd user/agent account; BYOK means prompts still go to the chosen model provider. CheerpX is a proprietary VM engine.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Browser extension | Load `extension/` (Chromium) or packaged Firefox XPI |
| Homepage / thesis | https://peerd.ai |
| Source / docs | https://github.com/NotASithLord/peerd — `CLAUDE.md`, `SECURITY.md`, `docs/` |
| Preview A2A | `peerd-distributed` WebRTC mesh (omitted from store builds) |
| MCP | Not shipped |
| Hosted API | None — "no backend" |

---

## Human-in-the-Loop Support

First-run vault and provider setup are human. **Confirm before actions** can require per-step approval. A sensitive-site denylist ships pre-loaded (banks, health, password managers, identity providers) and is editable. Audit entries record egress denies. Preview peer connections are experimental. Ordinary in-policy tab and sandbox work can proceed without a click.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Browserbase / Steel / Browser Use Cloud** | Remote or managed browser for agents; peerd refuses that topology |
| **Playwright MCP / Chrome DevTools MCP** | Drive a browser from an external agent; peerd *is* the in-browser harness |
| **Comet / Atlas / Dia "AI browsers"** | New browser product you switch to; peerd is an extension on the browser you already use |
| **Claude Code / OpenCode** | Terminal harnesses; they cannot see the logged-in page peerd shares a process with |

**Category note:** CONTRIBUTING maps `browser-and-web-execution/` to remote browser sessions. peerd is listed under Agent Harnesses because the browser is the harness, not a rented CDP session.

---

## Use Cases

- **In-page operator agent** — fill the form on screen using the live logged-in session
- **Local compute without a host VM product** — Notebook / WASI / WebVM inside tab isolation
- **Prompt-injection-aware browsing** — runner reads the page; orchestrator never gets raw DOM + keys + egress together
- **Preview P2P** — two browsers exchange signed apps or messages without a peerd host
