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
LLAMA_CLI_BIN="${LLAMA_CLI_BIN:-${LLAMA_SERVER_BIN%/llama-server}/llama-cli}"

echo "Kaitiaki local inference check"
echo "  server_bin: ${LLAMA_SERVER_BIN}"
echo "  cli_bin:    ${LLAMA_CLI_BIN}"
echo "  model:      ${LLAMA_MODEL_PATH}"
echo

if command -v nvidia-smi >/dev/null 2>&1; then
  echo "GPU:"
  nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv,noheader
else
  echo "GPU: nvidia-smi not found"
fi

echo
if command -v nvcc >/dev/null 2>&1; then
  echo "CUDA compiler:"
  nvcc --version | tail -n 2
else
  echo "CUDA compiler: nvcc not found"
fi

echo
if [[ -x "${LLAMA_CLI_BIN}" ]]; then
  echo "llama.cpp CUDA probe:"
  "${LLAMA_CLI_BIN}" --help 2>&1 | grep -m 2 -E "ggml_cuda_init|CUDA devices" || true
else
  echo "llama.cpp probe: ${LLAMA_CLI_BIN} not found or not executable"
fi

echo
if [[ -f "${LLAMA_MODEL_PATH}" ]]; then
  echo "Model file: ok"
else
  echo "Model file: missing"
fi
