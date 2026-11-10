[withHuman](/services/withhuman/) calls itself the approval layer for AI agents, and HumanLayer works on the same ground. What the HumanLayer dossier adds is a specific mechanism: a decorator on the risky function, an asynchronous pause, and the human's answer written back into the agent's context window.

### Pausing at a decorated function

The developer marks a high-risk function with `@require_approval()`. When the agent calls it, HumanLayer holds execution and routes an approval request to a person over Slack, email, Discord, or, on some tiers, Teams, SMS, or RCS. The person approves, denies, or modifies. The agent then resumes, either executing the action or reasoning about the refusal.

Denial feedback is the detail worth noticing. When a human says no, their explanation goes into the agent's context, so the next attempt can respond to the actual objection instead of retrying blindly. The dossier says the pause is asynchronous, so one agent can have several approval requests outstanding at once.

Agent webhooks reverse the direction: an incoming human message can launch an agent. Run IDs identify the whole task and Call IDs identify the specific function call, and both appear in requests, responses, and audit logs.

### SDKs first

The quickest documented path is `pip install humanlayer` and decorating functions with `@hl.require_approval()`. A TypeScript SDK offers the equivalent, a REST API manages the approval lifecycle, and webhooks deliver human responses. The [HumanLayer docs](https://humanlayer.dev/docs) cover framework support, which the dossier lists as LangChain, CrewAI, OpenAI, Claude, ControlFlow, Vercel AI SDK, and Mastra.

No standalone MCP server is published, and no official Agent Skill. The dossier says the SDKs work inside MCP-orchestrated agent loops, which means the gate lives in your code around a function, not in the MCP client.

### Open questions for adopters

Within [Oversight & Approval](/categories/oversight-and-approval/), neighbors split between human gates and automated policy. [Sondera Coding Agent Hooks](/services/sondera-coding-agent-hooks/) is a reference monitor for coding agents, and [Cordum](/services/cordum/) is an open agent control plane. [Tracekit](/services/tracekit/) is about proving every action an agent takes. HumanLayer's gate depends on a person answering. The [agent-native guide](/guides/what-makes-a-service-agent-native/) explains why an agent-initiated approval request counts as an agent-specific primitive.

The dossier leaves several things unspecified. It does not say what happens when nobody responds: whether a request times out, escalates, or waits indefinitely. It does not say how the approver is authenticated, which matters for email links that anyone holding the message could click. The function's arguments travel to HumanLayer and then into Slack or email, so consider what data appears in an approval message. Which channels your plan includes is a vendor-docs question.

### Editor's take

HumanLayer is the right shape for teams with Python or TypeScript agents where a handful of functions, such as moving money, sending bulk email, or deleting infrastructure, need a person's sign-off and that person already lives in Slack or email. Where a rule can decide without a human, Sondera or Cordum is a closer match. The verdict here leans on the dossier and HumanLayer's public docs; no approval request was routed through it for this page.
