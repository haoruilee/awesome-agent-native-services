The host constraint comes first. The dossier lists the surfaces as Apple Containers, a local sandbox CLI, and MCP, so the agent has to run on, or reach, a Mac set up with Apple's container tooling. An MCP-capable client is the natural caller. The catalog also lists HTTP, though the dossier does not describe an HTTP interface. No Agent Skill has been verified.

### Isolation on the developer's own machine

The tagline is "A local sandbox for your AI agents." The How to Use line says to install from GitHub and run agent workloads in isolated Apple containers. Those two sentences carry nearly all the product-specific information in the entry. The remaining sections follow the catalog's template for recent candidates and describe session boundaries, audit trails, and delegation in terms broad enough to fit many sandboxes.

What can be said with confidence: code the agent writes runs in a container on the local machine instead of directly on the host, and an MCP client can request that. The [repository](https://github.com/instavm/coderunner) serves as website, docs, and code, since the catalog has no separate docs URL. The dossier does not say which languages are available, whether files persist between runs, how the container gets network access, or which MCP tools are offered.

### Local against hosted

[Code Execution](/categories/code-execution/) offers three broad choices. Hosted sandboxes such as [E2B](/services/e2b/) and [Vercel Sandbox](/services/vercel-sandbox/) run code on vendor infrastructure behind an API key. Self-run platforms such as [OpenSandbox](/services/opensandbox/) and [Axern](/services/axern/) move that onto your servers. Local options like CodeRunner keep everything on the laptop. [AIO Sandbox](/services/agent-infra-sandbox/) is a single Docker container combining browser, shell, files, MCP, and VS Code Server, which makes it the nearest local alternative outside Apple's tooling.

Local execution means no network hop and no code leaving the machine, which matters for private repositories. The cost is that isolation is only as strong as the local container runtime, and capacity ends at one machine. The [sandboxes guide](/guides/sandboxes-and-code-execution/) compares those properties across the category.

### Read the README for these

Check the macOS version and hardware that Apple Containers requires. Find out what the container can see of the host filesystem and network by default. Confirm whether state is cleared between tasks or carried forward. Look at how actively the project is maintained.

### Editor's take

Mac-based developers who want their coding agent to execute generated code locally, without sending it to a cloud sandbox, are the obvious fit. Linux and Windows users should compare AIO Sandbox. Teams that need many concurrent sandboxes or shared infrastructure belong with E2B, Vercel Sandbox, or a self-run platform. With a dossier this short, the judgement here is mostly inference from the tagline, the install line, and the public repository; the project has not run CodeRunner.
