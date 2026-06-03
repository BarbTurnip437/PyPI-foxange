from typing import Sequence, TypeVar


def filter_string(text: str, *strings: str, replace_value: str = '') -> str:
    for string in strings:
        text = text.replace(string, replace_value)
    return text


def collect_input(*value) -> list[str]:
    return [input(input_text) for input_text in value]


T = TypeVar('T')


def lenth_limited_input(text, min, max, fallback: T = None) -> str | None | T:
    string = input(text)
    size = len(string)
    if min <= size <= max:
        return string
    else:
        return fallback


def choice_input(
    title, value: Sequence, input_text: str
) -> tuple[int, str] | tuple[None, None]:
    if title is not None:
        print(title)
    for idx, opt in enumerate(value, start=1):
        print(f'{idx}. {opt}')

    user_input = input(input_text)
    if user_input.isdigit():
        idx = int(user_input) - 1
        if 0 <= idx < len(value):
            return idx, value[idx]
    if user_input in value:
        idx = value.index(user_input)
        return idx, user_input

    return None, None


def confirm(
    text='', yes_str: list = ['yes'], no_str: list = ['no']
) -> None | bool:
    string = input(text + f'[{yes_str[0]}/{no_str[0]}] ')
    if string in yes_str:
        return True
    elif string in no_str:
        return False
    else:
        return None


if __name__ == '__main__':
    print('test sanitize_input:')
    print(f"return value: {filter_string('hello!', '!', 'o') = }")
    print()
    print('test collect_input:')
    print(f"return value: {collect_input('1> ', '2> ') = }")
    print()
    print('test lenth_limited_input:')
    print(f"return value: {lenth_limited_input('> ', 10, 20) = }")
    print()
    print('test choice_input:')
    print(f"return value: {choice_input(None, ['a', 'b', 'c'], '> ') = }")
    print()
    print('test confirm:')
    print(f'return value: {confirm() = }')
