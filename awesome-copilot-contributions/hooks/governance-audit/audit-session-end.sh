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

# Count events from this session
TOTAL=0
THREATS=0
if [[ -f "$LOG_FILE" ]]; then
  TOTAL=$(wc -l < "$LOG_FILE" 2>/dev/null || echo 0)
  THREATS=$(grep -c '"threat_detected"' "$LOG_FILE" 2>/dev/null || echo 0)
fi

jq -Rn \
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
