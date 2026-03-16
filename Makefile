.PHONY: help start-dev bootstrap check-tree

help:
	@echo "Available targets:"
	@echo "  make bootstrap   Prepare local scripts"
	@echo "  make start-dev   Start the local profile shell"
	@echo "  make check-tree  Show the profile tree"

bootstrap:
	chmod +x scripts/start-dev.sh

start-dev:
	./scripts/start-dev.sh

check-tree:
	find . -maxdepth 2 -mindepth 1 | sort
