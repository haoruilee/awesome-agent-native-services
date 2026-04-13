#!/usr/bin/env bash
# Generate docs/index.md from README.md and refresh the social preview image.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOCS="$ROOT/docs"
README="$ROOT/README.md"
INDEX="$DOCS/index.md"
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
IMG_DIR="$DOCS/assets/images"
IMG="$IMG_DIR/social-preview.png"

mkdir -p "$IMG_DIR"

if [[ ! -f "$README" ]]; then
  echo "Missing README at $README" >&2
  exit 1
fi

# Front matter for Jekyll SEO (description ~155 chars)
cat >"$INDEX" <<'YAML'
---
title: "Awesome Agent-Native Services | Curated List for AI Agents"
description: "A curated list of agent-first services, MCP servers, and infrastructure optimized for autonomous AI agents and LLM workflows."
image: /assets/images/social-preview.png
---

YAML
# Omit README line 1 — Jekyll theme already renders page.title as the on-page <h1>
tail -n +2 "$README" >>"$INDEX"

# 1200×630 Open Graph image (solid brand color + title)
if command -v ffmpeg >/dev/null 2>&1 && [[ -f "$FONT" ]]; then
  ffmpeg -y -f lavfi -i color=c=0x1a5f7a:s=1200x630 -vf "\
drawtext=fontfile=${FONT}:\
text='Awesome Agent-Native Services':fontsize=48:fontcolor=white:x=(w-text_w)/2:y=200,\
drawtext=fontfile=${FONT}:\
text='MCP servers, LLM tools & agent infrastructure':fontsize=32:fontcolor=white:x=(w-text_w)/2:y=290,\
drawtext=fontfile=${FONT}:\
text='haoruilee/awesome-agent-native-services':fontsize=24:fontcolor=0xDDEEFF:x=(w-text_w)/2:y=400\
" -frames:v 1 "$IMG" -loglevel error
  echo "Wrote $IMG"
else
  echo "Skipping OG image (ffmpeg or font missing); keep existing $IMG if present." >&2
fi

echo "Wrote $INDEX"
