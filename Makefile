.PHONY: help bootstrap start-dev profile-show profile-check check-tree llama-check llama-start llama-smoke llama-log llama-draft mcp-show project-recall phase-check verify-all

help:
	@echo "Available targets:"
	@echo "  make bootstrap   Prepare local scripts"
	@echo "  make start-dev   Start the local profile shell"
	@echo "  make profile-show Show the profile manifest summary"
	@echo "  make profile-check Validate expected profile files"
	@echo "  make llama-check Validate local CUDA/llama.cpp readiness"
	@echo "  make llama-start Start local llama.cpp server"
	@echo "  make llama-smoke Run a local inference smoke test"
	@echo "  make llama-log   Tail the local llama server log"
	@echo "  make llama-draft TASK='...'  Ask the local model for a draft stub"
	@echo "  make mcp-show    Show the MCP profile example"
	@echo "  make project-recall PROJECT='...'  Show the active contract surface for a project"
	@echo "  make phase-check PROJECT='...'     Check contract and phase anchors for a project"
	@echo "  make verify-all [TARGET='projects|project-name|/abs/path']  Run known test entrypoints"
	@echo "  make check-tree  Show the profile tree"

bootstrap:
	chmod +x scripts/start-dev.sh scripts/profile-check.sh scripts/llama-check.sh scripts/llama-start.sh scripts/llama-smoke.sh scripts/llama-draft.sh scripts/profile-log.sh scripts/project-recall.sh scripts/phase-check.sh scripts/verify-all.sh

start-dev:
	bash ./scripts/start-dev.sh

profile-show:
	@echo "Profile manifest: profiles/devcontainer-local/manifest.yaml"
	@sed -n '1,220p' profiles/devcontainer-local/manifest.yaml

profile-check:
	bash ./scripts/profile-check.sh

llama-check:
	bash ./scripts/llama-check.sh

llama-start:
	bash ./scripts/llama-start.sh

llama-smoke:
	bash ./scripts/llama-smoke.sh

llama-log:
	@tail -n 50 -f var/log/llama-server.log

llama-draft:
	bash ./scripts/llama-draft.sh "$(TASK)"

mcp-show:
	@echo "MCP profile: profiles/devcontainer-local/mcp.yaml"
	@sed -n '1,220p' profiles/devcontainer-local/mcp.yaml

project-recall:
	bash ./scripts/project-recall.sh "$(PROJECT)"

phase-check:
	bash ./scripts/phase-check.sh "$(PROJECT)"

verify-all:
	bash ./scripts/verify-all.sh "$(TARGET)"

check-tree:
	find . -maxdepth 2 -mindepth 1 | sort
