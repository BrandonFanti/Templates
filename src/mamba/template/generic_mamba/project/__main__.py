from ...create import *
from .. import src

from os import path, chdir, getcwd
sep = path.sep
from shutil import which

from subprocess import Popen, PIPE
import shlex
from time import sleep

if path.exists(destination):
    print(f"Path already exists... NOT PROCEEDING..")
    print(f"    (The path: {destination})")
    exit()

print("Running create.mamba.project")
print(f"    Creating {destination}{sep}{destination_name}...")

copy_file_or_folder(src+sep+"generic_mamba")

from ...file_templates import (
    export_pyproject, PoetryPackageInclusion,
    export_ui,
    export_readme,
)

readme_list = export_readme(destination, name=destination_name)

export_ui(destination_name, destination)
export_pyproject(
    destination,
    name=destination_name,
    readme_paths=readme_list,
    packages=[
        PoetryPackageInclusion(
            name="*",
            src="src/packages",
        )
    ],
    extras='mamba = {git = "https://github.com/BrandonFanti/pytemplates"}'
)

ide = which('codium')
ide = which('code') if not ide else ide

python = which('python')

chdir(destination_name)

def run_process(cmd):
    # print(f'$ {cmd}')
    # print(shlex.split(cmd))
    p = Popen(
        shlex.split(cmd),
        stderr=PIPE,
        stdout=PIPE,
        text=True
    )
    while p.poll() == None:
        try:
            err,out = p.communicate(timeout=0.25)
        except: continue
        if err: print(err)
        if out: print(out)
        sleep(0.25)

print(f"Creating {getcwd()+sep}.venv")
run_process(f"{python} -m venv .venv")

print(f"Running setup for {getcwd()+sep}.venv")
run_process(f".venv/bin/python -m pip install poetry poetry-plugin-bundle")

#Why not just poetry install? 
# site packages `.pth` does not work on *my* systems 
#   (honestly, don't know why, I've no memory of disabling/configuring it as such),
#   regardless, it is (likely?) to die soon and I am regretless-
# https://bugs.python.org/issue33944
# https://dfir.ch/posts/publish_python_pth_extension/

print(f"MORE setup for {getcwd()+sep}.venv ...")
run_process(f".venv/bin/poetry install")
run_process(f".venv/bin/poetry bundle venv .venv")

Popen(shlex.split(f"{ide} ."))
