#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

if [[ ! -x ".venv/bin/python" ]]; then
  echo "Missing project virtualenv. Run: make bootstrap-project" >&2
  exit 1
fi

export PYTHONPATH=.
.venv/bin/python api/mcp_server.py
