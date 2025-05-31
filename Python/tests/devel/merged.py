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

import traceback

path_hack = False
mamba_trace = False
colored_mamba_trace = False

try:
    from path_hack import *
    path_hack=True
except:
    traceback.print_exc()
    pass

assert path_hack==True, "PathHack pass"

try:
    from test_traceback_with_args import *
    mamba_trace = True
except:
    traceback.print_exc()
    pass

assert mamba_trace==True, "MambaTrace Failed"

try:
    from test_colorized_traceback_with_args import *
    colored_mamba_trace = True
except:
    traceback.print_exc()
    pass

assert colored_mamba_trace==True, "ColoredMambaTrace Failed"


meta_pass = True
