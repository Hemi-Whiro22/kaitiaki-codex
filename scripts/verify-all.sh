#!/usr/bin/env bash
set -eu

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-projects}"

resolve_project_dir() {
  local target="$1"
  if [ "$target" = "projects" ]; then
    printf '%s\n' "$ROOT/projects"
    return
  fi
  if [ -d "$target" ]; then
    cd "$target" && pwd
    return
  fi
  if [ -d "$ROOT/projects/$target" ]; then
    cd "$ROOT/projects/$target" && pwd
    return
  fi
  return 1
}

TARGET_DIR="$(resolve_project_dir "$TARGET")" || {
  echo "target not found: $TARGET" >&2
  exit 1
}

run_project_tests() {
  local dir="$1"
  local name
  name="$(basename "$dir")"
  echo "== Verifying $name =="

  if [ -x "$dir/.venv/bin/python" ] && [ -d "$dir/tests" ]; then
    (
      cd "$dir"
      ./.venv/bin/python -m pytest -q
    )
    echo
    return
  fi

  if [ -f "$dir/Makefile" ] && grep -q "^test:" "$dir/Makefile"; then
    (
      cd "$dir"
      make test
    )
    echo
    return
  fi

  echo "no known test entrypoint for $name"
  echo
}

if [ "$TARGET_DIR" = "$ROOT/projects" ]; then
  for project_dir in "$ROOT"/projects/*; do
    [ -d "$project_dir" ] || continue
    run_project_tests "$project_dir"
  done
else
  run_project_tests "$TARGET_DIR"
fi
