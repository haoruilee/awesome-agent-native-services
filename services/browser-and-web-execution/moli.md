# Moli

> **"Moli is a production-ready, structured-first browser engine for AI agents."**

| | |
|---|---|
| **Website** | https://browser.lexmount.com |
| **Docs** | https://github.com/lexmount/moli#readme |
| **GitHub** | https://github.com/lexmount/moli |
| **Stars** | [2,403 stars (snapshot: 2026-09-26)](https://github.com/lexmount/moli) |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution](README.md) |
| **Latest-month signal** | [v1.1.10](https://github.com/lexmount/moli/releases/tag/v1.1.10) released 2026-09-24; 2,403 stars; both `LICENSE-APACHE` and `LICENSE-MIT` are present (GitHub SPDX Apache-2.0); [browser.lexmount.com](https://browser.lexmount.com) returned HTTP 200 on 2026-09-26 with title "Lexmount Browser" ([repo metadata](https://api.github.com/repos/lexmount/moli)) |
| **Verified at** | 2026-09-26 |
| **Status** | Open-source engine; Apache-2.0 or MIT at the user's option; managed Lexmount Browser control plane is separate |

---

## Official Website

https://browser.lexmount.com

On 2026-09-26 the page title was **"Lexmount Browser - Cloud Browser Infrastructure for AI Agents"**. The repository README H1 is still **Moli**. The status row already separates the open-source engine from the managed Lexmount control plane.

---

## Official Repo

https://github.com/lexmount/moli

---

## How to Use (Agent Onboarding)

Build the browser from the official Rust workspace, then use either its extraction CLI or automation server:

```bash
cargo build --release -p moli

./target/release/moli fetch \
  --dump semantic_tree_text \
  --wait-selector body \
  https://example.com

./target/release/moli serve

# Or expose Moli's first-party MCP server over stdio:
./target/release/moli mcp
```

Use `moli serve --layout` when the agent needs real geometry, coordinate input, screenshots, or screencast surfaces; add `--resource` only when optional image, font, audio, video, media, and text-track fetching is required.

---

## Agent Skills

**Status:** ⚠️ Not yet published by the project.

```bash
npx clawhub@latest search moli browser
```

See the [AgentSkills specification](https://agentskills.io/specification) to contribute one.

---

## MCP

**Status:** ✅ Available — the first-party stdio server and `moli mcp` command ship in the `v0.1.1` source/release. The command is not yet advertised in the top-level README, so treat this as an early, under-documented interface.

| Detail | Value |
|---|---|
| **MCP source** | [`moli/src/mcp_server.rs` at `v0.1.1`](https://github.com/lexmount/moli/blob/v0.1.1/moli/src/mcp_server.rs) |
| **Command / transport** | `moli mcp` over stdio |
| **Protocol version announced by source** | `2024-11-05` |
| **Tools and resources** | Navigation, Markdown, links, evaluation, semantic trees, element queries/actions, plus page HTML/Markdown resources |
| **Compatible clients** | Any MCP host that can launch a local stdio command |

---

## What It Does

Moli is a Rust browser kernel built for agent workloads that usually need page structure rather than a continuously rendered visual world. It runs JavaScript, DOM, CSS, networking, browser storage, workers, and browser APIs by default, then computes real layout or software-rendered pixels only when an operation requests them.

Agents can extract HTML, Markdown, JSON, or compact semantic trees from the CLI, drive the same runtime through CDP and both WebDriver protocols, or launch the first-party stdio MCP server. Profiles, cookies, cache directories, proxies, network policies, timeouts, resource families, structured logging, and tracing are explicit operational controls rather than hidden browser defaults.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The official README calls Moli a ["structured-first browser engine for AI agents"](https://github.com/lexmount/moli#readme). |
| **Agent-specific primitive** | Semantic-tree and Markdown output, DOM-first execution, and on-demand layout/pixels minimize the visual work and tokens an agent does not need. |
| **Autonomy-compatible control plane** | Agents can fetch pages or operate a long-running automation server without a human browser window; profiles, resource policies, timeouts, proxies, and private-network rules bound operation. |
| **M2M integration surface** | CLI, a first-party stdio MCP server, CDP, WebDriver Classic, and WebDriver BiDi from one binary; Playwright connects directly over CDP. |
| **Identity / delegation** | Profile directories, cookie files, and storage scopes can isolate a delegated browser identity. This is a local deployment boundary: Moli does **not** claim built-in multi-tenant agent accounts or a signed per-agent audit log, so operators must enforce process, filesystem, and profile separation. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Semantic tree output** | Compact model-friendly page representation from the native browser runtime |
| **Structure-first execution** | Runs DOM, scripts, network, and storage without paying continuous layout/paint cost |
| **On-demand layout** | Builds real geometry only for bounding boxes, hit testing, coordinate input, screenshots, or screencast |
| **Explicit resource policy** | Enables visual/media resource families individually or together |
| **Browser profile** | Optional profile-scoped localStorage, IndexedDB, OPFS, cookies, and HTTP cache |
| **MCP browser session** | Stateful page navigation, extraction, evaluation, and element actions through standard MCP tools/resources |
| **Unified automation endpoint** | One process exposes CDP, WebDriver Classic, and WebDriver BiDi |
| **Structured diagnostics** | Network tracing, structured logs, waits, and explicit unsupported-path failures |

---

## Autonomy Model

1. The operator builds Moli and starts `moli serve` with the profile, proxy, private-network, resource, and rendering policies appropriate to the delegated task.
2. An agent connects over MCP, CDP, or WebDriver and creates/navigates pages.
3. Structure-only operations read the native DOM/runtime directly; geometry or pixel requests trigger an explicit layout/paint pass.
4. The agent consumes semantic trees, Markdown, JSON, DOM results, network observations, or screenshots.
5. The deployment retains only the profile/cache state explicitly configured. Unsupported protocol paths fail instead of returning a fabricated success.

---

## Identity and Delegation Model

- `--profile-dir`, `--cookie-file`, and `--http-cache-dir` opt a workload into persistent browser identity and state.
- Separate server processes and profile directories should be used for separate agents, users, or trust domains.
- Proxy, private-network, resource, connection, timeout, and user-agent controls bound what the delegated browser process can reach and consume.
- Moli delegates through local process and filesystem ownership; it does not document an application-level agent principal, role system, or credential broker.
- Structured logging and network traces support review, but they are not described as a complete or tamper-evident action audit. This boundary should remain explicit in multi-agent deployments.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **CLI fetch** | HTML, Markdown, JSON, semantic-tree, selector/script/response waits, profile and network controls |
| **CDP** | Browser automation and Playwright `connectOverCDP()` on the default server endpoint |
| **WebDriver Classic** | Standard WebDriver commands served by the same kernel and scheduler |
| **WebDriver BiDi** | Bidirectional browser automation on the same endpoint |
| **MCP stdio** | `moli mcp`; browser navigation, extraction, script evaluation, semantic-tree, wait, and element-action tools plus HTML/Markdown resources |
| **Screenshots / PDF / screencast** | Software-rendered visual surfaces under `--layout`, within the documented scope |

---

## Human-in-the-Loop Support

Moli is headless and has no native approval UI. An agent normally operates unattended through MCP or the browser protocols inside the policies chosen when its process starts. Human takeover, credential consent, or high-risk action approval must be supplied by the calling harness or managed Lexmount control plane; the open-source engine does not claim those features.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **General-purpose Chromium** | Continuously maintains a human-oriented rendered world even when an agent only needs DOM structure or semantic output. |
| **Plain HTTP scraper** | Cannot execute the real JavaScript, storage, worker, CSS, and browser API state that modern agent tasks depend on. |
| **Screenshot-only computer use** | Makes the model infer structure from pixels and lacks the direct semantic-tree/DOM path Moli uses by default. |

---

## Use Cases

- **High-volume web agents** — run DOM-first browsing episodes with lower visual compute overhead
- **Retrieval and crawling** — return Markdown or semantic trees after real JavaScript execution
- **Browser-agent evaluation** — expose one deterministic kernel through several standard automation protocols
- **Selective visual interaction** — pay for geometry or screenshots only on steps that need coordinates or pixels
- **Isolated local browser workers** — dedicate profiles and processes to agent tasks under OS-enforced boundaries
