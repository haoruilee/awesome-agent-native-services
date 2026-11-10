A TypeScript agent that calls a model, then three tools, then the model again, produces a nested sequence of events. When it misbehaves, a developer wants that nesting on screen: which step spawned which, and where the run turned. The agent-inspect project, tagged "Local execution trees for TypeScript AI agents," aims at exactly that view and little else.

### A tree in the terminal

The dossier describes three parts: TypeScript instrumentation, execution trees rendered in the terminal, and run metadata. Onboarding is to add the package to a TypeScript agent project and emit execution trees. That makes it an in-process tool. It is imported into the agent's own code, unlike a wrapper that watches a process from outside, and its output lands where the developer is already looking.

The record is thin on specifics. It does not show the import, name the instrumentation calls, or say whether trees can be written to a file or shipped elsewhere. MCP is marked as not the primary verified surface, and no Agent Skill is listed. The library is the documented path. The [GitHub repository](https://github.com/rajudandigam/agent-inspect) is the only vendor source the catalog cites, so check it for supported agent frameworks, how much code change instrumentation needs, and what run metadata is captured.

### Local first, platform later

Most of the [observability and tracing collection](/categories/observability-and-tracing/) assumes a server somewhere. [Langfuse](/services/langfuse/), [LangWatch](/services/langwatch/), and [Braintrust](/services/braintrust/) store traces, attach evaluations, and give a team a shared place to look. agent-inspect asks for none of that. The nearest neighbor is [Agent Trace](/services/agent-trace/), which also stays on one machine but wraps a run with a CLI and talks about OpenTelemetry-style traces and cost visibility instead of a code-level tree.

The practical split is language and depth. A wrapper works on any agent you can launch from a shell but sees what crosses the process boundary. An in-process library sees the structure the code itself creates, and only works where it can be imported, here TypeScript. Neither replaces a platform once several people need the same history. The [guide to what makes a service agent-native](/guides/what-makes-a-service-agent-native/) treats machine-readable output as a requirement. A terminal tree is readable by a person first, so check whether the run metadata is also available in a form a second agent could parse.

### Editor's take

For a single developer building a TypeScript agent who wants to see the shape of each run without signing up for anything, agent-inspect is a reasonable first tool. Python teams, or anyone who needs traces kept and searched across many runs, should look at Langfuse or LangWatch. If you cannot change the agent's code, Agent Trace's wrapper approach is the alternative. What is written here comes from the dossier and the public repository; no one on the index has instrumented an agent with this library.
