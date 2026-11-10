---
layout: default
title: "Sandboxes and code execution for agents"
description: "Where generated code should run, and how microVMs, Kubernetes sandboxes, and local hypervisors differ."
permalink: /guides/sandboxes-and-code-execution/
page_kind: document
ads: false
guide_order: 5
---

An agent that writes code has to run it somewhere. On the same machine as the agent, a bad snippet can read the environment, open the network, or leave a process behind. In a sandbox shared by every task, the second task inherits the first task's files. The [code execution collection](/categories/code-execution/) lists environments whose lifecycle an agent can drive: create, execute, read a structured result, destroy. The category notes also ask for state across more than one execution in the same environment, and for a startup that is fast enough to sit inside a loop. "Fast enough" is a requirement aimed at interactive use. The number you should plan around is the one in the vendor's current docs, not a figure frozen here.

This guide groups the listings by how the isolation is built. The groups overlap. A hosted API can be microVMs. A Kubernetes resource can front a microVM runtime. Read the group as a question to ask the dossier, not as a wall.

## Hosted sandboxes

[E2B](https://e2b.dev) is the catalog's plain statement of the hosted shape. The tagline is a cloud for agents, secure sandboxes for generated code. The documented quick path is a Python or TypeScript SDK that opens a sandbox, runs code, and closes it. The [docs](https://e2b.dev/docs) are also where to confirm the current MCP story. The dossier describes both an MCP server that exposes the interpreter and the ability to run other MCP servers inside a sandbox. Those are different features. One lets a coding agent call E2B. The other lets untrusted tools run where they cannot see the host. Do not assume both exist in the release you install without checking the docs.

[Riza](https://riza.io/) is an API for untrusted code, with SDKs and an MCP server in the dossier, plus a self-host path. The emphasis in the dossier is a short startup, controlled network and environment, and structured stdout, stderr, and exit status. [briq](https://briq.cloud) describes a Linux microVM the agent starts with a tool call, with Python, Node, git, and a shell, and the same platform starting adjacent services such as a database. Nothing in that description runs on the person's computer. [Runloop](https://runloop.ai) calls its environments devboxes: isolated machines for generated code and longer agent work, with suspend and resume, snapshots, and benchmark jobs. A devbox is closer to a computer that waits than to a function that boots per snippet. That is useful for a coding agent that installs dependencies once, and it is a cleanup problem if you treat it as disposable and it is not.

[Vercel Sandbox](https://vercel.com/docs/sandbox) documents Firecracker microVMs for untrusted and AI-generated code, with Node and Python, snapshots, and a beta notion of persistent sandboxes. It fits if the rest of the deployment is already on Vercel. It is still a sandbox API, not "the agent runs inside a Serverless Function." Functions and microVMs fail differently. Read their docs for the limits on time and network rather than inferring them from the brand.

Hosted sandboxes are the shortest path to "the model wrote Python and it ran somewhere else." The costs are a vendor seeing the code and the files, a network hop, and whatever egress policy the vendor actually enforces. Ask that last question in the docs. An isolated filesystem with open egress is isolated from your disk and not from the internet.

## MicroVMs and fan-out

Firecracker shows up more than once because it is a concrete way to get a machine boundary with a short boot. Vercel Sandbox and [forkd](https://github.com/deeplethe/sandstorm) both use it, for different shapes. forkd's dossier describes a parent microVM that boots and warms once, then child VMs created copy-on-write so a fan-out is closer to a fork than to a cold boot. A live branch can snapshot a running sandbox and resume. That is a runtime for "try five approaches," not a multi-tenant API you sign up for and forget. [SmolVM](https://docs.celesto.ai/smolvm) is another microVM sandbox in the collection, with a Python SDK and snapshots.

The design question is whether you need many sandboxes that share a warm base, or one sandbox per task that shares nothing. Copy-on-write is how you get the first without paying a full boot each time. It is also how a bug in the parent's warmed state reaches every child. A cold microVM per task is simpler to reason about and more expensive in the latency the category cares about.

[CubeSandbox](https://cubesandbox.com) and [Dormice](https://github.com/BitMiracle-AI/Dormice) sit near this conversation as sandbox platforms you can run, Dormice described by its own tagline as a self-hosted system where idle sandboxes are cheap. "Idle is cheap" is an economic claim about paused environments. Confirm the current behavior in the project docs if your cost model depends on it. This guide will not repeat a price.

## Kubernetes, because the cluster is the product

[Kubernetes Agent Sandbox](https://agent-sandbox.sigs.k8s.io) is a SIG API, not a SaaS. The dossier describes a Sandbox custom resource: a stable hostname, storage, create, scheduled delete, pause, and resume, with warm pools and claims as extensions. The official scope is isolated, stateful, singleton workloads. That matches an agent runtime that must still be there after a crash, more than it matches a one-shot calculator.

Choose it when you already operate Kubernetes and you want the sandbox to be a resource your existing policy, identity, and network tools can see. Do not choose it to avoid operating anything. The CRD will not invent a cluster. [OpenSandbox](https://open-sandbox.ai) and [Axern](https://axern.cofy-x.space) are the other "runtime you deploy" listings, OpenSandbox with Kubernetes in the category table and an MCP server recorded there. Their dossiers are thinner than E2B's. Treat thinness as a reason to read the upstream docs carefully, not as a reason to invent features.

[AIO Sandbox](https://github.com/agent-infra/sandbox) is a container image that bundles a browser, a shell, a code environment, and MCP. It belongs in this collection because the agent gets one environment, and it belongs in a browser conversation because a browser is in the image. Use it when splitting "code sandbox" and "browser session" across two vendors is the problem you are trying to avoid. The image is still yours to run.

## On the operator's machine

[CodeRunner](https://github.com/instavm/coderunner) is a local sandbox, using Apple containers in the category table, with MCP. [Clawk](https://github.com/clawkwork/clawk) is a local hypervisor VM with an egress allow-list and a JSON CLI. The tagline is the argument: give the coding agent a disposable Linux machine, not yours.

Local isolation is real only to the depth of the hypervisor and the network policy. A container that mounts the home directory is not a sandbox, even if the CLI says sandbox. Clawk's dossier mentions an egress allow-list because the authors treated the network as part of the boundary. When you evaluate a local project, that is the section to read. Hosted products hide the same question behind a default you should still look up.

[Latchkey](https://latchkey.dev) is the odd one that is still in the right list. It is CI a coding agent can run, read, and fix, with MCP and a jobs API. The "sandbox" is a pipeline rather than a REPL. Use it when the thing that must run is the project's tests, not an arbitrary snippet the model just wrote. A general interpreter will also run the tests, and it will not know what your CI already knows about services and caches.

[The Vibe Hosting](https://thevibehosting.com) is further toward "a machine the agent can leave running," with a skill file for onboarding. A long-lived root shell is a deployment target. It is a poor place to eval untrusted snippets from anonymous users. Match the lifetime of the environment to the trust of the code.

## State, secrets, and the result

The category wants state across calls in one environment, because agents write code in pieces. A pure function sandbox that forgets the filesystem every call forces the agent to resend the world. A sandbox that remembers forever forces you to define forever. Snapshots, which Runloop, Vercel, forkd, and SmolVM document in one form or another, are the middle: keep a known disk, branch it, throw the branch away.

Secrets do not belong in the prompt, and they do not belong in an image you reuse across tenants. Hosted products differ in whether a secret is injected per sandbox and stripped from the output. Read that section of the docs as carefully as the quickstart. An MCP server that runs inside the sandbox, the pattern E2B's dossier describes, is attractive because the tool is jailed, and dangerous if the tool's token is the user's production token. Jail the tool, not only the Python.

The result the agent reads should be structured enough to continue. stdout is necessary and not sufficient when the useful object is a file, a chart, or an exit code. Riza's dossier is explicit about stdout, stderr, and status. Others return files through the SDK. If the only interface is a streamed terminal with no exit status, the agent will guess whether the command worked. Guessing is what the sandbox was supposed to make unnecessary.

## A short sequence

Untrusted snippets from a product you host: a hosted microVM or an API such as E2B, Riza, briq, or Vercel Sandbox, one environment per tenant, network default-deny if the docs allow it.

A coding agent on a laptop: Clawk or CodeRunner, and read the mount and egress story before you grant the repo.

A coding agent that lives in CI: Latchkey or the sandbox your CI already uses, wrapped so the agent can read the log.

A fleet you already run on Kubernetes: the SIG sandbox API, and your own runtime class.

Many parallel attempts that should share a warm runtime: a fork-style microVM, and a plan for how the parent stays trustworthy.

A browser and a shell that must see the same files: AIO or a hosted product that documents both, not two vendors and a hope that you can copy files between them.

The [collection page](/categories/code-execution/) lists the rest, including projects this essay did not need in order to draw the map. Startup milliseconds, concurrent session caps, and prices change. They are not omitted because they do not matter. They are omitted because copying them into a guide would publish a stale benchmark under this site's name.
