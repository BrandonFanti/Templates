import mamba

from mamba_meta.debug.decorators import Protector
from mamba.parsers.argument_parser import MambaParser

from sys import argv

class MyAppParser(MambaParser):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


@Protector
def main(logger=None):
    parser = MyAppParser(argv)
    args = parser.parse_args()
    logger.info(args)


if __name__ == '__main__':
    main()