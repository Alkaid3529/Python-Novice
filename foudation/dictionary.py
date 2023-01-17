# 字典可以用于存储多个数据，数据类型可以不同
print('这里是字典')

# 字典创建：大括号，键值对，逗号隔开
dict1 = {'name': 'bob', 'age': 18, 'gender': '男'}
print(dict1['name'])
print(dict1['age'])
print(dict1['gender'])
print(type(dict1))
print(dict1)

dict2 = dict1
dict2['name'] = 'andy'
print(dict2)

print('')

print('这里是字典的常用操作')

print('这里是字典修改与新增操作')

# 若有该键值，则修改
dict2['name'] = 'cat'
print(dict2)

# 若无该键值，则新增
dict2['id'] = 2052152
print(dict2)

print('')

print('这里是字典删除数据操作')

# del 删除指定键值
del(dict2['gender'])
del dict2['id']
print(dict2)
print(dict1)

# clear 清空字典
dict3 = dict1
print(dict3)
dict3.clear()
print(dict3)

print('')

print('这里是字典查找操作')

# 根据 key 值查找
dict1 = {'name': 'bob', 'age': 18, 'gender': '男'}

# 循环输出
for i in dict1:
    print(f'{i} : {dict1[i]}')

# 查找 key，若无，返回 none 或 指定参数2
print(dict1.get('names'))
print(dict1.get('names', 0))

# keys 查找字典中所有的 keys，返回全部可迭代对象
print(dict1.keys())

for i in dict1.keys():
    print(i, end=' ')

print('')

# values 查找字典当中全部值，返回可迭代对象
print(dict1.values())

for i in dict1.values():
    print(i, end=' ')

print('')

# items 查找全部键值对，返回可迭代对象
print(dict1.items())

for i in dict1.items():
    print(i, end=' ')

print('')

