---
layout: default
title: "Getting started with MCP servers"
description: "Hosts, clients, and servers; local stdio versus remote HTTP; and the registries and credential layers in this catalog."
permalink: /guides/getting-started-with-mcp-servers/
page_kind: document
ads: false
guide_order: 6
---

The Model Context Protocol is an open standard for connecting an AI application to tools and data. The [official introduction](https://modelcontextprotocol.io/docs/getting-started/intro) describes it that way: one protocol so an application such as a coding agent or a chat client can talk to many external systems without a custom integration for each pair. The [architecture documentation](https://modelcontextprotocol.io/docs/learn/architecture) is the better next read once the slogan makes sense. As of the documentation current when this guide was written, the architecture is a host, a client, and a server. The host is the application, for example a desktop chat app or an IDE. The host creates one MCP client per server. The server is the program that offers tools, resources, and prompts.

This catalog is not the specification, and a guide on a directory site should not pretend to be. When this page and the spec disagree, the spec is right. The specification index linked from the architecture docs is the versioned contract. Protocol details move. The 2026-07-28 revision, for example, marks sampling as deprecated. Do not build a design that depends on a feature you remember from an older diagram without checking the current page.

What this catalog does have is a large set of servers, gateways, and credential layers in the [tool collection](/categories/tool-access-and-integration/), plus MCP switches on service pages in every other collection. MCP is a column. It is not the definition of agent-native. A service can pass the [five tests](/guides/what-makes-a-service-agent-native/) with an HTTP API and no server. A human product can ship a server and still fail those tests. Use this guide to attach a server safely. Use the other guides to decide whether the product behind the server is the right kind of product.

## Two transports, two places the process lives

The architecture docs describe two transports.

**Stdio.** The client starts a local process and speaks the protocol on its standard streams. The filesystem server in the official examples is the usual picture: it runs on the same machine as the host, because it has to see the files. There is no network hop. There is also no shared multi-tenant endpoint. The process is yours, and so is whatever credential you put in its environment.

**Streamable HTTP.** A remote server speaks the protocol over HTTP and can serve many clients. The architecture docs use a hosted server as the example. This is the transport you want when the tool is a vendor's API and the process should not be a binary on every laptop. It is also the transport that needs an authentication story. A URL with a secret in the query string is not that story.

You will still see older configs in the wild, including HTTP+SSE from earlier revisions. Prefer what the server's current README says, and prefer the spec's current transport names when you are choosing a design rather than following a vendor's install snippet.

## What a server is allowed to offer

The data layer is JSON-RPC. Servers expose features the architecture docs group as tools, resources, and prompts. Tools are actions the model can call. Resources are data the client can read. Prompts are templates the server is willing to supply. A server does not have to offer all three. A thin server that only exposes tools is normal. A server that offers a prompt the user did not ask for is a place to be careful, because the prompt is instructions.

The client discovers capabilities. That discovery is why a gateway can sit in the middle and why a registry can exist. The model does not need the server's source. It needs the list of tools the host decided to enable. "The server has a tool" and "this agent may call the tool" are different decisions. Hosts that enable every tool from every installed server are how a coding agent ends up able to delete a repository because a search tool and a write tool were both named in the same session.

## A first remote server

The [GitHub MCP Server](https://github.com/github/github-mcp-server) is a reasonable first remote server because the dossier documents a hosted endpoint and a local option, and because the permissions are ones a developer already understands: repositories, issues, pull requests. The dossier's remote configuration points a host at `https://api.githubcopilot.com/mcp/`. Authentication is GitHub's, OAuth or a personal access token depending on the mode you pick. Follow the repository README you are actually installing. The shapes of the config keys differ across hosts, which is frustrating and normal. The protocol is shared. The JSON file is the host's.

Start with a token that can read one repository, call one tool that lists issues, and stop. If that works, you have a host, a client, a server, and an auth path. Adding write tools is a second decision. The server being official does not make a wide token safe.

A first local server is the same lesson on stdio. The official filesystem server, linked from the architecture docs, is the teaching example: you pass it a directory. Pass it a scratch directory. Do not pass it your home directory to see if the demo works.

## Registries, gateways, and the temptation to install everything

Once one server works, the catalog's tool collection is a map of what people build next.

[Smithery](https://smithery.ai) is a registry and gateway for MCP servers and Agent Skills. The dossier describes search, install, and managed authentication. A registry answers "which server exists." It does not answer "should this agent have it." [ToolHive](https://docs.stacklok.com) is a control plane for running servers, including sandboxed execution. [MCPJungle](https://docs.mcpjungle.com), [MetaMCP](https://docs.metamcp.com), [MCPHub](https://docs.mcphub.app/), [Obot](https://docs.obot.ai), and [ContextForge](https://ibm.github.io/mcp-context-forge/) are gateways that put many servers behind one endpoint, with their own notions of namespaces, keys, and federation. [MCP Gateway](https://mcpgateway.com) is the commercial platform in that set.

A gateway is worth it when clients cannot be configured one server at a time, or when you want one place that can see tool calls. A gateway is a liability when it becomes an unaudited proxy in front of production systems. You have moved the trust boundary, not removed it. Read how the gateway stores upstream tokens. If you cannot find that section in the docs, you are not ready to point it at a real account.

## Credentials are the actual problem

Most MCP demos use a local API key because it is short. Production agents call systems that use OAuth, on behalf of a person who is not in the loop when the token expires.

[Arcade](https://docs.arcade.dev/en/mcp-servers) is in the catalog for that reason. The dossier's emphasis is tools that call third-party APIs with OAuth, while the secrets do not enter the model context. [Composio](https://docs.composio.dev) describes discovery and authenticated calls at runtime, so the set of tools is not only what a developer pasted into a config at build time. [Nango](https://docs.nango.dev) is the credential layer: the dossier says the agent asks for a connection and receives a valid token, and Nango stores and refreshes it. [Scalekit](https://docs.scalekit.com/agentkit/overview/) is the same neighborhood, virtual MCP servers and a token vault, with audit logs in the category table.

Use one of these when the tool acts as a user. Do not paste a refresh token into an MCP config and call it delegated auth. The model can be induced to print its environment. A vault that the model cannot read is the difference between a demo and a control. The contribution guide's identity test is this paragraph in formal clothes: the agent, the user, and the permission are different objects.

[Snyk Agent Scan](https://github.com/snyk/agent-scan) and [Grey Ridge](https://github.com/rezearcher/greyridge-x402-tools) are the listings about looking at a server before you trust it. A registry install is code execution with extra steps if the server is a local process. Scan or read it the way you would read a dependency. A remote server is a vendor. Treat the connection the way you treat any vendor that will see the data the tool sends.

## MCP shows up outside the tool collection

Email, browsers, memory, and sandboxes in this catalog often ship a server as one interface among others. AgentMail documents an MCP server beside its REST API. Browserbase documents one beside CDP and Stagehand. Mem0 documents one beside its HTTP API. E2B's dossier describes a server and also describes running servers inside the sandbox. The pattern is "the same product, reachable by a host that speaks MCP." It is not a new product.

That matters when you are choosing. An MCP URL for a browser does not remove the [session trade-offs](/guides/browser-infrastructure-for-agents/). An MCP tool for memory does not decide [who writes the fact](/guides/memory-layers-for-agents/). An MCP tool that runs code does not choose the [isolation boundary](/guides/sandboxes-and-code-execution/). The protocol gets the call across. The primitive is still the inbox, the session, the store, or the machine.

## A setup that is boring enough to keep

Pick one host you already use. Confirm in its docs how it declares a server. The keys are not identical across products, and copying a snippet from the wrong host is the usual first failure.

Add one server, with the narrowest credential that can succeed at a read. Call one tool on purpose. Read the tool result in the host's trace if it has one. The [observability collection](/categories/observability-and-tracing/) exists because "the model said it called the tool" is not a trace.

Then add a write tool only with a gate that is not the prompt. That gate might be the host's approval UI, an [oversight](/categories/oversight-and-approval/) product, or a token that cannot perform the write. MCP does not include a moral sense about destructive tools. Servers expose what they were given.

If the server is remote, prefer the vendor's OAuth over a long-lived key in a dotfile, and read the current spec's authorization notes rather than a blog post from a previous revision. If the server is local, assume it can do anything the operating-system user can do, restricted only by the arguments you passed and the permissions of that user.

Keep the list of enabled tools short. Discovery is a feature. Enabling every discovered tool in every session is how a registry becomes an incident. The catalog can tell you a server exists. It cannot tell you that your agent should have it today.
