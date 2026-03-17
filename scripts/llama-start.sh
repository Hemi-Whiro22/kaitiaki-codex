#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="${ROOT_DIR}/profiles/devcontainer-local/llama.env.example"

if [[ -f "${ENV_FILE}" ]]; then
  # shellcheck disable=SC1090
  source "${ENV_FILE}"
fi

LLAMA_SERVER_BIN="${LLAMA_SERVER_BIN:-$HOME/llama.cpp/build/bin/llama-server}"
LLAMA_MODEL_PATH="${LLAMA_MODEL_PATH:-$HOME/models/Qwen3.5-9B-Uncensored-Q8_0.gguf}"
LLAMA_API_HOST="${LLAMA_API_HOST:-0.0.0.0}"
LLAMA_API_PORT="${LLAMA_API_PORT:-8090}"
LLAMA_ARG_CTX_SIZE="${LLAMA_ARG_CTX_SIZE:-8192}"
LLAMA_ARG_BATCH="${LLAMA_ARG_BATCH:-512}"
LLAMA_ARG_THREADS="${LLAMA_ARG_THREADS:-8}"
LLAMA_ARG_N_GPU_LAYERS="${LLAMA_ARG_N_GPU_LAYERS:-99}"
LLAMA_ARG_MAIN_GPU="${LLAMA_ARG_MAIN_GPU:-0}"
LLAMA_ARG_CACHE_TYPE_K="${LLAMA_ARG_CACHE_TYPE_K:-f16}"
LLAMA_ARG_CACHE_TYPE_V="${LLAMA_ARG_CACHE_TYPE_V:-f16}"
LLAMA_ARG_TEMP="${LLAMA_ARG_TEMP:-0.8}"
LLAMA_ARG_TOP_P="${LLAMA_ARG_TOP_P:-0.95}"

if [[ ! -x "${LLAMA_SERVER_BIN}" ]]; then
  echo "Missing llama-server binary: ${LLAMA_SERVER_BIN}" >&2
  exit 1
fi

if [[ ! -f "${LLAMA_MODEL_PATH}" ]]; then
  echo "Missing model file: ${LLAMA_MODEL_PATH}" >&2
  exit 1
fi

echo "Starting llama.cpp server"
echo "  binary: ${LLAMA_SERVER_BIN}"
echo "  model:  ${LLAMA_MODEL_PATH}"
echo "  host:   ${LLAMA_API_HOST}"
echo "  port:   ${LLAMA_API_PORT}"
echo "  ngl:    ${LLAMA_ARG_N_GPU_LAYERS}"
echo

exec "${LLAMA_SERVER_BIN}" \
  -m "${LLAMA_MODEL_PATH}" \
  --host "${LLAMA_API_HOST}" \
  --port "${LLAMA_API_PORT}" \
  -c "${LLAMA_ARG_CTX_SIZE}" \
  --temp "${LLAMA_ARG_TEMP}" \
  --top_p "${LLAMA_ARG_TOP_P}" \
  -ngl "${LLAMA_ARG_N_GPU_LAYERS}" \
  --main-gpu "${LLAMA_ARG_MAIN_GPU}" \
  --cache-type-k "${LLAMA_ARG_CACHE_TYPE_K}" \
  --cache-type-v "${LLAMA_ARG_CACHE_TYPE_V}" \
  -b "${LLAMA_ARG_BATCH}" \
  --threads "${LLAMA_ARG_THREADS}"
