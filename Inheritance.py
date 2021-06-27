class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("Barking")


class Cat(Mammal):
    def Meow(self):
        print("Meow")


dog1 = Dog()
dog1.bark()

cat1 = Cat()
cat1.Meow()
