# 04. 5x2 2차원리스트 만들어서 1-10까지 채우기
lst = [
        [1,2],
        [3,4],
        [5,6],
        [7,8],
        [9,10]
       ]
a = 1

for i in range(len(lst)):
    for j in range(len(lst[0])):
        lst[i][j] = 2*i+j+1
        a += 1
        
for i in range(len(lst)):
    for j in range(len(lst[0])):
        print(lst[i][j], end = " ")
        
    print()
    
print("---------------------------------------------")
    
lst = []
num = 1

for i in range (2):
    temp = []
    for j in range(5):
        temp.append(num)
        num += 1
    print(temp)

print("---------------------------------------------")
# 03. list 함수 원리 구현 (숫자로)
# s = 123456 
# lst = list(s)
# print(lst)

s = 123456 
lst = []

while s > 0:
    lst.append(s%10) #s에 1의자리 숫자를 하나씩 채워넣는다
    s = s //10 #s를 10으로 나눈 몫을 넣어놓는다. #== s //= 10
    
lst.reverse() #다시 순서대로 하기위해 거꾸로   
print(lst)

print("---------------------------------------------")

lst = []
s = 123456 
num = 10
count= 0 #0부터 시작. (1을 넣으면 1부터 시작해서 값이 6이 나옴.)

while s > num:
    num *= 10
    count += 1
print(count) #5
print(s//10**count) #1

while s > 0:
    lst.append(s//10**count)
    s = s % 10**count #23456
    count -= 1 
print(lst) #[1, 2, 3, 4, 5, 6]