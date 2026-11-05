---
title: "AgentSight | Agent-Native Services"
service_name: "AgentSight"
description: "lightweight system-level observability for AI Agents"
permalink: /services/agentsight/
page_kind: service
service_slug: "agentsight"
category_slug: "observability-and-tracing"
category_label: "Observability & Tracing"
hero_image: "/assets/images/editorial-observability.webp"
image: "/assets/images/editorial-observability.webp"
classification: "agent-native"
dossier_path: "services/observability-and-tracing/agentsight.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/agentsight.md"
tagline: "lightweight system-level observability for AI Agents"
verified_at: "2026-10-13"
website: "https://eunomia.dev/agentsight/"
repository: "https://github.com/eunomia-bpf/agentsight"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Observability &amp; Tracing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://eunomia.dev/agentsight/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://eunomia.dev/agentsight/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/eunomia-bpf/agentsight" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/agentsight.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

AgentSight is a local-first `top`/`strace`-like observer for AI agents. Docs title: **"System-wide AI agent profiling and monitoring with eBPF"**. GitHub description: **"lightweight system-level observability for AI Agents"**. It correlates prompts, model calls, and tool decisions with **real host effects** — processes, files, network, TLS payloads at SSL call boundaries — without an SDK, proxy, or vendor hook inside the agent.

`record` writes `agentsight-*.db` session files. `report` queries them (prompts JSON, token grouping, audit JSON). Optional OTLP/HTTP export emits OpenTelemetry **GenAI** (`gen_ai.*`) spans. `top` / `vis` / `report` can also read native Claude/Codex/Gemini session files without eBPF; `record` and live eBPF need Linux + privileges.

**Complement, don't replace:** [Langfuse](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/langfuse.md) and [Laminar](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/laminar.md) are application/trace products (you instrument or proxy the app). [numbat](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/numbat.md) is endpoint/hook visibility with optional pre-action blocking. AgentSight is **system-level eBPF + session files + OTLP GenAI**, including closed-source CLIs that never called an SDK.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI wrapper (operator-surface track)
- **Catalog protocols:** CLI, http
- **MCP:** ⚠️ Not an MCP server.
- **Agent Skill:** ⚠️ No official Agent Skills package published.
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI wrapper (operator-surface track)

```bash
cargo install agentsight
# or: brew tap eunomia-bpf/tap && brew install eunomia-bpf/tap/agentsight

agentsight top
sudo agentsight record -- claude
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/agentsight.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `cargo install agentsight` / Homebrew tap `eunomia-bpf/tap` |
| Rust library | `agentsight-capture` |
| OTLP/HTTP | GenAI spans |
| Local UI | `http://127.0.0.1:7395` during a session; `report serve` for a saved DB |
| Session files | SQLite `agentsight-*.db`; `~/.agentsight/monitor` for the background service |

---

## Verification

Last verified **2026-10-13**.

Sources:
- https://api.github.com/repos/eunomia-bpf/agentsight

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/observability-and-tracing/' | relative_url }}"><small>Collection</small><strong>← Observability &amp; Tracing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
