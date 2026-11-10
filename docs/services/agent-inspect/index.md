---
title: "agent-inspect | Agent-Native Services"
service_name: "agent-inspect"
description: "Local execution trees for TypeScript AI agents"
permalink: /services/agent-inspect/
page_kind: service
service_slug: "agent-inspect"
category_slug: "observability-and-tracing"
category_label: "Observability & Tracing"
hero_image: "/assets/images/editorial-observability.webp"
image: "/assets/images/editorial-observability.webp"
classification: "agent-native"
dossier_path: "services/observability-and-tracing/agent-inspect.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/agent-inspect.md"
tagline: "Local execution trees for TypeScript AI agents"
website: "https://github.com/rajudandigam/agent-inspect"
repository: "https://github.com/rajudandigam/agent-inspect"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Observability &amp; Tracing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/rajudandigam/agent-inspect" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/rajudandigam/agent-inspect" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/agent-inspect.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

A TypeScript agent that calls a model, then three tools, then the model again, produces a nested sequence of events. When it misbehaves, a developer wants that nesting on screen: which step spawned which, and where the run turned. The agent-inspect project, tagged "Local execution trees for TypeScript AI agents," aims at exactly that view and little else.

### A tree in the terminal

The dossier describes three parts: TypeScript instrumentation, execution trees rendered in the terminal, and run metadata. Onboarding is to add the package to a TypeScript agent project and emit execution trees. That makes it an in-process tool. It is imported into the agent's own code, unlike a wrapper that watches a process from outside, and its output lands where the developer is already looking.

The record is thin on specifics. It does not show the import, name the instrumentation calls, or say whether trees can be written to a file or shipped elsewhere. MCP is marked as not the primary verified surface, and no Agent Skill is listed. The library is the documented path. The [GitHub repository](https://github.com/rajudandigam/agent-inspect) is the only vendor source the catalog cites, so check it for supported agent frameworks, how much code change instrumentation needs, and what run metadata is captured.

### Local first, platform later

Most of the [observability and tracing collection](/categories/observability-and-tracing/) assumes a server somewhere. [Langfuse](/services/langfuse/), [LangWatch](/services/langwatch/), and [Braintrust](/services/braintrust/) store traces, attach evaluations, and give a team a shared place to look. agent-inspect asks for none of that. The nearest neighbor is [Agent Trace](/services/agent-trace/), which also stays on one machine but wraps a run with a CLI and talks about OpenTelemetry-style traces and cost visibility instead of a code-level tree.

The practical split is language and depth. A wrapper works on any agent you can launch from a shell but sees what crosses the process boundary. An in-process library sees the structure the code itself creates, and only works where it can be imported, here TypeScript. Neither replaces a platform once several people need the same history. The [guide to what makes a service agent-native](/guides/what-makes-a-service-agent-native/) treats machine-readable output as a requirement. A terminal tree is readable by a person first, so check whether the run metadata is also available in a form a second agent could parse.

### Editor's take

For a single developer building a TypeScript agent who wants to see the shape of each run without signing up for anything, agent-inspect is a reasonable first tool. Python teams, or anyone who needs traces kept and searched across many runs, should look at Langfuse or LangWatch. If you cannot change the agent's code, Agent Trace's wrapper approach is the alternative. What is written here comes from the dossier and the public repository; no one on the index has instrumented an agent with this library.

</section>

## What it does

agent-inspect provides local execution trees for TypeScript AI agents. Its agent-facing value is to give autonomous systems a programmatic primitive that can be invoked during a task loop without requiring a human to operate a dashboard for each action.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, http
- **MCP:** ⚠️ MCP support is not the primary verified surface for this entry.
- **Agent Skill:** ⚠️ No dedicated catalog skill verified in this entry. Search ClawHub or the upstream README for the latest installable skills.
- **Onboarding type:** `other`

## Protocol surface

| Interface | Detail |
|---|---|
| **Primary surface** | TypeScript instrumentation, terminal execution trees, run metadata |
| **Repository** | https://github.com/rajudandigam/agent-inspect |
| **MCP** | ⚠️ |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/observability-and-tracing/' | relative_url }}"><small>Collection</small><strong>← Observability &amp; Tracing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
