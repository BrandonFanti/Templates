import traceback
import os
import sys

path_test_set = os.getcwd().split(os.path.sep)
if path_test_set[-1] == 'Python':
    mamba_path = os.getcwd()
if path_test_set[-1] == 'tests':
    mamba_path = os.path.sep.join(path_test_set[:-1])+os.path.sep
if path_test_set[-2] == 'tests' and path_test_set[-1] == 'devel':
    mamba_path = os.path.sep.join(os.getcwd().split(os.path.sep)[:-2])+os.path.sep

print(f"cwd:{os.getcwd()}")
print(f"mamba path: {mamba_path}")
sys.path.append(mamba_path)

from MAMBA_SUPER_META.debug import MambaTrace

from path_hack_test import i_should_exist

def foo(x):
    print(x)

def bar(x):
    if isinstance(x,str):
        raise ValueError(f"Oh no! Something is wrong with x!: \"{x}\"")
        foo(x)
    else:
        foo(x)

def baz(x):
    bar(x)


try:
    print(f"Should I exist? ... {i_should_exist}")
    baz(len("~laa~laa~laa"))
    baz("~laa~laa~laa")
except Exception as e:
    e_type, e_instance, exc_info = sys.exc_info()
    # traceback.print_exc()
    print("~~~~~~~~~~~~~~~~~~mamba-debug-begin~~~~~~~~~~~~~~~~~~")
    print(MambaTrace(e, line_prefix=True, vars_helper=True, preview_line_count=6))
