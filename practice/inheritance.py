class Mammal:
    def walk(self):
        print("walk")
    def run(self):
        print("run")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def meow(self):
        print("meow")

dog1 = Dog()
dog1.walk()
dog1.run()

cat1 =Cat()
cat1.meow()