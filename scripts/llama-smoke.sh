#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="${ROOT_DIR}/profiles/devcontainer-local/llama.env.example"
LOGGER="${ROOT_DIR}/scripts/profile-log.sh"

if [[ -f "${ENV_FILE}" ]]; then
  # shellcheck disable=SC1090
  source "${ENV_FILE}"
fi

LLAMA_API_HOST="${LLAMA_API_HOST:-127.0.0.1}"
LLAMA_API_PORT="${LLAMA_API_PORT:-8090}"
BASE_URL="http://127.0.0.1:${LLAMA_API_PORT}"

echo "Kaitiaki llama smoke test"
echo "  base_url: ${BASE_URL}"
echo

if curl -fsS "${BASE_URL}/health" >/tmp/kaitiaki_llama_health.json 2>/dev/null; then
  echo "health: ok"
  [[ -x "${LOGGER}" ]] && "${LOGGER}" "llama_smoke" "health_ok base_url=${BASE_URL}"
else
  echo "health: failed" >&2
  [[ -x "${LOGGER}" ]] && "${LOGGER}" "llama_smoke" "health_failed base_url=${BASE_URL}"
  exit 1
fi

if curl -fsS "${BASE_URL}/v1/models" >/tmp/kaitiaki_llama_models.json 2>/dev/null; then
  echo "models: ok"
  [[ -x "${LOGGER}" ]] && "${LOGGER}" "llama_smoke" "models_ok base_url=${BASE_URL}"
else
  echo "models: failed" >&2
  [[ -x "${LOGGER}" ]] && "${LOGGER}" "llama_smoke" "models_failed base_url=${BASE_URL}"
  exit 1
fi

echo
echo "Smoke test passed."
