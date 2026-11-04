# Oversight & Approval Services

> Services that give AI agents a structured, **programmatic way to request human approval** before executing high-stakes actions — turning human oversight from an ad-hoc interruption into a first-class, auditable primitive.

## Why This Category Exists

As AI agents gain the ability to take consequential real-world actions — sending emails, executing payments, deleting records, deploying code — the question of *who authorizes these actions* becomes critical. The naive answer ("just don't let the agent do anything risky") eliminates most of the value of autonomy. The right answer is an approval primitive that:

- Lets the agent operate fully autonomously **except** at explicitly annotated decision points
- Routes those decision points to the right human via the right channel (Slack, email, SMS)
- Injects the human's response (approve / deny / modify) back into the agent's context window
- Maintains a tamper-evident audit trail of every approval and every denial

No general-purpose approval workflow (Jira tickets, email threads, ServiceNow) was designed with this inverted control flow: the **agent** initiates, the **human** responds, and the response feeds back into machine context.

## Services

| Service | Tagline | Protocol Surface | MCP? |
|---|---|---|---|
| [Cordum](cordum.md) [![⭐](https://img.shields.io/github/stars/cordum-io/cordum?style=social)](https://github.com/cordum-io/cordum) | The open agent control plane | Pre-execution policy, approval gates, audit trails, MCP adapters | ✅ |
| [Sondera Coding Agent Hooks](sondera-coding-agent-hooks.md) [![⭐](https://img.shields.io/github/stars/sondera-ai/sondera-coding-agent-hooks?style=social)](https://github.com/sondera-ai/sondera-coding-agent-hooks) | A reference monitor for AI coding agents | Rust hooks, Cedar policies, shell/file/web-request interception | ⚠️ |
| [HumanLayer](humanlayer.md) | Human in the Loop for AI Agents | Python SDK, TypeScript SDK, REST API, Webhooks | ✅ |
| [Sallyport](sallyport.md) [![⭐](https://img.shields.io/github/stars/OlegSotnikov/sallyport?style=social)](https://github.com/OlegSotnikov/sallyport) | Let your agent touch prod. Keep the keys. | MCP gate, HTTP/SSH execution, session/per-call approval, signed audit journal | ✅ |
| [Preloop](preloop.md) [![⭐](https://img.shields.io/github/stars/preloop/preloop?style=social)](https://github.com/preloop/preloop) | The Open Source Control Plane for AI Agents | MCP firewall, CEL approvals, model gateway, session audit, CLI discover | ✅ |
| [withHuman](withhuman.md) [![⭐](https://img.shields.io/github/stars/withHumanAI/withHuman?style=social)](https://github.com/withHumanAI/withHuman) | Approval layer that intercepts agent tool calls | AAP protocol · hooks · Python/TS SDKs · review queue | ⚠️ |


---

## Criteria Reminder

To qualify for this category, a service must:

1. Be invoked **by the agent** (not by a human initiating a request).
2. Route approval to a human via a machine-readable channel with a structured response.
3. Inject the approval/denial response back into the **agent's context or control flow**.
4. Maintain a **per-action audit trail** attributable to both the agent and the approving human.
5. Support **asynchronous** approval — the agent should suspend and resume, not block a thread.
