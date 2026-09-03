#!/usr/bin/env bash
# Generate the editorial GitHub Pages collection from the Markdown catalog.
set -euo pipefail

export LC_ALL=C

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOCS="$ROOT/docs"
README="$ROOT/README.md"
INDEX="$DOCS/index.md"
CAT_ROOT="$DOCS/categories"
IMG_DIR="$DOCS/assets/images"
IMG="$IMG_DIR/social-preview.png"
HERO_IMG="$IMG_DIR/editorial-hero.webp"
ARRIVAL_ATLAS="$IMG_DIR/arrival-atlas.webp"
SERVICE_ATLAS="$IMG_DIR/service-atlas.webp"
EDITORIAL_IMAGES=(
  "$IMG_DIR/editorial-network.webp"
  "$IMG_DIR/editorial-authority.webp"
  "$IMG_DIR/editorial-runtime.webp"
  "$IMG_DIR/editorial-memory.webp"
  "$IMG_DIR/editorial-resonance.webp"
  "$IMG_DIR/editorial-routing.webp"
  "$IMG_DIR/editorial-routing-2.webp"
  "$IMG_DIR/editorial-communication.webp"
  "$IMG_DIR/editorial-browser.webp"
  "$IMG_DIR/editorial-tools.webp"
  "$IMG_DIR/editorial-oversight.webp"
  "$IMG_DIR/editorial-commerce.webp"
  "$IMG_DIR/editorial-harness.webp"
  "$IMG_DIR/editorial-search.webp"
  "$IMG_DIR/editorial-sandbox.webp"
  "$IMG_DIR/editorial-observability.webp"
  "$IMG_DIR/editorial-durable.webp"
  "$IMG_DIR/editorial-meeting.webp"
  "$IMG_DIR/editorial-voice.webp"
  "$IMG_DIR/editorial-social.webp"
  "$IMG_DIR/editorial-vault.webp"
  "$IMG_DIR/editorial-browser-2.webp"
  "$IMG_DIR/editorial-memory-2.webp"
  "$IMG_DIR/social-preview-wide.webp"
)

mkdir -p "$IMG_DIR"

if [[ ! -f "$README" ]]; then
  echo "Missing README at $README" >&2
  exit 1
fi

for asset in "$HERO_IMG" "$ARRIVAL_ATLAS" "$SERVICE_ATLAS" "${EDITORIAL_IMAGES[@]}"; do
  if [[ ! -s "$asset" ]]; then
    echo "Missing required editorial asset at $asset" >&2
    exit 1
  fi
done

category_label() {
  case "$1" in
    communication) echo "Communication" ;;
    browser-and-web-execution) echo "Browser & Web Execution" ;;
    tool-access-and-integration) echo "Tool Access & Integration" ;;
    oversight-and-approval) echo "Oversight & Approval" ;;
    commerce-and-payments) echo "Commerce & Payments" ;;
    agent-runtime-and-infrastructure) echo "Agent Runtime & Infrastructure" ;;
    agent-harnesses-and-control-planes) echo "Agent Harnesses & Operator Surfaces" ;;
    memory-and-state) echo "Memory & State" ;;
    search-and-web-intelligence) echo "Search & Web Intelligence" ;;
    code-execution) echo "Code Execution" ;;
    observability-and-tracing) echo "Observability & Tracing" ;;
    durable-execution-and-scheduling) echo "Durable Execution & Scheduling" ;;
    meeting-and-conversation) echo "Meeting & Conversation" ;;
    voice-and-phone) echo "Voice & Phone" ;;
    llm-gateway-and-routing) echo "LLM Gateway & Routing" ;;
    agent-social-network) echo "Agent Social & Community" ;;
    *) echo "$1" | tr '-' ' ' ;;
  esac
}

