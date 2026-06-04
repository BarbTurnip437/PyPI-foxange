from collections.abc import Collection


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
    print('test unique:')
    print(f'return value: {unique([1, 2, 3, 1, 2]) = }')
