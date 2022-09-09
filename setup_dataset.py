import argparse
import os
import zipfile

# Run setup-script from within repo (or set absolute paths below and remove
# assertion).
assert os.getcwd().endswith('/dl4de')

# Set paths accordingly if changed from default
DOWNLOAD_LOCATION = './tmp/downloads/'
DATASETS_LOCATION = './datasets/'

DATASET_FILE_NAMES = {
    'semantics': "data_semantics.zip",
    'sceneflow': "data_scene_flow.zip",
}

parser = argparse.ArgumentParser()
parser.add_argument(
    'dataset', help='select dataset', choices=['semantics', 'sceneflow'])
args = parser.parse_args()

file_path = DOWNLOAD_LOCATION + DATASET_FILE_NAMES[args.dataset]
assert os.path.isfile(file_path)

with zipfile.ZipFile(file_path) as archive:
    archive.extractall(path=DATASETS_LOCATION + 'kitti')
