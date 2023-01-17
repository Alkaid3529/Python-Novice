# 引用
print('这里是引用')

# 在 python 中，值是依靠引用传递的
# a 是存储数据1的地址的名字
a = 1

# a 的值赋给 b 后，两个变量指向同一块地址
b = a
c = 10
print(a)
print(b)
print(c)

# int 不可变类型，修改值后地址也改变

print(id(a))
print(id(b))
print(id(c))

a = 2
print(id(a))
print(b)

b = 10
print(a)
print(b)

print(id(a))
print(id(b))
print(id(c))

print('')

# 列表，可变类型，修改后地址不变

aa = [10, 20, 30]
bb = aa
print(id(aa))
print(id(bb))

aa.append(40)
print(aa)
print(bb)

print(id(aa))
print(id(bb))

print('')


# 引用做实参传递
def test01(num):
    num += 1
    print(num)
    print(id(num))


a = 10
print(a)
print(id(a))

# 形参传入，调用后原值不变，形参地址改变
test01(a)

print(a)
print(id(a))


def test02(list1):
    list1.append(10)
    print(list1)
    print(id(list1))


list2 = [10, 20, 30]
print(list2)
print(id(list2))

# 实参传入，调用后原值改变，但地址始终不变
test02(list2)

print(list2)
print(id(list2))

# 可变类型：列表，字典，集合
# 不可变类型：int float string tuple
