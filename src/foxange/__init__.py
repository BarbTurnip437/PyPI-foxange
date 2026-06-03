"""Github repo: https://github.com/foxange-org/PyPI-foxange"""

from warnings import deprecated

from . import file, input, list_proce, math
from .file import input_to_file
from .input import collect_input
from .list_proce import unique
from .math import sum

__all__ = [
    'file',
    'input',
    'list_proce',
    'math',
    'input_to_file',
    'collect_input',
    'unique',
    'sum',
]


__version__ = '0.5.0'


# 为向下兼容而保留，不过说实话删了更好
# 毕竟现在还在 0.x.x 的版本号，但是我懒得删
@deprecated('Use __version__ instead')
def version() -> str:
    return __version__


@deprecated('Use print(foxange.__doc__) or help(foxange) instead')
def get_help() -> None:
    print(__doc__)
