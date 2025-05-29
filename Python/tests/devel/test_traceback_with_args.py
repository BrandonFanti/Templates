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

from MAMBA_SUPER_META.path_hack.add_cwd_namespace import *
from MAMBA_SUPER_META.debug.traceback_with_args import frame_inspector,alt_frame_inspector

from path_hack_test import i_should_exist

def foo(x):
    print(x)

def bar(x):
    foo(x)
    raise Exception("Oh no!")

def baz(x):
    bar(x)


try:
    print(f"Should I exist? ... {i_should_exist}")
    bar("~laa~laa~laa")
except Exception as e:
    e_type, e_instance, exc_info = sys.exc_info()
    traceback.print_exc()
    print("~~~~~~~~~~~~~~~~~~mamba-debug-begin~~~~~~~~~~~~~~~~~~")
    frames = alt_frame_inspector()
    print(f"Traceback (most recent call last):")
    if frames and len(frames) >= 1:
        for index, frame in enumerate(frames):
            print(frame, end='')
    else:
        print(f"Exception without frames({len(frames)})? {e.__class__}")
