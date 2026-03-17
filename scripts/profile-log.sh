#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_DIR="${ROOT_DIR}/var/log"
STATE_DIR="${ROOT_DIR}/var/state"
LOG_FILE="${LOG_DIR}/profile-events.log"
STATE_FILE="${STATE_DIR}/profile-events.jsonl"

mkdir -p "${LOG_DIR}" "${STATE_DIR}"

EVENT_NAME="${1:-event}"
shift || true
DETAILS="${*:-}"
STAMP="$(date -Iseconds)"

printf '%s [%s] %s\n' "${STAMP}" "${EVENT_NAME}" "${DETAILS}" >> "${LOG_FILE}"
printf '{"timestamp":"%s","event":"%s","details":"%s"}\n' \
  "${STAMP}" \
  "${EVENT_NAME}" \
  "$(printf '%s' "${DETAILS}" | sed 's/\\/\\\\/g; s/"/\\"/g')" >> "${STATE_FILE}"
