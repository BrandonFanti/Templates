content="""
[tool.poetry]
name = "{}"
version = "0.0.0"
authors=["{}"]
description="The {} package is too generic and meta for description."

packages = [
    {}
]

[tool.poetry.dependencies]
python = "^3.13,<3.14"
"""

from typing import List

class PoetryPackageInclusion:
    src = None
    dest= None

    def __init__(
        self, 
        name=None,
        src=None,
        dest=None
    ):
        assert name != None
        self.name = name
        self.src = src
        self.dest = dest

    def __str__(self):
        s = '{ '
        s += f"include=\"{self.name}\" "
        if self.src:
            s+= f", from=\"{self.src}\" "
        if self.dest:
            s+= f", to=\"{self.dest}\" "
        s += '},'

        return s


def fmt_pyproject(
    name="my_project", 
    authors="Brandon Fanti: B14CKM4MB4",
    packages=[]
):

    packages_str_list = [str(p) for p in packages]
    packages_str = '\n'.join(packages_str_list)

    return content.format(
        name,
        authors,
        name,
        packages_str
    )


from os import makedirs
from os.path import sep

def export_pyproject(destination, **kwargs):
    try:
        makedirs(destination)
    except:
        pass

    with open(destination+sep+"pyproject.toml", 'w') as fout:
        fout.write(
            fmt_pyproject(**kwargs)
        )
