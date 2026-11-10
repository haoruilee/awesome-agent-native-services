---
title: "Vercel Sandbox | Agent-Native Services"
service_name: "Vercel Sandbox"
description: "Secure, isolated microVMs for AI-generated code"
permalink: /services/vercel-sandbox/
page_kind: service
service_slug: "vercel-sandbox"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/vercel-sandbox.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/vercel-sandbox.md"
tagline: "Secure, isolated microVMs for AI-generated code"
website: "https://vercel.com/docs/sandbox"
repository: "https://github.com/vercel/sandbox"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · CLI · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://vercel.com/docs/sandbox" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://vercel.com/docs/sandbox" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/vercel/sandbox" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/vercel-sandbox.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

Code a model just wrote should not run on the machine that wrote it. An agent acting as a code interpreter, or running tests on a cloned repository, needs a disposable computer per task: start it, push code in, read the output, throw it away. Vercel's offering for that is a microVM service, which the docs describe as "Secure, isolated microVMs for AI-generated code."

### A microVM per turn

The dossier describes Firecracker microVMs with full Node.js and Python runtimes. Each sandbox has its own filesystem and network policy. An agent, or the application hosting it, creates a sandbox, streams code or commands into it, reads stdout and files, optionally reaches an HTTP preview URL, and then snapshots or destroys the VM. Commands stream their output, so a long test run does not have to finish before the agent sees anything.

Three interfaces are documented. The TypeScript SDK installs with `npm install @vercel/sandbox`, and the [SDK reference](https://vercel.com/docs/sandbox/sdk-reference) lists its methods. The REST API creates sandboxes with `POST /v1/sandboxes`. A `sandbox` CLI is described for manual and agent-driven debugging. There is no dedicated first-party MCP server, and no official Agent Skill bundle was located. Agents reach it through the SDK or REST from their own runtime.

### Snapshots and the long task

Snapshots save and restore VM state. Persistent sandboxes, marked beta in the dossier, save state across stops automatically. Together they address tasks that outlast one turn, such as a multi-step refactor where the agent wants yesterday's environment back instead of reinstalling dependencies. Check the [Vercel Sandbox docs](https://vercel.com/docs/sandbox) for what a snapshot includes, how long it is kept, and what beta means for persistence guarantees. The docs, not this page, are the place for cold-start times, limits, and pricing.

Credentials are Vercel personal or team tokens, or OIDC when the caller is itself deployed on Vercel. Billing and quotas attach to the team. Isolation is per sandbox, and the host application decides which agents may create one. That last point is easy to miss. The sandbox contains the code, but it does not decide who gets to start sandboxes. Your application does.

### Editor's take

The [code execution collection](/categories/code-execution/) and the [sandboxes guide](/guides/sandboxes-and-code-execution/) cover hosted and local options. [E2B](/services/e2b/) is the most direct hosted comparison, also built around sandboxes for AI-generated code. [OpenSandbox](/services/opensandbox/) and [Axern](/services/axern/) are open-source runtimes you operate. [CodeRunner](/services/coderunner/) keeps execution on the local machine. [AIO Sandbox](/services/agent-infra-sandbox/) bundles browser, shell, files, and MCP in one container, which suits agents that need more than a process.

Teams already deploying on Vercel get the shortest path here, with OIDC instead of a stored token and billing on an existing account. Outside Vercel, compare E2B on features and an open-source runtime on control. Our position comes from reading the dossier and Vercel's public docs, not from creating or snapshotting a sandbox ourselves.

</section>

## What it does

Vercel Sandbox provides **Firecracker microVMs** with fast cold start, full **Node.js and Python** runtimes, optional **snapshots** for save/resume, and **persistent sandboxes** (beta). Documentation positions it for **AI agents**, **AI-generated code**, and **untrusted code** execution at scale.

---

## Agent-facing interfaces

- **Catalog protocols:** REST, CLI, SDK, http, API
- **MCP:** ⚠️ Not yet published as a dedicated first-party MCP server
- **Agent Skill:** ⚠️ No official npx skills add vercel/... bundle located.
- **Onboarding type:** `sdk`

## How agents onboard

```bash
npm install @vercel/sandbox
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/vercel-sandbox.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| TypeScript | `@vercel/sandbox` — [SDK reference](https://vercel.com/docs/sandbox/sdk-reference) |
| REST API | [Sandboxes REST](https://vercel.com/docs/rest-api/sandboxes/create-a-sandbox) |
| CLI | `sandbox` CLI for manual and agentic debugging workflows |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
