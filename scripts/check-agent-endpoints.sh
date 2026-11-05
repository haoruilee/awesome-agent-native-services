#!/usr/bin/env bash
set -euo pipefail

if [[ $# -gt 1 ]]; then
  echo "Usage: $0 [site-base-url]" >&2
  exit 2
fi

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
work_dir="$(mktemp -d)"
trap 'rm -rf "$work_dir"' EXIT

config_site_base="$(
  python3 - "$repo_root/docs/_config.yml" <<'PY'
import re
import sys
from pathlib import Path

text = Path(sys.argv[1]).read_text(encoding="utf-8")
url_match = re.search(r'^url:\s*["\']?([^"\'\n]+)', text, re.MULTILINE)
base_match = re.search(r'^baseurl:\s*["\']?([^"\'\n]*)', text, re.MULTILINE)
if not url_match:
    raise SystemExit(0)
url = url_match.group(1).rstrip("/")
base = (base_match.group(1) if base_match else "").strip().rstrip("/")
if base in {"", '""', "''"}:
    print(url + "/")
else:
    if not base.startswith("/"):
        base = "/" + base
    print(url + base + "/")
PY
)"

if [[ $# -eq 1 ]]; then
  arg_base="${1%/}/"
  if [[ -n "$config_site_base" && "$arg_base" != "$config_site_base" ]]; then
    echo "Note: using docs/_config.yml site URL ($config_site_base) instead of argument ($arg_base)" >&2
    site_base="${config_site_base%/}"
  else
    site_base="${1%/}"
  fi
elif [[ -n "$config_site_base" ]]; then
  site_base="${config_site_base%/}"
else
  echo "Usage: $0 <site-base-url>" >&2
  exit 2
fi

site_origin="$(python3 - "$site_base" <<'PY'
import sys
from urllib.parse import urlsplit

parsed = urlsplit(sys.argv[1])
if parsed.scheme not in {"http", "https"} or not parsed.netloc:
    raise SystemExit(f"invalid site URL: {sys.argv[1]}")
print(f"{parsed.scheme.lower()}://{parsed.netloc.lower()}")
PY
)"

fetch() {
  local endpoint="$1"
  local output_name="$2"
  local expected_content_type="$3"
  local url="$site_base${endpoint:+/$endpoint}"
  local metadata

  if ! metadata="$(
    curl --silent --show-error --location --fail-with-body \
      --retry 6 --retry-all-errors --retry-delay 3 --retry-max-time 150 \
      --connect-timeout 10 --max-time 30 \
      --output "$work_dir/$output_name" \
      --write-out $'%{http_code}\n%{content_type}\n%{url_effective}' \
      "$url"
  )"; then
    echo "::error::Unable to fetch $url" >&2
    return 1
  fi

  local status content_type effective_url effective_origin
  status="$(sed -n '1p' <<<"$metadata")"
  content_type="$(sed -n '2p' <<<"$metadata")"
  effective_url="$(sed -n '3p' <<<"$metadata")"
  effective_origin="$(python3 - "$effective_url" <<'PY'
import sys
from urllib.parse import urlsplit

parsed = urlsplit(sys.argv[1])
print(f"{parsed.scheme.lower()}://{parsed.netloc.lower()}")
PY
)"

  if [[ "$status" != "200" ]]; then
    echo "::error::$url returned HTTP $status" >&2
    return 1
  fi
  if [[ "$effective_origin" != "$site_origin" ]]; then
    echo "::error::$url redirected off-origin to $effective_url" >&2
    return 1
  fi
  if [[ ! -s "$work_dir/$output_name" ]]; then
    echo "::error::$url returned an empty body" >&2
    return 1
  fi
  if [[ ! "$content_type" =~ $expected_content_type ]]; then
    echo "::error::$url returned unexpected content type: ${content_type:-none}" >&2
    return 1
  fi

  printf 'OK  %-20s %s\n' "/${endpoint}" "${content_type:-unknown content type}"
}

fetch "" homepage.html '^text/html([;]|$)'
fetch "llms.txt" llms.txt '^text/plain([;]|$)'
fetch "skill.md" skill.md '^text/(markdown|plain)([;]|$)'
fetch "catalog.json" catalog.json '^application/json([;]|$)'
fetch "catalog.schema.json" catalog.schema.json '^application/json([;]|$)'
fetch "robots.txt" robots.txt '^text/plain([;]|$)'
fetch "sitemap.xml" sitemap.xml '^(application|text)/xml([;]|$)'

grep -Eiq '<!doctype html|<html' "$work_dir/homepage.html"
grep -Eq '^# +Awesome Agent-Native Services' "$work_dir/llms.txt"
grep -Eq '^# +(Find|Awesome|Agent)' "$work_dir/skill.md"
grep -Eiq 'agent' "$work_dir/skill.md"
grep -Eiq '^sitemap:' "$work_dir/robots.txt"

for endpoint in llms.txt skill.md catalog.json catalog.schema.json; do
  if ! grep -Fq "/$endpoint" "$work_dir/homepage.html"; then
    echo "::error::Homepage does not advertise /$endpoint." >&2
    exit 1
  fi
  if ! cmp -s "$work_dir/$endpoint" "$repo_root/docs/$endpoint"; then
    echo "::error::Deployed $endpoint does not match the checked-out release." >&2
    exit 1
  fi
done

if grep -Eiq '<!doctype html|<html' \
  "$work_dir/llms.txt" \
  "$work_dir/skill.md" \
  "$work_dir/catalog.json" \
  "$work_dir/catalog.schema.json"; then
  echo "::error::A machine-readable endpoint returned HTML." >&2
  exit 1
fi

python3 - \
  "$work_dir/catalog.json" \
  "$work_dir/catalog.schema.json" \
  "$work_dir/sitemap.xml" <<'PY'
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

catalog_path, schema_path, sitemap_path = map(Path, sys.argv[1:])
catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
schema = json.loads(schema_path.read_text(encoding="utf-8"))
if not isinstance(catalog, dict) or not catalog:
    raise SystemExit("catalog.json must be a non-empty JSON object")
if not isinstance(schema, dict) or not schema:
    raise SystemExit("catalog.schema.json must be a non-empty JSON object")
if catalog.get("$schema") != schema.get("$id"):
    raise SystemExit("catalog.json does not identify the deployed schema")
if catalog.get("counts") != {
    "categories": len(catalog.get("categories", [])),
    "services": len(catalog.get("services", [])),
}:
    raise SystemExit("catalog.json counts do not match its records")
ET.parse(sitemap_path)
PY

echo "Public agent endpoint smoke test passed for $site_base"
