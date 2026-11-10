Telemetry here enters through an SDK installed in the agent's own process, with API ingestion endpoints behind it. If you cannot add a dependency to the runtime, or your agent is a hosted product you do not control, the documented path does not apply. The catalog marks MCP as optional, and the dossier says it is not the primary surface. No Agent Skill was found.

### Trajectories, datasets, regressions

The vendor calls LangWatch an "Open-source LLM Ops platform for tracing, evals, and guardrails." The dossier is narrower. It lists three primitives: traces and spans for agent runs, evaluation datasets, and regression monitoring. Its agent-native argument is that it captures trajectory-level signals from loops and tool calls rather than single-turn chat logs.

The autonomy model is simple: the agent runs on its own and telemetry is recorded asynchronously. Attribution comes from run IDs and environment keys. Review dashboards and evaluation workflows are described as optional overlays for humans.

Guardrails appear in the tagline but not among the dossier's primitives, so the catalog entry tells you nothing about how they work or where they sit in the call path. The [quickstart](https://langwatch.ai/docs/introduction) is where to find that, along with the SDK's language coverage, which the dossier does not state.

### Among the open-source tracers

[Observability & Tracing](/categories/observability-and-tracing/) has several open-source options with similar aims. [Langfuse](/services/langfuse/) is described in nearly the same words: tracing and evaluation for agents. [OpenLIT](/services/openlit/) leads with OpenTelemetry. [AgentEvals](/services/agentevals/) scores from OpenTelemetry traces after the fact, and [agent-inspect](/services/agent-inspect/) produces local execution trees for TypeScript agents.

On the dossier evidence, the distinguishing pairing is evaluation datasets with regression monitoring. That points at catching quality drift between releases, not only debugging one bad run. Whether the spans follow OpenTelemetry conventions is not stated, and that matters if you want to send the same traces to more than one backend. The guide on [what makes a service agent-native](/guides/what-makes-a-service-agent-native/) explains why tool-call semantics count toward inclusion here.

### Before wiring production traffic

Decide whether you will self-host or use the vendor's cloud, and who then holds prompt and tool payloads. Check how environment keys are scoped, since the dossier names them without detail. Check whether asynchronous recording can drop data when a process exits, which matters for short-lived workers. Read the guardrails documentation if that feature was the reason you looked.

### Editor's take

LangWatch is a reasonable choice for a team that owns its agent code and wants regression checks tied to evaluation datasets in the same tool as tracing. Teams already standardized on OpenTelemetry may find OpenLIT closer to their pipeline, and anyone comparing open-source tracers should read Langfuse's entry alongside this one. Nothing here has been installed by this project; the opinion is formed from the dossier and LangWatch's published docs.
