from ...create import *
import os

print("Running create.generic.package")
copy_file_or_folder(
    os.path.sep.join([
        get_source(),
        "project",
        "generic",
        "src",
        "packages",
        "template_package"
    ]),
    "new_package"
)