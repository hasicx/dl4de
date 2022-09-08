# DL4DE

## Install

1.  Setup conda environment: `$ make build-conda-env`.
2.  Activate conda environment: `$ conda activate dl4de`.
3.  Install pip packages: `$ make install-pip-tools`.
4.  Compile requirements: `$ make pip-compile`.
5.  Sync requirements: `$ make pip-sync`.

## Setup dataset

1.  Create downloads directory in ./tmp: `$ mkdir -p ./tmp/downloads`.
2.  Download dataset (zip file) to `downloads`.
3.  Setup dataset (kitti segmentation): `$ python ./setup_dataset.py`.
    -   TODO: add argument parsing for scene flow dataset
