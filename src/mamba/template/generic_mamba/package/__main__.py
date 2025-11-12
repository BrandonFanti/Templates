from ...create import *
from .. import src
import os

print("Running create.mamba.package")
copy_file_or_folder(
    os.path.sep.join([
        src,
        "src",
        "packages",
        "template_package"
    ])
)