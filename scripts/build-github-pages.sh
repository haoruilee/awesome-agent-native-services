#!/usr/bin/env bash
# Generate docs/index.md from README.md, plus category landing pages for SEO/internal links.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOCS="$ROOT/docs"
README="$ROOT/README.md"
INDEX="$DOCS/index.md"
CAT_ROOT="$DOCS/categories"
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
IMG_DIR="$DOCS/assets/images"
IMG="$IMG_DIR/social-preview.png"

mkdir -p "$IMG_DIR"

if [[ ! -f "$README" ]]; then
  echo "Missing README at $README" >&2
  exit 1
fi

# Front matter for Jekyll SEO (meta description ~140–160 chars for search snippets)
cat >"$INDEX" <<'YAML'
---
title: "Awesome Agent-Native Services (2026) | MCP & Agent Infrastructure"
description: "Best agent-native services in 2026: MCP tools, browser automation, memory, code sandboxes, observability, and agent infrastructure."
image: /assets/images/social-preview.png
---

YAML
# Omit README line 1 — Jekyll theme already renders page.title as the on-page <h1>
tail -n +2 "$README" >>"$INDEX"

{
  echo ""
  echo "---"
  echo ""
  echo "## Explore by category pages (SEO hub)"
  echo ""
  echo "Navigate by category to compare services faster:"
  echo ""
  for dir in "$ROOT"/services/*; do
    [[ -d "$dir" ]] || continue
    slug="$(basename "$dir")"
    pretty="$(echo "$slug" | tr '-' ' ')"
    pretty="$(echo "$pretty" | sed -E 's/\b([a-z])/\U\1/g')"
    echo "- [${pretty}]({{ '/categories/${slug}/' | relative_url }})"
  done
  echo ""
  echo "_Last site build time: {{ site.time | date: '%Y-%m-%d %H:%M UTC' }}_"
} >>"$INDEX"

# Generate category landing pages (spokes)
rm -rf "$CAT_ROOT"
mkdir -p "$CAT_ROOT"
cat >"$CAT_ROOT/index.md" <<'YAML'
---
title: "Agent-Native Service Categories"
description: "Browse agent-native services by category: communication, browser automation, MCP tools, memory, runtimes, and more."
permalink: /categories/
---

This page helps search engines and humans discover the catalog through focused category landing pages.

YAML

for dir in "$ROOT"/services/*; do
  [[ -d "$dir" ]] || continue
  slug="$(basename "$dir")"
  pretty="$(echo "$slug" | tr '-' ' ')"
  pretty="$(echo "$pretty" | sed -E 's/\b([a-z])/\U\1/g')"
  out="$CAT_ROOT/$slug.md"

  {
    cat <<YAML
---
title: "${pretty} | Agent-Native Services"
description: "Agent-native ${pretty,,} services with onboarding links, MCP status, and official references."
permalink: /categories/${slug}/
---

> Category source: [services/${slug}/README.md](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/${slug}/README.md)

## Services in this category

| Service | Catalog Entry |
|---|---|
YAML

    for file in "$dir"/*.md; do
      [[ -f "$file" ]] || continue
      base="$(basename "$file")"
      [[ "$base" == "README.md" ]] && continue
      service_slug="${base%.md}"
      service_title="$(sed -n '1{s/^# //;p;q;}' "$file")"
      [[ -n "$service_title" ]] || service_title="$service_slug"
      echo "| ${service_title} | [services/${slug}/${base}](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/${slug}/${base}) |"
    done
  } >"$out"

  echo "- [${pretty}]({{ '/categories/${slug}/' | relative_url }})" >>"$CAT_ROOT/index.md"
done

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
echo "Wrote category pages under $CAT_ROOT"
