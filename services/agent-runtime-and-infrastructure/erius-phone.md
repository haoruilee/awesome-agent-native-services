# ERIUS PHONE

> **"Give your AI agent its own Android phone."**

| | |
|---|---|
| **Website** | https://eriusphone.com |
| **Docs** | https://eriusphone.com/docs.html |
| **GitHub** | https://github.com/Protremix/erius-phone-mcp |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | MIT for the public MCP server (Copyright 2026 ERIUS). The hosted Android phone service is closed-source |
| **Latest-month signal** | Checked 2026-11-27: [homepage](https://eriusphone.com) HTTP 200, title "Virtual Phone Infrastructure for AI Agents"; [ai-agents](https://eriusphone.com/ai-agents/) HTTP 200; [start](https://eriusphone.com/start/) HTTP 200; [llms.txt](https://eriusphone.com/llms.txt), [docs](https://eriusphone.com/docs.html), and [security](https://eriusphone.com/security.html) HTTP 200; API GET [https://api.eriusphone.com/](https://api.eriusphone.com/) 401; MCP GET [https://api.eriusphone.com/mcp](https://api.eriusphone.com/mcp) 405 Allow POST; MCP POST 401 Bearer realm; [repo](https://github.com/Protremix/erius-phone-mcp) MIT, 3 stars, pushed 2026-10-13T07:05:37Z |
| **Verified at** | 2026-11-27 |

---

## Official Website

https://eriusphone.com

Homepage title: *"Virtual Phone Infrastructure for AI Agents"*. H1: *"Give your AI agent its own Android phone."* Meta description: *"ERIUS PHONE is virtual phone infrastructure for AI agents: isolated, persistent cloud Android phones your agents control over one HTTP API and MCP."* `llms.txt` uses the same lead and adds that "phone" here means an Android device, not a phone number or a telephony service.

https://eriusphone.com/ai-agents/ (HTTP 200 on 2026-11-27): *"ERIUS PHONE gives your AI agent a real Android device in the cloud — not a simulator, not a browser sandbox."*

This is ERIUS's own hosted Android cloud phone plus its HTTP API and MCP. It is not [Mobilerun](mobilerun.md), [Phonebox](phonebox.md), [Mobilebox](mobilebox.md), [PhoneUse](phoneuse.md), [Phone Harness](phone-harness.md), [Mobile Next](mobile-next.md), [Auten](auten.md), or [Limrun](limrun.md).

---

## Official Repo

https://github.com/Protremix/erius-phone-mcp

The public repository is the MCP server only. MIT License, Copyright (c) 2026 ERIUS: https://github.com/Protremix/erius-phone-mcp/blob/main/LICENSE. GitHub license detection is MIT. On 2026-11-27 the repo had 3 stars, was not archived, and the last push was 2026-10-13T07:05:37Z. Description: *"MCP server that gives your AI agent a real Android phone (ERIUS PHONE)."* PyPI `erius-phone-mcp` is 0.2.0 and the README marks it pre-1.0, so tool names may still change.

The hosted device service — the Android phones, the API at `https://api.eriusphone.com`, and the dashboard — is closed-source. There is no public repository for that control plane. The start page names the operator as Golan Europe S.L.

The README section "Getting an API key" still describes early-access hand provisioning. That paragraph is older than the live signup: the repo has not been pushed since 2026-10-13, and https://eriusphone.com/start/ now provisions a phone after email confirmation and a Stripe card check.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** REST API + stdio MCP + remote HTTP MCP, after an operator creates the account and key. ⚠️ Not a one-URL join.

An agent cannot register itself from a URL alone. A person opens https://eriusphone.com/start/, confirms an email, and passes a Stripe card check. The page states the trial is 24 hours, EUR 0, nothing is charged, and one trial per person (email and card). The API key arrives in a follow-up email, and the phone is created about a minute after the card check. The 24 hours start when the phone is running. Calls are not included in the trial.

```bash
# Person first: https://eriusphone.com/start/
# email confirmation, then a Stripe card check (EUR 0, 24-hour trial). The key arrives by email.
claude mcp add erius-phone \
  -e ERIUS_PHONE_API_KEY="$ERIUS_PHONE_API_KEY" \
  -e ERIUS_PHONE_DEFAULT_DEVICE="your-device-id" \
  -- uvx erius-phone-mcp
# Remote MCP is POST-only: https://api.eriusphone.com/mcp
# Authorization: Bearer $ERIUS_PHONE_API_KEY
# or header X-API-Key: $ERIUS_PHONE_API_KEY
```

Machine-readable docs that returned HTTP 200 on 2026-11-27: https://eriusphone.com/llms.txt, https://eriusphone.com/docs.html, and https://eriusphone.com/security.html. https://eriusphone.com/skill.md and https://eriusphone.com/SKILL.md returned HTTP 404. GET https://api.eriusphone.com/ without a key returned 401 `missing or wrong X-API-Key`. GET https://api.eriusphone.com/mcp returned 405 with `Allow: POST` and `"use POST for MCP requests"`. POST to that URL without a key returned 401 with `WWW-Authenticate: Bearer realm="erius-phone", error="invalid_token"`.

https://eriusphone.com/docs.html#mcp, reviewed the same day, still documents only the local stdio server (`uvx erius-phone-mcp`, 21 tools). The remote endpoint above is live and is the second MCP path; it is not a substitute description of the stdio package.

---

## Agent Skills

**Status:** ⚠️ Not yet published

No official `SKILL.md` or `npx skills add` package was found. https://eriusphone.com/skill.md and https://eriusphone.com/SKILL.md returned HTTP 404 on 2026-11-27. The MCP repository README does not ship a skill package.

Search community skills: `npx clawhub@latest search erius-phone`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available — local stdio server and a remote POST endpoint

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/Protremix/erius-phone-mcp (MIT; the hosted phone service is closed-source) |
| **Stdio** | `uvx erius-phone-mcp` (Python 3.10+). Env: `ERIUS_PHONE_API_KEY` (required), `ERIUS_PHONE_DEFAULT_DEVICE` (optional), `ERIUS_PHONE_API_URL` (default `https://api.eriusphone.com`) |
| **Remote endpoint** | `POST https://api.eriusphone.com/mcp` |
| **Remote transport** | HTTP POST. GET and OPTIONS return 405 `Allow: POST` |
| **Remote auth** | `Authorization: Bearer <key>` or `X-API-Key`. Unauthenticated POST on 2026-11-27: 401, `WWW-Authenticate: Bearer realm="erius-phone", error="invalid_token"` |
| **Package** | PyPI `erius-phone-mcp` 0.2.0 (pre-1.0) |
| **Tools** | 21, listed in the repo README and on https://eriusphone.com/docs.html#mcp |
| **Compatible Clients** | Claude Code, Claude Desktop, Cursor, and other MCP clients (named on the docs page and in the README) |

Stdio tools cover `whoami`, `list_devices`, `get_device`, `snapshot`, `screenshot`, `foreground`, `wait_for_text`, `tap`, `long_press`, `type_text`, `press_key`, `swipe`, `scroll`, `launch_app`, `open_url`, `send_intent`, `stop_app`, `list_apps`, `install_apk`, `uninstall_app`, and `get_crash_log`. `snapshot` returns an accessibility tree with a `ref` on each element; refs reset on the next snapshot.

---

## What It Does

ERIUS PHONE runs an isolated, persistent cloud Android phone for an agent and exposes that phone over one HTTP API and MCP. The device is Android 13, with the phone profile described as Android 15 / Galaxy S25. The agent reads the screen (`/screenshot`, `/snapshot`, `/observe`) and acts with `/tap`, `/type`, and `/swipe`, plus launch, install, key presses, and crash logs. Apps, sign-ins, and files stay on that phone between sessions. Docs say devices are provisioned for the account — there is no create-device endpoint — and a key can see only that account's devices.

The homepage banner offers one real Android phone for 24 hours at EUR 0. Stripe checks the card and nothing is charged. After the trial, keeping the phone means choosing a plan. `llms.txt` points at https://eriusphone.com/pricing for current euro plans. Voice calls exist as a separate, billed add-on and are excluded from the trial; they are not what this listing is for. The product is the Android device, not a phone number.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage title *"Virtual Phone Infrastructure for AI Agents"* and meta description *"isolated, persistent cloud Android phones your agents control over one HTTP API and MCP."* Source: https://eriusphone.com/ . For-agents page: *"a real Android device in the cloud — not a simulator, not a browser sandbox."* Source: https://eriusphone.com/ai-agents/ |
| **Agent-specific primitive** | A per-snapshot accessibility tree with refs, plus `/tap`, `/type`, and `/swipe` that consume that snapshot. Refs reset on the next snapshot, so the loop is look, then act. A person uses the touchscreen; a test script pins selectors ahead of time. Source: https://eriusphone.com/docs.html |
| **Autonomy-compatible control plane** | After the key and device id exist, the agent installs an APK, launches it, reads the screen, taps, types, swipes, waits for text, and pulls the crash log with no click per action. Limits published by ERIUS: one container and private network per phone, account-scoped keys, per-device CPU and memory limits, 30 requests per second per IP (burst 60), and a per-device action queue. Sources: https://eriusphone.com/docs.html and https://eriusphone.com/security.html |
| **M2M integration surface** | JSON HTTP API (`X-API-Key` or `Authorization: Bearer`), stdio MCP (`uvx erius-phone-mcp`), and remote MCP at `POST https://api.eriusphone.com/mcp`. `llms.txt`: https://eriusphone.com/llms.txt |
| **Identity / delegation** | Each key is 256 bits, shown once, and stored as a SHA-256 hash. It belongs to one account and receives 403 for every other device id, whether or not that id exists. Requests are logged with a key fingerprint, not the key. There is no separate per-agent token beyond that account key and the phone mapped to the account. Source: https://eriusphone.com/security.html |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Hosted Android phone** | One isolated cloud phone per agent, Android 13 (phone profile: Android 15 / Galaxy S25), with its own container, storage, and private network. |
| **Screen snapshot** | `/snapshot` returns the accessibility tree as text with a `[ref]` on actionable elements. `/screenshot` and `/observe` return the screen for the same loop. Refs expire on the next snapshot. |
| **Gesture API** | `/tap`, `/type`, and `/swipe`, plus press, launch, install, and uninstall, on `https://api.eriusphone.com/device/:id/...`. |
| **Account API key** | Issued after https://eriusphone.com/start/. Sent as `X-API-Key` or `Authorization: Bearer`. |
| **Stdio MCP** | `uvx erius-phone-mcp`, 21 tools, MIT package. |
| **Remote MCP** | `POST https://api.eriusphone.com/mcp` with the same key. |

---

## Autonomy Model

1. A person completes https://eriusphone.com/start/: email confirmation, then a Stripe card check (EUR 0, nothing charged). The API key arrives by email and the phone is created for that account. The agent does not collect the card.
2. The agent calls `GET /devices` or MCP `list_devices` / `whoami` and takes the device id.
3. The agent reads `/snapshot`, `/screenshot`, or `/observe`, then `/tap`, `/type`, or `/swipe` against that fresh view. It can install an APK, launch a package, wait for text, and read the crash log.
4. UI actions on one device run in order, so a snapshot's refs stay valid for the next tap on that device. Other devices on the same key run in parallel.
5. On `403` the device is not this key's. On `429` the client backs off (`rate_limited` or `device_busy`). The agent does not guess other accounts' device ids.
6. Third-party app sign-ins stay with a person. The homepage states *"0 Passwords handled by the agent — sign-ins stay human."*
7. When the 24-hour trial ends, a person chooses a plan or the phone is stopped. The start page says an unused trial phone that is not opened in the first 24 hours is removed, and a stopped trial phone is kept for 3 days before deletion.

---

## Identity and Delegation Model

- The credential is an account API key, not a separate agent identity token. The start flow issues that key to the person who verified the email and card; the agent then uses the key.
- Every key belongs to exactly one account. `GET /devices` lists only that account. Any other device id returns the same 403 whether the device exists or not.
- The key is 256 random bits, shown once. The security page says ERIUS stores only a SHA-256 hash and logs a short fingerprint of the key on each request.
- An account can hold more than one key so the operator can switch keys without downtime. The same page, checked by ERIUS on 5 October 2026, says a customer cannot yet create, rotate, or revoke a key themselves: email info@eriusphone.com. Signing out of the dashboard removes the key from that browser and does not revoke it.
- Each phone is its own container and private network. The security page says adb is not open to the internet.
- No customer-facing audit export was described on the security or API pages reviewed on 2026-11-27. The evidence on the wire is the per-request key fingerprint.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | `https://api.eriusphone.com` — `X-API-Key` or `Authorization: Bearer`. Device routes include `/screenshot`, `/snapshot`, `/observe`, `/tap`, `/type`, `/swipe`. Docs: https://eriusphone.com/docs.html |
| MCP (stdio) | `uvx erius-phone-mcp` — https://github.com/Protremix/erius-phone-mcp |
| MCP (remote) | `POST https://api.eriusphone.com/mcp` — POST only; Bearer realm `erius-phone` |
| Account | `GET /devices`, `GET /whoami` (named in the docs examples) |
| Machine docs | https://eriusphone.com/llms.txt |
| Dashboard | https://eriusphone.com/start/ then the dashboard. The agent does not need the dashboard to drive the phone |

---

## Human-in-the-Loop Support

A person has to create the account and pass the Stripe card check before any key exists. That is why onboarding is ⚠️ rather than a one-URL join. After the key and device exist, taps and types do not each wait on a click.

Sign-ins inside Android apps stay with a person (homepage: *"0 Passwords handled by the agent"*). The dashboard can watch the phone live. Choosing a paid plan, and rotating or revoking a key, are person steps. The security page still routes key rotation and revocation through info@eriusphone.com.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **[Mobilerun](mobilerun.md)** | MIT framework plus Mobilerun Cloud for Android and iOS, at `cloud.mobilerun.ai`. ERIUS is a different hosted Android phone and a different API (`api.eriusphone.com`). |
| **[Phonebox](phonebox.md)** | Separate product at phonebox.dev: park-when-done billing, `pbx_` keys, hosted MCP at `phonebox.dev/mcp`. |
| **[Mobilebox](mobilebox.md)** | Separate product at mobilebox.dev. Its public repo is clients, docs, and skills; the fleet is not the ERIUS phone. |
| **[PhoneUse](phoneuse.md)** | Control plane at `mcp.phoneuse.com`. The MIT USB repo is not this cloud phone. |
| **[Phone Harness](phone-harness.md)** | MIT CLI for a phone the operator already has, plus a separate hosted MCP for Phone Harness cloud phones. |
| **[Mobile Next](mobile-next.md)** | Apache-2.0 Mobile MCP and Mobile Next Cloud at `app.mobilenext.ai`. |
| **[Auten](auten.md)** | Local desktop and a beta Android phone on the operator's machine via `@autenai/mcp`, not a hosted ERIUS device. |
| **[Limrun](limrun.md)** | Cloud iOS simulators, Android emulators, and remote Xcode. Not this hosted Android phone. |
| **Device farms and Appium** | Firebase Test Lab, BrowserStack, and Appium suites are built for scripts with selectors chosen in advance. They do not hand the model a fresh ref-per-snapshot tree on a persistent phone that belongs to one account key. |

ERIUS publishes its own comparison at https://eriusphone.com/guides/best-cloud-phones-for-ai-agents/ and `llms.txt` labels that guide as not neutral. This dossier uses the vendor's own product pages and the listings already in this catalog, not that guide's rankings.

---

## Use Cases

- **Android app smoke test** — install an APK, launch it, read the accessibility tree, tap through a flow, and attach the crash log if it fails.
- **Native apps without a public API** — messaging, stores, and other installed apps, driven through the touchscreen rather than a browser.
- **A persistent phone for one agent** — apps and sign-ins remain on that device between sessions, scoped to the account key.
