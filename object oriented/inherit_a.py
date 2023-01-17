# 继承
print('this is inherit, and it will be a little difficult')

print('first inherit definition')


# 类的两种执行方式
# 经典类 新式类
# 默认新式类

# 只有 object 是顶级类或基类，其余均为派生类

# 父类
class Person_Father(object):
    def __init__(self, name='none', age=18):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"hi, my name is {self.name}, I'm {self.age} years old")


class Person_Mother(object):
    def __init__(self, hobby='basketball', nature='outgoing'):
        self.hobby = hobby
        self.nature = nature

    def introduce(self):
        print(f'I like {self.hobby}, and I am {self.nature}')


#  子类
class Person_Son(Person_Father, Person_Mother):
    def __init__(self, hobby='chess', nature='outgoing'):
        super().__init__(hobby, nature)

        # 子类重写父类同名属性和方法
        self.hobby = hobby
        self.nature = nature

    def introduce(self):
        self.__init__()
        print(f"hi, my name is {self.name}, I'm {self.age} years old")
        print(f'I like {self.hobby}, and I am {self.nature}')

    def father_introduce(self):
        # 必须提前初始化父类，才能调用父类成员
        Person_Father.__init__(self)
        Person_Father.introduce(self)

    def mother_introduce(self):
        Person_Mother.__init__(self)
        Person_Mother.introduce(self)


s1 = Person_Son()

# 若父类有同名成员属性或者方法，调用时优先使用前者的成员属性与方法
s1.introduce()
s1.father_introduce()
s1.mother_introduce()

# 子类重写父类同名成员后，优先调用子类成员
print(s1.hobby)

# 查看继承的关系
print(Person_Son.mro())

print('')


# 多层继承
class Person_Grandson(Person_Son):

    def elders_introduce(self):
        """
        一次性调用多重复类的同名成员
        :return:
        """
        Person_Son.__init__(self)
        Person_Son.introduce(self)

        Person_Mother.__init__(self)
        Person_Mother.introduce(self)

        Person_Father.__init__(self)
        Person_Father.introduce(self)

        print('')

        #     使用 super() 调用父类中的同名方法
        super(Person_Grandson, self).__init__()
        super(Person_Grandson, self).introduce()


gs = Person_Grandson()
gs.introduce()
gs.father_introduce()
gs.mother_introduce()

print('')

gs.elders_introduce()
