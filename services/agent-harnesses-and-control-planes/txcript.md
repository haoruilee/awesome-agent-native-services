# txcript

> **"Continue your conversation in another coding agent."**

| | |
|---|---|
| **Website** | https://github.com/skillsynchq/txcript |
| **Docs** | https://github.com/skillsynchq/txcript/blob/main/docs/usage.md |
| **Product (related)** | https://skillsync.com |
| **GitHub** | https://github.com/skillsynchq/txcript |
| **Classification** | `agent-native` |
| **Category** | [Agent Harnesses & Operator Surfaces](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Launch HN 2026-09-17 ([item 49743049](https://news.ycombinator.com/item?id=49743049)); OSS core of Skillsync |
| **Verified at** | 2026-09-20 |

---

## Official Website

https://github.com/skillsynchq/txcript

Related commercial surface (honest, not this listing's name): [Skillsync](https://skillsync.com) — homepage line *"Own your context"*. Skillsync is a local-first desktop product that uses txcript as its conversion engine. This catalog entry lists the Apache-2.0 library / CLI / MCP core as **txcript**, not the closed Skillsync app.

---

## Official Repo

https://github.com/skillsynchq/txcript

Apache-2.0. Rust library, CLI (`txcript-cli`), and JavaScript / WASM package `txcript`.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + stdio MCP (read-only session tools)

Install a release binary from [GitHub Releases](https://github.com/skillsynchq/txcript/releases), or from source (Rust 1.96+):

```bash
cargo install --git https://github.com/skillsynchq/txcript txcript-cli --locked
```

Continue a Claude Code session in Codex:

```bash
txcript list --from claude_code
txcript continue <session-id> --with codex
```

`txcript continue` writes a new native session for the target harness and launches that harness in the recorded working directory. The source session is kept. The target agent must already be installed and signed in.

Read-only MCP for list / search / read:

```bash
txcript mcp
```

Library paths (no launch):

```bash
cargo add txcript
# or
npm install txcript
```

This is **not** URL Onboarding. txcript rewrites local harness session files; it does not register an agent identity at a hosted URL. Skillsync desktop is a separate commercial UI on top of the same engine.

---

## Agent Skills

**Status:** ⚠️ Not yet published as an official `npx skills add` pack.

Search community skills: `npx clawhub@latest search txcript skillsync`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available (stdio, read-only)

```bash
txcript mcp
```

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/skillsynchq/txcript |
| **Transport** | stdio |
| **Tools** | `list_sessions(from?, cwd?, limit?, offset?)`, `search_sessions(pattern, from?, cwd?)`, `read_session(id, from?)` |
| **Auth** | Local process; reads on-disk harness stores. Live Claude Chat / ChatGPT sources are never listed by `list_sessions`. |
| **Compatible Clients** | Claude Desktop, Claude Code, Cursor, Codex, and other stdio MCP hosts |

The MCP surface does not convert or launch a session. Use the CLI (`txcript continue`) or the library for writes.

---

## What It Does

txcript is a library for converting agent sessions — "Pandoc for AI chats" in the repository description. Start a conversation in Claude Code and continue it in Codex, Cursor, OpenCode, or another supported harness, carrying over messages, reasoning, and tool history where the target can represent them.

The CLI discovers local sessions, searches them, views or crops them, exports a harness-neutral **Simple** JSON document, and writes a native session the destination agent can resume. The Rust crate and npm WASM package expose the same canonical `Transcript` model so other tools can search, edit, or convert without re-implementing each on-disk format.

**Related product honesty:** Skillsync desktop (`https://skillsync.com`) markets portable, searchable context and a multiplayer UI. That app is not this listing. txcript is the OSS converter, CLI, and MCP session tools.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | *"Continue your conversation in another coding agent."* Source: [txcript README](https://github.com/skillsynchq/txcript). Also: *"txcript is a library for converting agent sessions."* Skillsync marketing ("Own your context") is a related commercial line, not the listed product name. |
| **Agent-specific primitive** | Canonical agent transcript (messages, reasoning, tool use/result, images, metadata) plus native load/save for each coding-agent harness. Ordinary chat export / copy-paste is not a typed harness codec. |
| **Autonomy-compatible control plane** | CLI and library convert and write sessions without a GUI. MCP is read-only by design. Constraints are the destination harness's own format limits and the operator's local files. |
| **M2M integration surface** | `txcript` CLI, `txcript mcp` stdio server, Rust crate, npm WASM package. See [usage](https://github.com/skillsynchq/txcript/blob/main/docs/usage.md). |
| **Identity / delegation** | Sessions keep source harness identity and working directory; conversion writes a **copy** and never modifies or deletes the source. Destination supplies its own system instructions and tools. No hosted txcript account. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Harness codec** | Read/write a coding agent's native session text (`claude_code`, `codex`, `opencode`, `cursor`, `cursor_desktop`, and others) |
| **Canonical transcript** | Shared model: messages, thinking, tool pairs, images, metadata, usage |
| **continue / resume** | Write a native session for a target harness and optionally launch it |
| **Simple document** | Harness-neutral JSON interchange (`txcript export`) for moving work between machines |
| **Session search** | CLI `query` and MCP `search_sessions` over local history |

Supported read/continue matrix is in the [README agent table](https://github.com/skillsynchq/txcript). Some sources are read-only (for example Hermes, Amp, live Claude Chat / ChatGPT).

---

## Autonomy Model

```
Operator has one or more coding-agent harnesses installed locally
    ↓
txcript list / query (or MCP list_sessions / search_sessions) finds a session
    ↓
txcript continue <id> --with <harness> writes a native copy and launches the target
    ↓
Target agent resumes conversation history; it supplies its own tools and system prompt
    ↓
Source session remains untouched
```

Project files are not packaged by conversion; they must already exist on the machine that continues the session. MCP tools stop at read/search.

---

## Identity and Delegation Model

- **Session identity** — each record belongs to a source harness and session id; `--from` scopes lookup.
- **Copy-on-continue** — cross-harness writes are always a new session; the source is never rewritten or removed.
- **Destination authority** — the target harness's own login, tools, and sandbox apply after launch. txcript does not mint those credentials.
- **MCP boundary** — list / search / read only. An MCP client cannot convert or resume through the server.
- **Live-account sources** — Claude Chat and ChatGPT reuse an existing app login and private web APIs; they are explicit opt-in `--from` sources, not default discovery.
- **Skillsync desktop** — commercial UI that can sit on this engine; not an agent identity provider for this listing.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `txcript list`, `continue` / `resume`, `query`, `view`, `crop`, `export`, `mcp` |
| stdio MCP | Read-only session tools |
| Rust crate | `txcript` — codecs, stores, search — https://docs.rs/txcript |
| npm / WASM | `npm install txcript` — in-memory convert / search |
| Simple JSON | Interchange document for agents without a native adapter |
| Skillsync desktop | Related commercial product at https://skillsync.com — not the listed interface |

---

## Human-in-the-Loop Support

Interactive `txcript crop` and `txcript query` pickers are optional operator tools. Conversion and `continue` can run non-interactively. MCP is read-only, so a connected agent can inspect history without mutating it. There is no hosted approval queue; the destination harness keeps its own HITL.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Copy-paste a chat into another CLI** | Loses typed tool pairs, reasoning blocks, and native resume metadata |
| **Generic JSONL / log shipper** | Does not implement per-harness codecs or `continue --with` |
| **Memory store (Mem0, Zep, …)** | Extracts facts; does not rewrite a Codex/Claude Code/Cursor session the target can `/resume` |
| **Skillsync desktop alone** | Commercial UI; this listing is the OSS converter. Desktop without txcript would be an operator app, not the M2M core |

**Category note:** Memory & State in this catalog expects self-managing memory lifecycle (extract / conflict / evict). txcript is harness-session portability, so it sits with Agent Harnesses & Operator Surfaces.

---

## Use Cases

- **Switch harness mid-task** — start in Claude Code, continue in Codex without re-explaining
- **Search local agent history** — `txcript query` or MCP `search_sessions` across every supported store
- **Move a run between machines** — `export` a Simple document, then `continue ./run.json --with claude_code`
- **Build a viewer or editor** — use the Rust or WASM API against one transcript model
