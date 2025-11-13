from mamba_meta.debug.decorators import Protector
from mamba.parsers.argument_parser import MambaParser

from sys import argv
import logging

class MyAppParser(MambaParser):
    defaults={
        #Set some default attributes for parser
        #  ie.:
        #    "debugging":True
    }

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


@Protector
def main(logger=None):
    parser = MyAppParser(argv, log_level=logging.DEBUG)
    parser.parse_args()
    if parser.debugging:
        logger.set_level(logging.DEBUG)
        logger.debug("Debugging enabled!")


if __name__ == '__main__':
    main()