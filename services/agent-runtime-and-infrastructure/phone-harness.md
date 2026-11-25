# Phone Harness

> **"Let your agent use your phone."**

| | |
|---|---|
| **Website** | https://phone-harness.com |
| **Docs** | https://phone-harness.com/docs/llms.txt |
| **GitHub** | https://github.com/phone-harness/phone-harness |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | MIT (Copyright 2026 shawn pana) |
| **Funding / Compliance** | YC-backed |
| **Latest-month signal** | Checked 2026-11-25: [homepage](https://phone-harness.com) HTTP 200, H1 "Let your agent use your phone."; [docs index](https://phone-harness.com/docs/llms.txt) and [docs skill](https://phone-harness.com/docs/skill.md) HTTP 200; MCP GET [https://mcp.phone-harness.com/mcp](https://mcp.phone-harness.com/mcp) 401; [repo](https://github.com/phone-harness/phone-harness) MIT, 5776 stars, pushed 2026-11-24T03:20:48Z, `SKILL.md` present |
| **Verified at** | 2026-11-25 |

---

## Official Website

https://phone-harness.com

Homepage H1: *"Let your agent use your phone."* Meta description: *"Let your AI agent tap, type, and scroll through the apps on your iPhone or Android. Open source. No jailbreak, no API."* The open-source project drives a phone the operator already has. The hosted product also starts a temporary Android or a saved phone, and hosts iPhones.

---

## Official Repo

https://github.com/phone-harness/phone-harness

MIT: https://github.com/phone-harness/phone-harness/blob/main/LICENSE (Copyright 2026 shawn pana). About 5776 stars on 2026-11-25, last push 2026-11-24T03:20:48Z. Repo description: *"let your agent control your phone."* `SKILL.md` is in the repository root.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** CLI + REST + hosted MCP, after a dashboard key. Not a one-URL join.

Open signup includes a $5 credit. A person creates a dashboard API key. The local path needs iPhone Mirroring (Mac) or `adb`. The hosted MCP is for cloud phones only, not for the phone on the operator's desk.

```bash
pip install phone-harness
# Hosted MCP (cloud phones only): https://mcp.phone-harness.com/mcp
# REST base: https://api.phone-harness.com
```

https://phone-harness.com/docs/skill.md (HTTP 200) names `POST /sessions`, `GET /sessions/{sid}`, and `DELETE /sessions/{sid}` on `https://api.phone-harness.com` with `Authorization: Bearer`. Do not use the Mintlify docs-search MCP at `https://phone-harness.com/docs/mcp` as the phone. That URL returned 405 on GET on 2026-11-25 and is the documentation host, not the product MCP.

---

## Agent Skills

**Status:** ✅ Available — `SKILL.md` in the repo and a docs-site skill

```bash
curl -fsSL https://raw.githubusercontent.com/phone-harness/phone-harness/main/SKILL.md
```

| Skill | What It Teaches the Agent |
|---|---|
| `phone-harness` | Tap, type, swipe, and read an iPhone via iPhone Mirroring, Android over adb, a rented cloud Android, or a cloud iPhone over HTTPS (repo `SKILL.md`) |
| `phone` | Provision cloud Android or Cloud iPhone sessions and call the REST API (https://phone-harness.com/docs/skill.md) |

---

## MCP

**Status:** ✅ Available — hosted Streamable HTTP for cloud phones

| Detail | Value |
|---|---|
| **MCP Repo** | Product server is hosted. Local control also ships in https://github.com/phone-harness/phone-harness |
| **Endpoint** | `https://mcp.phone-harness.com/mcp` |
| **Transport** | Streamable HTTP |
| **Auth** | Bearer API key. GET returned 401 Authentication required on 2026-11-25 |
| **Scope** | Cloud phones only. A desk iPhone or adb device uses the CLI, not this URL |
| **Docs** | https://phone-harness.com/docs/guides/mcp-server.md |
| **Compatible Clients** | Claude, Cursor, Codex, and other Streamable HTTP clients (docs) |

---

## What It Does

Phone Harness lets an agent tap, type, scroll, and read a phone screen. Locally that is the operator's iPhone through iPhone Mirroring, or an Android device over adb. In the cloud, the API can start a temporary Android emulator or a saved Android phone, and it can attach a hosted iPhone. Docs (https://phone-harness.com/docs/llms.txt) describe shared Android emulators and real Cloud iPhones on a flat subscription, with an optional viewer for video or a still screenshot.

The OpenClaw guide on that index says every script asks the person first. That is a property of the OpenClaw integration, not of every API call. The session API and hosted MCP do not require a human click for each tap. A viewer can watch.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage H1: *"Let your agent use your phone."* Repo: *"let your agent control your phone."* Sources: https://phone-harness.com and https://github.com/phone-harness/phone-harness |
| **Agent-specific primitive** | A phone session the agent starts, drives (tap/type/scroll/read), and ends, over CLI, REST, or MCP. The screen is the interface when the app has no API. |
| **Autonomy-compatible control plane** | After the API key, cloud session calls do not wait on a per-action click. A viewer is optional. The OpenClaw guide is the exception that asks first. |
| **M2M integration surface** | `phone-harness` CLI, REST `https://api.phone-harness.com`, hosted MCP, OpenAPI linked from the docs, `llms.txt`, and `SKILL.md`. |
| **Identity / delegation** | Dashboard API key on the account that owns the credit and the phones. Local mirroring uses the operator's Mac session. Cloud MCP cannot see that local phone. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Session** | `POST /sessions` starts a cloud phone; `DELETE /sessions/{sid}` ends it (docs skill). |
| **Screen actions** | Tap, type, scroll, and read, from the CLI or the API. |
| **Saved phone** | A cloud Android that comes back as the agent left it (docs Android guide). |
| **Viewer** | Optional live video or a screenshot. Not required to act. |

---

## Autonomy Model

1. A person signs up (the listed starting credit is $5) and copies a dashboard API key.
2. For a local phone, the person has iPhone Mirroring or adb already working.
3. The agent creates a cloud session or attaches the local device and drives the screen.
4. The agent ends the session. Billing follows the limits guide at https://phone-harness.com/docs/guides/limits-and-credits.md.

---

## Identity and Delegation Model

- The API key is the account credential. The agent uses it; it does not mint a second identity on the MCP tool list.
- Hosted MCP is limited to cloud phones. Pointing it at the operator's pocket phone is out of scope.
- Local control inherits the Mac user who approved mirroring or USB debugging.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `pip install phone-harness` |
| REST | `https://api.phone-harness.com` — bearer API key |
| Hosted MCP | `https://mcp.phone-harness.com/mcp` |
| Docs index | https://phone-harness.com/docs/llms.txt |
| Skills | Repo `SKILL.md` and https://phone-harness.com/docs/skill.md |

---

## Human-in-the-Loop Support

Signup and the API key are human steps. Local iPhones need the person to turn on iPhone Mirroring. A viewer can watch a cloud phone and is not on the path of each tap. The OpenClaw guide tells that integration to ask before each script.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Docs MCP at `/docs/mcp`** | Mintlify search over the documentation site. It does not start a phone. The product MCP is `https://mcp.phone-harness.com/mcp`. |
| **Phonebox / Mobilebox / PhoneUse** | Other hosted phone products. Phone Harness is the MIT CLI plus this vendor's cloud sessions. |
| **A VNC app** | A person drives the screen. There is no session API, agent CLI, or cloud-phone MCP. |

---

## Use Cases

- **The phone already on the desk** — iPhone Mirroring or adb, driven by the CLI.
- **A temporary cloud Android** — `POST /sessions`, install a build, tap through it, delete the session.
- **A saved cloud phone or a hosted iPhone** — the same API, with a viewer when a person wants to watch.
