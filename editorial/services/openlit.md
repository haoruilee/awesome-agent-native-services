Instrumentation has to go into the agent runtime itself. The dossier lists a Python or JS SDK, OpenTelemetry exporters, and backend APIs, with no MCP server and no Agent Skill. An agent does not call this service. Its code is instrumented, and telemetry flows out while the loop runs.

### Spans for tool calls and tokens

The tagline is "OpenTelemetry-native observability for LLMs and AI agents." According to the dossier, the SDK captures agent traces, tool-call spans, latency, token usage, and cost. The primitives are agent run traces, tool-call spans, and token and cost analytics. The How to Use path has three steps: add the SDK, emit traces and metrics, and connect to the OpenLIT backend for dashboards and analysis.

Attribution relies on per-agent and per-run metadata fields. The human side is review and alerting: teams can read traces and set escalation workflows for anomalous behavior. Nothing in the entry describes evaluation, datasets, or prompt management, so treat it as a telemetry product unless the [OpenLIT docs](https://docs.openlit.io) show more.

### OpenTelemetry as the selling point

Several listings in [Observability & Tracing](/categories/observability-and-tracing/) collect similar data. [Langfuse](/services/langfuse/) and [LangWatch](/services/langwatch/) pair tracing with evaluation, and LangWatch's dossier adds regression monitoring. [Braintrust](/services/braintrust/) presents observability and evaluation together. OpenLIT's dossier stays on instrumentation and cost analytics, and its framing is the standard it emits.

That framing has a practical consequence. If spans follow OpenTelemetry, the same data can go to a backend you already run, and tools that read OTel traces, such as [AgentEvals](/services/agentevals/), can score from it. The dossier describes the instrumentation as OpenTelemetry-style in one place and lists OpenTelemetry exporters in another, so check which semantic conventions are used before assuming another backend will render the spans the way OpenLIT's own does.

The [agent-native guide](/guides/what-makes-a-service-agent-native/) explains why the catalog accepts observability tools at all: the primitives are shaped around agent runs and tool calls rather than generic web requests.

### Before you export

Decide where the backend runs and who can read stored prompts and tool arguments. Find out how cost figures are computed, since they depend on model price tables someone has to keep current. Check which agent frameworks the instrumentation covers out of the box. The dossier does not address sampling, retention, or how the backend authenticates exporters.

### Editor's take

A team already running an OpenTelemetry collector is the natural adopter: add the SDK and route spans wherever they already go, with OpenLIT's backend as one destination among several. Teams that want evaluations and regression tracking in the same product should compare LangWatch, Langfuse, or Braintrust first. We have only read the dossier and OpenLIT's documentation, and have not instrumented an agent with it.
