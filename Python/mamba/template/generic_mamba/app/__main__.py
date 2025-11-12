from ...create import *
from .. import src
import os

print("Running create.mamba.app")
copy_file_or_folder(
    os.path.sep.join([
        src,
        "generic_mamba",
        "app"
    ])
)