category_description() {
  case "$1" in
    communication) echo "Agent-owned inboxes, messaging identities, and cross-channel communication." ;;
    browser-and-web-execution) echo "Browsers, web runtimes, and authenticated sessions built for autonomous navigation." ;;
    tool-access-and-integration) echo "Machine-native tools, MCP surfaces, delegated credentials, and execution gateways." ;;
    oversight-and-approval) echo "Approval, policy, escalation, and review boundaries for consequential agent actions." ;;
    commerce-and-payments) echo "Wallets, payment authorization, identity, and transactions for autonomous buyers and sellers." ;;
    agent-runtime-and-infrastructure) echo "Deployment substrates, isolation, identity, secrets, gateways, and production agent operations." ;;
    agent-harnesses-and-control-planes) echo "Harnesses, control planes, and purpose-built operator surfaces for capable agents." ;;
    memory-and-state) echo "Persistent context, structured knowledge, and cross-session state owned by agents." ;;
    search-and-web-intelligence) echo "Search and retrieval interfaces shaped for context windows and machine reasoning." ;;
    code-execution) echo "Secure, isolated environments for agent-generated code and reproducible artifacts." ;;
    observability-and-tracing) echo "Trajectories, costs, evidence, attribution, evaluation, and forensic replay for agent runs." ;;
    durable-execution-and-scheduling) echo "Fault-tolerant workflows, queues, checkpoints, triggers, and long-running agent jobs." ;;
    meeting-and-conversation) echo "Programmatic agent presence in live meetings, shared rooms, and conversation streams." ;;
    voice-and-phone) echo "Realtime speech, telephone identity, calls, and audio runtimes for agents." ;;
    llm-gateway-and-routing) echo "Budget-aware model access, routing, caching, policy, and trajectory-sensitive escalation." ;;
    agent-social-network) echo "Networks and shared spaces where agents are first-class participants and collaborators." ;;
    *) echo "Agent-native services selected for this collection." ;;
  esac
}

category_hero_image() {
  case "$1" in
    communication) echo "/assets/images/editorial-communication.webp" ;;
    browser-and-web-execution) echo "/assets/images/editorial-browser.webp" ;;
    tool-access-and-integration) echo "/assets/images/editorial-tools.webp" ;;
    oversight-and-approval) echo "/assets/images/editorial-oversight.webp" ;;
    commerce-and-payments) echo "/assets/images/editorial-commerce.webp" ;;
    agent-runtime-and-infrastructure) echo "/assets/images/editorial-runtime.webp" ;;
    agent-harnesses-and-control-planes) echo "/assets/images/editorial-harness.webp" ;;
    memory-and-state) echo "/assets/images/editorial-memory.webp" ;;
    search-and-web-intelligence) echo "/assets/images/editorial-search.webp" ;;
    code-execution) echo "/assets/images/editorial-sandbox.webp" ;;
    observability-and-tracing) echo "/assets/images/editorial-observability.webp" ;;
    durable-execution-and-scheduling) echo "/assets/images/editorial-durable.webp" ;;
    meeting-and-conversation) echo "/assets/images/editorial-meeting.webp" ;;
    voice-and-phone) echo "/assets/images/editorial-voice.webp" ;;
    llm-gateway-and-routing) echo "/assets/images/editorial-routing.webp" ;;
    agent-social-network) echo "/assets/images/editorial-social.webp" ;;
    *) echo "/assets/images/editorial-hero.webp" ;;
  esac
}

