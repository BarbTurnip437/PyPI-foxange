"""Github repo: https://github.com/foxange-org/PyPI-foxange"""

from . import file, input, list_proce, math
from .file import ouput_to_file
from .input import collect_input
from .list_proce import unique
from .math import deep_sum

__all__ = [
    'file',
    'input',
    'list_proce',
    'math',
    'ouput_to_file',
    'collect_input',
    'unique',
    'deep_sum',
]

version_info: tuple[int, int, int] = (0, 5, 0)
__version__: str = '.'.join(map(str, version_info))
