from ...create import *
from .. import src
import os

from ...file_templates import (
    export_readme,
    ReadMeType,
)

print("Running create.mamba.app")
copy_file_or_folder(
    os.path.sep.join([
        src,
        "generic_mamba",
        "app"
    ])
)

export_readme(destination, name=destination_name, template_type=ReadMeType.PythonApp)