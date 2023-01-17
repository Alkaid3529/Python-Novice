# 私有权限
print('this is private')


# 限制属性和方法，不继承给子类

class Father(object):
    def __init__(self, car, password='123445'):
        self.car = car
        # 设置私有属性，无法继承，类外无法访问
        self.__password = password

    def introduce(self):
        print(f'my car is {self.car}, my password is {self.__password}')

    # 无法继承，类外无法调用
    def __introduce(self):
        print(f'my car is {self.car}, my password is {self.__password}')

    # 修改私有属性值
    def set_password(self, password):
        self.__password = password

    # 获取私有属性值
    def get_password(self):
        return self.__password


class Son(Father):
    pass


f1 = Father('ba oma', '12345')
f1.introduce()
f1.set_password('3456')
print(f1.get_password())

s1 = Son('bench')
# s1.password
# s1.__password
s1.introduce()
s1.set_password('1234567')
print(s1.get_password())
