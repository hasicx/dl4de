default:
	@echo Missing argument.
	@echo Use reset-conda-env or update-conda-env to create and update conda environment.

reset-conda-env:
	# Reset conda environment according to `environment.yml`.
	# Note: reset -> prune existing packages
	@echo Resetting conda environemt (with prune)...
	conda env update --file "./environment.yml" --prune

update-conda-env:
	# Update conda environment according to `environment.yml`.
	# Use this instead of reset-conda-env to keep existing packages.
	@echo Updating conda environment...
	conda env update --file "./environment.yml"

.PHONY: default reset-conda-env update-conda-env
