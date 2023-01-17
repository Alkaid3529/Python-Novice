# 模块
print('this is module')

'''
了解模块
导入模块
制作模块
__all__
包的使用
'''

# 模块本质是一个 python 文件
# 导入模块的方式

# import 模块名
import math
# 需添加模块名前缀
print(math.sqrt(9))

# from 模块名 import 功能名
from math import sqrt
# 可直接使用功能
print(sqrt(9))

# from 模块名 import *
from math import *
print(sqrt(9))

# as 别名
# import 模块名 as 别名
# from 模块名 import 功能 as 别名

# 定义别名后，只能使用别名
import time as tt
tt.sleep(2)
print('hello')

from time import sleep as sl
sl(2)
print('hello')

print('')

# 制作模块

# 导入模块时自动执行模块内部全部代码
from four_operations import *

print(addition(10, 20))
print(subtraction(20, 10))
print(multiplication(10, 20))
print(division(20, 10))


# 模块定位顺序
"""
当前目录：当前 python 文件所在文件夹
在 shell 变量 PYTHONPATH 下的每个目录
默认路径
"""

"""
自己文件名不可与已有文件名重复，否则无法调用相应功能
from module import function 调用重名功能时，调用最后定义或导入的功能
"""

# 名字重复问题极大
import time
print(time)

time = 1
print(time)

# 为什么变量可以覆盖模块功能
# sleep(2)
# 引用传递

# __all__ 列表
# 限制特定方式导入模块时导入的功能
# 减少不必要的函数调用

# four_operations
# print(secret())
