class Dog:
    def __init__(self, name, color) :
        self.hungry = 0
        self.name = name
        self.color = color
    def eat(self) :
        self.hungry -= 10
        print("밥먹음", self.hungry)
    def walk(self):
        self.hungry += 10
        print("산책",self.hungry)
        

choco = Dog("choco", "black")
jjong = Dog("jjong", "white")

choco.eat()
choco.eat()
choco.walk()

print(choco.hungry)
print(jjong.hungry)






class Dog:
    def __init__(self, name, color) :
        self.hungry = 0
        self.name = name
        self.color = color
    def eat(self) :
        if self.hungry<=0:
            print("배가 너무 불러요!")
        else:
            self.hungry-=10
            print("밥먹음", self.hungry)
    def walk(self):
        self.hungry += 10
        print("산책",self.hungry)
    def condition(self):
        print("%s배고픔:%d",(self.name,self.hungry))
        

mery = Dog("mery", "black")

mery.eat()
mery.walk()
mery.walk()
mery.condition()

mery.hungry
        