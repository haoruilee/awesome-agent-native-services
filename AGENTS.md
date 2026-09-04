# AGENTS.md — For AI Coding Agents

This file provides project context for AI agents (Cursor, Claude Code, Windsurf, etc.) working on the Awesome Agent-Native Services catalog.

---

## What This Repo Is

A curated list of **agent-native** services — infrastructure designed from inception for AI agents as first-class consumers, plus a narrow track for purpose-built surfaces that operate live agent systems. Not agent-adapted (human products with agent layers) or agent-builder (platforms for humans to build agents).

---

## Quick Reference

| Need | Read |
|---|---|
| Find a service for a task | [skill.md](skill.md) — machine-readable catalog |
| Understand criteria & contribute | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Full catalog index | [README.md](README.md) |
| LLM-friendly manifest | [llms.txt](llms.txt) |

---

## Repository Layout

```
README.md              # Index: category tables, service summaries
CONTRIBUTING.md        # Five criteria, workflow, service format
skill.md               # Agent entry point — discover services by task
llms.txt               # llms.txt spec — curated links for LLMs
catalog.json            # Generated, versioned machine-readable catalog
catalog.schema.json     # JSON Schema for catalog consumers and CI
AGENTS.md              # This file
services/
  {category}/          # e.g. communication/, memory-and-state/
    README.md          # Category overview + service table
    {service}.md       # Per-service detail (required sections)
.skills/               # Direct SKILL.md packages (find-agent-service, etc.)
.github/               # Issue templates, PR template
```

---

## Contribution Workflow

1. **New service**: Open issue with [01-new-service.yml](.github/ISSUE_TEMPLATE/01-new-service.yml). Wait for ✅ Go. Then PR with:
   - `services/{category}/{service-name}.md`
   - Row in `services/{category}/README.md`
   - Row in root `README.md`
2. **Update**: Use [02-update-entry.yml](.github/ISSUE_TEMPLATE/02-update-entry.yml). Include source URL.
3. **Fix**: Direct PR for typos, broken links — no issue needed.

---

## Service File Format

Every service file must include (in order):

- Official Website, Official Repo
- How to Use (Agent Onboarding) — quickest entry point
- Agent Skills, MCP
- What It Does, Why It Is Agent-Native
- Primary Primitives, Autonomy Model, Identity and Delegation Model
- Protocol Surface, Human-in-the-Loop Support
- Why Generic Alternatives Do Not Qualify, Use Cases

See CONTRIBUTING.md §7 for the exact template.

---

## Classification

| Label | Meaning |
|---|---|
| `agent-native` | Designed for agents or purpose-built to operate live agent-native state — **only these in main list** |
| `agent-adapted` | Human-facing first, agent layer added — Excluded section |
| `agent-builder` | For humans to build agents — Excluded section |

---

## Agent Skills

Install through the Claude Code plugin marketplace or load the source folder directly:

```
git clone --depth=1 https://github.com/haoruilee/awesome-agent-native-services.git
mkdir -p ~/.claude/skills
cp -R awesome-agent-native-services/.skills/find-agent-service ~/.claude/skills/
```

See [SKILLS_HUB.md](SKILLS_HUB.md) for the Claude Code plugin and direct `SKILL.md` paths.

---

## URL Onboarding (⭐)

Services an agent can join with one instruction:

- **Moltbook**: `Read https://www.moltbook.com/skill.md and follow the instructions to register and join`
- **Ensue**: `Read https://raw.githubusercontent.com/mutable-state-inc/ensue-skill/main/skills/ensue-memory/SKILL.md and follow the instructions to connect`
- **autoresearch@home**: `Read https://raw.githubusercontent.com/mutable-state-inc/autoresearch-at-home/master/collab.md and follow the instructions to join`
- **db9**: `Read https://db9.ai/skill.md and follow the instructions`
- **mem9**: `Read https://mem9.ai/skill.md and follow the instructions to register and join`
- **mails.dev**: `Read https://mails.dev/skill.md and follow the instructions`
- **MailboxKit**: `Read https://mailboxkit.com/skill.md and follow the instructions`
- **Shellmates**: `Read https://shellmates.app/skill.md and follow the instructions`
- **SSSNACK**: `Read https://sssnack.com/agent.json and follow the instructions to discover the feed, complete the current registration proof, create an agent identity, and publish or respond to visual work.`

---

## Cursor Cloud specific instructions

This is a **documentation-only** repository — there is no application server, database, or backend service. The "application" is the Jekyll-powered GitHub Pages site rendered from Markdown files.

### Key commands

| Task | Command |
|---|---|
| Build all generated artifacts | `bash scripts/build-github-pages.sh && python3 scripts/build-machine-catalog.py` |
| Validate the machine contract | `python3 scripts/build-machine-catalog.py --check` |
| Start local site preview | `cd docs && bundle exec jekyll serve --host 0.0.0.0 --port 4000` |
| Validate generated artifacts match committed | `bash scripts/build-github-pages.sh && python3 scripts/build-machine-catalog.py && git diff --exit-code` |

### Important notes

- **CI validation workflow** (`validate-generated-docs.yml`) checks the catalog inventory, machine contract, local links, generated artifacts, and Jekyll build. If you modify `README.md`, `skill.md`, `llms.txt`, or `services/**`, regenerate and commit all affected artifacts.
- The build scripts force deterministic ordering. Generated output must reproduce without a diff on Linux CI.
- Jekyll emits a warning about missing GitHub API authentication when run locally (`No GitHub API authentication could be found`). This is harmless and does not affect site rendering.
- `ffmpeg` is used by the build script to generate an Open Graph image (`docs/assets/images/social-preview.png`). It is pre-installed in the Cloud Agent VM. If missing, the script skips image generation gracefully.
- GitHub Actions owns production deployment. Agents prepare source changes and PRs; they do not bypass required checks or directly mutate the deployed artifact.
- If a deployed commit regresses discovery or rendering, revert that commit with `git revert <sha>` on a repair branch, validate locally, merge the repair PR, and confirm the Pages smoke-test job succeeds.
