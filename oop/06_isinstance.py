class Animal(object):
    def run(self):
        print('Animal is run ...')
class Dog(Animal):
    def run(self):
        print('dog is run..')
class Cat(Animal):
    def run(self):
        print('cat is run..')
class Husky(Dog):
    pass
def runTwce(animal):
    animal.run()
    animal.run()
#对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
a=Animal()
b=Dog()
c=Cat()
h=Husky()
print(isinstance(h,Husky))
print(isinstance(h,Dog))
print(isinstance(h,Animal))
print(isinstance(h,Animal) and isinstance(h,Dog))
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))
