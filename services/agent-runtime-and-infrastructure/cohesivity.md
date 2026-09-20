# Cohesivity

> **"backend infra your agents can actually use."**

| | |
|---|---|
| **Website** | https://cohesivity.ai |
| **Docs** | https://cohesivity.ai/llms.txt · https://cohesivity.ai/docs |
| **GitHub** | https://github.com/cohesivity-org/cohesivity-plugin |
| **Skill source** | https://github.com/cohesivity-org/cohesivity-skill · https://cohesivity.ai/skill.md |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure](README.md) |
| **Related issue** | https://github.com/haoruilee/awesome-agent-native-services/issues/133 |
| **Admission** | Standard track — **Go with disclosure** (soft criterion 5; docs MCP vs mutating MCP; `confirmed:true`) |

---

## Official Website

https://cohesivity.ai

Live homepage H1 (2026-09-20): **"backend infra your agents can actually use."** Supporting copy also says the product is "on-the-fly infra, purpose-built for ai agents."

Ephemeral tenants expire in 72 hours, have no account and no payment method, and claiming, subscriptions, and top-ups each require human consent.

---

## Official Repo

https://github.com/cohesivity-org/cohesivity-plugin — Agent Skill plus local stdio MCP (`cohesivity-local`) and configuration for the remote management MCP.

Canonical skill bytes: https://github.com/cohesivity-org/cohesivity-skill (also served at https://cohesivity.ai/skill.md).

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI`

Pinned installer (creates or reuses a 72-hour ephemeral tenant and writes `.cohesivity`):

```bash
npx --yes @cohesivity/init@0.8.3
```

Plugin-aware shell quickstart (same job when Node is available to the script):

```bash
curl -fsSL https://cohesivity.ai/quickstart.sh | bash
```

Claude Code marketplace path from the plugin README:

```text
claude plugin marketplace add cohesivity-org/cohesivity-plugin
claude plugin install cohesivity@cohesivity
```

Standalone skill without plugin/MCP:

```bash
npx skills add cohesivity-org/cohesivity-skill -g
```

**MCP split (do not collapse these):**

1. **Public `https://cohesivity.ai/mcp`** — docs-oriented, no login. Live `initialize` on 2026-09-20 returned `serverInfo.name: cohesivity-docs` with instructions: "This server is read-only. Use get_cohesivity_documentation…" Discovery: https://cohesivity.ai/.well-known/mcp.json (`ai.cohesivity/docs`).
2. **Mutating MCP** — local stdio `cohesivity-local` from the plugin (`mcp/project-bootstrap.mjs`) using `.cohesivity`, or remote Streamable HTTP at https://cohesivity.ai/mcp/manage (OAuth / guest). Tools: `create_tenant`, `claim_tenant`, `tenant_status`, `provision_resource`, `give_feedback`.

Creating, claiming, and provisioning require literal `confirmed: true`. The skill permits that flag only when the **current user request** explicitly authorizes that exact action. That agent-attested authorization is the catalog autonomy bar for this entry (approval gates are allowed).

---

## Agent Skills

**Status:** ✅ Available

```bash
npx skills add cohesivity-org/cohesivity-skill -g
```

Live copy: https://cohesivity.ai/skill.md

| Skill | What It Teaches the Agent |
|---|---|
| `cohesivity` | Consent rules, `.cohesivity` credentials, control vs data plane, MCP tool split, claim/billing gates, and when to fetch live offering docs |

---

## MCP

**Status:** ✅ Available — **two different servers**

| Detail | Public docs MCP | Mutating management MCP |
|---|---|---|
| **URL / launch** | https://cohesivity.ai/mcp | Local stdio `cohesivity-local` (plugin) or https://cohesivity.ai/mcp/manage |
| **Transport** | Streamable HTTP (`GET` 405) | stdio (local) / Streamable HTTP + OAuth (hosted) |
| **Auth** | None | Project `.cohesivity` management key (local) or OAuth/guest (hosted) |
| **Role** | Read-only documentation (`cohesivity-docs`) | Tenant create/claim/status/provision/feedback |
| **Mutations** | None | `confirmed: true` required for create, claim, provision |

Do not list public `/mcp` as the provisioning surface. Discovery for the docs server: https://cohesivity.ai/.well-known/mcp.json.

---

## What It Does

Cohesivity is on-the-fly backend infrastructure for coding agents: one managed API for a project's databases, auth, hosting, storage, inbox, browser sessions, and AI/search APIs. The agent provisions an ephemeral project tenant without separate vendor accounts. Provider keys stay server-side; the app calls Cohesivity's edge. Humans claim the tenant if they want to keep it past 72 hours.

