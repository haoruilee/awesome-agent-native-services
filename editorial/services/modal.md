The machines belong to the vendor. A team writes Python, marks functions with Modal's decorator, and Modal schedules containers with the right image and GPU on its own infrastructure, then scales them down when idle. For an agent system, that means compute an orchestrator can start and stop with an SDK call, without anyone running a cluster. It also means code the agent did not write can run in a sandbox that is not on the orchestrator's own host.

### Functions, sandboxes, endpoints

The dossier describes serverless infrastructure for AI workloads: inference, fine-tuning, batch jobs, notebooks, and sandboxes, with elastic GPU and CPU scaling and unified observability. The primitives are a decorated serverless function with GPU, image, and concurrency settings; sandboxes, described as isolated, ephemeral environments for untrusted execution; volumes and buckets for models and datasets; web endpoints that expose a backend over HTTPS; and scheduling that maps a large batch across many containers.

The agent-facing reason is in the sandboxes and the fan-out. An orchestrator can create a sandbox for code a model just generated, run it, and throw it away. It can also spread an eval or a set of tool calls across parallel containers. The dossier lists evals, RL environments, and hosted MCP servers among the marketed workloads.

Integration is the Python SDK and CLI: `pip install modal`, then `modal setup`, with the CLI handling deploy, run, and logs. HTTP endpoints exist for deployed functions. MCP is marked as not the product's surface; teams deploy their own MCP servers on Modal. No official Agent Skill was located. The [Modal docs](https://modal.com/docs) and the guide they link are where to start.

### Compute rather than an agent framework

Most of [Agent Runtime & Infrastructure](/categories/agent-runtime-and-infrastructure/) packages a specific agent shape. [Cloudflare Agents SDK](/services/cloudflare-agents-sdk/) builds and hosts durable agents on Cloudflare's network. [Letta](/services/letta/) centers on stateful agents. [Cyberdesk](/services/cyberdesk/) provides virtual desktops for computer-use agents. Modal is lower in the stack: general compute that an agent system calls, with no opinion about memory, conversation state, or tool schemas. That makes it a host for pieces of an agent rather than an agent runtime. The guide on [what makes a service agent-native](/guides/what-makes-a-service-agent-native/) explains why sandboxes for agent-generated code are counted as an agent primitive here.

### Isolation and secrets to confirm

Modal tokens authenticate API access, secrets are injected as environment variables or Modal secret objects rather than placed in prompts, and team policies govern who can deploy and spend. Check how narrowly a token can be scoped, because an orchestrator holding a full deploy token can do more than create sandboxes.

The dossier does not describe the sandbox isolation boundary, network egress rules inside a sandbox, or how long sandbox state persists. For agent-generated code, those are the questions that matter most, so read the Sandboxes product page and the guide before routing untrusted code there. Data residency is listed as a team control; confirm the regions you need.

### Editor's take

Python teams that need GPUs on demand, parallel evals, or a place to execute model-written code without running Kubernetes have the clearest case. If you want a framework that already manages agent state and conversations, Letta or the Cloudflare Agents SDK start further along. Our read draws on the dossier and Modal's guide and product pages; the project has not deployed a function there.
