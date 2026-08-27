#!/bin/bash

# Governance Audit: Log session start with governance context

set -euo pipefail

if [[ "${SKIP_GOVERNANCE_AUDIT:-}" == "true" ]]; then
  exit 0
fi

INPUT=$(cat)

mkdir -p logs/copilot/governance

LOG_FILE="logs/copilot/governance/audit.log"
MARKER_FILE="logs/copilot/governance/.session_marker"
...
# Record the line count BEFORE this session's own event is appended, so
# audit-session-end.sh can compute stats scoped to only this session
# instead of the whole (cumulative, multi-session) log file.
if [[ -f "$LOG_FILE" ]]; then
  wc -l < "$LOG_FILE" > "$MARKER_FILE"
else
  echo 0 > "$MARKER_FILE"
fi

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
CWD=$(pwd)
LEVEL="${GOVERNANCE_LEVEL:-standard}"

jq -Rn \
  --arg timestamp "$TIMESTAMP" \
  --arg cwd "$CWD" \
  --arg level "$LEVEL" \
  '{"timestamp":$timestamp,"event":"session_start","governance_level":$level,"cwd":$cwd}' \
  >> logs/copilot/governance/audit.log

echo "🛡️ Governance audit active (level: $LEVEL)"
exit 0
