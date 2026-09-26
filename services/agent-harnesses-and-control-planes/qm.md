# QM

> **"A multiplayer agent harness for work. In Slack and on the web."**

| | |
|---|---|
| **Website** | https://qm.ycombinator.com |
| **Docs** | https://github.com/yc-software/qm/tree/main/docs |
| **GitHub** | https://github.com/yc-software/qm |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/yc-software/qm?style=social)](https://github.com/yc-software/qm) |
| **Classification** | `agent-native` |
| **Category** | [Agent Harnesses & Operator Surfaces](README.md) |
| **License** | MIT, except where noted upstream |
| **Latest-month signal** | [v0.1.12](https://github.com/yc-software/qm/releases/tag/v0.1.12) released 2026-09-19; 15,253 stars; root `LICENSE` is MIT; [qm.ycombinator.com](https://qm.ycombinator.com) returned HTTP 200 on 2026-09-26 ([repo metadata](https://api.github.com/repos/yc-software/qm)) |
| **Verified at** | 2026-09-26 |

---

## Official Website

https://qm.ycombinator.com

---

## Official Repo

https://github.com/yc-software/qm

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `Deployment CLI + generated deployment Skill`

Create an organization-owned deployment repository in the operator's cloud account:

```bash
npm exec --yes --package=@yc-software/qm@latest -- \
  qm init . --org <slug> --target <fly-or-aws>
npm install
```

`qm init` materializes a deployment skill and guides an agent through infrastructure, authentication, connector credentials, optional Slack access, deployment, and live verification. Review the generated deployment plan and security posture before allowing infrastructure mutations.

---

## Agent Skills

**Status:** ✅ Generated for each deployment

The CLI creates a deployment skill for the selected target. A running QM organization also supports scoped, shareable skills and git-imported skill packs; promotion to the entire organization can be admin-gated.

---

## MCP

**Status:** ⚠️ Not the primary surface

QM's headless core, HTTP API, fixed internal tool surface, harness adapters, CLI, and optional Slack/web plugins are its main interfaces. Individual deployments may expose or install MCP tools inside their scope-owned sandboxes.

---

## What It Does

QM gives each person and shared room a persistent agent scope with its own memory, files, keychain view, permissions, crons, web apps, skills, and durable sandbox. Personal and shared scopes can collaborate without collapsing their data or authority boundaries. Pi, OpenCode, Codex, and Claude Code can drive the same headless core, so the organization's durable state and policy are not tied to one model vendor.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Upstream calls QM a **multiplayer agent harness** and describes a shared organizational agent rather than a human collaboration app with an added chatbot — [README](https://github.com/yc-software/qm) |
| **Agent-specific primitive** | Personal/shared agent scopes, scope-owned memory/files/keychains/skills/crons, durable computers, watches, harness substitution, and agent-published internal apps are agent control abstractions |
| **Autonomy-compatible control plane** | Crons and watches run in the background; Auto/Dangerous postures permit unattended tool loops while fixed command denials and scope policy retain hard boundaries |
| **M2M integration surface** | Headless HTTP core, `qm` CLI, deployment Skill, harness adapters, queue/scheduler, and optional Slack service plugin |
| **Identity / delegation** | Each person/room is a distinct scope. The agent acts with that scope's credentials and permissions; narrower scopes can only tighten organization policy, and actions are audited |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Personal/shared scope** | Identity boundary owning memory, files, secrets view, permissions, and apps |
| **Durable sandbox** | Scope-specific computer where tools and logged-in services persist |
| **Harness abstraction** | Pi, OpenCode, Codex, or Claude Code can drive the same core |
| **Scoped skills** | Scope-owned skills shared by grants; organization promotion can require admin action |
| **Crons and watches** | Background work while no person is actively chatting |
| **Security posture** | Strict, Auto, or Dangerous layered under non-bypassable command denials |
| **Deployment directory** | Versionable organization configuration, tools, skills, sandbox image, and infrastructure |

---

## Autonomy Model

```text
Incoming work resolves to a person or shared-room scope
    -> headless core loads that scope's memory, policy, skills, and tools
    -> selected harness runs the agent loop
    -> execute operates inside the scope's durable sandbox
    -> command policy and configured security posture screen actions/data
    -> state, audit records, and scheduled follow-ups persist in Postgres/queue
```

---

## Identity and Delegation Model

- **Scope identity:** Each employee, room, channel, or project owns an isolated scope.
- **Delegated credentials:** The agent acts as the person or room it is working for, using only that scope's keychain view and permissions.
- **Monotonic restriction:** Organization security posture is the ceiling; narrower scopes can tighten but not loosen it.
- **Audit:** QM states that everything the agent does is audited. Session history and durable core state preserve who/where an action came from.
- **Human surfaces:** Slack, web, admin, and portal are optional plugins over the headless core, not required to define the agent's operational identity.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| HTTP API | Headless core for identity, policy, sessions, and scheduling |
| CLI | `qm init`, validation, deployment, and organization operations |
| Agent harnesses | Pi, OpenCode, Codex, Claude Code adapters |
| Deployment Skill | Generated agent-readable installation and verification workflow |
| Optional channels | Slack service plugin and web/admin/portal plugins |

---

## Human-in-the-Loop Support

`Strict` pauses nearly every harness tool call for approval. `Auto` screens provenance-labelled external content while allowing the loop to continue, and `Dangerous` removes screening but still cannot bypass hard command denials. Admin approval can gate organization-wide skill promotion.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Team chat plus bot** | No durable per-person/room computer, scope-owned keychain/skills, harness portability, or monotonic policy model |
| **Generic multi-user SaaS** | Models human accounts, not an organizational agent acting through isolated personal and shared scopes |
| **Single coding-agent CLI** | Lacks organization-wide identity, policy, scheduling, channel continuity, and persistent shared-state boundaries |

---

## Use Cases

- **Company knowledge agent** — search internal systems from the requesting person's allowed scope
- **Shared project room** — maintain files, tasks, memory, and follow-ups visible to a team scope
- **Scheduled inbox operations** — triage and draft on a cron under delegated credentials
- **Internal app delivery** — build and publish scope-authorized web apps from the durable sandbox
- **Vendor-neutral agent operations** — change harness/model without migrating organizational state and policy
