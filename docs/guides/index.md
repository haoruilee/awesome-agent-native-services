---
layout: default
title: "Guides"
description: "Original essays on how to read this catalog and choose agent-native infrastructure."
permalink: /guides/
page_kind: document
ads: false
---

These essays are the long form of the index. The collection pages say what a group of services is for, in a few paragraphs above the cards. A guide stays with one decision: what the catalog means by agent-native, or how the email, browser, memory, sandbox, tool, and payment listings differ from each other.

They are written to be read in any order. The first one is the admission rule. The others assume a service is already the kind of thing this list accepts, and they argue about fit. A card can pass every test and still be the wrong primitive for the job in front of you. That gap is why the essays exist beside the tables.

Each guide is written from the dossiers in this repository and from the public documentation those dossiers cite. It links the vendor when it states a product fact. It does not add a score, a price, or a measurement this project did not publish. The method is the [editorial policy](/editorial-policy/). The admission rules behind the first guide are in the repository's [contribution guide](https://github.com/haoruilee/awesome-agent-native-services/blob/main/CONTRIBUTING.md).

## Start here

**[What makes a service agent-native](/guides/what-makes-a-service-agent-native/).** The five tests, the narrow exception for operator surfaces, and the products the list refuses. Read this before arguing with a card.

## Choosing infrastructure

**[How to choose an email API for AI agents](/guides/choose-an-email-api-for-agents/).** Agent-owned inboxes, self-hosted mail, notification workflows, and the coordination mail coding agents use on a repository.

**[Browser infrastructure for agents compared](/guides/browser-infrastructure-for-agents/).** Hosted sessions, local engines, extraction APIs, and browsers that keep a login between tasks.

**[Memory layers for agents](/guides/memory-layers-for-agents/).** Fact extractors, temporal graphs, shared wikis, and local memory for coding agents. Why a vector database is not the whole problem.

**[Sandboxes and code execution for agents](/guides/sandboxes-and-code-execution/).** Where generated code should run, and what changes when the sandbox is a microVM, a Kubernetes resource, or a machine on the same laptop.

**[Getting started with MCP servers](/guides/getting-started-with-mcp-servers/).** Hosts, clients, and servers, local stdio versus remote HTTP, and the registries and credential layers in the tool collection.

**[Payments for autonomous agents](/guides/payments-for-autonomous-agents/).** Wallets and Know Your Agent identity, HTTP 402, mandates, and the checks that are supposed to run before anything is signed.

The collection essays link back to the guide that matches them. The other collections, including oversight, search, observability, voice, and gateways, are explained on their own pages. A guide will be added when there is enough in the catalog to compare, not to fill a grid.
