class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"hi, my name is {self.name} and i am talking")

    def learn(self):
        print(f"now {self.name} i am learning python ")

    def convey(self):
        print(f"tell {self.name} that haroon fayaz is learning pyhton ")


first = Person("haroon fayaz ")
first.talk()

sec = Person("wahdat")
sec.learn()

third = Person("hadi mir")
third.convey()
