#!/usr/bin/env bash
set -euo pipefail

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SNIPPET_FILE="$BASE_DIR/templates/booking-snippet.html"

# Insert into all castle pages: kasteel-*.html, burcht-*.html, chateau-*.html, waterkasteel-*.html
shopt -s nullglob
cd "$BASE_DIR"
for f in kasteel-*.html burcht-*.html chateau-*.html waterkasteel-*.html paleis-*.html; do
  # Skip if snippet already present
  if grep -q 'class="booking-card"' "$f"; then
    echo "Skip (exists): $f"; continue
  fi
  # Insert after the closing tag of .detail-grid inside .detail-header
  awk -v RS= -v ORS='' -v snippet="$(tr '\n' '\r' < "$SNIPPET_FILE")" '
    {
      gsub(/\r/,"\n",snippet);
      pattern = "<div class=\"detail-grid\"";
      start = index($0, pattern);
      if(!start){ print $0; next }
      pre = substr($0, 1, start-1);
      rest = substr($0, start);
      # find the first closing </div> after the pattern
      closepos = match(rest, /\n[ \t]*<\/div>[ \t]*\n/);
      if(closepos){
        before = substr(rest, 1, RSTART+RLENGTH-1);
        after  = substr(rest, RSTART+RLENGTH);
        print pre before snippet after;
      } else {
        print $0;
      }
    }
  ' "$f" > "$f.tmp" && mv "$f.tmp" "$f"
  echo "Updated: $f"
done
echo "Done."