**Dual-use honesty:** Postgres, object storage, and similar offerings are ordinary application primitives. This listing covers the agent-facing tenant bootstrap, inbox, MCP/skill surface, and consent model — not a claim that every endpoint is exclusively agent-specific.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Live H1: *"backend infra your agents can actually use."* — [cohesivity.ai](https://cohesivity.ai). Skill: "Cohesivity is on-the-fly infrastructure, purpose-built for AI agents." — [cohesivity.ai/skill.md](https://cohesivity.ai/skill.md) |
| **Agent-specific primitive** | Agent-provisioned **ephemeral project tenant** (no signup) plus an **agent-native inbox** (`<tenant_id>@inbox.cohesivity.app`) whose composer/mutation path is API/agent, not a human mailbox UI. Underlying DB/storage APIs remain ordinary. — [inbox offering](https://cohesivity.ai/offerings/inbox) · [llms.txt](https://cohesivity.ai/llms.txt) |
| **Autonomy-compatible control plane** | After a provisioned tenant exists, reads and already-authorized work proceed over HTTP/MCP without a dashboard click per call. Mutations use fail-closed MCP: `confirmed: true` is **agent-attested authorization from the current user request**, not a hosted human click per SQL query. Claim, subscriptions, top-ups, and paid/durable gates stay human. Approved on [#133](https://github.com/haoruilee/awesome-agent-native-services/issues/133) as meeting criterion 1.3 with that disclosure. |
| **M2M integration surface** | Management HTTP (`/api/*`), edge HTTP (`/edge/*`), local stdio MCP, hosted `/mcp/manage`, published skill, `@cohesivity/init`. Public `/mcp` is documentation only. |
| **Identity / delegation (soft)** | Credentials are **project/tenant-scoped** (`coh_man_*` / `coh_app_*` in `.cohesivity`). Hosted OAuth checks account ownership (or guest-created ephemeral tenants) per call. Local MCP records caller attribution. This is **not** a strong independently verified per-agent identity or a full per-agent delegation/audit model. Disclose that softness; it was accepted with the Go. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Ephemeral project tenant** | 72-hour no-signup tenant written to `.cohesivity` |
| **Management / application keys** | Tenant-scoped `coh_man_*` (control plane) and `coh_app_*` (data plane) |
| **Resource provision** | `POST /api/resources` for postgres, inbox, hosting, storage, AI APIs, and other offerings |
| **Agent inbox** | Canonical `<tenant_id>@inbox.cohesivity.app`; send/list/reply via edge API |
| **`confirmed: true`** | Agent-attested authorization for create/claim/provision MCP tools |
| **Claim approval URL** | `POST /api/claim/url` → human `approval_url`; agent polls `/api/wait` |

---

## Autonomy Model

1. With explicit authorization in the current request, bootstrap via `create_tenant` (`confirmed: true`) or `@cohesivity/init@0.8.3`.
2. Reuse `.cohesivity` across sessions. Do not mint a new tenant when one is valid.
3. Provision offerings (`provision_resource` with `confirmed: true`, or `POST /api/resources`).
4. The app calls `/edge/*` with the application key from a server tier. Quota and hard caps constrain the tenant.
5. Claim, plan upgrades, and top-ups mint a human `approval_url` / checkout URL. The agent does not complete those gates itself.
6. `give_feedback` may run without `confirmed` once tenant context exists; exclude secrets and personal data.

Fail-closed: do not pass `confirmed: true` unless the current user request authorized that exact action.

---

## Identity and Delegation Model

- **Soft criterion 5:** identity is the **project/tenant credential pair**, not a cryptographically distinct agent principal with a catalog-grade delegation ledger.
- Hosted MCP re-checks account ownership or the guest's own still-ephemeral tenant on each mutating call.
- Local MCP never prints `coh_*` keys; hosted `create_tenant` may return a secret-bearing `credentials_file` that the agent must write to `.cohesivity` (mode `0600`) and not echo in chat.
- Audit is tenant/account activity and `/api/observability` for claimed tenants, not a per-agent KYA token.
- Humans own claim, billing, and durable account state.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Homepage | https://cohesivity.ai |
| Agent docs | https://cohesivity.ai/llms.txt · https://cohesivity.ai/llms-full.txt · https://cohesivity.ai/skill.md |
| Management API | `https://cohesivity.ai/api/*` with `Authorization: Bearer <coh_management_key>` |
| Edge / data plane | `https://cohesivity.ai/edge/*` with application key (server-side only) |
| Docs MCP | https://cohesivity.ai/mcp — read-only |
| Mutating MCP | Plugin local stdio; https://cohesivity.ai/mcp/manage |
| Installer | `npx --yes @cohesivity/init@0.8.3` |
| Plugin | https://github.com/cohesivity-org/cohesivity-plugin |

---

## Human-in-the-Loop Support

Claim, subscriptions, top-ups, and paid/durable gates require a human approval or checkout URL. MCP create/claim/provision require `confirmed: true` tied to the current user request. The account page is read-oriented (billing and activity); composing inbox mail stays on the agent/API path. Humans are in the loop for keeping the project and spending money, not for every permitted edge call after provision.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Conventional cloud signup (AWS/GCP/Supabase console)** | A human creates vendor accounts and pastes keys. Cohesivity's first tenant is agent-bootstrapped and ephemeral. |
| **Generic BaaS REST API** | Same database primitives without the agent tenant, skill/MCP consent model, or agent inbox. |

The consent gates above are intentional and disclosed; they do not make this a human-first builder studio.

---

## Use Cases

- **Prompt-to-backend** — provision postgres/hosting/auth from a coding-agent session without sending the user through vendor consoles.
- **Agent inbox** — give the project `<tenant_id>@inbox.cohesivity.app` and operate mail over the edge API.
- **Prototype then claim** — build on a 72-hour tenant; hand the human an `approval_url` only if they want to keep it.
- **Docs lookup** — use public `/mcp` (`cohesivity-docs`) to fetch current offering contracts without mutating anything.
