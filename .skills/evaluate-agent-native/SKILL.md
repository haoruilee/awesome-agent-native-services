---
name: evaluate-agent-native
description: >
  Evaluate whether a service qualifies as "agent-native" using the five hard criteria
  from the awesome-agent-native-services standard. Use this when the user asks "is X
  agent-native?" or "should I add X to the list?" or "does Y meet the criteria?"
license: CC0-1.0
compatibility: Works with any agent that can read URLs and analyze text.
metadata:
  repo: https://github.com/haoruilee/awesome-agent-native-services
  catalog-version: "2026-03"
allowed-tools: WebSearch Read
---

# Skill: evaluate-agent-native

Use this skill to rigorously evaluate whether a service qualifies as "agent-native" according to the five-criterion standard defined in this catalog.

## When to activate

Activate when the user asks:
- "Is [service] agent-native?"
- "Does [service] qualify for the awesome list?"
- "I want to add [service] — does it meet the criteria?"
- "What's the difference between agent-native and agent-adapted?"
- "Why isn't [service] on the list?"

## The five hard criteria

A service must pass **all five** to qualify as `agent-native`. Evaluate each one explicitly.

### Criterion 1 — Agent-First Positioning

**Test:** Does the official homepage or documentation explicitly identify AI agents as the **primary consumer** (not a secondary use case, not a blog post, not a marketing footnote)?

**Evidence to look for:**
- Homepage headline or subheadline naming AI agents
- Documentation introduction framing agents as the core user
- Product name or tagline that only makes sense for agents

**Red flags:**
- "Now with AI agent support" (agents are an add-on)
- "Build apps, workflows, and agents" (agents are one of many outputs)
- Agents mentioned only in a "use cases" blog post

### Criterion 2 — Agent-Specific Primitives

**Test:** Does the API expose at least one primitive that has **no meaningful human-facing equivalent**? If a human developer would use the exact same API without modification for a human-facing product, it fails.

**Questions to ask:**
- What is the core API object? Is it an "agent inbox", a "KYA token", an "approval gate"? Or is it a generic "inbox", "token", "approval"?
- Would this primitive exist if agents didn't exist?
- Is the output format optimized for LLM consumption, or for human reading?

**Pass examples:** agent inbox, KYA identity token, approval gate with context-window injection, remote browser session, durable step checkpoint between LLM calls.

**Fail examples:** a REST API that sends emails (human emails too), a webhook that any server receives, a generic OAuth library.

### Criterion 3 — Autonomy-Compatible Control Plane

**Test:** Can an agent complete a full task loop using this service — including all the actions the service provides — **without a human clicking anything**?

**Questions to ask:**
- Can the agent provision its own credentials?
- Can the agent initiate, execute, and complete the action without a human redirect?
- Does the service provide agent-appropriate constraint mechanisms (spending limits, policy gates, session isolation) instead of per-action human confirmation?

### Criterion 4 — Machine-to-Machine Integration Surface

**Test:** Is the **primary interface** an SDK, REST API, MCP server, or webhook? A human-facing UI may exist as a secondary surface but must not be required for the agent's operational loop.

**Questions to ask:**
- Can an agent use this service entirely without opening a browser?
- Is there an SDK, REST API, or MCP server documented as the primary way to integrate?
- Does the service require a human to configure it through a UI before the agent can use it?

### Criterion 5 — Agent Identity / Delegation Semantics

**Test:** Where the service involves external actions, does it distinguish (a) the agent's own identity, (b) delegated user permissions, and (c) an audit trail attributable to the agent?

**Note:** If the service does not involve external actions (e.g., a pure in-process memory layer), this criterion may be N/A or satisfied trivially.

**Questions to ask:**
- Does the agent get its own credential, wallet, or identity token?
- Is there a delegation model — can the agent act on behalf of a user with scoped permissions?
- Are agent actions logged in a way that distinguishes which agent took which action?

---

## Classification decision tree

```
Does the service pass all 5 criteria?
├── YES → agent-native ✅ (eligible for the main list)
└── NO
    ├── Was it originally built for humans, with agent interfaces added later?
    │   └── YES → agent-adapted ⚠️ (goes in Excluded / Boundary Cases)
    └── Does it help humans BUILD agents (visual builders, orchestrators, no-code)?
        └── YES → agent-builder ❌ (not in this catalog at all)
```

---

## Evaluation output format

Produce a structured evaluation report:

```
## Evaluation: {Service Name}
**Website:** {url}

### Criterion 1 — Agent-First Positioning
**Result:** PASS / FAIL / PARTIAL
**Evidence:** "{exact quote from homepage/docs}" — {source URL}
**Notes:** {any qualifications}

### Criterion 2 — Agent-Specific Primitives
**Result:** PASS / FAIL / PARTIAL
**Evidence:** {description of the primitive(s)}
**Notes:** {would a human use this primitive? explanation}

### Criterion 3 — Autonomy-Compatible Control Plane
**Result:** PASS / FAIL / PARTIAL
**Evidence:** {how agents operate without human confirmation}
**Notes:** {any caveats}

### Criterion 4 — Machine-to-Machine Integration Surface
**Result:** PASS / FAIL / PARTIAL
**Evidence:** {SDK/API/MCP details}
**Notes:** {any caveats}

### Criterion 5 — Agent Identity / Delegation Semantics
**Result:** PASS / FAIL / PARTIAL / N/A
**Evidence:** {identity model details}
**Notes:** {any caveats}

---

### Bonus signals
- [ ] Dedicated agent identity model
- [ ] MCP server published
- [ ] Agent Skills (SKILL.md) published
- [ ] Per-agent state/memory/session
- [ ] Audit/trajectory/replay artifacts

---

### Overall verdict
**Classification:** agent-native / agent-adapted / agent-builder
**Recommendation:** Add to main list / Add to Excluded section / Do not add
**Confidence:** High / Medium / Low
**Reasoning:** {one paragraph summary of the decision}

### Next steps
{If agent-native: link to the new service issue template}
{If agent-adapted: explain what would need to change for it to qualify}
{If agent-builder: explain the distinction clearly}
```

---

## Common borderline cases

### "The product added an MCP server / Agent Skills — does that make it agent-native?"

No. MCP support is a bonus signal, not a criterion. The core question is whether the service was **designed from inception** for agents as first-class entities. A human email provider that adds an MCP server is still `agent-adapted`.

### "The company says it's 'for AI agents' in their marketing."

Check the actual primitives. Many companies add "for AI agents" to existing products. Look at what the API objects are named and what the core abstractions are — not just the marketing copy.

### "The service is brand new and only has a landing page."

Fail criterion 4 (no documented SDK/API) and possibly criterion 1 (no docs proving agent-first positioning). Mark as "not yet ready" rather than excluded.
