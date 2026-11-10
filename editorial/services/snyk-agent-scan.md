[ToolHive](/services/toolhive/) is about running MCP servers in a contained way. Snyk Agent Scan works a step earlier. It looks at the harnesses, MCP servers, and skills already present on a machine and reports what in them looks dangerous, before any agent is allowed to call them.

### What the scanner looks for

The dossier describes two stages. First comes inventory: the tool finds local agent components, including harness configurations, MCP servers, and Agent Skills. Then comes inspection: it connects to MCP servers to read the tools, prompts, and resources they expose, and checks that material for prompt injection, tool poisoning, tool shadowing, toxic flows, malware payloads, unsafe credential handling, and hardcoded secrets.

Most of those risks live in text. A tool description can carry instructions aimed at the model, and a second server can register a tool that shadows the first one's name. The dossier's point is that a dependency scanner or a traditional static analyzer does not read tool descriptions or skill files as attack surface, so it would pass a clean package that ships a poisoned prompt.

### A CLI, not a server

The documented interface is a command-line tool. The dossier's quick start is `uvx snyk-agent-scan@latest scan`, and it names `scan` and `inspect` among the commands. You can let it discover local components or pass explicit MCP configuration files. Scans run non-interactively, which is what makes them usable in CI.

The catalog marks MCP as available because the scanner is MCP-aware: it reads MCP configs and talks to MCP servers. The dossier does not describe it as an MCP server that an agent calls as a tool. There is no official Agent Skill package either; skills are something it scans, not something it ships. The [GitHub repository](https://github.com/snyk/agent-scan) is the docs.

### Before and beside runtime controls

The dossier is explicit that the scanner does not replace runtime auth. Its findings feed a decision: block, quarantine, or approve a tool, after which the approved tool can be delegated without per-call review. That makes it complementary to the credential layers in [Tool Access & Integration](/categories/tool-access-and-integration/). [Arcade](/services/arcade/) and [Nango](/services/nango/) govern how an agent authenticates to third-party APIs while it runs. Snyk Agent Scan governs whether a given server or skill gets installed at all. The [MCP servers guide](/guides/getting-started-with-mcp-servers/) shows where that install step happens.

A careful adopter should read the repository for three things the dossier leaves open. Inspection starts or contacts MCP servers, so find out what code executes during a scan. Find out whether analysis runs locally or sends tool descriptions to a Snyk service, and whether an account or token is required. Finally, confirm the output format your CI gate will parse. The dossier also recommends human review of critical findings rather than automatic action on every one.

### Editor's take

Teams that pull third-party MCP servers onto developer laptops, or that publish Agent Skills for others, get the most from a preflight scan like this. It is a gate, not a guard: once a tool is approved, the scanner is out of the loop. For containment while a server runs, ToolHive is the closer fit; for keeping credentials away from the model, Arcade. What is written here reflects the dossier and the public README only, and the scanner has not been pointed at any configuration on this project's behalf.
