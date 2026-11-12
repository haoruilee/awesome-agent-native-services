# E2B Desktop

> **"Build AI agents that see, understand, and control virtual Linux desktops using E2B Desktop sandboxes."**

| | |
|---|---|
| **Website** | https://e2b.dev |
| **Docs** | https://docs.e2b.dev/use-cases/computer-use |
| **GitHub** | https://github.com/e2b-dev/desktop |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Active on 2026-11-11 (~1.5k★) |
| **Verified at** | 2026-11-12 |

---

## Official Website

https://e2b.dev

This listing is the **Desktop Sandbox** computer-use product (`@e2b/desktop` / `e2b-desktop`), not the general E2B code-execution sandbox already listed under [Code Execution](../code-execution/e2b.md). Docs title and lead (https://docs.e2b.dev/use-cases/computer-use): *"Build AI agents that see, understand, and control virtual Linux desktops using E2B Desktop sandboxes."* GitHub description: *"E2B Desktop Sandbox for LLMs. E2B Sandbox with desktop graphical environment that you can connect to any LLM for secure computer use."*

---

## Official Repo

https://github.com/e2b-dev/desktop — Apache-2.0.

A complete working agent built on this SDK is [E2B Surf](https://github.com/e2b-dev/surf), with a live demo at https://surf.e2b.dev.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** SDK (`@e2b/desktop` / `e2b-desktop`).

This is not a one-URL join path. An operator must create an [E2B API key](https://e2b.dev/docs) first (`E2B_API_KEY`), the same account used by the core E2B sandbox product.

From the [repo README](https://github.com/e2b-dev/desktop) and [computer-use docs](https://docs.e2b.dev/use-cases/computer-use):

```bash
pip install e2b-desktop
# or: npm i @e2b/desktop
```

```python
from e2b_desktop import Sandbox

sandbox = Sandbox.create(
    resolution=(1024, 720),
    dpi=96,
    timeout=300,
)
sandbox.stream.start()
print("View desktop at:", sandbox.stream.get_url())

sandbox.left_click(500, 300)
sandbox.write("Hello, world!")
sandbox.press("Enter")
screenshot = sandbox.screenshot()  # bytes

sandbox.kill()
```

The typical agent loop, from the same docs: create a desktop sandbox (Ubuntu 22.04 with XFCE), take a screenshot, send it to a vision / computer-use model, execute the returned click/type/scroll/keypress, and repeat until the model ends the task.

---

## Agent Skills

**Status:** ⚠️ No official `SKILL.md` / `npx skills add` package was found on the Desktop repo or computer-use docs page reviewed.

```bash
npx clawhub@latest search e2b-desktop
```

---

## MCP

**Status:** ⚠️ No Desktop-specific MCP server is documented on https://github.com/e2b-dev/desktop or https://docs.e2b.dev/use-cases/computer-use. (The broader E2B platform has a separate MCP server for sandboxes; that is covered on the [E2B](../code-execution/e2b.md) listing and was not verified here as a Desktop computer-use transport.)

---

## What It Does

E2B Desktop is an open-source virtual computer for computer-use agents. Each sandbox is a Linux desktop (Ubuntu 22.04, XFCE) with mouse, keyboard, screenshot, window, and bash APIs, plus optional VNC streaming so a person can watch (and, depending on stream settings, interact). The SDK is meant to be wired to any LLM that can look at a screenshot and return a desktop action — the docs mention OpenAI Computer Use and Anthropic Claude as examples.

It shares E2B's account and API key with the code-execution sandbox, but the primitive is a graphical desktop, not a code interpreter.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Docs: *"Build AI agents that see, understand, and control virtual Linux desktops."* GitHub: *"virtual computer for computer use"* / *"connect to any LLM for secure computer use."* Sources: https://docs.e2b.dev/use-cases/computer-use, https://github.com/e2b-dev/desktop |
| **Agent-specific primitive** | A sandboxed desktop whose API is screenshot + click/type/scroll/keypress + window control — the computer-use agent loop, not a human VDI product. |
| **Autonomy-compatible control plane** | After `Sandbox.create`, the agent runs the screenshot→model→action loop until it calls `kill()`, with a configurable timeout. No per-click human approval is required. |
| **M2M integration surface** | Official Python and JS/TS SDKs (`e2b-desktop`, `@e2b/desktop`); public Apache-2.0 repo; computer-use guide with a complete agent-loop sample. |
| **Identity / delegation** | E2B API key plus a per-sandbox instance (`Sandbox.create` / `kill`). Stream URLs can be password-protected (README: streaming with password protection; a stream auth key). Pages reviewed for this listing do not describe a separate agent identity token beyond the account key and sandbox. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Desktop sandbox** | Ubuntu 22.04 + XFCE desktop at a chosen resolution and DPI, with a timeout. |
| **Input / screen API** | `left_click`, `right_click`, `double_click`, `move_mouse`, `drag`, `write`, `press`, `scroll`, `screenshot`. |
| **VNC stream** | `sandbox.stream.start()` / `get_url()`; optional auth key and user-interaction disable. |
| **Window and bash** | Launch apps, list windows, run `commands.run`. |

---

## Autonomy Model

1. Operator sets `E2B_API_KEY`.
2. Agent creates a desktop sandbox and optionally starts the VNC stream.
3. Loop: screenshot → LLM action → execute on the desktop, until the model signals done.
4. Agent calls `sandbox.kill()`.

---

## Identity and Delegation Model

- Authentication is the E2B API key on the operator's account.
- Each desktop is a sandbox the agent creates and destroys; isolation is at sandbox boundary.
- Stream URLs may carry an authentication key (README). Treat a live stream URL as access to that desktop for as long as the stream is up.
- No additional delegated-agent credential is documented on the Desktop pages reviewed.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install e2b-desktop` — `from e2b_desktop import Sandbox` |
| JS/TS SDK | `npm i @e2b/desktop` — `import { Sandbox } from '@e2b/desktop'` |
| Docs | https://docs.e2b.dev/use-cases/computer-use |
| Example agent | https://github.com/e2b-dev/surf — demo https://surf.e2b.dev |

---

## Human-in-the-Loop Support

VNC streaming lets a person watch the desktop in a browser. The README documents a mode that disables user interaction on the stream, and a password-protected stream. The agent loop itself does not require a human click.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **E2B code-execution sandbox** (already listed) | A shell and filesystem for generated code, not a graphical computer-use API. This listing is the desktop product. |
| **Generic VPS + VNC** | Human remote-desktop, no agent screenshot/action SDK or sandbox lifecycle. |

---

## Use Cases

- **Computer-use agents** — open a browser on a virtual desktop, click through a GUI, type, and screenshot.
- **Safe evaluation** — run a computer-use model against an isolated XFCE desktop rather than the operator's machine.
- **Surf-style demos** — the open-source Surf app is the reference loop.
