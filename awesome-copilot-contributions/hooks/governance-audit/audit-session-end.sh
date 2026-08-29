#!/bin/bash

# Governance Audit: Log session end with summary statistics

set -euo pipefail

if [[ "${SKIP_GOVERNANCE_AUDIT:-}" == "true" ]]; then
  exit 0
fi

INPUT=$(cat)

mkdir -p logs/copilot/governance

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
LOG_FILE="logs/copilot/governance/audit.log"
MARKER_FILE="logs/copilot/governance/.session_marker"

MARKER=0
if [[ -f "$MARKER_FILE" ]]; then
  MARKER=$(cat "$MARKER_FILE" 2>/dev/null || echo 0)
fi

TOTAL=0
THREATS=0
if [[ -f "$LOG_FILE" ]]; then
  TOTAL=$(tail -n +"$((MARKER + 1))" "$LOG_FILE" | grep -c '"event"' || true)
  THREATS=$(tail -n +"$((MARKER + 1))" "$LOG_FILE" | grep -c '"threat_detected"' || true)
fi

jq -c -Rn \
  --arg timestamp "$TIMESTAMP" \
  --argjson total "$TOTAL" \
  --argjson threats "$THREATS" \
  '{"timestamp":$timestamp,"event":"session_end","total_events":$total,"threats_detected":$threats}' \
  >> "$LOG_FILE"

if [[ "$THREATS" -gt 0 ]]; then
  echo "⚠️ Session ended: $THREATS threat(s) detected in $TOTAL events"
else
  echo "✅ Session ended: $TOTAL events, no threats"
fi

exit 0
