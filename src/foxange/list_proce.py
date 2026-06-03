from collections.abc import Callable, Collection
from warnings import deprecated


@deprecated(
    'Use filter() instead, '
    'beware that filter() behaves opposite as this function '
    'and returns an iterable instead of a list'
)
def remove(value: list, condition: Callable | None = None) -> list:
    # 这个函数太诡异了我要回家
    if condition is None:
        return value
    return [*filter(lambda x: not condition(x), value)]


# @deprecated(
#     'If you want to create a container with no overlapping items '
#     'you should use a set'
# )
def unique(value: list) -> list:
    return list(set(value))


def rotate(value: list, inx: int) -> list:
    value_len = len(value)
    shift = inx % value_len
    return value[-shift:] + value[:-shift] if shift != 0 else value[:]


def spread(*args) -> tuple:
    result = []
    for arg in args:
        if isinstance(arg, Collection):
            result.extend(arg)
        else:
            result.append(arg)
    return tuple(result)


if __name__ == '__main__':
    print('test remove:')
    print(f'return value: {remove([1, 2, 3, 4, 5], lambda x: x % 2 == 0) = }')
    print()
    print('test unique:')
    print(f'return value: {unique([1, 2, 3, 1, 2]) = }')
