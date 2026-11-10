---
title: "Meeting & Conversation | Agent-Native Services"
collection_label: "Meeting & Conversation"
description: "Programmatic agent presence in live meetings, shared rooms, and conversation streams."
hero_image: "/assets/images/editorial-meeting.webp"
hero_image_alt: "A cream pedestal holding a gold ring, with three black spheres in a sunlit corner."
image: "/assets/images/editorial-meeting.webp"
permalink: /categories/meeting-and-conversation/
page_kind: collection
collection_number: "13"
service_count: 7
---

<p class="collection-source"><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/README.md">Collection notes ↗</a></p>

<div class="collection-essay" markdown="1">

Video meetings were built for a person who clicks Join. An agent that needs the audio, the speakers, or a speaking slot has to be brought in by something that can sit on the call. This collection is that layer. A phone number is the neighboring one.

Recall.ai is documented as a meeting-bot API across conferencing platforms. Meeting BaaS is the same idea as a developer API for meeting data and bots. MeetStream focuses on recordings, transcripts, and metadata. Vexa is an open-source transcription API for Google Meet, Teams, and Zoom, including auto-join in its own description. Daily's Agent Toolkit is for realtime agents on Daily rather than a bot that dials into someone else's bridge. AgentCall and joinly.ai are framed as putting an agent into the meeting itself. Capture and presence are different jobs. A transcript webhook does not speak. A bot that talks needs a media path.

Platform coverage and speaker labels change, and they are documented per vendor rather than scored here. The useful questions are which meetings the bot can join, whether the transcript names speakers, and whether a calendar event can start the bot without a person clicking. Consent to record is a property of the meeting and the region, not a feature flag this catalog can grant. If the agent needs to dial a telephone number, look at Voice & Phone instead.

</div>

<div class="service-grid">
  <article class="service-card service-card--new atlas-sheet--service atlas-visual--01">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://agentcall.dev" rel="noopener noreferrer">AgentCall</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/agentcall/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Your AI agent, in every meeting.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/agentcall/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/agentcall.md">Dossier ↗</a>
      <a href="https://github.com/pattern-ai-labs/agentcall">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--02">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://www.daily.co" rel="noopener noreferrer">Daily Agent Toolkit</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/daily-agent/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Build realtime meeting agents on Daily.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/daily-agent/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/daily-agent.md">Dossier ↗</a>
      <a href="https://github.com/daily-co/daily-python">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--service atlas-visual--03">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://joinly.ai" rel="noopener noreferrer">joinly.ai</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/joinly/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Make your meetings accessible to AI Agents!</p>
    <div class="service-card__actions">
      <a href="{{ '/services/joinly/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/joinly.md">Dossier ↗</a>
      <a href="https://github.com/joinly-ai/joinly">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--04">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://meetingbaas.com" rel="noopener noreferrer">Meeting BaaS</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/meeting-baas/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Meeting Bots As A Service — The developer API for programmatic access to meeting data across Zoom, Google Meet, and Microsoft Teams.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/meeting-baas/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/meeting-baas.md">Dossier ↗</a>
      <a href="https://github.com/Meeting-Baas">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--05">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://meetstream.ai" rel="noopener noreferrer">MeetStream</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/meetstream/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">API &amp; Infrastructure to capture recordings, transcripts &amp; metadata from meetings.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/meetstream/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/meetstream.md">Dossier ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--06">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://recall.ai" rel="noopener noreferrer">Recall.ai</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/recall-ai/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">The meeting bot API for every platform.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/recall-ai/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/recall-ai.md">Dossier ↗</a>
      <a href="https://github.com/recallai">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--07">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://vexa.ai" rel="noopener noreferrer">Vexa</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/vexa/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Open-source meeting transcription API for Google Meet, Microsoft Teams &amp; Zoom. Auto-join bots, real-time WebSocket transcripts, MCP server for AI agents. Self-host or use hosted SaaS.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/vexa/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/meeting-and-conversation/vexa.md">Dossier ↗</a>
      <a href="https://github.com/Vexa-ai/vexa">Official repo ↗</a>
    </div>
    </div>
  </article>
</div>
<nav class="collection-pagination" aria-label="Adjacent collections">
  <a href="{{ '/categories/durable-execution-and-scheduling/' | relative_url }}"><small>Previous collection</small><strong>← Durable Execution & Scheduling</strong></a>
  <a href="{{ '/categories/voice-and-phone/' | relative_url }}"><small>Next collection</small><strong>Voice & Phone →</strong></a>
</nav>
