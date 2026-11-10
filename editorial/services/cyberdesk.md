An agent driving these desktops calls an SDK or API, and the model behind it has to work from screenshots and emit clicks and keystrokes. The dossier's install line is `pip install cyberdesk`, after which you create a desktop and send computer actions through the SDK or API. MCP is not the primary surface; the dossier calls the product API/SDK-first. No `SKILL.md` package exists yet.

### Desktops as disposable sessions

The tagline is "Open source virtual desktops for AI agents." The dossier describes cloud-hosted virtual desktops an agent controls with mouse, keyboard, screenshot, and app or browser interaction, in isolated sessions with auditable execution. Primitives are desktop create, start, stop, and delete; computer-use actions such as click, type, keypress, and screenshot; isolated sessions for concurrent agents; and execution logs.

The autonomy loop is: create a session, act, read the output, continue, then terminate or archive the session. Screenshots and logs are kept as session artifacts for replay, debugging, or compliance review. API keys identify the workspace and caller, and each session is attributable to a run. Humans can observe, review, or take over, though default operation is agent-driven.

One tension in the entry is worth resolving with the vendor. The tagline says open source, while the protocol section describes a cloud runtime. The dossier does not say whether you can host desktops yourself, which operating systems are offered, or how a human takeover works. Check the [Cyberdesk docs](https://docs.cyberdesk.io) and the [repository](https://github.com/cyberdesk-hq/cyberdesk).

### Where a desktop fits among runtimes

[Agent Runtime & Infrastructure](/categories/agent-runtime-and-infrastructure/) mostly hosts the agent itself. [Modal](/services/modal/) runs code, [Letta](/services/letta/) holds stateful agents, and the [Cloudflare Agents SDK](/services/cloudflare-agents-sdk/) hosts durable agents on Cloudflare. Cyberdesk hosts the environment an agent acts upon, which is a different layer. You might run the agent on Modal and point it at a Cyberdesk session.

Desktop control is the fallback for software without an API. When an API exists, a tool call is cheaper and easier to verify than a click sequence. Pairing desktop sessions with [APort Agent Guardrails](/services/aport-agent-guardrails/) for pre-action checks is one way to constrain what a computer-use agent can do. The [agent-native guide](/guides/what-makes-a-service-agent-native/) explains why lifecycle APIs for desktops count as agent primitives.

### Before handing it a workflow

Confirm what is retained in screenshots, since a session can capture anything on screen, including customer data. Check quota and concurrency behavior under your workspace key. Find out how credentials for applications inside the desktop are supplied and where they are stored.

### Editor's take

Teams automating back-office work in legacy desktop or web applications with no usable API are the intended users, especially where recorded sessions help with review. If the target system has an API, connect to it directly and skip the desktop. If you only need to run code, Modal is simpler. The dossier and Cyberdesk's public docs are the whole basis for this; we have not opened a session.
