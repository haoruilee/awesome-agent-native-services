---
title: "Modal | Agent-Native Services"
service_name: "Modal"
description: "AI infrastructure that developers love"
permalink: /services/modal/
page_kind: service
service_slug: "modal"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/modal.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/modal.md"
tagline: "AI infrastructure that developers love"
website: "https://modal.com"
repository: "https://github.com/modal-labs/modal-client"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI · SDK · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://modal.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://modal.com/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/modal-labs/modal-client" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/modal.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

The machines belong to the vendor. A team writes Python, marks functions with Modal's decorator, and Modal schedules containers with the right image and GPU on its own infrastructure, then scales them down when idle. For an agent system, that means compute an orchestrator can start and stop with an SDK call, without anyone running a cluster. It also means code the agent did not write can run in a sandbox that is not on the orchestrator's own host.

### Functions, sandboxes, endpoints

The dossier describes serverless infrastructure for AI workloads: inference, fine-tuning, batch jobs, notebooks, and sandboxes, with elastic GPU and CPU scaling and unified observability. The primitives are a decorated serverless function with GPU, image, and concurrency settings; sandboxes, described as isolated, ephemeral environments for untrusted execution; volumes and buckets for models and datasets; web endpoints that expose a backend over HTTPS; and scheduling that maps a large batch across many containers.

The agent-facing reason is in the sandboxes and the fan-out. An orchestrator can create a sandbox for code a model just generated, run it, and throw it away. It can also spread an eval or a set of tool calls across parallel containers. The dossier lists evals, RL environments, and hosted MCP servers among the marketed workloads.

Integration is the Python SDK and CLI: `pip install modal`, then `modal setup`, with the CLI handling deploy, run, and logs. HTTP endpoints exist for deployed functions. MCP is marked as not the product's surface; teams deploy their own MCP servers on Modal. No official Agent Skill was located. The [Modal docs](https://modal.com/docs) and the guide they link are where to start.

### Compute rather than an agent framework

Most of [Agent Runtime & Infrastructure](/categories/agent-runtime-and-infrastructure/) packages a specific agent shape. [Cloudflare Agents SDK](/services/cloudflare-agents-sdk/) builds and hosts durable agents on Cloudflare's network. [Letta](/services/letta/) centers on stateful agents. [Cyberdesk](/services/cyberdesk/) provides virtual desktops for computer-use agents. Modal is lower in the stack: general compute that an agent system calls, with no opinion about memory, conversation state, or tool schemas. That makes it a host for pieces of an agent rather than an agent runtime. The guide on [what makes a service agent-native](/guides/what-makes-a-service-agent-native/) explains why sandboxes for agent-generated code are counted as an agent primitive here.

### Isolation and secrets to confirm

Modal tokens authenticate API access, secrets are injected as environment variables or Modal secret objects rather than placed in prompts, and team policies govern who can deploy and spend. Check how narrowly a token can be scoped, because an orchestrator holding a full deploy token can do more than create sandboxes.

The dossier does not describe the sandbox isolation boundary, network egress rules inside a sandbox, or how long sandbox state persists. For agent-generated code, those are the questions that matter most, so read the Sandboxes product page and the guide before routing untrusted code there. Data residency is listed as a team control; confirm the regions you need.

### Editor's take

Python teams that need GPUs on demand, parallel evals, or a place to execute model-written code without running Kubernetes have the clearest case. If you want a framework that already manages agent state and conversations, Letta or the Cloudflare Agents SDK start further along. Our read draws on the dossier and Modal's guide and product pages; the project has not deployed a function there.

</section>

## What it does

Modal is **serverless infrastructure for AI workloads**: **inference**, **fine-tuning**, **batch** jobs, **notebooks**, and **dynamic sandboxes** with **sub-second cold starts**, **elastic GPU/CPU** scaling, and **unified observability**. It is explicitly marketed for **LLM inference**, **evals**, **RL environments**, and **MCP servers** at scale — workloads that autonomous agents and their orchestrators spawn unpredictably.

---

## Agent-facing interfaces

- **Catalog protocols:** CLI, SDK, http
- **MCP:** ⚠️ Not an MCP product; teams deploy MCP servers on Modal (see customer quotes on modal.com).
- **Agent Skill:** ⚠️ No official AgentSkills bundle located.
- **Onboarding type:** `sdk`

## How agents onboard

```bash
pip install modal
modal setup
# Define Modal app in Python per https://modal.com/docs/guide
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/modal.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install modal` |
| CLI | `modal` — deploy, run, logs |
| HTTP | Function endpoints — see docs |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
