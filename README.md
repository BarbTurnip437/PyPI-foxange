## foxange ，一个python第三方库😊

### 目录

- 下载
- 如何使用函数和函数的特殊注意🤔
  - `__init__.py`
  - `math.py`
  - `input.py`
  - `list_proce.py`
  - `file.py`
- 声明和其他
- 感谢和致谢

---

### 下载

```pip install foxange```

---

## 如何使用函数和函数的特殊注意🤔

### `__init__.py`

- `get_help() -> None`

  显示 foxange 的 Github 仓库地址

> [!WARNING]
> v0.5.0 被废弃，请使用 `print(foxange.__doc__)` 或 `help(foxange)`


- `version() -> str`
  
  返回你在使用的 foxange 版本

  **代码示例**：
  ```cmd
  C:\> pip install foxange==0.4.0
  ```

  ```python
  >>> import foxange
  >>> foxange.version()
  '0.4.0'
  ```

> [!IMPORTANT]
> v0.4.0 开始这个函数不会输出 `version : {version}` 文字了

> [!WARNING]
> v0.5.0 被废弃，请使用 `__version__`

------

## `math.py`

- `is_prime(number: int) -> bool`
  
  判断一个整数是否为素数。
  
  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.is_prime(7))
  print(foxange.math.is_prime(10))
  '''
  True
  False
  '''
  ```

> [!IMPORTANT]
> v0.5.0 极大的优化了这个函数  
> 在判断1000333是不是质数的性能测试中新版本是原版本的1437倍（卧槽这个数字真的不是乱填的真的测出来是这个数）

- `is_composite_number(number: int) -> bool`
  
  判断一个整数是否为合数（大于1且不是素数）。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.is_composite_number(9))
  print(foxange.math.is_composite_number(2))
  '''
  True
  False
  '''
  ```

- `pow(number1: float, number2: float) -> float`
  
  幂运算，返回 `number1 ** number2`。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.pow(2, 3))
  '''
  8.0
  '''
  ```

> [!WARNING]
> v0.5.0 被废弃，请使用 `number1 ** number2` 或 `math.pow()`

- `root(number: int, inx: int = 2) -> float`
  
  求 `number` 的 `inx` 次方根（默认平方根）。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.root(16))
  print(foxange.math.root(27, 3))
  '''
  4.0
  3.0
  '''
  ```

> [!CAUTION]
> v0.5.0 时此函数从`radical_sign()` 更名为 `root()`

- `factors(number: int, key=lambda x: True, recur: bool = False) -> list[int]`
  
  返回 `number` 的所有因子。

  - `key`：过滤函数，只有 `key(i)` 为 `True` 的因子才加入。
  - `recur`：若为 `True`，平方根因子会被添加两次（`i` 和 `j` 都加入）。
  
> [!TIP]
> `recur=True` 会使完全平方数的平方根因子出现两次。
  
  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.factors(12))
  print(foxange.math.factors(12, key=lambda x: x % 2 == 0))
  print(foxange.math.factors(16, recur=True))
  '''
  [1, 2, 3, 4, 6, 12]
  [2, 4, 6, 12]
  [1, 2, 2, 4, 8, 16]
  '''
  ```

> [!CAUTION]
> v0.5.0 时此函数从`factor()` 更名为 `factors()`

- `prime_factors(n: int) -> list[int]`
  
  返回 `n` 的所有质因子（包含重复次数）。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.prime_factors(12))
  print(foxange.math.prime_factors(18))
  '''
  [2, 2, 3]
  [2, 3, 3]
  '''
  ```

- `sum(*values)`
  
  增强求和函数，支持数字和列表混合。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.sum(1, 2, [3, 4], 5))
  '''
  15
  '''
  ```

  如果你输入的数据中不会包含不可迭代对象建议使用 `sum(itertools.chain())` （内置的sum）

  ~~有点hyw了这个函数想把它删了但是不太敢——Cbscfe~~

- `digit_separation(number: int) -> list`
  
  将整数按位拆分为数字列表。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.digit_separation(12345))
  '''
  [1, 2, 3, 4, 5]
  '''
  ```

