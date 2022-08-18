import os
import zipfile

# Run setup-script from within repo (or set absolute paths below and remove
# assertion).
assert os.getcwd().endswith('/dl4de')

# Set paths accordingly if changed from default
DOWNLOAD_LOCATION = './tmp/downloads/'
DATASETS_LOCATION = './datasets/'
FILENAME = 'data_semantics.zip'

assert os.path.isfile(DOWNLOAD_LOCATION + FILENAME)

with zipfile.ZipFile(DOWNLOAD_LOCATION + FILENAME) as archive:
    # archive.printdir()
    archive.extractall(path=DATASETS_LOCATION + 'kitti')
