# ProofFetch

> **"Web pages your agent can quote."**

| | |
|---|---|
| **Website** | https://prooffetch.steellantern.com |
| **Docs** | https://prooffetch.steellantern.com/llms.txt (agent guide) · https://prooffetch.steellantern.com/connect · https://prooffetch.steellantern.com/openapi.json |
| **Offer (JSON for agents)** | https://prooffetch.steellantern.com/offer |
| **MCP** | https://prooffetch.steellantern.com/mcp |
| **Verifier (open source, MIT)** | https://github.com/equinoxaifinance-rgb/prooffetch-verify |
| **Classification** | `agent-native` |
| **Category** | [Search & Web Intelligence Services](README.md) |
| **Disclosure** | Submitted by the founder of Steel Lantern, which makes and sells ProofFetch. |

---

## Official Website

https://prooffetch.steellantern.com

---

## Official Repo

The hosted ProofFetch service is **closed-source**; there is no public repository for the service itself yet.

The receipt verifier is open source (MIT): https://github.com/equinoxaifinance-rgb/prooffetch-verify. It recomputes ProofFetch's fingerprints from the page bytes on your own machine, without contacting ProofFetch, and its text cleanup code ([`normalize.mjs`](https://github.com/equinoxaifinance-rgb/prooffetch-verify/blob/main/normalize.mjs)) shows exactly what is hashed.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** remote MCP + REST, with an `llms.txt` agent guide.

```
# Agent guide:
Read https://prooffetch.steellantern.com/llms.txt and follow the instructions.

# MCP (Claude Code):
claude mcp add --transport http proof-fetch https://prooffetch.steellantern.com/mcp

# REST: get a free key (1,000 extractions, shown once), then fetch a page
POST https://prooffetch.steellantern.com/v1/keys/free
POST https://prooffetch.steellantern.com/v1/evidence   (Authorization: Bearer <key>; body: url, idempotencyKey)
```

The free preflight (`GET`/`POST /v1/preflight`, MCP tool `proof_fetch_preflight`) needs no key.

---

## Agent Skills

**Status:** ⚠️ Not yet published

Search community skills: `npx clawhub@latest search prooffetch`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available (hosted remote server)

| Detail | Value |
|---|---|
| **Endpoint** | `https://prooffetch.steellantern.com/mcp` |
| **Transport** | Remote HTTP (JSON-RPC over `POST /mcp`, protocol `2025-06-18`) |
| **Tools** | `proof_fetch_preflight` (free, no auth) · `proof_fetch_offer` (describes the paid offer, buys nothing) · `proof_fetch_evidence` (full extraction; listed only when the client sends a ProofFetch key as a request header) |
| **Auth** | None for the two discovery tools; ProofFetch key header for `proof_fetch_evidence` |
| **Compatible Clients** | Claude Code and other MCP clients that support remote HTTP servers |

---

## What It Does

ProofFetch fetches one public web page or text-layer PDF and returns it as **numbered, citable paragraphs** (`p1`, `p2`, …) so an agent can quote a specific paragraph by ID. Each response keeps the fetch time and two SHA-256 fingerprints: `rawSha256` over the exact bytes the server sent and `contentSha256` over the cleaned text.

Every fetch also runs a deterministic **hidden-instruction (prompt-injection) scan** and returns each match with its excerpt. A flag is a warning to review, not a safety guarantee; the text stays as the page had it.