- `is_perfect(number: int) -> bool`
  
  判断是否为完全数（真因子和等于自身）。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.is_perfect(6))
  print(foxange.math.is_perfect(12))
  '''
  True
  False
  '''
  ```

> [!CAUTION]
> v0.5.0 时此函数从`is_perfect_number()` 更名为 `is_perfect()`

- `is_excess_number(number: int) -> bool`
  
  判断是否为过剩数（真因子和大于自身）。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.is_excess_number(12))
  '''
  True
  '''
  ```

- `is_deficit(number: int) -> bool`
  
  判断是否为亏数（真因子和小于自身）。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.is_deficit(4))
  '''
  True
  '''
  ```

- `is_amicable_numbers(number1: int, number2: int) -> bool`
  
  判断两个数是否为亲和数（彼此的真因子和相等）。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.is_amicable_numbers(220, 284))
  '''
  True
  '''
  ```

- `is_engagements_number(number1: int, number2: int) -> bool`
  
  判断两个数是否为订婚数（除去1和自身的真因子和相等）。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.is_engagements_number(48, 75))
  '''
  True
  '''
  ```

- `is_smith_number(number: int) -> bool`
  
  判断是否为 Smith 数（合数，各位数字之和等于所有质因子（含重复）的各位数字之和）。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.is_smith_number(4))
  print(foxange.math.is_smith_number(22))
  '''
  True
  False
  '''
  ```

- `is_niven_number(number: int) -> bool`
  
  判断是否为 Harshad 数（能被其各位数字之和整除）。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.is_niven_number(18))
  '''
  True
  '''
  ```

- `is_moran_number(number: int) -> bool`
  
  判断是否为 Moran 数（Harshad 数，且商为素数）。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.is_moran_number(18))
  print(foxange.math.is_moran_number(27))
  '''
  False
  True
  '''
  ```

- `is_self_power(number: int) -> bool`
  
  判断是否为自幂数（每位数字的位数次幂之和等于自身）。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.is_self_power(153))
  print(foxange.math.is_self_power(9474))
  '''
  True
  True
  '''
  ```

> [!CAUTION]
> v0.5.0 时此函数从`is_self_power_number()` 更名为 `is_self_power()`

- `is_narcissus_number(number: int) -> bool`
  
  判断是否为水仙花数（三位自幂数）。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.is_narcissus_number(153))
  print(foxange.math.is_narcissus_number(9474))
  '''
  True
  False
  '''
  ```

- `is_palindrome(number: int) -> bool`
  
  判断是否为回文数。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.is_palindrome(12321))
  print(foxange.math.is_palindrome(12345))
  '''
  True
  False
  '''
  ```

> [!CAUTION]
> v0.5.0 时此函数从`is_palindrome_number()` 更名为 `is_palindrome()`

- `is_reversible_prime(number: int) -> bool`
  
  判断是否为可逆素数（本身为素数，反转后也是素数且不同）。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.is_reversible_prime(13))
  print(foxange.math.is_reversible_prime(11))
  '''
  True
  False
  '''
  ```

- `gcd(a: int, b: int) -> int`
  
  最大公约数。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.gcd(48, 18))
  '''
  6
  '''
  ```

> [!WARNING]
> v0.5.0 被废弃，请使用 `math.gcd()`

- `lcm(a: int, b: int) -> int`
  
  最小公倍数。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.lcm(12, 18))
  '''
  36
  '''
  ```

> [!WARNING]
> v0.5.0 被废弃，请使用 `math.lcm()`

- `factorial(n: int) -> int`
  
  阶乘。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.factorial(5))
  '''
  120
  '''
  ```

- `isqrt(n: int) -> int`
  
  整数平方根（向下取整）。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.isqrt(10))
  '''
  3
  '''
  ```
  
> [!WARNING]
> v0.5.0 被废弃，请使用 `int(math.sqrt())`

