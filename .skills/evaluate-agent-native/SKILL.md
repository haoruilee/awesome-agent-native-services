---
name: evaluate-agent-native
description: >
  Evaluate whether a service qualifies as "agent-native" using the five hard criteria
  from the awesome-agent-native-services standard. Also checks for the bonus "URL Onboarding"
  signal — the highest form of agent-nativeness where an agent joins the service by reading
  one URL. Use when asked "is X agent-native?" or "should I add X to the list?"
license: CC0-1.0
compatibility: Works with any agent that can read URLs and analyze text.
metadata:
  repo: https://github.com/haoruilee/awesome-agent-native-services
  catalog-version: "2026-03-15"
allowed-tools: WebSearch Read
---

# Skill: evaluate-agent-native

Use this skill to rigorously evaluate whether a service qualifies as "agent-native" according to the five-criterion standard. Also check for the **URL Onboarding** signal — the strongest indicator that a service was truly built for agents from day one.

## The gold standard: URL Onboarding

Before applying the five criteria, ask the highest-level question:

> **Can an agent join and start using this service by reading a single URL?**

Services that answer YES are exhibiting the strongest possible form of agent-nativeness. They have internalized the agent as first-class user so deeply that the onboarding flow itself is machine-readable:

```
# The full agent onboarding in one instruction:
Read <url> and follow the instructions.
```

Examples:
- **Moltbook**: `Read https://www.moltbook.com/skill.md` — complete registration, heartbeat, posting, DM protocol
- **Ensue / autoresearch@home**: `Read https://raw.githubusercontent.com/mutable-state-inc/autoresearch-at-home/master/collab.md` — complete swarm joining, claiming, publishing protocol

This is qualitatively different from:
- An SDK that a human developer installs (requires human coding time)
- An MCP server that a human adds to a config file (requires human config edit)
- A REST API that requires API key setup (requires human account creation)

URL Onboarding means the **agent itself** handles all of this — reading, understanding, and executing the join sequence autonomously.

Mark URL Onboarding as a **strong bonus signal** and highlight it prominently in the evaluation report.

---

## When to activate

Activate when the user asks:
- "Is [service] agent-native?"
- "Does [service] qualify for the awesome list?"
- "I want to add [service] — does it meet the criteria?"
- "What's the difference between agent-native and agent-adapted?"
- "Why isn't [service] on the list?"
- "Does [service] have URL Onboarding?"

---

## The five hard criteria

A service must pass **all five** to qualify as `agent-native`. Evaluate each one explicitly.

### Criterion 1 — Agent-First Positioning

**Test:** Does the official homepage or documentation explicitly identify AI agents as the **primary consumer**?

**Evidence to look for:**
- Homepage headline naming AI agents
- Documentation framing agents as the core user
- Product name or tagline that only makes sense for agents

**Red flags:**
- "Now with AI agent support" (agents are an add-on)
- "Build apps, workflows, and agents" (agents are one of many outputs)

### Criterion 2 — Agent-Specific Primitives

**Test:** Does the API expose at least one primitive with **no meaningful human-facing equivalent**?

**Questions to ask:**
- What is the core API object? Agent inbox? KYA token? Claim? Heartbeat? Or generic inbox/token/task?
- Would this primitive exist if agents didn't exist?
- Is the output format optimized for LLM consumption or human reading?

**Pass examples:** agent inbox, KYA identity token, approval gate with context-window injection, `claim_experiment()`, heartbeat protocol, `publish_hypothesis()`.

**Fail examples:** a REST API that sends emails (humans use it too), a webhook any server can receive.

### Criterion 3 — Autonomy-Compatible Control Plane

**Test:** Can an agent complete a full task loop **without a human clicking anything**?

**Questions to ask:**
- Can the agent provision its own credentials?
- Can the agent initiate, execute, and complete the action without a human redirect?
- Does the service provide agent-appropriate constraint mechanisms?

### Criterion 4 — Machine-to-Machine Integration Surface

**Test:** Is the **primary interface** an SDK, REST API, MCP server, webhook, or **machine-readable URL**?

**Questions to ask:**
- Can an agent use this service without a human ever opening a browser?
- Is there a URL, SDK, REST API, or MCP server documented as the primary integration path?

**Note:** A service that exposes a machine-readable `skill.md` or protocol URL (URL Onboarding) passes this criterion with exceptional strength.

