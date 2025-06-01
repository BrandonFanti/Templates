from ..create import *

def __call__():
    copy_file_or_folder((
        get_source(),
        "project",
        "generic",
    ))