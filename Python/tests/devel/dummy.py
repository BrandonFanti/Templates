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

from MAMBA_SUPER_META.debug.decorators import protector

def explosion_prompted():
    my_logger.colorize("Wanna see me explode?", color='red')
    explode = 'Y'

    if explode=='Y':
        raise Exception("SHOT?! IN THE BOMB?!")

@protector
def main(logger=None):
    if logger:
        my_logger = logger.getLogger()
        my_logger.info(f"Hey! I'm new! It's me, {logger.name}, from {__name__}!")


if __name__ == '__main__':
    main()