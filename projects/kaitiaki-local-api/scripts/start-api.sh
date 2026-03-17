#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."
uvicorn api.main:app --host 0.0.0.0 --port 8093 --reload
