# 包含四则运算

# __all__ 列表
__all__ = ['addition', 'subtraction', 'multiplication', 'division']


def addition(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    return a + b


def subtraction(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    return a - b


def multiplication(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    return a * b


def division(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    return a / b


def test(a, b):
    print(addition(a, b))
    print(subtraction(a, b))
    print(multiplication(a, b))
    print(division(a, b))


def secret():
    return 'this is secret'


print(__name__)

# 测试信息
if __name__ == '__main__':
    test(20, 10)

if __name__ == 'four_operations':
    print('-------------------')
