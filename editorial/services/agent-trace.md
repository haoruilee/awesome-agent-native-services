After an agent run goes wrong, the first question is plain: which tools did it call, in what order, and what did the run cost? Answering that should not require rebuilding the agent around a tracing SDK. Agent Trace, whose repository uses the tagline "Observability for AI agents," approaches it from the outside. The dossier's onboarding line is to install `agent-strace` from PyPI or GitHub and wrap agent runs with it.

### Wrapping a run from the outside

The package name echoes the Unix strace tool, and the dossier's description fits the comparison: a CLI that sits around a run and records OpenTelemetry-style traces, with visibility into tool calls and cost. The appeal is low commitment. You do not choose a vendor, create a project, or thread a client through every function. You put a command in front of the agent and read what comes out.

The dossier says less than you would want about that output. It does not describe the trace format beyond calling it OpenTelemetry-style, where traces are written, whether they can be exported to a collector, or how cost is calculated. MCP is marked as not the primary verified surface, and there is no Agent Skill in the catalog. The CLI is the documented path. Read the [GitHub repository](https://github.com/Siddhant-K-code/agent-trace) for which agent runtimes it can wrap and what it actually captures before you depend on it for a cost report.

### Choosing a trace store

The [observability and tracing collection](/categories/observability-and-tracing/) runs from single-binary tools to full platforms. [agent-inspect](/services/agent-inspect/) is the closest neighbor in spirit: local, aimed at one developer, but it instruments TypeScript agents from inside and prints execution trees in the terminal. [Langfuse](/services/langfuse/) and [OpenLIT](/services/openlit/) are where traces go when a team needs them stored, searched, and shared, with Langfuse adding evaluation and OpenLIT built around OpenTelemetry. [AgentEvals](/services/agentevals/) scores runs from OpenTelemetry traces after the fact.

That suggests a useful test. If Agent Trace's output is close enough to OpenTelemetry to feed one of those platforms, it can serve as a lightweight capture step in front of them. If it is a private format, it is a local debugging tool and nothing more, which is still useful but a different decision. The [guide to what makes a service agent-native](/guides/what-makes-a-service-agent-native/) frames why machine-readable output matters here: another agent, or a later step of the same one, should be able to read the trace without a person transcribing it.

### Editor's take

Agent Trace is worth trying for a developer who wants a quick account of tool calls and spend on a single machine without adopting a platform. A team that needs retention, sharing, or evaluation across many runs should start with Langfuse or OpenLIT and treat a wrapper as optional. If the agent is written in TypeScript and you can edit it, agent-inspect may tell you more. The repository and the dossier are the whole basis for this view; the index has not wrapped a run with the CLI or inspected its output.
