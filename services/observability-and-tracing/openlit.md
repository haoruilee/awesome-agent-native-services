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

## What It Does
OpenLIT captures LLM and agent runtime traces, tool calls, token/cost metrics, and latency spans using OpenTelemetry-compatible instrumentation.

## Why It Is Agent-Native
- Agent-first telemetry primitives (agent run, tool-call, prompt/response spans).
- Works headlessly in autonomous loops.
- API/SDK-first integration surface.

## Primary Primitives
- Agent traces
- Tool-call spans
- Cost/token analytics
- Evaluation hooks

## Protocol Surface
Python/JS SDK + OpenTelemetry exporters + backend APIs.

## Why Generic Alternatives Do Not Qualify
Traditional APM tools do not model agent-loop/tool-call semantics as first-class primitives.
