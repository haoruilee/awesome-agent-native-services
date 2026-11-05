---
title: "Qwen Audio Agent | Agent-Native Services"
service_name: "Qwen Audio Agent"
description: "A realtime voice runtime that keeps Agents talking, working, and present"
permalink: /services/qwen-audio-agent/
page_kind: service
service_slug: "qwen-audio-agent"
category_slug: "voice-and-phone"
category_label: "Voice & Phone"
hero_image: "/assets/images/editorial-voice.webp"
image: "/assets/images/editorial-voice.webp"
classification: "agent-native"
dossier_path: "services/voice-and-phone/qwen-audio-agent.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/qwen-audio-agent.md"
tagline: "A realtime voice runtime that keeps Agents talking, working, and present"
verified_at: "2026-09-26"
website: "https://github.com/QwenAudio/qwen-audio-agent"
repository: "https://github.com/QwenAudio/qwen-audio-agent"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Voice &amp; Phone</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache 2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI · ACP · STDIO</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/QwenAudio/qwen-audio-agent" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/QwenAudio/qwen-audio-agent/tree/main/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/QwenAudio/qwen-audio-agent" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/qwen-audio-agent.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Qwen Audio Agent is a local realtime voice front end for persistent tool-using agents. The voice layer keeps listening and speaking while long-running work continues asynchronously, so the conversation does not freeze during searches, code changes, or other tool calls. Users can ask for status, cancel work, interrupt speech naturally, and receive the completed result back in the originating conversation.

Its architecture separates a low-latency realtime assistant from one persistent backend-agent session. Requests that need tools are converted into Work records and sent through ACP to OpenCode, OpenClaw, Qoder, Qwen Code, Kimi Code, Hermes, CodeBuddy, Codex, Claude Code, or another ACP-compatible agent. The desktop, WebUI, and TUI share the same gateway primitives, local memory boundaries, permission relay, and result-delivery semantics.

---

## Agent-facing interfaces

- **Interaction pattern:** Daemon / CLI
- **Catalog protocols:** CLI, ACP, STDIO
- **MCP:** ⚠️ No MCP server exposed by Qwen Audio Agent. It connects to backend agents through ACP and can reuse the backend's configured MCP servers and tools.
- **Agent Skill:** ⚠️ No official Qwen Audio Agent SKILL.md is published.
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** Daemon / CLI

```bash
npm install -g qwen-audio-agent
qwenaudio config                 # add realtime voice credentials and optional backend
qwenaudio                        # start the local Gateway
qwenaudio tui                    # in another terminal; or: qwenaudio webui
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/voice-and-phone/qwen-audio-agent.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| ACP | Native or adapted stdio connections to supported backend coding agents; session new/resume/update/cancel semantics |
| CLI | `qwenaudio`, `config`, `setup`, `install`, `tui`, `webui`, and `gateway` service controls |
| Local Gateway | Coordinates realtime sessions, Work queues, task state, permission requests, and frontend clients |
| Voice Frontends | DashScope Qwen realtime models or a local Hugging Face speech-to-speech pipeline |
| User Interfaces | Terminal TUI, browser WebUI, and desktop floating orb for macOS, Windows, and Linux |
| Local State | Markdown identity/preferences/memory files, JSON task recovery, and redacted JSONL logs |

---

## Verification

Last verified **2026-09-26**.

Sources:
- https://github.com/QwenAudio/qwen-audio-agent/releases/tag/v2.0.0
- https://qwenaudio.github.io/qwen-audio-agent/
- https://api.github.com/repos/QwenAudio/qwen-audio-agent

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/voice-and-phone/' | relative_url }}"><small>Collection</small><strong>← Voice &amp; Phone</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
