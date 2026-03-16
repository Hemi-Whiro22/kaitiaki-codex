#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MANIFEST_PATH="${ROOT_DIR}/profiles/devcontainer-local/manifest.yaml"

echo "Kaitiaki Framework 101"
echo "Profile: devcontainer-local"
echo "Root: ${ROOT_DIR}"
echo
echo "Manifest: ${MANIFEST_PATH}"
echo

if [[ ! -f "${MANIFEST_PATH}" ]]; then
  echo "Missing manifest: ${MANIFEST_PATH}" >&2
  exit 1
fi

echo "Profile summary:"
awk '
  /^profile:/ { print "  " $0 }
  /^purpose:/ { in_purpose=1; next }
  in_purpose && /summary:/ { print "  purpose: " substr($0, index($0, ":") + 2); in_purpose=0 }
  /^stability_target:/ { in_stability=1; next }
  in_stability && /current_phase:/ { print "  current_phase: " substr($0, index($0, ":") + 2); in_stability=0 }
' "${MANIFEST_PATH}"

echo
echo "Current profile entry points:"
echo "  - docs/STRUCTURE_GUIDE_CURRENT_CONTRACT.md"
echo "  - docs/QUICK_REFERENCE_CURRENT_CONTRACT.md"
echo "  - docs/how_to_run_CURRENT_CONTRACT.md"
echo
echo "Useful commands:"
echo "  - make profile-show"
echo "  - make profile-check"
echo "  - make check-tree"
echo
echo "Local inference note:"
echo "  MCP can expose a local inference service to clients and tools."
echo "  GPU offload comes from how llama.cpp is built and launched, not from MCP itself."
