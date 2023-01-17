# 交换变量值
print('这里是交换变量值')

# method_1 通过第三方变量交换
a = 10
b = 20
print(a)
print(b)

mid = a

a = b
b = mid
print(a)
print(b)

# method_2
a, b = 1, 2
print(a)
print(b)

a, b = b, a
print(a)
print(b)
