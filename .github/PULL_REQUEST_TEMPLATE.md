## Type of change

<!-- Check the box that applies. Delete the others. -->

- [ ] 🆕 New service entry
- [ ] ✏️ Update to an existing entry (link fix, new MCP, new Agent Skills, pricing change, etc.)
- [ ] 🚩 Removal or reclassification of an existing entry
- [ ] 📂 New category
- [ ] 🔧 Repository maintenance (README, CONTRIBUTING.md, templates, etc.)

---

## Linked issue

Closes #<!-- issue number -->

> **All new service PRs must have a linked issue that was approved by a maintainer before this PR was opened.**
> Update/fix PRs for obvious factual corrections (broken links, typos) may be opened directly without a prior issue.

---

## Service being added / changed

**Service name:**
**File(s) modified:**

---

## New service checklist

> Complete this section only for PRs that add a new service. Skip for updates/fixes.

### Five hard criteria — evidence

| Criterion | Evidence (quote + source URL) |
|---|---|
| 1. Agent-first positioning | |
| 2. Agent-specific primitive | |
| 3. Autonomy-compatible control plane | |
| 4. Machine-to-machine integration surface | |
| 5. Agent identity / delegation semantics | |

### File structure

- [ ] Created `services/{category}/{service-name}.md`
- [ ] Added a row to `services/{category}/README.md`
- [ ] Added a row to the correct section in the root `README.md`

### Required sections in the service file

- [ ] **Official Website** — canonical homepage URL
- [ ] **Official Repo** — GitHub link(s)
- [ ] **Agent Skills** — status (✅ / ⚠️), install command, skill table or community search note
- [ ] **MCP** — status (✅ / ⚠️), server repo, transport, auth, compatible clients
- [ ] **What It Does** — one paragraph summary
- [ ] **Why It Is Agent-Native** — criterion evidence table
- [ ] **Primary Primitives** — table of agent-specific abstractions
- [ ] **Autonomy Model** — step-by-step execution flow
- [ ] **Identity and Delegation Model** — bullet list
- [ ] **Protocol Surface** — table of interfaces
- [ ] **Human-in-the-Loop Support** — description
- [ ] **Why Generic Alternatives Do Not Qualify** — comparison table
- [ ] **Use Cases** — bullet list

### Classification

- [ ] `agent-native` — I confirm the service was designed from inception for AI agents, not adapted from a human-facing product.

### Bonus signals (check all that apply)

- [ ] **⭐ URL Onboarding** — agent joins with `Read <url> and follow the instructions` (provide URL + what agent gets)
- [ ] Has dedicated agent identity model
- [ ] MCP server is published and linked
- [ ] Agent Skills (`SKILL.md`) are published and install command is documented
- [ ] Per-agent state / memory / session
- [ ] Audit / trajectory / replay / approval artifacts

---

## Update / fix checklist

> Complete this section only for PRs that update an existing entry. Skip for new services.

- [ ] I have included a source URL confirming the change.
- [ ] All links I modified have been verified as live.
- [ ] I have not changed the entry's classification without opening an issue first.

---

## Final checks (all PRs)

- [ ] All links in the changed files are live (I have clicked them).
- [ ] I have no undisclosed financial interest in the service(s) mentioned.
- [ ] Spell-check passed.
- [ ] The PR title follows the format: `[New Service] ServiceName`, `[Update] ServiceName — what changed`, `[Fix] description`, or `[New Category] CategoryName`.
