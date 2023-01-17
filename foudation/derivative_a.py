# 减少代码量
print('这里是推导式，也叫生成式')
print('仅适用于列表、字典、集合')
print('推导式可以有效缩减代码量')

print('')

print('首先是列表推导式')
print('用一个表达式创建一个有规律的列表或者控制一个有规律的列表')

list1 = []
for i in range(0, 10):
    list1.append(i)
else:
    print('赋值完毕')

for i in list1:
    print(i, end=' ')
else:
    print('输出完毕')

# 列表推导式
list1 = [i for i in range(9)]

for i in list1:
    print(i, end=' ')
else:
    print('输出完毕')

print('')

print('这里是带 if 的列表推导式')

# list1 = [i for i in range(0, 10, 2)]
list1 = [i for i in range(0, 10) if i % 2 == 0]
print(list1)

# 多个 for 循环实现列表推导式
# 等价于 for 循环嵌套
list1 = [(i, j) for i in range(3) for j in range(2)]
print(list1)

print('')

print('这里是字典推导式')
list1 = ['name', 'age', 'gender']
list2 = ['bob', 20, 'man']

dict1 = {i: j for i in list1 for j in list2}
print(dict1)

dict2 = {i: i**2 for i in range(1, 5)}
print(dict2)

dict1.clear()
dict1 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict1)

list1 = ['bob', 'andy', 'julie', 'gorge', 'cat']
list2 = [90, 70, 80, 50, 60]

dict1 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict1)

dict2 = {key: value for key, value in dict1.items() if value >= 60}
print(dict2)

print('')

print('这里是集合推导式')

list1 = [1, 2, 3, 4, 5]
s1 = {i*i for i in list1}
print(s1)
