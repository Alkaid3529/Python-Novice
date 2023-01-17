# 用一个变量去接收input的结果
# password = input('请输入你的密码：')

def calculate(x1, y1, x2, y2, x0, y0):
    k = (y2 - y1) / (x2 - x1)

    b = y0 - k * x0
    print(f'x0 = {x0}, y0 = {y0}, b = {b}')


x = [0.02, 0.04, 0.06, 0.09, 0.12, 0.16, 0.20, 0.24]
y = [0.06693, 0.06301, 0.06105, 0.05609, 0.05388, 0.04984, 0.04749, 0.04475]

for i in range(0, 6):
    calculate(x[i], y[i], x[i + 2], y[i + 2], x[i + 1], y[i + 1])

'''
将接收的数据全部当作字符处理
存储在变量中方便用户查找
运行到此时，等待用户输入

print(f'你输入的密码为：{password}')
print(f'你输入的密码数据类型为：{type(password)}')

强制转换为int整型数据

# password1 = int(input('请再次输入你的密码：'))
print(f'你输入的密码数据类型为：{type(password1)}')
'''

print('数据类型转换')

# float()
num1 = 1
print(type(num1))
print(type(float(num1)))

str1 = '10'
# str1 = 'Alkaid#3529' 此时不可转换
print(type(str1))
print(type(float(str1)))

# str()
print(type(num1))
print(str(num1))
print(type(str(num1)))

# tuple 转换为元组
list1 = [10, 20, 30]
print(type(list1))
print(tuple(list1))
print(type(tuple(list1)))

# list 转换为列表
t1 = (10, 20, 30)
print(type(t1))
print(list(t1))
print(type(list(t1)))

# eval 计算字符串中的有效表达式，并返回一个对象，把字符串转换为原有数据类型
str1 = '(10, 20, 30)'
str2 = '[10, 20, 30]'
str3 = '1'

print(eval(str1))
print(type(eval(str1)))
print(eval(str2))
print(type(eval(str2)))
print(eval(str2))
print(type(eval(str2)))
