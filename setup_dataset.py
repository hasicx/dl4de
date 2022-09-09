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

DATASET_SUBSETS = [
    'image_2', 'instance', 'semantic',
    'image_3', 'disp_occ_0', 'disp_noc_0',
]

parser = argparse.ArgumentParser()
parser.add_argument(
    'dataset', help='select dataset', choices=['semantics', 'sceneflow'])
args = parser.parse_args()

file_path = DOWNLOAD_LOCATION + DATASET_FILE_NAMES[args.dataset]
assert os.path.isfile(file_path)

with zipfile.ZipFile(file_path) as archive:
    for filename in archive.namelist():
        category = filename.split('/')[1]
        if category in DATASET_SUBSETS and filename.endswith('10.png'):
            archive.extract(filename, DATASETS_LOCATION + 'kitti')
