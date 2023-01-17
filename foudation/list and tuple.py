import random

print('这里是列表')

'''
列表的应用场景
列表的格式
列表的常用操作
列表的循环遍历
列表的嵌套使用
'''

# 列表可以一次性存储多个数据
print('这里是列表的书写格式')

# 列表存储的数据可以是不同的数据类型，但最好存储相同的数据类型
name_list = ['tom', 'bob', 'jack', 'allie']

print(name_list)

i = 0
while i < 3:
    print(name_list[i])
    i += 1
else:
    print('名字输出完毕')

print('这里是列表查找函数')

name_list = ['tom', 'bob', 'jack', 'allie', 'bob', 'jack', 'bob']

# 默认全列表查找
print(name_list.index('bob'))

# 未找到，即报错
# print(name_list.index('bob', 2, 3))

print(name_list.index('bob', 1, 3))

# count 统计出现的次数
print(name_list.count('bob'))
print(name_list.count('jack'))
print(name_list.count('name'))

# len访问列表长度
print(len(name_list))

print('')

print('这里是列表判断存在函数')

# 判断列表中是否存在
print('bob' in name_list)
print('bo' in name_list)

# 判断列表中是否不存在
print('bob' not in name_list)
print('bo' not in name_list)

name_list = ['tom', 'bob', 'jack', 'allie', 'bob', 'jack', 'bob']
name1 = 'Alkaid'

print(name_list)

name_list = ['tom', 'bob', 'jack', 'allie', 'bob', 'jack', 'bob', name1]

# 列表中元素也可以包括变量
print(name_list.index('Alkaid'))
print('Alkaid' in name_list)

name_find = input('请输入你要查找的名字')

if name_find in name_list:
    print(f'你要查找的名字{name_find}在第{name_list.index(name_find)}位')
else:
    print(f'你要查找的名字{name_find}不存在')

print('')

print('这里是列表增加元素函数')

# append() 在列表末尾追加数据
# 地址传递，会修改原列表
name_list = ['tom', 'bob', 'jack', 'allie', 'bob', 'jack', 'bob']
print(name_list)

name_add = input('请输入您想要增加的名字')
name_list.append(name_add)

print(name_list)

print('')

# 若 append() 追加的数据是一个列表，则会将整个列表仍以列表形式追加在原列表的结尾
name_list = ['tom', 'bob', 'jack', 'allie', 'bob', 'jack', 'bob']
list_add = ['jack', 'allie']

print(name_list)
print(list_add)

name_list.append(list_add)
print(name_list)

print('')

# extend 列表结尾追加数据，若追加的数据为字符串，则将字符串的每个字符逐一添加至列表结尾，若追加的数据为列表，则将列表内的数据逐一添加至原列表结尾
name_list = ['tom', 'bob', 'jack', 'allie', 'bob', 'jack', 'bob']
list_add = ['jack', 'allie']
name_add = 'Alkaid'

print(name_list)
print(list_add)
print(name_add)

name_list.extend(name_add)
print(name_list)

name_list = ['tom', 'bob', 'jack', 'allie', 'bob', 'jack', 'bob']
name_list.extend(list_add)
print(name_list)

print('')

# insert 在指定位置插入数据,若数据类型为列表，则在指定位置插入整个列表
name_list = ['tom', 'bob', 'jack', 'allie', 'bob', 'jack', 'bob']
name_add = 'Alkaid'

name_list.insert(2, name_add)
print(name_list)

name_list = ['tom', 'bob', 'jack', 'allie', 'bob', 'jack', 'bob']
name_list.insert(2, list_add)
print(name_list)

print('')

# del name_list 直接删除整个列表
# print(name_list)

name_list = ['tom', 'bob', 'jack', 'allie', 'bob', 'jack', 'bob']
print(name_list)
del name_list[0]
print(name_list)

# pop 删除指定下标的数据，默认删除最后一个数据并返回该数据
name_list = ['tom', 'bob', 'jack', 'allie', 'bob', 'jack', 'bob']
print(name_list)

# 默认删除最后一个
print(name_list.pop())
print(name_list.pop(2))
print(name_list)

# remove 删除指定数据
name_list = ['tom', 'bob', 'jack', 'allie', 'bob', 'jack', 'bob']
name_list.remove('bob')
print(name_list)

# clear 清空列表
name_list.clear()
print(name_list)

# reverse 元素逆置
name_list = ['tom', 'bob', 'jack', 'allie', 'bob', 'jack', 'bob']
print(name_list)
name_list.reverse()
print(name_list)

# sort 将列表排序
num_list = [1, 3, 9, 4, 6, 2, 8, 5]
print(num_list)
num_list.sort(key=None, reverse=True)
print(num_list)
num_list.sort(key=None, reverse=False)
print(num_list)

# 若列表中存储数据为字符串，则按首字母ASCII码进行排序
name_list = ['tom', 'bob', 'jack', 'allie', 'bob', 'jack', 'bob', 'cat', 'dog', 'Alkaid', ' ']
name_list.sort(reverse=True)
print(name_list)

# copy 将已有列表复制到新地列表中
name_list1 = name_list.copy()
print(name_list)
print(name_list1)

# 列表循环遍历

i = 0
while i < len(name_list):
    print(name_list[i], end='  ')
    i += 1
else:
    print('name_list 输出完毕')

for i in name_list:
    print(i, end='  ')
else:
    print('name_list 输出完毕')

# 列表嵌套
name_list = [['小明', '小红', '小强'], ['tom', 'bob', 'andy'], ['喜羊羊', '沸羊羊', '美羊羊']]

i = 0
while i < 3:
    j = 0
    while j < 3:
        print(name_list[i][j], end='  ')
        j += 1
    print(f'第{i}组输出完毕')
    i += 1
else:
    print('name_list 输出完毕')

print('')

print('随机分配老师')
teacher_list = ['teacher0', 'teacher1', 'teacher2', 'teacher3', 'teacher4', 'teacher5', 'teacher6', 'teacher7']

office_list = [[], [], []]

i = 0
while i < 8:
    office_list[random.randint(0, 2)].append(teacher_list[i])
    i += 1
else:
    print('老师分配完毕')

i = 0
while i < 3:
    print(f'这间办公室的老师有{len(office_list[i])}个')
    for name in office_list[i]:
        print(name, end='  ')
    print(f'第{i}间办公室输出完毕')
    i += 1
else:
    print('全部办公室输出完毕')

print('')

print('this is summary')
print('列表常存储同类型数据，有多种操作函数')
print('index len append pop remove clear')
print('列表嵌套，即多维列表')

print('')

# 元组与列表属性相同，但是元组中的数据无法修改
print('这里是元组')

# 多个数据元组
t1 = (10, 20, 30)

# 单个数据元组，必须有逗号
t2 = (10,)
# t3 = (10) 类型为 int
# print(type(t3))

print(t1)
print(type(t1))
print(type(t2))

# 元组的常见操作，仅有查找，不可修改
print('这里是元组的常见操作：查找')

t1 = ('tom', 'bob', 'jack', 'allie', 'bob', 'jack', 'bob', 'cat', 'dog', 'Alkaid', ' ')

print(t1)
print(type(t1))

for i in t1:
    print(i, end='  ')
else:
    print('元组输出完毕')

# index 查找数据
# print(t1.index('andy')) 报错
print(t1.index('bob'))

# count 统计数据出现次数
print(t1.count('bob'))
print(t1.count(' '))
print(t1.count('  '))

# len 统计元组长度
print(len(t1))

# 元组的修改
print('如何修改元组里的元素？')
print('不要修改元组里的数据')
