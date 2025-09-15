#!/usr/bin/env bash
set -euo pipefail

# Generate one .html per slug (from data/urls.txt) at repo root
BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
URLS_FILE="$BASE_DIR/data/urls.txt"
TEMPLATE="$BASE_DIR/templates/castle-page.html"

if [[ ! -f "$TEMPLATE" ]]; then
  echo "Template not found: $TEMPLATE" >&2
  exit 1
fi

# Read first column (URL) and ignore header
awk 'NR>1{print $1}' "$URLS_FILE" | while read -r url; do
  [[ -z "$url" ]] && continue
  # Remove trailing slash, extract last path segment as slug
  slug="${url%/}"
  slug="${slug##*/}"
  [[ -z "$slug" ]] && continue
  out="$BASE_DIR/${slug}.html"
  if [[ -f "$out" ]]; then
    echo "Skip existing: ${slug}.html"
    continue
  fi
  # Build a simple title from slug
  title="$(printf '%s' "$slug" | sed 's/-/ /g')"
  # Render template
  sed -e "s/{{TITLE}}/${title//\//}/g" -e "s/{{SLUG}}/${slug}/g" "$TEMPLATE" > "$out"
  echo "Created: ${slug}.html"
done

echo "Done."
