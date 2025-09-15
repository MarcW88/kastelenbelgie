#!/usr/bin/env bash
set -euo pipefail

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$BASE_DIR"
shopt -s nullglob

for f in kasteel-*.html burcht-*.html chateau-*.html waterkasteel-*.html paleis-*.html; do
  if grep -q 'href="#reserveren"' "$f"; then
    echo "Skip (exists): $f"; continue
  fi
  awk -v RS= -v ORS='' '
    {
      text=$0;
      if (text ~ /href="#reserveren"/) { printf "%s", text; next }
      navStart = index(text, "<nav class=\"nav\">");
      if (navStart == 0) { printf "%s", text; next }
      pre = substr(text, 1, navStart-1);
      rest = substr(text, navStart);
      closepos = index(rest, "</nav>");
      if (closepos == 0) { printf "%s", text; next }
      before = substr(rest, 1, closepos-1);
      after  = substr(rest, closepos);
      printf "%s%s        <a href=\"#reserveren\">Reserveren</a>\n      %s", pre, before, after;
    }
  ' "$f" > "$f.tmp" && mv "$f.tmp" "$f" && echo "Updated: $f"
done
echo "Done."
