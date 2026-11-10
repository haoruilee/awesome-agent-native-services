Before an agent runs a shell command, sends money, or deletes a record, something should check whether that action is allowed, and the check should not depend on the model remembering its instructions. Prompt rules can be ignored or argued around. A check that runs in code, before the tool executes, cannot be talked out of its answer. APort describes its guardrails as "Deterministic pre-action authorization for AI agents."

### Deny before the side effect

The dossier lays out the sequence. The agent proposes a tool call. An APort hook, callback, or provider adapter receives it. The proposed action is evaluated against an Open Agent Passport policy, either locally or through the APort API. The decision is logged as allow or deny. Allowed actions run, and denied ones are blocked before anything happens.

Setup starts with `npx @aporthq/aport-agent-guardrails`, which asks which framework you use. The dossier lists setup paths for OpenClaw, Cursor, Claude Code, LangChain, CrewAI, DeerFlow, and n8n. There is a Node package and a Python package. APort is explicitly not an MCP server; it sits in framework hooks and callbacks ahead of tool execution. No standalone Agent Skill is listed in the catalog. The [APort docs](https://aport.io/docs) and the Open Agent Passport spec linked from the dossier are the references for policy syntax.

### Passports and failure modes

The passport is a policy artifact describing allowed actions, limits, assurance, and verification rules. It can live in a file, or a hosted agent ID can reference a passport managed by APort. Each decision produces a record with timestamp, tool, outcome, policy, and context, which gives an operator a trail of what the agent tried and what was refused.

Two design choices deserve attention. First, evaluation fails closed: missing or invalid configuration blocks risky actions by default, which is the right default and also means a broken deployment stops work. Second, local mode supports only a subset of policy, according to the dossier, while API mode uses the hosted evaluator. Find out from the docs which rules need the API, what happens when it is unreachable, and where hosted decision logs are kept. APort is not a human approval queue; people write and review the passport, and runtime decisions are machine-evaluated.

### Editor's take

The [agent runtime and infrastructure collection](/categories/agent-runtime-and-infrastructure/) mostly holds places agents run. [Letta](/services/letta/) and the [Cloudflare Agents SDK](/services/cloudflare-agents-sdk/) host stateful agents. [Cyberdesk](/services/cyberdesk/) provides virtual desktops. [agentOS by Fiserv](/services/fiserv-agentos/) is the closest in intent, a governed operating layer for financial institutions, but it is a platform rather than a policy check you add to an existing framework. APort is the layer you bolt onto whichever of those you already use.

Pick it when your agents run on one of the listed frameworks and you want written, reviewable rules enforced before each tool call. If you are a financial institution that wants a governed platform rather than an add-on, agentOS by Fiserv is the comparison. If you need a person approving specific actions, the dossier is clear that APort is not an approval queue. The [guide to what makes a service agent-native](/guides/what-makes-a-service-agent-native/) covers why pre-action enforcement counts. Only the dossier, the docs, and the repository informed this view; no passport was written and no tool call was blocked while preparing it.
