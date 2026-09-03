# Compartment

> **"Encrypted, fully offline memory for AI agents."**

| | |
|---|---|
| **Website** | https://maxfreedompollard.github.io/Compartment/ |
| **Docs** | https://github.com/MaxFreedomPollard/Compartment#readme |
| **GitHub** | https://github.com/MaxFreedomPollard/Compartment |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/MaxFreedomPollard/Compartment?style=social)](https://github.com/MaxFreedomPollard/Compartment) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Last GitHub push 2026-09-02 ([repo metadata](https://api.github.com/repos/MaxFreedomPollard/Compartment)); PyPI `compartment` |
| **Verified at** | 2026-09-03 |

---

## Official Website

https://maxfreedompollard.github.io/Compartment/

Page H1 body (live 2026-09-03): **"Encrypted, fully offline memory for AI agents."** Site `<title>` uses the close variant “Encrypted, fully offline **agentic** memory…” — the catalog tagline is the **H1 sentence**, which matches the README bold lead.

---

## Official Repo

https://github.com/MaxFreedomPollard/Compartment

README: **"Encrypted, fully offline memory for AI agents."** One vault on the machine, read and written by Claude Code, Claude Desktop, Hermes, OpenClaw, Cursor, Codex, and any MCP client. No API key, no account, no network, no telemetry.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + MCP (`compartment serve`)

```bash
pip install compartment && compartment init
compartment integrate claude      # also: hermes, openclaw, or --all
# MCP clients without a recipe:
# { "mcpServers": { "compartment": { "command": "compartment", "args": ["serve"] } } }
```

`integrate --list` documents ~28 MCP clients (Cursor, VS Code, Cline, Codex CLI, Gemini CLI, …). `integrate claude` can install a PostToolUse capture hook (`--no-hooks` skips it) plus the `/compartmentalize` skill.

**The GUI is secondary.** The menu-bar / tray / Linux window unlocks the vault and opens a 127.0.0.1 read-only dashboard. The agent operational surface is **MCP + CLI**, not the panel.

There is no URL-onboarding document.

---

## Agent Skills

**Status:** ✅ `/compartmentalize` installed by `integrate claude|hermes|openclaw` (not `npx skills add`)

| Skill | What It Teaches the Agent |
|---|---|
| `/compartmentalize` | Store one-claim memories, recall, supersede opinions |
| Claude Code plugin | Marketplace: `/plugin marketplace add MaxFreedomPollard/Compartment` then `/plugin install compartment@maxfreedompollard` |

```bash
npx clawhub@latest search compartment
```

---

## MCP

**Status:** ✅ Available — this is the agent surface

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/MaxFreedomPollard/Compartment |
| **Transport** | stdio (`compartment serve`) |
| **Compatible Clients** | Any of the 28 `integrate` targets + generic MCP hosts |
| **Tools (upstream)** | `memory_store` / `memory_store_many`, recall, `memory_recent`, `memory_link` / `memory_relations`, expire, supersede |

While the vault is locked, tools no-op (hooks always exit 0 so they cannot break the editor).

---

## What It Does

Compartment is an **encrypted, fully offline** memory vault for AI agents. Official docs: one claim per memory (hard 200-character / no-list rule), required `source` + `discovered` date, optional `expires`, opinions that supersede rather than duplicate, hybrid vector+keyword recall (~12 ms) over an in-memory index, and a hash-chained audit log. Embeddings are a bundled ONNX model; **no LLM inside**, **CI-enforced no network**. Vectors are encrypted at rest; only the passphrase opens the vault.

A new vault includes ~6,700 reference facts (toggle-able). Capture does not depend on the model calling a tool: the Claude hook writes memory files even if the host’s system prompt overrides tool instructions.

Distinct from [Claude-Mem](claude-mem.md) / [agentmemory](agentmemory.md): Compartment’s differentiator is **offline + encryption + one-claim discipline**, not session compression or a shared unencrypted server.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README/site H1: **"Encrypted, fully offline memory for AI agents."** — [Compartment](https://maxfreedompollard.github.io/Compartment/), [repo](https://github.com/MaxFreedomPollard/Compartment) |
| **Agent-specific primitive** | One-claim memories with source/date; opinion supersede; MCP store/recall; hook capture that cannot be overridden by a host system prompt |
| **Autonomy-compatible control plane** | After unlock + `integrate`, MCP store/recall runs without the GUI. Auto-lock is a safety timer, not a per-write approval |
| **M2M integration surface** | `compartment` CLI, `compartment serve` MCP, plugin marketplace, 28-client `integrate` |
| **Identity / delegation** | **C5-local / passphrase:** the vault secret is the operator passphrase (+ optional 2FA/keyfile). Memories record `source`; dashboard shows per-agent counts. Recalled text is wrapped as data (not instructions); `quarantined` adds a warning. No minted KYA token — unlock is authorization |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Encrypted vault** | `memory.vault` under `.compartment`; vectors encrypted |
| **One-claim memory** | `max_memory_chars` (200); lists/headings rejected |
| **Source + discovered** | Required provenance clause on every record |
| **Opinion supersede** | Replace-in-place with audit pointer; facts accumulate |
| **`expires`** | Date or duration; swept by `compartment expire` |
| **`memory_link`** | Deterministic subject–predicate–object graph |
| **MCP `serve`** | Agent read/write while unlocked |
| **Hook capture** | PostToolUse write path independent of the model |

---

## Autonomy Model

```
pip install compartment → compartment init → unlock → integrate <agent>
    -> Agent calls MCP store/recall (or the Claude hook writes files)
    -> Opinions supersede; facts accumulate; expiry sweeps stale claims
    -> Next session / next MCP client on this machine uses the same vault
    -> Lock (or auto-lock) seals the file; agents no-op until unlock
```

---

## Identity and Delegation Model

- **Unlock = capability:** passphrase (and optional 2FA) opens the vault for every integrated agent on the machine.
- **Attribution:** `source` / `discovered` on each claim; per-agent dashboard counts.
- **Data vs instructions:** recall is wrapped; `quarantined` sources are warned.
- **Honest C5:** shared machine vault, not per-agent OAuth. Do not treat the GUI connect buttons as a KYA layer.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `compartment init`, `serve`, `integrate`, `unlock`/`lock`, `audit verify` |
| MCP | `compartment serve` (stdio) |
| Plugin | Claude Code / Codex marketplace |
| GUI / dashboard | Secondary; 127.0.0.1 read-only map |
| Packs | `compartment pack` / `setup airgap-bundle` |

---

## Human-in-the-Loop Support

Unlock, passphrase change, and 2FA are operator actions. The dashboard is read-only. Opinion-overlap audit (`compartment opinions audit`) can be manual. Store/recall after unlock does not need a click.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **@modelcontextprotocol/server-memory** | Plaintext `memory.jsonl`, substring search, no encryption |
| **Claude-Mem / agentmemory** | Local but not CI-enforced offline + encrypted vectors + one-claim store |
| **Hosted mem0 / cloud memory** | Network + API keys — fails the offline contract |
| **The Compartment GUI alone** | Operator panel; without MCP it would not be agent-native |

---

## Use Cases

- **Air-gapped agents** — memory never leaves the machine (CI-enforced)
- **Encrypted shared vault** — several MCP clients, one passphrase
- **Preference updates** — opinions supersede; facts stay in the audit chain
- **Time-bounded secrets** — door codes / sale prices with `expires`
