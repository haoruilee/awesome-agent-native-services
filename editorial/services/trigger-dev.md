Tasks for this platform are TypeScript files in the team's own repository, but the runs execute on a service the vendor describes as "Build and deploy fully-managed AI agents and workflows." The vendor holds the checkpoints, the schedule, and the run history. For an agent that runs for hours, that operator owns the state that lets a failed step resume instead of starting from the top, and the dossier does not describe a path that moves it in-house.

### Tasks, steps, and approval gates

The dossier describes a durable execution runtime for agent tasks without timeouts. A task is written in TypeScript with Zod schemas for type safety. Its work is split into steps, and each completed step is checkpointed, so an infrastructure failure resumes from the last checkpoint. Tasks start through the REST API or on a cron schedule, and progress streams to a frontend over server-sent events while the run continues.

Human approval is a first-class step. The dossier names a waitForApproval primitive that suspends the task durably, routes the request to operators over configurable channels such as email or Slack, and resumes when someone approves. It also says approval records capture who approved, when, and what context they saw, which is the audit detail regulated workflows ask for.

The quickest documented path is the official skills bundle, `npx skills add triggerdotdev/skills`, with individual skills for setup, tasks, agents, realtime streaming, and configuration; `npx skills add triggerdotdev/skills --skill trigger-agents` installs one. There is no dedicated MCP server. The dossier notes that the TypeScript SDK works inside agent frameworks that use MCP for their own tools, but Trigger.dev itself is reached by SDK and REST. The [Trigger.dev docs](https://trigger.dev/docs) cover both.

### A task framework next to middleware

[Restate](/services/restate/), a neighbor in [Durable Execution & Scheduling](/categories/durable-execution-and-scheduling/), explicitly contrasts itself with Trigger.dev: Restate wraps an existing agent as middleware, while Trigger.dev asks you to write the work as its tasks. [Inngest](/services/inngest/) sits on the same side as Trigger.dev, durable execution for agents in production. [pi-dispatch](/services/pi-dispatch/) runs a single coding agent in a container you control, a narrower and self-operated option. The guide on [what makes a service agent-native](/guides/what-makes-a-service-agent-native/) explains why a durable approval step counts as an agent primitive.

### Read the docs on these

Per-run task IDs give attribution in logs and traces, and cron-triggered runs are traced separately from manual ones. The dossier does not say how REST API keys are scoped or how environments are separated, so check both before an agent can trigger tasks on its own.

The claim that tasks run without timeouts deserves a careful read against the current plan terms. The cron example in the dossier uses a decorator form; confirm the current syntax in the docs before copying it. Also check whether a self-hosted deployment exists today, since the dossier is silent on it, and how a code deploy affects tasks still suspended at an approval gate.

### Editor's take

TypeScript teams starting new long-running agents, especially ones with human sign-off in the middle, will find the most here already built. Teams with an agent already written in another framework may lose less time with Restate's middleware approach. This is an editorial reading of the catalog entry and Trigger.dev's documentation; no task has been deployed to it for this page.
