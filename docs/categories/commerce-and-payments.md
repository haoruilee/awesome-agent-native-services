---
title: "Commerce & Payments | Agent-Native Services"
collection_label: "Commerce & Payments"
description: "Wallets, payment authorization, identity, and transactions for autonomous buyers and sellers."
hero_image: "/assets/images/editorial-commerce.webp"
hero_image_alt: "A gold coin standing in a slotted cream block, with a charcoal pillar and a red plane behind it."
image: "/assets/images/editorial-commerce.webp"
permalink: /categories/commerce-and-payments/
page_kind: collection
collection_number: "05"
service_count: 22
---

<p class="collection-source"><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/README.md">Collection notes ↗</a></p>

<div class="collection-essay" markdown="1">

Card checkout assumes a person clicked Buy. When an agent pays, the merchant, the network, or the operator still needs a different answer: who authorized this, inside what limit, and which agent the ledger should name. This collection lists wallets, identity, HTTP payment challenges, and the checks that sit in front of a payment. It does not list a processor that added an agent SDK onto a human checkout.

Skyfire, AgentsPay, and Circle Agent Stack are identity and wallet infrastructure. Skyfire's dossier describes a Know Your Agent token, an agent wallet, and spend limits. Coinbase's x402 work, OpenLibx402, Nevermined, MPP, and Tollex are closer to paying inside the HTTP request itself, using a 402 challenge rather than a hosted payment page. AP2 and the Universal Commerce Protocol are about expressing intent and checkout in a form another party can verify. They are not a processor. 402xAgent, AffixIO, INAM, SecondSign Core, Veyra, and send21 sit in front of the payment: probe the endpoint, attest the action, co-sign, cap the spend, or pay without handing the agent a raw key. 402xAgent's dossier is explicit that the check itself does not pay the target.

Chains, assets, and facilitators change. Read the docs linked from the dossier before treating a network as supported. A hosted wallet is a shorter start and puts custody with the vendor. A co-signer or a non-custodial draft keeps the key split and adds a protocol the agent has to speak. A mandate proves intent. It does not, by itself, move the money.

Those layers are mapped in [Payments for autonomous agents](/guides/payments-for-autonomous-agents/).

</div>

