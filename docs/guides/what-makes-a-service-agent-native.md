---
layout: default
title: "What makes a service agent-native"
description: "The five admission tests this catalog applies, the narrow operator-surface exception, and the products that stay off the list."
permalink: /guides/what-makes-a-service-agent-native/
page_kind: document
ads: false
guide_order: 1
---

Most products that mention agents are describing a feature. A smaller set is describing the caller. The Agent-Native Index only lists the second kind, and it writes the distinction down so a new proposal can be refused for a reason instead of a mood. This guide is that distinction, taken from the repository's [contribution guide](https://github.com/haoruilee/awesome-agent-native-services/blob/main/CONTRIBUTING.md) and applied to the way the site is organized.

The practical problem is vocabulary. "AI-powered," "agent-ready," and "now with MCP" all show up on products that were built for a person at a screen. Some of those products are good. They are still the wrong entry in a catalog whose job is to help an agent, or the person wiring one, find infrastructure the agent can operate. The tests below are how this project says no.

## The five tests

A service on the standard track has to pass all five. Four out of five is a miss. The contribution guide is explicit about that because partial matches are how adapted products sneak in: the API is real, the blog post says "agents," and the primitive is still a user account.

### The vendor has to mean agents

Official pages have to name AI agents as the primary consumer. A footnote, an integration section, or a launch post is not positioning. The contribution guide's pass examples are the kind of sentence that leaves little room: AgentMail's "Email for AI agents," Browserbase's "A web browser for AI agents & applications," HumanLayer's "Human in the Loop for AI Agents," Skyfire's "Identity and payments for autonomous AI agents." The fail examples are just as specific: a platform that is "now with AI agent support," a product for building apps and workflows and agents as one of several outputs, a developer platform that mentions agents in a post.

The quote has to be findable. Proposals paste the sentence and the URL. The dossier keeps the tagline in quotation marks so a later editor can see that the words were the vendor's. When the homepage changes, the update path is an issue with the new quote, not a silent rewrite. Positioning is easy to check and not sufficient on its own. A landing page can say "for agents" over a normal user API.

### The primitive has to be about an agent

The second test asks whether the API would look the same if the caller were a human application. If it would, the service is infrastructure a developer might use while building an agent, which is a large and respectable market, and it is not this list.

Pass examples from the guide are concrete. An inbox that belongs to the agent, with a webhook when mail arrives, is not a user inbox. An approval gate that puts the denial back into the agent's context is not a status field on a ticket. A Know Your Agent token is not a user login. A remote browser session whose whole lifecycle is create, drive, destroy is not "we also have a headless mode." A checkpoint between model calls is not a queue that retries a stateless job.

Fail examples are the ones people argue. A REST API any server could call. A webhook any server could receive. An email API that still requires a human Gmail account. Those can be excellent dependencies. They do not become agent-native because an agent is the process holding the token. The [communication collection](/categories/communication/) is built around this test: AgentMail's dossier describes inboxes created for the agent, threads as data, and inbound webhooks, which is why it is listed, while a general email API for applications is the comparison the contribution guide tells proposers to write down and then exclude.

### The agent has to be able to finish

The third test is whether the agent can complete the loop this service provides without a person clicking. The guide's question is blunt: can the agent do the thing, including the actions this service exists for, with no one at a button?

That is not a demand that every action be unsupervised. Budgets, isolation, session limits, and approval gates are how the test is met rather than how it is failed. Skyfire's dossier describes operator-set spend limits on an agent wallet. HumanLayer's category is the approval itself, which only makes sense if the rest of the loop runs and then stops at a named step. A product that requires a person to confirm every API call has no control plane an agent can inhabit. A product that offers no constraint at all is usually just an API key with a slogan. The test looks for the middle: unattended operation, with a constraint that is part of the product.

### The interface has to be for machines

On the standard track the primary interface is an SDK, an HTTP API, an MCP server, a webhook, or a structured CLI. A management UI can exist. It cannot be the only way to create the resource the agent needs.

This is where a lot of "we added a chat panel" products fall over. The panel is the product. The API, if there is one, is an afterthought for the customer's developers. The catalog's service pages record the interfaces the dossier actually names, which is why one card says MCP and another does not. MCP is not the test. It is one way to pass the test. [Getting started with MCP servers](/guides/getting-started-with-mcp-servers/) treats the protocol as a tool surface, not as a synonym for agent-native.

The operator-surface track, below, is the deliberate exception. It exists so the rule does not pretend that a status line speaks HTTP.

### The agent has to be someone

