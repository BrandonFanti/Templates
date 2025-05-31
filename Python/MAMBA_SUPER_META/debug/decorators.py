from os import environ
vscode_env_vars = ['DEBUGPY_RUNNING']
is_vscode = all([k in environ.keys() for k in vscode_env_vars])
from functools import wraps
import pdb

from time import sleep
from ..logging import logger, color
from . import ColoredMambaTrace


class Protector:
    pdb_enable = True
    vscode_enable = is_vscode
    magic=False

    def __init__(self, your_main):
        return self.get_protector(your_main)

    @staticmethod
    def get_protector(func):
        @wraps(func)
        def trace_util(*args, **kwargs):
            _exception = None
            protector_logger = logger(name='mamba_shield')
            try:
                return func(*args, logger=protector_logger, **kwargs)
            except Exception as e:
                _exception = e
                protector_logger.print(
                    ColoredMambaTrace(
                        e, 
                        line_prefix=True, 
                        vars_helper=True, 
                        preview_line_count=5, 
                        skip_frames=1,
                        magic=Protector.magic
                    )
                )
                if Protector.pdb_enable and not Protector.vscode_enable:
                    pdb.post_mortem(t=e.__traceback__)

            if not Protector.vscode_enable:
                protector_logger.info(f"Exiting... {color.RESET}")
            else:
                protector_logger.info(f"UNSAFELY FOR VSCODE... {color.RESET}")
                raise _exception

        return trace_util
