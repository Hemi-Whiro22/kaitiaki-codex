#!/usr/bin/env bash
set -eu

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-}"

if [ -z "$TARGET" ]; then
  echo "usage: scripts/phase-check.sh <project-name-or-path>" >&2
  exit 1
fi

if [ -d "$TARGET" ]; then
  PROJECT_DIR="$(cd "$TARGET" && pwd)"
elif [ -d "$ROOT/projects/$TARGET" ]; then
  PROJECT_DIR="$ROOT/projects/$TARGET"
else
  echo "project not found: $TARGET" >&2
  exit 1
fi

echo "== Phase Check =="
echo "project: $PROJECT_DIR"
echo

check_file() {
  local label="$1"
  local path="$2"
  if [ -f "$path" ]; then
    echo "[ok] $label: ${path#$ROOT/}"
  else
    echo "[missing] $label: ${path#$ROOT/}"
  fi
}

check_file "repo agents" "$ROOT/AGENTS.md"
check_file "project manifest" "$PROJECT_DIR/manifest.yaml"
check_file "project todo" "$PROJECT_DIR/TODO_AUTONOMOUS.md"
check_file "project readme" "$PROJECT_DIR/README.md"

echo
if [ -f "$PROJECT_DIR/TODO_AUTONOMOUS.md" ]; then
  echo "== Phase Anchors =="
  rg -n "^## Phase|^Status:|^## Immediate Next Work" "$PROJECT_DIR/TODO_AUTONOMOUS.md" || true
  echo
fi

if [ -f "$PROJECT_DIR/manifest.yaml" ]; then
  echo "== Boundary Hints =="
  rg -n "http|standalone|local-first|single external door|only in and out|API" "$PROJECT_DIR/manifest.yaml" || true
  echo
fi

echo "== Recommendation =="
echo "1. read manifest"
echo "2. read current phase section"
echo "3. run relevant tests after change"
