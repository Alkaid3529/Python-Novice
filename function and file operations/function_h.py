import functools

# 高阶函数
print('This is Higher-order functions')

# abs()
print(abs(-19))
print(abs(19))

# round()
print(round(1.5))
print(round(1.6))
print(round(1.4))


def abs_sum(a, b):
    return abs(a) + abs(b)


def round_sum(a, b):
    return round(a) + round(b)


print(abs_sum(-10, 20))
print(round_sum(2.5, 3.1))


# 高阶函数 函数式编程
def sum_p(a, b, f):
    return f(a) + f(b)


print(sum_p(-10, 20, abs))
print(sum_p(1.6, 2.1, round))


# 内置高阶函数

# map(func, list) 返回迭代器
def func_power(a):
    return a * a


list1 = [1, 2, 3, 4, 5]

list1_pans = map(func_power, list1)
print(list1_pans)
print(list(list1_pans))


# reduce(func, list) func必须有两个参数 返回计算结果
def func_sum(a, b):
    return a + b


list1_sans = functools.reduce(func_sum, list1)
print(list1_sans)

# filter() 过滤不符合条件的函数 返回 filter 对象
list1 = [1, 2, 3, 4, 5, 6]


def func_filter(a):
    return a % 2 == 0


list1_fans = filter(func_filter, list1)
print(list1_fans)
print(list(list1_fans))
