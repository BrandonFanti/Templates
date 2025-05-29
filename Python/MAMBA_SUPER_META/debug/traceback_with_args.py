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

class Mamba_Debug_Frame:
    _frame = None
    file = None
    line = None
    code = None
    faulty_line = None
    _preview_lines = 3

    def __init__(self, tb_frame, preview_code_line_count=3):
        self._frame = tb_frame
        if '__file__' in tb_frame.tb_frame.f_locals.keys():
            self.file = tb_frame.tb_frame.f_locals['__file__']
        if not self.file:
            self.file = tb_frame.tb_frame.f_globals['__file__']

        if not self.file or not isfile(self.file):
            print(f"Failed to read file from frame: {self._frame}")
            for k in dir(self._frame.tb_frame): print(f"{k}:{getattr(self._frame.tb_frame,k)}")
            raise ValueError(f"`{self.file}` is not a file path!")


        self.line = tb_frame.tb_lineno
        self._total_lines = preview_code_line_count

        self._line_start = round_down(self.line-self._total_lines/2)
        self._line_end = self._line_start+self._total_lines
        self.code = self.read_code(self.file, self._line_start, len=self._total_lines)

        self.faulty_line = self.code[self.line-self._line_start]
        print(f"Faulty line({self.line}): {self.faulty_line}")
        print(''.join([f"(L{i+self._line_start}) {l}" for i,l in enumerate(self.code)]))

    def __str__(self):
        odd_num_lines = int((self._total_lines/2)//2)

        #TODO: remove
        placeholder=''

        return \
            f"  File \"{self.file}\", line {self._line_start}, in {placeholder}\n"+\
            ''.join(self.code[:round_up(self._total_lines/2)])+\
            '*'+self.faulty_line[1:]+\
            ''.join(self.code[self._total_lines:])

    @staticmethod
    def read_code(file_path, line, len=None) -> list[str]:
        line_index = line-1
        if not isfile(file_path):
            raise ValueError(f"`{file_path}` is not a file path!")
        with open(file_path, 'r') as src:
            return src.readlines()[line_index:line_index+len]


def alt_frame_inspector():
    has_next_frame = lambda tbf: (hasattr(tbf, 'tb_next') and tbf.tb_next!=None)

    e_type, e_instance, exc_info = sys.exc_info()
    current_frame = exc_info
    frames = [Mamba_Debug_Frame(current_frame)]


    # print(f"next? {has_next_frame(current_frame)} - {current_frame.tb_next}")
    while has_next_frame(current_frame):
        current_frame = current_frame.tb_next
        frames.append(Mamba_Debug_Frame(current_frame))
        # print(f"next? {has_next_frame(current_frame)} - {current_frame.tb_next}")

    return frames

def frame_inspector():
    e_type, e_instance, exc_info = sys.exc_info()
    stack_frame_list = inspect.stack()[1:]
    stack_frame_list = filter_runpy(stack_frame_list)
    stack_frame_list = filter_ms_vscode_debug_python(stack_frame_list)
    return stack_frame_list

