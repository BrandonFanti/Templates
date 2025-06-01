from ...create import *
import os

print("Running create.generic.project")
copy_file_or_folder(
    os.path.sep.join([
        get_source(),
        "project",
        "generic",
    ]),
    "new_project"
)