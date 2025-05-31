from os.path import isfile, sep as path_sep
from math import floor as round_down
from math import ceil  as round_up


import re
import ast
import pprint

from ....general import obj_to_dict

def find_python_variable(line, variable_name):
    try:
        tree = ast.parse(line)
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id == variable_name:
                return True
    except SyntaxError:
        pass
    return False

class MambaFrame:
    _frame = None
    file = None
    line = None
    code = None
    faulty_line = None
    _preview_lines = 3
    line_prefix_enabled = False
    tf_locals = None
    vars_helper_enabled = False
    problem_vars_str = ''

    def __init__(self, tb_frame, preview_line_count=3, line_prefix=False, vars_helper=False):
        self._frame = tb_frame
        self.tf_locals = tb_frame.tb_frame.f_locals

        if '__file__' in self.tf_locals.keys():
            self.file = self.tf_locals['__file__']
        if not self.file:
            self.file = tb_frame.tb_frame.f_globals['__file__']

        if not self.file or not isfile(self.file):
            print(f"Failed to read file from frame: {self._frame}")
            for k in dir(self._frame.tb_frame): print(f"{k}:{getattr(self._frame.tb_frame,k)}")
            raise ValueError(f"`{self.file}` is not a file path!")

        self.line_prefix_enabled = line_prefix
        self.vars_helper_enabled = vars_helper

        self.line = tb_frame.tb_lineno
        self._total_lines = preview_line_count

        self._line_start = round_down(self.line-self._total_lines/2)
        self._line_end = self._line_start+self._total_lines
        self.code = self.read_code(self.file, self._line_start, len=self._total_lines)

        self.faulty_line = self.code[self.line-self._line_start]
        # print(f"Faulty line({self.line}): {self.faulty_line}")

        self.line_prefixed_faulty_line = f"{self.line}\t|*"+self.faulty_line
        self.line_prefixed_code = [f"{i+self._line_start}\t| {l}" for i,l in enumerate(self.code)]

        #Some final formatting convenience strings

        #TODO: fix/remove
        placeholder=''

        self.frame_prefix = \
            f"  File \"{self.file}\", "\
                +f"line {self._line_start+round_up(self._total_lines/2)},"\
                +f" in {placeholder}\n"

        odd_num_lines = self._total_lines%2

        self.pre_faulting_lines = \
            ''.join(self.code[:round_up(self._total_lines/2)])
        self.line_prefixed__pre_faulting_lines = \
            ''.join(self.line_prefixed_code[:round_up(self._total_lines/2)])

        self.post_faulting_lines = \
                ''.join(self.code[self._total_lines-odd_num_lines:])
        self.line_prefixed__post_faulting_lines = \
                ''.join(self.line_prefixed_code[self._total_lines-odd_num_lines:])

        if self.vars_helper_enabled:
            self.problem_vars_str = self.get_helpful_vars_str()

    def __str__(self) -> str:
        traceback_string = ""

        if self.line_prefix_enabled:
            traceback_string = \
                self.frame_prefix+\
                self.line_prefixed__pre_faulting_lines+\
                self.line_prefixed_faulty_line+\
                self.line_prefixed__post_faulting_lines+\
                self.problem_vars_str
        else:
            traceback_string = \
                self.frame_prefix+\
                self.pre_faulting_lines+\
                self.faulty_line+\
                self.post_faulting_lines+\
                self.problem_vars_str

        return traceback_string

    def get_helpful_vars_str(self):
        problem_vars_str = ""
        local_vars = self.tf_locals.keys()

        self.vars_in_faulty_line = re.match(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', self.faulty_line)


        local_var_filter = lambda x: \
            not callable(self.tf_locals[x]) \
            and x in self.faulty_line

        filtered_vars = list(filter(local_var_filter, local_vars))
        if any(filtered_vars):
            problem_vars_str = "MambaTrace has detected these variables as potentially relevant:\n"
            for var in filtered_vars:
                problem_vars_str += f"    {var} = "

                if isinstance(var, str):
                    if isinstance(var, object):
                        problem_vars_str += \
                            str(obj_to_dict(self.tf_locals[var]))\
                                .replace('{','{\n\t')\
                                .replace(',',',\n\t')\
                                .replace('}','\n}')\
                                +'\n'
                        continue
                    problem_vars_str += f'"{self.tf_locals[var]}"'
                else:
                    problem_vars_str += f"{self.tf_locals[var]}"

                problem_vars_str +='\n'
        return problem_vars_str

    @staticmethod
    def read_code(file_path, line, len=None) -> list[str]:
        line_index = line-1
        if not isfile(file_path):
            raise ValueError(f"`{file_path}` is not a file path!")
        with open(file_path, 'r') as src:
            return src.readlines()[line_index:line_index+len]