category_hero_alt() {
  case "$1" in
    communication)
      echo "Two white alcoves face each other on a dark plinth, joined by a thin gold line."
      ;;
    browser-and-web-execution)
      echo "A square opening in a plaster wall crossed by a brass rod, with dark stone steps and a red cube."
      ;;
    tool-access-and-integration)
      echo "Slender brass instruments standing in a grooved stone block, with two tools lying before a dark slab."
      ;;
    oversight-and-approval)
      echo "A black arched doorway in a plaster wall barred by a horizontal brass rod beside a burgundy column."
      ;;
    commerce-and-payments)
      echo "A gold coin standing in a slotted cream block, with a charcoal pillar and a red plane behind it."
      ;;
    agent-runtime-and-infrastructure)
      echo "Tiered beige stone platforms and matte-black pillars linked by thin gold rods."
      ;;
    agent-harnesses-and-control-planes)
      echo "A charcoal block strapped in a brushed-brass frame with handle-like rods."
      ;;
    memory-and-state)
      echo "A dark glass disc on a gold rod set against a layered white form with a spherical void."
      ;;
    search-and-web-intelligence)
      echo "Textured plates and a smoked-glass disc threaded on a brass rod that ends in a black block."
      ;;
    code-execution)
      echo "A gold sphere isolated in a glass case on a dark stone base and cream pedestals."
      ;;
    observability-and-tracing)
      echo "A cream stone block cut open to dark geological layers with a thin gold vein."
      ;;
    durable-execution-and-scheduling)
      echo "Cream L-shaped blocks and one dark stone block threaded on a single brass rod."
      ;;
    meeting-and-conversation)
      echo "A cream pedestal holding a gold ring, with three black spheres in a sunlit corner."
      ;;
    voice-and-phone)
      echo "A beige horn-shaped vessel with a gold sphere at its center, resting on a dark plinth."
      ;;
    llm-gateway-and-routing)
      echo "Parallel gold pipes flowing through dark translucent panels above a winding marble and stone base."
      ;;
    agent-social-network)
      echo "A black cylinder inside a gold ring, with black spheres gathered around it on a plaster floor."
      ;;
    *)
      echo "Editorial study for an agent-native collection: plaster volumes, charcoal forms, and gold connectors."
      ;;
  esac
}

category_order() {
  case "$1" in
    communication) echo 1 ;;
    browser-and-web-execution) echo 2 ;;
    tool-access-and-integration) echo 3 ;;
    oversight-and-approval) echo 4 ;;
    commerce-and-payments) echo 5 ;;
    agent-runtime-and-infrastructure) echo 6 ;;
    agent-harnesses-and-control-planes) echo 7 ;;
    memory-and-state) echo 8 ;;
    search-and-web-intelligence) echo 9 ;;
    code-execution) echo 10 ;;
    observability-and-tracing) echo 11 ;;
    durable-execution-and-scheduling) echo 12 ;;
    meeting-and-conversation) echo 13 ;;
    voice-and-phone) echo 14 ;;
    llm-gateway-and-routing) echo 15 ;;
    agent-social-network) echo 16 ;;
    *) echo 99 ;;
  esac
}

service_count_for() {
  find "$ROOT/services/$1" -maxdepth 1 -type f -name '*.md' ! -name README.md | wc -l | tr -d ' '
}

yaml_escape() {
  printf '%s' "$1" | sed 's/"/\\"/g'
}

html_escape() {
  printf '%s' "$1" | sed \
    -e 's/&/\&amp;/g' \
    -e 's/</\&lt;/g' \
    -e 's/>/\&gt;/g' \
    -e 's/"/\&quot;/g' \
    -e "s/'/\&#39;/g"
}

strip_inline_markdown() {
  printf '%s' "$1" | sed -E \
    -e 's/\[([^][]+)\]\([^)]*\)/\1/g' \
    -e 's/\*\*//g' \
    -e 's/`//g'
}

markdown_escape_cell() {
  printf '%s' "$1" | tr '\n' ' ' | sed 's/|/\\|/g'
}

