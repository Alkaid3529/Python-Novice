# 函数进一步学习
print('这里是函数的进一步学习')

print('首先是全局变量和局部变量')

num = 100


def test01():
    # a 只是函数体内部临时保存数据的局部变量，函数调用完成后立即释放
    a = 100
    print(a)
    # num 是全局变量，可以在任意位置访问，程序运行结束后才会被释放
    print(num)


def test02():
    # 此时 num 是局部变量
    # num = 200

    # 关键字声明 修改全局变量
    global num
    num = 30
    print(num)


# num 是全局变量
test01()
test02()

# 报错，a 是 test 中的局部变量
# print(a)

print('')

print('多函数执行流程')

# 定义全局变量
g_a = 100

# 当一个函数修改全局变量后，后面的函数访问该全局变量时将会访问被修改后的值

# 函数返回值可以作为参数传递

# 函数返回值字可以返回多个值，默认返回元祖

print('')


def test03():
    return 1, 2


t1 = test03()
print(t1)
print(type(t1))

# return 可以连接返回各种数据类型：列表，元组，字典


def test04():
    """
    返回一个列表
    :return:
    """
    return [10, 20]


def test05():
    """
    默认返回一个元组
    :return:
    """
    return 10, 20


def test06():
    """
    返回一个字典
    :return:
    """
    return {'name': 'bob', 'age': 18}


list1 = test04()
t1 = test05()
dict1 = test06()

print(list1)
print(type(list1))
help(test04)

print(t1)
print(type(t1))
help(test05)

print(dict1)
print(type(dict1))
help(test06)

print('这里是函数参数')

# 位置参数：参数的定义与传入数量、顺序必须一致
print('首先是位置参数')

print('这里是关键字参数')


def print_person(name, age, gender='man'):
    print(f'name = {name}, age = {age}, gender = {gender}')


# 位置参数按顺序传入
print_person('bob', 20, 'man')

# 关键字参数传入可以不按照顺序
print_person(name='andy', gender='women', age=25)

# 位置参数必须在关键词字数前
print_person('andy', gender='women', age=25)

print('这里是缺省参数')

# 定义函数时参数列表中的参数有默认值，但是默认参数必须位于参数列表末尾
print_person('bob', 20)
print_person('bob', 20, 'woman')

print('这里是不定长参数')

# 不定长参数也叫可变参数，用于不确定调用是传递参数的数量的情况
# 有两种方式：包裹位置参数，包裹关键字参数


def test07(*args):
    """
    包裹位置参数，可传入任意数量的参数
    :param args: 将传入的参数合并为一个元组
    :return:
    """
    print(args)


test07('bob', 18, 'man')
test07('bob', 18)
test07('bob', 18, 'man', 2052152)
test07()


def test08(**kwargs):
    """
    包裹关键字参数，可传入任意数量的键值对
    :param kwargs: 将传入的参数合并为一个字典
    :return:
    """
    print(kwargs)


test08(name='bob', age=26, gender='man')
test08(name='bob', age=26)
test08(name='bob', age=26, gender='man', id='2052152')
test08()

# 组包：将零散数据整合为一个整体

print('')

print('这里是拆包')

print('首先是元组拆包')
a, b = test05()
print(test05())
print(a)
print(b)

print('这里是字典拆包')
# 获得字典的键值
a, b = test06()
print(test06())
print(a)
print(b)
print(dict1[a])
print(dict1[b])
