# 402xAgent

> **"The check an agent calls before paying any x402 endpoint."**

| | |
|---|---|
| **Website** | https://402xagent.com |
| **GitHub** | https://github.com/withgrokbot/x402-spotcheck |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |

---

## Official Website

https://402xagent.com

---

## Official Repo

Fetch wrapper: https://github.com/withgrokbot/x402-spotcheck

---

## How to Use (Agent Onboarding)

**SDK / REST.** Free tier, no payment needed:

```bash
curl 'https://api.402xagent.com/v1/products/endpoint-spot-check?url=<endpoint>'
```

**MCP.** `https://api.402xagent.com/mcp` (tool `endpoint_spot_check`).

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **Endpoint** | https://api.402xagent.com/mcp |
| **Tool** | `endpoint_spot_check` |

---

## What It Does

402xAgent is the check an agent calls before paying any x402 endpoint. It probes the endpoint's 402 without paying and returns a pay/skip/recheck verdict with a reason. Each check produces a public receipt. It never pays the target.

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Unpaid 402 probe** | Reads the endpoint's 402 payment requirements without paying |
| **Verdict** | `pay`, `skip` or `recheck`, with a plain reason |
| **Public receipt** | A public receipt URL for each check |

---

## Protocol Surface

| Interface | Detail |
|---|---|
| HTTP | `https://api.402xagent.com/v1/products/endpoint-spot-check?url=<endpoint>` |
| MCP | `https://api.402xagent.com/mcp` (tool `endpoint_spot_check`) |
| Fetch wrapper | https://github.com/withgrokbot/x402-spotcheck |
| Free tier | Yes |
