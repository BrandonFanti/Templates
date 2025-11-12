import sys
from os.path import isfile, sep as path_sep
import traceback
import inspect
from inspect import FrameInfo

from math import floor as round_down
from math import ceil  as round_up

def filter_user_code(frame_list:list[FrameInfo]):
    #"is filename in CWD"?

    # lambda_filter_condition = lambda frame: 'runpy.py' == frame.filename.split(path_sep)[-1]
    # return list(filter(lambda_filter_condition, frame_list))
    pass

def filter_runpy(frame_list:list[FrameInfo]):
    lambda_filter_condition = lambda frame: 'runpy.py' != frame.filename.split(path_sep)[-1]
    return list(filter(lambda_filter_condition, frame_list))


def filter_ms_vscode_debug_python(frame_list:list[FrameInfo]):
    lambda_filter_condition = lambda frame: 'extensions/ms-python.debugpy' not in frame.filename
    return list(filter(lambda_filter_condition, frame_list))



def frame_inspector():
    e_type, e_instance, exc_info = sys.exc_info()
    stack_frame_list = inspect.stack()[1:]
    stack_frame_list = filter_runpy(stack_frame_list)
    stack_frame_list = filter_ms_vscode_debug_python(stack_frame_list)
    return stack_frame_list
