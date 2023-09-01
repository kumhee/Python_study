class Animal:
    def __init__(self) :
        self.hungry = 0
    def eat(self):
        self.hungry -= 10
        print("밥먹음", self.hungry)
    def walk(self):
        self.hungry += 10
        print("산책", self.hungry)
        

class Dog(Animal):
    def __init__(self):
        super().__init__()
    def sound(self):
        print("멍멍")
    def eat(self): #부모기능 물려받음 (eat)
        super().eat()
        print("왈왈")
        

class Cat(Animal):
    def __init__(self):
        super().__init__()
    def sound(self):
        print("야옹")



dog = Dog()
dog.sound() #멍멍
dog.walk() #산책10
dog.walk() #산책20 self.hungry += 10
dog.walk() #산책30 self.hungry += 10

dog.eat()

cat = Cat()
cat.sound()
cat.walk()