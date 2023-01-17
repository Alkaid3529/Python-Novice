# 类
print('this is class')


# 设置和访问类属性
class Dog(object):
    # 类属性，只有一份数据，全部实例化对象共享，只占用一分内存，实例属性则对每个对象单独开辟一份空间
    tooth = 10
    __age = 8

    # 装饰器
    @classmethod
    def get_age(cls):
        """
        方法多和私有类属性配合使用
        :return:
        """
        return cls.__age

    # 静态方法：无需实例化对象和类对象，取消参数传递，减少内存消耗
    @staticmethod
    def introduce():
        print('this is a dog')


wangcai = Dog()
xiaohei = Dog

print(wangcai.tooth)
print(Dog.tooth)
print(xiaohei.tooth)

print('')

# 修改类属性

# 仅能通过类进行修改
Dog.tooth = 20

print(wangcai.tooth)
print(Dog.tooth)
print(xiaohei.tooth)

print('')

# 若通过实例化对象进行修改，实则为创建一个同名的实例化对象属性，类属性不会改变
wangcai.tooth = 30

print(wangcai.tooth)
print(Dog.tooth)
print(xiaohei.tooth)

print('')

print(Dog.get_age())

print('')

# 静态方法调用
wangcai.introduce()
Dog.introduce()
