# 文件操作
print('This is file')

# 文件基本操作
# 打开文件，读写，关闭文件

print('first open file')

# open(name, mode) name: 文件名  mode: 打开模式
f = open('test.txt', 'w')

# write() read()
f.write('hello python\n')
f.write('hello pycharm')

# .close()
print('remember to close file')
f.close()

# 主访问模式
# w r a
# 只读 只写 追加

# 不同访问模式对文件的影响
# 访问模式对 write 的影响
# 访问模式能否省略

# r 只能读存在的文件
# f = open('test1.txt', 'r') 报错
f = open('test.txt', 'r')

# f.write('aaa') 报错，不支持写入
f.close()

# w
# 若打开文件不存在，则新建
f = open('test1.txt', 'w')
# 写入时会覆盖原有内容
f.write('hello python ii')
f.close()

# a 追加
# 若打开文件不存在，则新建
f = open('test2.txt', 'a')

# 在结尾追加内容
f.write('hello python\n')
f.write('hello python\n')
f.write('hello python\n')
f.close()

# 访问模式默认'r'
f = open('test.txt')
f.close()

# 文件读取
# .read(num) num: 读取单位长度，默认全部

f = open('test.txt', 'r')

# 换行也会占一个字节

print(f.read(3))
print(f.read(3))
print(f.read(3))
print(f.read(3))

f.close()

# readlines() 以行的方式读取整个文件，返回一个列表，每一行数据为一个元素
f = open('test.txt', 'r')
print(f.readlines())

f.close()

# readline() 单次读取单行内容
f = open('test.txt', 'r')

print(f'first line: {f.readline()}', end='')
print(f'second line: {f.readline()}')

# 读取完后不再有结果
print(f'third line: {f.readline()}')

f.close()

print('')

# b 表示以二进制操作
# + 表示可读可写

# 文件指针相当于光标位置

# 访问模式的特点 文件指针对数据的一些
print('This is Access mode')

print('')

print('first r+')
# 可读可写，但只能操作现有文件，无法新建文件
f = open('test.txt', 'r+')
print(f.read())

f.close()

print('')

# w 访问模式，每次打开文件会覆盖原有文件
print('then w+')
f = open('test.txt', 'w+')
print(f.read())

f.close()

print('')

# a 访问模式，文件指针默认在文件结尾
print('next a+')
f = open('test1.txt', 'a+')
print(f.read())

f.close()

print('')

print('this is seek')
# seek() 移动文件指针
# seek(offset, position)
# 0: 文件开头
# 1: 当前位置
# 2: 文件结尾

f = open('test1.txt', 'r+')
# f.seek(0, 2)
print(f.read())
f.close()

print('')

f = open('test1.txt', 'a+')
f.seek(0, 0)
print(f.read())
f.close()

print('')

print('this is file backs')

# 数据备份，后缀
# 备份文件名字必须加后缀

# 接收文件名
# 规划备份文件名
# 备份文件写入数据

# 用户输入备份文件
name_file = input("please input back_file's name: ")

# 规划备份文件名
position = name_file.rfind('.')
print(position)

# 备份文件写入数据
