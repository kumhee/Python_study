s = {1,2,3}

s.add(3)

print(s)

print("01. --------------------------------------")

# 01. 사람 세 명이 각각 먹고싶은 음식이 여러개 있을 때, 어떤 메뉴를 시키는게 가장 좋을지(교집합)
a = ["apple", "banana", "orange"]
b = ["lemon", "grape", "peach", "banana"]
c = ["apple", "banana", "orange", "grape", "peach", "lime", "mango"]

menu1 = set(a)
menu2 = set(b)
menu3 = set(c)

print(menu1 & menu2 & menu3)

# 리스트 상태에서 공통음식 찾기 - 과제
# 01.
for i in a:
    for j in b:
        for k in c:
            if(i == j == k):
                print("공통된 과일: ", i)
                
# 02.
for i in a:
    if i in b and i in c:
        print("공통된 과일: ", i)


print("02. --------------------------------------")

# 02. 사람 세 명이 각각 음식을 여러개 가지고 있을 때, 두 명이 서로 음식을 교환.

while True:
    print(menu1)
    print(menu2)
    print(menu3)
    inputSet = int(input("1. 교환하기, 2. 종료하기"))
        
    if inputSet == 1:
        inputSet = print("누구와 교환하시겠습니까?    2.b   3.c")
        changeMenu = int(input())
        if changeMenu == 2:
            myFood = (input("어떤 음식과 교환하시겠습니까? "))
            youFood = (input("어떤 음식과 교환하시겠습니까? "))
            if myFood in menu2 or youFood in menu1:
                print('이미 가지고 있는 음식입니다. 교환할 수 없습니다.')
            elif myFood in menu1 and youFood in youFood:
                menu1.add(youFood)
                menu2.remove(myFood)
                menu1.remove(myFood)
                menu2.add(youFood)
            else :
                print('가지고 있는 음식이 아닙니다. 교환할 수 없습니다.')
        elif changeMenu == 3:
            myFood = (input("어떤 음식과 교환하시겠습니까? "))
            youFood = (input("어떤 음식과 교환하시겠습니까? "))
            if myFood in menu2 or youFood in menu1:
                print('이미 가지고 있는 음식입니다. 교환할 수 없습니다.')
            elif myFood in menu1 and youFood in youFood:
                menu1.add(youFood)
                menu2.remove(myFood)
                menu1.remove(myFood)
                menu2.add(youFood)
            else :
                print('가지고 있는 음식이 아닙니다. 교환할 수 없습니다.')
        else :
            print("잘못된 입력입니다. 다시 입력하세요.")
    elif inputSet == 2 :
        break
    else :
        print("잘못된 입력입니다. 다시 입력하세요.")
        
print(menu1)
print(menu2)
print(menu3)