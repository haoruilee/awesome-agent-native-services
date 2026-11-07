# Tadka

> **"The booking layer for AI agents."**

| | |
|---|---|
| **Website** | https://tadka.xyz |
| **Docs** | https://tadka.xyz/developers · https://tadka.xyz/llms.txt · https://tadka.xyz/openapi.json |
| **GitHub** | — (no public application repository found as of 2026-11-07; hosted MCP/REST are live) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **Verified at** | 2026-11-07 |
| **Latest-month signal** | Homepage H1 "The booking layer for AI agents." HTTP 200. `https://tadka.xyz/llms.txt` and `https://tadka.xyz/openapi.json` HTTP 200. MCP `https://tadka.xyz/mcp` answered HTTP 401 (OAuth-protected, expected). Public REST `GET /api/public/v1/restaurants` documented no-key |

---

## Official Website

https://tadka.xyz

Tadka is an open restaurant discovery and table-reservation directory built for AI assistants and agents. Any assistant can find and reserve a table at a Tadka restaurant through MCP, REST, `llms.txt`, and OpenAPI. Launch coverage advertised for New York (with SF, London, India mentioned in earlier launches).

---

## Official Repo

No public application repository was found as of 2026-11-07. The live contract is the hosted MCP, OpenAPI, and `llms.txt` surfaces.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** MCP (OAuth as diner) + open REST directory

Remote MCP (Streamable HTTP; OAuth 2.1 with dynamic client registration):

```
https://tadka.xyz/mcp
```

In Claude / ChatGPT / MCP clients: Settings → Connectors → Add custom connector → paste the URL → sign in as the diner and approve.

Open directory (no key):

```bash
curl "https://tadka.xyz/api/public/v1/restaurants?city=New%20York&limit=5"
```

OpenAPI: https://tadka.xyz/openapi.json · Agent map: https://tadka.xyz/llms.txt

---

## Agent Skills

**Status:** ⚠️ Not yet published as an installable Agent Skills package

`https://tadka.xyz/llms.txt` teaches agents the open JSON API, MCP booking tools, and OpenAPI path. There is no `npx skills add` package cited on the site as of 2026-11-07.

---

## MCP

**Status:** ✅ Available — OAuth required for booking tools

| Detail | Value |
|---|---|
| **Endpoint** | `https://tadka.xyz/mcp` |
| **Transport** | Streamable HTTP (unauthenticated probe returned HTTP 401 on 2026-11-07) |
| **Auth** | OAuth 2.1 with dynamic client registration; diner signs in and approves the assistant. Discovery metadata at `/.well-known/oauth-protected-resource` |
| **Tools (site docs)** | `search_restaurants`, `get_restaurant`, `check_availability`, `book_table`, `list_my_bookings`, `cancel_booking`, `join_waitlist` |
| **Compatible clients** | Documented for Claude, ChatGPT, and generic MCP clients |

---

## What It Does

Tadka publishes structured, agent-ready restaurant profiles (cuisines, price for two, dietary options, amenities, menus, live availability) and an atomic booking engine so agents do not double-book. The open REST API is read-only discovery without a key. Booking, cancel, and waitlist run through MCP under the signed-in diner's permissions. Restaurants can list for free during launch; partner POS sync via signed webhooks is documented under Advanced.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage H1: "The booking layer for AI agents." Developers page: "Tadka agent booking protocol." — [tadka.xyz](https://tadka.xyz/) · [developers](https://tadka.xyz/developers) |
| **Agent-specific primitive** | MCP tools for search → availability → atomic `book_table` / waitlist under diner OAuth; structured restaurant profiles for agents |
| **Autonomy-compatible control plane** | After one OAuth approval, the agent can search, check slots, book, list, and cancel without a booking-site UI click. Capacity is enforced server-side |
| **M2M integration surface** | Remote MCP, REST, OpenAPI 3.1, `llms.txt` |
| **Identity / delegation** | Agent acts as the signed-in diner via OAuth; tools run with that diner's permissions; bookings are attributable to the diner account |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **search_restaurants / get_restaurant** | Find partners by city, cuisine, vibe, price, diet |
| **check_availability** | Live slots and seats left for a party size/date |
| **book_table / cancel_booking** | Atomic reservation for the signed-in diner |
| **join_waitlist** | Waitlist when a slot is full |
| **Open directory REST** | No-key restaurant list/detail for crawl-time discovery |

---

## Autonomy Model

1. Person connects `https://tadka.xyz/mcp` once and signs in as the diner.
2. Agent searches and checks availability.
3. Agent calls `book_table` with restaurant, date, time, party size, guest name.
4. Agent lists or cancels via MCP tools.
5. Optional: agent uses the open REST directory without auth for discovery-only flows.

---

## Identity and Delegation Model

- Booking tools require OAuth as the diner; the assistant is approved for that diner's permissions.
- Open REST discovery is anonymous and read-only.
- There is no separate per-agent wallet; attribution is to the diner account / OAuth client.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP | https://tadka.xyz/mcp (OAuth 2.1) |
| REST | https://tadka.xyz/api/public/v1/restaurants |
| OpenAPI | https://tadka.xyz/openapi.json |
| llms.txt | https://tadka.xyz/llms.txt |

---

## Human-in-the-Loop Support

Diner signs in once via OAuth. Ongoing search/book/cancel is agent-driven. Restaurant partners manage listings in a partner dashboard; that is secondary to the agent booking loop.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **OpenTable / Resy consumer apps** | Human booking UIs; agents are blocked or limited to brittle scraping, not a sanctioned MCP booking protocol |
| **A generic restaurant CRUD API** | Lists venues but does not provide agent-first MCP booking with diner OAuth and atomic capacity |
| **PlaceCall-style phone booking** | Solves voice outreach; Tadka is a direct table inventory + MCP book path |

---

## Use Cases

- **Dinner for N** — agent finds a quiet vegetarian-friendly table in NYC and books it
- **Availability sweep** — check several partner restaurants for a party size/date
- **Cancel / waitlist** — agent manages the diner's reservations after the fact
