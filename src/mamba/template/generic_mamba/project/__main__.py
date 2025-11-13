from ...create import *
from .. import src
import os

sep = os.path.sep

if os.path.exists(destination):
    print(f"Path already exists... NOT PROCEEDING..")
    print(f"    (The path: {destination})")
    exit()

print("Running create.mamba.project")
print(f"    Creating {destination}{sep}{destination_name}...")

copy_file_or_folder(src+sep+"generic_mamba")

from .templates import (
    export_pyproject, PoetryPackageInclusion,
    export_ui,
    export_readme,
)

export_ui(destination_name, destination)
export_pyproject(
    destination,
    name=destination_name,
    packages=[
        PoetryPackageInclusion(
            name="*",
            src="src/packages",
        )
    ]
)
export_readme(destination, name=destination_name)