When the service acts in the world, it has to know who is acting. The contribution guide requires a distinction between the agent's identity and the user's, a model of what was delegated, and an audit trail that can name the agent. Mail the agent sends should not be indistinguishable from the operator clicking Send on a personal account, unless the product's whole point is that a person reviews the draft, and even then the draft should be the agent's. Payments are the sharp version of the same idea. [Payments for autonomous agents](/guides/payments-for-autonomous-agents/) is about wallets, mandates, and checks that exist because "the user clicked Buy" is no longer available.

Read-only operator surfaces do not mint delegated authority. They still have to attach what they display to a session, and they have to say that observation is not authorization. A HUD that cannot refuse a tool call is not an oversight product. The [oversight collection](/categories/oversight-and-approval/) is where refusal lives.

## The exception that is easy to stretch

A human-facing surface can qualify when it is purpose-built to operate live agents. The contribution guide sets five conditions, and they are conditions, not themes. The surface is for agents rather than for applications in general. It continuously interprets agent-specific state: a rollout or session, context pressure, tool or subagent activity, permissions, skills, MCP configuration, quota windows. It attributes that state to a concrete session. It is a dedicated operational surface, such as a CLI, a wrapper, a daemon, a hook, or a status-line protocol. And it documents the powers it does not have.

Claude HUD, listed in the [harness collection](/categories/agent-harnesses-and-control-planes/), is the shape of the operator track: a plugin whose job is to show what a coding agent is doing. The two Codex HUD entries are separate projects that both render a status line for Codex. They are not one product counted twice. Generic terminal themes and system monitors stay out even if someone skins them in the language of agents. The guide's phrase is that the exception changes the interface and delegation tests for read-only operator tools. It does not admit a product that was human first and later grew a tab.

Harnesses that own loop state sit next to those surfaces because both wrap an agent that can already act. LoopX's tagline in the catalog is a control plane for long-horizon agents. That is a different responsibility from a status line. The collection essay keeps the tracks apart so a reader does not install one and believe they bought the other.

## What the list refuses

The contribution guide names whole classes that are out no matter how the marketing is phrased.

Agent builders are for people who configure or visually assemble agents. The guide's examples include Dify, n8n, Flowise, AutoGen Studio, and LangGraph. RAG studios that help people build retrieval pipelines are out. The examples given are LlamaIndex Cloud and Cohere Compass. Chat workspaces where a person talks to a model are out. No-code bot platforms are out. None of that is a claim that those projects are low quality. It is a claim that a catalog of agent-native services becomes useless if it also contains the tools humans use to construct agents.

Agent-adapted services are the subtle bucket. The guide's examples are Resend after adding MCP, Stripe's Agent Toolkit, and Twilio: human products that grew an agent interface. They can be the right dependency for an application. They are recorded, when at all, as boundary cases in the repository README so the next proposer can see the refusal in advance. A thin MCP server on top of a human SaaS product does not relocate the product into this list. The primitive, the identity model, and the control plane still have to be about the agent.

## Signals that help, and do not admit

URL onboarding is the bonus the contribution guide weights highest. The agent reads one document and follows it. No SDK install, no dashboard, and no human-issued key as the join step itself. The repository keeps a current table. mails.dev, MailboxKit, and Moltbook are among the services marked that way. Shellmates used to be, and its join URL later returned HTTP 404, so the catalog keeps the entry and says the path is offline. A star means the join path is machine-readable. It is not a rank and not a security review.

MCP support, published Agent Skills, per-agent state, and machine-readable traces are recorded because they are evidence of the same design. They are medium-weight signals in the guide's table. A service with all of them can still fail positioning or identity. A service with none of them can still pass, if the five tests pass on an HTTP API alone. E2B's dossier, for example, centers on sandboxes for generated code. Whether a given release also ships an MCP server is a fact to check in the [E2B docs](https://e2b.dev/docs) and in the dossier, not a substitute for the sandbox primitive.

## How to read a page on this site

A collection essay says what that group is for. The cards under it are generated from the dossiers. A service introduction repeats the dossier's summary and the interfaces the catalog recorded. The file on GitHub is the evidence: the quote, the primitive, the protocol, and why a generic alternative was refused.

Apply the five tests before you trust a tagline. "Email for AI agents" fits AgentMail because the primitive is an inbox the agent creates. The same sentence on a product that only forwards a person's mailbox would fail the second test. After a service has passed, the guide for that job is about fit. Passing is not a recommendation.

## What this guide is not claiming

It is not a legal definition, and it is not a standard outside this repository. Other people use "agent-native" for a product philosophy about software that people mostly delegate to agents. Related idea, different scope. Here the phrase is an admission label with written tests.

The tests do not measure uptime, price, or how well a product works. A service can pass and still be a poor fit, early, or offline. The editorial policy is how those facts get corrected. If a test itself seems wrong, change the contribution guide in public, where the next proposal can see it. Quiet exceptions are how the list turns back into a pile of links.
