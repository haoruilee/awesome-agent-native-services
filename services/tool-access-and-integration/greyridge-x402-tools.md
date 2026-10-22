# Grey Ridge x402 Tools

> **"Vet an MCP server before your agent trusts it."**

| | |
|---|---|
| **Website** | https://x402-data-api.sigrunner.workers.dev/ |
| **Docs** | https://github.com/rezearcher/greyridge-x402-tools |
| **GitHub** | https://github.com/rezearcher/greyridge-x402-tools |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/rezearcher/greyridge-x402-tools?style=social)](https://github.com/rezearcher/greyridge-x402-tools) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **License** | MIT |

---

## Official Website

https://x402-data-api.sigrunner.workers.dev/

---

## Official Repo

https://github.com/rezearcher/greyridge-x402-tools

---

## How to Use (Agent Onboarding)

```bash
# Keyless CLI, no install — scan any MCP server's advertised tools before trusting them.
# (the package ships multiple bins, so -p selects mcpscan)
npx -y -p github:rezearcher/greyridge-x402-tools#v0.3.0 mcpscan https://mcp.deepwiki.com/mcp

# Coding-time Skill / Claude Code plugin:
/plugin marketplace add rezearcher/greyridge-x402-tools
```

The CLI exit code is the machine contract: `0` = clear, `1` = review, `2` = block, `3` = scan could not run (**fails closed**, so a broken scan never silently passes an admission gate).

---

## Agent Skills

**Status:** ✅ Available

```bash
/plugin marketplace add rezearcher/greyridge-x402-tools
```

| Skill | What It Teaches the Agent |
|---|---|
| `mcp-scan` | How to statically scan an MCP server's advertised tools for prompt-injection / tool-poisoning before enabling them, and how to read the clear/review/block verdict. |

---

## MCP

**Status:** ✅ MCP-aware scanner, plus a hosted MCP server entry.

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/rezearcher/greyridge-x402-tools |
| **Transport** | stdio (CLI scanner) · Streamable HTTP (hosted endpoints) |
| **Compatible Clients** | Claude Code / Claude Desktop, Cursor, any MCP client |

The scanner connects to a target MCP server over Streamable HTTP, reads its advertised `tools/list` (names, descriptions, JSON schemas) without authenticating, and checks each tool for agent-specific risk. The service is also published to the Model Context Protocol registry under `io.github.rezearcher`.

---

## What It Does

Grey Ridge x402 Tools gives an autonomous agent two preflight gates it can call on its own before it takes an irreversible action.

The first is **mcpscan**: every tool an MCP server advertises runs inside the agent's context — its name, description and JSON schema are read by the model — so a poisoned or injection-laden tool description can steer the agent before any tool is ever invoked. `mcpscan` statically scans a server's advertised tools for prompt-injection and tool-poisoning patterns (OWASP LLM01 / LLM08), returns a clear/review/block verdict, and is usable as a CI admission gate or an in-loop check.

The second is a **pre-trade token gate** for agents acting on Base: given a token address, it runs a live `eth_call` state-override transfer simulation (can a synthetic wallet actually sell the token?) plus a proxy/mint/pause/blacklist/fee-setter selector scan and an owner-renounce check, and returns `allow` / `review` / `block`. Both gates expose a free, keyless preview and a paid itemized endpoint settled per call in USDC over x402 on Base — no account and no API key.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "Agent-native, pay-per-call data on Base (USDC via x402). No account, no API key — agents pay inline." (https://x402-data-api.sigrunner.workers.dev/llms.txt) |
| **Agent-specific primitive** | Scans the MCP `tools/list` metadata that only an agent's model consumes, and gates an autonomous swap step — neither has a human-facing equivalent. |
| **Autonomy-compatible control plane** | Keyless CLI + GitHub Action run non-interactively; the exit-code / verdict contract lets an agent block, review, or proceed with no human click. |
| **M2M integration surface** | CLI (`mcpscan`), GitHub Action admission gate, REST endpoints, and LangChain / CrewAI / ElizaOS integrations. |
| **Identity / delegation** | x402 settlement attaches the paying agent's own on-chain identity to each call; findings are attributable evidence for which tools are safe to delegate. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`mcpscan`** | Reads a target MCP server's advertised tools and flags prompt-injection / tool-poisoning (OWASP LLM01/LLM08). Keyless CLI; itemized findings paid per call. |
| **Pre-trade swap gate** | `allow`/`review`/`block` on a Base token from a live transfer simulation + proxy/mint/pause/blacklist/fee-setter scan. |
| **Fail-closed verdict contract** | Exit `0`/`1`/`2`/`3` (clear/review/block/could-not-run) so a broken scan never passes an admission gate. |
| **Free keyless preview** | `GET /scan/mcp/preview?url=` and `GET /gate/swap/preview?token=` return a verdict with no wallet, so an agent can evaluate before paying. |

---

## Autonomy Model

1. Before enabling a newly discovered MCP server, the agent (or its CI gate) runs `npx -y -p github:rezearcher/greyridge-x402-tools#v0.3.0 mcpscan <url>`.
2. The scanner reads the server's advertised tools over Streamable HTTP and returns a verdict + exit code.
3. On `block` (exit 2) or scan failure (exit 3, fails closed) the agent refuses to enable the server; on `clear` it proceeds — no human in the loop.
4. Before an autonomous swap, the agent calls the pre-trade gate; `block` halts the trade, `allow` lets the loop continue.
5. Itemized paid calls settle inline in USDC over x402 — the agent pays per call with no account setup.

---

## Identity and Delegation Model

- x402 payment binds each paid call to the agent's own wallet identity on Base, separate from any end user.
- Scan findings are machine-readable, attributable evidence of which tools / servers were inspected and why they were allowed or blocked.
- The service validates the artifacts an agent is about to delegate to; it does not itself mint runtime auth for other services.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `npx -y -p github:rezearcher/greyridge-x402-tools#v0.3.0 mcpscan <mcp-url>` — keyless, fails closed |
| GitHub Action | `uses: rezearcher/greyridge-x402-tools@v0.3.0` — admission gate on every push |
| REST API | `GET /scan/mcp`, `GET /scan/mcp/preview?url=`, `GET /gate/swap`, `GET /gate/swap/preview?token=` |
| Framework adapters | LangChain, CrewAI, ElizaOS (`CHECK_BASE_TOKEN`) |
| Payments | x402 / USDC on Base, inline per call |

---

## Human-in-the-Loop Support

The `review` verdict (exit 1) is the explicit hand-back-to-human signal for borderline cases; `clear` and `block` are designed to be acted on autonomously. Scans otherwise run unattended in CI or an agent loop.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Traditional SAST / dependency scanners** | Inspect source and packages, not MCP tool descriptions, prompts, or tool-call semantics read by the model. |
| **A generic data API behind a paywall** | Would be callable unchanged by a human product; the agent-specific value here is the MCP tool-metadata scan and the autonomous verdict/exit-code contract. |
| **Manual MCP review** | Does not scale across dynamically discovered servers or run as a non-interactive admission gate in an agent loop. |

---

## Use Cases

- **MCP admission gate** — scan a newly discovered MCP server before an agent enables its tools.
- **CI preflight** — fail a build when an MCP server or published skill carries injection/poisoning risk.
- **Pre-trade safety** — gate an autonomous Base swap on a live honeypot/rug check.
- **Keyless evaluation** — an agent runs the free preview to decide before spending any USDC.
