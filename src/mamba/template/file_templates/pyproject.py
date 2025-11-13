from .format_strings import PoetryFormatStrings

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

class PoetryScript:
    def __init__(
        self, 
        name=None,
        entry_point=None
    ):
        assert name != None
        assert entry_point != None
        self.name = name
        self.entry_point = entry_point

    def __str__(self):
        return f""

def fmt_pyproject(
    name="my_project", 
    authors="Brandon Fanti: B14CKM4MB4",
    readme_paths=[],
    packages=[],
    gui_scripts=[],
    cli_scripts=[],
):

    reformat_type_lists = lambda packs: '\n'.join([str(p) for p in packs])

    packages_str = reformat_type_lists(packages)
    gui_str = reformat_type_lists(gui_scripts)
    cli_str = reformat_type_lists(cli_scripts)

    if readme_paths:
        readme_paths = '["'+'", "'.join(readme_paths)+'"]'
    else:
        readme_paths = '[]'

    if gui_str:
        gui_str = '[project.gui-scripts]\n'+gui_str
    else:
        gui_str = ''
    if cli_str:
        cli_str = '[project.scripts]\n'+cli_str
    else:
        cli_str = ''

    return PoetryFormatStrings.base.format(
        name,
        authors,
        name,
        readme_paths,
        packages_str,
        gui_str,
        cli_str
    )


from os import makedirs
from os.path import sep

def export_pyproject(
    destination, 
    name="my_project", 
    authors="Brandon Fanti: B14CKM4MB4",
    readme_paths=[],
    packages=[],
    gui_scripts=[],
    cli_scripts=[],
    extras=''
):
    try:
        makedirs(destination)
    except:
        pass

    with open(destination+sep+"pyproject.toml", 'w') as fout:
        fout.write(
            fmt_pyproject(
                name=name,
                authors=authors,
                readme_paths=readme_paths,
                packages=packages,
                gui_scripts=gui_scripts,
                cli_scripts=cli_scripts,
            )+extras
        )
