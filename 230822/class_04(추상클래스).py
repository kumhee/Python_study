from abc import*
from abc import ABC, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def eat(self):
        pass
    
class Dog(ABC, Animal): #다중상속
    @abstractmethod
    def walk(self):
        pass
    
    def eat(self):
        print("우걱우걱")
        
class Golden(Dog):
    def walk(self):
        print("터벅터벅")
    
golden = Golden()
golden.walk()
# 인터페이스는 왜 없어?
# 다중상속 가능 = 인터페이스 필요없음.