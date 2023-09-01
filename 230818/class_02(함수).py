# 01.
# x = int(input("입력: "))

lis = [1, 2, 3, 1, 4, 2, 1]
# temp = []

# def allindex (lis,x):  
#     for i in range(len(lis)):
#         if x == lis[i]:
#             temp.append(i)

#     print(temp)

# allindex (lis,x)

# 01-2. 입력X
def allindex (lis,a):  
    temp = []
    for i in range(len(lis)):  
        if lis[i] == a:
            temp.append(i)
    return temp

print(allindex(lis, 1))

print("---------------------------------------------------------")

# 02.
person1 = ["치킨", "피자", "족발", "삼겹살"]
person2 = ["김밥", "김치찌개", "삼겹살", "쌈밥"]
person3 = ["치킨", "김치찌개", "떡볶이", "초밥", "삼겹살", "족발", "햄버거", "보쌈", "한우", "아이스크림"]
                
res = any(food in person2 for
          food in person1)
common_food = [food for food in person1 if any(food == food2 for food2 in person2)]

print(res) # True
print(common_food) # ['삼겹살']

# lst = [food for food in common_food if food in person3]
# any 사용 : 
lst = [food for food in common_food if any(food==food3 for food3 in person3)]

print(lst) # ['삼겹살']