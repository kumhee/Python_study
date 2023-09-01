a = [i for i in range(10)]
# a에 list[i]를 넣겠다
# i가 뭔데?
# i는 for i in range(0) : 0....9
# a = [0...9]
print(a) 


a = [i+5 for i in range(10)] # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(a) 


a = [i*3 for i in range(10)] # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
print(a) 


a = [i for i in range(10) if i%2 == 0] # [0, 2, 4, 6, 8] 짝수만 출력
print(a) 

a = [i for i in range(10) if i%2 == 1] # [0, 2, 4, 6, 8] 홀수만 출력
print(a) 

print("---------------------------------------------------------")

a = [i*j for i in range(2, 10) for j in range(1, 10)]
# a = [i*j] a에 i*j를 넣겠다
# i = ?


# for i in range(2, 10) i는 2...9
# j = ?
# for j in range(1, 10) j는 1...9
print(a)

print("---------------------------------------------------------")

a = [0,0,0,0,0,0,0,0,0,0]

a = [0 for _ in range(10)] # i-i = 0
# a = [i for i in range(1) for j in range(0, 10)] 
# a = [i*0 for i in range(10)] 
print(a)

print("---------------------------------------------------------")

word = ["school", "game", "piano", "science", "hotel", "mountain"]

a = [i for i in word if len(i) >= 6]
# a = [word[i] for i in range (len(word)) if len(word[i]) >= 6]
print(a)

print("---------------------------------------------------------")

word = ["school", "game", "piano", "science", "hotel", "mountain"]
count = 0

a = [len(i) for i in word ]

print(a)


print("2차원리스트----------------------------------------------")
print("01. ")

a = [[10,20],[30,40],[50,60]]
b = [[2,3],[4,5],[6,7]]
lst = []

# 01.
for i in range(len(a)): # 012
    lst2 = []
    for j in range(len(a[i])): # 01    for j in range(2)):       
        lst2.append(a[i][j] * b[i][j]) 
    lst.append(lst2) 
    lst2 = []   
print(lst)

# 02.
for i in range(3): 
    temp = []
    for j in range(2):    
        temp.append(a[i][j] * b[i][j]) 
    lst.append(temp)
    temp = []
print(lst)
    
print("02. -----------------------------------------------------")

# 01.
a = []
for i in range(3):
    temp = []
    for j in range(2):
        # temp.append((i+j+1)+i)
        temp.append(i*2+j+1)
    a.append(temp)
print(a)  

# 01-2.
a = [[2*j+i+1 for i in range(2)] for j in range(3)]
print(a) 

print("---------------------------------------------------------")

# 02.
a = [[0 for _ in range(10)] for j in range(10)]
print(a)

print()

a = [[i+1 for i in range(10)] for j in range(10)] # -> i+1은 0부터10까지가 열개 출력됨.
print(a)

print()

a = [[j*10+i+1 for i in range(10)] for j in range(10)] # -> j*10+i+1 은 1부터100까지 출력됨.
print(a)

print("---------------------------------------------------------")

# 01.
prime_number = []

for i in range(2,101):
    for j in range(2,i):
        if i%j == 0:
            break
        elif i-1 == j:
            prime_number.append(i)
            
print(prime_number)



# 02.
prime_number = []

for i in range(2,101):
    isPrime = True
    
    for j in range(2,i):
        if i%j == 0:
            isPrime = False
            break
    if isPrime :
            prime_number.append(i)
            
print(prime_number)


print("all함수, any함수-----------------------------------------")

# all함수, any함수
# 여러 개의 조건 or 값이 있는 리스트, 튜플, set...값의 조건에 따라 True or False를 리턴하는 함수

# all함수 : 모든 값으 True
# any함수 : 하나라도 True면 True를 리턴한다. 

num = [i+1 for i in range(10)] # 1...10
lst = [x for x in num if x%2 == 0] # 짝수만

res = all(x%2 == 0 for x in num) # False
print(res)

res = all(x%2 == 0 for x in lst) # True
print(res)

# any
res = any(x == 5 for x in num) # False
print(res)

res = any(x == 5 for x in lst) # False
print(res)

print("03. -----------------------------------------------------")

# 03.
prime_number = [i for i in range(2, 101) if all(i%j != 0 for j in range(2, i))] #if i%j != 0 for j in range(2, i)  -> 이 부분을 묶는 방법

print(prime_number)