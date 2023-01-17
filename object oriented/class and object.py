# 类和对象
print('this is class and object')

print('encapsulation inherit polymorphism')


# 使用类创建一个对象
# 先有类，再有对象
class Person:
    """
    self: 调用该函数的对象 "this"
    """

    def __init__(self, name='None', age=18):
        """
        添加、获取对象属性
        :param name:
        :param age:
        """
        self.name = name
        self.age = age

    def __str__(self):
        """
        打印对象即可返回此返回值
        :return: 返回类的信息
        """
        return 'this is a person'

    def __del__(self):
        print(f'{self.name} is deleted')

    def introduce(self):
        print(f"hi, my name is {self.name}, I'm {self.age} years old")


p1 = Person('tom', 20)
p1.introduce()
print(p1)

p2 = Person()
p2.introduce()
