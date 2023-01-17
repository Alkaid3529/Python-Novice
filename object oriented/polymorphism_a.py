# 多态
print('this is polymorphism')


class animal(object):
    def speak(self):
        print('the animal is speaking')


class cat(animal):
    def speak(self):
        print('the cat is speaking')

    def __del__(self):
        print('the cat is gone')


class dog(animal):
    def speak(self):
        print('the dog is speaking')

    def __del__(self):
        print('the dog is gone')


def speak(a: animal):
    a.speak()


speak(cat())
speak(dog())
