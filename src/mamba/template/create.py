import site
import shutil
import os
import sys

destination_name = sys.argv[-1]

def copy_file_or_folder(source, suffix_dest=''):
    print(f"Copying {source}...")
    destination = None
    if os.path.isdir(source):
        destination = os.path.join(os.getcwd(), destination_name+suffix_dest)
        shutil.copytree(source, destination)
    else:
        destination = os.path.join(os.getcwd(), destination_name+suffix_dest)
        shutil.copy2(source, destination)
    print(f"Copied {source} to {destination}")

def get_source():
    return \
        site.getsitepackages()[0]+\
        os.path.sep+\
        os.path.sep.join(["mamba", "template", "templates", "project_type"])


