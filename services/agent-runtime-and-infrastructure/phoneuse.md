# PhoneUse

> **"Your agent now has a phone."**

| | |
|---|---|
| **Website** | https://www.phoneuse.com |
| **Docs** | https://docs.phoneuse.com/ |
| **GitHub** | https://github.com/phoneuse-official/phoneuse |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | MIT for the local USB iPhone repo (Copyright 2026 PhoneUse contributors); the hosted cloud control plane is a separate commercial product |
| **Latest-month signal** | Checked 2026-11-25: [homepage](https://www.phoneuse.com) HTTP 200, title "PhoneUse: Phones for AI agents", H1 "Your agent now has a phone."; [docs](https://docs.phoneuse.com/) HTTP 200, description "The mobile execution layer for AI agents."; MCP GET [https://mcp.phoneuse.com/mcp](https://mcp.phoneuse.com/mcp) 405; [healthz](https://mcp.phoneuse.com/healthz) HTTP 200 with `status` `degraded`; [repo](https://github.com/phoneuse-official/phoneuse) MIT, 123 stars, pushed 2026-11-23T09:51:52Z |
| **Verified at** | 2026-11-25 |

---

## Official Website

https://www.phoneuse.com

Title: *"PhoneUse: Phones for AI agents."* H1: *"Your agent now has a phone."* Meta description: *"Give your agent a phone. Cloud Android phones for scale, real iPhones tapped by a robot when your agent has to be undetectable."* Docs lead (https://docs.phoneuse.com/): *"The mobile execution layer for AI agents."*

The homepage sells both a cloud phone and a physical robot-hand iPhone tier. The live agent path documented for this listing is the hosted control plane, mainly cloud Android, plus that optional hardware.

---

## Official Repo

https://github.com/phoneuse-official/phoneuse

MIT: https://github.com/phoneuse-official/phoneuse/blob/main/LICENSE (Copyright 2026 PhoneUse contributors). The README title is "PhoneUse Local": *"Open-source tools for controlling a USB-connected iPhone from your Mac"* with local video, prompts, REST, and MCP. That repository is not the hosted cloud control plane. The cloud API and fleet are a separate commercial product.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** hosted control-plane MCP + REST, after a human-minted key. Not a one-URL join.

Console signup, then a person mints a `pbk_` / `puk_` key. The phone is bought or rented in the console. Checkout and billing stay off MCP. Docs say interactive MCP OAuth is not live yet. After a key and a device, `devices:lease` / `devices:act` / runs do not ask for a confirmation on each action. Idempotent retries and traces are part of the control plane.

```bash
# Control-plane MCP (stateless Streamable HTTP): https://mcp.phoneuse.com/mcp
# Docs for agents: https://docs.phoneuse.com/getting-started/for-agents.md
```

GET https://mcp.phoneuse.com/mcp returned 405 on 2026-11-25 (stateless server; GET is not the RPC). GET https://mcp.phoneuse.com/healthz returned 200 with `"status":"degraded"`: `fleetIntegrity.ok` false, `cloudRenewalScan.ok` false, `provisioning.state` `running` and `provisioning.ok` true. Do not treat the docs-site MCP as the control plane. https://docs.phoneuse.com/getting-started/for-agents.md says the docs server only searches documentation; the control plane is the server that drives the device.

---

## Agent Skills

**Status:** ⚠️ Not yet published

No official `SKILL.md` or `npx skills add` package was found on the docs pages reviewed on 2026-11-25.

Search community skills: `npx clawhub@latest search phoneuse`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available — hosted control-plane Streamable HTTP. Interactive OAuth is not live yet.

| Detail | Value |
|---|---|
| **MCP Repo** | Not the local USB repo. Control plane is hosted |
| **Endpoint** | `https://mcp.phoneuse.com/mcp` |
| **Transport** | Stateless Streamable HTTP (GET 405) |
| **Auth** | Org-scoped API key (`pbk_` / `puk_`). Interactive MCP OAuth: not live yet |
| **Health** | https://mcp.phoneuse.com/healthz — `degraded` on 2026-11-25 (see onboarding) |
| **Docs** | https://docs.phoneuse.com/getting-started/mcp-config.md |
| **Compatible Clients** | MCP clients that can send a bearer key to a remote Streamable HTTP server |

Name the control-plane server differently from the docs-search server (`phoneuse` vs something like `phoneuse-docs`), as https://docs.phoneuse.com/getting-started/for-agents.md asks.

---

## What It Does

PhoneUse's hosted product is a mobile execution layer: an agent leases a device, acts on it, and reads a trace. The public GitHub project is the local USB iPhone stack on a Mac. The website also offers a robot hand on a physical iPhone for traffic that must look like a person holding the phone. Cloud Android is the scale path described on the homepage.

On 2026-11-25 the API process was up and answered healthz, and it labeled itself degraded. Fleet integrity and the cloud renewal scan were not ok. Provisioning was still running and ok. Treat a lease as subject to that fleet state.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage title: *"Phones for AI agents."* H1: *"Your agent now has a phone."* Docs: *"The mobile execution layer for AI agents."* Sources: https://www.phoneuse.com and https://docs.phoneuse.com/ |
| **Agent-specific primitive** | `devices:lease`, `devices:act`, and runs, with traces and idempotent retries. The object is a device session for an agent, not a person's VNC desktop. |
| **Autonomy-compatible control plane** | After the key and the device, acts do not wait on a per-action confirmation. Billing and checkout are human console steps and are not MCP tools. |
| **M2M integration surface** | Hosted MCP `https://mcp.phoneuse.com/mcp`, the control-plane HTTP API, and the docs index at https://docs.phoneuse.com/llms.txt. The MIT repo is a separate local USB stack. |
| **Identity / delegation** | Org-scoped `pbk_` / `puk_` keys. The agent acts as that org on leased devices. Run tools are marked destructive on the control plane (`for-agents.md`). |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **devices:lease** | Take a cloud device (or the optional hardware tier) into a run. |
| **devices:act** | Observe and act on the leased phone. |
| **runs** | A traced attempt with idempotent retries. |
| **Local USB stack** | The MIT repo: a Mac controlling one cabled iPhone. Not the hosted fleet. |

---

## Autonomy Model

1. A person creates the console account, mints a key, and buys or rents a phone. Payment stays in the console.
2. The agent connects to `https://mcp.phoneuse.com/mcp` with that key.
3. The agent leases a device, acts, and reads the trace. Retries use the idempotency the control plane documents.
4. The agent releases the device when the run ends. If healthz is still `degraded`, a lease can fail even when the API process is up.

---

## Identity and Delegation Model

- Keys are org-scoped (`pbk_` / `puk_`), minted by a person. Interactive OAuth for MCP was not live on 2026-11-25.
- The agent does not get its own PhoneUse login separate from that key.
- Traces attribute actions to the run. Docs tell agents to keep the control-plane server distinct from the read-only docs server so a docs search is never a tap.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST | Control-plane HTTP API. Start at https://docs.phoneuse.com/getting-started/for-agents.md |
| Hosted MCP | `https://mcp.phoneuse.com/mcp` |
| Health | `https://mcp.phoneuse.com/healthz` |
| Docs | https://docs.phoneuse.com/ |
| Docs index | https://docs.phoneuse.com/llms.txt |
| Local USB repo | https://github.com/phoneuse-official/phoneuse — MIT, not the cloud fleet |

---

## Human-in-the-Loop Support

Signup, key minting, and buying or renting a phone are human console steps. Checkout is not an MCP tool. Webhooks can say when a run needs a person (https://docs.phoneuse.com/guides/webhooks.md). The act loop itself does not require a click per tap. The robot-hand iPhone is optional hardware, not the default cloud path.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **PhoneUse Local README, read as if it were the cloud** | The MIT repo controls one USB iPhone on a Mac. The hosted lease/act control plane is a different product. |
| **Phonebox / Mobilebox** (already listed, or listed separately) | Other vendors' cloud phones. PhoneUse's control plane, key prefix, and health endpoint are its own. |
| **A phone mirror** | Shows a person's screen. It does not lease a device, trace a run, or retry an action idempotently. |

---

## Use Cases

- **Cloud Android at fleet scale** — lease a device, act, and release it under an org key.
- **A physical iPhone when the site must see a real hand** — the robot-hand tier on the homepage, still through the same API story.
- **Local USB automation** — the MIT repo, when the phone is cabled to the operator's Mac rather than leased from the cloud.