extract_field() {
  local file="$1"
  local label="$2"
  awk -F'|' -v target="$label" '
    $0 ~ "\\*\\*" target "\\*\\*" {
      value=$3
      gsub(/^[[:space:]]+|[[:space:]]+$/, "", value)
      gsub(/`/, "", value)
      print value
      exit
    }
  ' "$file"
}

extract_tagline() {
  local file="$1"
  awk '
    /^> / {
      line=$0
      sub(/^> /, "", line)
      gsub(/\*\*/, "", line)
      gsub(/^"|"$/, "", line)
      print line
      exit
    }
  ' "$file" | sed -E \
    -e 's/\[([^][]+)\]\([^)]*\)/\1/g' \
    -e 's/`//g'
}

extract_repo_url() {
  local file="$1"
  local value
  local repo_pattern='https://github\.com/[^[:space:]<]+'
  value="$(extract_field "$file" "GitHub")"
  if [[ "$value" =~ $repo_pattern ]]; then
    printf '%s' "${BASH_REMATCH[0]}" | sed 's/[),·].*$//'
  else
    # Only accept a URL declared immediately under "Official Repo". Falling
    # back to the first GitHub link in the dossier can mislabel an SDK,
    # registry, specification, or comparison project as the service's repo.
    awk '
      /^## Official Repo[[:space:]]*$/ { in_repo = 1; next }
      in_repo && /^## / { exit }
      in_repo && /^https:\/\/github\.com\// { print; exit }
      in_repo && NF { exit }
    ' "$file" | sed -nE 's#^(https://github\.com/[^[:space:]|),·]+).*#\1#p'
  fi
}

extract_latest_signal() {
  strip_inline_markdown "$(extract_field "$1" "Latest-month signal")"
}

is_new_arrival() {
  local file="$1"
  [[ -n "$(extract_latest_signal "$file")" ]]
}

mapfile -t CATEGORY_SLUGS < <(
  for dir in "$ROOT"/services/*; do
    [[ -d "$dir" ]] || continue
    slug="$(basename "$dir")"
    printf '%03d\t%s\n' "$(category_order "$slug")" "$slug"
  done | sort -n -k1,1 | cut -f2
)

TOTAL_SERVICES=0
for slug in "${CATEGORY_SLUGS[@]}"; do
  TOTAL_SERVICES=$((TOTAL_SERVICES + $(service_count_for "$slug")))
done
TOTAL_COLLECTIONS="${#CATEGORY_SLUGS[@]}"
NEW_ARRIVALS=0
while IFS= read -r file; do
  if is_new_arrival "$file"; then
    NEW_ARRIVALS=$((NEW_ARRIVALS + 1))
  fi
done < <(find "$ROOT/services" -mindepth 2 -maxdepth 2 -type f -name '*.md' ! -name README.md | sort)

cat >"$INDEX" <<YAML
---
title: "The Agent-Native Index"
description: "A curated 2026 collection of agent-native infrastructure: MCP tools, harnesses, identity, memory, sandboxes, browsers, payments, and runtimes."
image: /assets/images/social-preview-wide.webp
page_kind: home
service_count: ${TOTAL_SERVICES}
collection_count: ${TOTAL_COLLECTIONS}
new_arrivals_count: ${NEW_ARRIVALS}
---

<section id="new-arrivals" aria-labelledby="new-arrivals-title">
  <div class="section-intro">
    <span class="section-number">01</span>
    <h2 class="section-title" id="new-arrivals-title">New arrivals</h2>
    <p class="section-note">13 Jul—13 Aug 2026</p>
  </div>
  <div class="arrival-rail" role="region" aria-label="Last 30 days additions" tabindex="0">
YAML

arrival_visual_index=0
while IFS= read -r record; do
  arrival_visual_index=$((arrival_visual_index + 1))
  file="${record#*$'\t'}"
  slug="$(basename "$(dirname "$file")")"
  base="$(basename "$file")"
  title="$(sed -n '1{s/^# //;p;q;}' "$file")"
  label="$(category_label "$slug")"
  visual_number="$(printf '%02d' "$(((arrival_visual_index - 1) % 16 + 1))")"
  if (( ((arrival_visual_index - 1) / 16) % 2 == 0 )); then
    atlas_sheet="atlas-sheet--arrival"
  else
    atlas_sheet="atlas-sheet--service"
  fi
  title_html="$(html_escape "$title")"
  label_html="$(html_escape "$label")"
  {
    printf '    <a class="arrival-card %s atlas-visual--%s" href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/%s/%s">\n' "$atlas_sheet" "$visual_number" "$slug" "$base"
    echo '      <span class="arrival-card__image" aria-hidden="true"></span>'
    echo '      <span class="arrival-card__copy">'
    printf '        <span class="arrival-card__category">%s</span>\n' "$label_html"
    printf '        <strong class="arrival-card__name">%s</strong>\n' "$title_html"
    echo '        <span class="arrival-card__arrow" aria-hidden="true">↗</span>'
    echo '      </span>'
    echo '    </a>'
  } >>"$INDEX"
done < <(
  while IFS= read -r file; do
    if is_new_arrival "$file"; then
      signal="$(extract_latest_signal "$file")"
      printf '%s\t%s\n' "$signal" "$file"
    fi
  done < <(find "$ROOT/services" -mindepth 2 -maxdepth 2 -type f -name '*.md' ! -name README.md | sort) | sort -r
)

cat >>"$INDEX" <<HTML
  </div>
</section>

<section id="material-studies" class="editorial-gallery" aria-label="Material studies for agent-native infrastructure">
  <figure class="editorial-gallery__item editorial-gallery__item--wide"><img src="{{ '/assets/images/editorial-network.webp' | relative_url }}" alt="Gold wires passing through a sequence of stone arches and converging into a circular hub." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-communication.webp' | relative_url }}" alt="Two white alcoves face each other on a dark plinth, joined by a thin gold line." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-authority.webp' | relative_url }}" alt="A gold beam balanced on stone disks in front of nested golden arches." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-oversight.webp' | relative_url }}" alt="A black arched doorway in a plaster wall barred by a horizontal brass rod beside a burgundy column." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-browser.webp' | relative_url }}" alt="A square opening in a plaster wall crossed by a brass rod, with dark stone steps and a red cube." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-runtime.webp' | relative_url }}" alt="Tiered beige stone platforms and matte-black pillars linked by thin gold rods." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-harness.webp' | relative_url }}" alt="A charcoal block strapped in a brushed-brass frame with handle-like rods." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-memory.webp' | relative_url }}" alt="A dark glass disc on a gold rod set against a layered white form with a spherical void." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-search.webp' | relative_url }}" alt="Textured plates and a smoked-glass disc threaded on a brass rod that ends in a black block." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-tools.webp' | relative_url }}" alt="Slender brass instruments standing in a grooved stone block, with two tools lying before a dark slab." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-routing-2.webp' | relative_url }}" alt="Five brass rods with spherical nodes converging into a vertical slot on a plaster wall." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-vault.webp' | relative_url }}" alt="A beige stone block with a central brass keyhole, standing on a dark pedestal." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-browser-2.webp' | relative_url }}" alt="A gold sphere resting on the ledge of a stepped rectangular recess in a plaster wall." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-memory-2.webp' | relative_url }}" alt="Pale sheets stacked on a black cube and burgundy plinth, framed by a gold hoop, with a brass wedge marking one layer." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item editorial-gallery__item--panorama"><img src="{{ '/assets/images/editorial-routing.webp' | relative_url }}" alt="Parallel gold pipes flowing through dark translucent panels above a winding marble and stone base." width="1536" height="1024" loading="lazy" decoding="async"></figure>
</section>

<section id="collections" aria-labelledby="collections-title">
  <div class="section-intro">
    <span class="section-number">02</span>
    <h2 class="section-title" id="collections-title">The collections</h2>
    <p class="section-note">${TOTAL_COLLECTIONS} fields · ${TOTAL_SERVICES} dossiers</p>
  </div>
  <div class="collection-grid">
HTML

for slug in "${CATEGORY_SLUGS[@]}"; do
  number="$(printf '%02d' "$(category_order "$slug")")"
  label="$(category_label "$slug")"
  description="$(category_description "$slug")"
  count="$(service_count_for "$slug")"
  label_html="$(html_escape "$label")"
  description_html="$(html_escape "$description")"
  {
    printf '    <a class="collection-card atlas-visual--%s" href="{{ '\''/categories/%s/'\'' | relative_url }}">\n' "$number" "$slug"
    echo '      <span class="collection-card__image" aria-hidden="true"></span>'
    echo '      <span class="collection-card__copy">'
    printf '      <span class="collection-card__number">%s</span>\n' "$number"
    printf '      <span class="collection-card__title">%s</span>\n' "$label_html"
    printf '      <span class="collection-card__count">%s</span>\n' "$count"
    echo '      </span>'
    echo '    </a>'
  } >>"$INDEX"
done

cat >>"$INDEX" <<HTML
  </div>
</section>

<section id="for-agents" class="agent-entry-panel" aria-labelledby="agent-entry-title">
  <p class="eyebrow">Machine entrance</p>
  <h2 id="agent-entry-title">Enter as an agent.</h2>

  <pre><code>Read https://lihaorui.com/awesome-agent-native-services/skill.md then find services designed for you natively.</code></pre>

  <div class="agent-entry-panel__links">
    <a href="{{ '/skill.md' | relative_url }}">skill.md ↗</a>
    <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/CONTRIBUTING.md">Criteria ↗</a>
    <a href="#faq">FAQ</a>
  </div>
</section>

{% include home-faq.html %}

<section class="source-gateway" id="complete-index">
  <span class="source-gateway__image" aria-hidden="true"></span>
  <div>
  <span class="section-number">03</span>
  <h2 class="section-title">Full source.</h2>
  <a class="source-gateway__link" href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/README.md">Open ${TOTAL_SERVICES} dossiers ↗</a>
  </div>
</section>
HTML

# Generate collection landing pages.
if [[ -d "$CAT_ROOT" ]]; then
  find "$CAT_ROOT" -mindepth 1 -maxdepth 1 -type f -delete
else
  mkdir -p "$CAT_ROOT"
fi

cat >"$CAT_ROOT/index.md" <<YAML
---
title: "Agent-Native Collections"
description: "Browse ${TOTAL_SERVICES} agent-native services across ${TOTAL_COLLECTIONS} curated infrastructure collections."
permalink: /categories/
page_kind: document
---

<div class="collection-grid">
YAML

for slug in "${CATEGORY_SLUGS[@]}"; do
  number="$(printf '%02d' "$(category_order "$slug")")"
  label="$(category_label "$slug")"
  description="$(category_description "$slug")"
  count="$(service_count_for "$slug")"
  label_html="$(html_escape "$label")"
  description_html="$(html_escape "$description")"
  {
    printf '  <a class="collection-card atlas-visual--%s" href="{{ '\''/categories/%s/'\'' | relative_url }}">\n' "$number" "$slug"
    echo '    <span class="collection-card__image" aria-hidden="true"></span>'
    echo '    <span class="collection-card__copy">'
    printf '    <span class="collection-card__number">%s</span>\n' "$number"
    printf '    <span class="collection-card__title">%s</span>\n' "$label_html"
    printf '    <span class="collection-card__count">%s</span>\n' "$count"
    echo '    </span>'
    echo '  </a>'
  } >>"$CAT_ROOT/index.md"
done
echo '</div>' >>"$CAT_ROOT/index.md"

for index in "${!CATEGORY_SLUGS[@]}"; do
  slug="${CATEGORY_SLUGS[$index]}"
  label="$(category_label "$slug")"
  description="$(category_description "$slug")"
  hero_image="$(category_hero_image "$slug")"
  hero_alt="$(category_hero_alt "$slug")"
  number="$(printf '%02d' "$(category_order "$slug")")"
  count="$(service_count_for "$slug")"
  out="$CAT_ROOT/$slug.md"
  prev_index=$((index - 1))
  next_index=$((index + 1))

  cat >"$out" <<YAML
---
title: "$(yaml_escape "$label") | Agent-Native Services"
collection_label: "$(yaml_escape "$label")"
description: "$(yaml_escape "$description")"
hero_image: "${hero_image}"
hero_image_alt: "$(yaml_escape "$hero_alt")"
image: "${hero_image}"
permalink: /categories/${slug}/
page_kind: collection
collection_number: "${number}"
service_count: ${count}
---

<p class="collection-source"><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/${slug}/README.md">Collection notes ↗</a></p>

<div class="service-grid">
YAML

  service_visual_index=0
  while IFS=$'\t' read -r _sort_key service_title base; do
    [[ -n "$base" ]] || continue
    service_visual_index=$((service_visual_index + 1))
    service_visual_number="$(printf '%02d' "$(((service_visual_index - 1) % 16 + 1))")"
    if (( ((((service_visual_index - 1) / 16) + index) % 2) == 0 )); then
      service_atlas_sheet="atlas-sheet--service"
    else
      service_atlas_sheet="atlas-sheet--arrival"
    fi
    file="$ROOT/services/$slug/$base"
    repo_url="$(extract_repo_url "$file")"
    signal="$(extract_latest_signal "$file")"
    classification="$(extract_field "$file" "Classification")"
    service_title_html="$(html_escape "$service_title")"
    classification_html="$(html_escape "${classification:-agent-native}")"
    class_name="service-card"
    badge="Curated dossier"
    if [[ -n "$signal" ]]; then
      class_name="service-card service-card--new"
      badge="New · Last 30 days"
    fi
    {
      printf '  <article class="%s %s atlas-visual--%s">\n' "$class_name" "$service_atlas_sheet" "$service_visual_number"
      echo '    <span class="service-card__image" aria-hidden="true"></span>'
      echo '    <div class="service-card__copy">'
      printf '    <div class="service-card__overline"><span>%s</span><span>%s</span></div>\n' "$badge" "$classification_html"
      printf '    <h2 class="service-card__title">%s</h2>\n' "$service_title_html"
      echo '    <div class="service-card__actions">'
      printf '      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/%s/%s">Open dossier ↗</a>\n' "$slug" "$base"
      if [[ -n "$repo_url" ]]; then
        printf '      <a href="%s">Official repo ↗</a>\n' "$repo_url"
      fi
      echo '    </div>'
      echo '    </div>'
      echo '  </article>'
    } >>"$out"
  done < <(
    for file in "$ROOT/services/$slug"/*.md; do
      [[ -f "$file" ]] || continue
      base="$(basename "$file")"
      [[ "$base" == README.md ]] && continue
      service_title="$(sed -n '1{s/^# //;p;q;}' "$file")"
      sort_key="$(printf '%s' "$service_title" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+//g')"
      printf '%s\t%s\t%s\n' "$sort_key" "$service_title" "$base"
    done | sort -t $'\t' -k1,1 -k3,3
  )

  echo '</div>' >>"$out"
  echo '<nav class="collection-pagination" aria-label="Adjacent collections">' >>"$out"
  if (( prev_index >= 0 )); then
    prev_slug="${CATEGORY_SLUGS[$prev_index]}"
    printf '  <a href="{{ '\''/categories/%s/'\'' | relative_url }}"><small>Previous collection</small><strong>← %s</strong></a>\n' "$prev_slug" "$(category_label "$prev_slug")" >>"$out"
  else
    echo '  <a href="{{ '\''/categories/'\'' | relative_url }}"><small>Collection index</small><strong>← All collections</strong></a>' >>"$out"
  fi
  if (( next_index < TOTAL_COLLECTIONS )); then
    next_slug="${CATEGORY_SLUGS[$next_index]}"
    printf '  <a href="{{ '\''/categories/%s/'\'' | relative_url }}"><small>Next collection</small><strong>%s →</strong></a>\n' "$next_slug" "$(category_label "$next_slug")" >>"$out"
  else
    echo '  <a href="{{ '\''/'\'' | relative_url }}#new-arrivals"><small>Return to edition</small><strong>New arrivals →</strong></a>' >>"$out"
  fi
  echo '</nav>' >>"$out"
done

# Branded 1200x630 Open Graph image, cropped from the editorial hero without embedded text.
if command -v ffmpeg >/dev/null 2>&1 && [[ -f "$HERO_IMG" ]]; then
  ffmpeg -y -i "$HERO_IMG" \
    -vf "scale=1200:800:force_original_aspect_ratio=increase,crop=1200:630:(iw-ow)/2:(ih-oh)/2" \
    -frames:v 1 "$IMG" -loglevel error
  echo "Wrote $IMG"
else
  echo "Skipping OG image (ffmpeg or editorial hero missing); keeping existing image." >&2
fi

echo "Wrote $INDEX (${TOTAL_SERVICES} services, ${TOTAL_COLLECTIONS} collections, ${NEW_ARRIVALS} new arrivals)"
echo "Wrote collection pages under $CAT_ROOT"
