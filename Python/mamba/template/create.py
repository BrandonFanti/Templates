import site
import shutil
import os
import sys

def copy_file_or_folder(source, destination_name):
    print(f"Copying {source}...")
    destination = None
    if os.path.isdir(source):
        destination = os.path.join(os.getcwd(), destination_name)
        shutil.copytree(source, destination)
    else:
        destination = os.path.join(os.getcwd(), destination_name)
        shutil.copy2(source, destination)
    print(f"Copied {source} to {destination}")

def get_source():
    return \
        site.getsitepackages()[0]+\
        os.path.sep+\
        os.path.sep.join(["mamba", "template", "templates"])

def generic_module():
    copy_file_or_folder((
        get_source(),
        "project",
        "generic",
        "src",
        "packages",
        "template_package",
        "my_module.py"
    ))

