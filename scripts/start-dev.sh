#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Kaitiaki Framework 101"
echo "Profile: devcontainer-local"
echo "Root: ${ROOT_DIR}"
echo
echo "This script currently provides a profile entry point only."
echo "Next steps in this branch:"
echo "- refine the dev container"
echo "- add concrete runtime/profile examples"
echo "- wire local services against the docs contract"
