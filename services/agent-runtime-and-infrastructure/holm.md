# Holm

> **"Isolated desktops for AI agents."**

| | |
|---|---|
| **Website** | https://holm.computer |
| **Docs** | https://github.com/holm-inc/holm |
| **GitHub** | https://github.com/holm-inc/holm |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | MIT (Copyright 2026 Oyetoke Toby) |
| **Latest-month signal** | Checked 2026-11-25: [homepage](https://holm.computer) HTTP 200, title "holm — Isolated desktops for AI agents."; [repo](https://github.com/holm-inc/holm) MIT, 10 stars, last push 2026-10-05T07:01:29Z. No hosted cloud: `/login` on the site returned HTTP 404 |
| **Verified at** | 2026-11-25 |

---

## Official Website

https://holm.computer

Title: *"holm — Isolated desktops for AI agents."* Meta description: *"holm gives every agent its own Linux desktop, with a browser, native apps, a shell and files, in a container, a microVM or a cloud sandbox."* H1 on the page: *"Every agent gets its own island."* The site is the product home. There is no hosted fleet to sign into: the path `/login` returned HTTP 404 on 2026-11-25.

---

## Official Repo

https://github.com/holm-inc/holm

MIT: https://github.com/holm-inc/holm/blob/main/LICENSE (Copyright 2026 Oyetoke Toby). About 10 stars, last push 2026-10-05T07:01:29Z. README: *"holm provides isolated desktop boxes that agents can use to complete and drive real tasks."* Install is `holm` / `holmd` plus a runtime. This is self-hosted software, not a vendor cloud.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** local CLI and self-hosted MCP. Not a one-URL join.

Install the binaries and a container or microVM runtime. There is no public vendor MCP URL.

```bash
# Install holm and holmd, then a runtime (Docker, Podman, smolvm, microsandbox, or E2B).
holm mcp --stdio
# or Streamable HTTP on your own holmd: /mcp
```

E2B can be one runtime under Holm. [E2B Desktop](e2b-desktop.md) is a separate listing. Holm is the desktop control plane in front of whichever runtime the operator starts.

---

## Agent Skills

**Status:** ⚠️ Not yet published

No official `SKILL.md` or `npx skills add` package was found in the repo README reviewed on 2026-11-25.

Search community skills: `npx clawhub@latest search holm`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available — local stdio, or Streamable HTTP on a server you run

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/holm-inc/holm |
| **Endpoint** | No public vendor URL. `holm mcp --stdio`, or `holmd` at `/mcp` on your host |
| **Transport** | stdio, or self-hosted Streamable HTTP |
| **Auth** | Whatever you put in front of your own `holmd`. Nothing is hosted at holm.computer |
| **Docs** | https://github.com/holm-inc/holm |
| **Compatible Clients** | MCP clients that can launch a local stdio command or POST to a private HTTP MCP |

---

## What It Does

Holm runs an isolated Linux desktop box for an agent: browser, native apps, shell, files, and screens. The agent drives it from the CLI, a Rust crate, REST, or MCP. The operator can watch in a browser and take the pointer when the agent asks. `hand_over` is optional and is how a person clears a CAPTCHA or a login. Traces and forks are part of the box, so a run can be inspected or branched.

Runtimes named for this project are Docker, Podman, smolvm, microsandbox, and E2B. The last push on the public repo was 2026-10-05. The website still answered HTTP 200 on 2026-11-25. Treat the repo date as the code's last published change, not as a hosted status page.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Site title: *"Isolated desktops for AI agents."* README: *"isolated desktop boxes that agents can use to complete and drive real tasks."* Sources: https://holm.computer and https://github.com/holm-inc/holm |
| **Agent-specific primitive** | A desktop box with screen, input, shell, files, traces, and forks, plus optional `hand_over` when a person must touch the screen. |
| **Autonomy-compatible control plane** | After install, the agent opens and drives a box with no per-action click. `hand_over` is opt-in for CAPTCHA or login, not the default for every click. |
| **M2M integration surface** | CLI (`holm`, `holmd`), Rust crate, REST, and MCP (`holm mcp --stdio` or self-hosted `/mcp`). |
| **Identity / delegation** | The operator who installed Holm. There is no hosted account. A box is isolated from the host and from other boxes. Traces attribute the run to that box. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Box** | Isolated Linux desktop in Docker, Podman, smolvm, microsandbox, or E2B. |
| **Desktop control** | Browser, native apps, pointer, keyboard, shell, files, screenshots. |
| **hand_over** | Optional. A person takes the screen for a CAPTCHA or login, then the agent continues. |
| **Trace / fork** | Built-in record of the run, and a fork of the box. |

---

## Autonomy Model

1. The operator installs `holm` and `holmd` and starts a runtime.
2. The agent connects with `holm mcp --stdio` or to its own `holmd /mcp`.
3. The agent creates a box and drives the desktop.
4. If a site demands a person, the agent calls `hand_over`. Otherwise it finishes and can fork or discard the box.

---

## Identity and Delegation Model

- There is no Holm account service. `/login` on the website was HTTP 404.
- Whoever can run `holmd` on the machine can create boxes. Isolate that daemon the way you isolate any local admin tool.
- Each box is a separate desktop. Traces stay with the box the agent drove.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `holm`, `holmd` |
| Rust | Crate in https://github.com/holm-inc/holm |
| REST | Served by the self-hosted daemon |
| MCP | `holm mcp --stdio`, or Streamable HTTP `/mcp` on `holmd` |
| Docs | https://github.com/holm-inc/holm and https://holm.computer |

---

## Human-in-the-Loop Support

Install is a human step. `hand_over` is the in-loop handoff for a login or CAPTCHA. The README also describes watching the agent in a browser and taking control. Neither is required for an ordinary click or shell command.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **E2B Desktop** (already listed) | E2B's own desktop SDK and API key. Holm can use E2B as one runtime and still owns the box, trace, fork, and `hand_over` API. |
| **A Docker desktop container** | A container with a GUI is not a box lifecycle, MCP tool surface, or trace/fork model. |
| **Holm as a hosted cloud** | The site does not offer login or a public MCP URL. This entry is install-only. |

---

## Use Cases

- **A desktop on the operator's own machines** — Docker or Podman, no Holm account.
- **A microVM or E2B runtime behind the same API** — swap the runtime, keep the agent-facing box tools.
- **A login the agent cannot pass** — `hand_over`, then the agent resumes on the same box.
