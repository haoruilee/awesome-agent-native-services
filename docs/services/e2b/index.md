---
title: "E2B | Agent-Native Services"
service_name: "E2B"
description: "Cloud for AI agents — secure sandboxes for AI-generated code"
permalink: /services/e2b/
page_kind: service
service_slug: "e2b"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/e2b.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/e2b.md"
tagline: "Cloud for AI agents — secure sandboxes for AI-generated code"
website: "https://e2b.dev"
repository: "https://github.com/e2b-dev/e2b"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://e2b.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://e2b.dev/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/e2b-dev/e2b" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/e2b.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

[Vercel Sandbox](/services/vercel-sandbox/) describes itself through its isolation boundary: microVMs for AI-generated code. E2B describes itself through what the agent experiences. Each session gets a Linux sandbox that remembers variables and imports between code blocks and streams output back while the code runs.

### A REPL per session

The dossier describes secure, isolated Linux cloud sandboxes with a full filesystem and internet connectivity. The stateful execution context is the part that changes agent behavior. Variables, imports, and files persist across multiple code blocks in one session, so an agent can load a dataset once, inspect it, and then try a second analysis without starting over. Python, JavaScript and TypeScript, and shell commands are supported.

Output comes back as it is produced: stdout, stderr, error traces, charts from matplotlib or plotly, and files. Agents can upload inputs and download results. When the task ends, the agent destroys the sandbox. The dossier quotes a cold-start figure; current startup timing belongs in the vendor docs.

### SDKs, MCP in both directions

The quickest documented path is `pip install e2b-code-interpreter`, then `from e2b_code_interpreter import Sandbox` and a `with Sandbox() as sandbox:` block. The TypeScript equivalent is `import { Sandbox } from "@e2b/code-interpreter"`. A REST API manages sandbox lifecycle and execution, and the dossier lists LangChain, AutoGen, and CrewAI integrations. The [E2B docs](https://e2b.dev/docs) cover all of these.

The dossier describes E2B's MCP relationship as unique, because it runs both ways. An official MCP server exposes the code interpreter to MCP clients. Separately, a sandbox can host MCP servers from the Docker MCP Catalog behind a gateway, so third-party tools run inside the isolated VM rather than on the agent's host.

Skills are distributed through the LobeHub marketplace CLI: an `e2b` skill for SDK patterns and an `e2b-desktop` skill for computer-use agents. The dossier says official and community skills both exist, so check which one you are installing.

### Egress, lifetime, and neighbors

Within [Code Execution](/categories/code-execution/), [Agent Sandbox](/services/agent-sandbox/) centers on sessions and an artifact pipeline behind a single API. [CodeRunner](/services/coderunner/) runs locally, which avoids sending code off the machine. [AIO Sandbox](/services/agent-infra-sandbox/) packs browser, shell, files, and an editor into one container. The [sandboxes guide](/guides/sandboxes-and-code-execution/) frames the general choice between fresh environments and persistent ones.

Internet connectivity by default is convenient for installing packages and risky for untrusted code, so check how egress can be restricted. Check how long an idle sandbox lives, what happens to its files on timeout, and whether API keys can be scoped narrower than one integration. The dossier links a GitHub repository but does not describe self-hosting; confirm that before planning around it.

### Editor's take

E2B is the obvious first stop for data-analysis and coding agents that iterate in a REPL, read charts, and benefit from state carrying over between steps. Its MCP hosting is also a reasonable way to quarantine third-party MCP servers. Teams that cannot use a hosted cloud should look at CodeRunner or [OpenSandbox](/services/opensandbox/). No sandbox was opened for this page; the assessment rests on the dossier and E2B's public documentation.

</section>

## What it does

E2B provides secure, isolated Linux cloud sandboxes that AI agents can spin up in ~150ms to execute generated code. Each agent session gets its own sandbox with a full Linux filesystem, internet connectivity, and stateful execution contexts. Agents can run Python, JavaScript, shell commands, and more — with stdout, stderr, charts, and files streamed back in real time.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, REST, SDK, API
- **MCP:** ✅ Available — and uniquely, E2B *runs MCP servers inside sandboxes*
- **Agent Skill:** ✅ Official and community skills available via ClawHub and LobeHub
- **Onboarding type:** `sdk`

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `from e2b_code_interpreter import Sandbox` |
| TypeScript SDK | `import { Sandbox } from "@e2b/code-interpreter"` |
| REST API | Sandbox lifecycle management and code execution |
| LangChain | Native tool integration |
| AutoGen | Compatible with AutoGen's code execution model |
| CrewAI | Compatible with CrewAI tool definitions |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
