import traceback
import os
import sys

from MAMBA_SUPER_META.debug.MambaTrace import ColoredMambaTrace


def foo(x):
    print(x)

def bar(x):
    if isinstance(x,str):
        foo(x)
        raise ValueError(f"Oh no! Something is wrong with x!: \"{x}\"")
    else:
        foo(x)

def baz(x):
    bar(x)

try:
    baz(len("~laa~laa~laa"))
    baz("~laa~laa~laa")
except Exception as e:
    e_type, e_instance, exc_info = sys.exc_info()
    # traceback.print_exc()
    print("~~~~~~~~~~~~~~~~~~mamba-debug-begin~~~~~~~~~~~~~~~~~~")
    print(ColoredMambaTrace(e, line_prefix=True, vars_helper=True, preview_line_count=5))