- `reverse_int(n: int) -> int`
  
  反转整数，保留符号。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.reverse_int(12345))
  print(foxange.math.reverse_int(-678))
  '''
  54321
  -876
  '''
  ```

- `bin_to_int(bin_str: str) -> int`
  
  二进制字符串转整数。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.bin_to_int("1010"))
  '''
  10
  '''
  ```

- `int_to_bin(n: int) -> str`
  
  整数转二进制字符串（不带 `0b` 前缀）。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.int_to_bin(10))
  '''
  "1010"
  '''
  ```

- `digits_count(n: int) -> int`
  
  返回整数的位数（0 算 1 位）。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.digits_count(0))
  print(foxange.math.digits_count(12345))
  '''
  1
  5
  '''
  ```

- `combination(n: int, k: int) -> int`
  
  组合数 C(n, k)。

  **代码示例**：

  ```python
  import foxange
  
  print(foxange.math.combination(5, 2))
  '''
  10
  '''
  ```

> [!WARNING]
> v0.5.0 被废弃，请使用 `math.comb()`

## `input.py`

- `collect_input(*value) -> list[str]`
  
  一次性接受多个输入，返回一个列表

  **代码示例**：

  ```python
  import foxange

  print(foxange.input.collect_input("name> ", "age> "))
  '''
  name> 张三
  age> 20
  ['张三' , '20']
  '''
  ```

- `filter_string(text: str, *strings: str, replace_value: str = '') -> str`
  
  将`text`字符串中所有的`*strings`子字符串替换为`replace_value`

  **代码示例**：

  ```python
  import foxange

  print(foxange.input.filter_string('hello world!', 'h', 'o'))
  '''
  ell wrld!
  '''
  ```

> [!NOTE]
> v0.5.0 增加了一个关键字参数 `replace_value` 表示要替换为的值

> [!CAUTION]
> v0.5.0 时此函数从 `sanitize_input()` 更名为 `filter_string()`

  **注意** : 在让这个函数导入`text` 形参时,务必使用:`text=...`否则会有问题

- `lenth_limited_input[T](text, min, max, fallback: T = None) -> str | None | T`

  判断`input(text)`字符串的长度是否满足**大于等于`min`小于等于`max`**，如果不满足则返回fallback

  **代码示例**：

  ```python
  import foxange
  foxange.input.numeric_input(
      "请输入一个长度小于等于1大于等于5的字符串> ", 
      1, 
      5, 
      "你输入错了!😠",
  )
  '''
  请输入一个长度小于等于1大于等于5的字符串> 4874964345465488
  你输入错了!😠
  '''
  ```

> [!IMPORTANT]
> v0.5.0 时 `notvalid` 参数更名为 `fallback`

> [!CAUTION]
> v0.5.0 时此函数从`numeric_input()` 更名为 `lenth_limited_input()`

- `choice_input(title, value: Sequence, input_text: str) -> tuple[int, str] | tuple[None, None]:`
  
  输出一个类似于这个:
  ```
  title
  1. ***
  2. xxx
  input>
  ```
  菜单的函数，并返回一个`(参数在value中的位置, 这个值)`的元组

  **代码示例**：

  ```python
  import foxange
  print(foxange.input.choive_input("菜单", ['hi','bye'], "选择> "))
  '''
  菜单
  1. hi
  2. bye
  选择>1
  [0,'hi']
  '''
  ```

  ~~我都不知道这个东西有什么用~~  
  ~~你前面的东西更没用——Cbscfe~~

- `confirm(text='', yes_str: list = ['yes'], no_str: list = ['no']) -> None | bool`:

  一个类似于tkinter.askyesno的东西

  **代码示例**：

  ```python
  import foxange

  print(foxange.input.confirm("你确定要退出吗?",yes_str=["yes",'y'],no_str=['no','n']))
  '''
  你确定要退出吗?[yes/no] yes
  True
  '''
  ```

> [!TIP]
> 在`[]`中,他只会显示`yes_str`和`no_str`的第一项,如果是`no_str`的则返回`True`,如果是`yes_str`的,返回`False`,什么都不是返回`None`,**`yes_str`会比`no_str`优先判断!**

