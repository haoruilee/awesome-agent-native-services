---
title: "Braintrust | Agent-Native Services"
service_name: "Braintrust"
description: "Ship quality AI at scale — AI observability and evaluation"
permalink: /services/braintrust/
page_kind: service
service_slug: "braintrust"
category_slug: "observability-and-tracing"
category_label: "Observability & Tracing"
hero_image: "/assets/images/editorial-observability.webp"
image: "/assets/images/editorial-observability.webp"
classification: "agent-native"
dossier_path: "services/observability-and-tracing/braintrust.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/braintrust.md"
tagline: "Ship quality AI at scale — AI observability and evaluation"
website: "https://www.braintrust.dev"
repository: "https://github.com/braintrustdata/autoevals"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Observability &amp; Tracing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.braintrust.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://www.braintrust.dev/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/braintrustdata/autoevals" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/braintrust.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

### Open questions first

Two things are left loose in the dossier. It records no verified Agent Skill bundle, so a coding agent cannot be handed a single `SKILL.md` and told to get on with it. And it mentions hybrid and self-hosted data plane options in one line, without saying which components run where, who upgrades them, or what still talks to the vendor. Anyone whose prompts cannot leave their network should treat that line as a pointer to the [Braintrust docs](https://www.braintrust.dev/docs), not as an answer.

What the dossier does document is a loop. Agent code initializes a logger and a trace processor. Every LLM call, tool call, and retriever step lands as a nested span. Scorers built from code, LLM judges, or human review grade the output, and traces that fail become dataset rows for the next regression run. The OpenAI Agents SDK path is specific: install `braintrust[openai-agents]` and register `BraintrustTracingProcessor`. Python, TypeScript, Go, Ruby, and C# SDKs are listed, along with a REST API and a storage engine called Brainstore built for large nested traces.

### Two ways in

The SDK serves the agent being observed. The MCP server serves a different agent: the coding assistant that reads the results. The dossier gives a hosted HTTP endpoint at `api.braintrust.dev/mcp`, a separate EU endpoint, and bearer-token auth with an API key, with OAuth also mentioned. Through it, an IDE agent can query logs, run evals, and manage prompts without leaving the editor.

That split matters for credentials. The key in a production agent's environment and the key in an editor's MCP config do not need the same reach. The dossier says API keys scope access to org and project data, with RBAC deciding who can view traces that may hold sensitive prompts. How narrow a key can be made is a docs question worth settling before one key gets reused in both places.

### Against the rest of the category

The [Observability & Tracing](/categories/observability-and-tracing/) collection holds several products that trace agent runs. [Langfuse](/services/langfuse/) describes itself as open-source LLM observability, tracing, and evaluation. [OpenLIT](/services/openlit/) is OpenTelemetry-native. [AgentEvals](/services/agentevals/) scores agents from existing OpenTelemetry traces without re-running them. Braintrust's weight, per the dossier, sits on the experiment side: comparing prompts and models against datasets and blocking a release when scorers regress, with tracing feeding that loop. The vendor's tagline, "Ship quality AI at scale", points the same way. The catalog's reasons for listing an eval platform at all are in [What makes a service agent-native](/guides/what-makes-a-service-agent-native/).

### Editor's take

Teams already on the OpenAI Agents SDK who want evals as a release gate get a short path here: one processor, a dataset loop, and an MCP endpoint their coding agent can query. If the requirement is source code you can run yourself, start with Langfuse or OpenLIT and come back if the experiment tooling is what you miss. This page is a reading of the catalog dossier and Braintrust's published docs; nobody on this project has instrumented an agent with it.

</section>

## What it does

Braintrust is an **AI observability and evaluation** platform: **trace** every LLM call, tool invocation, and intermediate step in production; **score** outputs with code, LLM judges, or humans; **compare** prompts and models; and **convert traces to datasets** for regression testing. It explicitly targets **agents** — e.g. native **OpenAI Agents SDK** trace processors — and exposes an **MCP server** so coding agents can query experiments and logs directly.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, SDK, http, API
- **MCP:** ✅ Hosted MCP endpoint for coding agents and IDEs.
- **Agent Skill:** ⚠️ No single npx skills add bundle verified; MCP exposes logs, evals, and prompt workflows to compatible hosts.
- **Onboarding type:** `sdk`

## How agents onboard

```bash
pip install "braintrust[openai-agents]"
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/braintrust.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install braintrust` / `braintrust[openai-agents]` |
| TypeScript SDK | `@braintrust/*` packages per docs |
| MCP | HTTPS `api.braintrust.dev/mcp` |
| REST API | https://www.braintrust.dev/docs/api-reference/introduction |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/observability-and-tracing/' | relative_url }}"><small>Collection</small><strong>← Observability &amp; Tracing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
