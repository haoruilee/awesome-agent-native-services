An operations agent eventually reaches a step that should not run on its own say-so: a write to production, a payment, a message to a customer. Somebody has to decide before the call goes out, and somebody later has to see what was decided. The Cordum repository describes itself as "The open agent control plane." The dossier turns that into four pieces: pre-execution policy, approval gates, audit trails, and MCP adapters.

### Gates before the tool call

The onboarding line in the dossier is one sentence. An operator deploys Cordum, then connects LangChain, CrewAI, or MCP agents to its policy gates. From then on the agent works through the CLI, API, or MCP surface the project documents. Each bounded action passes policy, waits at an approval gate, or stops. The outcome returns to the agent loop instead of sitting on a dashboard someone has to watch.

MCP is marked as documented. No dedicated Agent Skill is listed, so an agent cannot read one bootstrap file and wire itself in. A person deploys the service first and points the agent at it. The [GitHub repository](https://github.com/cordum-io/cordum) is the only vendor source the catalog cites. There is no separate docs site in the record.

The [oversight and approval collection](/categories/oversight-and-approval/) holds several services with overlapping words, so the shape matters more than the label. [Preloop](/services/preloop/) also presents itself as an open-source control plane for agents and deserves a side-by-side read. [HumanLayer](/services/humanlayer/) and [withHuman](/services/withhuman/) put the human approval request at the center. [Sondera Coding Agent Hooks](/services/sondera-coding-agent-hooks/) wraps a coding agent's session and intercepts its shell, file, and web actions. Cordum's pitch is the combination: policy, approval, and audit held by one deployed service that several agent frameworks can call.

### What the repository has to answer

Parts of the dossier are generic. Its identity section says a session is represented by caller configuration or a policy subject, and that delegation comes from runtime limits, allowlists, approval thresholds, or deployment credentials. That is a menu, not a specification. Before you depend on Cordum, read the repository for which of those it enforces, how a policy is written, what an approval request looks like to the person who receives it, and where audit records live.

Check who runs the process, too. Self-deployment means your team owns its availability. If the gate is unreachable, does the agent fail closed or carry on? The record does not say. The [guide to what makes a service agent-native](/guides/what-makes-a-service-agent-native/) explains why that question decides whether a control plane is a boundary or a suggestion.

### Editor's take

Cordum fits a team that already runs agents on LangChain, CrewAI, or MCP and wants policy, approvals, and audit in one place it hosts itself. If the real need is a human approval step in front of specific actions, start with HumanLayer or withHuman. If the agent is a coding assistant and the risk is its shell, Sondera is closer to the problem. This opinion comes from reading the catalog entry and the public repository. Nobody on this project has deployed Cordum or routed an agent through its gates.
