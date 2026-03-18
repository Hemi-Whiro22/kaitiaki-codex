#!/usr/bin/env bash
set -eu

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-}"

if [ -z "$TARGET" ]; then
  echo "usage: scripts/project-recall.sh <project-name-or-path>" >&2
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

echo "== Project =="
echo "$PROJECT_DIR"
echo

show_file() {
  local path="$1"
  local lines="${2:-160}"
  if [ -f "$path" ]; then
    echo "== ${path#$ROOT/} =="
    sed -n "1,${lines}p" "$path"
    echo
  fi
}

show_file "$ROOT/AGENTS.md" 200
show_file "$PROJECT_DIR/AGENTS.md" 200
show_file "$PROJECT_DIR/manifest.yaml" 220
show_file "$PROJECT_DIR/TODO_AUTONOMOUS.md" 260
show_file "$PROJECT_DIR/README.md" 220
