import site
import shutil
import os
import sys

def copy_file_or_folder(source):
    destination = None
    if os.path.isdir(source):
        destination = os.path.join(os.getcwd(), os.path.basename(source))
        shutil.copytree(source, destination)
    else:
        destination = os.path.join(os.getcwd(), os.path.basename(source))
        shutil.copy2(source, destination)
    print(f"Copied {source} to {destination}")

def get_source():
    return (
        site.getsitepackages()[0],
        os.path.sep,
        os.path.sep.join( ("mamba", "template", "templates")),
    )

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

def generic_package():
    copy_file_or_folder((
        get_source(),
        "project",
        "generic",
        "src",
        "packages",
        "template_package"
    ))

def generic_project():
    copy_file_or_folder((
        get_source(),
        "project",
        "generic",
    ))

