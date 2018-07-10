class Animal(object):
    def run(self):
        print('Animal is run ...')
class Dog(Animal):
    def run(self):
        print('dog is run..')
class Cat(Animal):
    def run(self):
        print('cat is run..')
def runTwce(animal):
    animal.run()
    animal.run()
dog = Dog()
dog.run()
cat = Cat()
cat.run()
print()
runTwce(Animal())
runTwce(Dog())
runTwce(Cat())
