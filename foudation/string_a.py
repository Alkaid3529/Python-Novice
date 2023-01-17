# 字符串学习
print('这里是字符串,是 python 中最常用的数据类型')

'''
input 接收的数据默认为 string 类型
获取的数据基本全部为 string 类型
'''

a = 'hello python'
print(a)
print(type(a))

b = "hello python"
print(b)
print(type(b))

c = '''hello python'''
print(c)
print(type(c))

d = """hello python"""
print(d)
print(type(d))

a = 'hello ' \
    'python'
print(a)
print(type(a))

b = "hello " \
    "python"
print(b)
print(type(b))

c = '''hello 
python'''
print(c)
print(type(c))

d = """hello 
python"""
print(d)
print(type(d))

# e = 'I'm Alkaid'
# e = 'I\'m Alkaid'
e = "I'm Alkaid"
print(e)
print(type(e))

name = 'Alkaid'
print('我的名字是%s' % name)
print(f'我的名字是{name}')

# password = input('请输入你的密码')
password = '08112012lzy'
print('您的密码是%s' % password)
print(f'您的密码类型是{type(password)}')

# input 接收的数据均为 str

print('')

print('这里是字符串下标 索引 索引值')
name = 'Alkaid#3529'
num = 0
while num < 5:
    print(name[num], end='')
    num += 1
else:
    print('\n名字输出完毕')

print('')

print('这里是切片，用于获取字符串中某些数据')
name = 'Alkaid#3529'
print(type(name[2]))

'''
切片的语法：
序列[开始位置下标:结束位置下标:步长]
区间范围左闭右开,切正负数均可
步长默认为1
'''

print('体验一下切片')
name = 'Alkaid#3529'

# 从 2 开始，下标递增 1，且不包括下表为 5 的字符
print(name[2:5:1])

# 从 2 开始，下标递增 2，且不包括下表为 6 的字符
print(name[2:6:2])

# 步长默认为 1
print(name[2:5])

# 起始下标默认从 0 开始，下标递增 1 ，且不包括下表为 5 的字符
print(name[:5])

# 起始下标默认从 0 开始，结束下标默认为最后
print(name[:])

# 步长为负数，表示倒序选取
print(name[::-1])

# 区间左值小于或等于右值且步长为 1 无意义，输出为空
print(name[-1:-4])

# 区间左值小于或等于右值但步长为 -1 ，有意义
print(name[-1:-4:-1])

# 区间方向与步长方向应统一
print(name[-1:-10:-2])

print('')

print('这里是字符串常用操作方法')
print('常用的操作方法主要有查找、修改、判断三大类')

print('首先是字符串查找操作')

name = 'Alkaid#3529'

# 查找子串，若有返回下标，否则返回 -1
# 字符串序列.find(查找的子串，开始下标，结束下标)
# 开始和结束的下标默认为起始和结束
print(name.find('ai'))
print(name.find('ai', 3, 9))
print(name.find('ai', 4, 9))

# 仅查找有无，不检查始末范围
print(name.find('ai', 20, 20))

print(name.find('a'))
print(name.find('b'))

print(name[name.find('3')::])

print(name.index('a'))

# 报错
# print(name.index('b'))

# count 返回子串出现的次数，若无，返回 0
print(name.count('a'))
print(name.count('i'))

# rfind rindex 查找方向为从右侧开始
print(name.rfind('ai'))
print(name.rindex('a'))

print('')

print('现在是字符串修改操作')

print('')

print('首先是替换操作')

# .replace(旧子串, 新子串, 替换次数默认全部替换)
str1 = 'Hello World and Python and Pycharm'

# 不会修改原字符串，原字符串以形参形式传入，返回值为修改后的字符串
# 字符串是常量 const
str1.replace('and', '&')
new_str1 = str1.replace('and', '&')

# 若想修改，可以重新赋值
# str1 = str1.replace('and', '&')

print(str1)
print(str1.replace('and', '&'))
print(str1.replace('and', '&', 1))

# 次数超出子串出现的次数，默认全部替换
print(str1.replace('and', '&', 10))

print(new_str1)

print('')

print('现在是分割操作')

# split 将字符串按照子串分割为一个列表，并返回这个列表，舍弃出现的子串
# .split(旧子串,分割次数默认全部替换)
print(str1.split('and'))
print(str1.split('and', 1))

print('')

print('现在是拼接操作')

# join 将序列里的若干字符串合并为一个大的字符串，并返回这个字符串
list1 = str1.split('and')
print(list1)
str2 = 'and'.join(list1)
print(str2)

print('')

print('现在是一些基本的字符串操作函数')

# capitalize 将字符串第一个字母转为大写，其余均转为小写
print(str1)
print(str1.capitalize())

# title 将字符串中每个单词首字母转大写
print(str1)
print(str1.title())

# lower 大写转小写
print(str1)
print(str1.lower())

# upper 小写转大写
print(str1)
print(str1.upper())

str2 = '   Hello World and Python and Pycharm   '

# lstrip 删除字符串左侧空白
print(str2)
print(str2.lstrip())

# rstrisp 删除字符串右侧空白
print(str2)
print(str2.rstrip())

# strip 删除两侧空白
print(str2)
print(str2.strip())

str3 = 'hello world'

# ljust 左对齐，用指定字符补齐
print(str3)
print(str3.ljust(20, '.'))

# rjust 右对齐，用指定字符补齐
print(str3)
print(str3.rjust(20))  # 默认空格填充
print(str3.rjust(20, '.'))

# center 居中对齐，用指定字符补齐
print(str3)
print(str3.center(20, '.'))
print(str3.center(20))  # 默认空格填充

print('')

print('现在是字符串判断操作')

# 字符串序列.startswith(子串，开始位置下标，结束位置下标)
print(str1)
print(str1.startswith('H'))  # 默认开始至结尾
print(str1.startswith('h'))  # 区分大小写
print(str1.startswith('He', 1, 10))
print(str1.startswith('Hello'))

# 字符串序列.endswith(子串，开始位置下标，结束位置下标)
print(str1)
print(str1.endswith('m'))  # 默认开始至结尾
print(str1.endswith('arm'))
print(str1.endswith('arms'))
print(str1.endswith('mra'))  # 注意方向

'''
.isalpha 判断非空字符串是否全为字母
.isdigit 判断非空字符串是否全为数字
.isalnum 判断非空字符串是否全为数字和字母
.isspace 判断字符串是否全为空格
'''

str1 = '1234567890'
str2 = 'qazwsxedc'
str3 = '12345qwer'
str4 = '         '

print(str1)
print(str1.isalpha())
print(str1.isdigit())
print(str1.isalnum())
print(str1.isspace())

print('')

print(str2)
print(str2.isalpha())
print(str2.isdigit())
print(str2.isalnum())
print(str2.isspace())

print('')

print(str3)
print(str3.isalpha())
print(str3.isdigit())
print(str3.isalnum())
print(str3.isspace())

print('')

print(str4)
print(str4.isalpha())
print(str4.isdigit())
print(str4.isalnum())
print(str4.isspace())
