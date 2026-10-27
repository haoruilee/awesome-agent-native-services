# Reef

> **"Infrastructure for continually self-improving agents."**

| | |
|---|---|
| **Website** | https://reefinfra.ai |
| **Docs** | https://reefinfra.ai/docs/getting-started/quickstart/ |
| **GitHub** | https://github.com/Human-Agent-Society/reef |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/Human-Agent-Society/reef?style=social)](https://github.com/Human-Agent-Society/reef) |
| **Classification** | `agent-native` |
| **Category** | [Agent Harnesses & Operator Surfaces](README.md) |
| **License** | Apache-2.0 |
| **Verified at** | 2026-10-27 |
| **Latest-month signal** | PyPI `reef-infra` 0.1.3; docs quickstart HTTP 200; GitHub ~7.7k stars, last push 2026-10-27 |

---

## Official Website

https://reefinfra.ai

---

## Official Repo

https://github.com/Human-Agent-Society/reef — open-source continual self-improvement loop for agents (serve → observe → grow → commit). Package: `reef-infra` on PyPI.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** Local/self-hosted Python infra (CLI)

```bash
uv venv && source .venv/bin/activate
uv pip install reef-infra
python3 -c "import reef; print(reef.__version__)"
# minimal inference serve example from upstream README:
uv run reef serve --inference.model-path Qwen/Qwen2.5-1.5B-Instruct
```

Quickstart: https://reefinfra.ai/docs/getting-started/quickstart/

Requires `git-lfs` for artifact/checkpoint flows. Source checkout recommended for training examples.

---

## Agent Skills

**Status:** ⚠️ No official AgentSkills bundle located; integration is the `reef-infra` Python package and CLI.

---

---

## MCP

**Status:** ⚠️ No MCP server in the verified materials — primary surface is the `reef` CLI / Python package (serve, train, evaluate, artifact delivery).

---

## What It Does

Reef connects **agent inference, feedback, learning, and versioned delivery**. Recipes can train model weights (e.g. with Slime/SGLang) or improve an agent's **harness** (prompts, rules, skills) without local training GPUs. Learning cycles: Serve → Observe → Grow → Commit, with version history for accepted updates.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first** | Positioned as infrastructure for continually self-improving agents |
| **Harness primitives** | Versioned artifact delivery, feedback matching, harness optimization path |
| **Autonomy-compatible** | Stays live through updates; selection policy commits accepted updates |
| **M2M** | CLI/Python package for serve and training pipelines |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Serve** | Live inference + interaction records |
| **Observe** | Match feedback to stored interactions |
| **Grow** | Produce updates via recipes (weights or harness) |
| **Commit** | Evaluate and publish versioned artifacts while staying live |

---

## Autonomy Model

```
reef serve — live agent requests + interaction records
    ↓
Observe — match feedback to stored interactions
    ↓
Grow — recipe produces candidate update (weights or harness)
    ↓
Commit — evaluate, accept/reject, publish versioned artifact while service stays live
```

---

## Identity and Delegation Model

- Deployments are configured by operators (model path, recipe, evaluation policy).
- Artifact history versions accepted updates; runtime applies configured selection policy.
- No separate hosted multi-tenant identity layer in the open-source package — identity is deployment-local.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| PyPI | `uv pip install reef-infra` |
| CLI | `reef serve`, training/eval modules under the package |
| Docs | https://reefinfra.ai/docs/getting-started/quickstart/ |
| Source | https://github.com/Human-Agent-Society/reef |

---

## Human-in-the-Loop Support

Operators choose models, recipes, and evaluation/selection policy. Learning cycles can run continuously from interaction feedback; humans supervise deployment and policy, not every request.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Bare vLLM / SGLang serve** | Serves traffic but does not close the feedback→learn→version loop |
| **Offline RL trainer alone** | Trains weights but is not a live harness with versioned delivery while serving |
| **Prompt file in git** | No structured observe/grow/commit pipeline or artifact policy |

---

## Use Cases

- Keep an agent endpoint live while promoting improved weights or harness artifacts
- Optimize prompts/rules/skills from interaction feedback without local GPUs
- Run continual learning recipes with evaluation gates before commit

---

## Verification Sources

- https://github.com/Human-Agent-Society/reef (Apache-2.0)
- https://pypi.org/project/reef-infra/ (0.1.3)
- https://reefinfra.ai/docs/getting-started/quickstart/ (HTTP 200)
