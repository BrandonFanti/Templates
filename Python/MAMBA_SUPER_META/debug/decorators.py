from os import environ
vscode_env_vars = ['__vsc_stable', '__vsc_initialized', '__vsc_status']
is_vscode = all([k in environ.keys() for k in vscode_env_vars])
from functools import wraps
import pdb

from ..logging import logger
from . import ColoredMambaTrace


class Protector:
    pdb_enable = True
    vscode_enable = is_vscode

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
                        skip_frames=1
                    )
                )
                if Protector.pdb_enable: pdb.post_mortem(t=e.__traceback__)
            if not Protector.vscode_enable:
                protector_logger.info("Exiting...")
            else:
                protector_logger.info("UNSAFELY FOR VSCODE...")
                raise _exception

        return trace_util
