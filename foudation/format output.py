print("这里是格式化输出\n")

# 终于开始进入正门了
"""
常用的有三个：
%s string 字符型
%d decimal 整型
%f float 浮点型
"""

age = 19
name = 'Alkaid#3529'
weight = 52.5123456789
stu_id = 2052152

print('这是格式化输出的基本使用方法')

print("我今年", age, "岁了")
print("我的名字是", name)
print("我的体重为", weight)

print("我今年的年龄为%d岁" % age, "我的名字是%s" % name)
print('我的体重为%f' % weight)
print('我的体重为%.2f' % weight)
print('我的体重为%.10f' % weight)

print('\n这里是格式化输出的高级使用方法')

stu_ord = 1
print('我在班级里的排序为%02d' % stu_ord)
print('我在班级里的排序为%03d' % stu_ord)

stu_ord = 1000
print('我在班级里的排序为%d' % stu_ord)

print('我今年%d岁了，我的名字是%s' % (age, name))
print('我明年%d岁了，我的名字是%s，我的学号是%06d' % (age + 1, name, stu_ord))

print('\n这里是‘%s’的高级使用方法')
print('我明年%s岁了，我的名字是%s，我的学号是%s' % (age + 1, name, stu_ord))

print('\n这里是f格式化输出字符串的高级使用方法')
print(f'我明年{age + 1}岁了，我的名字是{name}，我的学号是{stu_id}')

print('\n这里是转义字符的使用方法')

'''
\n 表示换行
\t 制表符，一个tab键
'''

print('Hello\nworld')

print('abc\ta')

print('\n这里是print结束符的使用方法')
print('hello', end="\n")
print('python')
print('我们可以观察到默认换行')

print('hello', end="\t")
print('python')

print('hello', end=" wow ")
print('python')
