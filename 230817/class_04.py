list = []

lst = [1,2,3,4,5,6,7,8,9]

print(max(lst))
print(min(lst))
print(sum(lst))

maxNum = lst[0]
minNum = lst[0]
sumNum = 0

for i in lst:
    if maxNum < i :
        maxNum = i
    if minNum > i: 
        minNum = i
    sumNum += i
    
print("max :", maxNum, ", min: ", minNum, ", sum: ",sumNum)
    
print("01-------------------------------------------------")
    
#split
fruit = "apple,peer,corn,carrot"
fruit_list = fruit.split(",")
print(fruit_list)


#join
fruit = "-".join(fruit_list)
print(fruit)

print("02-------------------------------------------------")
fruit = "apple,peer,corn,carrot"

for i in fruit:
    if i == ',':
        print(end = " ")
    else :
        print(i, end = "")
print(fruit)

print("03-------------------------------------------------")        
        
fruit = "apple,peer,corn,carrot"
fruit_list = []
s = ''

for i in fruit:
    if i == ',':
        fruit_list.append(s)
        s = ''
    else :
        s += i
        
fruit_list.append(s)

print(fruit_list)

print("04-------------------------------------------------")

fruit = "apple+peer-corn,carrot"
fruit_list = []
s = 0

for i in range(len(fruit)):
    if fruit[i] == ','  or fruit[i] == '-' or fruit[i] == '+' :
        fruit_list.append(fruit[s:i])   
        s = i + 1
        
fruit_list.append(fruit[s:len(fruit)])

print(fruit_list)

print("05-------------------------------------------------")

#아스키코드
print(ord('Z')) #ordinal position
print(chr(97)) #character

fruit = "apple,./+peer-25-corn,carrot"
fruit_list = []
s = 0

for i in range(len(fruit)):
    if not((ord(fruit[i]) >= 65 and ord(fruit[i]) <= 90) or (ord(fruit[i]) >= 97 and ord(fruit[i]) <= 122 )): ##대문자 혹은 소문자가 아니라면 (특수기호나 다른 문자가 있다면)
        if fruit[s:i] != "": # s != i-1
            fruit_list.append(fruit[s:i])    
        s = i + 1
        
fruit_list.append(fruit[s:len(fruit)])

print(fruit_list)

print("06-------------------------------------------------")

fruit = "carrotapplecornpeer" #만약 구분자가 없다면, 단어 데이터 베이스
fruit_list = ['apple', 'peer', 'corn', 'carrot']
lst = []

s = ''

for i in fruit:
    s += i
    
    if s in fruit_list:
        lst.append(s)
        s = ''
        
if s in fruit_list:
    lst.append(s)
    
print(lst)
