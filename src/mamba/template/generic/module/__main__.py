from ...create import *
from .. import src
import os

print("Running create.generic.module")
copy_file_or_folder(
    os.path.sep.join([
        src,
        "src",
        "packages",
        "template_package",
        "my_module.py"
    ]),
    suffix_dest='.py'
)