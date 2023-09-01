class Animal:
    def __init__(self) :
        self._name = "백구"
        self._age = 3
        
    def set_name(self, name):
        self._name = name
    
    def set_age(self, age):
        self._age = age
    
    def sayHello(self):
        print ("멍멍:", animal._name , ",왈왈: ", animal._age)
        
    def ageCal(self):
        print("사람 나이로 환산하면 ", 24 + (animal._age-2)*4, "세 입니다.")
        
    def compareToAge(self, personAge):
        return 24 + (animal._age-2)*4 > personAge
    
    def printB (self, p):
        if 24 + (animal._age)*4 > p.get_age():
            print(animal._name,"의 나이가",p.get_name(),"의 나이보다 더 많습니다.")
        else :
            print(animal._name,"의 나이가",p.get_name(),"의 나이보다 더 적습니다.")
        


class Person: 
    def __init__(self) :
        self._name = "Kim"
        self._age = 20
        
    def set_name(self, name):
        
        self._name = name
    
    def set_age(self, age):
        self._age = age
        
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def sayHello(self):
        print ("Hello, my name is" , person._name , "and i'm" , person._age , "years old.")    
           
        
animal = Animal()
animal.sayHello()
animal.ageCal()
animal.compareToAge(24)

person = Person()
person.sayHello()

animal.printB(person)


print()
str = "jpgpgjgpjpgjgpjgpjgpjpgjpjgpjp"
count = 0

# 01-1.
# for i in range(len(str)-2):
#     if str[i] == 'j':
#         if str[i+1] == 'p':
#             if str[i+2] == 'g':
#                 count += 1
# print(count) #3

# 01-2
for i in range(len(str)-2):
    if str[i] == 'j' and str[i+1] == 'p' and str[i+2] == 'g':
        count += 1
print(count) #3

# 01-3
lst = []

for i in range(len(str)-2):
    if str[i] == 'j' and str[i+1] == 'p' and str[i+2] == 'g':
        lst.append(str[i:i+3])
print(count) #3

# 01-4
for i in range(len(str)-2):
    if str[i] + str[i+1] + str[i+2] == 'jpg':
        lst.append(str[i:i+3])
print(count) #3


print()
print("gpjgpj")

str = "jpgpgjgpjpgjgpjgpjgpjpgjpjgp"
# 01-5 몇개의 gpjgpj가 있는지 gpjgpjgpj - 1개 (겹치는 것 불가)
    
i = 0
count = 0
while i < len(str)-5:
    temp = ""
    for j in range(6):
        temp += str[i+j]
    # if str[i] + str[i+1] + str[i+2]...:
    if temp == "gpjgpj":
        count += 1
        i += 5
    i+=1

print(count)



# 01-6
count = 0
while len(str) >= 6:
    temp = ""
    for j in range(6):
        temp += str[j]
        
    if temp == "gpjgpj":
        count += 1
        str = str[6:]
       
    str = str[1:]

print(count)

# 람다식
str = "jpgpgjgpjpgjgpjgpjgpjpgjpjgp"
# 01
res = list(filter(lambda x: x[0]=="j", [str[i:i+3] for i in range(len(str) -2)]))
print(res)

# 02
result = list(filter(lambda y:y=="jpg", res))
print(result)

#위 두 개를 합친:
print(list(filter(lambda y:y=="jpg", list(filter(lambda x: x[0]=="j", [str[i:i+3] for i in range(len(str) -2)])))))