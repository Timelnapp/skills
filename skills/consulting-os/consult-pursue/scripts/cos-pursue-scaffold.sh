#!/usr/bin/env bash
# Scaffold a cold-start pursue folder (structure only — agent fills content via /cos-pursue).
#
# Usage:
#   ./scripts/cos-pursue-scaffold.sh "Vodafone Portugal" "agentic customer support"
#   ./scripts/cos-pursue-scaffold.sh "Acme Corp" "data platform" acme-corp
#
# All artifacts live in prospects/{slug}/ — single folder, no Output/ nesting.
# Does NOT run research or write pursuit copy — run /cos-pursue in Cursor for that.

set -euo pipefail
SKILL_ROOT="$(cd "$(dirname "$0")/.." && pwd)"      # consult-pursue/
CATEGORY_ROOT="$(cd "$SKILL_ROOT/.." && pwd)"        # consulting-os/
ROOT="${COS_PROSPECTS_ROOT:-$PWD}"                   # where prospects/{slug}/ is written
CLIENT="${1:-}"
TOPIC="${2:-}"
SLUG="${3:-}"

if [[ -z "$CLIENT" || -z "$TOPIC" ]]; then
  echo "Usage: $0 \"Client Name\" \"engagement topic\" [slug]"
  echo "Example: $0 \"Vodafone Portugal\" \"agentic customer support\" vodafone-portugal"
  exit 1
fi

if [[ -z "$SLUG" ]]; then
  SLUG="$(echo "$CLIENT" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-|-$//g')"
fi

# Pack filename from slug (vodafone-portugal → Vodafone-Portugal-Engagement-Proposal-Pack.md)
PACK_BASENAME="$(echo "$SLUG" | awk -F- '{for (i=1; i<=NF; i++) $i=toupper(substr($i,1,1)) substr($i,2)} 1' OFS=-)-Engagement-Proposal-Pack.md"
PROSPECT="$ROOT/prospects/$SLUG"
PROSPECT_TEMPLATE="$CATEGORY_ROOT/consult-pipeline/prospect-template"
COLD="$SKILL_ROOT/cold-start"
DATE="$(date +%Y-%m-%d)"

if [[ -f "$PROSPECT/engagement-passport.yaml" && -f "$PROSPECT/pursue/email.md" ]]; then
  echo "Prospect folder already exists: $PROSPECT"
  echo "Run /cos-pursue $SLUG (or client + topic) to refresh artifacts."
  exit 0
fi

mkdir -p "$PROSPECT/Input" "$PROSPECT/pursue"

if [[ ! -f "$PROSPECT/engagement-passport.yaml" ]]; then
  cp "$PROSPECT_TEMPLATE/engagement-passport.yaml" "$PROSPECT/engagement-passport.yaml"
fi

cat > "$PROSPECT/Input/README.md" <<EOF
# Input

No client brief, transcript, or RFP on file.

Topic: **$TOPIC**

When added, drop files here. All other artifacts are in the parent folder (\`prospects/$SLUG/\`).
EOF

sed -e "s/{Client}/$CLIENT/g" \
    -e "s/{client}/$CLIENT/g" \
    -e "s/{topic}/$TOPIC/g" \
    -e "s/{YYYY-MM-DD}/$DATE/g" \
    "$COLD/00-research-public.md" > "$PROSPECT/00-research-public.md"

sed -e "s/{Client}/$CLIENT/g" \
    -e "s/{client}/$CLIENT/g" \
    -e "s/{topic}/$TOPIC/g" \
    -e "s/{YYYY-MM-DD}/$DATE/g" \
    "$COLD/proposal-pack-synthesized.md" > "$PROSPECT/$PACK_BASENAME"

cp "$COLD/pursue/email.md" "$PROSPECT/pursue/email.md"
cp "$COLD/pursue/call-script.md" "$PROSPECT/pursue/call-script.md"

PASSPORT="$PROSPECT/engagement-passport.yaml"
{
  echo "# Engagement passport — $CLIENT"
  echo "# Cold-start — all artifacts in prospects/$SLUG/"
  echo "# Scaffold $DATE — run /cos-pursue to populate"
  echo ""
  echo "client: $CLIENT"
  echo "slug: $SLUG"
  echo "stage: PURSUE"
  echo "option_selected: POC"
  echo "source_mode: cold_start"
  echo "revision_loop: 0"
  echo ""
  echo "artifacts:"
  echo "  input_dir: Input/"
  echo "  research: 00-research-public.md"
  echo "  pack: $PACK_BASENAME"
  echo "  pursue_email: pursue/email.md"
  echo "  pursue_script: pursue/call-script.md"
  echo ""
  echo "checkpoints:"
  echo "  pursuit_approved: null"
  echo "  frame_approved: null"
  echo "  option_picked: null"
  echo "  ship_approved: null"
  echo "  sent_to_client: null"
  echo ""
  echo "timeln_pulls: []"
} > "$PASSPORT"

echo "Created cold-start scaffold: $PROSPECT"
echo "  Client: $CLIENT"
echo "  Topic:  $TOPIC"
echo "  Slug:   $SLUG"
echo ""
echo "Layout (single folder):"
echo "  prospects/$SLUG/"
echo "    engagement-passport.yaml"
echo "    00-research-public.md"
echo "    $PACK_BASENAME"
echo "    pursue/email.md"
echo "    pursue/call-script.md"
echo "    Input/"
echo ""
echo "Next: run in Cursor →  /cos-pursue $CLIENT for $TOPIC"
