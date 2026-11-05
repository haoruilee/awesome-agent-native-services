---
title: "AIO Sandbox (agent-infra) | Agent-Native Services"
service_name: "AIO Sandbox (agent-infra)"
description: "AIO Sandbox is an all-in-one agent sandbox environment that combines Browser, Shell, File, MCP operations, and VSCode Server in a single Docker container"
permalink: /services/agent-infra-sandbox/
page_kind: service
service_slug: "agent-infra-sandbox"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/agent-infra-sandbox.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/agent-infra-sandbox.md"
tagline: "AIO Sandbox is an all-in-one agent sandbox environment that combines Browser, Shell, File, MCP operations, and VSCode Server in a single Docker container"
website: "https://github.com/agent-infra/sandbox"
repository: "https://github.com/agent-infra/sandbox"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · CLI · SDK · openapi</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/agent-infra/sandbox" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="http://localhost:8080/v1/docs (when container running) · https://github.com/agent-infra/sandbox" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/agent-infra/sandbox" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/agent-infra-sandbox.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

AIO Sandbox provides a **single isolated environment** where agents can use a **real browser (VNC)**, **shell**, **files**, **Jupyter**, **VS Code Server**, and **MCP** together with a **unified filesystem** — addressing coordination friction when separate single-purpose sandboxes cannot share artifacts. README markets it as **agent-ready** with **MCP-compatible APIs**.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, CLI, SDK, openapi
- **MCP:** ✅ Built-in MCP HTTP endpoint in the container
- **Agent Skill:** ⚠️ Not yet published as a dedicated npx skills add … pack
- **Onboarding type:** `cli`

## How agents onboard

```bash
docker run --security-opt seccomp=unconfined --rm -it -p 8080:8080 ghcr.io/agent-infra/sandbox:latest
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/agent-infra-sandbox.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **REST/OpenAPI** | `/v1/docs` on port 8080 |
| **MCP** | `/mcp` on port 8080 |
| **VNC / VS Code / Jupyter** | Browser-accessible URLs in README |
| **SDKs** | PyPI, npm, Go module per repo |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
