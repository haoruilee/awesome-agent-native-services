---
layout: default
title: "Payments for autonomous agents"
description: "Wallets and Know Your Agent identity, HTTP 402, payment mandates, and the checks that run before anything is signed."
permalink: /guides/payments-for-autonomous-agents/
page_kind: document
ads: false
guide_order: 7
---

A payment flow built for people has a reliable signal that an agent does not. Someone clicked Buy. They were logged in. A card form, a redirect, and a receipt followed. When the caller is an agent, that click is gone, and the questions that remain are the ones the [commerce collection](/categories/commerce-and-payments/) is organized around. Who is the agent? What was it allowed to spend? Did a person authorize this class of payment earlier, or this exact cart? Which record names the agent rather than a shared company card?

The collection is not one product. It is four layers that people stack, and that marketing pages tend to blur. This guide keeps them apart. It does not recommend a chain, a token, or a fee. Those are in the vendor docs because they change. A figure copied here would be the kind of stale fact the [editorial policy](/editorial-policy/) tells this site not to publish.

## Identity and a wallet

[Skyfire](https://skyfire.xyz) is the contribution guide's example of agent-first positioning in payments: "Identity and payments for autonomous AI agents." The dossier describes a Know Your Agent token, an agent wallet with spend limits set by an operator, and a protocol it calls KYAPay. There is no public repository recorded. Integration is through the developer portal. The idea, whether or not you use this vendor, is the one the category notes require. The agent is a principal the receiver can recognize. The spend limit is enforced by the payment layer, not by a sentence in the prompt. The ledger can name the agent.

[AgentsPay](https://agentspay.dev) is the crypto-identity and embedded-wallet entry, with an MCP-facing gateway in the category table. [Circle Agent Stack](https://developers.circle.com/agent-stack) is Circle's agent-facing financial stack. The dossier's summary is wallets, discovery of paid services, and programmable payments with guardrails. Circle is a stablecoin company. Do not infer from this paragraph which networks or assets a given release supports. The developer docs are the list.

[Payman](https://paymanai.com) is the banking-shaped entry: the tagline in the catalog is agentic banking under a person's control, with an API. It is the right row to read if the money is fiat and a regulated account, and the wrong row if you wanted a 402 challenge inside an HTTP call. Those are different controls. A bank-like product can refuse a transfer that exceeds a policy. It will not be the thing a random API returns instead of a JSON body.

Use this layer when the agent will pay many counterparties and you need an account, a limit, and a name. Do not use it when the only problem is "this one HTTP endpoint wants to be paid before it answers." That is the next layer.

## Pay inside the request

HTTP status 402 has meant Payment Required for a long time and was rarely used. A set of listings in this catalog revive it for machines. The caller requests a resource. The server answers with 402 and terms. The caller pays and retries with a proof. No checkout page, no person, no redirect.

[Coinbase's x402 documentation](https://docs.cdp.coinbase.com/x402/welcome) and the [x402 site](https://x402.org) are the reference the dossier points at. Coinbase's role in that dossier is a facilitator that verifies and settles, plus SDKs, plus a discovery surface called Bazaar. The protocol is aimed at autonomous clients paying per call. [OpenLibx402](https://github.com/openlibx402/openlibx402) is an open library for the same kind of integration. [Nevermined](https://nevermined.ai/) describes an x402 facilitator: the 402 comes back, the agent pays, the request completes inside that exchange.

[MPP](https://mpp.dev) is a sibling protocol, not a rename. The dossier describes a challenge, a credential, and a receipt, and it says the method is extensible beyond a single chain. The site is the list of rails. Do not take a secondary summary as the list. [Tollex](https://tollex.org) calls itself an economic control plane and documents HTTP and x402. Read its docs for which assets it actually speaks. The catalog row is not a promise that every 402 network is accepted.

This layer fits metered APIs: search, inference, a fetch that should cost something. It fits badly as a person's monthly rent. There is no cart, unless you build one above it. The agent needs a way to pay that does not ask a human each time, which means a funded wallet and a limit. x402 does not invent the limit. The wallet or the client policy does. An agent with a hot wallet and no cap will pay any 402 it sees, including one it should have refused. That is why the collection also contains the checks below.

## A mandate is not a payment

[AP2](https://ap2-protocol.org), the Agent Payments Protocol, is an open protocol for verifiable intent. The dossier is careful about the distinction this section exists to repeat. x402 settles an HTTP challenge. AP2 is how a merchant or a network can see what the user authorized when no one clicked Buy. The mechanism is verifiable digital credentials: checkout mandates and payment mandates, open or closed. Open means constraints before a final cart. Closed means a specific checkout. The dossier says the mandates chain into an audit trail for both human-present and human-not-present flows, and that samples include cards and x402. The [Universal Commerce Protocol](https://ucp.dev) is the neighboring listing, a common language for platforms, agents, and businesses, which the AP2 dossier says can carry AP2 as its payment path.

If you are a merchant, a mandate answers "were you allowed to buy this?" A facilitator receipt answers "did the money move?" You can need both. If you only integrate a wallet, you may have a payer and no proof of the user's intent beyond "the operator funded the wallet." If you only integrate a mandate, you have a signed constraint and no settlement. The catalog lists them separately so a proposal cannot wave at one and claim the other.

## Checks that are supposed to run first

Several listings exist to slow the agent down in a specific way.

[402xAgent](https://402xagent.com) probes an endpoint's 402 without paying. The dossier says it compares the challenge to what the listing claimed and returns pay, skip, or recheck, with a public receipt for the check. It does not pay the target. That is a useful sentence to keep. A safety tool that also holds the wallet has a different failure mode.

[AffixIO](https://www.affix-io.com/agent-trust/) is host-side attestation: know which agent acted, and check the action before pay or tool use. [INAM](https://inamprotocol.org) is a check of an agent or an x402 seller before you pay, with signed receipts in the dossier. [SecondSign Core](https://github.com/Bestpart-Irene/secondsign-core) is an independent co-signer for agents that move other people's money, with an execute-once rail and hash-chained receipts. [Veyra](https://veyra.money) exposes a per-agent MCP endpoint with bands the dossier describes as auto, ask, and block. [send21](https://send21.io) is non-custodial. The dossier describes pay links and drafts the agent creates, while the keys stay off the agent, and a rate that is locked for a limited window. The window length is a product parameter. Read the current [docs](https://send21.io/docs/mcp) for it. [Shinjuku Shield](https://shinjukustaition.com) is a privacy-oriented facilitator on Solana, self-custody, with spend caps. [Lumen Tab](https://github.com/Dansgit2b/lumen-tab) is an early, and in the dossier unaudited, prepaid tab for pay-per-call APIs. Early and unaudited are reasons to read the repository before sending funds, not flavor text.

[Priors](https://priors.trade) is reputation rather than a rail: a public, recomputable record for agents. Reputation is only as useful as the thing it measures. Read what actions feed it before you treat a score as a payment control.

The pattern across the serious entries is the same pattern as oversight, applied to money. The prompt is not the policy. A co-signer, a band, a probe, or a cap that the signing key cannot bypass is the policy. [Oversight products](/categories/oversight-and-approval/) are the general form. These listings are the form that understands a payment.

## What the category will not list

The contribution guide's exclusion examples for adapted products include Stripe's Agent Toolkit. A human payment company that publishes an SDK for agents can be the right way to charge a human's card. It is not, on this list, an agent-native wallet. The tests are the usual five. The payer identity has to be the agent's or an explicit delegation. The spend control has to be a primitive. The agent has to be able to complete a payment that was pre-authorized without a person clicking that payment. A checkout page the agent drives with a browser is a browser problem plus a human payment problem. It is not this category, even if it works.

The same refusal applies in reverse. A token transfer with no identity, no limit, and no record is not "programmable money for agents" just because the caller was a script. The category notes ask for an agent-controlled account, unattended execution inside a policy, operator-defined spend controls, a per-agent audit trail, and an identity story. Drop one and the proposal is supposed to fail.

## How to assemble a stack without collecting logos

If you are selling an API to agents, start with the 402 layer and a facilitator you understand, and publish terms a probe can read. x402, MPP, or Nevermined's facilitator are the docs to open. Add a mandate if a merchant or a network has to see user intent, which is AP2's problem, not the facilitator's.

If you are operating an agent that spends, start with a wallet that is not your personal key, a cap enforced outside the model, and a log that names the agent. Skyfire, Circle's agent stack, or AgentsPay are the identity-and-wallet docs. Put a probe or a co-signer in front if the agent discovers endpoints by itself. 402xAgent's refusal to pay during the check is the property to look for in anything you use as a gate. A gate that pays "just this once" to see the price has already failed.

If a person must approve above a threshold, that threshold should be the wallet's or the co-signer's, and the approval should re-enter the run as data. Veyra's ask band is one documented version. An oversight product from the other collection is another. A Slack message nobody's workflow waits on is not a control.

If you cannot explain, for a given payment, which component proved identity, which component moved funds, and which component was allowed to refuse, you have a demo. The collection is large enough to build the three separately. It is not a single signup.
