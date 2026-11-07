# Account Access

> **"Connect once. Grant specific permissions. Let your existing AI agent do the routine work."**

| | |
|---|---|
| **Website** | https://github.com/fainir/account-access |
| **Docs** | https://github.com/fainir/account-access/blob/main/docs/setup.md |
| **GitHub** | https://github.com/fainir/account-access |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration](README.md) |
| **Status** | 0.7.4 public preview; reviewed connectors required for real websites |

---

## Official Website

https://github.com/fainir/account-access

---

## Official Repo

https://github.com/fainir/account-access (MIT)

---

## How to Use (Agent Onboarding)

**Interaction pattern:** Agent Skill + structured CLI over a local service.

The owner first installs the service, connects supported accounts and grants named operations. An agent cannot enroll itself by reading a URL.

Follow the official [Mac installation or Linux setup instructions](https://github.com/fainir/account-access#easy-installation). The Mac app installs the skill and CLI for detected Codex and Claude Code installations. Start a fresh agent session, then ask for an approved account read in ordinary language; the agent discovers permitted accounts and operations through the installed launcher. Other local agents can use that CLI or load the skill.

The public README labels the Mac package a Developer ID signed preview with notarization pending. Included public examples are not evidence of private-account coverage. No native Windows support is claimed.

---

## Agent Skills

**Status:** ✅ Available through the official installer.

The [automatic session setup guide](https://github.com/fainir/account-access/blob/main/docs/automatic-sessions.md) documents installation and discovery. There is no required `npx skills add` command.

| Skill | What It Teaches the Agent |
|---|---|
| `account-access` | Discover permitted accounts and operations, request approved reads, preserve resumable tasks, and surface a specific owner challenge without requesting secrets in chat |

---

## MCP

**Status:** ⚠️ Not published; MCP is not a dependency.

The supported agent interface is the portable skill and structured CLI over a private service API, not an MCP server.

---

## What It Does

Account Access is a local authentication and delegated-access service for existing agents. The service manages credentials, sessions, renewal and resumable tasks while an agent requests fixed, owner-approved operations. Owner setup is separate from the agent API.

The [public README](https://github.com/fainir/account-access) identifies this as a preview: real websites require reviewed connectors. It does not establish validated production access to arbitrary websites, banks, Google, Meta or insurance accounts. Local operation under the same OS user is a trusted-agent pilot, not isolation from an agent with unrestricted shell access.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The README describes a local authentication and delegated-access service for Codex, Claude Code and other agents: https://github.com/fainir/account-access |
| **Agent-specific primitive** | Named operations granted to a particular agent principal, with durable tasks and owner challenges: https://github.com/fainir/account-access/blob/main/docs/architecture.md |
| **Autonomy-compatible control plane** | Routine reads and supported login recovery run inside standing grants; genuine owner-presence challenges pause the same task rather than requiring approval for every read. |
| **M2M integration surface** | Portable Agent Skill and structured CLI over an authenticated private Unix-socket API; owner setup is a separate interface. |
| **Identity / delegation** | Per-client identity, grants binding principal/account/operation/configuration, and permission rechecks for operations and result access. The approved proposal discloses that an exportable per-agent audit artifact was not established: https://github.com/haoruilee/awesome-agent-native-services/issues/286 |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Named operation** | A reviewed account read, rather than an arbitrary URL or credential export |
| **Standing grant** | Owner permission scoped to principal, account, operation and configuration fingerprint, with optional expiry |
| **Durable task** | Reviewed read steps with per-principal idempotency keys and saved results |
| **Owner challenge** | A specific unresolved login/device/passkey/admin action that pauses dependent work |

---

## Autonomy Model

1. The owner installs the service, configures a supported connector and grants named operations.
2. The agent discovers the accounts and operations it may use.
3. The service checks the grant and performs the read, renewing a supported session when permitted.
4. The agent receives permitted data or a structured status, not passwords or cookies.
5. A task needing genuine owner presence pauses. After reconnection, the service can continue that task; it does not automatically wake a stopped AI conversation.

---

## Identity and Delegation Model

- Each agent client has a scoped identity resolved from its bearer credential, not an identity selected in an operation payload.
- Operation and result access recheck standing permissions; configuration drift fails closed.
- The agent API cannot grant permissions or export credentials.
- Architecture documentation describes audit metadata excluding provider bodies, secrets and business outputs. An exportable per-agent audit trail was not established by the admission proposal; no stronger audit guarantee is claimed.
- Same-user shell access can bypass broker interfaces; strong credential custody requires a separate OS identity or host.

Source: https://github.com/fainir/account-access/blob/main/docs/architecture.md

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Agent Skill | Portable `SKILL.md` integration, automatically discovered by supported hosts |
| Structured CLI | Account discovery, approved reads, durable task submission and inspection |
| Private service API | Unix-domain socket with bearer authentication; separate from owner setup |
| Provider adapters | Reviewed OAuth or browser reads under fixed operation and destination boundaries |

---

## Human-in-the-Loop Support

Owners connect accounts and choose grants once. Device, passkey, biometric, payment or administrator challenges remain owner actions. The agent presents the specific challenge rather than requesting passwords or login codes in chat. The published architecture implements reads, not arbitrary writes or payment execution.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails This Catalog's Agent-Native Test |
|---|---|
| **A password manager alone** | Secret storage does not provide an agent-principal operation grant, resumable read task or bounded owner challenge. |
| **Unrestricted browser automation alone** | Browser control does not itself impose named delegated operations or separate credentials from agent-visible results. |

---

## Use Cases

- **Approved account reads** - let an existing agent retrieve permitted information through a reviewed connector.
- **Session recovery** - resume supported reads after an expired session or owner reconnection.
- **Multi-account tasks** - preserve completed read steps while one account waits for an owner challenge.
