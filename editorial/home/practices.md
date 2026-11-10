<!--
Homepage source for the practices section. scripts/home_editorial.py renders
this file into docs/index.md. Edit this file, then run
bash scripts/build-github-pages.sh. Do not hand-edit the generated section.
-->

# Practices we keep coming back to

Seven decisions the guides keep returning to. The essays are the long form. These are the lines that still seem true once the comparison tables are closed.

## Four out of five is still a miss

takeaway: A page that says "for agents" can still be a person's account with a new headline.
guide: /guides/what-makes-a-service-agent-native/
guide_title: What makes a service agent-native
collection: /categories/
collection_title: All collections

The catalog refuses a service with tests you can point at. The vendor's pages have to name agents as the caller. The primitive has to be something a human product would not need. The agent has to finish the loop. The interface has to be a machine's. Outward action needs an identity that is not the operator's. Drop one and the proposal is out. The usual miss is an adapted product: a real API, a post that welcomes agents, and a user account. Operator surfaces are a narrow exception. They must read live agent state, tie it to a session, and admit the powers they lack. A passing card is a listing, not a recommendation.

## Who replies decides the inbox

takeaway: Correspondence, a one-time code, a notification, and notes between coding agents are four different products.
guide: /guides/choose-an-email-api-for-agents/
guide_title: How to choose an email API for AI agents
collection: /categories/communication/
collection_title: Communication

"Send email" is not a requirement until the other party has a name. A stranger who must reach the agent needs an address the agent owns, threads as data, and inbound mail as an event. A signup that only needs a code needs a mailbox that can wait. A person who already uses the product needs a notification, not a second public identity. Another coding agent in the same repository needs a record beside the code, not an MX record. A review-before-send gate is a real control. A sentence in the prompt that says not to email the customer is not. When a person must prove the domain first, that step is DNS being honest.

## A document, a click, or someone else's login

takeaway: Extraction, a disposable session, and a browser that is already signed in are not interchangeable.
guide: /guides/browser-infrastructure-for-agents/
guide_title: Browser infrastructure for agents compared
collection: /categories/browser-and-web-execution/
collection_title: Browser & Web Execution

The browser collection shares a page and not an architecture. An extraction API returns markdown or JSON and never submits the form. A hosted session is a browser the agent creates, drives, and throws away, which is what a click with a side effect requires. A local browser that kept its cookies can do what a fresh cloud profile cannot, because it is already signed in as a person. Mixing those up is how an agent reports a task that never happened, or pays for a full browser to fetch a public document. A task that works only when someone is already signed in is borrowing an identity, and the gate has to sit outside the model.

## Retrieval is not a memory

takeaway: What may be written, contradicted, forgotten, and named is the product. The index is only a part.
guide: /guides/memory-layers-for-agents/
guide_title: Memory layers for agents: approaches and trade-offs
collection: /categories/memory-and-state/
collection_title: Memory & State

The next call sees the prompt you assembled, not the previous session, unless something was stored on purpose. Putting the transcript back in fails once the old lines crowd out the question. A vector index finds similar chunks and still has no lifecycle. Something has to decide that a sentence was a fact, that a newer sentence retired it, and which identity may read the row. Automatic extractors write when the agent forgets to, and also when the agent would have refused. A shared store leaks if user and agent are the same key. A store on one laptop is blank in CI unless the sync is real.

## Name the wall, including the network

takeaway: A filesystem that cannot see your disk, and a network that can still see the internet, are different promises.
guide: /guides/sandboxes-and-code-execution/
guide_title: Sandboxes and code execution for agents
collection: /categories/code-execution/
collection_title: Code Execution

Code a model just wrote should not run in the process that wrote it. This collection is environments an agent can create, run, read a result from, and destroy, with enough state that the next snippet still sees the previous files. A hosted microVM is the short path, and the vendor sees the code. A Kubernetes resource fits when you already operate a cluster, and nowhere else. A local hypervisor is only as strict as its mounts and its egress list. A container that bind-mounts a home directory is not a sandbox because the command says so. Secrets belong in neither the prompt nor an image shared across tenants.

## The protocol is not the permission

takeaway: A registry can tell you a tool exists. It cannot decide that this agent may call it.
guide: /guides/getting-started-with-mcp-servers/
guide_title: Getting started with MCP servers
collection: /categories/tool-access-and-integration/
collection_title: Tool Access & Integration

MCP is how a host talks to servers that offer tools. It is not what this catalog means by agent-native. An HTTP API can pass the admission tests with no server, and a product built for people can ship a server and still fail. Stdio is a program you start beside the host. Remote HTTP is someone else's endpoint, and a secret in the query string is not an auth design. One server, one read, and the narrowest token that works is a finished first setup. The block on a bad write should not be a sentence in the prompt. A gateway moves where tokens sit. It does not remove the trust boundary.

## Three layers before anything is signed

takeaway: Identity, settlement, and the right to refuse are different parts. A demo usually has only one.
guide: /guides/payments-for-autonomous-agents/
guide_title: Payments for autonomous agents
collection: /categories/commerce-and-payments/
collection_title: Commerce & Payments

A checkout for people has a signal an agent lacks: someone clicked Buy. What remains is who the agent is, what it may spend, and which record names the agent rather than a shared card. A wallet whose cap lives outside the model makes the agent a principal. An HTTP 402 challenge lets a metered API demand payment inside the request, and it does not create that cap. A mandate is evidence of what a person authorized when nobody was at the button. A probe, a co-signer, or a band the signing key cannot bypass is the check that should run first. A token transfer with no identity and no limit is not this category.
