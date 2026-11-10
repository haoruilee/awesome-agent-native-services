Code a model just wrote should not run on the machine that wrote it. An agent acting as a code interpreter, or running tests on a cloned repository, needs a disposable computer per task: start it, push code in, read the output, throw it away. Vercel's offering for that is a microVM service, which the docs describe as "Secure, isolated microVMs for AI-generated code."

### A microVM per turn

The dossier describes Firecracker microVMs with full Node.js and Python runtimes. Each sandbox has its own filesystem and network policy. An agent, or the application hosting it, creates a sandbox, streams code or commands into it, reads stdout and files, optionally reaches an HTTP preview URL, and then snapshots or destroys the VM. Commands stream their output, so a long test run does not have to finish before the agent sees anything.

Three interfaces are documented. The TypeScript SDK installs with `npm install @vercel/sandbox`, and the [SDK reference](https://vercel.com/docs/sandbox/sdk-reference) lists its methods. The REST API creates sandboxes with `POST /v1/sandboxes`. A `sandbox` CLI is described for manual and agent-driven debugging. There is no dedicated first-party MCP server, and no official Agent Skill bundle was located. Agents reach it through the SDK or REST from their own runtime.

### Snapshots and the long task

Snapshots save and restore VM state. Persistent sandboxes, marked beta in the dossier, save state across stops automatically. Together they address tasks that outlast one turn, such as a multi-step refactor where the agent wants yesterday's environment back instead of reinstalling dependencies. Check the [Vercel Sandbox docs](https://vercel.com/docs/sandbox) for what a snapshot includes, how long it is kept, and what beta means for persistence guarantees. The docs, not this page, are the place for cold-start times, limits, and pricing.

Credentials are Vercel personal or team tokens, or OIDC when the caller is itself deployed on Vercel. Billing and quotas attach to the team. Isolation is per sandbox, and the host application decides which agents may create one. That last point is easy to miss. The sandbox contains the code, but it does not decide who gets to start sandboxes. Your application does.

### Editor's take

The [code execution collection](/categories/code-execution/) and the [sandboxes guide](/guides/sandboxes-and-code-execution/) cover hosted and local options. [E2B](/services/e2b/) is the most direct hosted comparison, also built around sandboxes for AI-generated code. [OpenSandbox](/services/opensandbox/) and [Axern](/services/axern/) are open-source runtimes you operate. [CodeRunner](/services/coderunner/) keeps execution on the local machine. [AIO Sandbox](/services/agent-infra-sandbox/) bundles browser, shell, files, and MCP in one container, which suits agents that need more than a process.

Teams already deploying on Vercel get the shortest path here, with OIDC instead of a stored token and billing on an existing account. Outside Vercel, compare E2B on features and an open-source runtime on control. Our position comes from reading the dossier and Vercel's public docs, not from creating or snapshotting a sandbox ourselves.
