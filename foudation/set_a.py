print('这里是集合')

# 创建集合
s1 = {10, 20, 30, 40, 50, 60}
print(s1)
print(type(s1))

# 集合无顺序，不支持下标
s2 = {10, 20, 30, 40, 30, 20, 30, 10}

# 集合内无重复数据，自动去重
print(s2)
print(type(s2))

# 自动转换为单个元素，无顺序
s3 = set('Alkaid#35295')
print(s3)
print(type(s3))

# 创建空集合 sets34()
s4 = set()
print(s4)
print(type(s4))

# 创建空集合 ()
s5 = ()
print(s5)
print(type(s5))

# {}用于创建空字典
s6 = {}
print(s6)
print(type(s6))

print('')

print('集合常见操作')

print('首先是增加数据')
s1 = {10, 20, 30}

# add() 增加单个数据至随机位置
s1.add(100)
print(s1)

# 自动去重
s1.add(20)
print(s1)

# 不可追加数据序列，报错
# s1.add([10, 20, 30])

# update() 增加一个序列
s1.update([10, 20, 30, 50])
print(s1)

# 不可追加单个数据，报错
# s1.update(100)

print('')

print('这里是集合的删除操作')

# remove() 删除指定数据，不存在则报错
s1 = {10, 20, 30, 40, 50, 60}
print(s1)
s1.remove(10)
print(s1)

# 不存在，报错
# s1.remove(100)

# discard()
s1 = {10, 20, 30, 40, 50, 60}
print(s1)
s1.discard(10)
print(s1)

# 不存在，不报错
s1.discard(10)
print(s1)

# pop() 随即删除某个数据，并返回这个数据
print(s1)
del_num = s1.pop()
print(s1)
print(del_num)

print('')

print('这里是集合查找操作')
s1 = {10, 20, 30, 40, 50, 60}

# in
print(100 in s1)
print(10 in s1)

# not in
print(100 not in s1)
print(10 not in s1)
