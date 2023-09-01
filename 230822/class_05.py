from abc import*
from abc import ABC, abstractmethod

class Food(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price
 
    @abstractmethod
    def cook(self):
        pass
    
class Pizza(Food): 
    def __init__(self, name = "피자", price = 10000, topping = "페퍼로니", crust = "올리브"):
        self._name = name
        self._price = price
        self._topping = topping
        self._crust = crust
    
    def cook(self):
        toppings = ',' .join(self._topping)
        return f"도미노에서 {self._name}가 나왔습니다. 가격은 {self._price}원, 토핑은 {toppings}이고, 크러스트는 {self._crust}입니다."
        
    def addTopping(self, topping):
        self._topping.append(topping)
        
    def addCrust(self, crust):
        self._crust = crust
        
    def pizzaPrice(self, price):
        self._price = price

    def toppingInfo(self):
        print()
        # print(self._topping)
        # for i in self._topping:
        #     print(i,end= " ")


        
class Hamburger(Food):
    @abstractmethod
    def cook(self):
        print("햄버거가 나왔습니다.")
        
        
        
        
class Pasta(Food):
    def cook(self):
        print("도미노에서 파스타가 나왔습니다.")
  
  
  
  
p = Pizza(name="피자",price=100,crust="치즈",topping=["페페로니", "올리브"])  
p.addTopping("포테이토")

print(p.cook())



# 숙제 :  topping, addTopping() -> 리스트, 값 여러개, 값 하나