> [!NOTE]
> v0.5.0 略微调整了输出格式

## `list_proce.py`

- `remove(value: list, condition: Callable | None = None) -> list:`

  删除满足条件的值，`condition` 为 `None` 时直接返回原列表

  **代码示例**：

  ```python
  import foxange

  print(foxange.list_proce.remove(value=[1,2,3,4,5,6],condition=lambda x:x%2==0)) #删除所有的偶数
  '''
  [1,3,5]
  '''
  ```

> [!WARNING]
> v0.5.0 被废弃，请使用 `filter()`  
> 请注意 `filter()` 的过滤逻辑上与此函数相反，也就是删除不满足条件的值

- `unique(value: list) -> list`

  剔除列表中重复的元素

  此函数实现是将整个 list 转换成 set 再转换回来，因此请确保 list 中所有的内容都是 Hashable

  如果你想要创建一个内容不重复的 Container，建议直接创建一个 set

  **代码示例**：

  ```python
  import foxange
  print(foxange.list_proce.unique([1,1,2,3]))
  '''
  [1,2,3]
  '''
  ```

- `rotate(value: list, inx: int) -> list:`

  将列表`value`向右旋`inx`步数

  **代码示例**：

  ```python
  import foxange
  print(foxange.list_proce.rotate([1,2,3,4],1))
  '''
  [4,1,2,3]
  '''
  ```

  **注意** : **如果旋转步数是 0 或列表长度的整数倍，则返回原列表的副本**

- `spread(*args) -> tuple`

  `spread` 函数用于将传入的参数“展开”成一个元组。

  - 如果某个参数是列表或元组，就会将其元素逐一取出添加到结果中；
  - 如果参数是其他类型的值，则直接添加到结果中。

  最终返回一个元组（不可变序列）。

  **代码示例**：

  ```python
  from foxange.list_proce import spread
  
  result = spread([1, 2], 3, (4, 5), "hello")
  print(result)  
  '''
  (1, 2, 3, 4, 5, 'hello')
  '''
  ```

  它常用于需要将多个可能嵌套的可迭代对象合并成一个扁平元组的场景。

  如果你输入的数据中不会包含不可迭代对象建议使用 `itertools.chain()`

## `file.py`

- `input_to_file(*value, path, mode='w', end='', sep='\n') -> None`
  
  将传入的多个字符串按 `sep` 拼接，末尾加上 `end`，写入指定文件。支持写入模式（`'w'` 覆写，`'a'` 追加）。

  **代码示例**：

  ```python
  import foxange
  
  foxange.file.input_to_file("hello", "world", path="test.txt", sep=",", end="!")
  # 文件内容: hello,world!
  '''
  (无返回值，文件被写入)
  '''
  ```

- `read_lines(path: str, strip_newline: bool = True, encoding: str = 'utf-8') -> List[str]`
  
  读取文件所有行，默认去除末尾换行符。

  **代码示例**：

  ```python
  import foxange
  
  lines = foxange.file.read_lines("test.txt")
  print(lines)
  '''
  ['hello,world!']
  '''
  ```

- `write_lines(path: str, lines: List[str], mode: str = 'w', encoding: str = 'utf-8') -> None`
  
  将字符串列表写入文件，每行自动添加换行符。自动创建缺失的父目录。

  **代码示例**：

  ```python
  import foxange
  
  foxange.file.write_lines("output.txt", ["first", "second"], mode='w')
  '''
  (文件 output.txt 包含两行: first 和 second)
  '''
  ```

- `tail(path: str, n: int = 10, encoding: str = 'utf-8') -> List[str]`
  
  高效读取文件最后 `n` 行（按字节倒查，适合大文件）。

  **代码示例**：

  ```python
  import foxange
  
  last = foxange.file.tail("test.txt", n=1)
  print(last)
  '''
  ['hello,world!']
  '''
  ```

