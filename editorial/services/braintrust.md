### Open questions first

Two things are left loose in the dossier. It records no verified Agent Skill bundle, so a coding agent cannot be handed a single `SKILL.md` and told to get on with it. And it mentions hybrid and self-hosted data plane options in one line, without saying which components run where, who upgrades them, or what still talks to the vendor. Anyone whose prompts cannot leave their network should treat that line as a pointer to the [Braintrust docs](https://www.braintrust.dev/docs), not as an answer.

What the dossier does document is a loop. Agent code initializes a logger and a trace processor. Every LLM call, tool call, and retriever step lands as a nested span. Scorers built from code, LLM judges, or human review grade the output, and traces that fail become dataset rows for the next regression run. The OpenAI Agents SDK path is specific: install `braintrust[openai-agents]` and register `BraintrustTracingProcessor`. Python, TypeScript, Go, Ruby, and C# SDKs are listed, along with a REST API and a storage engine called Brainstore built for large nested traces.

### Two ways in

The SDK serves the agent being observed. The MCP server serves a different agent: the coding assistant that reads the results. The dossier gives a hosted HTTP endpoint at `api.braintrust.dev/mcp`, a separate EU endpoint, and bearer-token auth with an API key, with OAuth also mentioned. Through it, an IDE agent can query logs, run evals, and manage prompts without leaving the editor.

That split matters for credentials. The key in a production agent's environment and the key in an editor's MCP config do not need the same reach. The dossier says API keys scope access to org and project data, with RBAC deciding who can view traces that may hold sensitive prompts. How narrow a key can be made is a docs question worth settling before one key gets reused in both places.

### Against the rest of the category

The [Observability & Tracing](/categories/observability-and-tracing/) collection holds several products that trace agent runs. [Langfuse](/services/langfuse/) describes itself as open-source LLM observability, tracing, and evaluation. [OpenLIT](/services/openlit/) is OpenTelemetry-native. [AgentEvals](/services/agentevals/) scores agents from existing OpenTelemetry traces without re-running them. Braintrust's weight, per the dossier, sits on the experiment side: comparing prompts and models against datasets and blocking a release when scorers regress, with tracing feeding that loop. The vendor's tagline, "Ship quality AI at scale", points the same way. The catalog's reasons for listing an eval platform at all are in [What makes a service agent-native](/guides/what-makes-a-service-agent-native/).

### Editor's take

Teams already on the OpenAI Agents SDK who want evals as a release gate get a short path here: one processor, a dataset loop, and an MCP endpoint their coding agent can query. If the requirement is source code you can run yourself, start with Langfuse or OpenLIT and come back if the experiment tooling is what you miss. This page is a reading of the catalog dossier and Braintrust's published docs; nobody on this project has instrumented an agent with it.
