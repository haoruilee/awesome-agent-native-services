---
title: "SmolVM | Agent-Native Services"
service_name: "SmolVM"
description: "SmolVM: secure microVM sandboxes for AI agents"
permalink: /services/smolvm/
page_kind: service
service_slug: "smolvm"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/smolvm.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/smolvm.md"
tagline: "SmolVM: secure microVM sandboxes for AI agents"
verified_at: "2026-09-26"
website: "https://docs.celesto.ai/smolvm"
repository: "https://github.com/CelestoAI/celesto"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI · SDK · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://docs.celesto.ai/smolvm" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.celesto.ai/smolvm" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/CelestoAI/celesto" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/smolvm.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

SmolVM gives AI agents a **disposable computer**: a hardware-isolated microVM that boots in hundreds of milliseconds, runs arbitrary code or a full browser, can mount host directories, snapshot/restore, and disappear when the task ends. One API covers Firecracker (Linux), QEMU (macOS), and libkrun.

Docs body (live): “SmolVM gives AI agents their own disposable computer. Each microVM boots in milliseconds, runs any code or software you throw at it, persists files and state across sessions, and disappears when you're done — built for scale in production.”

**Distinct from catalog peers:**

| Peer | Difference |
|---|---|
| [E2B](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/e2b.md) | Hosted cloud sandboxes. SmolVM is local/self-host multi-VMM |
| [CubeSandbox](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/cubesandbox.md) | E2B-compatible self-host *service* (cluster API). SmolVM is an SDK/CLI on the machine |
| [forkd](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/forkd.md) | Firecracker CoW fork/BRANCH fan-out. SmolVM is create/run/snapshot of a single disposable VM |
| [OpenSandbox](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/opensandbox.md) | K8s/runtime abstraction + MCP |
| [Clawk](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/clawk.md) | Local hypervisor VM for one coding agent on a desk (macOS). SmolVM is Linux+macOS+Windows guests with a unified SDK |

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + Python SDK
- **Catalog protocols:** CLI, SDK, http
- **MCP:** ⚠️ Not yet published as a first-party MCP server.
- **Agent Skill:** ⚠️ No official npx skills add package published yet.
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI + Python SDK

```bash
curl -sSL https://celesto.ai/install.sh | bash
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/smolvm.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Installer | `curl -sSL https://celesto.ai/install.sh \| bash` |
| Python SDK | `from smolvm import SmolVM` |
| CLI | `smolvm sandbox`, `smolvm browser`, `smolvm claude start` |
| Docs | https://docs.celesto.ai/smolvm · llms.txt index |
| License | Apache-2.0 |

---

## Verification

Last verified **2026-09-26**.

Sources:
- https://api.github.com/repos/CelestoAI/celesto
- https://docs.celesto.ai/smolvm

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
