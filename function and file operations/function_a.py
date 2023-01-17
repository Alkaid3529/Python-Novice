# 函数：一段具有独立功能的代码块，高效代码重用
# 函数必须先定义，再调用
print('这里是函数')

# 独立书写，上下各空两行


def calculator_a(a, b, str1):
    """
    真是太好用了
    :param a: 参数一
    :param b: 参数二
    :param str1: 指定运算
    :return: 运算结果
    """
    if str1 == '+':
        return a + b
    elif str1 == '-':
        return a - b
    elif str1 == '*':
        return a * b
    elif str1 == '/':
        return a / b
    elif str1 == '_':
        return (a + b) / 2


print(calculator_a(10, 20, '+'))
print(calculator_a(10, 20, '-'))
print(calculator_a(10, 20, '*'))
print(calculator_a(10, 20, '/'))
print(calculator_a(10, 20, '_'))

# help() 查看函数说明文档
help(calculator_a)
