# usdc-paywall

> **"Crypto-native paywall for Node — verify USDC payments on Base/Polygon by tx hash and unlock your API."**

| | |
|---|---|
| **Website** | https://github.com/essentoclothes-sudo/usdc-paywall |
| **Docs** | https://github.com/essentoclothes-sudo/usdc-paywall#readme |
| **GitHub** | https://github.com/essentoclothes-sudo/usdc-paywall |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |

## Official Website
The GitHub repository is the canonical public surface.

## Official Repo
https://github.com/essentoclothes-sudo/usdc-paywall

---

## How to Use (Agent Onboarding)

**Quickest verified path:**

`npm i @josealbertomaquina/usdc-paywall`, then on the server side:

    const { verifyPayment } = require('@josealbertomaquina/usdc-paywall')
    const r = await verifyPayment({ txHash: '0x…', wallet: '0x…', amount: 3, chain: 'base' })
    if (r.ok) res.send(paidContent) // paid >= 3 USDC, confirmed

CLI: `npx @josealbertomaquina/usdc-paywall --tx 0x… --to 0x… --amount 3 --chain base`

---

## Agent Skills
**Status:** ⚠️ None found.

## MCP
**Status:** ⚠️ Not an MCP server; Node.js library + CLI.

## What It Does
Host-side paywall for API providers: checks the ERC-20 Transfer log of the official USDC contracts on Base and Polygon against your own wallet by transaction hash, so a paying agent (or human) unlocks content or endpoints per call. Adds a live watch mode (eth_getLogs) and Ed25519 offline license verification in the Pro tier.

## Why It Is Agent-Native
Agents pay USDC directly from their own wallet; the provider verifies on-chain settlement with no Stripe, accounts, or KYC — an HTTP 402-style machine checkout with no human in the loop.
