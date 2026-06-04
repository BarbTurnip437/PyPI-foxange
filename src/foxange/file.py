import json
import os
from typing import Any, List


def ouput_to_file(path, *value, mode='w', end='', sep='\n') -> None:
    all_input_value: str = ''
    for input_value in value:
        all_input_value += input_value + sep
    all_input_value += end
    with open(path, mode) as f:
        f.write(all_input_value)


def read_lines(
    path: str, strip_newline: bool = True, encoding: str = 'utf-8'
) -> List[str]:

    with open(path, 'r', encoding=encoding) as f:
        lines = f.readlines()
    if strip_newline:
        lines = [line.rstrip('\n\r') for line in lines]
    return lines


def write_lines(
    path: str, lines: List[str], mode: str = 'w', encoding: str = 'utf-8'
) -> None:
    dirname = os.path.dirname(path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    with open(path, mode, encoding=encoding) as f:
        for line in lines:
            f.write(line + '\n')


def tail(path: str, n: int = 10, encoding: str = 'utf-8') -> List[str]:
    with open(path, 'rb') as f:
        f.seek(0, os.SEEK_END)
        file_size = f.tell()
        buffer = bytearray()
        lines = []
        pos = file_size
        while pos > 0 and len(lines) < n:
            chunk_size = min(4096, pos)
            pos -= chunk_size
            f.seek(pos)
            chunk = f.read(chunk_size)
            buffer[:0] = chunk
            lines = buffer.splitlines()
            if len(lines) > n:
                lines = lines[-n:]
        lines = [line.decode(encoding) for line in lines]
        return lines


def head(path: str, n: int = 10, encoding: str = 'utf-8') -> List[str]:
    lines = []
    with open(path, 'r', encoding=encoding) as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            lines.append(line.rstrip('\n\r'))
    return lines


def safe_read_json(
    path: str, fallback: Any = None, writeback: bool = False
) -> Any:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        if writeback:
            safe_write_json(path, fallback)
        return fallback


def safe_write_json(path: str, data: Any, indent: int = 2) -> None:
    dirname = os.path.dirname(path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)


def format_size(size_bytes: float, *, binary_unit=False) -> str:
    if binary_unit:
        unit_set = ('B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'Zib')
        base = 1024
    else:
        unit_set =('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB')
        base = 1000

    for unit in unit_set:
        if abs(size_bytes) < base:
            return f'{size_bytes:.2f} {unit}'
        size_bytes /= base
    else:
        return f'{size_bytes:.2f} {unit}'  # type: ignore


if __name__ == '__main__':
    print('我已急苦QAQ')