### Criterion 5 — Agent Identity / Delegation Semantics

**Test:** Does the service distinguish (a) agent's own identity, (b) delegated user permissions, (c) audit trail?

---

## Bonus signals (check all that apply)

| Signal | Weight | Evidence to look for |
|---|---|---|
| **URL Onboarding** ⭐⭐⭐ | **Highest** | Service hosts a machine-readable `skill.md` / protocol doc an agent reads and follows to self-register |
| Dedicated agent identity model | High | Agent gets its own credential/wallet/token |
| MCP server published | Medium | Official MCP server with documented tools |
| Agent Skills (SKILL.md) published | Medium | `npx skills add org/repo` works |
| Per-agent state / memory / session | Medium | State isolated by agent instance |
| Audit / trajectory artifacts | Medium | Machine-readable evidence of agent actions |

**How to test for URL Onboarding:**
1. Look for a `skill.md`, `SKILL.md`, `collab.md`, or similar machine-readable protocol file hosted at the service's domain or GitHub.
2. Ask: could an agent read that URL and complete the full registration/onboarding sequence autonomously?
3. Try the instruction: `Read <url> and follow the instructions` — does it work?

---

## Classification decision tree

```
Does the service pass all 5 criteria?
├── YES → agent-native ✅
│   └── Does it also have URL Onboarding?
│       ├── YES → agent-native ⭐ (URL Onboarding — highest tier)
│       └── NO  → agent-native (standard)
└── NO
    ├── Originally built for humans, agent interfaces added later?
    │   └── YES → agent-adapted ⚠️
    └── Helps humans BUILD agents?
        └── YES → agent-builder ❌
```

---

## Evaluation output format

```
## Evaluation: {Service Name}
**Website:** {url}

### URL Onboarding Check ⭐
**Has URL Onboarding:** YES / NO
**Onboarding instruction (if YES):** Read {url} and follow the instructions to {join/register/participate}
**Notes:** {what the agent gets by reading that URL}

---

### Criterion 1 — Agent-First Positioning
**Result:** PASS / FAIL / PARTIAL
**Evidence:** "{exact quote}" — {source URL}

### Criterion 2 — Agent-Specific Primitives
**Result:** PASS / FAIL / PARTIAL
**Evidence:** {primitive name and description}
**No human equivalent because:** {explanation}

### Criterion 3 — Autonomy-Compatible Control Plane
**Result:** PASS / FAIL / PARTIAL
**Evidence:** {how agents operate without human confirmation}

### Criterion 4 — Machine-to-Machine Integration Surface
**Result:** PASS / FAIL / PARTIAL
**Evidence:** {URL, SDK, API, MCP details}

### Criterion 5 — Agent Identity / Delegation Semantics
**Result:** PASS / FAIL / PARTIAL / N/A
**Evidence:** {identity model details}

---

### Bonus signals
- [ ] URL Onboarding ⭐⭐⭐ — agent joins by reading one URL
- [ ] Dedicated agent identity model
- [ ] MCP server published
- [ ] Agent Skills (SKILL.md) published
- [ ] Per-agent state/memory/session
- [ ] Audit/trajectory/replay artifacts

---

### Overall verdict
**Classification:** agent-native ⭐ (URL Onboarding) / agent-native / agent-adapted / agent-builder
**Recommendation:** Add to main list / Add to Excluded section / Do not add
**Confidence:** High / Medium / Low
**Reasoning:** {one paragraph summary}

### Next steps
{If agent-native with URL Onboarding: highlight this in the issue and service file prominently}
{If agent-native without: link to issue template}
{If agent-adapted: explain what would need to change}
```

---

## Common borderline cases

### "The product added an MCP server — does that make it agent-native?"

No. MCP support is a bonus signal, not a criterion. The core question is whether the service was **designed from inception** for agents. A human email provider that adds an MCP server is still `agent-adapted`.

### "The service has URL Onboarding but other criteria are weak."

URL Onboarding is the strongest bonus signal but cannot substitute for the five hard criteria. Evaluate all five independently; URL Onboarding is an amplifier, not a replacement.

### "The service says 'for AI agents' in marketing."

Check the actual primitives. URL Onboarding is a reliable signal because it requires genuine design effort — you can't fake it with a marketing blog post.
