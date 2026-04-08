# ClawHub

This directory documents how this repository relates to [ClawHub](https://claw-hub.net/) (the OpenClaw skill registry) and optional CLI configuration.

Skill source files for this catalog live under [`.skills/`](../.skills/) in the repo root.

## China mirror (access acceleration)

[mirror-cn.clawhub.com](https://mirror-cn.clawhub.com) is the official landing page for the China mirror; it redirects to the registry front-end.

For the CLI, set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or pass `--registry https://cn.clawhub-mirror.com` (see the mirror site for copy-paste examples).
