---
title: "Amazon Bedrock AgentCore | Agent-Native Services"
service_name: "Amazon Bedrock AgentCore"
description: "Purpose-built for deploying and scaling dynamic AI agents and tools"
permalink: /services/amazon-bedrock-agentcore/
page_kind: service
service_slug: "amazon-bedrock-agentcore"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/amazon-bedrock-agentcore.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/amazon-bedrock-agentcore.md"
tagline: "Purpose-built for deploying and scaling dynamic AI agents and tools"
website: "https://aws.amazon.com/bedrock/agentcore/"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://aws.amazon.com/bedrock/agentcore/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/amazon-bedrock-agentcore.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Amazon Bedrock AgentCore is a modular, purpose-built agent runtime suite from AWS. Unlike Bedrock's model inference APIs (which are general-purpose), AgentCore addresses the specific operational problems of running agents at scale: **Runtime** (managed execution), **Memory** (session and cross-session persistence), **Identity** (verified agent tokens), **Gateway** (tool access routing and security), and **Observability** (OpenTelemetry-based tracing and dashboards).

---

## Agent-facing interfaces

- **Catalog protocols:** REST, SDK, API
- **MCP:** ⚠️ No standalone MCP server
- **Agent Skill:** ⚠️ No official skill published by AWS for AgentCore yet.
- **Onboarding type:** `sdk`

## Protocol surface

| Interface | Detail |
|---|---|
| AWS SDK | Primary integration surface for all AgentCore modules |
| REST API | AgentCore management and query APIs |
| OpenTelemetry | OTEL-compatible telemetry export |
| CloudWatch | Metrics, traces, and logs dashboard |
| ADOT SDK | AWS Distro for OpenTelemetry for custom instrumentation |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
