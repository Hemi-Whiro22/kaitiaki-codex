#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

required_paths=(
  "${ROOT_DIR}/docs/STRUCTURE_GUIDE_CURRENT_CONTRACT.md"
  "${ROOT_DIR}/docs/QUICK_REFERENCE_CURRENT_CONTRACT.md"
  "${ROOT_DIR}/docs/how_to_run_CURRENT_CONTRACT.md"
  "${ROOT_DIR}/profiles/devcontainer-local/manifest.yaml"
  "${ROOT_DIR}/profiles/devcontainer-local/mcp.example.yaml"
  "${ROOT_DIR}/.devcontainer/devcontainer.json"
  "${ROOT_DIR}/.devcontainer/Dockerfile"
  "${ROOT_DIR}/scripts/start-dev.sh"
  "${ROOT_DIR}/Makefile"
)

missing=0

for path in "${required_paths[@]}"; do
  if [[ -e "${path}" ]]; then
    echo "ok: ${path}"
  else
    echo "missing: ${path}" >&2
    missing=1
  fi
done

if [[ ${missing} -ne 0 ]]; then
  echo
  echo "Profile check failed." >&2
  exit 1
fi

echo
echo "Profile check passed."
