class Car:
    car_number = 0
    
    def __init__(self) :
        self._name = ""
        self._exhaust = 0
        self._production = 0
        Car.car_number  += 1
        
    def set_name(self, name):
        self._name = name
        
    def set_exhaust(self, exhaust):
        self._exhaust = exhaust
        
    def set_production(self, pro):
        self._production = pro
        
    def checkName(self):
        return self._name
    
    def size(self):
        if self._exhaust <= 1000:
            return "소형"
        elif self._exhaust >= 1000 and self._exhaust <= 2000:
            return "중형"
        elif self._exhaust >= 2000 :
            return "대형"
        else :
            return
        
    def get_production(self):
        return self._production
    
    @classmethod
    def carNumber(self):
        return Car.car_number
    
        
car = Car()
car.set_name("투싼")
car.set_exhaust(3000)
car.set_production(2020)

print("Car Name:", car.checkName())
print("Car Size:", car.size())
print("Car Production:", car.get_production())
print("Car Number:", Car.carNumber())

print()

car1 = Car()
car1.set_name("BMW")
car1.set_exhaust(2000)
car1.set_production(2022)

print("Car Name:", car1.checkName())
print("Car Size:", car1.size())
print("Car Production:", car1.get_production())
print("Car Number:", Car.carNumber())
