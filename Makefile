default:
	@echo Missing argument.
	@echo Use build-conda-env or update-conda-env to \
		create and reset/update conda environment.

build-conda-env:
	# Reset/build conda environment according to `environment.yml`.
	# Note: reset -> prune existing packages.
	@echo "Building conda environemt (with prune)..."
	conda env update -f "./environment.yml" --prune

update-conda-env:
	# Update/build conda environment according to `environment.yml`.
	# Use this instead of reset-conda-env to already installed packages.
	@echo Updating conda environment...
	conda env update --file "./environment.yml"

install-pip-tools:
	pip install pip-tools==6.8.0 setuptools==65.0.2

pip-compile:
	pip-compile ./requirements/requirements.in

pip-sync:
	pip-sync ./requirements/requirements.txt

.PHONY: default \
	build-conda-env \
	update-conda-env \
	install-pip-tools \
	pip-compile \
	pip-sync