<div class="service-grid">
  <article class="service-card service-card--new atlas-sheet--service atlas-visual--01">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://402xagent.com" rel="noopener noreferrer">402xAgent</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/402xagent/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">The check an agent calls before paying any x402 endpoint.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/402xagent/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/402xagent.md">Dossier ↗</a>
      <a href="https://github.com/withgrokbot/x402-spotcheck">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--02">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://www.affix-io.com/" rel="noopener noreferrer">AffixIO</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/affixio/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Know which agent acted. Prove it stayed inside the lines.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/affixio/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/affixio.md">Dossier ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--service atlas-visual--03">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://ap2-protocol.org" rel="noopener noreferrer">Agent Payments Protocol (AP2)</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/ap2/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">An open protocol for the emerging Agent Economy.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/ap2/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/ap2.md">Dossier ↗</a>
      <a href="https://github.com/google-agentic-commerce/AP2">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--04">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://agentspay.dev" rel="noopener noreferrer">AgentsPay</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/agentspay/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Crypto identity and embedded wallets for AI agents.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/agentspay/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/agentspay.md">Dossier ↗</a>
      <a href="https://github.com/AgentPayy/agentpayy-platform">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--05">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://www.circle.com/" rel="noopener noreferrer">Circle Agent Stack</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/circle-agent-stack/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Financial infrastructure for the agentic economy.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/circle-agent-stack/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/circle-agent-stack.md">Dossier ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--06">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://docs.cdp.coinbase.com/x402/welcome" rel="noopener noreferrer">Coinbase Developer Platform (x402)</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/coinbase-x402/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">HTTP-native payments for the machine web — verify, settle, discover.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/coinbase-x402/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/coinbase-x402.md">Dossier ↗</a>
      <a href="https://github.com/coinbase/x402">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--07">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://cymetica.com" rel="noopener noreferrer">CyMetica AI (EventTrader)</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/cymetica-ai/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Agentically engineered financial platform with autonomous AI trading agents.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/cymetica-ai/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/cymetica-ai.md">Dossier ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--08">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://apexfaucet.xyz/g2/jobs/" rel="noopener noreferrer">G2 Jobs (APEX Faucet)</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/g2-jobs/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">An ERC-8183-readable job escrow for AI agents on Base and Arc, in USDC. No owner, no upgrade, 2% fee. If the evaluator stays silent after the work is delivered, the working agent is paid.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/g2-jobs/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/g2-jobs.md">Dossier ↗</a>
      <a href="https://github.com/apexfaucet-hub/g2-agentkit">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--service atlas-visual--09">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://inamprotocol.org" rel="noopener noreferrer">INAM Protocol</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/inam-protocol/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Check an AI agent or x402 seller before you pay it.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/inam-protocol/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/inam-protocol.md">Dossier ↗</a>
      <a href="https://github.com/inamprotocol/inam-protocol">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--service atlas-visual--10">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://dansgit2b.github.io/lumen-tab/" rel="noopener noreferrer">Lumen Tab</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/lumen-tab/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Prepaid USDC tabs for pay-per-call AI agent APIs on Arc.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/lumen-tab/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/lumen-tab.md">Dossier ↗</a>
      <a href="https://github.com/Dansgit2b/lumen-tab">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--service atlas-visual--11">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://mpp.dev" rel="noopener noreferrer">MPP</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/mpp/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">MPP lets agents pay for services on the web, extensible to any payment method.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/mpp/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/mpp.md">Dossier ↗</a>
      <a href="https://github.com/wevm/mppx">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--12">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://nevermined.ai/" rel="noopener noreferrer">Nevermined</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/nevermined/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">The payment layer AI agents actually need.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/nevermined/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/nevermined.md">Dossier ↗</a>
      <a href="https://github.com/nevermined-io/payments">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--13">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://github.com/openlibx402/openlibx402" rel="noopener noreferrer">OpenLibx402</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/openlibx402/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">An open-source library for AI-native x402 integrations.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/openlibx402/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/openlibx402.md">Dossier ↗</a>
      <a href="https://github.com/openlibx402/openlibx402">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--14">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://paymanai.com" rel="noopener noreferrer">Payman AI</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/payman-ai/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Agentic AI that does the banking. Under your control.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/payman-ai/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/payman-ai.md">Dossier ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--service atlas-visual--15">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://priors.trade" rel="noopener noreferrer">Priors</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/priors/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Reputation for AI agents that is earned, public and recomputable.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/priors/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/priors.md">Dossier ↗</a>
      <a href="https://github.com/priors-agents/priors">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--service atlas-visual--16">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://secondsignruntime.com" rel="noopener noreferrer">SecondSign Core</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/secondsign-core/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">An independent transaction co-signer for AI agents that manage other people&#39;s money.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/secondsign-core/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/secondsign-core.md">Dossier ↗</a>
      <a href="https://github.com/Bestpart-Irene/secondsign-core">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--arrival atlas-visual--01">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://send21.io" rel="noopener noreferrer">send21</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/send21/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Payments for AI agents, without giving them your keys</p>
    <div class="service-card__actions">
      <a href="{{ '/services/send21/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/send21.md">Dossier ↗</a>
      <a href="https://github.com/send21io/send21-examples">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--arrival atlas-visual--02">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://shinjukustaition.com" rel="noopener noreferrer">Shinjuku Shield</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/shinjuku-shield/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Privacy-only x402 facilitator for AI agents on Solana.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/shinjuku-shield/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/shinjuku-shield.md">Dossier ↗</a>
      <a href="https://github.com/ShinjukuStaition/shinjuku-shielded">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--arrival atlas-visual--03">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://skyfire.xyz" rel="noopener noreferrer">Skyfire</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/skyfire/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Identity and payments for autonomous AI agents.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/skyfire/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/skyfire.md">Dossier ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--arrival atlas-visual--04">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://tollex.org" rel="noopener noreferrer">Tollex</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/tollex/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">The economic control plane for autonomous software.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/tollex/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/tollex.md">Dossier ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--arrival atlas-visual--05">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://ucp.dev" rel="noopener noreferrer">Universal Commerce Protocol (UCP)</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/ucp/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">The common language for platforms, agents, and businesses.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/ucp/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/ucp.md">Dossier ↗</a>
      <a href="https://github.com/Universal-Commerce-Protocol/ucp">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--arrival atlas-visual--06">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://veyra.money" rel="noopener noreferrer">Veyra</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/veyra/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Let your AI agents make payments — with guardrails you control.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/veyra/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/veyra.md">Dossier ↗</a>
      <a href="https://github.com/zapxlabs/veyra-mcp">Official repo ↗</a>
    </div>
    </div>
  </article>
</div>
<nav class="collection-pagination" aria-label="Adjacent collections">
  <a href="{{ '/categories/oversight-and-approval/' | relative_url }}"><small>Previous collection</small><strong>← Oversight & Approval</strong></a>
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Next collection</small><strong>Agent Runtime & Infrastructure →</strong></a>
</nav>
