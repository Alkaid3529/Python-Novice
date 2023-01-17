print('这里是循环')

print('首先是while循环')

a = 0
while a < 5:
    print(f'第{a + 1}次好好学习python')
    a += 1

print('坚持努力')

print('1...100的和为：')
summation = 0
num = 1
while num < 101:
    summation += num
    num += 1
print(summation)


print('1...100的偶数和为：')
summation = 0
num = 1
while num < 101:
    if num % 2 == 0:
        summation += num
        num += 1
    else:
        num += 1
print(summation)


print('1...100的偶数和为：')
summation = 0
num = 0
while num < 101:
    summation += num
    num += 2
print(summation)

print('1...100的奇数和为：')
summation = 0
num = 1
while num < 101:
    summation += num
    num += 2
print(summation)

print('学习开始')
num1 = 0
while num1 < 3:
    print(f'第{num1 + 1}天好好学习')
    num2 = 0
    while num2 < 2:
        print(f'第{num2 + 1}次好好学python')
        num2 += 1
    num1 += 1
print('学习完成')

print('输出 * 正方形')
num1 = 0
while num1 < 5:
    num2 = 0
    while num2 < 5:
        print('*', end='')
        num2 += 1
    print('')
    num1 += 1


print('输出九九乘法表')
num1 = 1
while num1 < 10:
    num2 = 1
    while num2 < num1 + 1:
        if num1 * num2 < 10:
            print(f'{num2} * {num1} = {num1 * num2}    ', end='')
        else:
            print(f'{num2} * {num1} = {num1 * num2}   ', end='')
        num2 += 1
    print('')
    num1 += 1


print('然后是for循环')

'''
for 临时变量 in 序列:
    ...
    ...
'''

for i in 'Alkaid':
    print(i, end='')

print('')

for i in 'Alkaid':
    if i == 'a':
        continue
    print(i, end='')

print('')

for i in 'Alkaid':
    if i == 'i':
        break
    print(i, end='')

print('')

num1 = 0
while num1 < 3:
    print('好好学习python')
    num1 += 1
else:
    print('坚持努力')

print('')

num1 = 0
while num1 < 3:
    print('好好学习python')
    num1 += 1
print('坚持努力')

print('')

# while or for else 配合 break 或者 continue 是很好的逻辑搭配

num1 = 0
while num1 < 3:
    print('好好学习python')
    num1 += 1
    break
else:
    print('坚持努力')

print('')

num1 = 0
while num1 < 3:
    print('好好学习python')
    num1 += 1
    continue
else:
    print('坚持努力')

print('')

for i in 'Alkaid':
    print(i, end='')
else:
    print('#3529')

print('')

for i in 'Alkaid':
    if i == 'a':
        break
    print(i, end='')
else:
    print('#3529')
