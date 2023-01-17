# 包
# 包含很多相关联的模块的文件夹，称为包
# 并在这个文件夹下创建一个 __init__.py 文件

# 必须在 __init__.py 中利用 __all__ = [] 控制允许导入的模块
from mypackage import *
my_module1.print_a()

# 未导入
# my_module2.print_b()

# 全部导入
import mypackage.my_module2
mypackage.my_module2.print_b()
