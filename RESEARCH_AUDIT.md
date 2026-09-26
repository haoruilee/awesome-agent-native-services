# Research & Freshness Audit — 2026-09-26

This note records the latest catalog-wide research and freshness pass. New
services remain issue-first; this file records the scope, evidence window, and
maintenance work that was actually completed.

## Scope

- Window: catalog changes and live checks from the previous watermark
  (2026-08-13) through 2026-09-26 (UTC). Asia/Shanghai is the same calendar
  date.
- Reconciled inventory: **238** service dossiers across **16** collections.
  The 2026-08-13 pass recorded 172 dossiers. The difference is 66 dossiers
  added after that watermark. Kitaru was moved into Observability on
  2026-08-29; that move is not a new admission.
- Probed **615** canonical URLs (official sites, repositories, onboarding
  URLs, and verification sources) with
  `python3 scripts/check-repository-health.py --external-canonical` on
  2026-09-26. Result: **589 ok, 26 protected, 0 hard failures**.
- Queried the GitHub API for the **206** catalog repository fields that point
  at a `owner/name` repo: existence, rename, archive bit, `pushed_at`, and
  SPDX license. All 206 resolved. Nine other repository fields point at a
  GitHub user or organization page rather than a repository; those were not
  treated as missing repos.
- Fetched the nine URL-onboarding documents listed in `AGENTS.md`, plus
  Shellmates, and re-checked MCPVerse.
- Compared dossier **License** rows with GitHub license metadata where the
  dossier names a single SPDX-style license and the API returned a definite
  SPDX id.
- This pass did **not** re-read every legacy claim, price, or MCP auth
  detail. It did **not** copy this audit date onto service-level
  `verified_at` values that were not individually re-checked.

## Services added since 2026-08-13

66 dossiers, in merge order. None were removed or reclassified in this pass.

