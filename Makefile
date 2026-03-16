.PHONY: help bootstrap start-dev profile-show profile-check check-tree

help:
	@echo "Available targets:"
	@echo "  make bootstrap   Prepare local scripts"
	@echo "  make start-dev   Start the local profile shell"
	@echo "  make profile-show Show the profile manifest summary"
	@echo "  make profile-check Validate expected profile files"
	@echo "  make check-tree  Show the profile tree"

bootstrap:
	chmod +x scripts/start-dev.sh scripts/profile-check.sh

start-dev:
	./scripts/start-dev.sh

profile-show:
	@echo "Profile manifest: profiles/devcontainer-local/manifest.yaml"
	@sed -n '1,220p' profiles/devcontainer-local/manifest.yaml

profile-check:
	./scripts/profile-check.sh

check-tree:
	find . -maxdepth 2 -mindepth 1 | sort
