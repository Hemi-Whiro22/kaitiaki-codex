#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

if [[ ! -x ".venv/bin/uvicorn" ]]; then
  echo "Missing project virtualenv. Run: make bootstrap-project" >&2
  exit 1
fi

PYTHONPATH=. .venv/bin/uvicorn api.main:app --host 0.0.0.0 --port 8093 --reload
