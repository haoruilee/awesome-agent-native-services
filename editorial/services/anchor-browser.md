Every browser in this product runs on Anchor's fleet, not on the agent's machine. The agent holds API credentials and a task description. Anchor holds the Chromium fork, the proxies, the VPN options, and the login state. That removes a local browser from the agent's list of things that can break, and it puts a vendor in the path of every page the agent opens.

### Tasks, cached actions, and OmniConnect

The vendor's wording is "The Secure Infrastructure for Computer Use Agents." In the dossier that means a cloud fleet of humanized Chromium sessions with authenticated browsing, CAPTCHA and anti-bot positioning, and parallel sessions. The flow it describes starts with a natural-language task. Anchor chooses the proxy, browser, and AI settings, runs the work, and returns results to the caller.

Two named primitives set it apart from a plain session pool. Web Action Cache records a workflow as deterministic actions and replays them, calling a model only when the cached path fails. OmniConnect is described as the auth lifecycle for cloud computer-use agents, covering SSO, MFA, and VPN patterns. The dossier's argument is that replaying known steps costs fewer tokens and flakes less than prompting a model at every click.

Agents reach it through the REST API in the [Anchor docs](https://docs.anchorbrowser.io), the Python and TypeScript SDKs on GitHub, or MCP. The MCP entry is thin: the homepage lists MCP as an integration path for Claude, Cursor, and other hosts, and the dossier sends readers to the docs for configuration. No official Agent Skill pack was found.

### Hosted fleets compared

Within [Browser & Web Execution](/categories/browser-and-web-execution/), Anchor belongs with the hosted sessions. [Browserbase](/services/browserbase/) and [Steel](/services/steel/) also rent browsers to agents, and their dossiers center on the session an agent drives. [Browser Use Cloud](/services/browser-use-cloud/) is closer in intent, with AI browser automation, stealth, and CAPTCHA handling as the headline. Anchor's distinguishing bet is the action cache and the auth product. [Browser MCP](/services/browser-mcp/) sits at the opposite pole, an MCP server rather than a fleet. The [browser infrastructure guide](/guides/browser-infrastructure-for-agents/) lays out the session-versus-engine split.

### Questions for the vendor

API credentials scope tenant access to the fleet, and enterprise controls cover SSO, RBAC, and retention. Ask where stored login state lives, who at Anchor can reach it, and how an agent's delegated session is revoked.

The cache raises its own questions. The dossier does not explain how a cached workflow notices that a site has changed, when the model fallback runs, or how a team audits what was replayed. It also does not name an MCP package or transport, so confirm that path exists for your host before planning around it.

### Editor's take

Teams automating logged-in SaaS work that repeats daily, where most runs should take the same path, are the audience this design is aimed at. If the agent needs a fresh, open-ended session each time, Browserbase or Steel are simpler places to start. What is written here is drawn from the dossier and Anchor's public pages, without running a session on its fleet.
