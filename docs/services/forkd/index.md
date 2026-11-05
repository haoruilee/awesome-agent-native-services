---
title: "forkd | Agent-Native Services"
service_name: "forkd"
description: "A microVM sandbox runtime for AI agent fan-out"
permalink: /services/forkd/
page_kind: service
service_slug: "forkd"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/forkd.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/forkd.md"
tagline: "A microVM sandbox runtime for AI agent fan-out"
verified_at: "2026-10-20"
website: "https://github.com/deeplethe/sandstorm"
repository: "https://github.com/deeplethe/sandstorm"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · CLI · SDK</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-20</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/deeplethe/sandstorm" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/deeplethe/sandstorm/blob/dev/README.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/deeplethe/sandstorm" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/forkd.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

forkd is a **Firecracker copy-on-write sandbox runtime** for AI-agent fan-out. A parent microVM boots once, warms the runtime (imports, JIT, model weights), and is paused to disk. Each child is a separate Firecracker process that `mmap`s the parent with `MAP_PRIVATE`, so spawn cost is closer to `fork(2)` than to a cold-boot VM.

**BRANCH** pauses a *live* sandbox, snapshots in-flight state, and resumes so an agent can fork mid-thought — not only at warm-up. v0.4 live BRANCH advertises a 56 ms p50 pause window; v0.5 adds stacked diff-snapshot chains.

**Distinct from catalog peers:**

| Peer | Difference |
|---|---|
| [E2B](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/e2b.md) | Hosted cold-start cloud VMs. forkd is self-host Firecracker **fork-from-warm** |
| [CubeSandbox](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/cubesandbox.md) | E2B-compatible self-host microVMs (pool / cold-start). forkd’s primitive is CoW fork + live BRANCH |
| [OpenSandbox](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/opensandbox.md) | Runtime abstraction over Docker/K8s/etc. |
| [SmolVM](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/smolvm.md) | Disposable agent computers (Firecracker/QEMU/libkrun). No fork/BRANCH fan-out primitive |
| [Dormice](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/dormice.md) | Cheap-idle E2B-compat daemon, not Firecracker CoW fork |

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + REST / SDK / MCP
- **Catalog protocols:** MCP, REST, CLI, SDK
- **MCP:** ✅ Available — forkd-mcp
- **Agent Skill:** ⚠️ No official npx skills add package published yet.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** CLI + REST / SDK / MCP

```bash
curl -sSL https://github.com/deeplethe/sandstorm/releases/download/v0.5.3/forkd-v0.5.3-x86_64-linux.tar.gz \
  | sudo tar -xz -C /usr/local/bin/
sudo -E forkd quickstart
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/forkd.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `forkd quickstart`, `fork`, `snapshot`, `doctor` |
| REST | `/v1/sandboxes`, live BRANCH `mode: "live"` |
| Python SDK | `pip install forkd` |
| TypeScript SDK | `npm install @deeplethe/sandstorm` |
| MCP | `pip install forkd-mcp` |
| License | Apache-2.0 |

---

## Verification

Last verified **2026-10-20**.

Sources:
- https://api.github.com/repos/deeplethe/sandstorm

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