- 2026-08-17: Agent QA
- 2026-08-18 (#102): Claude HUD, LoopX, Cloudflare Computer, Google AX,
  AgentGram, Kernel, AgentTeam Email, Atomic Mail, AgentCall, AgentMemory,
  TencentDB Agent Memory, Preloop, Agent Search MCP, Toolport, Patter
- 2026-08-24: SandBase CLI
- 2026-08-25: Bifrost; DeepSeek Harness, Agent Substrate, Stealth Browser MCP,
  Kubernetes Agent Sandbox, AP2, UCP, MemPalace, MemSearch, AgentSight,
  ContextForge, MCP Gateway Registry
- 2026-08-27: Clawk, Dormice, MPP, claude-mem, Engram
- 2026-08-28: XiuRouter
- 2026-08-31: SandBase Harness
- 2026-09-02 (#120): Joinly, Beads, Compartment, Memoir, Memorix, ProjectMem,
  MCPHub, MCPJungle
- 2026-09-03: SSSNACK; CubeSandbox, Forkd, SmolVM, Graphiti, MCP Memory
  Service, MetaMCP
- 2026-09-11: SwarmMemo
- 2026-09-12: OrcaReplay, Open Task Relay, Dasha Compute
- 2026-09-14: GoodMem
- 2026-09-17: AffixIO
- 2026-09-20: YYLO, TERM, Cohesivity, Pizza Bot, txcript, peerd, Cua
- 2026-09-23: Mnemoverse (#155), SendRaven (#158)

Mnemoverse and SendRaven were spot-checked only through the canonical URL
probe (sites and repos returned success; their hosted MCP endpoints answered
401/405, which this checker treats as protected rather than down). Their
dossier claims were not re-litigated.

## Link and repository check

- No canonical URL in the 615-URL set returned a hard failure (HTTP 404/410,
  DNS failure, or connection error) on 2026-09-26.
- Protected responses (not counted as dead) included API routes that reject
  unauthenticated GET/HEAD (401/405), bot challenges (403) on `obot.ai`,
  `skyfire.xyz`, `mempalaceofficial.com`, an OpenAI.com marketing URL, and
  two npm package pages, plus HTTP 429 from `console.notte.cc`. `obot.ai`
  is still the homepage on the live GitHub repo, so the 403 is treated as
  blocking this client, not as proof the site is down.
- GitHub renames confirmed and canonical URLs updated:
  - SmolVM: `CelestoAI/SmolVM` redirects to `CelestoAI/celesto`. Product name
    and docs host are unchanged. License file is still Apache-2.0. Last push
    2026-09-25.
  - Toolport: `tsouth89/toolport` redirects to `btsouth/toolport`. License
    MIT. Last push 2026-09-26.
- One archived repository: `loopedautomation/meet` (Looped Meet). Last push
  2026-08-17. `meet.looped.sh` is still DNS NXDOMAIN. The tree is still
  public and the license file is still FSL-1.1-ALv2. Not removed.
- URL-onboarding documents that returned instructional content: Moltbook,
  Ensue, autoresearch@home, db9 (`db9.ai/skill.md` redirects to a CloudFront
  `skill.md`), mem9, mails.dev, MailboxKit, SSSNACK `agent.json`, and
  SwarmMemo `llms.txt`. Shellmates `skill.md` is still HTTP 404.
- Other live redirects recorded and pointed at the post-redirect URL:
  - LiveKit marketing page `livekit.io/agents` → `livekit.com/agents`.
    `docs.livekit.io` still serves the agents docs.
  - Agent Search MCP `take-a-deep-breath0.com/en/agent-search-mcp` →
    `lennney.com/en/agent-search-mcp`.
  - Vercel Sandbox docs `/docs/vercel-sandbox` → `/docs/sandbox` (including
    the SDK reference).
  - LangWatch `docs.langwatch.ai` → `langwatch.ai/docs/introduction`.
  - Cloudflare product page → `www.cloudflare.com/products/browser-rendering/`
    (title still "Cloudflare Browser Rendering"). Docs index
    `/browser-rendering/` → `/browser-run/`. The old AI guide
    `/browser-rendering/how-to/ai/` now lands on
    `/browser-run/quick-actions/json-endpoint/`, which is a different page.
    The docs nav links Playwright MCP at
    `/browser-run/playwright/playwright-mcp/` (HTTP 200). Citations were
    updated to that page.
  - `agentuity.dev`, including `/agents/creating-agents`, redirects to the
    marketing page `agentcompany.com/agentuity` ("Agentuity — The Agent
    Company"). This pass did not find a replacement for that old docs path.
  - Dasha Compute HTML `www.getdasha.com/compute` redirects to
    `lobby.getdasha.com/compute`. `compute/skill.md`, `/.well-known/agent.json`,
    and `compute/mcp.json` on `www.getdasha.com` still describe Dasha Compute.
    Apex `www.getdasha.com/llms.txt` did **not**: on 2026-09-26 it described
    a Solana token site. The onboarding instruction no longer tells agents
    to read that file.

## License and open-source status

Checked dossier license rows against GitHub's detected SPDX id and, for
mismatches, the raw `LICENSE` text.

Corrected in the dossiers:

- Hindsight (`vectorize-io/hindsight`): root `LICENSE` is MIT, not
  Apache-2.0. Last push 2026-09-25.
- OpenViking (`volcengine/OpenViking`): root `LICENSE` and the README license
  section are AGPL-3.0 for the main project. `crates/ov_cli` and examples are
  Apache-2.0; the Hermes plugin is MIT. The dossier had said Apache 2.0 only.
- Obot (`obot-platform/obot`): root `LICENSE` is MIT (copyright 2026 Obot AI,
  Inc.), not Apache 2.0.
- Serena (`oraios/serena`): GitHub reports `NOASSERTION` because `LICENSE` is
  a component notice, not a single SPDX grant. SolidLSP is MIT. The Serena
  application is GPL-3.0-or-later. Combined distributions such as
  `serena-agent` are GPL-3.0-or-later. The dossier had said MIT only.

Noted, not rewritten into a different license than the project states:

- Daytona (`daytonaio/daytona`): the default branch has no `LICENSE` file
  (GitHub license `NONE`). The README, read 2026-09-26, says the repository
  is **no longer maintained**, that core development moved to a private
  codebase in June 2026, and that the public grant remains the AGPL-3.0 text
  at tag `v0.190.0`. The dossier now says that. Last push 2026-07-24.
- Looped Meet, Agent QA, and Restate still use license texts GitHub will not
  reduce to a single SPDX id (FSL-1.1-ALv2 or BSL). Those rows were left as
  written after the license file or prior dossier text still matched.
- Twelve other rows name a license while GitHub reports `NOASSERTION` or no
  detected license (including Novu, Langfuse, CubeSandbox, TencentDB Agent
  Memory, and the Codex HUD snapshots that already say they have no root
  `LICENSE` file). Those were not changed. CubeSandbox and TencentDB already
  explain the `NOASSERTION` result in the dossier.
- Ensue's summary says MIT, but the catalog repository field is
  `mutable-state-inc/ensue-mcp-stdio`, which has no `LICENSE` file (last push
  2025-12-11). `ensue-skill` also has no GitHub-detected license. The MIT
  claim was **not** re-proven from a license file in this pass.

## Status changes and review candidates

No service was removed and no classification was changed.

Maintainer review, not an automatic removal:

- **Daytona** — public repo explicitly unmaintained; core development moved
  private; default branch has no license file.
- **Looped Meet** — repository archived and the hosted site does not resolve.
  Self-hosted source is still public.
- **Shellmates** — still HTTP 404 on `shellmates.app` and `/skill.md`
  (2026-09-26). Already recorded as offline.
- **MCPVerse** — `mcpverse.org` still does not resolve; `mcpverse.com`
  returned HTTP 403; `mcpverse.ai` timed out during TLS. Already recorded as
  offline. No replacement domain was verified.
- **Obot** — license corrected to MIT, but the live README no longer leads
  with "Complete MCP Platform". It now describes an open-source platform to
  manage, secure, and govern an organization's AI ecosystem (clients, MCP
  servers, skills, credentials, hosted workloads). The tagline and admission
  table were left unchanged for a maintainer review. `obot.ai` returned 403
  to this client.

Quiet public repos (no push in the 180 days before 2026-09-26) whose catalog
websites still returned HTTP 200 with a product title, or whose website is
the GitHub repo itself. These are maintenance signals, not removal
candidates: Toolhouse, Browser MCP, Cyberdesk, Scrapybara, Hyperbrowser,
OpenLibx402, Inferable, Ensue (`ensue-mcp-stdio`), mcp-agent, AgentsPay,
Bright Data AI SDK, Polos, ATXP, AgentAnycast.

Nine `repository` fields are GitHub user or org pages because the first
GitHub URL in Official Repo is not `owner/name`: AgentMail, ATXP Email, Jina
DeepSearch, Riza, Galileo, Meeting BaaS, Recall.ai, OpenRouter, Kinthai.
Not changed.

## Per-entry verification that this date does not refresh

The first 2026-09-26 pass updated `verified_at` only for SmolVM, Toolport,
Looped Meet, and Agent Search MCP. A same-day follow-up then re-checked the
18 dossiers that were still dated 2026-08-13. Each of those 18 was
re-verified against its live repository and canonical URL, and `verified_at`
is now **2026-09-26** with a rewritten latest-month signal. `skill.md`
`version` stays 2026-09-26, so none of these dates is newer than
`catalog_version`.

Follow-up evidence, all checked 2026-09-26:

- All 18 GitHub repositories resolved and none is archived.
- Codex HUD (`fwyc0573/codex-hud`): still no root `LICENSE` file; `package.json`
  still says MIT. Latest release is v1.2 (2026-09-01), 79 stars, last push
  2026-09-06.
- oh-my-codex: a root `LICENSE` file is now present and is MIT. The previous
  "no root LICENSE file" caveat was removed. v0.21.6, 33,371 stars.
  `oh-my-codex.dev` returned HTTP 200.
- LongHorizon-Harness, QM, Agent Chamber, Axern, SecondSign Core, pi-dispatch,
  SageRoute, Memmy, numbat, and Qwen Audio Agent: license SPDX matches the
  dossier (MIT or Apache-2.0). Releases and star counts moved; signals were
  updated. Axern's public star count is 66, down from the 232 recorded on
  2026-08-13. Sallyport is 192, down from 246, and its last push is still
  2026-07-19. SageRoute's last push is still 2026-07-29 and it still has no
  release. Their sites or repository pages responded.
- Moli: `LICENSE-APACHE` and `LICENSE-MIT` are both present. Latest release
  v1.1.10, 2,403 stars. `browser.lexmount.com` is up; its title is "Lexmount
  Browser" while the repository H1 is still Moli.
- OpenChatCut: root `LICENSE` is AGPL-3.0. v0.2.14, 2,000 stars.
  `openchatcut.com` returned HTTP 200.
- Caspian: root `LICENSE` is still AGPL-3.0 and the README license section
  still says Apache-2.0. `api.trycaspianai.com/SKILL.md` returned the channel
  SDK guide. The homepage title is now "The Constructor"; the meta
  description still names Caspian.
- contextX: still no `LICENSE` file and still no GitHub release. 175 stars,
  last push 2026-09-09. `https://mcp.twitter.monster/mcp` responded HTTP 406
  until the client accepted both `application/json` and `text/event-stream`,
  which is a live MCP listener rather than a dead host.
- OpenAI Symphony: repository checks passed (Apache-2.0, v0.0.3 on 2026-09-15,
  27,409 stars). The marketing page
  `https://openai.com/index/open-source-codex-orchestration-symphony/`
  returned HTTP 403 to this client, the same protected response as the
  earlier canonical-link probe. The dossier date was bumped from the
  repository evidence, and the 403 is recorded on the website section. The
  page body was not re-read.

No dossier in this cohort was left at 2026-08-13. Daytona and Looped Meet
were not removed. One other record is dated 2026-08-18 and 15 are dated
2026-08-19. Those stay inside a 45-day window a few days longer than
2026-09-28. 159 dossiers have no `verified_at`. The freshness checker has no
as-of date flag; a 2026-09-28 result was simulated by running the same age
rule with the clock fixed on that date.

## Applied catalog updates

Factual corrections only. No admissions and no removals.

- License rows: Hindsight, OpenViking, Obot, Serena, Daytona.
- Canonical repo URLs: SmolVM, Toolport.
- Canonical site or docs URLs: LiveKit Agents, Agent Search MCP, Vercel
  Sandbox, LangWatch, Cloudflare Browser Rendering, Agentuity, Dasha Compute.
- Dasha onboarding no longer points at the apex `llms.txt`.
- Looped Meet, Shellmates, and MCPVerse notes record the 2026-09-26 re-check.
- Catalog snapshot date in `skill.md` and `.skills/*/SKILL.md` is 2026-09-26.
- Generated catalog and docs artifacts were regenerated from those inputs.

## Evidence and acceptance

- Primary evidence: GitHub repository metadata and `LICENSE` bodies, HTTP
  responses (status and final URL) from the repository link checker and
  follow-up fetches, and page titles where a redirect changed the canonical
  URL. Checked 2026-09-26.
- Anything not fetched is called out above rather than treated as confirmed.
- Generated documentation must reproduce without diff; the public machine
  files must pass schema/parser checks.
- Scheduled freshness automation treats this audit date as the catalog-wide
  review watermark. It does not imply that every legacy claim was
  independently reverified on this date.

## Freshness checklist for future passes

1. Re-run the generator and contract validator after any catalog change.
2. Re-check volatile onboarding commands, hosted MCP endpoints, releases, license
   boundaries, and authentication requirements against official sources.
3. Keep per-entry verification evidence explicit; do not convert this broad audit
   date into a fabricated service-level `verified_at` value.
4. Open an issue before admitting a new service or category unless the change is
   an obvious factual or broken-link correction.
5. Run a broad research pass before the freshness watermark exceeds 45 days.