Anyone can check a response with the open-source verifier, which recomputes both fingerprints from the page bytes and confirms every paragraph comes from that text in order. The service reads public resources only: no cookies, credentials, browser actions, JavaScript rendering, or private networks.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Page title "ProofFetch — cited web pages for AI agents"; tagline "Web pages your agent can quote." — https://prooffetch.steellantern.com. Agent card: "Evidence-bearing public web extraction for autonomous agents." — https://prooffetch.steellantern.com/.well-known/agent-card.json |
| **Agent-specific primitive** | Paragraph-addressable evidence (`p1`, `p2`, …) with `rawSha256` / `contentSha256` receipts and a deterministic prompt-injection indicator scan on every fetch, built for a model to cite and for the agent's output to be checked later. |
| **Autonomy-compatible control plane** | An agent can get a free key with `POST /v1/keys/free` (1,000 extractions, no card), or pay $0.50 per request through Stripe MPP and receive a key for 49 more extractions, with no account or dashboard step. Caller-generated idempotency keys allow safe retries for 7 days without double charges; 20 requests a minute per key; a 402 response points to the paid pack when credits run out. |
| **M2M integration surface** | Remote MCP server (`/mcp`), REST API with OpenAPI (`/openapi.json`), machine-readable offer (`/offer`), `llms.txt` agent guide, A2A-style agent card (`/.well-known/agent-card.json`). |
| **Identity / delegation** | **Partial, stated plainly:** ProofFetch only reads public pages and takes no action on a user's behalf beyond the fetch. Access is per key; there is no separate per-agent identity or delegated-permission model. Each response's receipt is the audit artifact and can be verified independently. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Cited evidence** (`POST /v1/evidence`, MCP `proof_fetch_evidence`) | One public URL in; numbered paragraphs, fetch time, `rawSha256`, `contentSha256`, provenance metadata and injection indicators out |
| **Batch evidence** (`POST /v1/evidence/batch`) | Up to 10 URLs per call, fetched 5 at a time |
| **Free preflight** (`/v1/preflight`, MCP `proof_fetch_preflight`) | Checks whether a source can be extracted, with no key and no charge |
| **Prompt-injection indicators** | Deterministic scan on every fetch; each match returned with its excerpt as a warning |
| **Offline receipt verification** | `npx github:equinoxaifinance-rgb/prooffetch-verify response.json page.html` recomputes both fingerprints and checks paragraph order |

---

## Autonomy Model

1. Agent reads `https://prooffetch.steellantern.com/llms.txt` (or connects to the MCP server).
2. Agent calls the free preflight to confirm the source is extractable.
3. Agent gets a free key with `POST /v1/keys/free`, or pays per request through Stripe MPP.
4. Agent calls `/v1/evidence` with the URL and an idempotency key; a credit is used only when extraction succeeds.
5. Agent quotes paragraph IDs in its answer, keeps the fingerprints, and reviews any injection flags before acting on the text.
6. Anyone downstream can re-check the response with the open-source verifier.

---

## Identity and Delegation Model

- Access is by bearer key (`Authorization: Bearer <key>`); one key can serve an agent and the owner's own code.
- No per-agent identity or delegated-permission model; the service is read-only over public URLs.
- Free keys: one per network per month, with a daily issuance cap.
- Audit trail: each response carries fetch time and SHA-256 receipts that can be verified without trusting ProofFetch.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | `/v1/preflight`, `/v1/evidence`, `/v1/evidence/batch`, `/v1/credits`, `/v1/keys/free` — OpenAPI at `/openapi.json` |
| MCP | Remote HTTP at `/mcp`; 3 tools |
| Payments | Stripe MPP pay-per-request ($0.50 for 50 pages); card packs (500 / 5,000 / 25,000 / 100,000 extractions) |
| Agent discovery | `llms.txt`, `/offer` JSON, A2A-style agent card at `/.well-known/agent-card.json` |
| Verifier | Open-source Node.js CLI and library (MIT), no dependencies |

---

## Human-in-the-Loop Support

None required for preflight, free keys, pay-per-request, or extraction. Injection indicators are returned to the agent as warnings, so a calling agent or its operator can route flagged pages to human review.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Plain HTTP fetch / scraping API** | Returns raw HTML for any client; no paragraph-level citation, no injection scan before the text reaches a model, no verifiable receipt of what was fetched |
| **Reader-style markdown converters** | Return clean text for an LLM, but not paragraph IDs bound to SHA-256 receipts that a third party can recompute offline |

---

## Use Cases

- **Cited answers** — an agent quotes paragraph `p7` of a source and keeps the fingerprints so the quote can be checked later
- **Injection-aware browsing** — an agent sees hidden-instruction matches before it acts on fetched text
- **Evidence trails** — research, compliance or support agents store receipts that anyone can re-verify without the vendor
