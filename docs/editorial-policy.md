---
layout: default
title: "Editorial policy"
description: "How The Agent-Native Index chooses, updates, and corrects listings, and what the guides will not claim."
permalink: /editorial-policy/
page_kind: document
ads: false
---

This page is the methodology behind [The Agent-Native Index](/). The rules themselves live in the repository, in [CONTRIBUTING.md](https://github.com/haoruilee/awesome-agent-native-services/blob/main/CONTRIBUTING.md). What follows is how those rules are applied, how a mistake gets fixed, and what the essays on this site are allowed to say. If this page and the contribution guide ever disagree, the contribution guide is the admission contract. Open an issue and this page should be corrected to match.

## What the catalog is selecting for

The catalog lists services designed for AI agents as the caller, plus a narrow set of surfaces built to operate a live agent. It does not list every product that mentions agents in a headline.

The standard track requires all five of the following. Dropping one fails the service, even if the others are strong.

**Agent-first positioning.** The vendor's own website or documentation must say that agents are the primary consumer. A line in a changelog, or a platform that "now supports agents" alongside its original human product, does not pass. The contribution guide uses "Email for AI agents" and "A web browser for AI agents & applications" as the kind of positioning that passes, and "now with AI agent support" as the kind that does not.

**An agent-specific primitive.** The interface has to expose something a human product would not need in the same form. Examples the guide already gives: an inbox that is the agent's rather than a user's, an approval result injected back into the agent's context, a Know Your Agent token, a remote browser session whose lifecycle the agent controls, a checkpoint between model calls. A normal REST API that an agent can call is not such a primitive.

**An autonomy-compatible control plane.** The agent must be able to complete the task this service exists for without a person confirming each action. Limits still belong here. A budget, a policy, an isolated session, or an approval gate can be the control. The test is whether the happy path is a loop, not whether the service is reckless.

**A machine-to-machine interface.** For the standard track the primary surface is an SDK, HTTP API, MCP server, webhook, or structured CLI. A dashboard can exist for the operator. The agent should not have to drive that dashboard to do the job.

**Identity and delegation.** If the service sends mail, pays, calls tools, or otherwise acts outward, it has to tell the agent's identity from the user's, represent what was delegated, and leave an audit trail that names the agent. A read-only operator surface does not have to mint authority. It does have to attribute what it shows to a real session, and it has to say that watching is not the same as allowing.

## The operator-surface exception

Some listings are not APIs an agent calls. They are surfaces a person uses to run an agent that already exists. They can qualify only when every part of the exception holds: the surface is for operating agents and not general applications, it reads agent-specific state continuously, it attributes that state to a session or rollout, it is a dedicated operational surface such as a CLI, wrapper, daemon, hook, or status line, and it is honest about capabilities it does not have. Missing autonomy, missing enforcement, or a missing MCP server must be written down, not implied.

The contribution guide is explicit that this exception does not admit generic terminal themes, IDE skins, process monitors, or a human product with an agent tab added later. Harness and control-plane projects, which own loop state such as objectives and checkpoints, are a related but separate idea. They are grouped in the same collection because both sit around a live agent. The category notes on that collection keep the two tracks apart.

## Evidence, not enthusiasm

A proposal has to show the five tests, or every clause of the operator-surface track, with a quote and a source URL. The tagline at the top of a dossier is taken from the vendor's public page and marked as a quotation. Interface tables are filled from the vendor's docs or repository, not from a demo that cannot be linked.

Bonus signals do not replace a missing test. The contribution guide treats URL onboarding as the strongest bonus: an agent joins by reading one machine-readable document and following it. MCP, published Agent Skills, per-agent state, and replay or approval artifacts are recorded when they exist. A service can pass with none of them. A service cannot pass on MCP alone if the underlying product is a human application with a server bolted on.

Classification uses three labels. `agent-native` is the main list. `agent-adapted` is a human product with an agent layer added later. `agent-builder` is a product for people to construct agents. Only `agent-native` is in the main list. The other two, when they are worth pointing at so people stop proposing them, go in the excluded section of the repository README.

## No paid placement

The repository does not describe a sponsorship, a featured slot, or a fee to be listed, moved, or removed. Listings are not sold. There is no way to pay for a kinder summary in a guide.

Contributors do have to disclose a financial interest. The contribution guide says that if you work for, invest in, or otherwise benefit from a service you propose, you say so in the issue and the pull request. Undisclosed interest is grounds for rejection. That rule is about honesty of the proposer. It is not a ban on maintainers later listing a service that happens to have a commercial vendor. Most of the catalog is commercial. The test is the admission track, applied to public documentation.

Guides on this site name vendors because the catalog contains them. A mention is not an endorsement and not a ranking. Where one approach fits a job better than another, the essay says why in terms of the primitive, and it points at the docs. It does not invent a winner from a benchmark this project did not run.

## How listings change

Anyone can report a stale entry. The update issue template asks for the file, the text that is wrong, the replacement, and a source URL. Typical reasons are a newly published MCP server, a new Agent Skill, a changed tagline, a broken link, or a pricing note that no longer matches the vendor. Broken links and obvious factual mistakes can be fixed with a pull request and no prior issue. New services cannot. A new service waits for a maintainer response on the proposal issue. The contribution guide says that response is one of go, no-go, or needs clarification, and that maintainers aim to answer new-service issues within seven days and review pull requests within fourteen. Those are the repository's stated windows, not a service-level agreement with visitors of this website.

If a service shuts down, pivots away from agents, or never qualified, the flag template asks for evidence and a proposed action: remove, reclassify, or leave a deprecation note. Shellmates is the current example of keeping an entry while marking the join path offline, because the old URL returned HTTP 404 and pretending otherwise would be worse. Offline is a fact to record. It is not a quiet deletion.

The rendered site is generated. Collection cards, service introductions, `catalog.json`, and `skill.md` are built from the dossiers. Editing a card by hand does not last. The fix belongs in `services/{category}/{service}.md`, then a regeneration. The essays at the top of each collection, the guides, and the service commentaries in `editorial/services/{slug}.md` are written separately. The generator inserts those files and does not overwrite them. A service commentary is a reading of the dossier and the vendor's public docs. It is not a new source of product facts. When it and the dossier disagree, correct the dossier from the vendor's docs first, then the commentary.

## Corrections

Send a correction as a [GitHub issue](https://github.com/haoruilee/awesome-agent-native-services/issues) or a pull request. Use the update template when a dossier is wrong, and say which sentence on the website is wrong if the problem is a guide or a collection essay. Include the URL you are relying on. This project does not publish an email address for editorial requests. The privacy policy says the same thing about privacy questions.

A correction about a vendor's product should cite that vendor. A correction about whether a service belongs in the catalog should cite the admission test it fails or meets. Disagreement with the test itself is a proposal to change the contribution guide, not a request to make a quiet exception.

## What the guides are

The [guides](/guides/) are original writing for this site. They use the catalog's real categories and the services those categories contain. When a sentence states a product fact, it is taken from the service dossier or from the vendor's public documentation, and the page links one of those. Taglines in quotation marks are the vendor's words, as stored in the dossier.

The guides do not report prices except by pointing at the vendor's current page, and they do not repeat a price that would go stale in the essay. They do not report latency, accuracy, or uptime as a result this project measured. If a dossier repeats a vendor's performance claim, a guide will either omit it or attribute it as the vendor's claim and send the reader to the source. They do not say "we tested." Nobody at this project ran a bake-off for these essays.

Guides will go out of date as products ship. The dossiers are the maintained record. When a guide and a dossier disagree, treat the dossier plus the linked docs as the thing to fix first, then the guide.

## What this policy does not cover

It does not govern the listed products. Their terms, privacy policies, and data retention are theirs. It does not govern GitHub's hosting of the repository or GitHub Pages' delivery of this site. The [privacy policy](/privacy/) covers the pages, the AdSense verification tag, and the fact that advertising is not turned on. Selection rules and advertising configuration are unrelated. A listing decision is not for sale, and an ad slot is not a listing.
