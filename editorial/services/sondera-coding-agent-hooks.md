A coding agent with shell access will at some point decide to delete a directory, rewrite a config file, or fetch a script from the internet. Asking it nicely in the system prompt not to is a hope, not a control. Something outside the model has to see each action before it happens and say yes or no. Sondera's project calls itself "A reference monitor for AI coding agents," borrowing the security term for a component that mediates every access and cannot be bypassed.

### Intercepting shell, file, and web

The dossier names the pieces: hooks written in Rust, policies written in Cedar, and interception of shell commands, file operations, and web requests. Onboarding is to install the hook binaries and Cedar policy files around coding-agent sessions. In other words, the monitor sits in the agent host's hook points, and each intercepted action is checked against policy before it runs.

That placement matters. A gate the agent calls voluntarily can be skipped by an agent that forgets or is talked out of it. A hook in the host's execution path is closer to what the reference-monitor label promises. Whether it fully lives up to that depends on which hosts expose which hooks, and the dossier does not list supported coding agents. Read the [GitHub repository](https://github.com/sondera-ai/sondera-coding-agent-hooks) for that list before planning a rollout.

The catalog does not record a verified MCP server for these hooks, and it lists no Agent Skill. The integration is binaries and policy files on the machine where the agent runs.

### Policy as Cedar files

Cedar is a policy language with a defined evaluation model, which means rules can be read and reviewed apart from the code that enforces them. That is a real advantage for a security team that wants to diff policy changes. The record does not include example policies, the shape of the request each hook builds, or what a denial looks like to the agent. It also leaves open whether denials and allows are logged, and where. Those are the questions to answer from the repository.

### Editor's take

Among the [oversight and approval services](/categories/oversight-and-approval/), Sondera is the narrow one. [Cordum](/services/cordum/) and [Preloop](/services/preloop/) are control planes for agents in general, run as services. [HumanLayer](/services/humanlayer/) routes decisions to a person. [Tracekit](/services/tracekit/) is about proving after the fact what an agent did. Sondera's record describes deterministic local checks on one class of agent, the coding assistant, with no human in the path unless your policy sends one there.

Pick it if your risk is a coding agent's shell and file system and you want rules a reviewer can read. If you need approvals from a person, or one policy plane across many kinds of agents, start with HumanLayer or Cordum. The [guide to what makes a service agent-native](/guides/what-makes-a-service-agent-native/) is useful background on why enforcement location matters. The judgement on this page was formed from the dossier and the repository alone. Nobody here has installed the hooks on a live agent.
