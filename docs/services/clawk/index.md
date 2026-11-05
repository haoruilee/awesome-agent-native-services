---
title: "Clawk | Agent-Native Services"
service_name: "Clawk"
description: "Give a coding agent its own disposable Linux machine, not yours"
permalink: /services/clawk/
page_kind: service
service_slug: "clawk"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/clawk.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/clawk.md"
tagline: "Give a coding agent its own disposable Linux machine, not yours"
verified_at: "2026-10-13"
website: "https://github.com/clawkwork/clawk"
repository: "https://github.com/clawkwork/clawk"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/clawkwork/clawk" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/clawkwork/clawk/tree/main/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/clawkwork/clawk" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/clawk.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Clawk gives a coding agent a **disposable Linux VM** on the operator's desk instead of the host laptop. `cd` into a repo and run `clawk`: the project is live-mounted, the agent runs as root in the guest with permission-bypass flags, and host files, keychain, and unlisted network destinations stay out of reach.

Isolation is a **hypervisor** (Apple Virtualization.framework / Firecracker), not a process sandbox. Egress is deny-by-default and **DNS-aware** — the userspace stack in the per-sandbox daemon filters TCP/UDP/ICMP; the guest cannot reconfigure it. Idle VMs balloon memory and can suspend; `clawk destroy` drops the VM disk while repo and agent conversation state stay on the host.

**Pre-1.0:** README IMPORTANT callout and Status section both say the project is pre-1.0, moving fast, and will break between releases.

**Distinct from** hosted [Agent Sandbox](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/agent-sandbox.md) (`agentsandbox.co`), [Kubernetes SIG Agent Sandbox](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/kubernetes-agent-sandbox.md), E2B / Runloop / Vercel Sandbox (cloud microVMs), and [CodeRunner](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/coderunner.md) (Apple Containers). Clawk is local-first hypervisor VMs with a DNS-aware egress allow-list.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI (local hypervisor VM)
- **Catalog protocols:** CLI, http
- **MCP:** ⚠️ Not a hosted MCP server. Clawk can *provision* MCP servers in the guest via clawk.mod.
- **Agent Skill:** ⚠️ No official npx skills add / SKILL.md package published.
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI (local hypervisor VM)

```bash
brew install clawkwork/tap/clawk
cd <repo>
clawk                      # boot a sandbox for this dir + attach Claude Code
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/clawk.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `brew install clawkwork/tap/clawk` then `clawk`, `run`, `status --json`, `up`/`down`/`snapshot`/`destroy` |
| Config | Optional `clawk.mod` |
| Docs | https://github.com/clawkwork/clawk/tree/main/docs |
| MCP | Guest-side servers via `clawk.mod`; not a Clawk-hosted MCP package |

---

## Verification

Last verified **2026-10-13**.

Sources:
- https://api.github.com/repos/clawkwork/clawk

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
