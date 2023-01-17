print('这里是公共操作')

print('首先是运算符')
print('+ * in nin')
print('支持的类型分别为：')
print('+ : string list tuple')
print('* : string list tuple')
print('in : string list tuple dict')
print('not in : string list tuple dict')

str1 = 'Alkaid'
str2 = '#3529'

list1 = [10, 20, 30]
list2 = [40, 50, 60]

tuple1 = (10, 20, 30)
tuple2 = (30, 40, 50)

dict1 = {'name': 'bob', 'age': 20, 'gender': '男'}
dict2 = {'name': 'andy', 'age': 19, 'gender': '女'}

print('')

# + : 合并
print(str1 + str2)
print(list1 + list2)
print(tuple1 + tuple2)

# 字典不支持合并运算，报错
# print(dict1 + dict2)

print('')

# * : 复制
print(str1 * 1)
print('-' * 10)
print(list1 * 2)
print(tuple1 * 3)

# 字典不支持复制，报错
# print(dict1 * 1)

print('')

# in : 判断是否存在
print('A' in str1)
print('3' in str1)
print('A' in str2)
print('3' in str2)

print(10 in list2)
print(30 in list1)

print(10 in tuple1)
print(40 in tuple1)
print(40 in tuple2)

print('name' in dict1)
print('name' in dict1.keys())
print('bob' in dict1.values())

# not in : 判断是否不存在
print('A' not in str1)
print('3' not in str1)
print('A' not in str2)
print('3' not in str2)

print(10 not in list2)
print(30 not in list1)

print(10 not in tuple1)
print(40 not in tuple1)
print(40 not in tuple2)

print('name' not in dict1)
print('name' in dict1.keys())
print('bob' not in dict1.values())
print('andy' not in dict2)

print('')

print('这里是公共方法')

# len() 返回容器中元素的个数
print(str1)
print(len(str1))

print(list1)
print(len(list1))

print(tuple1)
print(len(tuple1))

print(dict1)
print(len(dict1))

# del() 删除指定数据
print(str1)
# del str1
# 报错
# print(str1)

print(list1)
del list1[2]
print(list1)

print(tuple1)
# 不可修改，报错
# del tuple1[1]

print(dict1)
del dict1['name']
print(dict1)

# max() 返回容器中的最大值
str1 = 'Alkaid'
print(str1)
print(max(str1))

list1 = [10, 20, 30]
print(list1)
print(max(list1))

tuple1 = (10, 20, 30)
print(tuple1)
print(max(tuple1))

dict1 = {'name': 'bob', 'age': 20, 'gender': '男'}
print(dict1)
print(max(dict1))

# min() 返回容器中的最小值
str1 = 'Alkaid'
print(str1)
print(min(str1))

list1 = [10, 20, 30]
print(list1)
print(min(list1))

tuple1 = (10, 20, 30)
print(tuple1)
print(min(tuple1))

dict1 = {'name': 'bob', 'age': 20, 'gender': '男'}
print(dict1)
print(min(dict1))

print('')

# range(start, end, step) 生成从 start 到 end 的数字，步长为 step ，可以迭代的对象，供 for 遍历
# 包含 start ，不包含 end

print(range(1, 20, 5))

for i in range(1, 10):
    print(f'{i} ', end='')
else:
    print('遍历完成')

for i in range(1, 20, 2):
    print(f'{i} ', end='')
else:
    print('遍历完成')

for i in range(1, 20, 5):
    print(f'{i} ', end='')
else:
    print('遍历完成')

for i in range(20):
    print(f'{i} ', end='')
else:
    print('遍历完成')

print('')

# enumerate(可遍历对象, start=0) start 用于设置下标起始值，默认为 0
list1 = ['a', 'b', 'c', 'd', 'e', 'f']
print(enumerate(list1))

# 组合为一个索引序列，同时列出数据下标与数据，多用于 for 循环
for i in enumerate(list1):
    print(i, end='')
else:
    print('遍历完成')

for i in enumerate(list1, start=1):
    print(i, end='')
else:
    print('遍历完成')

print('')

print('这里是容器类型转换')

list1 = [10, 20, 30]
tuple1 = (10, 20, 30)
set1 = {10, 20, 30}

# tuple()
print('tuple():')
print(tuple(list1))
print(tuple(set1))
print(tuple(tuple1))

# list()
print('list():')
print(list(list1))
print(list(set1))
print(list(tuple1))

# sets34()
print('sets34():')
print(set(list1))
print(set(set1))
print(set(tuple1))
