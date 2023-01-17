# 函数提高
from typing import Callable, Any

print('这里是函数提高')

print('首先是递归')


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))

print('')

print('这里是 lambda 表达式')


# 一个函数，仅有一个返回值，仅有一句代码，可以用 lambda 简化
# 简化后缩减代码量，减少内存占用，优化

# lambda 参数列表 : 表达式（必须有返回值）
# 可以接受任意数量的参数，但只能返回一个值


def fn1():
    return 100


# 得到函数地址
print(fn1)
# 得到函数返回值
print(fn1())

fn2: Callable[[], int] = lambda: 200

print(fn2)
print(fn2())

fn3: Callable[[Any, Any], Any] = lambda a, b: a + b

print(fn3(10, 20))

fn4: Callable[[], int] = lambda: 2
print(fn4)
print(fn4())

# lambda 不同参数调用

# 无参调用
fn5: Callable[[], int] = lambda: 50
print(fn5)

# 单个参数调用
fn6: Callable[[Any], Any] = lambda a: a
print(fn6('hello python'))

# 默认参数
fn7: Callable[[Any, Any, Any], Any] = lambda a, b, c = 100: a + b + c
print((fn7(10, 20)))
print((fn7(10, 20, 200)))

# 可变参数 *args
fn8: Callable[[Any], Any] = lambda *args: args
print(fn8(10, 20, 30))

# 可变参数 *kwargs
fn9: Callable[[Any], Any] = lambda **kwargs: kwargs
print(fn9(name='bob', age=26, gender='man', id='2052152'))
print(fn9(name='bob', age=26, ))
print(fn9(name='bob', age=26, gender='man'))

print('这里是 lambda 应用')

# 带判断的 lambda

fn10: Callable[[Any, Any], Any] = lambda a, b: a if a > b else b
print(fn10(10, 20))

# 列表数据根据 key 值排序
students = \
    [
        {'name': 'Tom', 'age': 20, 'gender': 1},
        {'name': 'bob', 'age': 18, 'gender': 1},
        {'name': 'cat', 'age': 25, 'gender': 0},
        {'name': 'alk', 'age': 21, 'gender': 1}
    ]

students.sort(key=lambda x: x['age'])
print(students)

students.sort(key=lambda x: x['name'], reverse=True)
print(students)
