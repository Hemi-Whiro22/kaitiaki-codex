#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="${ROOT_DIR}/profiles/devcontainer-local/llama.env.example"
LOGGER="${ROOT_DIR}/scripts/profile-log.sh"
STATE_DIR="${ROOT_DIR}/var/state"

if [[ -f "${ENV_FILE}" ]]; then
  # shellcheck disable=SC1090
  source "${ENV_FILE}"
fi

PROMPT_INPUT="${*:-${TASK:-}}"
if [[ -z "${PROMPT_INPUT}" ]]; then
  echo "Usage: scripts/llama-draft.sh \"Describe the stub you want\"" >&2
  echo "Or: TASK=\"Describe the stub you want\" make llama-draft" >&2
  exit 1
fi

mkdir -p "${STATE_DIR}"

LLAMA_API_PORT="${LLAMA_API_PORT:-8090}"
BASE_URL="http://127.0.0.1:${LLAMA_API_PORT}"
STAMP="$(date +%Y%m%d_%H%M%S)"
REQUEST_FILE="${STATE_DIR}/llama-draft-${STAMP}.request.json"
RESPONSE_FILE="${STATE_DIR}/llama-draft-${STAMP}.response.json"

python3 - <<PY
import json
from pathlib import Path

request_path = Path(${REQUEST_FILE@Q})
payload = {
    "prompt": (
        "You are a local draft helper for Kaitiaki Codex. "
        "Produce a concise implementation stub or recommendation only. "
        "Do not assume authority to change files. "
        "Prefer clear scaffolds, short explanations, and explicit next steps.\n\n"
        "Task:\n"
        + ${PROMPT_INPUT@Q}
        + "\n\nDraft:\n"
    ),
    "temperature": 0.3,
    "n_predict": 700,
    "stream": False,
}
request_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
PY

if [[ -x "${LOGGER}" ]]; then
  "${LOGGER}" "llama_draft" "request path=${REQUEST_FILE} base_url=${BASE_URL}"
fi

curl -fsS \
  -H "Content-Type: application/json" \
  -d @"${REQUEST_FILE}" \
  "${BASE_URL}/completion" > "${RESPONSE_FILE}"

if [[ -x "${LOGGER}" ]]; then
  "${LOGGER}" "llama_draft" "response path=${RESPONSE_FILE} base_url=${BASE_URL}"
fi

echo "Draft response:"
python3 - <<PY
import json
from pathlib import Path
path = Path(${RESPONSE_FILE@Q})
data = json.loads(path.read_text())
content = ""
content = data.get("content") or ""
print(content.strip())
PY

echo
echo "Saved:"
echo "  request:  ${REQUEST_FILE}"
echo "  response: ${RESPONSE_FILE}"
