import time

# 异常
print('this is anomalous')

# 尝试执行可能发生错误的代码

try:
    f = open('test.txt', 'r')
except:
    f = open('test.txt', 'w')

# 捕获指定异常类型
# 异常类型：异常信息

# print(num) NameError
try:
    print(num)
except NameError:
    print('NameError')

try:
    print(1 / 0)
except ZeroDivisionError:
    print('ZeroDivisionError')

# 捕获多个制定异常
try:
    print(num)
except (NameError, ZeroDivisionError):
    print('NameError')

# 捕获指定异常描述信息
try:
    print(num)
except (NameError, ZeroDivisionError) as result:
    print(result)

try:
    print(1 / 0)
except (NameError, ZeroDivisionError) as result:
    print(result)

# 捕获所有异常
try:
    print(num)
except Exception as result:
    print(result)

try:
    print(1 / 0)
except Exception as result:
    print(result)

# 异常中的 else 表示没有异常时执行的代码
try:
    print(1 / 1)
except Exception as result:
    print(result)
else:
    print('this is normal')

# 异常中的 finally 表示无论是否发生异常都执行的代码
# 多用来关闭文件
try:
    f = open('test.txt', 'r')
except Exception as result:
    f = open('test.txt', 'w')
else:
    print('this is normal')
finally:
    f.close()

print('')

# 异常传递
# 异常嵌套书写
try:
    f = open('test.txt')
    try:
        while True:
            content_line = f.readline()
            if len(content_line) == 0:
                break
            time.sleep(1)
            print(content_line, end='')
    except:
        print('Unexpected outages')
    finally:
        f.close()
        print('\nThe file is closed')
except:
    print('The file does not exist')

print('')


# 自定义异常
# 将不符合程序逻辑的情况进行反馈
class Insufficient_length(Exception):
    def __init__(self, length, min_length):
        self.length = length
        self.min_length = min_length

    def __str__(self):
        if self.length < self.min_length:
            return f'Insufficient_length: The length you enter is {self.length}, cannot be less than {self.min_length}'
        else:
            return 'The length you enter is reasonable, the password is entered'


def main():
    try:
        password = input('Please enter a password:')
        print(Insufficient_length(len(password), 5))
    except Exception as result:
        print(result)

main()
