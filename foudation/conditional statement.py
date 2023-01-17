# 导入模块
import random

print('这里是条件语句')

a = 10
b = 20

if a > 5:
    b = b - a
    b += 5
print(f'b = {b}')

print('系统启动')

# input接收到的数据默认为str，需要转换类型为需要读入的数据
age = int(input('您的年龄为：'))

if age >= 18:
    if age > 60:
        print('您年龄过大，不可以上网')
    else:
        print('您可以上网')
elif age <= 14:
    print('您年龄过小，不可以上网')
else:
    print('请耐心等待，好好学习，不许上网')

print('系统关闭')

age = int(input('您的年龄为：'))

if age < 18:
    print('小朋友属于童工，雇佣童工是违法的')
elif 18 <= age <= 60:
    print('您正值壮年，祝您工作顺利')
elif age > 60:
    print('老年人属于退休人群，请老人注意身体')

num = random.randint(0, 100)
print(f'随机数生成：num = {num}')

# 三目运算符
'''
语法如下：
条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
'''

print('随机生成的数字小于50') if num < 50 else print('随机生成的数字不小于50')
