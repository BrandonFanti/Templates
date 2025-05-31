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