.PHONY: help bootstrap start-dev profile-show profile-check check-tree llama-check llama-start llama-smoke

help:
	@echo "Available targets:"
	@echo "  make bootstrap   Prepare local scripts"
	@echo "  make start-dev   Start the local profile shell"
	@echo "  make profile-show Show the profile manifest summary"
	@echo "  make profile-check Validate expected profile files"
	@echo "  make llama-check Validate local CUDA/llama.cpp readiness"
	@echo "  make llama-start Start local llama.cpp server"
	@echo "  make llama-smoke Run a local inference smoke test"
	@echo "  make check-tree  Show the profile tree"

bootstrap:
	chmod +x scripts/start-dev.sh scripts/profile-check.sh scripts/llama-check.sh scripts/llama-start.sh scripts/llama-smoke.sh scripts/profile-log.sh

start-dev:
	./scripts/start-dev.sh

profile-show:
	@echo "Profile manifest: profiles/devcontainer-local/manifest.yaml"
	@sed -n '1,220p' profiles/devcontainer-local/manifest.yaml

profile-check:
	./scripts/profile-check.sh

llama-check:
	./scripts/llama-check.sh

llama-start:
	./scripts/llama-start.sh

llama-smoke:
	./scripts/llama-smoke.sh

check-tree:
	find . -maxdepth 2 -mindepth 1 | sort
