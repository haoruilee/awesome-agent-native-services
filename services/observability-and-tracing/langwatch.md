# LangWatch

> **"Open-source LLM Ops platform for tracing, evals, and guardrails."**

| | |
|---|---|
| **Website** | https://langwatch.ai |
| **Docs** | https://docs.langwatch.ai |
| **GitHub** | https://github.com/langwatch/langwatch |
| **Classification** | `agent-native` |
| **Category** | [Observability & Tracing Services](README.md) |

## Official Website
https://langwatch.ai

## Official Repo
https://github.com/langwatch/langwatch

## Agent Skills
**Status:** ⚠️ None found.

## MCP
**Status:** ⚠️ MCP not primary surface.

## What It Does
Tracks agent traces, evaluates quality, and monitors production behavior for autonomous systems.

## Why It Is Agent-Native
Captures trajectory-level signals from agent loops and tool calls, not just single-turn chat logs.

## Primary Primitives
- Traces/spans for agent runs
- Evaluation datasets
- Regression monitoring

## Autonomy Model
Agents execute independently while telemetry is recorded asynchronously.

## Identity and Delegation Model
Run IDs and environment keys attribute actions to agent instances.

## Protocol Surface
SDK + API ingestion endpoints.

## Human-in-the-Loop Support
Human review dashboards and evaluation workflows are optional overlays.

## Why Generic Alternatives Do Not Qualify
Traditional APM lacks agent reasoning/tool-use semantics and eval-centric primitives.

## Use Cases
Production monitoring, eval regression detection, and postmortem analysis of agent failures.
