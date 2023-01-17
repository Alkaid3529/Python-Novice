print('这里是运算符')
'''
运算符
算数，逻辑，赋值，比较，复合赋值
五类运算符
'''

print('五种运算符分别为：算数，逻辑，赋值，比较，复合赋值')

print('首先是算术运算符：')
print('+  -  * /  //  %  **   ()')
print('加 减 乘 除 整除 模 指数 小括号')
print('优先级依次递增')

# 自动转换为float
print(2 * 0.5 // 2)

# 默认为float
print(4 / 2)
print(9 / 4)

# 指数运算
print(2 ** 3)

# ’**‘优先级高于’*‘
print(2 * 3 ** 2)
print((2 * 3) ** 2)

print('这里是赋值运算符：')

# 多个变量赋值 按顺序依次赋值，一一对应
num1, f1, str1 = 10, 2.5, 'Alkaid'
print(num1, f1, str1)

# 多个变量赋相同的值
a = b = c = d = 10
# e = 100 = f
print(a, b, c, d)

print('这里是复合赋值运算符：')
print('其实就是算术运算符和赋值运算符的结合，计算后将计算结果复制给原数')
print('+=  -=  *=  /=  //=  %=  **=')
print(f'a = {a}, a += 1')
a += 1
print(f'a = {a}')

c += 1 + 2
print(c)
'''
究竟是
c = 10 + 1 +2
c += 3, c = c + 3
'''

d *= 1 + 2
print(d)
'''
d = 30
验证可得，'+'优先级高于'+='
'''

print('这里是比较运算符：')
print('> < >= <= != ==')

print(c < d)
print(int(c < d))
print(c != d)

# 非零为真零为假
print(bool(3))

print('这里是逻辑运算符：')
print('and or not')

# and 都真才真，一假即假
print((c < d) and (d < 100))
# or 一真即真
print((c > d) or (d < 100))
# not 取反
print(not (c < d))

'''
逻辑运算符书写习惯
在合适的地方加括号
增强代码可读性
'''

# and 一0即0,无0即末
print(1 and 2)
print(2 and 1)
print(1 and 0)

# or 全0为0，无0即首
print(0 or 0)
print(1 or 2)
print(2 or 1)
print(0 or 1)