- `head(path: str, n: int = 10, encoding: str = 'utf-8') -> List[str]`
  
  读取文件前 `n` 行。

  **代码示例**：

  ```python
  import foxange
  
  first = foxange.file.head("test.txt", n=1)
  print(first)
  '''
  ['hello,world!']
  '''
  ```

- `safe_read_json(path: str, default: Any = None) -> Any`

  安全读取 JSON 文件。若文件不存在或 JSON 无效，返回 `default`。

  **代码示例**：

  ```python
  import foxange
  
  data = foxange.file.safe_read_json("config.json", default={})
  print(data)
  '''
  {}   (假设文件不存在或无效)
  '''
  ```  

- `safe_write_json(path: str, data: Any, indent: int = 2) -> None`

  将数据写入 JSON 文件，自动创建父目录，支持非 ASCII 字符。

  **代码示例**：

  ```python
  import foxange
  
  foxange.file.safe_write_json("data.json", {"name": "foxange", "version": "0.4.0"})
  '''
  (生成 data.json 文件)
  '''
  ```

- `get_file_size(path: str, human_readable: bool = False) -> Union[int, str]`

  返回文件大小（字节）。若 `human_readable=True`，转换为 B/KiB/MiB 等易读格式。

  **代码示例**：

  ```python
  import foxange
  
  size = foxange.file.get_file_size("test.txt")
  print(size)
  size_hr = foxange.file.get_file_size("test.txt", human_readable=True)
  print(size_hr)
  '''
  12
  '12.0 B'
  '''
  ```

> [!NOTE]
> v0.5.0 修复了显示的单位错误的使用了 KB/MB/GB... 而不是 KiB/MiB/GiB 的bug

- `ensure_dir(path: str) -> None`

  创建目录

  **代码示例**：

  ```python
  import foxange
  
  foxange.file.ensure_dir("./new_folder/sub")
  '''
  (目录被创建，无返回值)
  '''
  ```

> [!WARNING]
> v0.5.0 被废弃，请使用 `os.makedirs()` 或 `pathlib.Path().mkdir()`

- `atomic_write(path: str, data: Union[str, bytes], mode: str = 'w', encoding: str = 'utf-8') -> None`
  原子写入：先写入临时文件，再替换目标文件，避免写入中途崩溃导致文件损坏。

  **注意**：Windows 下若目标文件被其他进程打开，`os.replace` 可能失败。

  **代码示例**：

  ```python
  import foxange
  
  foxange.file.atomic_write("important.txt", "critical data")
  '''
  (文件被安全写入)
  '''
  ```

> [!CAUTION]
> v0.5.0 彻底移除此一开始就不能运行起来的函数，这是AI写的吗IDE都爆红了没看到？完全不知道这个函数的用意

- `find_files(directory: str, pattern: str = '*', recursive: bool = True) -> List[str]`
  查找目录下匹配通配符 `pattern` 的文件，返回相对路径列表。支持 `*` 和 `?`（`fnmatch` 规则）。

  **代码示例**：

  ```python
  import foxange
  
  all_py = foxange.file.find_files(".", "*.py", recursive=True)
  print(all_py)
  '''
  ['input.py', 'list_proce.py', 'math.py', 'file.py', ...]
  '''
  ```

> [!WARNING]
> v0.5.0 被废弃，请使用 `glob.glob()` 或 `pathlib.Path().glob()`

---

## 声明和其他

如果你发现了问题，请在Github仓库提交问题。

发送格式: `函数`   `问题`    `你的代号` 我们会在这个文件里记录你的名字,从而感谢你对foxange第三方库的贡献和支持!

**foxange** 第三方库开源github链接 - <https://github.com/foxange-org/PyPI-foxange>

---

## 感谢和致谢

这里放着所有找bug和帮助完成foxange第三方库的所有人(这些人都是在这个版本之前提交的)

| 代号 | 邮箱 | 时间 | 版本 | 函数 | 问题 | 严重程度 |
| :--: | :--: | :--: | :--: | :--: | :--: | -------- |
|      |      |      |      |      |      |          |

