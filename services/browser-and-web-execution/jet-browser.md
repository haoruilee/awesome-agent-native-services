# Jet Browser

> **"Jet Browser — the browser runtime agents can carry."**

| | |
|---|---|
| **Website** | https://masaka-ai.vercel.app/jet-browser/ |
| **Docs** | https://github.com/masakaai/jet-browser#readme |
| **GitHub** | https://github.com/masakaai/jet-browser |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/masakaai/jet-browser?style=social)](https://github.com/masakaai/jet-browser) |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |
| **License** | Apache-2.0 |
| **Latest release** | [v0.8.0](https://github.com/masakaai/jet-browser/releases/tag/v0.8.0) |
| **Verified at** | 2026-10-11 |

---

## Official Website

https://masaka-ai.vercel.app/jet-browser/

---

## Official Repo

https://github.com/masakaai/jet-browser

---

## How to Use (Agent Onboarding)

**Interaction pattern:** self-hosted container runtime with an ordered JSONL stdio protocol. Docker and curl are enough for the bounded acceptance proof:

```bash
curl -fsSL https://raw.githubusercontent.com/masakaai/jet-browser/main/scripts/try-jet.sh | sh
```

The script verifies the release seccomp policy, pulls the `linux/amd64` runtime by immutable digest, disables browser networking, then checks startup, native input, matching DOM state, PNG capture, and cleanup. It requires no repository checkout, Node.js installation, account, API key, model, or hosted control plane. Review the [script](https://github.com/masakaai/jet-browser/blob/main/scripts/try-jet.sh) before running it.

For the full runtime protocol, supervise one Jet Browser container per mutually untrusted session and send one JSON command per line as documented in the [README](https://github.com/masakaai/jet-browser/tree/v0.8.0#4-embed-the-runtime-boundary).

---

## Agent Skills

**Status:** ✅ Available — the repository publishes one Jet Browser skill through Codex and Claude Code plugin manifests, and keeps the same source at `.agents/skills/jet-browser/SKILL.md`.

```bash
# Codex
codex plugin marketplace add masakaai/jet-browser --ref v0.8.0
codex plugin add jet-browser@masaka

# Claude Code
claude plugin marketplace add masakaai/jet-browser
claude plugin install jet-browser@masaka
```

| Skill | What It Teaches the Agent |
|---|---|
| [`jet-browser`](https://github.com/masakaai/jet-browser/blob/v0.8.0/.agents/skills/jet-browser/SKILL.md) | Check requirements, run the verified standalone flow, integrate the ordered JSONL and versioned tool schemas, and preserve the WPE WebKit and profile-isolation boundaries |

---

## MCP

**Status:** ✅ Available — a deliberately bounded runtime verifier, not a general browsing server.

| Detail | Value |
|---|---|
| **Registry name** | [`io.github.masakaai/jet-browser`](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.masakaai%2Fjet-browser/versions/latest) |
| **Source** | [`integrations/mcp`](https://github.com/masakaai/jet-browser/tree/v0.8.0/integrations/mcp) |
| **Transport** | stdio, distributed as `ghcr.io/masakaai/jet-browser-mcp:0.8.0` |
| **Tools** | `jet_browser_capabilities`, `jet_browser_verify` |
| **Boundary** | Accepts no URL, profile, credential, host path, arbitrary image, or command; browser networking is disabled |

The verifier needs the Docker socket to start the separately isolated browser container, so it should be configured only in a trusted local MCP client. The broader browser runtime remains the framework-neutral JSONL interface rather than an MCP-only product.

---

## What It Does

Jet Browser packages WPE WebKit, a headless Wayland compositor, and a Rust WebDriver bridge as a standalone runtime for agent systems. One container owns one browser session; a harness sends ordered JSONL commands and receives machine-readable results for navigation, native pointer/keyboard/touch input, tabs, JavaScript evaluation, semantic DOM capture, screenshots, downloads, state import/export, and close.

The runtime is intentionally smaller than a complete browser-agent framework. It includes no model, reasoning loop, account, database, proxy network, or hosted control plane. Native input, DOM state, and a fresh screenshot come from the same runtime, while versioned tool declarations let an embedding harness expose only the operations it chooses.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The official product page calls Jet Browser ["the browser runtime agents can carry"](https://masaka-ai.vercel.app/jet-browser/), and the repository describes a standalone runtime supervised by an agent harness. |
| **Agent-specific primitive** | One-session-per-container ownership, ordered action/result lines, versioned model-facing tool declarations, and same-runtime native-input/DOM/PNG evidence provide an execution boundary for agent loops rather than a human browsing UI. |
| **Autonomy-compatible control plane** | A supervisor can create, operate, inspect, and close the browser without per-action human confirmation; resource limits, explicit profile paths, outbound-network policy, failure cleanup, and optional control epochs bound autonomous runs. |
| **M2M integration surface** | Ordered JSONL over stdin/stdout is the core interface; versioned JSON Schemas, a public OCI image, GitHub Action, Agent Skill, Hermes plugin, and bounded stdio MCP verifier provide integration paths. |
| **Identity / delegation** | Each container and explicit profile path map browser state to one delegated task/session. Jet does not mint user credentials or silently inherit a daily browser profile; credential policy, authorization, and durable audit storage remain the embedding application's responsibility. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Isolated browser session** | One WPE WebKit session, runtime directory, process tree, and explicit profile path per container |
| **Ordered command/result stream** | One JSON command per input line and one attributable machine-readable response per output line |
| **Native interaction** | Pointer, keyboard, text, touch, wheel, drag, navigation, and tab operations through the real browser input path |
| **Semantic and visual evidence** | DOM/document state, JavaScript results, screenshots, and visual frames from the same session |
| **Versioned agent tools** | JSON Schema declarations for binding runtime operations into model-facing harnesses without changing the execution contract |
| **Bounded acceptance proof** | Network-disabled startup, native-input, DOM, PNG, and cleanup verification against an immutable release image |

---

## Autonomy Model

1. A trusted supervisor starts one resource-bounded Jet Browser container for an agent task, with network and profile policy chosen explicitly.
2. The harness sends `create`, `navigate`, input, inspection, and capture commands as ordered JSONL.
3. Jet executes those operations inside the one WPE WebKit session and returns one structured result per command.
4. The agent uses semantic evidence to select targets and fresh screenshots when visual verification is required.
5. The supervisor sends `close` in guaranteed cleanup and removes the disposable container; optional profile or download mounts persist only when explicitly configured.

---

## Identity and Delegation Model

- A container, process tree, runtime directory, and browser session form the primary task identity boundary.
- Explicit profile paths allow an operator to delegate only the cookie and storage state intended for that task; Jet never attaches to a running personal Chrome profile.
- Network, evaluate, imported-profile, download, and filesystem access are privileged capabilities that the embedding harness must grant deliberately.
- Optional monotonically increasing control epochs let a distributed supervisor reject stale controllers after session ownership changes.
- Ordered responses and evidence artifacts support attribution to a session, but Jet does not claim an application-level agent principal, credential broker, signed audit ledger, or policy engine.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **JSONL stdio** | Core create → navigate → native input → inspect → screenshot → close protocol, usable from any subprocess supervisor |
| **Agent tool schemas** | Versioned JSON Schema declarations in [`sdk/tools.mjs`](https://github.com/masakaai/jet-browser/blob/v0.8.0/sdk/tools.mjs) |
| **MCP stdio verifier** | Two bounded tools for capability discovery and immutable network-disabled runtime acceptance |
| **OCI image** | Public `linux/amd64` runtime at `ghcr.io/masakaai/jet-browser:0.8.0`; pin its digest in production |
| **GitHub Action** | [`masakaai/jet-browser@v0.8.0`](https://github.com/marketplace/actions/jet-browser-runtime-smoke-test) runs the acceptance proof in CI |
| **Agent plugins** | Codex, Claude Code, and Hermes integration metadata around the same runtime boundary |

---

## Human-in-the-Loop Support

The standalone core is designed for unattended execution and has no built-in approval dialog. Optional distributed components can provide live visual frames and human takeover around the same session, but approvals, credential consent, and high-risk action policy belong to the calling harness. The bounded MCP verifier cannot navigate public URLs or receive credentials at all.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **A personal Chrome profile** | Couples an agent to a human's live cookies, extensions, tabs, and desktop session instead of creating an explicit disposable task boundary. |
| **A generic Chromium container** | Provides a browser process but not Jet's ordered agent command/result contract, versioned tool declarations, or same-session native-input/DOM/PNG acceptance proof. |
| **A complete browser-agent framework** | Bundles model choice and reasoning with execution; Jet keeps the browser runtime replaceable underneath any harness or deterministic test runner. |

---

## Use Cases

- **Coding-agent browser checks** — give a repository-aware agent a disposable non-Chromium runtime for UI verification without access to daily Chrome.
- **Framework-neutral browser workers** — supervise isolated WPE WebKit processes from an existing agent loop in any language.
- **Cross-engine evaluation** — add a WPE WebKit execution boundary beside Chromium-based Playwright or CDP tests.
- **Evidence-gated automation** — require native input, DOM state, and a fresh PNG to agree before accepting a browser step.
- **CI runtime acceptance** — verify browser startup and cleanup from a pinned image with outbound browser networking disabled.
