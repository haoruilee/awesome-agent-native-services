# ClawHub

> **"Claw Hub: OpenClaw Skill Marketplace"**

| | |
|---|---|
| **Website** | https://claw-hub.net/ |
| **Docs** | https://github.com/openclaw/clawhub/tree/main/docs |
| **GitHub** | https://github.com/openclaw/clawhub |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/openclaw/clawhub?style=social)](https://github.com/openclaw/clawhub) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |

---

## Official Website

https://claw-hub.net/

---

## Official Repo

https://github.com/openclaw/clawhub — web app, Convex backend, shared HTTP/API schema (`packages/schema`), and the `clawhub` CLI (`npx clawhub@latest`).

---

## How to Use (Agent Onboarding)

**CLI — discover, install, update, and publish agent skills (`SKILL.md` packs) and OpenClaw package artifacts.**

```bash
npx clawhub@latest login
npx clawhub@latest search <topic>
npx clawhub@latest install <skill-slug>
npx clawhub@latest list
npx clawhub@latest update --all
```

Publish and versioning (authenticated): `clawhub skill publish`, `clawhub sync`, `clawhub skill rename`, `clawhub skill merge` — see [CLI docs](https://github.com/openclaw/clawhub/blob/main/docs/cli.md) and [quickstart](https://github.com/openclaw/clawhub/blob/main/docs/quickstart.md).

**China mirror (access acceleration):** [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com) — set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or pass `--registry https://cn.clawhub-mirror.com`.

---

## Agent Skills

**Status:** ✅ ClawHub is a **public registry of Agent Skills** (and related OpenClaw packages). Skills are installed with the CLI; this catalog’s companion skills live under [`.skills/`](https://github.com/haoruilee/awesome-agent-native-services/tree/main/.skills) and publish via ClawHub.

```bash
npx clawhub@latest install find-agent-service
npx clawhub@latest install evaluate-agent-native
npx clawhub@latest install add-to-awesome-list
```

Skill format and frontmatter (runtime requirements, OpenClaw metadata): [docs/skill-format.md](https://github.com/openclaw/clawhub/blob/main/docs/skill-format.md) — see also [agentskills.io/specification](https://agentskills.io/specification).

---

## MCP

**Status:** ⚠️ ClawHub is a **skill and package registry**, not an MCP server directory. Integration is via the **CLI and HTTP/registry APIs** (consumers are agent hosts that load `SKILL.md` and tooling, not MCP `tools/list`).

---

## What It Does

ClawHub is the **public skill marketplace for OpenClaw-style agents**: browse thousands of versioned **`SKILL.md`** bundles, run **embedding-based search**, install and update skills locally from the CLI, and **publish** new versions with changelogs and tags. It also hosts an **OpenClaw package catalog** (code and bundle plugins) with family/trust/capability metadata. The stack pairs a web UI with a **Convex-backed** API, **GitHub OAuth** for publishers, moderation workflows, and optional **install telemetry** (disable with `CLAWHUB_DISABLE_TELEMETRY=1` per [telemetry.md](https://github.com/openclaw/clawhub/blob/main/docs/telemetry.md)).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Site title and OG copy describe an **OpenClaw skill marketplace for AI agent skills** with vector search and versioning ([claw-hub.net](https://claw-hub.net/) HTML meta / OG). Repo README: **public skill registry** for **text-based agent skills** (`SKILL.md` + files), **CLI-friendly API** ([openclaw/clawhub README](https://github.com/openclaw/clawhub/blob/main/README.md)). |
| **Agent-specific primitive** | **Versioned skill artifact** with **`SKILL.md` frontmatter** declaring machine-oriented requirements (`requires.env`, `requires.bins`, OpenClaw/clawdbot metadata, optional nix plugin pointers) — a packaging model for **agent runtimes**, not a generic document store ([skill-format.md](https://github.com/openclaw/clawhub/blob/main/docs/skill-format.md), [spec.md](https://github.com/openclaw/clawhub/blob/main/docs/spec.md)). |
| **Autonomy-compatible control plane** | After **one-time GitHub login** for publish, agents and agent hosts use **CLI and API** for search, install, sync, and inspect without a human in the loop per operation ([CLI overview](https://github.com/openclaw/clawhub/blob/main/README.md#cli)). |
| **M2M integration surface** | **`npx clawhub@latest` CLI**, shared **HTTP/API schema** (`clawhub-schema` / `packages/schema`), registry **download and metadata JSON** per product spec ([spec.md](https://github.com/openclaw/clawhub/blob/main/docs/spec.md)). |
| **Identity / delegation** | **GitHub-authenticated publisher identity**; **owner-scoped** skills; **moderator/admin roles**; **audit log** for badge and moderation actions; **soft-delete / restore** and ownership tools ([spec.md — User, AuditLog, Auth + roles](https://github.com/openclaw/clawhub/blob/main/docs/spec.md)). |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Skill listing** | Slug, owner, semver versions, tags (`latest` + custom), changelog, stats |
| **Vector search** | Embedding search over skill text and metadata (per README + spec) |
| **CLI install/update** | Local skill lifecycle: `install`, `uninstall`, `list`, `update`, `inspect` |
| **Publish pipeline** | Authenticated upload, validation (`SKILL.md` required, size limits), moderation flags |
| **OpenClaw packages** | Native catalog for code/bundle plugins alongside skills ([README — packages](https://github.com/openclaw/clawhub/blob/main/README.md)) |
| **SOUL.md registry** | Shared platform for `SOUL.md` bundles (onlycrabs.ai / souls routes per README) |

---

## Autonomy Model

```
Agent or operator runs clawhub CLI (or calls registry HTTP API)
    ↓
Search / explore skills (vector or filters)
    ↓
Install selected SKILL.md pack to local agent host paths
    ↓
Agent host loads skill instructions + declared requirements
    ↓
Optional: authenticated publisher pushes new version + tags (no per-consumer UI step)
```

---

## Identity and Delegation Model

- **Publishers** authenticate with **GitHub**; skills are **owned by a user** with role-based admin/moderator overrides ([spec.md](https://github.com/openclaw/clawhub/blob/main/docs/spec.md)).
- **Consumers** pull **public read** artifacts; install is **local to the machine** running the CLI (`uninstall` removes local copy only — [README — Removal permissions](https://github.com/openclaw/clawhub/blob/main/README.md)).
- **Moderation and audits** tie actions to **actor user IDs** in the audit log; reporting and soft-delete flows attribute changes to moderators and owners.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| `clawhub` CLI | `npx clawhub@latest` — search, install, publish, package explore/publish per [docs/cli.md](https://github.com/openclaw/clawhub/blob/main/docs/cli.md) |
| HTTP / JSON API | Convex HTTP actions — metadata, downloads (zip), described in [docs/spec.md](https://github.com/openclaw/clawhub/blob/main/docs/spec.md) |
| Shared schema | `packages/schema` (`clawhub-schema`) for CLI and app alignment |

---

## Human-in-the-Loop Support

**GitHub OAuth** is required to **publish** or comment (with account-age rules per spec). **Browsing and installing** public skills does not require interactive HITL per operation. Moderators may **hide, restore, or badge** listings as part of governance ([spec.md](https://github.com/openclaw/clawhub/blob/main/docs/spec.md)).

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw GitHub repo of SKILL files** | No **central vector search**, **semver/tag governance**, **moderation**, or **unified CLI install** from a registry |
| **npm/PyPI** | General package indexes — no **SKILL.md–first** model, **agent requirement frontmatter**, or **OpenClaw package** metadata |
| **MCP-only registries (e.g. Smithery)** | Optimized for **remote MCP servers** and OAuth to tools; ClawHub optimizes **agent skill packs** and **OpenClaw plugins**, a different primitive |

---

## Use Cases

- **Coding agents** — install community **skills** for workflows (`clawhub search`, `clawhub install`)
- **OpenClaw / Clawdbot hosts** — resolve **published skill versions** and **plugin bundles** from one marketplace
- **Skill authors** — **publish**, **rename**, **merge duplicates**, and track **downloads/stars** with moderation support
