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
	# Use this instead of reset-conda-env to keep already installed packages.
	@echo Updating conda environment...
	conda env update --file "./environment.yml"

install-pip-tools:
	pip install pip-tools==6.8.0 setuptools==65.3.0

pip-compile:
	pip-compile "./requirements/requirements.in" \
		&& pip-compile "./requirements/dev-requirements.in"

pip-sync:
	pip-sync --python-executable ~/miniconda3/envs/dl4de/bin/python \
		"./requirements/requirements.txt" \
		"./requirements/dev-requirements.txt"

configure-paths:
	# Required for gpu support, see https://www.tensorflow.org/install/pip
	mkdir -p $$CONDA_PREFIX/etc/conda/activate.d
	mkdir -p $$CONDA_PREFIX/etc/conda/deactivate.d
	echo 'export OLD_LD_LIBRARY_PATH=$$LD_LIBRARY_PATH' \
		> $$CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
	echo 'export LD_LIBRARY_PATH=$$OLD_LD_LIBRARY_PATH:$$CONDA_PREFIX/lib' \
		>> $$CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
	echo 'export LD_LIBRARY_PATH=$$OLD_LD_LIBRARY_PATH' \
		> $$CONDA_PREFIX/etc/conda/deactivate.d/env_vars.sh
	@echo Important: reactivate conda environment for changes to take effect!

.PHONY: default \
	build-conda-env \
	update-conda-env \
	install-pip-tools \
	pip-compile \
	pip-sync \
	configure-paths
