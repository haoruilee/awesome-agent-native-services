# OpenLIT

> **"OpenTelemetry-native observability for LLMs and AI agents."**

| | |
|---|---|
| **Website** | https://openlit.io |
| **Docs** | https://docs.openlit.io |
| **GitHub** | https://github.com/openlit/openlit |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/openlit/openlit?style=social)](https://github.com/openlit/openlit) |
| **Classification** | `agent-native` |
| **Category** | [Observability & Tracing Services](README.md) |

## Official Website
https://openlit.io

## Official Repo
https://github.com/openlit/openlit

## How to Use (Agent Onboarding)
Install SDK instrumentation in the agent runtime, emit traces/metrics, and connect to OpenLIT backend for dashboards and analysis.

## Agent Skills
**Status:** ⚠️ No official AgentSkills package found.

## MCP
**Status:** ⚠️ No standalone official MCP server package.

## What It Does
Captures agent traces, tool-call spans, latency, token usage, and cost telemetry via OpenTelemetry-style instrumentation.

## Why It Is Agent-Native
Observability primitives are centered on LLM/agent run structure rather than generic web-request-only metrics.

## Primary Primitives
- Agent run traces
- Tool-call spans
- Token/cost analytics

## Autonomy Model
Runs continuously in autonomous loops without requiring operator interaction.

## Identity and Delegation Model
Per-agent and per-run metadata fields enable attribution and policy-aware analysis.

## Protocol Surface
Python/JS SDK, OpenTelemetry exporters, backend APIs.

## Human-in-the-Loop Support
Teams can review traces and set alert/escalation workflows for anomalous behavior.

## Why Generic Alternatives Do Not Qualify
General APM products do not natively model prompt/tool/reasoning lifecycle semantics.

## Use Cases
- Production agent monitoring
- Cost and latency optimization
- Tool reliability analysis
