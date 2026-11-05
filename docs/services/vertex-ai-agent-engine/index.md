---
title: "Gemini Enterprise Agent Platform (formerly Vertex AI Agent Engine) | Agent-Native Services"
service_name: "Gemini Enterprise Agent Platform (formerly Vertex AI Agent Engine)"
description: "Scale your agents — Gemini Enterprise Agent Platform"
permalink: /services/vertex-ai-agent-engine/
page_kind: service
service_slug: "vertex-ai-agent-engine"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/vertex-ai-agent-engine.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/vertex-ai-agent-engine.md"
tagline: "Scale your agents — Gemini Enterprise Agent Platform"
verified_at: "2026-10-19"
website: "https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale"
repository: "https://github.com/googleapis/python-aiplatform"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · GRPC · SDK · A2A · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-19</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/googleapis/python-aiplatform" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/vertex-ai-agent-engine.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Gemini Enterprise Agent Platform (formerly Vertex AI Agent Engine) is Google Cloud’s managed layer for **running agent workloads in production**. Live docs: *"a fully managed environment for developers to handle testing, release management, and reliability at a global scale"* — **Agent Runtime**, **Sessions**, **Memory Bank**, **Code Execution**, **Computer Use**, plus evaluation and example-store quality loops. Framework guides on the scale page still cover ADK, LangChain, LangGraph, LlamaIndex, AG2, and Agent2Agent (A2A).

---

## Agent-facing interfaces

- **Catalog protocols:** REST, GRPC, SDK, A2A, http
- **MCP:** ⚠️ No standalone MCP server
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `sdk`

## How agents onboard

```bash
pip install "google-cloud-aiplatform[agent_engines,adk]"
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/vertex-ai-agent-engine.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Vertex AI SDK (Python) | `google-cloud-aiplatform` with `agent_engines` — primary path in docs |
| REST / gRPC | Vertex AI platform APIs for ReasoningEngine / agent resources |
| OpenTelemetry | Tracing integration per [runtime tracing docs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/tracing) |
| A2A | Agent2Agent protocol guides remain linked from the [scale hub](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale) |

---

## Verification

Last verified **2026-10-19**.

Sources:
- https://github.com/googleapis/python-aiplatform

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
