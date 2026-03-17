.PHONY: help bootstrap-project install run-api run-mcp test show-manifest

help:
	@echo "Available targets:"
	@echo "  make bootstrap-project Create local .venv and install dependencies"
	@echo "  make install      Install project dependencies"
	@echo "  make run-api      Start the local API"
	@echo "  make run-mcp      Start the local MCP surface"
	@echo "  make test         Run project tests"
	@echo "  make show-manifest Show project manifest"

bootstrap-project:
	bash scripts/bootstrap-project.sh

install:
	.venv/bin/python -m pip install -r requirements.txt

run-api:
	bash scripts/start-api.sh

run-mcp:
	bash scripts/start-mcp.sh

test:
	PYTHONPATH=. .venv/bin/pytest -q

show-manifest:
	@sed -n '1,220p' manifest.yaml
