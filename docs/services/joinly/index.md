---
title: "joinly.ai | Agent-Native Services"
service_name: "joinly.ai"
description: "Make your meetings accessible to AI Agents!"
permalink: /services/joinly/
page_kind: service
service_slug: "joinly"
category_slug: "meeting-and-conversation"
category_label: "Meeting & Conversation"
hero_image: "/assets/images/editorial-meeting.webp"
image: "/assets/images/editorial-meeting.webp"
classification: "agent-native"
dossier_path: "services/meeting-and-conversation/joinly.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/joinly.md"
tagline: "Make your meetings accessible to AI Agents!"
verified_at: "2026-10-20"
website: "https://joinly.ai"
repository: "https://github.com/joinly-ai/joinly"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Meeting &amp; Conversation</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-20</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://joinly.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/joinly-ai/joinly#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/joinly-ai/joinly" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/joinly.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

joinly.ai puts an **AI participant** into Zoom, Google Meet, or Microsoft Teams (browser-based). Official README: live voice/chat interaction, interruption-aware conversational flow, bring-your-own LLM, pluggable STT/TTS (Whisper/Kokoro local defaults; Deepgram/ElevenLabs optional). Self-host via Docker (~2.3 GB with browser + models); CUDA image available.

**Distinct from catalog peers:**

| Peer | Difference |
|---|---|
| [Vexa](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/vexa.md) | Self-host **transcription + interactive bot API** (17 MCP tools, REST). joinly is middleware: any agent talks MCP to a meeting connector |
| [AgentCall](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/agentcall.md) | Hosted **join-meeting Skill** (`ak_ac_` keys), not an OSS MCP server you run |

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + MCP server
- **Catalog protocols:** MCP
- **MCP:** ✅ Available — MCP is the backbone (homepage: “MCP: The backbone of joinly”)
- **Agent Skill:** ⚠️ No official npx skills add package published yet.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** CLI + MCP server

```bash
docker pull ghcr.io/joinly-ai/joinly:latest
# Quickstart client-in-container (no external MCP):
docker run --env-file .env ghcr.io/joinly-ai/joinly:latest --client <MeetingURL>

# Server mode — bind localhost only:
docker run -p 127.0.0.1:8000:8000 ghcr.io/joinly-ai/joinly:latest
uvx joinly-client --env-file .env <MeetingUrl>
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/joinly.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Docker MCP | `ghcr.io/joinly-ai/joinly:latest` (`--client` or server `:8000`) |
| Client | `uvx joinly-client` / PyPI `joinly-client` |
| Extra tools | `--mcp-config` JSON (`mcpServers`) |
| Cloud | Former optional host `cloud.joinly.ai` — DNS dead as of 2026-09-08; not required |

---

## Verification

Last verified **2026-10-20**.

Sources:
- https://api.github.com/repos/joinly-ai/joinly

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/meeting-and-conversation/' | relative_url }}"><small>Collection</small><strong>← Meeting &amp; Conversation</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
